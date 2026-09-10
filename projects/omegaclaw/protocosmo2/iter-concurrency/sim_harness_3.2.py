#!/usr/bin/env python3
"""Sim harness for M3 Step 3.2: try/except wrapper → error markers onto merge queue (R14).

Tests the actual code from iter.py via AST extraction — not copies.
All tests are provider-free (no OpenAI API calls).
"""
import ast
import copy
import json
import os
import queue
import subprocess
import sys
import threading
import time
import types
import uuid
from pathlib import Path

ITER_PATH = Path(__file__).parent.parent / "iter-port" / "repos" / "iter.py"

# ─── Extract functions from iter.py source ────────────────────────────────
source = ITER_PATH.read_text(encoding="utf-8")
tree = ast.parse(source)

ns = {}
ns["queue"] = queue
ns["threading"] = threading
ns["time"] = time
ns["uuid"] = uuid
ns["copy"] = copy
ns["Path"] = Path
ns["os"] = os

needed_names = [
    "_merge_queue", "_branch_lock", "_active_branch",
    "BranchState", "_bg_llm_thread_target",
    "threaded_llm_call", "drain_merge_queue", "check_background_deadline",
    "_build_tool_call_map",
]

for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        if node.name in needed_names:
            exec(compile(ast.Module([node], type_ignores=[]), str(ITER_PATH), "exec"), ns)
    elif isinstance(node, ast.ClassDef):
        if node.name == "BranchState":
            exec(compile(ast.Module([node], type_ignores=[]), str(ITER_PATH), "exec"), ns)
    elif isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in needed_names:
                exec(compile(ast.Module([node], type_ignores=[]), str(ITER_PATH), "exec"), ns)

# Set SESSION_ID
if "SESSION_ID" not in ns:
    ns["SESSION_ID"] = "test-" + uuid.uuid4().hex[:8]

# Monkeypatch openai
class FakeOpenAI:
    def __init__(self, **kwargs):
        pass
ns["openai"] = types.SimpleNamespace(OpenAI=FakeOpenAI)

# Constants needed
ns["ITER_PROMOTE_SECONDS"] = 30
ns["LLM_TIMEOUT"] = 600
ns["API_KEY"] = "dummy"
ns["BASE_URL"] = "http://localhost"

# ─── Mock clients (simplified) ────────────────────────────────────────────

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


# ─── Reset helpers ────────────────────────────────────────────────────────

def reset_state():
    with ns["_branch_lock"]:
        ns["_active_branch"] = None
    ns["_merge_queue"] = queue.Queue()

# ─── Tests ─────────────────────────────────────────────────────────────────

passed = 0
failed = 0

