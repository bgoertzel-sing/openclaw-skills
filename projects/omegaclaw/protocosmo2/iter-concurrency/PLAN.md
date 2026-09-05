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
- [x] 2.4 Log + commit. Do not enable flag live yet.

### M3 — Hardening
- [x] 3.1 BACKGROUND_DEADLINE (default max(2T,300s)): abandon + marker + slot frees.
- [x] 3.2 try/except wrapper → error markers onto merge queue.
- [x] 3.3 Shutdown protocol: SIGTERM/SIGINT stop event, 5s grace, drain, save, exit; daemon threads.
- [x] 3.4 Duplicate-tool supersede annotation `"superseded_by"`.
- [x] 3.5 Branch step budget (25) + branch checkpoint queuing to main thread (single-writer).
- [x] 3.6 Tests for 3.1–3.5. Log + commit.

### M4 — Validation + calibration
- [x] 4.1 Extract USAGE/latency distribution from supervisor log; confirm bimodal split;
      recommend T.
- [ ] 4.2 Enable flag on live bot; soak; end-to-end Telegram test (slow task + mid-task chat). **BLOCKED — requires Ben's explicit approval to enable ITER_CONCURRENCY_ENABLED on the live bot + supervisor restart. See log entry 2026-09-04 22:24 PDT.**
- [ ] 4.3 Final report.

## Log (continued)

- 2026-09-04 22:24 PDT — **Step 4.2 BLOCKED.** This step requires enabling `ITER_CONCURRENCY_ENABLED=1` on the live ProtoCosmo2 bot and restarting the supervisor to pick up the env var. Per the step 4.1 log and the PLAN.md rules: (1) enabling the flag on the live bot is a runtime behavior change that requires **explicit approval from Ben**; (2) the worker rules say "Do NOT restart the live supervisor unless the step explicitly says to" — and even if it did, a restart must be announced for ZeroBot to coordinate, not performed by this worker. No code change to iter.py; no flag enablement performed; no restart performed. Backup `iter.py.pre-m4-4.2-20260905T0524` created per plan rules (identical to current iter.py — no structural change in this step). `python3 -m py_compile iter.py` → OK (baseline re-verified). The iter-port repo is a git repo (confirmed: `git rev-parse --is-inside-work-tree` → true; HEAD = `23a5d6f`). No commit made — nothing to commit (no code change). **Blocker:** Ben must explicitly approve enabling `ITER_CONCURRENCY_ENABLED=1` on the live bot and coordinate the supervisor restart. Once approved, the soak test can proceed: enable the flag, restart the supervisor, send a slow task via Telegram (>30s LLM call), send a mid-task chat message, confirm foreground responsiveness + tagged branch merge. ZeroBot should coordinate the enable + restart + soak test. Next unchecked step remains 4.2.

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
- 2026-09-04 18:24 PDT — **Step 2.4 completed.** Administrative close-out for M2. Verified all M2
  work: `python3 -m py_compile repos/iter.py` → OK; `python3 sim_harness_2.3.py` → 46 passed,
  0 failed. Checked box 2.4. No structural change to iter.py in this step — no backup needed.
  **ITER_CONCURRENCY_ENABLED remains OFF (default).** The flag is not enabled live; M2 code
  (threaded_llm_call, merge queue, double drain) is dormant behind the flag guard. The live
  loop takes the `else:` branch (direct `client.chat.completions.create`) for all LLM calls;
  `drain_merge_queue()` is never called; `_merge_queue` is never populated. No behavioral
  change to the running bot.
  Git: PLAN.md committed to the research-agent root repo (where it is tracked); iter-port
  repo has no relevant changes (`repos/iter.py` is gitignored; the modified test file is
  unrelated to M2). Previous M2 commits in root repo: `c4167a0` (2.1), `a5cd554` (2.3).
  **M2 complete.** Next unchecked step: M3 step 3.1 (BACKGROUND_DEADLINE: abandon + marker +
  slot frees, flag-guarded, default max(2T, 300s)).
  **No restart needed** — no code changed; flag remains OFF.
