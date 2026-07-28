#!/usr/bin/env bash
set -u
repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
cd "$repo" || exit 97
/usr/bin/time -v -o /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T071500Z-vector-recurrence-attractor-v1/timing.txt \
  env PYTHONPATH=src python3 -m chaoslang.benchmarks.vector_recurrence_attractor \
  > /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T071500Z-vector-recurrence-attractor-v1/results.json \
  2> /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T071500Z-vector-recurrence-attractor-v1/stderr.txt
status=$?
printf '%s\n' "$status" > /home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T071500Z-vector-recurrence-attractor-v1/exit-status.txt
exit "$status"
