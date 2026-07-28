#!/usr/bin/env bash
set -o pipefail
cd ../../../omegaclaw/workspace/relaleap-v4/comcrit/comcrit
export PYTHONPATH=src
python3 examples/v4_functional_gate_torch.py \
  --output ../../../../../relaleap/experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/artifacts/results.json
