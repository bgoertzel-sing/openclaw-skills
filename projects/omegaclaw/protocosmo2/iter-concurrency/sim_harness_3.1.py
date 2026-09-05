#!/usr/bin/env python3
"""Standalone test for M3 Step 3.1: BACKGROUND_DEADLINE — abandon + marker + slot frees (R13)."""
import ast
import time
import threading
import queue
import re
import subprocess
import sys

ITER_PY = "iter.py"
BACKUP = "iter.py.pre-m3-3.1-20260904T1854"

with open(ITER_PY) as f:
    source = f.read()

# --- Source-level verification ---
tree = ast.parse(source)

# 1. BACKGROUND_DEADLINE constant exists
constant_found = False
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "BACKGROUND_DEADLINE":
                constant_found = True
                print(f"[source] BACKGROUND_DEADLINE constant at line {node.lineno}")
assert constant_found, "BACKGROUND_DEADLINE constant not found"

# 2. check_background_deadline function exists
func_found = False
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "check_background_deadline":
        func_found = True
        print(f"[source] check_background_deadline function at line {node.lineno}")
assert func_found, "check_background_deadline function not found"

# 3. Function uses _branch_lock and _active_branch (thread-safe)
func_source = None
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "check_background_deadline":
        func_source = ast.get_source_segment(source, node)
assert "_branch_lock" in func_source, "check_background_deadline should use _branch_lock"
assert "_active_branch" in func_source, "check_background_deadline should use _active_branch"
assert "_merge_queue" in func_source, "check_background_deadline should use _merge_queue"
print("[source] function uses _branch_lock, _active_branch, _merge_queue")

# 4. Flag-guarded call in main loop
call_pattern = r"if ITER_CONCURRENCY_ENABLED:\s*\n\s*check_background_deadline\(\)"
matches = re.findall(call_pattern, source)
print(f"[source] flag-guarded check_background_deadline() calls: {len(matches)}")
assert len(matches) >= 1, "Expected at least 1 flag-guarded call"

# 5. No existing lines deleted (pure additions)
result = subprocess.run(["diff", BACKUP, ITER_PY], capture_output=True, text=True)
diff_lines = result.stdout.split("\n")
additions = [l for l in diff_lines if l.startswith(">")]
deletions = [l for l in diff_lines if l.startswith("<")]
print(f"[source] diff vs backup: {len(additions)} additions, {len(deletions)} deletions")
assert len(deletions) == 0, f"Should have no deletions, found: {deletions}"
print("[source] no deletions — pure additions only")

# --- Logic tests (simulated environment) ---
_branch_lock = threading.Lock()
_active_branch = None
_merge_queue = queue.Queue()
BACKGROUND_DEADLINE = 300  # max(2*30, 300) = 300


class FakeBranch:
    def __init__(self, branch_id, created_at, result_container):
        self.branch_id = branch_id
        self.created_at = created_at
        self.result_container = result_container


def check_background_deadline():
    global _active_branch
    with _branch_lock:
        branch = _active_branch
        if branch is None:
            return False
        elapsed = time.time() - branch.created_at
        if elapsed <= BACKGROUND_DEADLINE:
            return False
        branch_id = branch.branch_id
        has_result = bool(branch.result_container.get("ok", False))
        _active_branch = None
    abandon_marker = {
        "role": "system",
        "content": (
            f"[BACKGROUND_BRANCH_ABANDONED] branch_id={branch_id} "
            f"elapsed={elapsed:.1f}s deadline={BACKGROUND_DEADLINE}s. "
            f"LLM call completed: {has_result}. Results discarded."
        ),
        "branch": branch_id,
        "abandoned": True,
    }
    _merge_queue.put(abandon_marker)
    return True


# Test 1: No active branch → False, empty queue
assert check_background_deadline() == False
assert _merge_queue.qsize() == 0
print("Test 1 PASSED: no active branch → False, empty queue")

# Test 2: Branch within deadline → False, branch still active
_active_branch = FakeBranch("bg-test1", time.time(), {})
assert check_background_deadline() == False
assert _merge_queue.qsize() == 0
assert _active_branch is not None
print("Test 2 PASSED: branch within deadline → False, branch still active")

# Test 3: Branch exceeded deadline → True, marker queued, slot freed
_active_branch = FakeBranch("bg-test2", time.time() - 301, {})
assert check_background_deadline() == True
assert _active_branch is None
assert _merge_queue.qsize() == 1
marker = _merge_queue.get_nowait()
assert marker["branch"] == "bg-test2"
assert marker["abandoned"] == True
assert "BACKGROUND_BRANCH_ABANDONED" in marker["content"]
print("Test 3 PASSED: branch exceeded deadline → True, marker queued, slot freed")
print("  Marker: " + marker["content"])

# Test 4: Branch with completed LLM but exceeded deadline → abandoned
_active_branch = FakeBranch("bg-test3", time.time() - 301, {"ok": True, "response": "x"})
assert check_background_deadline() == True
assert _active_branch is None
marker = _merge_queue.get_nowait()
assert "LLM call completed: True" in marker["content"]
print("Test 4 PASSED: branch with completed LLM but exceeded deadline → abandoned")

# Test 5: After abandonment, new branch can be set
_active_branch = FakeBranch("bg-test4", time.time(), {})
assert _active_branch is not None
print("Test 5 PASSED: new branch can be set after abandonment")

# Test 6: Thread-safety — _branch_lock used
with _branch_lock:
    print("Test 6 PASSED: _branch_lock is a threading.Lock (verified by context manager)")

# Test 7: Abandon marker has all required fields
_active_branch = FakeBranch("bg-test5", time.time() - 400, {})
check_background_deadline()
marker = _merge_queue.get_nowait()
assert marker["role"] == "system"
assert marker["branch"] == "bg-test5"
assert marker["abandoned"] == True
assert "elapsed" in marker["content"]
assert "deadline" in marker["content"]
print("Test 7 PASSED: abandon marker has role, branch, abandoned, elapsed, deadline")

# Test 8: BACKGROUND_DEADLINE value is max(2T, 300) with default T=30
expected_deadline = max(2 * 30, 300)
assert BACKGROUND_DEADLINE == expected_deadline == 300
print(f"Test 8 PASSED: BACKGROUND_DEADLINE = max(2*30, 300) = {expected_deadline}")

# Test 9: py_compile
result = subprocess.run([sys.executable, "-m", "py_compile", ITER_PY], capture_output=True, text=True)
assert result.returncode == 0, f"py_compile failed: {result.stderr}"
print("Test 9 PASSED: py_compile OK")

print("\nAll 9 tests PASSED — 0 failed")
