#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
export PYTHONPATH=src
run_dir=/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T234609Z-e4-textlike-calibration-channel-matched
for seed in 42013 43117 44221; do
  /usr/bin/time -f '%e seconds' -o "$run_dir/artifacts/time_${seed}.txt" \
    python3 scripts/run_e4_textlike_bridge.py \
      --config configs/e4_textlike_bridge_calibration_v1.json \
      --seed "$seed" \
      --output "$run_dir/artifacts/seed_${seed}.json"
done
python3 scripts/summarize_e4_textlike_bridge.py \
  --inputs "$run_dir"/artifacts/seed_*.json \
  --output "$run_dir/artifacts/result.json"
