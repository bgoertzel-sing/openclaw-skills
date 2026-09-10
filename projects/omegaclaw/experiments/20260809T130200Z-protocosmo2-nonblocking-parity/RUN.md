# ProtoCosmo2 non-blocking transport and supervisor parity

- Status: in progress; production untouched
- Date: 2026-08-09
- Project: `omegaclaw`
- Authorization: Ben requested the improvement process ASAP and step by step;
  this authorizes offline implementation and testing, not an unreviewed live
  restart. A guarded production restart will require an explicit final approval
  after independent review.
- Relevant research rules: Rule 2 (stateful routing/concurrency specification),
  Rule 5 (reproducible evidence), and Rule 7 (modular supervisor/transport seam).

## Deliverable and acceptance

ProtoCosmo2 must load the already shared schema-3 deferred-job transport and
the repaired responder path without weakening its existing routing envelope.
Its owning supervisor must gain identity-bound PID validation, serialized
start/cutover, exact one-child readiness, secure schema-compatible synchronous
rollback, and watchdog recognition. Provider-free tests must cover the new
boundaries and an isolated copy of schema-2 state must migrate/reload in both
deferred and rollback modes. A separate frontier review must PASS before a
guarded production restart is requested. Completion requires fresh external
short and long-document/interleaved-short production traces.

## Exact routed trace

`Telegram update -> sole ProtoCosmo2 Bot API receiver -> immutable chat/user/
source-message envelope -> durable inbox/outbox -> synchronous or deferred
responder -> strict rendering -> Telegram reply receipt`.

## Rollback

Do not restore schema-2 code after state migration. Stop only the owning
ProtoCosmo2 supervisor, activate a private create-exclusive/no-follow mode-0600
single-link marker, restart the same schema-3 runtime with deferred admission
disabled, and require preserved cursor/processed/outbox/context state plus one
receiver and healthy watchdog recognition.

## Baseline and results

### Production baseline

- Live owner PID 1918102 and receiver child 1918105 started 2026-08-07
  14:40 PDT. The repaired runner/supervisor files were updated after that
  process start, so the running interpreter has not loaded them.
- Durable state SHA-256 before any production action:
  `b5196fffc15630d3d5b5b1d2466782c3e8407839e33d94214030fa6614a6814a`.
  It is schema 2 with offset 387572719, 191 processed message IDs, 42 outbox
  records, no pending inbound item, and no deferred-job ledger.
- Config and environment files are private mode 0600. Only key names were
  inspected; no credential values were read or recorded.
- Source commits at baseline: ProtoCosmo2 notebook/runtime `046592b`; shared
  transport worktree `2c3341a`. Production remained running and untouched
  throughout offline work.

### Implementation

- Parameterized the already reviewed Protomega outer supervisor at its modular
  runtime seam while retaining all Protomega defaults. ProtoCosmo2 now has a
  thin identity/path wrapper binding its own credential, config, state, worker,
  PID, log, lock, marker, model, and Telegram identity.
- Added a ProtoCosmo2 watchdog wrapper and parameterized receiver identity in
  the shared watchdog. The shared implementation retains the accepted
  identity-bound PID/start-time/cmdline checks, serialized start/cutover,
  exact one-child readiness, receiver-drain behavior, and secure synchronous
  rollback marker.
- Added five focused tests for identity/path isolation, unchanged Protomega
  defaults, secure marker creation/revalidation, symlink/hardlink rejection,
  and watchdog binding.

### Deterministic and isolated gates

- First pytest command failed during collection because the shared transport
  worktree was omitted from `PYTHONPATH`; exact error was
  `ModuleNotFoundError: channels`. No test body ran and no production action
  occurred.
- Corrected focused gate: 72/72 tests passed in 2.70 seconds. This includes
  ProtoCosmo2 supervisor tests, existing Protomega supervisor regressions,
  live runner/prompt-file/rendering/rollback tests, and durable transport
  concurrency/recovery tests.
- Python compilation and four shell syntax checks pass.
- Final focused replay command is exactly:

  ```bash
  PYTHONPATH=projects/omegaclaw/worktrees/protocosmo2-phase6-live:. \
    python3 -m pytest -q \
    tests/test_protocosmo2_supervisor.py \
    tests/test_protomega_outer_supervisor.py \
    tests/test_omegaclaw_watchdog.py \
    projects/omegaclaw/protocosmo2/tests/test_live_runtime_prompt.py \
    projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary.py \
    projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary_telegram.py
  ```
