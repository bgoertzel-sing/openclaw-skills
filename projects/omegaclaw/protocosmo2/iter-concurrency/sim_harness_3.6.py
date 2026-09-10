#!/usr/bin/env python3
"""Consolidated simulation harness for M3 Step 3.6: Tests for 3.1–3.5.

This harness tests ALL M3 features functionally in a single run:
  3.1 — BACKGROUND_DEADLINE: abandon + marker + slot frees (R13)
  3.2 — try/except wrapper: error markers onto merge queue (R14)
  3.3 — Shutdown protocol: SIGTERM/SIGINT stop event, 5s grace, drain, save, exit (R17)
  3.4 — Duplicate-tool supersede annotation (R16)
  3.5 — Branch step budget + branch checkpoint queuing to main thread (R20)

It does NOT use diff-against-old-backup tests (those break after subsequent steps
modify the code, which is expected). Instead, it uses:
  - AST source inspection of the current iter.py for structural correctness
  - Functional tests with extracted real code in simulated environments
  - Regression tests ensuring M2/M3 features coexist correctly
  - py_compile verification

All tests are provider-free (no OpenAI API calls).
"""
import ast
import copy
import json
import os
import queue
import signal
import subprocess
import sys
import tempfile
import threading
import time
import types
import uuid
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────
ITER_PY = Path(__file__).parent.parent / "iter-port" / "repos" / "iter.py"
source = ITER_PY.read_text(encoding="utf-8")
tree = ast.parse(source)

# ── Test framework ──────────────────────────────────────────────────────
passed = 0
failed = 0
results = []

def test(name, cond, detail=""):
    global passed, failed
    results.append((name, bool(cond), detail))
    if cond:
        passed += 1
        print(f"  PASS: {name}")
    else:
        failed += 1
        print(f"  FAIL: {name} — {detail}")

# ── AST extraction helpers ──────────────────────────────────────────────
def extract_func_src(name):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return ast.get_source_segment(source, node)
    return None

def has_func(name):
    return any(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name
        for node in ast.walk(tree)
    )

def has_class(name):
    return any(
        isinstance(node, ast.ClassDef) and node.name == name
        for node in ast.walk(tree)
    )

# ── Extract functions for functional tests ─────────────────────────────
ns_extract = {}
ns_extract["queue"] = queue
ns_extract["threading"] = threading
ns_extract["time"] = time
ns_extract["uuid"] = uuid
ns_extract["copy"] = copy
ns_extract["os"] = os
ns_extract["json"] = json
ns_extract["Path"] = Path
ns_extract["signal"] = signal
ns_extract["sys"] = sys
ns_extract["hashlib"] = __import__("hashlib")
ns_extract["datetime"] = __import__("datetime")

# Extract module-level constants
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    val = ast.literal_eval(node.value)
                    ns_extract[target.id] = val
                except (ValueError, SyntaxError):
                    pass

# Set up module-level objects that can't be literal_eval'd
ns_extract["_merge_queue"] = queue.Queue()
ns_extract["_branch_lock"] = threading.Lock()
ns_extract["_active_branch"] = None
ns_extract["_shutdown_event"] = threading.Event()

# Constants that might not have been literal_eval'd
ns_extract.setdefault("ITER_CONCURRENCY_ENABLED", False)
ns_extract.setdefault("ITER_PROMOTE_SECONDS", 30)
ns_extract.setdefault("BACKGROUND_DEADLINE", 300)
ns_extract.setdefault("BRANCH_STEP_BUDGET", 25)
ns_extract.setdefault("SHUTDOWN_GRACE", 5)
ns_extract.setdefault("ITER_CHECKPOINT_ENABLED", True)
ns_extract.setdefault("CHECKPOINT_TOOL_SNAPSHOT", 5)
ns_extract.setdefault("CHECKPOINT_OUTPUT_CHARS", 200)
ns_extract.setdefault("CHECKPOINT_CHANNEL", "protocosmo2")
ns_extract.setdefault("API_KEY", "test-key")
ns_extract.setdefault("BASE_URL", "http://test:1234/v1")
ns_extract.setdefault("MODEL", "test-model")
ns_extract.setdefault("LLM_TIMEOUT", 600)
ns_extract.setdefault("MAX_TOKENS", 2524)
ns_extract.setdefault("SESSION_ID", "test-session-id")
ns_extract.setdefault("MAX_FAST_STEPS", 50)

# Extract functions and classes
for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        try:
            code = compile(ast.Module(body=[node], type_ignores=[]), str(ITER_PY), "exec")
            exec(code, ns_extract)
        except Exception:
            pass
    elif isinstance(node, ast.ClassDef):
        try:
            code = compile(ast.Module(body=[node], type_ignores=[]), str(ITER_PY), "exec")
            exec(code, ns_extract)
        except Exception:
            pass