def test(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS: {name}")
    else:
        failed += 1
        print(f"  FAIL: {name} — {detail}")

print("=" * 70)
print("M3 Step 3.2: try/except wrapper → error markers onto merge queue (R14)")
print("=" * 70)

# ── Group A: Error marker pushed on background LLM failure ─────────────────

print("\n--- Group A: Error marker on background LLM failure ---")

reset_state()

# Slow error: delay=0.5s, T=0.1s → thread alive at T, gets promoted, then errors
# But ITER_PROMOTE_SECONDS is 30 in the extracted code. We need to override it.
# Actually, threaded_llm_call reads ITER_PROMOTE_SECONDS from the module namespace.
# Let's override it in ns.
ns["ITER_PROMOTE_SECONDS"] = 0.1  # 100ms timeout

mock_client = MockErrorClient(delay=0.5, exc_type=RuntimeError, exc_msg="connection reset")

result, branch = ns["threaded_llm_call"](
    mock_client, "test-model", [], [], "required", 1000, {}
)

test("A1: threaded_llm_call returns (None, BranchState) on timeout",
     result is None and branch is not None,
     f"result={result}, branch={branch}")
test("A2: branch has bg- prefix in branch_id",
     branch is not None and branch.branch_id.startswith("bg-"),
     f"branch_id={branch.branch_id if branch else 'None'}")

# Wait for the thread to error out
time.sleep(1.0)

rc = branch.result_container
test("A3: result_container has ok=False after error",
     rc.get("ok") == False, f"ok={rc.get('ok')}")
test("A4: result_container has error with RuntimeError",
     "RuntimeError" in rc.get("error", ""), f"error={rc.get('error','')}")
test("A5: result_container has branch_id matching branch.branch_id",
     rc.get("branch_id") == branch.branch_id,
     f"rc.branch_id={rc.get('branch_id')}, branch.branch_id={branch.branch_id}")

# Check merge queue for error markers
mq = ns["_merge_queue"]
markers = []
while True:
    try:
        markers.append(mq.get_nowait())
    except queue.Empty:
        break

test("A6: exactly 1 error marker in merge queue",
     len(markers) == 1, f"got {len(markers)} markers")

if markers:
    m = markers[0]
    test("A7: marker role is 'system'",
         m.get("role") == "system", f"role={m.get('role')}")
    test("A8: marker has branch id matching branch.branch_id",
         m.get("branch") == branch.branch_id,
         f"marker.branch={m.get('branch')}, branch.branch_id={branch.branch_id}")
    test("A9: marker has error=True",
         m.get("error") == True, f"error={m.get('error')}")
    test("A10: marker has error_type='RuntimeError'",
         m.get("error_type") == "RuntimeError",
         f"error_type={m.get('error_type')}")
    test("A11: marker content contains BACKGROUND_BRANCH_ERROR",
         "BACKGROUND_BRANCH_ERROR" in m.get("content", ""),
         f"content: {m.get('content','')[:80]}")
    test("A12: marker content contains branch_id",
         branch.branch_id in m.get("content", ""),
         f"content: {m.get('content','')[:80]}")
    test("A13: marker has error_message field",
         "error_message" in m, f"keys: {list(m.keys())}")

# Check that branch slot was freed
with ns["_branch_lock"]:
    active = ns["_active_branch"]
test("A14: _active_branch freed (None) after error",
     active is None, f"got {active}")

# ── Group B: Error marker message bounded (500 chars) ─────────────────────

print("\n--- Group B: Error message bounding (500 chars) ---")

reset_state()
ns["ITER_PROMOTE_SECONDS"] = 0.1

long_msg = "X" * 5000
mock_client2 = MockErrorClient(delay=0.5, exc_type=ValueError, exc_msg=long_msg)

result2, branch2 = ns["threaded_llm_call"](
    mock_client2, "test-model", [], [], "required", 1000, {}
)

time.sleep(1.0)

mq2 = ns["_merge_queue"]
markers2 = []
while True:
    try:
        markers2.append(mq2.get_nowait())
    except queue.Empty:
        break

test("B1: error marker present", len(markers2) == 1)
if markers2:
    m2 = markers2[0]
    test("B2: error_message bounded to <=500 chars",
         len(m2.get("error_message", "")) <= 500,
         f"len={len(m2.get('error_message', ''))}")
    test("B3: error_type is ValueError",
         m2.get("error_type") == "ValueError",
         f"error_type={m2.get('error_type')}")
    # Content should also be bounded (contains the truncated message)
    test("B4: content contains truncated error (not full 5000 chars)",
         "X" * 5000 not in m2.get("content", ""),
         f"content len={len(m2.get('content', ''))}")

# ── Group C: Branch slot freed after error ──────────────────────────────────

print("\n--- Group C: Branch slot freed after error ---")

reset_state()
ns["ITER_PROMOTE_SECONDS"] = 0.1

mock_client3 = MockErrorClient(delay=0.3, exc_type=ConnectionError, exc_msg="network unreachable")

result3, branch3 = ns["threaded_llm_call"](
    mock_client3, "test-model", [], [], "required", 1000, {}
)

test("C1: branch created", branch3 is not None)
with ns["_branch_lock"]:
    active_before = ns["_active_branch"]
test("C2: _active_branch set after promotion",
     active_before is not None and active_before.branch_id == branch3.branch_id)

time.sleep(1.0)

with ns["_branch_lock"]:
    active_after = ns["_active_branch"]
test("C3: _active_branch freed after error",
     active_after is None, f"got {active_after}")

# ── Group D: Error before promotion (fast error) → no marker ──────────────

print("\n--- Group D: Error before promotion (fast error, no marker) ---")

reset_state()
ns["ITER_PROMOTE_SECONDS"] = 5  # long timeout, error fires first

mock_client_fast = MockErrorClient(delay=0, exc_type=TypeError, exc_msg="bad type")

try:
    result_fast, branch_fast = ns["threaded_llm_call"](
        mock_client_fast, "test-model", [], [], "required", 1000, {}
    )
    test("D1: fast error raised (not promoted)", False, "expected exception")
except Exception as e:
    test("D1: fast error raised (not promoted)", True)
    test("D2: error contains TypeError",
         "TypeError" in str(e), f"got: {e}")

mq_d = ns["_merge_queue"]
markers_d = []
while True:
    try:
        markers_d.append(mq_d.get_nowait())
    except queue.Empty:
        break
test("D3: no error markers when error before promotion",
     len(markers_d) == 0, f"got {len(markers_d)} markers")

# ── Group E: Slot not freed if already freed by deadline ───────────────────

print("\n--- Group E: Slot already freed — thread still pushes marker ---")

reset_state()
ns["ITER_PROMOTE_SECONDS"] = 0.1

# Manually simulate: promote, then deadline frees, then thread errors
mock_client_e = MockErrorClient(delay=0.5, exc_type=OSError, exc_msg="connection lost")
result_e, branch_e = ns["threaded_llm_call"](
    mock_client_e, "test-model", [], [], "required", 1000, {}
)

# Immediately free the slot (simulating deadline check)
with ns["_branch_lock"]:
    ns["_active_branch"] = None

# Wait for thread to error
time.sleep(1.0)

# Thread should still have pushed error marker (branch_id was in result_container)
mq_e = ns["_merge_queue"]
markers_e = []
while True:
    try:
        markers_e.append(mq_e.get_nowait())
    except queue.Empty:
        break

test("E1: error marker still pushed even when slot pre-freed",
     len(markers_e) == 1, f"got {len(markers_e)} markers")
if markers_e:
    test("E2: marker has correct branch_id",
         markers_e[0].get("branch") == branch_e.branch_id,
         f"got {markers_e[0].get('branch')}, expected {branch_e.branch_id}")

# Slot should still be None (thread checked before freeing)
with ns["_branch_lock"]:
    active_e = ns["_active_branch"]
test("E3: _active_branch remains None (thread saw it already freed)",
     active_e is None, f"got {active_e}")

# ── Group F: Flag-off path unchanged ────────────────────────────────────────

print("\n--- Group F: Flag-off path byte-identical ---")

source_text = ITER_PATH.read_text(encoding="utf-8")

test("F1: 'if ITER_CONCURRENCY_ENABLED:' guards threaded_llm_call",
     "if ITER_CONCURRENCY_ENABLED:\n                response, _branch = threaded_llm_call" in source_text)

test("F2: else branch has direct client.chat.completions.create",
     "else:\n                response = client.chat.completions.create" in source_text)

# Diff analysis
diff_result = subprocess.run(
    ["diff", str(ITER_PATH) + ".pre-m3-3.2-20260904T1924", str(ITER_PATH)],
    capture_output=True, text=True
)
diff_lines = diff_result.stdout.strip().split("\n") if diff_result.stdout else []
added = [l for l in diff_lines if l.startswith(">")]
removed = [l for l in diff_lines if l.startswith("<")]

# Only the docstring line was replaced (1 line removed, rest additions)
test("F3: diff has <= 1 removed line (docstring expansion)",
     len(removed) <= 1,
     f"removed {len(removed)} lines: {removed[:3]}")

test("F4: additions include error_marker dict",
     any("error_marker" in a for a in added))
test("F5: additions include _merge_queue.put",
     any("_merge_queue.put" in a for a in added))
test("F6: additions include result_container branch_id assignment",
     any('result_container["branch_id"]' in a for a in added))
test("F7: additions include _active_branch None check",
     any("_active_branch" in a and "None" in a for a in added))
test("F8: additions include error_type field",
     any("error_type" in a for a in added))
test("F9: additions include error_message field",
     any("error_message" in a for a in added))

# ── Group G: py_compile ─────────────────────────────────────────────────────

print("\n--- Group G: py_compile ---")

import py_compile
try:
    py_compile.compile(str(ITER_PATH), doraise=True)
    test("G1: py_compile passes", True)
except py_compile.PyCompileError as e:
    test("G1: py_compile passes", False, str(e))

# ── Summary ─────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print(f"RESULTS: {passed} passed, {failed} failed")
print("=" * 70)
sys.exit(1 if failed else 0)