- An isolated copy of the real schema-2 production state migrated to schema 3,
  added an empty deferred-job ledger, reloaded exactly, and preserved the
  cursor/processed/outbox/rate/incident/context projection at SHA-256
  `28691896b7966959a162dcadc65ec5542308aef02a78c0e86718fa7eb771d404`.
- An isolated supervisor rehearsal created and validated the secure rollback
  marker, started exactly one fake receiver with `--disable-deferred-jobs`,
  passed topology status, and stopped cleanly. Production remained untouched.

Remaining gates: rerun after final scoped diff review, pin focused commits,
obtain independent frontier PASS, then request one guarded production restart.

### Independent review R1 — BLOCK

- Run `a650a863-5150-4e2f-9875-1873bb82e5b9` used OpenAI GPT-5.6 Sol with no
  fallback. It independently passed 84 tests, compilation, shell syntax, and
  scoped diff checks.
- It blocked the first cutover because the live pre-sidecar owner is rejected
  by the new `alive()` check, so ordinary `stop`/`start` could overlap it. It
  also rejected ambient environment overrides of ProtoCosmo2 production paths.
- Remediation freezes every production identity/path in the wrapper and adds a
  one-purpose `stop-pre-sidecar EXPECTED_PID EXPECTED_START
  EXPECTED_CMDLINE_SHA256` action. Under the cutover lock it content-binds the
  legacy owner, exact resolved wrapper `run` command, process group, and exactly
  one expected receiver child before signaling the group; any mismatch fails
  closed. It removes the PID file only after owner and child both disappear.

### Independent review R2 — BLOCK

- Run `9c2cca88-3978-4b8b-9085-7d0d8b11db13` used OpenAI GPT-5.6 Sol with no
  fallback and independently passed all 84 tests and static gates.
- It accepted the frozen paths and exact legacy drain, but found that ambient
  `OMEGACLAW_CUTOVER_LOCK_HELD=1` could bypass serialization.
- Remediation requires the flag to be accompanied by inherited descriptor 9
  resolving exactly to the configured cutover lock. The watchdog now preserves
  its genuinely locked descriptor through the supervisor handoff; the owner
  launcher closes it before detaching. A regression proves the ambient flag
  without the locked descriptor fails before PID mutation.

### Independent review R3/R3b — infrastructure failure then BLOCK

- R3 terminated during Gateway transcript compaction without a verdict.
- R3b run `6ad02325-c2e4-45d4-96ce-5dafa7b56908` used OpenAI GPT-5.6 Sol with
  no fallback. It accepted the watchdog handoff, frozen paths, and legacy
  drain, but observed that fd 9's path alone did not prove/acquire its flock;
  it also could not reconstruct the exact 85-test command from the RUN.
- Remediation adds `flock -n 9` after exact path validation, which either
  confirms the inherited open-file description already owns the lock or safely
  acquires it before bypassing the ordinary lock-open path. The exact focused
  replay command is now embedded above.

### Independent review R4 — PASS

- Run `cd372a54-1646-4374-b6d7-79ff1636e2b6` used OpenAI GPT-5.6 Sol with no
  fallback and returned `PASS`.
- The reviewer independently reran the literal gate: 85/85 tests, compilation,
  four shell syntax checks, diff check, and ancestry all passed.
- It verified exact fd-9 path plus successful nonblocking flock acquisition,
  real watchdog lock handoff, detached-owner descriptor closure, frozen
  ProtoCosmo2 isolation, schema-compatible rollback, and unchanged Protomega
  defaults. No remaining production-safety blocker was found in scope.
- Technical readiness only: production remains the original pre-sidecar owner.
  One explicitly authorized guarded restart and fresh external canaries remain.

### First guarded production cutover — fail-safe rollback active

- Ben explicitly authorized the guarded restart on 2026-08-09. The exact
  pre-sidecar owner (PID 1918102, start tick 41230822, cmdline SHA-256
  `839ceb5e458138bf3f84e87396b0e5edbd889a240523939dcfdc9be1fcde0706`)
  and its sole receiver child 1918105 passed content-bound validation.
