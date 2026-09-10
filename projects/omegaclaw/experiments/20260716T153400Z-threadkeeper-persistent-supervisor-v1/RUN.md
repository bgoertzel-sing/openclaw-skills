# Persistent-worker supervisor reconciliation v1

- Time: `2026-07-16 15:34 UTC`
- Gate status: `partial`
- GGB capacities: `3.1, 3.2, 3.4, 3.5, 4.1, 5.1, 5.2, 5.5`
- Source: ThreadKeeper branch `agent/threadkeeper-persistent-workers`, commit
  `3673e94f3d9a5dd71f3c54f1ba7d783f77e2de03`

## Contract

Implement one bounded, provider-free reconciliation pass. Before any callback,
verify the complete durable status set. For each task, perform no more than one
claim/run or recovery/requeue action. Cancellation, corrupt state, and exhausted
budgets must prevent queue/provider/tool effects. Do not start a supervisor
process or wire ProtoMegaBot, ProtoMegaBot2, Telegram, or a provider.

## Evidence

`supervise_persistent_once` derives operation IDs from verified task versions,
making lifecycle retries stable across a restarted caller. Synthetic fixtures
passed for expired-attempt recovery plus explicit requeue, cancellation before
queue execution, corrupted-event preflight failure with zero callbacks, and
attempt-budget exhaustion with zero enqueue callbacks.

Commands:

```text
python3 -m py_compile src/persistent_worker.py tests/test_persistent_worker_lifecycle.py
python3 -m pytest -q tests/test_persistent_worker_lifecycle.py
# 47 passed in 0.38s

/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m pytest -q tests/test_persistent_worker_lifecycle.py \
  Autotests/mock/test_subagent_hardening_mock.py \
  Autotests/mock/test_threadkeeper_budget_hardening_mock.py
# 360 passed in 2.52s

git diff --check
# pass
```

## Claim boundary and next task

This proves the reconciliation logic and callback boundary in one Python
process. It does not yet prove persistence across interpreter exit, process
signals, concurrent supervisors, or a deployed supervisor wrapper. The next
small gate is a synthetic subprocess restart harness over temporary state,
still with fake queue callbacks and no live runtime authority.

No live egress, memory write/promotion, paid compute, secret access, push,
merge, runtime deployment, or production path/process change occurred.
