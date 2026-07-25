#!/usr/bin/env bash
set -euo pipefail
repo="/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1"
output="/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260725T020759Z-e4-cmcp-typed-retention-smoke"
cd "$repo"
export PYTHONPATH="src"
python3 -m pytest -q \
  tests/test_e4_cmcp_store.py \
  tests/test_e4_cmcp.py \
  tests/test_e4_cmcp_persistent.py
/usr/bin/time -v python3 scripts/run_e4_cmcp_typed_retention.py \
  --config configs/e4_cmcp_typed_retention_calibration_v1.json \
  --seed 61001 \
  --output "$output/artifacts/seed-61001.json"
