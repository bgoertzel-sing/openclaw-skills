#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare
PYTHONPATH=src python3 -m hdpc_tiny_shakespeare.sweep_lambda \
  --output /home/openclaw/research-agent/projects/hdpc-tiny-shakespeare/experiments/20260715T042000Z-lambda-T-sweep/artifacts/sweep_results.json \
  --lambdas 0.01 0.02 0.03 0.05 \
  --Ts 1 2 4
