#!/usr/bin/env bash
set -euo pipefail
repo="/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1"
output="/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260725T021200Z-e4-cmcp-typed-retention-calibration"
cd "$repo"
export PYTHONPATH="src"
for seed in 61001 62119 63241; do
  python3 scripts/run_e4_cmcp_typed_retention.py \
    --config configs/e4_cmcp_typed_retention_calibration_v1.json \
    --seed "$seed" \
    --output "$output/artifacts/seed-${seed}.json"
done
