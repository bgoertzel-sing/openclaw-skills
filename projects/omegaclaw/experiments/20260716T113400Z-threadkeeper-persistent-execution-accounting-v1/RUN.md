# ThreadKeeper persistent execution accounting v1

- UTC: `2026-07-16T11:34:00Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Implementation commit: `c1f7b57d274d808a27066bc3826153b2a503508e`
- Documentation head: `a756315bcfa99e901975a944d13709423e31ad52`
- Result: pass

## Change

The bounded queue runner now emits compact, mechanically observed execution
usage alongside token usage: attempted non-`emit` tool calls and wall-clock
runtime rounded up to whole seconds. Persistent attempt-result receipts verify
and bind all five counters before the existing crash-retry-safe ledger append.
Malformed, negative, boolean, or extra execution fields fail closed. Older
token-only queue results remain replayable.

## Checks

- `python3 -m py_compile src/persistent_worker.py src/subagent.py`
- focused lifecycle/subagent/budget gate: `356 passed in 2.93s`
- `git diff --check`
- clean isolated worktree after commits

## Claim boundary

This establishes provider-free accounting plumbing, not a live worker or
supervisor deployment. No provider, paid compute, queue/supervisor process,
Telegram, credential, ProtoMegaBot/ProtoMegaBot2 process, production path,
push, merge, force-push, or security/access change was used.

Next: a provider-free supervisor integration gate that exercises restart,
cancellation, and budget-exhaustion boundaries against synthetic queue results;
only after that consider an isolated ProtoMegaBot2 canary under separate
approval.
