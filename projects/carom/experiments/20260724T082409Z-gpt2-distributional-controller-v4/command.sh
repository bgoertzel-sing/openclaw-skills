#!/usr/bin/env bash
set -euo pipefail

# BLOCKED until REMOTE_JOB.md is explicitly marked APPROVED and local preflight
# passes. The remote command will run from /workspace/carom-gpt2-controller-v4.
python3 run_carom_gpt2_distributional_controller_v4.py \
  --checkpoint step_4000.pt \
  --output artifacts/results.json \
  --seed 2407 \
  --base-updates 2000 \
  --checkpoint-every 500 \
  --calibration-branches 12 \
  --heldout-branches 4 \
  --branch-updates 8