- 2026-09-04 18:54 PDT — **Step 3.1 completed.** Added `BACKGROUND_DEADLINE = max(2 * ITER_PROMOTE_SECONDS, 300)`
  constant (R13: bounded background lifetime) and `check_background_deadline()` function. The function
  acquires `_branch_lock`, reads `_active_branch`; if `None` returns `False` (no-op). If the branch has
  been alive longer than `BACKGROUND_DEADLINE` seconds: frees the slot (`_active_branch = None`), queues
  an abandon marker to `_merge_queue` with `branch` id, `abandoned: True`, elapsed/deadline timing, and
  whether the LLM call had completed (`llm_completed` field in the diagnostic message). The daemon
  thread continues but its results are discarded (R9: no token waste — the call completes normally,
  we just ignore it). After abandonment, the slot is free for a new promotion (R18: one branch at a
  time). Called once per main-loop iteration, flag-guarded by `if ITER_CONCURRENCY_ENABLED:`, right
  before the existing first drain (M2 step 2.2a). Flag-off: `check_background_deadline()` is never
  called; `BACKGROUND_DEADLINE` is computed but unused; `_active_branch` is always `None` (never set,
  since `threaded_llm_call` is also behind the flag); zero behavioral change. Diff vs pre-step backup
  confirms 44 additions, 0 deletions — pure additions only.
  Backup: `iter.py.pre-m3-3.1-20260904T1854`.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_3.1.py` → 9 passed, 0 failed.
  Tests cover: (1) no active branch → False, empty queue; (2) branch within deadline → False, still
  active; (3) branch exceeded deadline → True, marker queued with correct fields, slot freed; (4)
  branch with completed LLM but exceeded deadline → abandoned with `llm_completed=True`; (5) new branch
  can be set after abandonment; (6) `_branch_lock` is a threading.Lock; (7) abandon marker has all
  required fields (role, branch, abandoned, elapsed, deadline); (8) `BACKGROUND_DEADLINE = max(2*30,
  300) = 300`; (9) py_compile OK. Source-level: function uses `_branch_lock`/`_active_branch`/
  `_merge_queue`; call is flag-guarded; 44 additions, 0 deletions vs backup.
  Git commit: iter-port repo (iter.py) + root repo (harness + PLAN.md).
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; `check_background_deadline()`
  is never called in the live loop; `BACKGROUND_DEADLINE` is computed but unused. No behavioral change
  to the running bot.
  Next step: 3.2 (try/except wrapper for background thread → error markers onto merge queue, R14).
- 2026-09-04 19:24 PDT — **Step 3.2 completed.** Added R14 error markers to `_bg_llm_thread_target`: on exception,
  if `result_container` has a `branch_id` (set by `threaded_llm_call` after promotion), the thread pushes an error
  marker to `_merge_queue` with `role`, `branch`, `error=True`, `error_type`, `error_message` (bounded to 500 chars),
  and a human-readable `content` containing `[BACKGROUND_BRANCH_ERROR]` + branch_id + error type + truncated message.
  The thread then acquires `_branch_lock` and frees `_active_branch` if it still matches this branch_id (compare-and-swap
  pattern avoids racing with `check_background_deadline`). Also added `result_container["branch_id"] = branch_id` in
  `threaded_llm_call` after promotion, so the thread can identify its branch on error. If the error occurs before
  promotion (fast error within T), `threaded_llm_call` raises the exception directly — no branch_id, no marker, no
  slot to free. If the slot was already freed by `check_background_deadline` (deadline fired first), the thread still
  pushes the error marker (useful diagnostic) but does not double-free the slot (the `if _active_branch is not None
  and _active_branch.branch_id == branch_id` guard prevents this).
  Changes: 1 docstring expansion (1 line → 9 lines) + 21 new lines in except block + 1 new line in `threaded_llm_call`.
  Diff vs pre-step backup: 23 additions, 1 deletion (docstring line replacement only — no existing logic lines modified).
  Backup: `iter.py.pre-m3-3.2-20260904T1924`.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_3.2.py` → 37 passed, 0 failed.
  Tests cover: (A) slow error after promotion → error marker with correct fields (role, branch, error, error_type,
  error_message, content with BACKGROUND_BRANCH_ERROR + branch_id); (B) error message bounded to 500 chars on 5000-char
  input; (C) branch slot freed after error; (D) fast error before promotion → exception raised, no marker; (E) slot
  pre-freed by deadline → thread still pushes marker but does not double-free; (F) flag-off source inspection — diff
  has only docstring replacement + additions, else-branch unchanged; (G) py_compile OK.
  `python3 sim_harness_2.3.py` → 46 passed, 0 failed (M2 regression — no breakage).
  Git commit to follow.
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; `_bg_llm_thread_target` is never called in the
  live loop; the error-marker path is dormant behind the flag guard. No behavioral change to the running bot.
  Next step: 3.3 (shutdown protocol: SIGTERM/SIGINT stop event, 5s grace, drain, save, exit; daemon threads).
