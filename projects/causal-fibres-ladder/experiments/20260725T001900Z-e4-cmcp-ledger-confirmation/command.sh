#!/usr/bin/env bash
set -euo pipefail

repo="/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1"
output="/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260725T001900Z-e4-cmcp-ledger-confirmation"
cd "$repo"
export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}src"
config="configs/e4_cmcp_ledger_calibration_v1.json"
thresholds="configs/e4_cmcp_ledger_confirmation_frozen_v1.json"
seeds=(54311 55439 56543 57649 58757)
inputs=()

for seed in "${seeds[@]}"; do
  artifact="$output/artifacts/seed-${seed}.json"
  python3 scripts/run_e4_cmcp_ledger.py \
    --config "$config" \
    --seed "$seed" \
    --output "$artifact"
  inputs+=("$artifact")
done

python3 scripts/summarize_e4_cmcp_ledger.py \
  --inputs "${inputs[@]}" \
  --thresholds "$thresholds" \
  --output "$output/artifacts/result.json"
