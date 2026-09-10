#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v python3 run_carom_e2_e3.py --outdir /home/openclaw/research-agent/projects/carom/experiments/e2-e3-smoke-artifacts-temp --seeds 7 17 --steps 4 --batch-size 8 --eval-size 64 --eval-batch-size 32 --d 16 --K 4 --controller-steps 8 
