#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260725T224500Z-cmcp-estimator-calibration
python=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
for estimator in response gradient; do
  for seed in 101 211 307; do
    PYTHONPATH="$repo/src" "$python" "$repo/scripts/run_cmcp_epc_kd_bridge.py" \
      --seed "$seed" --train-updates 160 --normalize-weights \
      --fixture complementary --cmcp-estimator "$estimator" \
      --output "$run/artifacts/calibration-${estimator}-seed${seed}.json"
  done
done
