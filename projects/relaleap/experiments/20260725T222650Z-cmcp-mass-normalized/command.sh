#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260725T222650Z-cmcp-mass-normalized
python=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
for seed in 101 211 307; do
  PYTHONPATH="$repo/src" "$python" "$repo/scripts/run_cmcp_epc_kd_bridge.py" \
    --seed "$seed" --train-updates 160 --normalize-weights \
    --output "$run/artifacts/normalized-seed${seed}.json"
done
