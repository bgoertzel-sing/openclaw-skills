#!/bin/sh
set -eu
cd /home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers
python3 -m py_compile src/persistent_worker.py tests/test_persistent_worker_lifecycle.py
/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest -q tests/test_persistent_worker_lifecycle.py Autotests/mock/test_subagent_hardening_mock.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py
git diff --check
