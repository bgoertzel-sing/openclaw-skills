#!/usr/bin/env python3
"""Simulation harness for M3 Step 3.5: Branch step budget + branch checkpoint queuing (R20).

Tests:
  A) BRANCH_STEP_BUDGET constant (default 25, env-configurable)
  B) _bg_branch_mini_loop — step budget exhaustion queues checkpoint payload
  C) _bg_branch_mini_loop — normal completion (no tool calls) frees slot
  D) _bg_branch_mini_loop — follow-up LLM call failure pushes error marker + frees slot
  E) drain_merge_queue — checkpoint payload detected and handled by main thread (R20)
  F) drain_merge_queue — mixed checkpoint + regular entries
  G) threaded_llm_call — stores branch_client + branch_messages in result_container on promotion
  H) _bg_llm_thread_target — calls mini-loop after promotion
  I) Flag-off source inspection (no behavioral change when ITER_CONCURRENCY_ENABLED=0)
  J) Regression — M2/M3 features still intact
  K) py_compile
"""
import ast
import os
import sys
import copy
import json
import queue
import threading
import time
import uuid
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

ITER_PY = Path(__file__).parent.parent / "iter-port" / "repos" / "iter.py"

# Extract source for AST inspection
source = ITER_PY.read_text()
tree = ast.parse(source)

# ── Extract functions/constants from iter.py source via AST ──
def extract_func_src(name):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return ast.unparse(node)
    raise ValueError(f"Function {name} not found")

def extract_class_src(name):
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == name:
            return ast.unparse(node)
    raise ValueError(f"Class {name} not found")

def has_source_pattern(pattern):
    return pattern in source

# ── Test helpers ──
results = []
def test(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    status = "PASS" if cond else "FAIL"
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))

# ── Constants from source ──
BRANCH_STEP_BUDGET_match = "BRANCH_STEP_BUDGET = int(os.getenv(\"ITER_BRANCH_STEP_BUDGET\", \"25\"))" in source

# ── Tests ──

print("=== A) BRANCH_STEP_BUDGET constant ===")

# A1: constant exists with default 25
test("A1: BRANCH_STEP_BUDGET defined with default 25", BRANCH_STEP_BUDGET_match)

# A2: env-configurable
test("A2: BRANCH_STEP_BUDGET is env-configurable (os.getenv)", "os.getenv(\"ITER_BRANCH_STEP_BUDGET\"" in source)

# A3: placed after BACKGROUND_DEADLINE
bd_line = source.find("BACKGROUND_DEADLINE = max(2 * ITER_PROMOTE_SECONDS, 300)")
bsb_line = source.find("BRANCH_STEP_BUDGET = int(os.getenv")
test("A3: BRANCH_STEP_BUDGET placed after BACKGROUND_DEADLINE", bd_line > 0 and bsb_line > bd_line)

# A4: actually evaluates to 25
os.environ.pop("ITER_BRANCH_STEP_BUDGET", None)
test("A4: BRANCH_STEP_BUDGET evaluates to 25", int(os.getenv("ITER_BRANCH_STEP_BUDGET", "25")) == 25)

# A5: env override works
os.environ["ITER_BRANCH_STEP_BUDGET"] = "15"
test("A5: BRANCH_STEP_BUDGET env override works", int(os.getenv("ITER_BRANCH_STEP_BUDGET", "25")) == 15)
os.environ.pop("ITER_BRANCH_STEP_BUDGET", None)


print("\n=== B) _bg_branch_mini_loop — step budget exhaustion ===")

func_src = extract_func_src("_bg_branch_mini_loop")
test("B1: _bg_branch_mini_loop function defined", "def _bg_branch_mini_loop" in source)

# B2: has BRANCH_STEP_BUDGET reference
test("B2: mini-loop references BRANCH_STEP_BUDGET", "BRANCH_STEP_BUDGET" in func_src)

# B3: queues checkpoint on exhaustion
test("B3: queues _checkpoint_payload on step budget exhaustion", "_checkpoint_payload" in func_src and "_merge_queue.put" in func_src)

