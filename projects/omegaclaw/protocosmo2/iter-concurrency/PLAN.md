# Iter Concurrency Worker Plan (M1→M4)

**Goal:** Implement the v4 spec (`projects/omegaclaw/docs/turn-budget-continuation-design-spec-v4.md`)
in the live ProtoCosmo2 iter loop, milestone by milestone, with tests and evidence.

**Target file:** `projects/omegaclaw/protocosmo2/iter-port/repos/iter.py` (live, PID-managed by supervisor)
**Spec:** `projects/omegaclaw/docs/turn-budget-continuation-design-spec-v4.md`
**Status board:** this file — the worker updates checkboxes + appends a log entry each run.

## Rules for the worker

- One step per run. Do the next unchecked item, test it, update this file, commit, stop.
- All loop changes flag-guarded; flag-off path must be byte-identical behavior.
- Back up iter.py before each structural change: `cp iter.py iter.py.pre-<tag>-<timestamp>`.
- Verify with `python3 -m py_compile iter.py` after every edit.
- Do NOT restart the live supervisor unless the step explicitly says to; restarts are
  announced in the log so ZeroBot can coordinate.
- Never touch credentials, canary config, or the outer transport files.
- If blocked, log the blocker precisely in this file and stop — do not improvise scope.

## Steps

### M1 — Mechanical forced checkpoint
- [x] 1.1 Add flag-guarded `ITER_CHECKPOINT_ENABLED` (env, default on) + Tier-1 mechanical
      checkpoint at MAX_FAST_STEPS with no send: extract last N=5 tool calls (names +
      200-char truncated outputs), prompt hash, step count, timestamps.
- [x] 1.2 Atomic checkpoint file write (temp+rename) to `checkpoints/<session>/<ts>.json`
      BEFORE any send, per v4 write-ordering.
- [x] 1.3 Human-readable checkpoint via normal `send` path after file write.
- [x] 1.4 Tests: py_compile; a provider-free simulation harness run showing checkpoint
      fires at step 50; flag-off path diff-identical.
- [x] 1.5 Log + commit. Announce restart needed.

### M2 — Time-based promotion core (flag `ITER_CONCURRENCY_ENABLED`, default OFF)
- [x] 2.1 Threaded LLM call wrapper with deadline T (env `ITER_PROMOTE_SECONDS`, default 30):
      foreground first; on T expiry, deep copy messages, separate OpenAI client, branch id.
- [x] 2.2 Merge queue (queue.Queue) + double drain (top of loop AND before building messages);
      single-writer discipline; tagged entries `"branch": "bg-<id>"`.
- [x] 2.3 Tests: py_compile; offline harness — fake slow call detaches, fake chat answered,
      tagged merge; kill -9 mid-merge simulation leaves experience file valid JSON.
- [ ] 2.4 Log + commit. Do not enable flag live yet.

### M3 — Hardening
- [ ] 3.1 BACKGROUND_DEADLINE (default max(2T,300s)): abandon + marker + slot frees.
- [ ] 3.2 try/except wrapper → error markers onto merge queue.
- [ ] 3.3 Shutdown protocol: SIGTERM/SIGINT stop event, 5s grace, drain, save, exit; daemon threads.
- [ ] 3.4 Duplicate-tool supersede annotation `"superseded_by"`.
- [ ] 3.5 Branch step budget (25) + branch checkpoint queuing to main thread (single-writer).
- [ ] 3.6 Tests for 3.1–3.5. Log + commit.

### M4 — Validation + calibration
- [ ] 4.1 Extract USAGE/latency distribution from supervisor log; confirm bimodal split;
      recommend T.
- [ ] 4.2 Enable flag on live bot; soak; end-to-end Telegram test (slow task + mid-task chat).
- [ ] 4.3 Final report.

## Log

- 2026-09-04 14:25 PDT — Plan created by ZeroBot. Worker cron `iter-concurrency-worker`
  every 30 min. M1 in progress.