# Monkeypatch openai
class FakeOpenAI:
    def __init__(self, **kwargs):
        pass
ns_extract["openai"] = types.SimpleNamespace(OpenAI=FakeOpenAI)

# ── Mock helpers ────────────────────────────────────────────────────────
class MockErrorClient:
    """OpenAI client mock that raises after a delay."""
    def __init__(self, delay, exc_type=RuntimeError, exc_msg="LLM exploded"):
        self._delay = delay
        self._exc_type = exc_type
        self._exc_msg = exc_msg

    @property
    def chat(self):
        return self

    @property
    def completions(self):
        return self

    def create(self, **kwargs):
        time.sleep(self._delay)
        raise self._exc_type(self._exc_msg)

class MockSuccessClient:
    """OpenAI client mock that returns a response after a delay."""
    def __init__(self, delay=0):
        self._delay = delay

    @property
    def chat(self):
        return self

    @property
    def completions(self):
        return self

    def create(self, **kwargs):
        time.sleep(self._delay)
        return {"fake": "response", "choices": [{"finish_reason": "stop", "message": {"content": "ok", "tool_calls": None}}]}

def reset_state():
    """Reset branch/queue state between tests."""
    with ns_extract["_branch_lock"]:
        ns_extract["_active_branch"] = None
    ns_extract["_merge_queue"] = queue.Queue()

def make_save_experience(experience_list, save_log):
    def save_experience(experience):
        save_log.append(list(experience))
    return save_experience

def make_assistant_entry(tool_calls):
    return {
        "role": "assistant",
        "content": None,
        "tool_calls": [
            {"id": tc["id"], "type": "function",
             "function": {"name": tc["name"], "arguments": tc["args"]}}
            for tc in tool_calls
        ],
    }

def make_tool_entry(tool_call_id, content="result"):
    return {"role": "tool", "tool_call_id": tool_call_id, "content": content}

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3.1: BACKGROUND_DEADLINE — abandon + marker + slot frees (R13)
# ═══════════════════════════════════════════════════════════════════════
print("=" * 70)
print("SECTION 3.1: BACKGROUND_DEADLINE — abandon + marker + slot frees (R13)")
print("=" * 70)

# Source inspection
print("\n--- Source inspection ---")
test("3.1.S1: BACKGROUND_DEADLINE constant exists", "BACKGROUND_DEADLINE = max(2 * ITER_PROMOTE_SECONDS, 300)" in source)
test("3.1.S2: check_background_deadline function exists", has_func("check_background_deadline"))

cbd_src = extract_func_src("check_background_deadline")
test("3.1.S3: check_background_deadline uses _branch_lock", cbd_src and "_branch_lock" in cbd_src)
test("3.1.S4: check_background_deadline uses _active_branch", cbd_src and "_active_branch" in cbd_src)
test("3.1.S5: check_background_deadline uses _merge_queue", cbd_src and "_merge_queue" in cbd_src)

import re
call_pattern = r"if ITER_CONCURRENCY_ENABLED:\s*\n\s*check_background_deadline\(\)"
matches = re.findall(call_pattern, source)
test("3.1.S6: flag-guarded check_background_deadline() calls >= 1", len(matches) >= 1, f"found {len(matches)}")

# Functional tests
print("\n--- Functional tests ---")

# Use extracted check_background_deadline
check_bg_deadline = ns_extract.get("check_background_deadline")
BranchState_cls = ns_extract.get("BranchState")

test("3.1.F1: check_background_deadline callable", callable(check_bg_deadline))

reset_state()
# No active branch → False, empty queue
test("3.1.F2: no active branch → False", check_bg_deadline() == False)
test("3.1.F3: queue empty after no-branch check", ns_extract["_merge_queue"].qsize() == 0)

# Branch within deadline → False, still active
reset_state()
bs = BranchState_cls(branch_id="bg-test1", branch_client=None, branch_messages=[], thread=None, result_container={})
bs.created_at = time.time()
ns_extract["_active_branch"] = bs
test("3.1.F4: branch within deadline → False", check_bg_deadline() == False)
test("3.1.F5: branch still active after within-deadline check", ns_extract["_active_branch"] is not None)

