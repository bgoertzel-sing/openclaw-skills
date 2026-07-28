#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 -m pytest tests/test_hdpc_tinyshakespeare.py -q 
