#!/usr/bin/env python3
"""Simulation harness for M3 Step 3.4: Duplicate-tool supersede annotation (R16).

Tests the supersede detection logic in drain_merge_queue by:
- Extracting the real functions from iter.py source via AST
- Testing with mock experience lists and merge queue entries
- Verifying that duplicate tool calls get annotated with superseded_by
- Verifying that non-duplicate tool calls do NOT get annotated
- Verifying flag-off behavior is unchanged
- Regression: M2 drain_merge_queue basic functionality still works
"""

import ast
import json
import os
import queue
import sys
import tempfile
import types

# ─── Extract real code from iter.py ────────────────────────────────────────
ITER_PATH = os.path.join(
    os.path.dirname(__file__), "..", "iter-port", "repos", "iter.py"
)
ITER_PATH = os.path.abspath(ITER_PATH)

with open(ITER_PATH, "r", encoding="utf-8") as f:
    source = f.read()
    source_tree = ast.parse(source)

# Extract _build_tool_call_map and drain_merge_queue
target_names = {"_build_tool_call_map", "drain_merge_queue"}
extracted = {}
for node in source_tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in target_names:
        mod = ast.Module(body=[node], type_ignores=[])
        code = compile(mod, ITER_PATH, "exec")
        ns = {}
        exec(code, ns)
        extracted[node.name] = ns[node.name]

build_tool_call_map = extracted["_build_tool_call_map"]
drain_merge_queue = extracted["drain_merge_queue"]

# Also need save_experience for drain_merge_queue to call
def make_save_experience(experience_list, save_log):
    def save_experience(experience):
        save_log.append(list(experience))  # save a copy
    return save_experience

# ─── Test helpers ──────────────────────────────────────────────────────────
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

def make_assistant_entry(tool_calls):
    """Create an assistant entry with tool_calls (simulating model_dump output)."""
    return {
        "role": "assistant",
        "content": None,
        "tool_calls": [
            {
                "id": tc["id"],
                "type": "function",
                "function": {"name": tc["name"], "arguments": tc["args"]},
            }
            for tc in tool_calls
        ],
    }

def make_tool_entry(tool_call_id, content="result"):
    """Create a tool result entry."""
    return {
        "role": "tool",
        "tool_call_id": tool_call_id,
        "content": f"Step 2026-09-05 03:24:00: {content}",
    }

# ─── Tests ─────────────────────────────────────────────────────────────────

print("=" * 70)
print("M3 Step 3.4: Duplicate-tool supersede annotation (R16)")
print("=" * 70)

# --- Group A: _build_tool_call_map ---
print("\n--- Group A: _build_tool_call_map ---")

# A1: Basic lookup from assistant with tool_calls
msgs = [make_assistant_entry([{"id": "tc1", "name": "send", "args": '{"channel":"test"}'}])]
lookup = build_tool_call_map(msgs)
test("A1: single tool call mapped", lookup == {"tc1": ("send", '{"channel":"test"}')},
     f"got {lookup}")

# A2: Multiple tool calls in one assistant message
msgs = [make_assistant_entry([
    {"id": "tc1", "name": "send", "args": '{"channel":"test"}'},
    {"id": "tc2", "name": "nop", "args": '{}'},
])]
lookup = build_tool_call_map(msgs)
test("A2: two tool calls mapped", lookup == {"tc1": ("send", '{"channel":"test"}'), "tc2": ("nop", '{}')},
     f"got {lookup}")

# A3: No assistant entries → empty lookup
lookup = build_tool_call_map([{"role": "tool", "tool_call_id": "x", "content": "y"}])
test("A3: no assistant → empty lookup", lookup == {})

# A4: Assistant without tool_calls → empty lookup
lookup = build_tool_call_map([{"role": "assistant", "content": "hello"}])
test("A4: assistant without tool_calls → empty lookup", lookup == {})

# A5: Multiple assistant messages, later overrides earlier with same id
msgs = [
    make_assistant_entry([{"id": "tc1", "name": "send", "args": '{"channel":"a"}'}]),
    make_assistant_entry([{"id": "tc1", "name": "send", "args": '{"channel":"b"}'}]),
]
lookup = build_tool_call_map(msgs)
test("A5: later assistant overrides same tool_call_id", lookup == {"tc1": ("send", '{"channel":"b"}')},
     f"got {lookup}")

# A6: Non-dict tool_calls are skipped
msgs = [{"role": "assistant", "tool_calls": ["not_a_dict", {"id": "tc1", "function": {"name": "send", "arguments": "{}"}}]}]
lookup = build_tool_call_map(msgs)
test("A6: non-dict tool_calls skipped", lookup == {"tc1": ("send", "{}")},
     f"got {lookup}")

