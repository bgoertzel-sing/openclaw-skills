#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T224751Z-e4-symbolic-extractor-calibration
python_bin=/home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python
exec > >(tee "$run/stdout.log") 2> >(tee "$run/stderr.log" >&2)
cd "$repo"
export PYTHONPATH="$repo/src:$repo"
for seed in 33013 34123 35227; do
  /usr/bin/time -v -o "$run/artifacts/time_${seed}.txt" \
    "$python_bin" scripts/run_e4_symbolic_extractor.py \
      --base-config configs/e3_partial_student_v1.json \
      --extractor-config configs/e4_symbolic_extractor_calibration_v1.json \
      --seed "$seed" \
      --output "$run/artifacts/seed_${seed}.json"
done
"$python_bin" scripts/summarize_e4_symbolic_extractor.py \
  --inputs \
    "$run/artifacts/seed_33013.json" \
    "$run/artifacts/seed_34123.json" \
    "$run/artifacts/seed_35227.json" \
  --output "$run/artifacts/result.json"
