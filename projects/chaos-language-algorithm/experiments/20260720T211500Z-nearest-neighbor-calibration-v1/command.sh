#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=/home/openclaw/research-agent/scratch/chaoslang-strict-replay/src
python3 -m chaoslang.benchmarks.nearest_neighbor_calibration
