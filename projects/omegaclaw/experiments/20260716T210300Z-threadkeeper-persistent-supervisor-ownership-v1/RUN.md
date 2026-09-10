# Persistent-worker exclusive supervisor ownership v1

- Time: `2026-07-16 21:03 UTC`
- Gate status: `pass` for the provider-free concurrent-invocation slice
- Source: ThreadKeeper branch `agent/threadkeeper-persistent-workers`, commit
  `e7e997e`

## Contract and evidence

`supervise_persistent_once` now acquires a non-blocking root-scoped OS file
lock before durable-state preflight or callbacks. Concurrent passes and hosts
without the locking primitive fail closed before queue/runner effects. The lock
path uses the persistent store's regular-file/no-symlink guard, and process
exit releases ownership.

A subprocess regression holds the first supervisor inside its fake enqueue
callback, invokes a second independent interpreter, and proves the contender
fails with `already active` while the effect journal remains absent. Releasing
the owner produces exactly one enqueue effect and a durable `QUEUED` state.

Commands and results:

```text
/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m pytest -q tests/test_persistent_worker_lifecycle.py
# 49 passed in 0.70s

/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m pytest -q tests/test_persistent_worker_lifecycle.py \
  Autotests/mock/test_subagent_hardening_mock.py \
  Autotests/mock/test_threadkeeper_budget_hardening_mock.py
# 362 passed in 2.93s

/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python \
  -m py_compile src/persistent_worker.py \
  tests/test_persistent_worker_lifecycle.py \
  tests/persistent_supervisor_subprocess.py
git diff --check
# pass
```

No live queue, provider, Telegram, ProtoMegaBot/ProtoMegaBot2 path or process,
paid compute, credential/access change, push, merge, force-push, or remote-ref
deletion occurred. A deployed supervisor wrapper or canary still requires a
separate approval gate.
