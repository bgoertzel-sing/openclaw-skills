#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T221117Z-e4-non-label-equivalent-confirmation
python_bin=/home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python
cd "$repo"
export PYTHONPATH="$repo/src"
for seed in 27449 28559 29669 30781 31891; do
  "$python_bin" scripts/run_e4_non_label_constraints.py \
    --base-config configs/e3_partial_student_v1.json \
    --constraints configs/e4_non_label_constraints_calibration_v1.json \
    --seed "$seed" \
    --output "$run/artifacts/seed_${seed}.json"
done
"$python_bin" scripts/summarize_e4_non_label_constraints.py \
  --inputs \
    "$run/artifacts/seed_27449.json" \
    "$run/artifacts/seed_28559.json" \
    "$run/artifacts/seed_29669.json" \
    "$run/artifacts/seed_30781.json" \
    "$run/artifacts/seed_31891.json" \
  --thresholds configs/e4_non_label_constraints_confirmation_frozen_v1.json \
  --output "$run/artifacts/result.json"
