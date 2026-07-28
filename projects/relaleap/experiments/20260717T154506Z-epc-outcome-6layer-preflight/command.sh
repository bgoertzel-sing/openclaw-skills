#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
bash -lc PYTHONPATH=src\ python3\ -m\ pytest\ tests/\ -q\ \&\&\ python3\ -m\ py_compile\ scripts/run_gpt2_outcome_gpu.py\ scripts/run_gpt2_pilot_gpu.py\ \&\&\ git\ diff\ --check 
