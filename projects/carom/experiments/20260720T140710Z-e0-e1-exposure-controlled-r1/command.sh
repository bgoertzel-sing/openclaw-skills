#!/usr/bin/env bash
set -euo pipefail
python3 /workspace/carom/run_carom_e0_e1.py \
  --outdir /workspace/carom/results/e0_e1_r1 \
  --seeds 7 17 27 37 47 \
  --steps 3000 \
  --batch-size 128 \
  --eval-size 2048 \
  --eval-batch-size 256 \
  --eval-seed 20260720 \
  --d 64 \
  --K 16 \
  --controller-steps 70 \
  --log-every 100
