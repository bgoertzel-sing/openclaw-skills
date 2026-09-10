#!/usr/bin/env bash
set -euo pipefail

export PYTHONPATH="/home/openclaw/research-agent/scratch/chaoslang-strict-replay/src"
cd "/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260716T191500Z-joint-chunk-category-diagnostic-v1"
python3 -m chaoslang.benchmarks.joint_diagnostic > results.json 2> stderr.txt
