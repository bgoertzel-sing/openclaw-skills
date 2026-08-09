# Protomega non-blocking long-task repair

- Status: staging complete; production deployment pending final PASS
- Date: 2026-08-08
- Project: `omegaclaw`
- Question: can long/document requests be acknowledged and executed outside
  the Telegram polling loop while preserving immutable reply routing and
  allowing interleaved short group/DM messages?
- Relevant research rules: Rule 2 (stateful routing/concurrency spec), Rule 5
  (reproducible evidence), and Rule 7 (modular queue/worker seam).

## Baseline

- Production identity: ProtomegaTron / `@Protomegabot`.
- Production topology at task start: one outer supervisor and one receiver;
  no legacy receiver.
- Observed failure trace: bot-philosophy message 9729 was admitted, its PDF and
  addressed follow-up were synchronously sent through the responder, the
  provider ran until the bounded bridge deadline, and the polling loop could
  not acquire later messages during that interval. A visible failure receipt
  was eventually delivered.
- Staging identity: ProtoMegaBot2 / `@Protomega2bot`, with distinct Telegram
  credential, launcher, repository, and mutable-state paths. Its existing
  repository is dirty with unrelated work and must not be overwritten.
- Rollback target: the current production runner and outer supervisor; restore
  its pre-change source and restart only through the owning supervisor if live
  acceptance fails.

## Acceptance

1. Provider-free tests show a long job is durably admitted and immediately
   acknowledged without running the responder in the polling thread.
2. An interleaved short message is admitted and answered while the long job is
   still running.
3. Long-task completion/failure is durably delivered to its original chat and
   source message after restart-safe reconciliation; no cross-chat routing.
4. Internal `(send ...)` wrappers are removed only under a strict recognized
   rendering grammar.
5. Isolated live ProtoMegaBot2 staging and independent frontier review pass
   before production deployment.
6. Fresh production external-channel trace passes with one owning receiver.

## Commands and results

### External staging trace R2 (2026-08-08 21:39 PDT)

- Reply-to-PDF request: Telegram message 112.
- Durable acknowledgement: receipt 113.
- Deferred task:
  `86a1f8c3e058a425baaca87a99a7d0fe4d957d360a7a484e91fd33964ff99e6b`.
- Deferred failure: receipt 114; the task became terminal `failed` and its
  prompt was cleared after failure.
- Interleaved short request: message 115; clean `PING-OK` receipt 116.
- Interpretation: polling-loop concurrency and immutable reply routing passed;
  deferred execution failed before provider completion.

### Root-cause reproduction and repair

- The matching 656,809-byte source PDF at
  `library/omegaself/OmegaSelf_Architecture_and_Deployment_Guide.pdf` extracts
  to 161,305 bytes. A provider-free `/bin/true` launch with one 161,305-byte
  argument reproduces `OSError 7: Argument list too long`. Linux's per-string
  argv ceiling is below the extracted prompt even though system `ARG_MAX` is
  2,097,152 bytes.
- Repair: `phase6_private_canary_runner.py` now places the complete prompt in
  a create-exclusive 0600 temporary regular file, passes only
  `--prompt-file`, and unlinks it on every launch/completion/failure path.
  `phase5_omegaclaw_case.py` accepts exactly one of inline `--prompt` or a
  private, single-link, non-symlink regular prompt file.
- Focused/provider-free gate: 55 tests passed in 0.66 seconds; compilation and
  targeted `git diff --check` passed. The added regression transfers an
  800,000-byte prompt outside argv and verifies mode 0600 plus cleanup.
- A full deterministic OmegaClaw Test-provider replay read the 161,305-byte
  file and reached the mock LLM (`LARGE-PDF-WORKER-OK`) but did not produce a
  file-channel send result before the 90-second deadline. This is not counted
  as end-to-end success; the live responder uses the separate
  OpenClawFileBridge raw-answer seam. Exact failure was recorded rather than
  weakened.
- Staging-only supervisor restarted successfully at owner PID 2425077 with one
  child. Production remained untouched at owner PID 2343127 with one child.

## Current gate

### External staging trace R3 — PASS (2026-08-08 22:03 PDT)

- Telegram source message 118 replied to the existing PDF.
- Immediate durable acknowledgement delivered as receipt 119.
- Deferred task
  `2c69c9daed8075dc96afd12cafdc9b22422d1deb379b829bff9187b34ea96c9a`
  started without blocking the polling loop and completed in 56 seconds.
- Provider session `protomegabot2-staging-1786251831` recorded actual provider
  `anthropic`, actual model `claude-opus-4-6`, and terminal stop reason `stop`.
- Clean summary was queued as durable outbox item
  `f17ebc0cc50aa3d2f0549b1541b8ec65b9f921fd84fb9d8530c1064ee12126f3`
  and delivered to the immutable source message as Telegram receipt 120.
- The final text contains no internal `(send ...)` wrapper. Production remained
  separate at owner PID 2343127 with one child throughout staging.