# --- Group B: drain_merge_queue with supersede detection ---
print("\n--- Group B: drain_merge_queue with supersede detection ---")

# B1: Duplicate tool call — background calls same tool+args as foreground
experience = []
merge_q = queue.Queue()
save_log = []

# Foreground already has: assistant with tool_call send(channel=test), tool result
fg_assistant = make_assistant_entry([{"id": "fg_tc1", "name": "send", "args": '{"channel":"test"}'}])
fg_tool = make_tool_entry("fg_tc1", "foreground result")
experience = [fg_assistant, fg_tool]

# Background pushes: assistant with same tool+args (different tool_call_id), tool result
bg_assistant = make_assistant_entry([{"id": "bg_tc1", "name": "send", "args": '{"channel":"test"}'}])
bg_tool = make_tool_entry("bg_tc1", "background result")
bg_tool["branch"] = "bg-test1"
merge_q.put(bg_assistant)
merge_q.put(bg_tool)

# Run drain_merge_queue with injected globals
# We need to create a module-like environment
import threading

# Create a temporary module to hold the function with the right globals
def setup_mod(name, merge_q, experience_list, save_log):
    m = types.ModuleType(name)
    m._merge_queue = merge_q
    m._build_tool_call_map = build_tool_call_map
    m.experience = experience_list
    m.save_experience = make_save_experience(experience_list, save_log)
    m.queue = queue
    for node in source_tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "drain_merge_queue":
            mod_code = compile(ast.Module(body=[node], type_ignores=[]), ITER_PATH, "exec")
            exec(mod_code, m.__dict__)
            break
    return m

mod = setup_mod("test_mod", merge_q, experience, save_log)

result = mod.drain_merge_queue()
test("B1: merged count is 2", result == 2, f"got {result}")
test("B1: experience grew to 4", len(mod.experience) == 4, f"got {len(mod.experience)}")
# The bg_tool entry should have superseded_by pointing to index 1 (fg_tool)
bg_tool_entry = mod.experience[-1]  # last entry is bg_tool
test("B1: bg_tool has superseded_by", "superseded_by" in bg_tool_entry,
     f"keys={bg_tool_entry.keys()}")
test("B1: superseded_by points to fg_tool index 1", bg_tool_entry.get("superseded_by") == "1",
     f"got {bg_tool_entry.get('superseded_by')}")
test("B1: bg_assistant does NOT have superseded_by", "superseded_by" not in mod.experience[-2],
     f"keys={mod.experience[-2].keys()}")

# B2: Non-duplicate tool call — different tool name
experience2 = []
merge_q2 = queue.Queue()
save_log2 = []

fg_assistant2 = make_assistant_entry([{"id": "fg_tc2", "name": "send", "args": '{"channel":"test"}'}])
fg_tool2 = make_tool_entry("fg_tc2", "foreground result")
experience2 = [fg_assistant2, fg_tool2]

bg_assistant2 = make_assistant_entry([{"id": "bg_tc2", "name": "nop", "args": '{}'}])
bg_tool2 = make_tool_entry("bg_tc2", "background result")
bg_tool2["branch"] = "bg-test2"
merge_q2.put(bg_assistant2)
merge_q2.put(bg_tool2)

mod2 = setup_mod("test_mod2", merge_q2, experience2, save_log2)

result2 = mod2.drain_merge_queue()
test("B2: merged count is 2", result2 == 2, f"got {result2}")
test("B2: bg_tool2 does NOT have superseded_by (different tool)", "superseded_by" not in mod2.experience[-1],
     f"keys={mod2.experience[-1].keys()}")

# B3: Same tool name, different arguments → NOT a duplicate
experience3 = []
merge_q3 = queue.Queue()
save_log3 = []

fg_assistant3 = make_assistant_entry([{"id": "fg_tc3", "name": "send", "args": '{"channel":"test"}'}])
fg_tool3 = make_tool_entry("fg_tc3", "foreground result")
experience3 = [fg_assistant3, fg_tool3]

bg_assistant3 = make_assistant_entry([{"id": "bg_tc3", "name": "send", "args": '{"channel":"other"}'}])
bg_tool3 = make_tool_entry("bg_tc3", "background result")
bg_tool3["branch"] = "bg-test3"
merge_q3.put(bg_assistant3)
merge_q3.put(bg_tool3)

mod3 = setup_mod("test_mod3", merge_q3, experience3, save_log3)