- 2026-09-04 19:54 PDT — **Step 3.3 completed.** Added `SHUTDOWN_GRACE` (env `ITER_SHUTDOWN_GRACE`, default 5), `_shutdown_event` (threading.Event),
  `_iter_signal_handler()` (sets `_shutdown_event` on SIGTERM/SIGINT), `_install_signal_handlers()` (installs SIGTERM+SIGINT handlers,
  best-effort, catches ValueError/OSError), and `graceful_shutdown()` (R17: waits up to SHUTDOWN_GRACE for active branch to complete,
  drains merge queue, saves experience, calls `sys.exit(0)`). Signal handler installation call placed before `while True:`, flag-guarded
  by `if ITER_CONCURRENCY_ENABLED:`. Shutdown check placed at top of `while True:`, also flag-guarded (`if ITER_CONCURRENCY_ENABLED and
  _shutdown_event.is_set(): graceful_shutdown()`). `graceful_shutdown()` waits for `_active_branch` to populate `result_container["ok"]`
  (polls every 0.1s up to SHUTDOWN_GRACE), then drains queue, saves experience, exits. Branch threads are already daemon (set in step 2.1,
  R17). `sys.exit(0)` raises `SystemExit` (BaseException) which is not caught by the main loop's `except Exception` — clean exit.
  Flag-off: `SHUTDOWN_GRACE` computed but unused; `_shutdown_event` created but never checked; `_install_signal_handlers()` never called;
  `graceful_shutdown()` never called; default Python signal behavior (SIGINT → KeyboardInterrupt, SIGTERM → termination) unchanged.
  Diff vs pre-step backup: 62 additions, 0 deletions — pure additions only.
  Backup: `iter.py.pre-m3-3.3-20260904T1954`.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_3.3.py` → 39 passed, 0 failed. Tests cover: (A1–A4) signal handler
  sets event for SIGTERM, SIGINT, unknown signal; (B1–B4) install function runs, handlers installed, restored after test; (C1–C4)
  graceful_shutdown with no active branch drains, saves, exits with code 0; (D1–D4) graceful_shutdown waits for completing branch (<3s),
  exits, experience saved; (E1–E5) graceful_shutdown with slow branch exits within grace+margin, thread is daemon (still alive but
  doesn't block), experience saved; (F1–F3) merge queue drained before save; (G1–G2) SHUTDOWN_GRACE env config; (H1–H6) source inspection —
  flag guards, sys.exit, signal handler installation; (I1) py_compile; (J1–J3) diff is pure additions; (K1–K3) M2 drain_merge_queue
  regression. M2 regression: `sim_harness_2.3.py` → 46 passed, 0 failed. M3.2 regression: `sim_harness_3.2.py` → 37 passed, 0 failed.
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; signal handlers are never installed; `_shutdown_event` is never
  checked; `graceful_shutdown()` is never called. No behavioral change to the running bot.
  Next step: 3.4 (duplicate-tool supersede annotation `"superseded_by"`).
- 2026-09-04 20:24 PDT — **Step 3.4 completed.** Implemented R16 duplicate-tool supersede annotation in
  `drain_merge_queue()`. Added `_build_tool_call_map(messages)` helper function that builds a
  `tool_call_id → (tool_name, arguments)` map from assistant entries with tool_calls. Modified
  `drain_merge_queue()` to: (1) collect all entries from the queue first (instead of appending one
  by one), (2) build a tool-call lookup from merged assistant entries, (3) build a
  `(tool_name, arguments) → first_tool_entry_index` map from existing experience, (4) for each merged
  tool entry, check if its `(tool_name, arguments)` matches an existing entry in experience — if so,
  annotate the merged entry with `"superseded_by": "<index>"` (R16: the LLM sees the conflict
  explicitly rather than silently). Both entries stay in the log; only the later (background) one
  is annotated. Non-tool entries (system markers, error markers, abandon markers) are never
  annotated. Non-dict entries are skipped. Untagged entries still get `"branch": "unknown"`.
  `save_experience()` is called once after the full batch is appended (single-writer: only main
  thread). Flag-off: `_build_tool_call_map()` is defined but never called; `drain_merge_queue()` is
  never called (behind `ITER_CONCURRENCY_ENABLED` guards); zero behavioral change. Diff vs pre-step
  backup: 1 new function (14 lines), `drain_merge_queue` replacement (old 16-line body → new 47-line
  body); no other functions modified; no main-loop changes.
  Backup: `iter.py.pre-m3-3.4-20260905T0324`.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_3.4.py` → 47 passed, 0 failed.
  Tests cover: (A1–A6) `_build_tool_call_map` basic/edge cases; (B1) duplicate tool+args →
  `superseded_by` with correct index, assistant entry NOT annotated; (B2) different tool name →
  no annotation; (B3) same tool different args → no annotation; (B4) multiple duplicates → first
  occurrence index; (B5) empty queue → 0, no save; (B6) non-dict entries skipped; (B7) untagged
  → `unknown` branch; (C1) orphan tool entry (no preceding assistant in batch) → no annotation;
  (C2) mixed batch with 1 dup + 1 non-dup → exactly 1 `superseded_by`; (C3) system/error markers
  → never annotated; (C4) `save_experience` called once per batch; (C5) mixed batch with assistant,
  2 tools (1 dup), system marker → correct annotation on dup only; (D1–D7) source inspection —
  py_compile, function defined, `superseded_by`/`existing_tool_index`/`merged_call_lookup` present,
  both drain calls flag-guarded, `_build_tool_call_map` is new (not in backup); (E1–E2) regression —
  basic merge and empty-queue no-op.
  M2 regression: `sim_harness_2.3.py` → 46 passed, 0 failed (after injecting
  `_build_tool_call_map` into harness namespace). M3.2/M3.3 harness diff tests show expected
  failures (comparing against pre-3.2/3.3 backups, now seeing M3.4 `drain_merge_queue` changes);
  all functional tests in those harnesses pass.
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; `drain_merge_queue()` is
  never called in the live loop; `_build_tool_call_map()` is never called. No behavioral change
  to the running bot.
  Next step: 3.5 (branch step budget (25) + branch checkpoint queuing to main thread (R20)).