The external staging acceptance gate now passes. A fresh independent frontier
review of the prompt-file change and complete evidence remains required before
production deployment; production has not been restarted or modified.

### Independent review R2 and hardening

- GPT-5.6 Sol independently reran 55 tests and returned `BLOCK`. Concrete
  blockers were pathname-validation TOCTOU, incomplete cleanup if prompt
  write/flush/fsync failed, missing adversarial tests, no single combined live
  successful-long/interleaved-short trace, and no pinned deploy/rollback
  boundary.
- Prompt reading now uses one `os.open(O_NOFOLLOW|O_CLOEXEC)` descriptor,
  validates that same descriptor with `fstat`, and reads it through `fdopen`.
  Path substitution after open fails closed when link count changes.
- Prompt creation now cleans the partial file on every write/flush/fsync/close
  exception before propagating failure. Adversarial substitution and injected
  flush-failure cleanup regressions were added.
- Revised gate: 57 tests passed in 0.74 seconds; compilation and targeted diff
  check passed.
- Pinned local commits (not pushed): transport worktree
  `eb29a3388530dc7fdc27171b372037a9f77dc9ce`; outer runner/tests/evidence
  `b07936bad28fd06bf556b5dcb95374897469f7de`.
- Exact rollback target is transport parent `0a344d105651a464afaa81965eb51ee516f282e1`
  plus outer parent `7231c67`; rollback is performed only through the owning
  staging/production supervisor after restoring those pinned trees.

Remaining pre-production gate: load the hardened commits in staging, obtain
one combined external trace where a successful long document overlaps an
interleaved short request, then obtain a fresh independent PASS.

### External staging trace R4 — PASS (2026-08-08 22:17 PDT)

- Telegram source message 121 replied to the existing PDF.
- Immediate durable acknowledgement delivered as receipt 122.
- Interleaved short request message 123 delivered the exact clean reply
  `SHORT-R4-OK` as receipt 124 while the deferred task remained active.
- Deferred task
  `8fe4a22de5dc90429426406c300e426404267d7ed556bf215c1892ae04242515`
  completed in 39 seconds and delivered its final summary as receipt 125,
  immutably replying to source message 121.
- Receipt 124 preceded the long result by 31 seconds, directly demonstrating
  that the Telegram polling loop remained responsive during document work.
- Durable final state records the task as `completed`, with no pending inbound
  item, no undelivered outbox item, and no internal `(send ...)` wrapper in
  either reply.
- Production remained on its pre-repair process; no production restart or
  deployment occurred during R4.

The combined hardened staging gate passes. Remaining gate: one fresh
independent frontier PASS over the pinned implementation, 57-test replay, R4
evidence, and exact production restart/rollback boundary.

### Independent review R3 — BLOCK on evidence closure

- Run: `6fee84cb-37b3-4bcb-a5dd-c05468749d9b`.
- Actual provider/model: OpenAI `gpt-5.6-sol`; fallback false; terminal stop.
- The reviewer independently passed 57/57 tests and accepted the code coverage,
  but blocked because R4 lacked committed content-bound raw artifacts, this
  run still said `in progress`, and deploy/rollback commands were not exact.
- Raw bounded evidence is now retained under `artifacts/`: a redacted R4
  durable-state projection containing source IDs, task identity/timestamps,
  outbox IDs, immutable reply routes, receipts 122/124/125, and final status;
  a topology snapshot; and verified SHA-256 manifests. No credential or full
  source document is included.

### Exact production deployment and rollback boundary

Deployment changes no source: production already resolves the pinned repaired
files but its current long-lived Python process predates them. The guarded
deployment is exactly:

1. Verify `protomega-outer-telegram-supervisor.sh status`, one child, zero
   legacy receiver, free topology lock, and no pending/undelivered durable item.
2. Copy the production `state.json` to the experiment artifact directory and
   hash it before restart.
3. Run `projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh stop`.
4. Prove zero production Bot-API receivers.
5. Run `projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh start`.
6. Require one owner/one child, zero legacy receiver, watchdog recognition,
   free topology lock, unchanged cursor/processed/outbox state, and no pending
   or undelivered item.

Immediate rollback on any failed postcondition is exactly:

1. Stop the production outer supervisor and prove zero receivers.
2. Restore runtime files only from outer parent `7231c67`:
   `phase5_omegaclaw_case.py`, `phase5_openclaw_bridge.py`, and
   `phase6_private_canary_runner.py`.
3. Restore transport runtime files only from transport parent
   `0a344d105651a464afaa81965eb51ee516f282e1`:
   `channels/private_canary.py` and
   `channels/private_canary_telegram.py`.
4. Start the same owning production outer supervisor and require one owner/one
   child, zero legacy receiver, preserved durable state, watchdog recognition,
   and a free topology lock.

These restores use `git restore --source=<pinned-parent> -- <exact-files>`;
they do not rewrite history or touch unrelated working-tree changes.
