#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src python3 scripts/run_pcstep_gpu_smoke.py \
  --output results/gpu_smoke.json \
  --revision 607a30d783dfa663caf39e06633721c8d4cfcd7e \
  --seed 1729 \
  --sequence-length 16
