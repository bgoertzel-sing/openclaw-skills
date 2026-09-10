#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 scripts/run_epc_representation_audit.py --checkpoints /home/openclaw/research-agent/projects/relaleap/experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints --output /home/openclaw/research-agent/projects/relaleap/experiments/epc-correctness-audit-output-v2.json 
