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
- [ ] 1.2 Atomic checkpoint file write (temp+rename) to `checkpoints/<session>/<ts>.json`
      BEFORE any send, per v4 write-ordering.
- [ ] 1.3 Human-readable checkpoint via normal `send` path after file write.
- [ ] 1.4 Tests: py_compile; a provider-free simulation harness run showing checkpoint
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
