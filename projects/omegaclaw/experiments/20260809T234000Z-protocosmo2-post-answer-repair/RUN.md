# ProtoCosmo2 post-answer runtime repair

- Date: 2026-08-09
- Production failure: Telegram source message 848 -> bounded failure receipt 849
- Live transport pin before repair: `2c96a1b6727dca440e1f27ee55da5ca1dcdeade9`
- Production mutation during offline repair: none

## Observed failure

ProtoCosmo2 accepted message 848 and the inner OmegaClaw runtime emitted a complete
`send` result into durable `history.metta`. The driver subsequently exited with code
1. The outer responder checked the exit code before parsing captured stdout, so it
discarded the completed answer and emitted failure receipt 849. The private incident
record contains `omegaclaw_runtime_failure`, 20,623 stderr bytes, and SHA-256
`a496898d0f95055618d389a71861c722c6a484b7f2ba6bc6d09d8dfd22a74169`.

## Contract

The bridge result is the immutable inner-to-outer handoff. If captured stdout contains
a complete `status=ok`, nonempty answer, the outer layer validates its rendering. A
later nonzero child exit remains a recorded runtime incident but does not invalidate
that already captured answer. Nonzero exit without a valid answer remains a bounded
failure. Malformed action-shaped output remains rejected.

Relevant research rules: Rule 2 (explicit routed-state invariant), Rule 5
(reproducible evidence), and Rule 7 (keep bridge-result validation separate from
process-lifecycle diagnostics).

## Implementation and verification

- Added `captured_bridge_answer()` and reordered responder processing so nonzero exits
  are recorded before a captured answer is validated and returned.
- Added exact provider-free regressions for:
  - valid answer plus nonzero exit;
  - malformed answer plus nonzero exit;
  - nonzero exit without an answer.
- Focused command:
  `python3 -m pytest -q projects/omegaclaw/protocosmo2/tests/test_live_runtime_prompt.py`
  -> 19 passed.
- Full provider-free command:
  `PYTHONPATH=projects/omegaclaw/worktrees/protocosmo2-phase6-live:. python3 -m pytest -q tests/test_protocosmo2_supervisor.py tests/test_protomega_outer_supervisor.py tests/test_omegaclaw_watchdog.py projects/omegaclaw/protocosmo2/tests/test_live_runtime_prompt.py projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary.py projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary_telegram.py`
  -> 99 passed.
- `python3 -m py_compile` for the runner and focused test passed.
- Scoped `git diff --check` passed.

## Remaining acceptance

Production remains unchanged. A guarded restart must load the pinned repair, preserve
schema-3 durable state and exactly-one-receiver topology, and pass a fresh ordinary
long-message Telegram canary. Until then, full-utilization acceptance remains withdrawn
and petta-memory handoff remains paused.

## Guarded production restart

- Ben explicitly authorized the restart in Telegram source message 17899.
- Pre-restart state snapshot SHA-256:
  `874fe5e8eb1c839cb48dcb0c458c9b00244bf1616bfb7d122126aaa1a53212c5`.
- The protected schema/identity/cursor/processed/outbox/pending/context/deferred
  projection matched before and immediately after restart at SHA-256
  `c7a211a80261b729590fc45ad3d8666343fc225896ad71a8b339209ecef6f71d`.
- New identity-bound owner: PID 2682018; exactly one receiver child: PID 2682031.
- Schema 3 and deferred mode remain active; no rollback marker was present.
- Independent post-command cutover-lock acquisition passed. The first in-command lock
  probe correctly failed because the cutover coordinator still owned descriptor 9; the
  coordinator then exited and released it.
- Process readiness passed. End-to-end acceptance remains open pending one fresh ordinary
  long-message Telegram canary that exercises the message-848 failure shape.