- 2026-09-04 14:27 PDT — **Step 1.1 completed.** Added `import hashlib`, `ITER_CHECKPOINT_ENABLED`
  flag (env, default ON), `CHECKPOINT_TOOL_SNAPSHOT=5`, `CHECKPOINT_OUTPUT_CHARS=200` constants,
  and `extract_tier1_checkpoint()` function. Function extracts: checkpoint_type, session_id,
  step_count, timestamp + ISO timestamp, prompt_hash (SHA-256[:16] of prompt.txt), and
  tool_snapshot (last N tool-call entries with tool_name + 200-char truncated output). Called
  in the `elif autonomous_steps >= MAX_FAST_STEPS:` branch, flag-guarded with `not send_since_checkpoint`.
  Flag-off: only adds `_checkpoint_data = None` (unused local, no-op); existing reset + slow_wait
  path unchanged. Evidence: `py_compile` OK; standalone function test with mock experience list
  passed all assertions (2 tool calls, correct names, 200-char truncation, prompt_hash present).
  Backup: `iter.py.pre-m1-1.1-20260904-2124`. Git commit to follow. No restart needed yet
  (checkpoint data is only extracted+printed; file write + send come in steps 1.2–1.3).
- 2026-09-04 14:55 PDT — **Step 1.2 completed.** Added `CHECKPOINT_DIR = Path("checkpoints")` constant
  and `write_checkpoint_file()` function: creates `checkpoints/<session_id>/` dir, writes JSON to
  `<ts>.json.tmp` then `os.replace` to `<ts>.json` atomically. Second-resolution timestamp with UUID4
  suffix fallback for same-second collisions. Returns `Path` on success, `None` on failure (never raises —
  prints `CHECKPOINT_FILE_WRITE_FAILED` and cleans up temp file). Called in the
  `ITER_CHECKPOINT_ENABLED and not send_since_checkpoint` branch after `extract_tier1_checkpoint()`,
  before the (future) send from step 1.3. Flag-off: only adds `_checkpoint_path = None` (unused local,
  no-op); existing `autonomous_steps = 0; pending_event_append = slow_wait_for_input()` unchanged.
  Backup: `iter.py.pre-m1-1.2-20260904-2154`. `checkpoints/` added to `.gitignore`.
  Evidence: `py_compile` OK; standalone tests passed — (1) atomic write to correct path with correct
  content, (2) write-failure (read-only dir) returns None without crash, (3) flag-off creates no files.
  Git commit: `2f79cab`. No restart needed (file write is a no-op to the running loop until step 1.3
  adds the send).
- 2026-09-04 15:24 PDT — **Step 1.3 completed.** Added `CHECKPOINT_CHANNEL` env constant (default
  `protocosmo2`), `format_checkpoint_message()` function (formats Tier-1 data into a concise
  human-readable summary: step count, last N tool calls with truncated outputs, checkpoint file path,
  session id), and `send_checkpoint_message()` function (calls `invoke_dynamic` on `tools/send.py`
  with `channel=CHECKPOINT_CHANNEL`; best-effort, never raises — prints `CHECKPOINT_SEND_*` diagnostics
  on failure). Called in the checkpoint branch AFTER `write_checkpoint_file()` per v4 write-ordering
  (R2: file before send). Updated the `CHECKPOINT_FILE_WRITE_FAILED` log message (removed
  "in step 1.3" since step 1.3 is now implemented). Flag-off: the `else` branch is unchanged
  (`_checkpoint_data = None; _checkpoint_path = None`); new functions are defined but never called;
  `CHECKPOINT_CHANNEL` is set but never read. Diff vs pre-step backup confirms only additions +
  the one log-message wording update. Backup: `iter.py.pre-m1-1.3-20260904T2224`.
  Evidence: `py_compile` OK; standalone tests passed — (1) format_checkpoint_message with data
  produces correct output with step count, tool names, file path, session; (2) empty snapshot +
  no file path produces fallback text; (3) flag-off else-block byte-identical in source;
  (4) send call positioned after file write in source ordering; (5) CHECKPOINT_CHANNEL env-gated
  with protocosmo2 default; (6) send_checkpoint_message has try/except guard. Git commit to follow.
  **Restart needed:** yes — the live supervisor must restart iter.py for the checkpoint send
  to take effect. Until restart, the live loop still runs the pre-1.3 code (file write but no
  human-readable send). ZeroBot should coordinate the restart.
