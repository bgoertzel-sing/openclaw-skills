#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers
/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest -q tests/test_subagent_hardening.py tests/test_persistent_worker_lifecycle.py 
