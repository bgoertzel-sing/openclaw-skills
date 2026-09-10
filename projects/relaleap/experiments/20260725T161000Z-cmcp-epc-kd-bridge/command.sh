#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
cd "$repo"
for bridge_seed in 101 211 307; do
  PYTHONPATH=src python3 scripts/run_cmcp_epc_kd_bridge.py \
    --seed "$bridge_seed" \
    --train-updates 160 \
    --output "/home/openclaw/research-agent/projects/relaleap/experiments/20260725T161000Z-cmcp-epc-kd-bridge/artifacts/calibration-seed${bridge_seed}-u160-contradictory-v4.json"
done
