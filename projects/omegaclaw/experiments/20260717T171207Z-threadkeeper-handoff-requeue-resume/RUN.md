# ThreadKeeper formal-handoff requeue/process-resume gate

- Date: `2026-07-17T17:12:07Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Commit: `35bf3b1` (`Require formal handoff before persistent requeue`)
- Base coordination: draft PR #1 safety-floor ancestry verified locally.
- Result: succeeded; `367 passed in 2.89s`.

## Question

Can an expired persistent attempt be requeued only when its newest immutable
checkpoint is a formal handoff, and can a fresh process reconstruct the next
action solely from verified durable records and a referenced project file?

## Result

`requeue_persistent` now fails before enqueue when the checkpoint chain is
empty or its newest checkpoint is not a strict formal handoff. The supervisor
reports `handoff_required` and leaves the task `FAILED_RETRYABLE`. A
provider-free fixture uses three separate Python interpreters for initial
work/process exit, stale-attempt recovery/requeue, and resume. The final
interpreter verifies the manifest/checkpoint/handoff chain and reconstructs
`durable-state-v1` from the handoff's `project/state.txt` evidence reference.

Python compilation, the 54-test persistent lifecycle suite, the combined
367-test lifecycle/subagent/budget gate, and `git diff --check` passed. No
provider, live queue, Telegram, ProtoMegaBot path, paid compute, secret/access
change, merge, force-push, or remote-ref deletion was used.
