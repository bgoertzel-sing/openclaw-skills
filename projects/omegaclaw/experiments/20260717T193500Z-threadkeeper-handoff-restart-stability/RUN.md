# ThreadKeeper handoff-required restart-stability gate

- Date: `2026-07-17T19:35:00Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Commit: `8c106b6` (`Test handoff-required supervisor restart stability`)
- Base coordination: branch retains draft PR #1 safety-floor ancestry and changes only the isolated persistent-worker test suite.
- Result: succeeded; lifecycle `57 passed`, combined provider-free gate `370 passed`.

## Result

A new regression runs two fresh bounded supervisor passes against the same
`FAILED_RETRYABLE` task with no formal handoff. Both passes return the same
`handoff_required` outcome, leave the task retryable, and cause zero enqueue
effects. This establishes restart-stable fail-closed behavior for a
crash-before-handoff case; it does not establish a liveness/recovery policy.

Python compilation, the focused lifecycle suite, the combined
lifecycle/subagent/budget gate, and `git diff --check` passed. No provider,
live queue, Telegram, ProtoMegaBot path, paid compute, secret/access change,
push, merge, force-push, or remote-ref deletion was used.

## Next bounded gate

Specify provider-free operator dispositions for a task stranded before a
formal handoff. The policy must not fabricate a handoff or silently resume
from an older checkpoint; cancellation/abandonment and an explicitly reviewed
restart-from-known-input path should remain distinct auditable actions.
