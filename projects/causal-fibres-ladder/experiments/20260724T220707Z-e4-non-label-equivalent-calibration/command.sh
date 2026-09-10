#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T220707Z-e4-non-label-equivalent-calibration
python_bin=/home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python
cd "$repo"
export PYTHONPATH="$repo/src"
for seed in 24109 25219 26339; do
  "$python_bin" scripts/run_e4_non_label_constraints.py \
    --base-config configs/e3_partial_student_v1.json \
    --constraints configs/e4_non_label_constraints_calibration_v1.json \
    --seed "$seed" \
    --output "$run/artifacts/seed_${seed}.json"
done
"$python_bin" scripts/summarize_e4_non_label_constraints.py \
  --inputs \
    "$run/artifacts/seed_24109.json" \
    "$run/artifacts/seed_25219.json" \
    "$run/artifacts/seed_26339.json" \
  --output "$run/artifacts/result.json"
