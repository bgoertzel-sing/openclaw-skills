# ThreadKeeper handoff-blocked operator dispositions

- Date: `2026-07-17T21:07:50Z`
- Branch: `agent/threadkeeper-persistent-workers`
- Commit: `f09c621`
- Scope: provider-free persistent-worker lifecycle only

## Result

Added immutable, self-hashed operator dispositions for retryable tasks whose
newest checkpoint is not a formal handoff. The bounded actions are `hold`,
`request_cancel`, `fail_terminal`, and `expire`. Records bind the task version,
manifest digest, newest checkpoint identity/digest when present, actor,
rationale, and bounded evidence references. They are persisted before any
lifecycle effect, replay idempotently after a crash, and cannot create a
handoff, select an older checkpoint, or enqueue work.

## Checks

- `python3 -m py_compile src/persistent_worker.py tests/test_persistent_worker_lifecycle.py`
- Lifecycle pytest: `62 passed`
- Combined provider-free lifecycle/subagent/budget pytest: `375 passed`
- `git diff --check`

No provider, live queue, Telegram, ProtoMegaBot, paid compute, secrets/access
change, push, merge, force-push, or remote-ref deletion was used.
