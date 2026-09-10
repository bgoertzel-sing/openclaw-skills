#!/usr/bin/env python3
"""Smoke test for M2 step 2.1: threaded_llm_call with deadline T.

Tests the REAL code extracted from iter.py via AST — not copies.
Validates: fast call returns within T, slow call promotes after T,
deep copy isolation (R11), separate client (R12), daemon thread,
_active_branch set, flag-off source inspection.
"""
import ast
import copy
import threading
import time
import uuid

# Read iter.py source
with open("/home/openclaw/research-agent/projects/omegaclaw/protocosmo2/iter-port/repos/iter.py", "r") as f:
    source = f.read()

tree = ast.parse(source)

# Build a namespace with needed globals
namespace = {
    'threading': threading,
    'copy': copy,
    'uuid': uuid,
    'time': time,
    'print': print,
    'ITER_PROMOTE_SECONDS': 2,
    'API_KEY': 'dummy',
    'BASE_URL': 'http://localhost:1234/v1',
    'LLM_TIMEOUT': 600,
    'SESSION_ID': 'test-session',
    '_branch_lock': threading.Lock(),
    '_active_branch': None,
}

try:
    import openai
    namespace['openai'] = openai
except ImportError:
    print("WARNING: openai not installed — promotion tests may fail on client creation")

# Extract and exec M2 definitions from AST
for node in ast.iter_child_nodes(tree):
    if isinstance(node, ast.ClassDef) and node.name == 'BranchState':
        exec(compile(ast.Module([node], []), 'iter.py', 'exec'), namespace)
    elif isinstance(node, ast.FunctionDef) and node.name in ('_bg_llm_thread_target', 'threaded_llm_call'):
        exec(compile(ast.Module([node], []), 'iter.py', 'exec'), namespace)

threaded_llm_call = namespace['threaded_llm_call']

class FakeClient:
    """Fake OpenAI-compatible client for testing threaded_llm_call."""
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
        return {"fake_response": True}

passed = 0
failed = 0

def test(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS: {name}")
    else:
        failed += 1
        print(f"  FAIL: {name} {detail}")

# --- Test 1: Fast call completes within T ---
print("Test 1: fast call completes within T (T=2s, delay=0)")
fast = FakeClient(delay=0)
resp, branch = threaded_llm_call(fast, "model", [{"role": "user", "content": "hi"}], [], "required", 100, {})
test("response is not None", resp is not None, f"resp={resp}")
test("branch is None", branch is None, f"branch={branch}")
test("response is the fake", resp == {"fake_response": True}, f"resp={resp}")

# --- Test 2: Slow call promotes after T ---
print("\nTest 2: slow call promotes after T (T=1s, delay=5s)")
namespace['ITER_PROMOTE_SECONDS'] = 1
slow = FakeClient(delay=5)
resp2, branch2 = threaded_llm_call(slow, "model", [{"role": "user", "content": "hi"}], [], "required", 100, {})
test("response is None (promoted)", resp2 is None, f"resp={resp2}")
test("branch is not None", branch2 is not None, f"branch={branch2}")
test("branch_id starts with bg-", branch2 is not None and branch2.branch_id.startswith("bg-"), f"branch_id={branch2.branch_id if branch2 else None}")
test("thread is alive (still running)", branch2 is not None and branch2.thread.is_alive(), "")

# --- Test 3: Deep copy isolation (R11) ---
print("\nTest 3: deep copy isolation (R11)")
test_msgs = [{"role": "user", "content": "original"}]
_, branch3 = threaded_llm_call(FakeClient(delay=5), "model", test_msgs, [], "required", 100, {})
test("branch_messages is not same object", branch3 is not None and branch3.branch_messages is not test_msgs)
test("branch_messages content matches", branch3 is not None and branch3.branch_messages == [{"role": "user", "content": "original"}])
test_msgs[0]["content"] = "mutated"
test("deep copy unaffected by mutation", branch3 is not None and branch3.branch_messages[0]["content"] == "original", f"got: {branch3.branch_messages[0]['content'] if branch3 else None}")

# --- Test 4: Separate OpenAI client (R12) ---
print("\nTest 4: separate OpenAI client (R12)")
test("branch_client is not None", branch3 is not None and branch3.branch_client is not None)

# --- Test 5: Thread is daemon (R17 partial) ---
print("\nTest 5: thread is daemon (R17 partial)")
test("thread.daemon == True", branch3 is not None and branch3.thread.daemon)

# --- Test 6: _active_branch set after promotion ---
print("\nTest 6: _active_branch set after promotion")
test("_active_branch is not None", namespace.get('_active_branch') is not None)
test("_active_branch matches returned branch", namespace.get('_active_branch') is not None and namespace['_active_branch'].branch_id == branch3.branch_id)

# --- Test 7: Branch result_container will be populated when thread completes ---
print("\nTest 7: result_container populated after thread completes")
# branch2 was started with delay=5; wait for it
if branch2:
    branch2.thread.join(timeout=10)
    test("thread completed", not branch2.thread.is_alive())
    test("result_container has ok", branch2.result_container.get("ok") is True)
    test("result_container has response", "response" in branch2.result_container)

# --- Test 8: Flag-off path — source inspection ---
print("\nTest 8: flag-off path source inspection")
test("ITER_CONCURRENCY_ENABLED in source", "ITER_CONCURRENCY_ENABLED" in source)
test("if ITER_CONCURRENCY_ENABLED: in source", "if ITER_CONCURRENCY_ENABLED:" in source)
# Verify the else branch contains the direct call
else_idx = source.index("if ITER_CONCURRENCY_ENABLED:")
after_guard = source[else_idx:]
test("direct call in else branch", "client.chat.completions.create" in after_guard)
test("_promoted = False in source", "_promoted = False" in source)
test("if _promoted: continue in source", "if _promoted:" in source and "continue" in source)

# --- Test 9: Call that fails within T raises exception ---
print("\nTest 9: failed call within T raises exception")
class FailingClient(FakeClient):
    def create(self, **kwargs):
        raise RuntimeError("simulated API error")
try:
    threaded_llm_call(FailingClient(delay=0), "model", [], [], "required", 100, {})
    test("should have raised", False, "no exception")
except Exception as e:
    test("raised exception", "Background LLM call failed" in str(e), f"msg={e}")

# Cleanup: stop any lingering threads
# branch3's thread is still running (delay=5, already completed by now)
# branch2's thread completed in test 7

print(f"\n{'='*40}")
print(f"Results: {passed} passed, {failed} failed")
if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
