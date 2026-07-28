#!/bin/sh
set -eu
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
cd /home/openclaw/research-agent/scratch/chaoslang-strict-replay
/usr/bin/time -v -o /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260716T172310Z-frozen-heldout-calibration-v1/timing.txt \
  python3 -m chaoslang.benchmarks.frozen_heldout \
    --steps 512 --discard 1024 --bins 8 --train-fraction 0.7 \
  > /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260716T172310Z-frozen-heldout-calibration-v1/results.json \
  2> /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260716T172310Z-frozen-heldout-calibration-v1/stderr.txt