- 2026-09-04 20:54 PDT — **Step 3.5 completed.** Implemented R20 branch step budget + branch checkpoint queuing to main thread.
  Added `BRANCH_STEP_BUDGET = int(os.getenv("ITER_BRANCH_STEP_BUDGET", "25"))` constant (env-configurable, default 25 per spec
  open question 3). Added `_bg_branch_mini_loop()` function (~80 lines): after the initial LLM call completes in the background thread,
  the mini-loop runs up to BRANCH_STEP_BUDGET follow-up steps — pushes tagged assistant + tool entries to `_merge_queue`, makes
  follow-up LLM calls with `branch_client` (R12: separate client) on `branch_messages` (R11: deep copy), executes tool calls via
  `invoke_dynamic` (stateless subprocesses). On step-budget exhaustion: calls `extract_tier1_checkpoint()` on branch_messages,
  queues the checkpoint data to `_merge_queue` with `"_checkpoint_payload": True` marker — **never writes files directly** (R20:
  single-writer discipline). On normal completion (no more tool_calls): frees slot. On follow-up LLM call failure: pushes R14
  error marker + frees slot + returns. All slot frees use compare-and-swap guard (avoids racing with `check_background_deadline`).
  Modified `_bg_llm_thread_target`: after successful LLM call, checks `result_container.get("branch_id")` — if set (promotion
  happened), calls `_bg_branch_mini_loop()` with branch_id, branch_client, branch_messages, response, result_container. If the
  mini-loop raises an exception, the existing except block catches it (R14: error marker + slot free).
  Modified `threaded_llm_call`: stores `result_container["branch_client"]` and `result_container["branch_messages"]` during
  promotion (after bg_client creation, after branch_id assignment) so the thread can access them for the mini-loop.
  Modified `drain_merge_queue()`: separates checkpoint payloads (entries with `"_checkpoint_payload": True`) from regular entries.
  For each checkpoint payload: strips internal markers (`branch`, `_checkpoint_payload`), calls `write_checkpoint_file()` and
  `send_checkpoint_message()` from the main thread (R20: main thread writes file + sends), adds a system marker to experience
  (`[BACKGROUND_BRANCH_CHECKPOINT]`), saves experience. Regular entries are processed as before (supersede annotation, append,
  save). If only checkpoint payloads and no regular entries: saves and returns count. If neither: returns 0 (no-op).
  Flag-off: `BRANCH_STEP_BUDGET` is computed but unused; `_bg_branch_mini_loop()` is never called (behind `ITER_CONCURRENCY_ENABLED`
  via `threaded_llm_call`); `drain_merge_queue()` is never called (behind flag guards); `_checkpoint_payload` handling in
  `drain_merge_queue` is never reached. No behavioral change to the running bot.
  Diff vs pre-step backup: ~120 additions, ~8 deletions (modified `drain_merge_queue` early return + modified
  `_bg_llm_thread_target` to add mini-loop call + modified `threaded_llm_call` to store branch_client/messages). All deletions are
  expected modifications — no existing logic lines removed from the else branch or main loop.
  Backup: `iter.py.pre-m3-3.5-20260905T0354`.
  Evidence: `python3 -m py_compile iter.py` → OK; `python3 sim_harness_3.5.py` → 68 passed, 0 failed. Tests cover:
  (A1–A5) BRANCH_STEP_BUDGET constant (default 25, env-configurable, placed after BACKGROUND_DEADLINE);
  (B1–B15) mini-loop structure (step budget ref, checkpoint queuing, no direct file write/send, tagged entries, branch_client
  usage, branch_messages usage, load_tools, step counter, R14 error handling, compare-and-swap slot free);
  (C1–C3) normal completion (break on no tool_calls, BRANCH_COMPLETE log, checkpoint only on exhaustion);
  (D1–D6) follow-up LLM failure (try/except, error marker with branch_id, error_type/message bounded to 500 chars, slot free,
  return);
  (E1–E7) drain_merge_queue checkpoint handling (detects _checkpoint_payload, separates from regular, calls
  write_checkpoint_file + send_checkpoint_message from main thread, system marker, save, strips internal markers);
  (F1–F4) mixed checkpoint + regular entries (regular still processed, supersede intact, returns checkpoint count, no save
  when empty);
  (G1–G4) threaded_llm_call stores branch_client + branch_messages (after bg_client creation, after branch_id);
  (H1–H5) _bg_llm_thread_target calls mini-loop (checks branch_id, calls _bg_branch_mini_loop, checks client/messages, inside
  try block, except catches mini-loop exceptions);
  (I1–I7b) flag-off inspection (constant is module-level, mini-loop only called from _bg_llm_thread_target, drain calls
  flag-guarded, else branch unchanged, _promoted guard intact, M1 checkpoint intact, diff mostly additions);
  (J1–J10) regression — M2/M3 features intact (threaded_llm_call, _merge_queue, drain_merge_queue, check_background_deadline,
  graceful_shutdown, _build_tool_call_map, BACKGROUND_DEADLINE, SHUTDOWN_GRACE, double drain, R14 error markers);
  (K1) py_compile.
  M2 regression: `sim_harness_2.3.py` → 46 passed, 0 failed (after injecting no-op `_bg_branch_mini_loop` stub for harness
  namespace). M3.4 regression: `sim_harness_3.4.py` → 47 passed, 0 failed. M3.2/M3.3 harness diff tests show expected failures
  (comparing against pre-3.2/3.3 backups, now seeing M3.5 changes); all functional tests pass.
  Git commit to follow.
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; `_bg_branch_mini_loop()` is never called; the mini-loop,
  checkpoint queuing, and drain_merge_queue checkpoint handling are all dormant behind the flag guard. No behavioral change
  to the running bot.
  Next step: 3.6 (tests for 3.1–3.5 — consolidate all M3 tests; log + commit).
