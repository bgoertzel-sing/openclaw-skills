#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v python3 run_carom_e2_e3.py --outdir /home/openclaw/research-agent/projects/carom/experiments/e2-e3-fixture-artifacts-temp --seeds 7 17 27 37 47 --steps 40 --batch-size 32 --eval-size 128 --eval-batch-size 64 --d 24 --K 8 --controller-steps 12 
