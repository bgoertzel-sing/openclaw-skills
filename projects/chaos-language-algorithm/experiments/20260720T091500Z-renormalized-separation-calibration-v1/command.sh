#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
export PYTHONPATH="$repo/src"
cd "$repo"
python3 -m chaoslang.benchmarks.renormalized_separation_calibration
