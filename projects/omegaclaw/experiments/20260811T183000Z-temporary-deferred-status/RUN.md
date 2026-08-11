# Temporary deferred-status replies

- Started: 2026-08-11T18:30:00Z
- Status: staging implementation complete and locally validated; independent review and production deployment open
- Scope: ProtoCosmo2, Protomega, and Protomega2 shared Telegram transport
- Baseline transport commit: `df06c29`

## Deliverable

Replace permanent deferred acknowledgements with the temporary reply
`Formulating my response...`. Persist the exact Telegram receipt against the
immutable deferred task, deliver the correlated final result or bounded
failure first, and then delete only that recorded status message.

## Invariants and acceptance

- Status and final replies retain the original chat/message routing envelope.
- A task executes once across fast-grace promotion and explicit background
  admission.
- Deletion is eligible only after the correlated final/failure delivery has a
  durable receipt.
- The delete target is exactly the status receipt recorded for that task; an
  unrelated message ID or chat ID can never be selected.
- Delete retries are idempotent across process crashes and Telegram's
  already-absent response.
- Crash recovery preserves visible bounded failure behavior and eventually
  cleans an already-delivered temporary status.

## Staging result

The shared transport now emits exactly `Formulating my response...` for both
explicit persistent admission and fast-grace promotion. It records the
Telegram status receipt on the immutable deferred task. Only after the
correlated final result or bounded failure has its own durable delivery receipt
does the transport select that exact chat/message pair for deletion. A
successful deletion is durably marked; a crash between Telegram deletion and
the marker safely retries, accepting only Telegram's exact bounded
`message to delete not found` response as already complete.

Provider-free regressions cover task/chat/message mismatch rejection,
post-final eligibility, restart retry, repeat-call idempotency, unrelated
message preservation, one-execution promotion, explicit persistent work, and
exact Telegram absent-versus-other-400 behavior.

- Focused contract/transport suite: `114 passed in 1.42s`.
- Full provider-free suite: `148 passed in 1.61s`.
- Python compilation passed for the contract, transport, and production runner.
- Staging and scoped workspace `git diff --check` passed.
- Production remained unchanged.

## Next command

Obtain separate frontier-model review of the exact clean staging commits. If
it passes, request authorization for guarded restarts of ProtoCosmo2,
Protomega, and Protomega2 and require a fresh externally initiated slow-turn
trace on each identity before acceptance.

## Evidence path

This record, the exact staging commit, test output, and any later guarded
production acceptance artifacts.