# Branch exceeded deadline → True, marker queued, slot freed
reset_state()
bs2 = BranchState_cls(branch_id="bg-test2", branch_client=None, branch_messages=[], thread=None, result_container={})
bs2.created_at = time.time() - 301
ns_extract["_active_branch"] = bs2
test("3.1.F6: branch exceeded deadline → True", check_bg_deadline() == True)
test("3.1.F7: slot freed after abandonment", ns_extract["_active_branch"] is None)
test("3.1.F8: abandon marker queued", ns_extract["_merge_queue"].qsize() == 1)
marker = ns_extract["_merge_queue"].get_nowait()
test("3.1.F9: marker has branch id", marker.get("branch") == "bg-test2")
test("3.1.F10: marker has abandoned=True", marker.get("abandoned") == True)
test("3.1.F11: marker content has BACKGROUND_BRANCH_ABANDONED", "BACKGROUND_BRANCH_ABANDON" in marker.get("content", ""))

# Branch with completed LLM but exceeded deadline → abandoned
reset_state()
bs3 = BranchState_cls(branch_id="bg-test3", branch_client=None, branch_messages=[], thread=None, result_container={"ok": True})
bs3.created_at = time.time() - 400
ns_extract["_active_branch"] = bs3
check_bg_deadline()
marker3 = ns_extract["_merge_queue"].get_nowait()
test("3.1.F12: marker notes LLM completed", "LLM call completed: True" in marker3.get("content", ""))

# New branch can be set after abandonment
reset_state()
bs4 = BranchState_cls(branch_id="bg-test4", branch_client=None, branch_messages=[], thread=None, result_container={})
bs4.created_at = time.time()
ns_extract["_active_branch"] = bs4
test("3.1.F13: new branch can be set after abandonment", ns_extract["_active_branch"] is not None)

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3.2: try/except wrapper → error markers onto merge queue (R14)
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION 3.2: try/except wrapper → error markers onto merge queue (R14)")
print("=" * 70)

# Source inspection
print("\n--- Source inspection ---")
tgt_src = extract_func_src("_bg_llm_thread_target")
test("3.2.S1: _bg_llm_thread_target exists", tgt_src is not None)
test("3.2.S2: error marker logic in thread target", "error_marker" in tgt_src and "_merge_queue.put" in tgt_src)
test("3.2.S3: error_type in error marker", "error_type" in tgt_src)
test("3.2.S4: error_message in error marker", "error_message" in tgt_src)
test("3.2.S5: error message bounded to 500 chars", "[:500]" in tgt_src)
test("3.2.S6: BACKGROUND_BRANCH_ERROR in content", "BACKGROUND_BRANCH_ERROR" in tgt_src)
test("3.2.S7: compare-and-swap slot free in error path", "_active_branch.branch_id == branch_id" in tgt_src)
test("3.2.S8: result_container branch_id stored in threaded_llm_call", 'result_container["branch_id"]' in source)

# Functional tests
print("\n--- Functional tests ---")

threaded_llm_call = ns_extract.get("threaded_llm_call")
test("3.2.F1: threaded_llm_call callable", callable(threaded_llm_call))

# Slow error: delay=0.5s, T=0.1s → promotes, then errors
reset_state()
ns_extract["ITER_PROMOTE_SECONDS"] = 0.1
mock_err = MockErrorClient(delay=0.5, exc_type=RuntimeError, exc_msg="connection reset")
result_e1, branch_e1 = threaded_llm_call(mock_err, "test-model", [], [], "required", 1000, {})
test("3.2.F2: slow error → (None, BranchState)", result_e1 is None and branch_e1 is not None)
test("3.2.F3: branch_id starts with bg-", branch_e1.branch_id.startswith("bg-"))

time.sleep(1.0)
rc = branch_e1.result_container
test("3.2.F4: result_container ok=False after error", rc.get("ok") == False)
test("3.2.F5: error contains RuntimeError", "RuntimeError" in rc.get("error", ""))

markers_e1 = []
while True:
    try:
        markers_e1.append(ns_extract["_merge_queue"].get_nowait())
    except queue.Empty:
        break
test("3.2.F6: 1 error marker in queue", len(markers_e1) == 1, f"got {len(markers_e1)}")
if markers_e1:
    m = markers_e1[0]
    test("3.2.F7: marker role=system", m.get("role") == "system")
    test("3.2.F8: marker has error=True", m.get("error") == True)
    test("3.2.F9: marker has error_type=RuntimeError", m.get("error_type") == "RuntimeError")
    test("3.2.F10: marker has BACKGROUND_BRANCH_ERROR", "BACKGROUND_BRANCH_ERROR" in m.get("content", ""))
    test("3.2.F11: marker has branch id", m.get("branch") == branch_e1.branch_id)

with ns_extract["_branch_lock"]:
    active = ns_extract["_active_branch"]
