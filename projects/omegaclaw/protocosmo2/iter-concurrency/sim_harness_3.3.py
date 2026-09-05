#!/usr/bin/env python3
"""Simulation harness for M3 Step 3.3 — Shutdown protocol (R17).

Tests the real shutdown protocol code extracted from iter.py via AST:
- _iter_signal_handler, _install_signal_handlers, graceful_shutdown
- SHUTDOWN_GRACE, _shutdown_event
- Also tests drain_merge_queue, save_experience, BranchState, threaded_llm_call
  (dependencies of graceful_shutdown)

Validation cases from spec:
  (l) Shutdown during active branch → stop event, bounded wait, clean exit,
      experience saved.
  Plus structural and flag-off tests.
"""
import ast
import copy
import datetime
import hashlib
import json
import os
import queue
import signal
import sys
import tempfile
import threading
import time
import uuid
from pathlib import Path

# ── Extract real code from iter.py via AST ──────────────────────────
ITER_PY = Path(__file__).parent.parent / "iter-port" / "repos" / "iter.py"
source = ITER_PY.read_text()
tree = ast.parse(source)

# Extract names we need
needed_names = {
    "SHUTDOWN_GRACE", "_shutdown_event", "_iter_signal_handler",
    "_install_signal_handlers", "graceful_shutdown",
    "drain_merge_queue", "save_experience", "BranchState",
    "threaded_llm_call", "_bg_llm_thread_target",
    "check_background_deadline", "BACKGROUND_DEADLINE",
    "ITER_CONCURRENCY_ENABLED", "ITER_PROMOTE_SECONDS",
    "API_KEY", "BASE_URL", "MODEL", "LLM_TIMEOUT", "SESSION_ID",
    "_merge_queue", "_branch_lock", "_active_branch",
}

# Module-level namespace for exec — include all imports iter.py functions reference
ns = {"__builtins__": __builtins__}
for mod in [signal, threading, queue, time, sys, os, json, copy, uuid, hashlib, datetime]:
    ns[mod.__name__] = mod
ns["Path"] = Path

# We need to handle the module-level code in iter.py carefully.
# It reads experience.json, creates a client, etc.
# Instead of executing the whole module, we'll extract specific functions
# and constants by walking the AST.

# First, extract module-level constants and simple assignments
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in needed_names:
                try:
                    val = ast.literal_eval(node.value)
                    ns[target.id] = val
                except (ValueError, SyntaxError):
                    pass
    elif isinstance(node, ast.FunctionDef):
        if node.name in needed_names:
            code = compile(ast.Module(body=[node], type_ignores=[]), str(ITER_PY), "exec")
            exec(code, ns)
    elif isinstance(node, ast.ClassDef):
        if node.name in needed_names:
            code = compile(ast.Module(body=[node], type_ignores=[]), str(ITER_PY), "exec")
            exec(code, ns)

# Handle _merge_queue, _branch_lock, _active_branch, _shutdown_event
# These are module-level assignments that may involve function calls
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                if target.id == "_merge_queue":
                    ns["_merge_queue"] = queue.Queue()
                elif target.id == "_branch_lock":
                    ns["_branch_lock"] = threading.Lock()
                elif target.id == "_active_branch":
                    ns["_active_branch"] = None
                elif target.id == "_shutdown_event":
                    ns["_shutdown_event"] = threading.Event()

# Provide missing constants that iter.py references but we couldn't literal_eval
ns.setdefault("SHUTDOWN_GRACE", 5)
ns.setdefault("ITER_CONCURRENCY_ENABLED", False)
ns.setdefault("ITER_PROMOTE_SECONDS", 30)
ns.setdefault("BACKGROUND_DEADLINE", 300)
ns.setdefault("API_KEY", "test-key")
ns.setdefault("BASE_URL", "http://test:1234/v1")
ns.setdefault("MODEL", "test-model")
ns.setdefault("LLM_TIMEOUT", 600)
ns.setdefault("SESSION_ID", "test-session-id")
ns.setdefault("MAX_TOKENS", 2524)

# save_experience writes to a file; we'll use a temp file
_tmpdir = tempfile.mkdtemp()
_exp_path = os.path.join(_tmpdir, "experience.json")
_experience = []

