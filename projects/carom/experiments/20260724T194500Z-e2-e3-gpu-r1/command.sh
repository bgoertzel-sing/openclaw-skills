#!/usr/bin/env bash
set -euo pipefail
cd /workspace/carom-e2-e3/source
python3 run_carom_e2_e3.py \
  --outdir /workspace/carom-e2-e3/results \
  --seeds 7 17 27 37 47 \
  --steps 3000 \
  --batch-size 128 \
  --eval-size 2048 \
  --eval-batch-size 256 \
  --eval-seed 20260720 \
  --lr 0.002 \
  --d 64 \
  --K 16 \
  --controller-steps 70 \
  --noise 0.02 \
  --device cuda