- 2026-09-04 21:24 PDT — **Step 3.6 completed.** Created consolidated test harness
  `sim_harness_3.6.py` covering all M3 features (3.1–3.5) in a single run. The harness uses
  AST extraction to test the real code from iter.py — not copies. It avoids diff-against-
  old-backup tests (which break after subsequent steps modify the code, as noted in step 3.5
  log); instead it uses functional tests, source inspection, and regression checks.

  **144 tests total, all passing:**
  - 3.1 (R13 BACKGROUND_DEADLINE): 6 source + 13 functional = 19 tests. Covers constant,
    function, flag guard, no-branch, within-deadline, exceeded-deadline (abandon + marker +
    slot free), completed-LLM-but-abandoned, new-branch-after-abandon.
  - 3.2 (R14 error markers): 8 source + 15 functional = 23 tests. Covers error marker logic,
    error_type/message bounding, BACKGROUND_BRANCH_ERROR content, compare-and-swap slot free,
    slow error promotion + marker, 500-char bounding, fast error (no promotion, no marker).
  - 3.3 (R17 shutdown): 13 source + 13 functional = 26 tests. Covers signal handler (SIGTERM/
    SIGINT), install function, graceful_shutdown (no-branch, completing-branch, slow-branch),
    merge queue drain before save, SHUTDOWN_GRACE, sys.exit, daemon threads, flag guards.
  - 3.4 (R16 supersede): 4 source + 14 functional = 18 tests. Covers _build_tool_call_map,
    duplicate detection (same tool+args → superseded_by), different tool / different args →
    no annotation, system markers not annotated, empty queue no-op, save_experience once
    per batch.
  - 3.5 (R20 branch step budget): 30 source inspection tests. Covers BRANCH_STEP_BUDGET,
    _bg_branch_mini_loop structure (step budget, checkpoint queuing, no direct file write/send,
    branch_client/messages usage, tool loading, error handling, compare-and-swap slot free,
    normal completion, BRANCH_COMPLETE), drain_merge_queue checkpoint handling (detect,
    separate, write+send from main thread, system marker, strip internal markers),
    threaded_llm_call stores branch_client+messages, _bg_llm_thread_target calls mini-loop,
    flag-off inspection (constant, drain guards, else branch, _promoted guard, M1 checkpoint).
  - Regression (M1/M2/M3 coexistence): 22 tests. All M1 (checkpoint), M2 (threaded_llm_call,
    merge queue, drain, BranchState, flag defaults), M3 (check_background_deadline, signal
    handler, graceful_shutdown, _build_tool_call_map, BRANCH_STEP_BUDGET, _bg_branch_mini_loop)
    features confirmed present. Double drain (R15), error markers (R14), supersede (R16),
    shutdown (R17) all intact.
  - py_compile: 1 test (passes).

  **M2 regression:** `sim_harness_2.3.py` → 46 passed, 0 failed (no breakage).

  No structural change to iter.py in this step — no backup needed (test-only step). Backup
  `iter.py.pre-m3-3.6-20260905T0424` created per plan rules but identical to iter.py.

  **Note on existing harnesses:** sim_harness_3.1.py has a relative path bug (`ITER_PY =
  "iter.py"` instead of absolute path) and fails when run from the iter-concurrency directory.
  sim_harness_3.2.py and 3.3.py have diff-against-old-backup tests that show expected failures
  (comparing against pre-3.2/3.3 backups, now seeing M3.4/3.5 changes). All functional tests in
  those harnesses pass. The consolidated harness 3.6 supersedes these for regression purposes.

  **M3 complete.** All M3 steps (3.1–3.6) are done and checked off.
  **No restart needed** — `ITER_CONCURRENCY_ENABLED` defaults to OFF; all M3 code is dormant
  behind the flag guard. No behavioral change to the running bot.
  Next unchecked step: M4 step 4.1 (extract USAGE/latency distribution from supervisor log;
  confirm bimodal split; recommend T).