result3 = mod3.drain_merge_queue()
test("B3: merged count is 2", result3 == 2)
test("B3: same tool different args → NO superseded_by", "superseded_by" not in mod3.experience[-1],
     f"keys={mod3.experience[-1].keys()}")

# B4: Multiple duplicates — only first occurrence gets superseded_by
experience4 = []
merge_q4 = queue.Queue()
save_log4 = []

# Foreground has two calls to send(channel=test)
fg_a4 = make_assistant_entry([
    {"id": "fg_tc4a", "name": "send", "args": '{"channel":"test"}'},
    {"id": "fg_tc4b", "name": "send", "args": '{"channel":"test"}'},
])
fg_t4a = make_tool_entry("fg_tc4a", "result a")
fg_t4b = make_tool_entry("fg_tc4b", "result b")
experience4 = [fg_a4, fg_t4a, fg_t4b]

# Background also calls send(channel=test)
bg_a4 = make_assistant_entry([{"id": "bg_tc4", "name": "send", "args": '{"channel":"test"}'}])
bg_t4 = make_tool_entry("bg_tc4", "bg result")
bg_t4["branch"] = "bg-test4"
merge_q4.put(bg_a4)
merge_q4.put(bg_t4)

mod4 = setup_mod("test_mod4", merge_q4, experience4, save_log4)

result4 = mod4.drain_merge_queue()
test("B4: merged count is 2", result4 == 2)
# existing_tool_index maps ("send", '{"channel":"test"}') → 1 (first occurrence, which is fg_t4a at index 1)
bg_t4_entry = mod4.experience[-1]
test("B4: superseded_by points to first occurrence index 1", bg_t4_entry.get("superseded_by") == "1",
     f"got {bg_t4_entry.get('superseded_by')}")

# B5: Empty queue → returns 0, no-op
merge_q5 = queue.Queue()
exp5 = [{"role": "user", "content": "hello"}]
save_log_5 = []
mod5 = setup_mod("test_mod5", merge_q5, exp5, save_log_5)

result5 = mod5.drain_merge_queue()
test("B5: empty queue returns 0", result5 == 0)
test("B5: empty queue → no save called", len(save_log_5) == 0)
test("B5: experience unchanged", len(exp5) == 1)

# B6: Non-dict entries skipped
merge_q6 = queue.Queue()
merge_q6.put("not a dict")
merge_q6.put(42)
merge_q6.put({"role": "system", "content": "marker", "branch": "bg-x"})
mod6 = setup_mod("test_mod6", merge_q6, [], [])

result6 = mod6.drain_merge_queue()
test("B6: non-dict entries skipped, only 1 merged", result6 == 1, f"got {result6}")
test("B6: experience has 1 entry", len(mod6.experience) == 1)

# B7: Untagged entry gets "unknown" branch tag
merge_q7 = queue.Queue()
entry7 = {"role": "system", "content": "test marker"}
merge_q7.put(entry7)
mod7 = setup_mod("test_mod7", merge_q7, [], [])

result7 = mod7.drain_merge_queue()
test("B7: untagged entry gets 'unknown' branch", mod7.experience[0].get("branch") == "unknown",
     f"got {mod7.experience[0].get('branch')}")

# --- Group C: Edge cases for supersede ---
print("\n--- Group C: Edge cases for supersede ---")

# C1: Background tool entry without a preceding assistant in merge batch
# (tool_call_id not in merged_call_lookup → no annotation)
experience_c1 = []
merge_q_c1 = queue.Queue()

fg_c1 = make_assistant_entry([{"id": "fg_c1", "name": "send", "args": '{"channel":"test"}'}])
fg_t_c1 = make_tool_entry("fg_c1", "fg result")
experience_c1 = [fg_c1, fg_t_c1]

# Background pushes only a tool entry (no assistant in queue)
bg_t_c1 = make_tool_entry("orphan_tc", "bg result")
bg_t_c1["branch"] = "bg-c1"
merge_q_c1.put(bg_t_c1)

mod_c1 = setup_mod("test_c1", merge_q_c1, experience_c1, [])

result_c1 = mod_c1.drain_merge_queue()
test("C1: orphan tool entry merged without supersede", result_c1 == 1)
test("C1: no superseded_by on orphan tool entry", "superseded_by" not in mod_c1.experience[-1],
     f"keys={mod_c1.experience[-1].keys()}")

# C2: Multiple background tool calls, some duplicate some not
experience_c2 = []
merge_q_c2 = queue.Queue()

