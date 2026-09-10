#!/usr/bin/env bash
set -euo pipefail
cd projects/omegaclaw/worktrees/threadkeeper-persistent-workers
/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest -q tests/test_persistent_worker_lifecycle.py Autotests/mock/test_subagent_hardening_mock.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py 