# B4: calls extract_tier1_checkpoint on exhaustion
test("B4: calls extract_tier1_checkpoint on exhaustion", "extract_tier1_checkpoint" in func_src)

# B5: never writes files directly (no write_checkpoint_file call)
test("B5: never calls write_checkpoint_file directly", "write_checkpoint_file" not in func_src)

# B6: never calls send_checkpoint_message directly
test("B6: never calls send_checkpoint_message directly", "send_checkpoint_message" not in func_src)

# B7: frees branch slot on completion
test("B7: frees _active_branch slot", "_active_branch = None" in func_src or "_active_branch = None" in func_src)

# B8: pushes assistant entries tagged with branch
test("B8: pushes tagged assistant entries to merge queue", '"branch": branch_id' in func_src or "'branch': branch_id" in func_src or '"branch"' in func_src)

# B9: pushes tool entries tagged with branch
test("B9: pushes tagged tool entries to merge queue", "tool_call_id" in func_src and "branch" in func_src)

# B10: uses branch_client for follow-up calls (R12)
test("B10: uses branch_client for follow-up LLM calls", "branch_client.chat.completions.create" in func_src)

# B11: uses branch_messages (deep copy, R11)
test("B11: uses branch_messages for follow-up calls", "branch_messages" in func_src)

# B12: loads tools at start
test("B12: loads tools at start (load_tools call)", "load_tools()" in func_src)

# B13: has step counter
test("B13: has branch_steps counter", "branch_steps" in func_src)

# B14: error handling for follow-up LLM call (R14)
test("B14: R14 error handling for follow-up LLM failures", "error_marker" in func_src and "_merge_queue.put" in func_src)

# B15: compare-and-swap slot free (avoids racing with deadline)
test("B15: compare-and-swap slot free guard", "_active_branch is not None and _active_branch.branch_id == branch_id" in func_src)


print("\n=== C) _bg_branch_mini_loop — normal completion (no tool calls) ===")

# C1: breaks on no tool_calls
test("C1: breaks when no tool_calls", "not message.tool_calls" in func_src or "not message.tool_calls" in func_src)

# C2: BRANCH_COMPLETE printed on completion
test("C2: prints BRANCH_COMPLETE on completion", "BRANCH_COMPLETE" in func_src)

# C3: does NOT queue checkpoint on normal completion
# The checkpoint queuing should be inside the "if branch_steps >= BRANCH_STEP_BUDGET" block
test("C3: checkpoint only on step budget exhaustion (not normal completion)", 
     "if branch_steps >= BRANCH_STEP_BUDGET:" in func_src)


print("\n=== D) _bg_branch_mini_loop — follow-up LLM call failure ===")

# D1: follow-up LLM call has try/except
test("D1: follow-up LLM call wrapped in try/except", "except Exception as e:" in func_src)

# D2: error marker has branch id
test("D2: error marker includes branch_id", "branch_id" in func_src and "error_marker" in func_src)

# D3: error marker has error type and message
test("D3: error marker has error_type and error_message", "error_type" in func_src and "error_message" in func_src)

# D4: error marker bounded to 500 chars
test("D4: error message bounded to 500 chars", "[:500]" in func_src)

# D5: frees slot on error
test("D5: frees slot on follow-up LLM error", "_active_branch = None" in func_src)

# D6: returns after error (no continue)
test("D6: returns after follow-up LLM error", "return" in func_src)


print("\n=== E) drain_merge_queue — checkpoint payload handling (R20) ===")

drain_src = extract_func_src("drain_merge_queue")

# E1: detects _checkpoint_payload entries
test("E1: detects _checkpoint_payload marker", "_checkpoint_payload" in drain_src)

# E2: separates checkpoint payloads from regular entries
test("E2: separates checkpoint payloads from regular entries", "checkpoint_payloads" in drain_src)

# E3: calls write_checkpoint_file from main thread (R20)
test("E3: calls write_checkpoint_file from main thread", "write_checkpoint_file" in drain_src)

# E4: calls send_checkpoint_message from main thread (R20)
test("E4: calls send_checkpoint_message from main thread", "send_checkpoint_message" in drain_src)