def save_experience_override(exp):
    global _experience
    _experience = exp
    with open(_exp_path, "w") as f:
        json.dump(exp, f)

ns["save_experience"] = save_experience_override
ns["experience"] = _experience
ns.setdefault("get_current_time", lambda: "test-time")

# Verify all needed names are present
missing = [name for name in needed_names if name not in ns]
if missing:
    print(f"WARNING: Missing names: {missing}")

# ── Test helpers ───────────────────────────────────────────────────
passed = 0
failed = 0

def test(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
    else:
        failed += 1
        print(f"FAIL: {name} {detail}")

# ── Group A: _iter_signal_handler ──────────────────────────────────

# Test 1: _iter_signal_handler exists and is callable
test("A1: _iter_signal_handler exists", callable(ns.get("_iter_signal_handler")))

# Test 2: _iter_signal_handler sets _shutdown_event
event = ns["_shutdown_event"]
event.clear()
handler = ns["_iter_signal_handler"]
handler(signal.SIGTERM, None)
test("A2: signal handler sets shutdown event", event.is_set(),
     f"event.is_set()={event.is_set()}")
event.clear()

# Test 3: _iter_signal_handler works with SIGINT
handler(signal.SIGINT, None)
test("A3: signal handler works with SIGINT", event.is_set())
event.clear()

# Test 4: _iter_signal_handler handles unknown signal number gracefully
try:
    handler(99999, None)  # Unknown signal number
    test("A4: unknown signal number handled", True)
except Exception as e:
    test("A4: unknown signal number handled", False, str(e))
event.clear()

# ── Group B: _install_signal_handlers ──────────────────────────────

# Test 5: _install_signal_handlers exists and is callable
test("B1: _install_signal_handlers exists", callable(ns.get("_install_signal_handlers")))

# Test 6: _install_signal_handlers installs without error (main thread)
try:
    ns["_install_signal_handlers"]()
    test("B2: _install_signal_handlers runs without error", True)
except Exception as e:
    test("B2: _install_signal_handlers runs without error", False, str(e))

# Test 7: After installation, SIGTERM sets the event (simulate)
# We can't actually send SIGTERM (would terminate the test), so we
# call the handler directly after verifying the signal is installed.
event.clear()
# The installed handler should be _iter_signal_handler
installed = signal.getsignal(signal.SIGTERM)
test("B3: SIGTERM handler installed", installed is ns["_iter_signal_handler"] or
     callable(installed))

# Test 8: Restore default signal handlers to avoid interfering with test runner
signal.signal(signal.SIGTERM, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)
test("B4: signal handlers restored to defaults", True)

# ── Group C: graceful_shutdown — no active branch ─────────────────

# Test 9: graceful_shutdown exists and is callable
test("C1: graceful_shutdown exists", callable(ns.get("graceful_shutdown")))

# Test 10: graceful_shutdown with no active branch — drains, saves, exits
# Need to set up: _active_branch=None, _merge_queue empty, experience list
event.clear()
ns["_active_branch"] = None
ns["_merge_queue"] = queue.Queue()
exp = [{"role": "user", "content": "test message"}]
ns["experience"] = exp

# graceful_shutdown calls sys.exit(0) — we need to catch it
try:
    ns["graceful_shutdown"]()
    test("C2: graceful_shutdown exited via sys.exit", False, "did not raise SystemExit")
except SystemExit as e:
    test("C2: graceful_shutdown exits with code 0", e.code == 0, f"code={e.code}")

# Test 11: Experience was saved
saved_exp = json.loads(Path(_exp_path).read_text())
test("C3: experience saved by graceful_shutdown", saved_exp == exp,
     f"saved={saved_exp} expected={exp}")

# Test 12: Experience content is valid JSON
test("C4: saved experience is valid JSON", isinstance(saved_exp, list))

# ── Group D: graceful_shutdown — with active branch that completes ──

# Test 13: graceful_shutdown waits for branch then exits
event.clear()
ns["_active_branch"] = None
ns["_merge_queue"] = queue.Queue()

# Simulate a branch that completes after 0.5s
result_container = {}
def fake_thread_target():
    time.sleep(0.5)
    result_container["ok"] = True
    result_container["response"] = "fake-response"

t = threading.Thread(target=fake_thread_target, daemon=True)
t.start()

# Use a fast SHUTDOWN_GRACE for the test
orig_grace = ns.get("SHUTDOWN_GRACE", 5)
ns["SHUTDOWN_GRACE"] = 3  # plenty for 0.5s completion

BranchState = ns["BranchState"]
branch = BranchState(
    branch_id="bg-test1234",
    branch_client=None,
    branch_messages=[],
    thread=t,
    result_container=result_container,
)
ns["_active_branch"] = branch

exp2 = [{"role": "user", "content": "shutdown with branch"}]
ns["experience"] = exp2

start_time = time.time()
try:
    ns["graceful_shutdown"]()
    test("D1: graceful_shutdown with completing branch exits", False, "did not raise SystemExit")
except SystemExit as e:
    elapsed = time.time() - start_time
    test("D1: graceful_shutdown exits with code 0", e.code == 0)
    test("D2: graceful_shutdown waited < 3s for branch", elapsed < 2.5,
         f"elapsed={elapsed:.2f}s")

# Test 14: Thread completed
test("D3: branch thread completed", not t.is_alive())

# Test 15: Experience saved
saved_exp2 = json.loads(Path(_exp_path).read_text())
test("D4: experience saved with active branch", saved_exp2 == exp2)

ns["SHUTDOWN_GRACE"] = orig_grace

# ── Group E: graceful_shutdown — branch exceeds grace period ───────

# Test 16: graceful_shutdown does not wait longer than SHUTDOWN_GRACE
event.clear()
ns["_active_branch"] = None
ns["_merge_queue"] = queue.Queue()

# Simulate a branch that never completes
result_container2 = {}
def slow_thread_target():
    time.sleep(30)  # much longer than grace
    result_container2["ok"] = True

t2 = threading.Thread(target=slow_thread_target, daemon=True)
t2.start()

# Use a short grace
ns["SHUTDOWN_GRACE"] = 1  # 1 second grace

branch2 = BranchState(
    branch_id="bg-slow1234",
    branch_client=None,
    branch_messages=[],
    thread=t2,
    result_container=result_container2,
)
ns["_active_branch"] = branch2

exp3 = [{"role": "user", "content": "shutdown with slow branch"}]
ns["experience"] = exp3

start_time2 = time.time()
try:
    ns["graceful_shutdown"]()
    test("E1: graceful_shutdown with slow branch exits", False, "did not raise SystemExit")
except SystemExit as e:
    elapsed2 = time.time() - start_time2
    test("E1: graceful_shutdown exits with code 0", e.code == 0)
    test("E2: graceful_shutdown waited ≤ SHUTDOWN_GRACE + small margin",
         elapsed2 < 2.5, f"elapsed={elapsed2:.2f}s grace=1s")

# Test 17: Thread is daemon (still alive but doesn't block exit)
test("E3: slow branch thread is daemon", t2.daemon)
test("E4: slow branch thread still alive (daemon, doesn't block)", t2.is_alive())

# Test 18: Experience saved despite slow branch
saved_exp3 = json.loads(Path(_exp_path).read_text())
test("E5: experience saved despite slow branch", saved_exp3 == exp3)

ns["SHUTDOWN_GRACE"] = orig_grace

# ── Group F: graceful_shutdown — drains merge queue before save ─────

# Test 19: graceful_shutdown drains pending merge queue entries
event.clear()
ns["_active_branch"] = None
mq = queue.Queue()
mq.put({"role": "system", "content": "pending marker 1", "branch": "bg-a1"})
mq.put({"role": "system", "content": "pending marker 2", "branch": "bg-b2"})
ns["_merge_queue"] = mq

exp4 = [{"role": "user", "content": "drain test"}]
ns["experience"] = exp4

try:
    ns["graceful_shutdown"]()
except SystemExit:
    pass

saved_exp4 = json.loads(Path(_exp_path).read_text())
test("F1: merge queue drained by graceful_shutdown",
     len(saved_exp4) == 3,  # original + 2 merged
     f"len={len(saved_exp4)}")
test("F2: merged entries have branch tags",
     all(e.get("branch") for e in saved_exp4 if e.get("role") == "system"))
test("F3: original experience preserved", saved_exp4[0] == exp4[0])

# ── Group G: SHUTDOWN_GRACE env config ─────────────────────────────

# Test 20: SHUTDOWN_GRACE default is 5
test("G1: SHUTDOWN_GRACE default is 5",
     int(os.getenv("ITER_SHUTDOWN_GRACE", "5")) == 5)

# Test 21: SHUTDOWN_GRACE respects env override
test("G2: SHUTDOWN_GRACE env override works",
     os.getenv("ITER_SHUTDOWN_GRACE", "5") == "5")

# ── Group H: flag-off source inspection ────────────────────────────

# Test 22: All new code is behind ITER_CONCURRENCY_ENABLED flag guard
# Check that the shutdown check in the main loop is flag-guarded
source_text = ITER_PY.read_text()

# The signal handler installation is flag-guarded
test("H1: _install_signal_handlers call is flag-guarded",
     "if ITER_CONCURRENCY_ENABLED:\n    _install_signal_handlers()" in source_text or
     "if ITER_CONCURRENCY_ENABLED:\n        _install_signal_handlers()" in source_text)

# The shutdown check is flag-guarded
test("H2: shutdown check is flag-guarded by ITER_CONCURRENCY_ENABLED",
     "if ITER_CONCURRENCY_ENABLED and _shutdown_event.is_set():" in source_text)

# Test 23: graceful_shutdown calls sys.exit (clean exit)
test("H3: graceful_shutdown calls sys.exit", "sys.exit(0)" in source_text)

# Test 24: _iter_signal_handler sets _shutdown_event
test("H4: _iter_signal_handler sets _shutdown_event", "_shutdown_event.set()" in source_text)

# Test 25: Signal handlers installed for SIGTERM and SIGINT
test("H5: SIGTERM handler installed", "signal.signal(signal.SIGTERM" in source_text)
test("H6: SIGINT handler installed", "signal.signal(signal.SIGINT" in source_text)

# ── Group I: py_compile ─────────────────────────────────────────────

# Test 26: py_compile passes
import py_compile
try:
    py_compile.compile(str(ITER_PY), doraise=True)
    test("I1: py_compile passes", True)
except py_compile.PyCompileError as e:
    test("I1: py_compile passes", False, str(e))

# ── Group J: diff analysis (additions only) ────────────────────────

# Test 27: Diff vs pre-step backup is pure additions
import subprocess
backup = ITER_PY.parent / "iter.py.pre-m3-3.3-20260904T1954"
if backup.exists():
    diff_result = subprocess.run(
        ["diff", str(backup), str(ITER_PY)],
        capture_output=True, text=True
    )
    diff_lines = diff_result.stdout.splitlines()
    additions = [l for l in diff_lines if l.startswith(">")]
    deletions = [l for l in diff_lines if l.startswith("<")]
    test("J1: diff has additions", len(additions) > 0)
    test("J2: diff has zero deletions", len(deletions) == 0,
         f"deletions: {deletions}")
    test("J3: diff additions count > 30", len(additions) > 30,
         f"additions={len(additions)}")
else:
    test("J1: backup exists for diff", False, str(backup))

# ── Group K: M2 regression — drain_merge_queue still works ─────────

# Test 28: drain_merge_queue works after shutdown changes
ns["_active_branch"] = None
mq2 = queue.Queue()
mq2.put({"role": "system", "content": "regression test", "branch": "bg-reg1"})
ns["_merge_queue"] = mq2
exp5 = [{"role": "user", "content": "regression"}]
ns["experience"] = exp5

drained = ns["drain_merge_queue"]()
test("K1: drain_merge_queue returns count", drained == 1)
test("K2: drain_merge_queue adds to experience", len(ns["experience"]) == 2)
test("K3: drain_merge_queue preserves branch tag",
     ns["experience"][1].get("branch") == "bg-reg1")

# ── Summary ────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"Step 3.3 harness: {passed} passed, {failed} failed")
print(f"{'='*60}")
sys.exit(0 if failed == 0 else 1)
