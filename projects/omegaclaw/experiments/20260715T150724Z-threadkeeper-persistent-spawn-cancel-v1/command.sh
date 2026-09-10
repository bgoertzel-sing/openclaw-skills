#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers
bash -lc python3\ -m\ unittest\ tests.test_persistent_worker_lifecycle\ \&\&\ /home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python\ -m\ pytest\ -q\ tests/test_persistent_worker_lifecycle.py\ Autotests/mock/test_subagent_hardening_mock.py\ \&\&\ python3\ -m\ py_compile\ src/persistent_worker.py\ src/subagent.py\ tests/test_persistent_worker_lifecycle.py\ Autotests/mock/test_subagent_hardening_mock.py\ \&\&\ git\ diff\ --check 
