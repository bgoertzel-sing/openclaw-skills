#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260725T230300Z-cmcp-epc-ablation
python=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
for mode in epc direct; do
  for seed in 701 809 907; do
    PYTHONPATH="$repo/src" "$python" "$repo/scripts/run_cmcp_epc_kd_bridge.py" \
      --seed "$seed" --train-updates 160 --normalize-weights \
      --fixture complementary --cmcp-estimator response \
      --distillation-mode "$mode" \
      --output "$run/artifacts/${mode}-seed${seed}.json"
  done
done
