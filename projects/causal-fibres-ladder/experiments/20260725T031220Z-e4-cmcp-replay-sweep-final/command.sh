#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e4_cmcp_replay_sweep.py --config configs/e4_cmcp_replay_sweep_v1.json --output /home/openclaw/research-agent/projects/causal-fibres-ladder/artifacts/e4-cmcp-replay-sweep-v1.json 
