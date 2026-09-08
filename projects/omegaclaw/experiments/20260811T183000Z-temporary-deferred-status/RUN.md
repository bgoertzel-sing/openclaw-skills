# Temporary deferred-status replies

- Started: 2026-08-11T18:30:00Z
- Status: PASS — independently reviewed, guarded-deployed, and externally accepted
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

## Independent review and repair

Independent review BLOCKED the first exact candidate (`215a344` + `f6cec1e`).
Deletion ran before Telegram polling, so any non-absent deletion failure could
abort every cycle and wedge ingress forever on the same stale target.

Transport commit `93fc721` closes that blocker. A failed deletion now records
task/chat/message-bound attempts, retry time, and an incident without marking
the status deleted. Polling continues, backed-off targets cannot starve later
cleanup, and retry state survives restart. The exact already-absent Telegram
response remains the only failure response treated as successful deletion.

- Corrected focused suite: `116 passed`.
- Full isolated suite: `149 passed`; one unrelated layout test failed because
  its hard-coded repository-relative driver path is absent in the detached
  review worktree.
- Compilation and `git diff --check`: passed.
- Independent re-review: PASS, including an additional restart/starvation
  adversarial reproduction.

## Guarded deployment

At approximately 14:34 PDT, ProtoCosmo2, Protomega, and Protomega2 were
restarted onto exact runner `215a344` and transport `93fc721`. Each identity
has exactly one supervisor-owned receiver; pending ingress, active deferred
jobs, and unsent outbox counts were all zero. Restart cursors were preserved at
`387572913`, `940522440`, and `491553089`, respectively. ProtoCosmo2 retained
its independently reviewed long-reply driver `42c0461`; the other two retained
their reviewed baseline driver. External acceptance remains open pending one
fresh slow/deferred human request on each identity.

## Next command

No further acceptance action. Preserve runner `215a344` and transport
`93fc721` as the rollback/promotion pair.

## External acceptance

Ben confirmed the behavior works. Durable state independently binds one fresh
temporary-status lifecycle for each identity:

- ProtoCosmo2: source `1038`, temporary receipt `1039`, completed result, and
  non-null `status_deleted_at` (`1786485211`).
- Protomega: source `9929`, temporary receipt `9930`, completed result, and
  non-null `status_deleted_at` (`1786485270`).
- Protomega2: source `323`, temporary receipt `324`, bounded terminal failure,
  and non-null `status_deleted_at` (`1786485250`).

All three have zero status receipts left eligible-but-undeleted. This accepts
the requested invariant for both successful and bounded-failure terminal paths.

## Evidence path

This record, the exact staging commit, test output, and any later guarded
production acceptance artifacts.
