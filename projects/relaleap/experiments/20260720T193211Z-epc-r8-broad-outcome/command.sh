#!/usr/bin/env bash
set -euo pipefail

cd /workspace/relaleap
python3 -m pip install --break-system-packages \
  transformers==4.57.6 datasets==4.0.0 safetensors==0.8.0 pytest==8.4.2

python3 -m pytest -q \
  tests/test_r8_battery.py \
  tests/test_outcome_probes.py \
  tests/test_representation_diagnostics.py

python3 scripts/run_gpt2_r8_train.py \
  --protocol configs/gpt2_epc_r8.json \
  --output results/r8/train \
  --device cuda \
  --source-commit 9ccb151

python3 scripts/run_gpt2_r8_outcomes.py \
  --protocol configs/gpt2_epc_r8.json \
  --checkpoints results/r8/train/checkpoints \
  --output results/r8/outcomes.json \
  --device cuda
