#!/usr/bin/env bash
set -o pipefail
/usr/bin/time -p python3 -m chaoslang.benchmarks.phase1_lorenz63 --steps 256 --discard 64 --lift-dimension 256 --noise 0.001 --embedding-dim 3 --microstates 12 --lag 2 --bins 2 --iterations 4 --surrogates 3 --seed 20260712 --backend pure