- The immutable pre-restart state snapshot is
  `production-pre-restart-state.json`, SHA-256
  `81e647e77a5af4db505339c64779aed604d450adddc8e65ff8c1289808d5b164`.
- The owner and child drained, but `stop-pre-sidecar` returned failure at its
  final postcondition because the terminating legacy owner removed its own PID
  file. No second receiver was started during this failed gate.
- Per the approved failure rule, synchronous rollback was activated. The
  identity-bound schema-3 supervisor started as PID 2560477 with exactly one
  receiver child and `--disable-deferred-jobs`. Watchdog check returned
  `OUTER_OWNER_RUNNING`; the topology lock was independently acquired as free.
- The protected cursor/processed/outbox/pending/context projection matches the
  snapshot exactly at SHA-256
  `64c5df7d34b5af5a70f0d03a2974bf28c451d1d88eef1ad57c620b144a497b62`.
  State is schema 3 with 191 processed IDs, 42 outbox records, no pending
  inbound item, and zero deferred jobs.
- Status: operational in tested synchronous rollback mode; the non-blocking
  upgrade and external canaries remain unaccepted. Before retry, repair and
  regression-test the legacy PID-file drain postcondition and obtain a fresh
  production cutover decision.

### PID-file shutdown-race repair — independently passed

- The first minimal absence-or-value patch passed 86 tests but independent
  review blocked it because a same-value replacement file could pass.
- The repaired guard captures device, inode, owner, mode, link count,
  nanosecond change/modify times, and size before drain. After owner/child
  disappearance it accepts clean absence, or opens the exact remaining file
  with no-follow semantics, validates identity and value, revalidates the
  directory entry, unlinks through the directory descriptor, and proves via
  the still-open descriptor that the captured inode reached link count zero.
- Executable regressions cover legacy self-unlink, exact original consumption,
  same-value replacement, changed value, symlink, hardlink, and a deterministic
  pathname swap between pre-unlink validation and unlink.
- Final local gates: 11/11 focused tests and 90/90 full provider-free tests,
  Python compilation, four shell syntax checks, and scoped diff check passed.
- Independent final review replayed the same gates and returned PASS with no
  remaining production-safety blocker in scope. Production was not changed and
  remains online in synchronous rollback mode pending fresh cutover approval.

### Fresh guarded cutover — process gates passed

- Ben explicitly authorized the fresh cutover on 2026-08-09. The current
  identity-bound rollback owner was stopped through its supervisor after a new
  state snapshot at `production-pre-deferred-retry-state.json`, SHA-256
  `daa6a1461ac05095aa6c3f7968c17caab08335528d279f11582c02da0a2d87d6`.
- The secure rollback marker was validated and directory-anchored before exact
  unlink; its opened inode was proven unlinked. The schema-3 supervisor started
  in deferred mode as owner 2590176 with exactly one receiver child 2590189 and
  no `--disable-deferred-jobs` flag.
- The protected cursor/processed/outbox/pending/context projection matched the
  snapshot exactly at SHA-256
  `beb668895c6dbf41367f408992a34d083f365645aed66834f724639594ac8112`.
  Watchdog returned `OUTER_OWNER_RUNNING`, and the topology lock was free.
- Rollback was not activated. Process readiness passed; fresh short and
  PDF-plus-interleaved-short external Telegram traces remain required for full
  production acceptance.
## Final production acceptance — 2026-08-09

- Fresh short source 827 delivered exact `PC2-OK` as receipt 828.
- PDF-related sources 840 and 841 entered durable task IDs
  `7ac7316bc904...` and `cda87a9f6418...`; acknowledgements were receipts 842
  and 843.
- Interleaved short source 844 delivered exact `PC2-FULL-SHORT-OK` as receipt
  845 before either PDF result.
- Deferred results 846 and 847 remained bound to sources 840 and 841;
  respectively, with receipt 847 containing the requested Omega Linux summary.
- Both deferred tasks completed exactly once. Final checks found schema 3, no
  pending inbound item, exactly one identity-bound receiver, healthy
  ProtoCosmo2 watchdog ownership, a free topology lock, deferred mode enabled,
  clean rendering, and no rollback.

Result: production acceptance passed. ProtoCosmo2 is ready for normal/full use
within its existing authorized capabilities. This does not expand unavailable
tools, side-effect authority, paid-compute authority, or other approval gates.