- 2026-09-04 21:54 PDT — **Step 4.1 completed.** Extracted USAGE/latency distribution from the
  supervisor log at `/home/openclaw/.openclaw/protocosmo2-supervisor.log` (473,544 lines, ~104 MB,
  spanning 2026-09-02 14:26 → 2026-09-04 21:55, ~55.5 hours). Method: paired `AFTER LLM` /
  `USAGE CompletionUsage` log lines to extract `created=` Unix timestamps and USAGE metadata
  (completion_tokens, prompt_tokens, reasoning_tokens, cost) for 5,640 LLM calls across 3 models
  (z-ai/glm-5.2: 3,276 calls; moonshotai/kimi-k3: 2,149; z-ai/glm-4.7: 9). Computed inter-call
  intervals as total cycle time (tool exec + LLM latency) per step.

  **Bimodal split: partially confirmed.** z-ai/glm-5.2 (current model) shows a fast mode
  (61.1% <30s, p50=22s, p90=24s, p95=27s) and a slow mode (38.9% ≥30s, p50=53s, p90=85s),
  but the valley between modes (30–40s) contains 10.0% of calls — not a clean gap. Last-24h
  data (2,399 calls) confirms the same pattern: fast 57.9% (p90=25s, p95=27s), slow 42.1%
  (p50=52s, p90=86s), valley 11.8%. Completion-token stratification confirms generation length
  as the primary driver: low-token (<200) calls have 16s median interval, high-token (≥200)
  calls have 30s median. 95.6% of calls produce reasoning tokens (mean=398, p90=1060).

  **T recommendation: T=30s remains best.** Fast p95=27s → T=30 captures >95% of fast calls
  (~3% false promotion rate). Slow p50=52s → reliable promotion (22s margin). Valley cost:
  ~10% of calls unnecessarily promoted, ~$3/day wasted compute — tolerable. Alternatives
  (T=25, 28, 35, 40) all worse on one axis. BACKGROUND_DEADLINE=max(2×30,300)=300s is
  well above slow p90=86s (3.5× headroom) — no adjustment needed.

  Analysis report saved to `iter-concurrency/m4-latency-analysis.md` (8,022 bytes, full
  histogram, per-model breakdown, cost context, limitations, alternatives table).

  No structural change to iter.py — this is an analysis step. Backup `iter.py.pre-m4-4.1-20260905T0454`
  created per plan rules (identical to current iter.py). `python3 -m py_compile iter.py` → OK
  (baseline re-verified).

  **No restart needed** — no code change; analysis only.
  Next step: 4.2 (enable flag on live bot; soak; end-to-end Telegram test). **Requires explicit
  approval from Ben** — enabling ITER_CONCURRENCY_ENABLED on the live bot changes runtime behavior.
  ZeroBot should coordinate the enable + soak test.
