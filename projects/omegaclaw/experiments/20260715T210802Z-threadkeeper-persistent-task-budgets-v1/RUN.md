# ThreadKeeper persistent task budgets v1

- UTC: `2026-07-15T21:08:02Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Commit: `4b7399ef2497b60b3476103fdb5df3a23b612ee4`
- Remote: `fork/agent/threadkeeper-persistent-workers`

## Change

Added strict positive task-budget schema validation plus bounded, append-only,
hash-linked task usage events. Usage records are idempotent by usage ID and
bound to a verified immutable attempt. `budget_status()` reconstructs monotone
attempt/token/time/tool consumption across restarts. Exhausted limits block
claim or explicit requeue before the queue runner/provider/tool effect.

## Checks

- Python compilation
- focused lifecycle/storage pytest: `30 passed`
- combined persistent lifecycle/subagent/budget hardening pytest: `343 passed`
- `git diff --check`
- clean branch after normal push

No provider, paid compute, live queue/supervisor, Telegram, credential,
ProtoMegaBot process, production path, merge, force-push, or remote-ref deletion
was used. Next: make queued-attempt accounting handoff crash-safe, then add
idempotent inbox/result delivery.
