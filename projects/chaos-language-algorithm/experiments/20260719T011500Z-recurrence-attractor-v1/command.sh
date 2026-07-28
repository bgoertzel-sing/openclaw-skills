#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=/home/openclaw/research-agent/scratch/chaoslang-strict-replay/src
cd /home/openclaw/research-agent/scratch/chaoslang-strict-replay
/usr/bin/time -f 'wall_seconds=%e\nmax_rss_kib=%M' -o /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T011500Z-recurrence-attractor-v1/timing.txt \
  python3 -m chaoslang.benchmarks.recurrence_attractor \
  > /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T011500Z-recurrence-attractor-v1/results.json \
  2> /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T011500Z-recurrence-attractor-v1/stderr.txt
