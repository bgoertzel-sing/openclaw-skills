#!/usr/bin/env bash
set -euo pipefail
python3 run_a6.py --condition 1 --timesteps 120 --seed 20260701 --noise 0.01 --outdir runs/condition-1-smoke