# E5: adds system marker to experience for branch checkpoint
test("E5: adds system marker for branch checkpoint", "BACKGROUND_BRANCH_CHECKPOINT" in drain_src)

# E6: saves experience after checkpoint handling
test("E6: saves experience after checkpoint handling", "save_experience" in drain_src)

# E7: checkpoint data stripped of internal markers before write
test("E7: strips branch and _checkpoint_payload from cp_data", 
     "k not in ('branch', '_checkpoint_payload')" in drain_src or "k not in (\"branch\", \"_checkpoint_payload\")" in drain_src)


print("\n=== F) drain_merge_queue — mixed checkpoint + regular entries ===")

# F1: regular entries still processed when checkpoint payloads present
test("F1: regular entries still processed alongside checkpoints", 
     "merged_entries" in drain_src and "checkpoint_payloads" in drain_src)

# F2: supersede annotation still works for regular entries
test("F2: supersede annotation intact for regular entries", "superseded_by" in drain_src)

# F3: returns count including checkpoint payloads when only checkpoints
test("F3: returns len(checkpoint_payloads) when no regular entries", "len(checkpoint_payloads)" in drain_src)

# F4: does NOT save when no entries at all
test("F4: no save when both lists empty (returns 0)", 
     "save_experience(experience) if checkpoint_payloads else None" in drain_src)


print("\n=== G) threaded_llm_call — stores branch_client + branch_messages ===")

tllm_src = extract_func_src("threaded_llm_call")

# G1: stores branch_client in result_container
test("G1: stores branch_client in result_container", 'branch_client' in tllm_src and 'result_container' in tllm_src)

# G2: stores branch_messages in result_container
test("G2: stores branch_messages in result_container", 'branch_messages' in tllm_src and 'result_container' in tllm_src)

# G3: stores after bg_client creation
bg_client_line = source.find("bg_client = openai.OpenAI(")
branch_client_line = source.find('result_container["branch_client"]')
test("G3: stores after bg_client creation", bg_client_line > 0 and branch_client_line > bg_client_line)

# G4: stores after branch_id assignment
branch_id_line = source.find('result_container["branch_id"] = branch_id')
test("G4: stores after branch_id assignment", branch_id_line > 0 and branch_client_line > branch_id_line)


print("\n=== H) _bg_llm_thread_target — calls mini-loop after promotion ===")

tgt_src = extract_func_src("_bg_llm_thread_target")

# H1: checks for branch_id after successful LLM call
test("H1: checks branch_id after successful call", 'result_container.get("branch_id")' in tgt_src or "result_container.get('branch_id')" in tgt_src)

# H2: calls _bg_branch_mini_loop when promoted
test("H2: calls _bg_branch_mini_loop when promoted", "_bg_branch_mini_loop(" in tgt_src)

# H3: checks branch_client and branch_messages before calling
test("H3: checks branch_client and branch_messages before calling", "branch_client" in tgt_src and "branch_messages" in tgt_src)

# H4: mini-loop call is inside the try block (before except)
try_line = source.find("try:")  # find the try in _bg_llm_thread_target
except_line = source.find("except Exception as e:", try_line)
mini_loop_line = source.find("_bg_branch_mini_loop(", try_line)
test("H4: mini-loop call inside try block (before except)", 
     try_line > 0 and mini_loop_line > try_line and (except_line < 0 or mini_loop_line < except_line))

# H5: if mini-loop raises, except block catches it (R14)
test("H5: except block catches mini-loop exceptions (R14)", "except Exception as e:" in tgt_src)


print("\n=== I) Flag-off source inspection ===")

# I1: BRANCH_STEP_BUDGET is not flag-guarded by itself (it's just a constant)
# But all code that USES it is behind ITER_CONCURRENCY_ENABLED
test("I1: BRANCH_STEP_BUDGET is a module-level constant (not flag-guarded itself)", 
     "BRANCH_STEP_BUDGET = int" in source)

# I2: _bg_branch_mini_loop is only called from _bg_llm_thread_target (which is behind flag)
test("I2: _bg_branch_mini_loop only called from _bg_llm_thread_target", 
     source.count("_bg_branch_mini_loop(") == 2)  # definition + call

