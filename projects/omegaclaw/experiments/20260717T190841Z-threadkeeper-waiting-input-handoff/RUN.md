# ThreadKeeper WAITING_INPUT formal-handoff gate

- Date: `2026-07-17T19:08:41Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Commit: `50aaaa2` (`Require handoff before persistent inbox resume`)
- Base coordination: draft PR #1 safety-floor ancestry verified locally.
- Result: succeeded; `369 passed in 2.94s`.

## Result

`consume_inbox_item` now verifies the bounded checkpoint chain and requires
its newest checkpoint to be a formal handoff from the current durable attempt
before enqueue or consumption-receipt replay. Provider-free regressions prove
that a missing handoff and a newer opaque checkpoint both leave the task in
`WAITING_INPUT` and cause zero queue calls.

Python compilation, the 56-test persistent lifecycle suite, the combined
369-test lifecycle/subagent/budget gate, and `git diff --check` passed. No
provider, live queue, Telegram, ProtoMegaBot path, paid compute, secret/access
change, push, merge, force-push, or remote-ref deletion was used.