# Foreground: send(channel=test) and nop()
fg_c2 = make_assistant_entry([
    {"id": "fg_c2a", "name": "send", "args": '{"channel":"test"}'},
    {"id": "fg_c2b", "name": "nop", "args": '{}'},
])
fg_t_c2a = make_tool_entry("fg_c2a", "send result")
fg_t_c2b = make_tool_entry("fg_c2b", "nop result")
experience_c2 = [fg_c2, fg_t_c2a, fg_t_c2b]

# Background: send(channel=test) [DUPLICATE] and memory() [NEW]
bg_c2 = make_assistant_entry([
    {"id": "bg_c2a", "name": "send", "args": '{"channel":"test"}'},
    {"id": "bg_c2b", "name": "memory", "args": '{"action":"read"}'},
])
bg_t_c2a = make_tool_entry("bg_c2a", "bg send result")
bg_t_c2b = make_tool_entry("bg_c2b", "bg memory result")
bg_t_c2a["branch"] = "bg-c2"
bg_t_c2b["branch"] = "bg-c2"
merge_q_c2.put(bg_c2)
merge_q_c2.put(bg_t_c2a)
merge_q_c2.put(bg_t_c2b)

mod_c2 = setup_mod("test_c2", merge_q_c2, experience_c2, [])

result_c2 = mod_c2.drain_merge_queue()
test("C2: 3 entries merged (1 assistant + 2 tool)", result_c2 == 3, f"got {result_c2}")
# Check the tool entries
merged_entries = mod_c2.experience[-3:]  # last 3 are the merged ones
# Find the tool entries among merged
merged_tools = [e for e in merged_entries if e.get("role") == "tool"]
test("C2: 2 merged tool entries", len(merged_tools) == 2)
# send duplicate should have superseded_by
send_entry = [e for e in merged_tools if "superseded_by" in e]
test("C2: exactly 1 tool has superseded_by (the duplicate send)", len(send_entry) == 1,
     f"found {len(send_entry)} with superseded_by")
if send_entry:
    test("C2: superseded_by points to index 1 (first fg send tool result)",
         send_entry[0].get("superseded_by") == "1",
         f"got {send_entry[0].get('superseded_by')}")

# C3: System/error markers are NOT annotated (only role=tool entries)
experience_c3 = []
merge_q_c3 = queue.Queue()

fg_c3 = make_assistant_entry([{"id": "fg_c3", "name": "send", "args": '{"channel":"test"}'}])
fg_t_c3 = make_tool_entry("fg_c3", "fg result")
experience_c3 = [fg_c3, fg_t_c3]

# Background pushes an error marker (not a tool entry)
error_marker = {
    "role": "system",
    "content": "[BACKGROUND_BRANCH_ERROR] branch_id=bg-xxx error=TestError: test",
    "branch": "bg-xxx",
    "error": True,
    "error_type": "TestError",
    "error_message": "test",
}
merge_q_c3.put(error_marker)

mod_c3 = setup_mod("test_c3", merge_q_c3, experience_c3, [])

result_c3 = mod_c3.drain_merge_queue()
test("C3: system marker merged without supersede", result_c3 == 1)
test("C3: no superseded_by on system marker", "superseded_by" not in mod_c3.experience[-1],
     f"keys={mod_c3.experience[-1].keys()}")

# C4: save_experience called exactly once per drain with entries
save_count_c4 = []
experience_c4 = []
merge_q_c4 = queue.Queue()
merge_q_c4.put({"role": "system", "content": "marker1", "branch": "bg-1"})
merge_q_c4.put({"role": "system", "content": "marker2", "branch": "bg-2"})

mod_c4 = setup_mod("test_c4", merge_q_c4, experience_c4, save_count_c4)

mod_c4.drain_merge_queue()
test("C4: save_experience called once for batch of 2", len(save_count_c4) == 1,
     f"save called {len(save_count_c4)} times")

# C5: Mixed batch — assistant, tool(dup), tool(non-dup), system marker
experience_c5 = []
merge_q_c5 = queue.Queue()

fg_c5 = make_assistant_entry([
    {"id": "fg_c5a", "name": "send", "args": '{"channel":"test"}'},
    {"id": "fg_c5b", "name": "memory", "args": '{"action":"write"}'},
])
fg_t_c5a = make_tool_entry("fg_c5a", "send result")
fg_t_c5b = make_tool_entry("fg_c5b", "memory result")
experience_c5 = [fg_c5, fg_t_c5a, fg_t_c5b]