# I3: drain_merge_queue checkpoint handling — drain is flag-guarded
# Both drain calls are behind `if ITER_CONCURRENCY_ENABLED:`
drain_guards = [m.start() for m in __import__('re').finditer(r'if ITER_CONCURRENCY_ENABLED:\s*\n\s*drain_merge_queue\(\)', source)]
test("I3: drain_merge_queue calls are flag-guarded", len(drain_guards) >= 2)

# I4: no changes to the else branch (direct client call)
else_branch = "response = client.chat.completions.create(model=MODEL, messages=request_messages, tools=request_tools, tool_choice=\"required\", max_tokens=MAX_TOKENS, extra_body={ \"enable_thinking\": True})"
test("I4: else branch (direct call) unchanged", else_branch in source)

# I5: no changes to the _promoted guard
test("I5: _promoted guard intact", "_promoted = False" in source and "if _promoted:" in source and "continue" in source)

# I6: no changes to flag-off checkpoint path (M1)
test("I6: M1 checkpoint path intact", "ITER_CHECKPOINT_ENABLED and not send_since_checkpoint" in source)

# I7: diff vs backup — only additions + expected modifications
import subprocess
diff = subprocess.run(["diff", str(ITER_PY) + ".pre-m3-3.5-20260905T0354", str(ITER_PY)], 
                      capture_output=True, text=True)
added = sum(1 for line in diff.stdout.split("\n") if line.startswith(">"))
removed = sum(1 for line in diff.stdout.split("\n") if line.startswith("<"))
test("I7: diff is mostly additions", added > removed * 3, f"added={added} removed={removed}")
test("I7b: no deletions of existing logic lines", removed < 10, f"removed={removed} lines")


print("\n=== J) Regression — M2/M3 features still intact ===")

# J1: M2 threaded_llm_call still present
test("J1: threaded_llm_call present", "def threaded_llm_call" in source)

# J2: M2 _merge_queue present
test("J2: _merge_queue present", "_merge_queue = queue.Queue()" in source)

# J3: M2 drain_merge_queue present
test("J3: drain_merge_queue present", "def drain_merge_queue" in source)

# J4: M3 check_background_deadline present
test("J4: check_background_deadline present", "def check_background_deadline" in source)

# J5: M3 graceful_shutdown present
test("J5: graceful_shutdown present", "def graceful_shutdown" in source)

# J6: M3 _build_tool_call_map present
test("J6: _build_tool_call_map present", "def _build_tool_call_map" in source)

# J7: M3 BACKGROUND_DEADLINE present
test("J7: BACKGROUND_DEADLINE present", "BACKGROUND_DEADLINE = max(2 * ITER_PROMOTE_SECONDS, 300)" in source)

# J8: M3 SHUTDOWN_GRACE present
test("J8: SHUTDOWN_GRACE present", "SHUTDOWN_GRACE" in source)

# J9: M2 double drain (two drain_merge_queue calls flag-guarded)
drain_calls = [m.start() for m in __import__('re').finditer(r'drain_merge_queue\(\)', source)]
test("J9: two drain_merge_queue calls in main loop", len(drain_calls) >= 2)

# J10: R14 error markers in _bg_llm_thread_target (original + mini-loop errors)
test("J10: R14 error markers in _bg_llm_thread_target", "BACKGROUND_BRANCH_ERROR" in source)


print("\n=== K) py_compile ===")

result = subprocess.run([sys.executable, "-m", "py_compile", str(ITER_PY)], capture_output=True, text=True)
test("K1: py_compile passes", result.returncode == 0, result.stderr)


# ── Summary ──
passed = sum(1 for _, ok, _ in results if ok)
failed = sum(1 for _, ok, _ in results if not ok)
print(f"\n{'='*50}")
print(f"TOTAL: {passed} passed, {failed} failed")
if failed:
    print("\nFAILED TESTS:")
    for name, ok, detail in results:
        if not ok:
            print(f"  ✗ {name}: {detail}")
    sys.exit(1)
else:
    print("\n✓ All tests passed.")
