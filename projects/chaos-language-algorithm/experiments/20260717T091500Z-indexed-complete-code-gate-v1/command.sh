#!/usr/bin/env bash
set -euo pipefail

export PYTHONPATH="/home/openclaw/research-agent/scratch/chaoslang-strict-replay/src"
cd "/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T091500Z-indexed-complete-code-gate-v1"
python3 -m chaoslang.benchmarks.indexed_code_gate > results.json 2> stderr.txt
