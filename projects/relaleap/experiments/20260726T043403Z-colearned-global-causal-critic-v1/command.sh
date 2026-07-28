#!/usr/bin/env bash
set -euo pipefail

cd /home/openclaw/research-agent/projects/relaleap/worktrees/colearned-causal-critic-v1

PYTHONPATH=src python3 -m pytest tests/test_causal_critic.py -q
PYTHONPATH=src:. /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python -m pytest tests/ -q
python3 -m py_compile src/relaleap/hdpc/causal_critic.py tests/test_causal_critic.py
git diff --check
