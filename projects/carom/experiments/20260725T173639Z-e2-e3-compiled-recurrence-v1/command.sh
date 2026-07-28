#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
python3 -m pytest test_e0_e1.py test_e2_e3.py test_e2_e3_compile.py -q
python3 benchmark_e2_e3_compile.py \
  --device cpu \
  --output /home/openclaw/research-agent/projects/carom/experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/artifacts/cpu-compile-benchmark.json
