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
- [ ] 1.5 Log + commit. Announce restart needed.

### M2 — Time-based promotion core (flag `ITER_CONCURRENCY_ENABLED`, default OFF)
- [ ] 2.1 Threaded LLM call wrapper with deadline T (env `ITER_PROMOTE_SECONDS`, default 30):
      foreground first; on T expiry, deep copy messages, separate OpenAI client, branch id.
- [ ] 2.2 Merge queue (queue.Queue) + double drain (top of loop AND before building messages);
      single-writer discipline; tagged entries `"branch": "bg-<id>"`.
- [ ] 2.3 Tests: py_compile; offline harness — fake slow call detaches, fake chat answered,
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