# Background: send(channel=test) [DUP], memory(action=read) [NOT DUP], error marker
bg_c5 = make_assistant_entry([
    {"id": "bg_c5a", "name": "send", "args": '{"channel":"test"}'},
    {"id": "bg_c5b", "name": "memory", "args": '{"action":"read"}'},
])
bg_t_c5a = make_tool_entry("bg_c5a", "bg send result")
bg_t_c5b = make_tool_entry("bg_c5b", "bg memory result")
bg_t_c5a["branch"] = "bg-c5"
bg_t_c5b["branch"] = "bg-c5"
error_c5 = {
    "role": "system",
    "content": "[BACKGROUND_BRANCH_ERROR] something",
    "branch": "bg-c5",
    "error": True,
}
merge_q_c5.put(bg_c5)
merge_q_c5.put(bg_t_c5a)
merge_q_c5.put(bg_t_c5b)
merge_q_c5.put(error_c5)

mod_c5 = setup_mod("test_c5", merge_q_c5, experience_c5, [])

result_c5 = mod_c5.drain_merge_queue()
test("C5: 5 entries merged (1 assistant + 2 tool + 1 system + 1... wait)",
     result_c5 == 4, f"got {result_c5}")
# Find the tool entries
all_exp = mod_c5.experience
merged_part = all_exp[3:]  # first 3 are fg
merged_tools = [e for e in merged_part if e.get("role") == "tool"]
test("C5: 2 merged tool entries", len(merged_tools) == 2, f"got {len(merged_tools)}")
superseded = [e for e in merged_tools if "superseded_by" in e]
test("C5: 1 tool with superseded_by (send dup)", len(superseded) == 1, f"got {len(superseded)}")
if superseded:
    test("C5: superseded_by = '1' (fg send tool at index 1)",
         superseded[0].get("superseded_by") == "1",
         f"got {superseded[0].get('superseded_by')}")

# --- Group D: Source inspection ---
print("\n--- Group D: Source inspection ---")

# D1: py_compile
import py_compile
try:
    py_compile.compile(ITER_PATH, doraise=True)
    test("D1: py_compile passes", True)
except py_compile.PyCompileError as e:
    test("D1: py_compile passes", False, str(e))

# D2: _build_tool_call_map is defined
test("D2: _build_tool_call_map defined in source", "def _build_tool_call_map" in source)

# D3: drain_merge_queue has supersede logic
test("D3: superseded_by in drain_merge_queue source", "superseded_by" in source)

# D4: existing_tool_index in drain_merge_queue
test("D4: existing_tool_index in source", "existing_tool_index" in source)

# D5: merged_call_lookup in drain_merge_queue
test("D5: merged_call_lookup in source", "merged_call_lookup" in source)

# D6: flag-off — drain_merge_queue only called behind ITER_CONCURRENCY_ENABLED guard
# Check that both drain calls are guarded
import re
drain_guards = re.findall(r'if ITER_CONCURRENCY_ENABLED:\s*\n\s*drain_merge_queue\(\)', source)
test("D6: drain_merge_queue calls are flag-guarded (2 found)", len(drain_guards) == 2,
     f"found {len(drain_guards)}")

# D7: Diff is pure additions + drain_merge_queue replacement
# (verified by structural analysis: new function + modified function)
test("D7: _build_tool_call_map is new (not in old backup)",
     "def _build_tool_call_map" not in open(
         ITER_PATH.replace("iter.py", "iter.py.pre-m3-3.4-20260905T0324"), encoding="utf-8"
     ).read())

# --- Group E: Regression — basic drain still works ---
print("\n--- Group E: Regression — basic drain ---")

# E1: Simple tagged merge (no duplicates possible)
experience_e1 = [{"role": "user", "content": "hello"}]
merge_q_e1 = queue.Queue()
entry_e1 = {"role": "system", "content": "bg update", "branch": "bg-e1"}
merge_q_e1.put(entry_e1)

mod_e1 = setup_mod("test_e1", merge_q_e1, experience_e1, [])

result_e1 = mod_e1.drain_merge_queue()
test("E1: simple merge returns 1", result_e1 == 1)
test("E1: entry has branch tag", mod_e1.experience[1].get("branch") == "bg-e1")

# E2: Empty queue is no-op
merge_q_e2 = queue.Queue()
exp_e2 = [{"role": "user", "content": "test"}]
mod_e2 = setup_mod("test_e2", merge_q_e2, exp_e2, [])

result_e2 = mod_e2.drain_merge_queue()
test("E2: empty queue returns 0", result_e2 == 0)
test("E2: experience unchanged", len(mod_e2.experience) == 1)

# ─── Summary ─────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print(f"RESULTS: {passed} passed, {failed} failed")
print("=" * 70)
sys.exit(1 if failed > 0 else 0)