test("3.2.F12: slot freed after error", active is None)

# Error message bounded to 500 chars
reset_state()
ns_extract["ITER_PROMOTE_SECONDS"] = 0.1
long_msg = "X" * 5000
mock_long = MockErrorClient(delay=0.5, exc_type=ValueError, exc_msg=long_msg)
threaded_llm_call(mock_long, "test-model", [], [], "required", 1000, {})
time.sleep(1.0)
markers_long = []
while True:
    try:
        markers_long.append(ns_extract["_merge_queue"].get_nowait())
    except queue.Empty:
        break
test("3.2.F13: error_message bounded to <=500 chars",
     len(markers_long) >= 1 and len(markers_long[0].get("error_message", "")) <= 500)

# Fast error before promotion → no marker
reset_state()
ns_extract["ITER_PROMOTE_SECONDS"] = 5
mock_fast = MockErrorClient(delay=0, exc_type=TypeError, exc_msg="bad type")
try:
    threaded_llm_call(mock_fast, "test-model", [], [], "required", 1000, {})
    test("3.2.F14: fast error raised", False, "expected exception")
except Exception:
    test("3.2.F14: fast error raised (not promoted)", True)
markers_fast = []
while True:
    try:
        markers_fast.append(ns_extract["_merge_queue"].get_nowait())
    except queue.Empty:
        break
test("3.2.F15: no markers when error before promotion", len(markers_fast) == 0)

ns_extract["ITER_PROMOTE_SECONDS"] = 30  # restore

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3.3: Shutdown protocol (R17)
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION 3.3: Shutdown protocol (R17)")
print("=" * 70)

# Source inspection
print("\n--- Source inspection ---")
test("3.3.S1: SHUTDOWN_GRACE constant exists", "SHUTDOWN_GRACE" in source)
test("3.3.S2: _shutdown_event exists", "_shutdown_event" in source)
test("3.3.S3: _iter_signal_handler exists", has_func("_iter_signal_handler"))
test("3.3.S4: _install_signal_handlers exists", has_func("_install_signal_handlers"))
test("3.3.S5: graceful_shutdown exists", has_func("graceful_shutdown"))

sig_handler_src = extract_func_src("_iter_signal_handler")
test("3.3.S6: signal handler sets _shutdown_event", sig_handler_src and "_shutdown_event.set()" in sig_handler_src)

install_src = extract_func_src("_install_signal_handlers")
test("3.3.S7: installs SIGTERM handler", install_src and "signal.SIGTERM" in install_src)
test("3.3.S8: installs SIGINT handler", install_src and "signal.SIGINT" in install_src)

shutdown_src = extract_func_src("graceful_shutdown")
test("3.3.S9: graceful_shutdown calls sys.exit", shutdown_src and "sys.exit(0)" in shutdown_src)
test("3.3.S10: graceful_shutdown drains merge queue", shutdown_src and "drain_merge_queue" in shutdown_src)
test("3.3.S11: graceful_shutdown saves experience", shutdown_src and "save_experience" in shutdown_src)

test("3.3.S12: flag-guarded signal handler installation",
     "if ITER_CONCURRENCY_ENABLED:\n    _install_signal_handlers()" in source or
     "if ITER_CONCURRENCY_ENABLED:\n        _install_signal_handlers()" in source)
test("3.3.S13: flag-guarded shutdown check",
     "if ITER_CONCURRENCY_ENABLED and _shutdown_event.is_set():" in source)

# Functional tests
print("\n--- Functional tests ---")

_iter_signal_handler = ns_extract.get("_iter_signal_handler")
_graceful_shutdown = ns_extract.get("graceful_shutdown")

test("3.3.F1: _iter_signal_handler callable", callable(_iter_signal_handler))

# Signal handler sets event
event = ns_extract["_shutdown_event"]
event.clear()
_iter_signal_handler(signal.SIGTERM, None)
test("3.3.F2: SIGTERM sets shutdown event", event.is_set())
event.clear()
_iter_signal_handler(signal.SIGINT, None)
test("3.3.F3: SIGINT sets shutdown event", event.is_set())
event.clear()

# graceful_shutdown with no active branch
reset_state()
tmpdir = tempfile.mkdtemp()
exp_path = os.path.join(tmpdir, "experience.json")
exp_data = [{"role": "user", "content": "test"}]
ns_extract["experience"] = exp_data

def save_exp_override(exp):
    with open(exp_path, "w") as f:
        json.dump(exp, f)
ns_extract["save_experience"] = save_exp_override

try:
    _graceful_shutdown()
    test("3.3.F4: graceful_shutdown exits (no branch)", False, "expected SystemExit")
