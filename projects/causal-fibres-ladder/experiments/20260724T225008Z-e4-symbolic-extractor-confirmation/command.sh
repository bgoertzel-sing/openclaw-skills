#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T225008Z-e4-symbolic-extractor-confirmation
python_bin=/home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python
exec > >(tee "$run/stdout.log") 2> >(tee "$run/stderr.log" >&2)
cd "$repo"
export PYTHONPATH="$repo/src:$repo"
for seed in 36341 37447 38557 39671 40787; do
  /usr/bin/time -v -o "$run/artifacts/time_${seed}.txt" \
    "$python_bin" scripts/run_e4_symbolic_extractor.py \
      --base-config configs/e3_partial_student_v1.json \
      --extractor-config configs/e4_symbolic_extractor_calibration_v1.json \
      --seed "$seed" \
      --output "$run/artifacts/seed_${seed}.json"
done
"$python_bin" scripts/summarize_e4_symbolic_extractor.py \
  --inputs \
    "$run/artifacts/seed_36341.json" \
    "$run/artifacts/seed_37447.json" \
    "$run/artifacts/seed_38557.json" \
    "$run/artifacts/seed_39671.json" \
    "$run/artifacts/seed_40787.json" \
  --output "$run/artifacts/result.json" \
  --thresholds configs/e4_symbolic_extractor_confirmation_frozen_v1.json