- 2026-09-04 15:56 PDT — **Step 1.4 completed.** Created provider-free simulation harness at
  `iter-concurrency/sim_harness_1.4.py`. The harness uses AST to extract the actual checkpoint
  functions (`extract_tier1_checkpoint`, `write_checkpoint_file`, `format_checkpoint_message`,
  `send_checkpoint_message`) from iter.py source — tests the real code, not copies. Five tests:
  (a) Flag ON — checkpoint fires at simulated step 50: file written atomically to
  `checkpoints/<session>/<ts>.json`, no .tmp left behind, file content matches returned data,
  send called with correct message containing CHECKPOINT marker, step count, tool names, file path,
  session id. (b) Flag OFF — no file, no send, else-branch noop. (c) Flag ON + send_since_checkpoint=True
  — checkpoint skipped (else branch). (d) Flag-off diff-identical — diff vs pre-M1 backup confirms
  all changes are pure additions (new import, constants, functions, if/else branch); no existing
  lines modified; else-branch only assigns None to two unused locals; core reset+slow_wait lines
  unchanged. (e) Write-failure resilience — read-only session dir forces write_checkpoint_file to
  return None without crash; send_checkpoint_message still called (best-effort).
  Evidence: `py_compile` OK; `python3 sim_harness_1.4.py` → 5 passed, 0 failed.
  Backup: `iter.py.pre-m1-1.4-20260904T2254` (no structural change to iter.py in this step —
  harness is a new file outside the repo). Git commit: `06a897f` (in research-agent root repo —
  both PLAN.md and harness file committed there since iter.py itself was not modified).
  **No restart needed** — this step only adds tests, no code change to iter.py.
- 2026-09-04 16:24 PDT — **Step 1.5 completed.** M1 milestone fully checked off.
  All four implementation steps (1.1–1.4) are done and committed. This step is the
  administrative close-out: checking the 1.5 box, appending this log entry, and
  committing the updated PLAN.md to the iter-port repo.
  **Evidence:** `python3 -m py_compile iter.py` → OK (re-verified). Git log in
  iter-port repo: `2f79cab` (1.2), `c26da12` (1.3); research-agent root repo:
  `1ef96de` (1.1 log), `151ffc8` (1.4 harness). Pre-step backups preserved:
  `iter.py.pre-m1-1.1-20260904-2124`, `iter.py.pre-m1-1.2-20260904-2154`,
  `iter.py.pre-m1-1.3-20260904T2224`, `iter.py.pre-m1-1.4-20260904T2254`.
  **Restart needed:** yes — same as announced in step 1.3. The live supervisor
  must restart iter.py for the Tier-1 checkpoint send (step 1.3) to take effect.
  Until restart, the live loop runs pre-1.3 code (file write but no human-readable
  send). ZeroBot should coordinate the restart. No restart performed by this worker.
  **M1 complete.** Next unchecked step: M2 step 2.1 (threaded LLM call wrapper
  with deadline T, flag `ITER_CONCURRENCY_ENABLED`, default OFF).
- 2026-09-04 16:54 PDT — **Step 2.1 completed.** Added `import copy`, `import threading`, `ITER_CONCURRENCY_ENABLED`
  flag (env, default OFF), `ITER_PROMOTE_SECONDS` (env, default 30), `BranchState` class, `_bg_llm_thread_target`
  function, and `threaded_llm_call()` function. `threaded_llm_call` starts the LLM call in a daemon thread,
  joins with timeout T. If the call completes within T: returns `(response, None)` — identical to direct call.
  If T expires: creates `bg-<uuid8>` branch id, `copy.deepcopy(messages)` (R11), separate `openai.OpenAI` client
  with `x-branch-id` header (R12), stores branch in `_active_branch` under `_branch_lock`, returns `(None, BranchState)`.
  Original thread continues running (R9: no token waste). Main loop change: `_promoted = False` before inner loop;
  `if ITER_CONCURRENCY_ENABLED:` calls `threaded_llm_call`, on `None` response sets `_promoted=True` and breaks;
  `else:` branch is the exact original `client.chat.completions.create(...)` call. After inner loop: `if _promoted:
  continue` resumes receive() polling (no-op when flag off). Flag-off diff vs pre-step backup confirms all changes
  are pure additions (2 imports, 2 constants, 1 class, 2 functions, `_promoted = False`, if/else branch, `if
  _promoted: continue`); the `else:` branch is byte-identical to the original direct call; `_promoted` is always
  False when flag is off.
  Backup: `iter.py.pre-m2-2.1-20260904T2354`.
  Evidence: `py_compile` OK; `python3 sim_harness_2.1.py` → 23 passed, 0 failed. Tests cover: (1) fast call returns
  within T with correct response; (2) slow call promotes after T with `bg-` branch id and live thread; (3) deep
  copy isolation — mutating original messages does not affect branch copy (R11); (4) separate client created (R12);
  (5) thread is daemon (R17 partial); (6) `_active_branch` set after promotion; (7) `result_container` populated
  after thread completes; (8) flag-off source inspection — if/else, direct call in else, `_promoted` guard present;
  (9) failed call within T raises exception (caught by outer try/except).
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; the live loop takes the `else:` branch
  which is the original direct call. No behavioral change when flag is off. Next step: 2.2 (merge queue + double
  drain + single-writer discipline + tagged entries).