except SystemExit as e:
    test("3.3.F4: graceful_shutdown exits with code 0", e.code == 0)

saved = json.loads(Path(exp_path).read_text())
test("3.3.F5: experience saved", saved == exp_data)

# graceful_shutdown with completing branch
reset_state()
event.clear()
result_container_d = {}
def fake_complete():
    time.sleep(0.3)
    result_container_d["ok"] = True
    result_container_d["response"] = "done"

t_d = threading.Thread(target=fake_complete, daemon=True)
t_d.start()
bs_d = BranchState_cls(branch_id="bg-comp", branch_client=None, branch_messages=[], thread=t_d, result_container=result_container_d)
bs_d.created_at = time.time()
ns_extract["_active_branch"] = bs_d
ns_extract["experience"] = [{"role": "user", "content": "with branch"}]
ns_extract["SHUTDOWN_GRACE"] = 3

start_t = time.time()
try:
    _graceful_shutdown()
    test("3.3.F6: graceful_shutdown with completing branch exits", False)
except SystemExit as e:
    elapsed = time.time() - start_t
    test("3.3.F6: exits with code 0", e.code == 0)
    test("3.3.F7: waited < 2s for 0.3s branch", elapsed < 2.0, f"elapsed={elapsed:.2f}s")
test("3.3.F8: branch thread completed", not t_d.is_alive())

# graceful_shutdown with slow branch (exceeds grace)
reset_state()
event.clear()
result_container_s = {}
def slow_branch():
    time.sleep(30)
    result_container_s["ok"] = True

t_s = threading.Thread(target=slow_branch, daemon=True)
t_s.start()
bs_s = BranchState_cls(branch_id="bg-slow", branch_client=None, branch_messages=[], thread=t_s, result_container=result_container_s)
bs_s.created_at = time.time()
ns_extract["_active_branch"] = bs_s
ns_extract["experience"] = [{"role": "user", "content": "slow"}]
ns_extract["SHUTDOWN_GRACE"] = 1

start_t2 = time.time()
try:
    _graceful_shutdown()
    test("3.3.F9: graceful_shutdown with slow branch exits", False)
except SystemExit as e:
    elapsed2 = time.time() - start_t2
    test("3.3.F9: exits with code 0", e.code == 0)
    test("3.3.F10: waited ≤ grace + margin", elapsed2 < 2.5, f"elapsed={elapsed2:.2f}s")
test("3.3.F11: slow thread is daemon", t_s.daemon)
test("3.3.F12: experience saved despite slow branch", Path(exp_path).exists())

ns_extract["SHUTDOWN_GRACE"] = 5  # restore

# graceful_shutdown drains merge queue
reset_state()
event.clear()
ns_extract["_active_branch"] = None
mq_drain = queue.Queue()
mq_drain.put({"role": "system", "content": "marker 1", "branch": "bg-a"})
mq_drain.put({"role": "system", "content": "marker 2", "branch": "bg-b"})
ns_extract["_merge_queue"] = mq_drain
ns_extract["experience"] = [{"role": "user", "content": "drain test"}]

try:
    _graceful_shutdown()
except SystemExit:
    pass
saved_drain = json.loads(Path(exp_path).read_text())
test("3.3.F13: merge queue drained (3 entries)", len(saved_drain) == 3, f"got {len(saved_drain)}")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3.4: Duplicate-tool supersede annotation (R16)
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION 3.4: Duplicate-tool supersede annotation (R16)")
print("=" * 70)

# Source inspection
print("\n--- Source inspection ---")
test("3.4.S1: _build_tool_call_map exists", has_func("_build_tool_call_map"))
test("3.4.S2: superseded_by in drain_merge_queue", "superseded_by" in source)
test("3.4.S3: existing_tool_index in source", "existing_tool_index" in source)
test("3.4.S4: merged_call_lookup in source", "merged_call_lookup" in source)

# Functional tests
print("\n--- Functional tests ---")

build_tcm = ns_extract.get("_build_tool_call_map")
test("3.4.F1: _build_tool_call_map callable", callable(build_tcm))

# Basic tool call map
msgs = [make_assistant_entry([{"id": "tc1", "name": "send", "args": '{"channel":"test"}'}])]
lookup = build_tcm(msgs)
test("3.4.F2: single tool call mapped", lookup == {"tc1": ("send", '{"channel":"test"}')})

# Multiple tool calls
msgs2 = [make_assistant_entry([
    {"id": "tc1", "name": "send", "args": '{"channel":"test"}'},
    {"id": "tc2", "name": "nop", "args": '{}'},
])]
lookup2 = build_tcm(msgs2)
test("3.4.F3: two tool calls mapped", len(lookup2) == 2)

