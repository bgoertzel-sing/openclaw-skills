#!/usr/bin/env bash
set -o pipefail
/usr/bin/time -p python3 -m chaoslang.benchmarks.phase1_sweep \
  --output-dir ../../experiments/20260712T200200Z-lorenz63-r256-deeptime-multiseed \
  --steps 192 --discard 64 --lift-dimension 256 --noise 0.001 \
  --seeds 101,202,303 --embedding-dims 3,5 --microstates 8,16,24 --lags 1,3 \
  --iterations 2 --surrogates 2
