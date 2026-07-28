# Persistent-worker supervisor subprocess restart v1

- Time: `2026-07-16 19:38 UTC`
- Gate status: `pass` for the synthetic restart slice
- GGB capacities: `3.1, 3.2, 3.4, 3.5, 4.1, 5.1, 5.2, 5.5`
- Source: ThreadKeeper branch `agent/threadkeeper-persistent-workers`, commit
  `c06725e`

## Contract

Prove that the bounded provider-free reconciliation state survives real Python
interpreter exit. Use temporary durable state and fake callbacks only. After an
expired attempt is recovered and explicitly requeued, a fresh supervisor caller
with cancellation asserted must not repeat enqueue or call the queue runner.

## Evidence

`tests/persistent_supervisor_subprocess.py` is invoked in three independent
interpreter lifetimes. The first creates a `CLAIMED` task with an expired lease;
the second returns `recover_requeue`; the third observes cancellation before
claim. A fourth read-only status invocation confirms `QUEUED`. The bounded
effect journal contains exactly one enqueue record and no runner record.

Commands and results:

```text
/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m pytest -q tests/test_persistent_worker_lifecycle.py
# 48 passed in 0.56s

/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m pytest -q tests/test_persistent_worker_lifecycle.py \
  Autotests/mock/test_subagent_hardening_mock.py \
  Autotests/mock/test_threadkeeper_budget_hardening_mock.py
# 361 passed in 2.67s

python3 -m py_compile src/persistent_worker.py \
  tests/test_persistent_worker_lifecycle.py \
  tests/persistent_supervisor_subprocess.py
git diff --check
# pass
```

## Claim boundary and next task

This proves restart persistence for one synthetic recover/requeue/cancel path.
It does not prove signal handling, concurrent-supervisor exclusion, deployed
wrapper behavior, or live queue/provider operation. Next add an exclusive-owner
or concurrent-invocation gate before considering a supervisor wrapper.

No live egress, memory write/promotion, paid compute, secret access, push,
merge, runtime deployment, or ProtoMegaBot/ProtoMegaBot2 path/process change
occurred.
