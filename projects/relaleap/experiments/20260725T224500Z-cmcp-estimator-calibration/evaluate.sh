#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260725T224500Z-cmcp-estimator-calibration
python=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
for seed in 401 503 607; do
  PYTHONPATH="$repo/src" "$python" "$repo/scripts/run_cmcp_epc_kd_bridge.py" \
    --seed "$seed" --train-updates 160 --normalize-weights \
    --fixture complementary --cmcp-estimator response \
    --output "$run/artifacts/evaluation-response-seed${seed}.json"
done