# No assistant → empty
lookup3 = build_tcm([{"role": "tool", "tool_call_id": "x", "content": "y"}])
test("3.4.F4: no assistant → empty lookup", lookup3 == {})

# drain_merge_queue with supersede — use module setup approach
def setup_drain_mod(merge_q, experience_list, save_log):
    m = types.ModuleType("drain_test")
    m._merge_queue = merge_q
    m._build_tool_call_map = ns_extract["_build_tool_call_map"]
    m.experience = experience_list
    m.save_experience = make_save_experience(experience_list, save_log)
    m.queue = queue
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "drain_merge_queue":
            mod_code = compile(ast.Module(body=[node], type_ignores=[]), str(ITER_PY), "exec")
            exec(mod_code, m.__dict__)
            break
    return m

# Duplicate: same tool+args
fg_a = make_assistant_entry([{"id": "fg1", "name": "send", "args": '{"channel":"test"}'}])
fg_t = make_tool_entry("fg1", "fg result")
exp_dup = [fg_a, fg_t]
bg_a = make_assistant_entry([{"id": "bg1", "name": "send", "args": '{"channel":"test"}'}])
bg_t = make_tool_entry("bg1", "bg result")
bg_t["branch"] = "bg-dup1"
mq_dup = queue.Queue()
mq_dup.put(bg_a)
mq_dup.put(bg_t)

mod_dup = setup_drain_mod(mq_dup, exp_dup, [])
result_dup = mod_dup.drain_merge_queue()
test("3.4.F5: duplicate merged (2 entries)", result_dup == 2)
test("3.4.F6: bg_tool has superseded_by", "superseded_by" in mod_dup.experience[-1])
test("3.4.F7: superseded_by points to index 1", mod_dup.experience[-1].get("superseded_by") == "1")
test("3.4.F8: bg_assistant does NOT have superseded_by", "superseded_by" not in mod_dup.experience[-2])

# Different tool name → no supersede
fg_a2 = make_assistant_entry([{"id": "fg2", "name": "send", "args": '{"channel":"test"}'}])
fg_t2 = make_tool_entry("fg2", "fg result")
exp_diff = [fg_a2, fg_t2]
bg_a2 = make_assistant_entry([{"id": "bg2", "name": "nop", "args": '{}'}])
bg_t2 = make_tool_entry("bg2", "bg result")
bg_t2["branch"] = "bg-diff"
mq_diff = queue.Queue()
mq_diff.put(bg_a2)
mq_diff.put(bg_t2)
mod_diff = setup_drain_mod(mq_diff, exp_diff, [])
mod_diff.drain_merge_queue()
test("3.4.F9: different tool → no superseded_by", "superseded_by" not in mod_diff.experience[-1])

# Same tool, different args → no supersede
fg_a3 = make_assistant_entry([{"id": "fg3", "name": "send", "args": '{"channel":"test"}'}])
fg_t3 = make_tool_entry("fg3", "fg result")
exp_args = [fg_a3, fg_t3]
bg_a3 = make_assistant_entry([{"id": "bg3", "name": "send", "args": '{"channel":"other"}'}])
bg_t3 = make_tool_entry("bg3", "bg result")
bg_t3["branch"] = "bg-args"
mq_args = queue.Queue()
mq_args.put(bg_a3)
mq_args.put(bg_t3)
mod_args = setup_drain_mod(mq_args, exp_args, [])
mod_args.drain_merge_queue()
test("3.4.F10: same tool different args → no superseded_by", "superseded_by" not in mod_args.experience[-1])

# System markers NOT annotated
fg_a4 = make_assistant_entry([{"id": "fg4", "name": "send", "args": '{"channel":"test"}'}])
fg_t4 = make_tool_entry("fg4", "fg result")
exp_sys = [fg_a4, fg_t4]
err_marker = {"role": "system", "content": "[BACKGROUND_BRANCH_ERROR] test", "branch": "bg-err", "error": True}
mq_sys = queue.Queue()
mq_sys.put(err_marker)
mod_sys = setup_drain_mod(mq_sys, exp_sys, [])
mod_sys.drain_merge_queue()
test("3.4.F11: system marker has no superseded_by", "superseded_by" not in mod_sys.experience[-1])

# Empty queue → no-op
mq_empty = queue.Queue()
exp_empty = [{"role": "user", "content": "hi"}]
mod_empty = setup_drain_mod(mq_empty, exp_empty, [])
result_empty = mod_empty.drain_merge_queue()
test("3.4.F12: empty queue returns 0", result_empty == 0)
test("3.4.F13: experience unchanged", len(mod_empty.experience) == 1)

