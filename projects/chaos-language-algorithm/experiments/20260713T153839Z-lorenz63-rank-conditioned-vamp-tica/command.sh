#!/usr/bin/env bash
set -euo pipefail
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
python3 -m chaoslang.benchmarks.rank_conditioned_lorenz63 \
  --output-dir "$PWD/../../experiments/20260713T153839Z-lorenz63-rank-conditioned-vamp-tica" \
  --steps 2048 --discard 2048 --lift-dimension 256 \
  --trajectory-seeds 101,202,303 --ranks 3,10 --dimensions 2,3 \
  --lags 1,4,16 --microstates 8,16 --block-lengths 4,16 \
  --surrogates 20 --iterations 1