- 2026-09-05 00:24 PDT — **Step 2.2 completed.** Added `import queue`, `_merge_queue = queue.Queue()` (R15 merge
  queue), and `drain_merge_queue()` function. The function pops all entries non-blocking from
  `_merge_queue`, ensures each has a `"branch"` tag (R16 — fallback `"unknown"` if missing), appends to
  `experience`, and calls `save_experience()` (single-writer: only the main loop thread calls this — R6).
  Non-dict entries are skipped. Returns count of merged entries; 0 when queue is empty (pure no-op).
  Double drain placed in the main loop: (a) after cleanup, before `history_checkpoint = len(experience)`
  and before `receive()`; (b) immediately before `request_messages = [...]` construction. Both drain calls
  are flag-guarded by `if ITER_CONCURRENCY_ENABLED:` (default OFF). Flag-off: `drain_merge_queue()` is
  never called; `_merge_queue` is never populated; `_merge_queue` and `drain_merge_queue` are defined but
  unused — behavior is byte-identical. Diff vs pre-step backup confirms all changes are pure additions:
  1 import, 1 constant, 1 function definition, 2 flag-guarded drain calls (3 lines each).
  Backup: `iter.py.pre-m2-2.2-20260905T0024`.
  Evidence: `py_compile` OK; 4 standalone tests passed — (1) empty queue drain is no-op, (2) tagged
  entries merge correctly with branch ids, (3) untagged entry gets fallback `"unknown"` tag, (4) non-dict
  entries are skipped; AST source inspection confirms both `drain_merge_queue()` calls are guarded by
  `if ITER_CONCURRENCY_ENABLED:` (lines 512–513 and 561–562).
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; both drain calls are behind the flag
  guard; the live loop never reaches `drain_merge_queue()`. No behavioral change when flag is off.
  Next step: 2.3 (tests — offline harness: fake slow call detaches, fake chat answered, tagged merge,
  kill -9 mid-merge simulation leaves experience file valid JSON).
- 2026-09-04 17:54 PDT — **Step 2.3 completed.** Created offline simulation harness at
  `iter-concurrency/sim_harness_2.3.py`. The harness extracts the real `threaded_llm_call`,
  `drain_merge_queue`, `save_experience`, `BranchState`, and `_bg_llm_thread_target` from iter.py
  source via AST — tests the actual code, not copies. 46 tests in 5 groups:
  **Group A (8 tests):** fake slow call (delay=5s, T=1s) promotes after T with `bg-` branch id,
  daemon thread, still-alive detachment; fast call (delay=0, T=5s) returns within T with correct
  response and no branch.
  **Group B (7 tests):** slow call (3s delay, T=1s) promotes; while branch runs in background,
  foreground handles a fast call (delay=0) and returns immediately; branch thread completes and
  result_container is populated.
  **Group C (11 tests):** 3 tagged entries merge with correct content and branch ids; untagged
  entry gets `"unknown"` fallback; empty queue drain is no-op (returns 0); non-dict entries
  (string, int) are skipped; only valid dict entries merged.
  **Group D (11 tests):** save_experience writes valid JSON to experience.json; partial
  experience.tmp (simulated crash mid-write) leaves experience.json intact (atomic-rename
  guarantee); experience.json unchanged when os.replace not called; save_experience works
  after crash recovery; concurrent push (10 entries from bg thread) + drain + save produces
  valid JSON with all 10 entries and branch tags; partial drain (3 of 5, simulating crash
  mid-merge) produces valid JSON with 3 entries, 2 remain in queue.
  **Group E (9 tests):** py_compile passes; ITER_CONCURRENCY_ENABLED defaults to OFF
  (`"0"`); drain_merge_queue flag-guarded in 2 places (regex match across both indentation
  levels); threaded_llm_call behind `if ITER_CONCURRENCY_ENABLED:`; `_promoted = False` and
  `if _promoted: continue` present; else branch has direct `client.chat.completions.create`;
  `_merge_queue` defined at module level; `drain_merge_queue` defined.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_2.3.py` → 46 passed,
  0 failed.
  No backup needed (test-only step — no structural change to iter.py). No restart needed —
  step 2.3 adds no code to iter.py; all M2 code is behind `ITER_CONCURRENCY_ENABLED` (default
  OFF). Git commit to follow.
  Next step: 2.4 (log + commit; do not enable flag live yet).
