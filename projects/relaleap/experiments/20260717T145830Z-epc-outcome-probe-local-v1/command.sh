#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 scripts/run_epc_outcome_probe.py --config configs/epc_outcome_probe_local.json --data-dir data/tinyshakespeare --output results/epc_outcome_probe_local_v1.json --device cpu 