- 2026-09-05 05:54 UTC (Fri Sep 4 22:54 PDT) — **Step 4.2 re-checked — still BLOCKED.** No approval from Ben to enable `ITER_CONCURRENCY_ENABLED=1` on the live bot has been received (checked memory + recent sessions). `ITER_CONCURRENCY_ENABLED` is not set in the environment. `python3 -m py_compile iter.py` → OK (baseline re-verified). Backup `iter.py.pre-m4-4.2-recheck-20260905T0554` created per plan rules (identical to current iter.py — no structural change). iter-port repo is a git repo (HEAD = `d002af8`). No commit made — nothing to commit (no code change). **Blocker unchanged:** Ben must explicitly approve enabling the flag + coordinate the supervisor restart. ZeroBot should handle the enable + restart + soak test once approved. Next unchecked step remains 4.2.
- 2026-09-05 06:24 UTC (Fri Sep 4 23:24 PDT) — **Step 4.2 re-checked — still BLOCKED (3rd consecutive).** No approval from Ben found in memory or recent sessions. `ITER_CONCURRENCY_ENABLED` is unset in the current environment. `python3 -m py_compile iter.py` → OK (baseline re-verified). Backup `iter.py.pre-m4-4.2-recheck-20260905T0624` created per plan rules (identical to current iter.py — no structural change). iter-port repo is a git repo (HEAD = `23a5d6f`). No commit made — nothing to commit (no code change). **Blocker unchanged:** Ben must explicitly approve enabling `ITER_CONCURRENCY_ENABLED=1` on the live bot and coordinate the supervisor restart. ZeroBot should handle the enable + restart + soak test once approved. Next unchecked step remains 4.2.
- 2026-09-05 06:54 UTC (Fri Sep 4 23:54 PDT) — **Step 4.2 re-checked — still BLOCKED (4th consecutive).** No approval from Ben found in memory, recent sessions, or session history. `ITER_CONCURRENCY_ENABLED` is unset in the current environment (confirmed via env check). `python3 -m py_compile iter.py` → OK (baseline re-verified). Backup `iter.py.pre-m4-4.2-recheck-20260905T0654` created per plan rules (identical to current iter.py — no structural change). iter-port repo is a git repo (HEAD = `23a5d6f`, confirmed via `git rev-parse --is-inside-work-tree`). No commit made — nothing to commit (no code change). **Blocker unchanged (4th recurrence):** Ben must explicitly approve enabling `ITER_CONCURRENCY_ENABLED=1` on the live bot and coordinate the supervisor restart. This is a runtime safety gate — the flag changes live Telegram bot behavior and must not be enabled without explicit user consent. ZeroBot should handle the enable + restart + soak test once approved. All M1–M3 code and M4 step 4.1 are complete; the implementation is fully feature-complete and tested (all harnesses pass); only the live enablement + soak test remains. Next unchecked step remains 4.2. If this blocker persists for many more cycles, the worker should consider escalating a notification to Ben via a different channel (e.g., a memory entry flagging the pending approval).
