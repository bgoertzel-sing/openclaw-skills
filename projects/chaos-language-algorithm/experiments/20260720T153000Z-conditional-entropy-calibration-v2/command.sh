#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/scratch/chaoslang-strict-replay
python3 -m chaoslang.benchmarks.conditional_entropy_calibration