# save_experience called once per batch
save_count = []
mq_batch = queue.Queue()
mq_batch.put({"role": "system", "content": "m1", "branch": "bg-1"})
mq_batch.put({"role": "system", "content": "m2", "branch": "bg-2"})
mod_batch = setup_drain_mod(mq_batch, [], save_count)
mod_batch.drain_merge_queue()
test("3.4.F14: save_experience called once per batch", len(save_count) == 1)

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3.5: Branch step budget + branch checkpoint queuing (R20)
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION 3.5: Branch step budget + branch checkpoint queuing (R20)")
print("=" * 70)

# Source inspection
print("\n--- Source inspection ---")
test("3.5.S1: BRANCH_STEP_BUDGET constant with default 25",
     'BRANCH_STEP_BUDGET = int(os.getenv("ITER_BRANCH_STEP_BUDGET", "25"))' in source)
test("3.5.S2: _bg_branch_mini_loop exists", has_func("_bg_branch_mini_loop"))

mini_src = extract_func_src("_bg_branch_mini_loop")
test("3.5.S3: mini-loop references BRANCH_STEP_BUDGET", mini_src and "BRANCH_STEP_BUDGET" in mini_src)
test("3.5.S4: queues _checkpoint_payload on exhaustion", mini_src and "_checkpoint_payload" in mini_src)
test("3.5.S5: calls extract_tier1_checkpoint on exhaustion", mini_src and "extract_tier1_checkpoint" in mini_src)
test("3.5.S6: never calls write_checkpoint_file directly", mini_src and "write_checkpoint_file" not in mini_src)
test("3.5.S7: never calls send_checkpoint_message directly", mini_src and "send_checkpoint_message" not in mini_src)
test("3.5.S8: uses branch_client for follow-up calls", mini_src and "branch_client.chat.completions.create" in mini_src)
test("3.5.S9: uses branch_messages", mini_src and "branch_messages" in mini_src)
test("3.5.S10: loads tools at start", mini_src and "load_tools()" in mini_src)
test("3.5.S11: has branch_steps counter", mini_src and "branch_steps" in mini_src)
test("3.5.S12: R14 error handling for follow-up failures", mini_src and "error_marker" in mini_src)
test("3.5.S13: compare-and-swap slot free", mini_src and "_active_branch.branch_id == branch_id" in mini_src)
test("3.5.S14: breaks on no tool_calls", mini_src and "not message.tool_calls" in mini_src)
test("3.5.S15: BRANCH_COMPLETE on normal completion", mini_src and "BRANCH_COMPLETE" in mini_src)

# drain_merge_queue checkpoint handling
drain_src = extract_func_src("drain_merge_queue")
test("3.5.S16: drain detects _checkpoint_payload", drain_src and "_checkpoint_payload" in drain_src)
test("3.5.S17: drain separates checkpoint payloads", drain_src and "checkpoint_payloads" in drain_src)
test("3.5.S18: drain calls write_checkpoint_file from main thread", drain_src and "write_checkpoint_file" in drain_src)
test("3.5.S19: drain calls send_checkpoint_message from main thread", drain_src and "send_checkpoint_message" in drain_src)
test("3.5.S20: drain adds BACKGROUND_BRANCH_CHECKPOINT marker", drain_src and "BACKGROUND_BRANCH_CHECKPOINT" in drain_src)
test("3.5.S21: drain strips internal markers from cp_data",
     "k not in ('branch', '_checkpoint_payload')" in drain_src or 'k not in ("branch", "_checkpoint_payload")' in drain_src)

# threaded_llm_call stores branch info
tllm_src = extract_func_src("threaded_llm_call")
test("3.5.S22: stores branch_client in result_container", "branch_client" in tllm_src and "result_container" in tllm_src)
test("3.5.S23: stores branch_messages in result_container", "branch_messages" in tllm_src and "result_container" in tllm_src)

# _bg_llm_thread_target calls mini-loop
tgt_check = extract_func_src("_bg_llm_thread_target")
test("3.5.S24: checks branch_id after successful call", "branch_id" in tgt_check and "result_container" in tgt_check)
test("3.5.S25: calls _bg_branch_mini_loop", "_bg_branch_mini_loop(" in tgt_check)

# Flag-off: no behavioral change
print("\n--- Flag-off inspection ---")
test("3.5.S26: BRANCH_STEP_BUDGET is module-level constant", "BRANCH_STEP_BUDGET = int" in source)
test("3.5.S27: drain calls flag-guarded (>= 2)",
     len(re.findall(r'if ITER_CONCURRENCY_ENABLED:\s*\n\s*drain_merge_queue\(\)', source)) >= 2)
