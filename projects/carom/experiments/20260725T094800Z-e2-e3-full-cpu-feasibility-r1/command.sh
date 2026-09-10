#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v python3 run_carom_e2_e3.py --outdir /home/openclaw/research-agent/projects/carom/experiments/e2-e3-full-slice-temp --seeds 7 --steps 1 --batch-size 128 --eval-size 2048 --eval-batch-size 256 --eval-seed 20260720 --lr 0.002 --d 64 --K 16 --controller-steps 70 --noise 0.02 --device cpu 