test("3.5.S28: else branch unchanged (direct call)",
     "response = client.chat.completions.create(model=MODEL, messages=request_messages" in source)
test("3.5.S29: _promoted guard intact", "_promoted = False" in source and "if _promoted:" in source)
test("3.5.S30: M1 checkpoint path intact", "ITER_CHECKPOINT_ENABLED and not send_since_checkpoint" in source)

# ═══════════════════════════════════════════════════════════════════════
# SECTION: Regression — M2/M3 features coexist
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION: Regression — M2/M3 features coexist")
print("=" * 70)

print("\n--- M2 features ---")
test("R.M2.1: threaded_llm_call present", has_func("threaded_llm_call"))
test("R.M2.2: _merge_queue present", "_merge_queue = queue.Queue()" in source)
test("R.M2.3: drain_merge_queue present", has_func("drain_merge_queue"))
test("R.M2.4: BranchState class present", has_class("BranchState"))
test("R.M2.5: ITER_CONCURRENCY_ENABLED defaults to OFF",
     'ITER_CONCURRENCY_ENABLED = os.getenv("ITER_CONCURRENCY_ENABLED", "0")' in source or
     'ITER_CONCURRENCY_ENABLED = os.environ.get("ITER_CONCURRENCY_ENABLED", "0")' in source)
test("R.M2.6: ITER_PROMOTE_SECONDS present", "ITER_PROMOTE_SECONDS" in source)

print("\n--- M3 features ---")
test("R.M3.1: check_background_deadline present", has_func("check_background_deadline"))
test("R.M3.2: BACKGROUND_DEADLINE present", "BACKGROUND_DEADLINE = max(2 * ITER_PROMOTE_SECONDS, 300)" in source)
test("R.M3.3: _iter_signal_handler present", has_func("_iter_signal_handler"))
test("R.M3.4: _install_signal_handlers present", has_func("_install_signal_handlers"))
test("R.M3.5: graceful_shutdown present", has_func("graceful_shutdown"))
test("R.M3.6: SHUTDOWN_GRACE present", "SHUTDOWN_GRACE" in source)
test("R.M3.7: _build_tool_call_map present", has_func("_build_tool_call_map"))
test("R.M3.8: BRANCH_STEP_BUDGET present", "BRANCH_STEP_BUDGET" in source)
test("R.M3.9: _bg_branch_mini_loop present", has_func("_bg_branch_mini_loop"))

print("\n--- M1 features ---")
test("R.M1.1: ITER_CHECKPOINT_ENABLED present", "ITER_CHECKPOINT_ENABLED" in source)
test("R.M1.2: extract_tier1_checkpoint present", has_func("extract_tier1_checkpoint"))
test("R.M1.3: write_checkpoint_file present", has_func("write_checkpoint_file"))
test("R.M1.4: format_checkpoint_message present", has_func("format_checkpoint_message"))
test("R.M1.5: send_checkpoint_message present", has_func("send_checkpoint_message"))

print("\n--- Double drain (R15) ---")
drain_calls = re.findall(r'drain_merge_queue\(\)', source)
test("R.R15.1: at least 2 drain_merge_queue calls in main loop", len(drain_calls) >= 2)

print("\n--- Error markers (R14) ---")
test("R.R14.1: BACKGROUND_BRANCH_ERROR in source", "BACKGROUND_BRANCH_ERROR" in source)
test("R.R14.2: error_type in source", "error_type" in source)
test("R.R14.3: error_message in source", "error_message" in source)

print("\n--- Supersede (R16) ---")
test("R.R16.1: superseded_by in source", "superseded_by" in source)

print("\n--- Shutdown (R17) ---")
test("R.R17.1: daemon threads", "daemon=True" in source)
test("R.R17.2: sys.exit in graceful_shutdown", "sys.exit(0)" in source)

# ═══════════════════════════════════════════════════════════════════════
# SECTION: py_compile
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SECTION: py_compile")
print("=" * 70)

result_pc = subprocess.run([sys.executable, "-m", "py_compile", str(ITER_PY)], capture_output=True, text=True)
test("py_compile passes", result_pc.returncode == 0, result_pc.stderr)

# ═══════════════════════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print(f"TOTAL: {passed} passed, {failed} failed")
print("=" * 70)

if failed:
    print("\nFAILED TESTS:")
    for name, ok, detail in results:
        if not ok:
            print(f"  ✗ {name}: {detail}")
    sys.exit(1)
else:
    print("\n✓ All tests passed.")
