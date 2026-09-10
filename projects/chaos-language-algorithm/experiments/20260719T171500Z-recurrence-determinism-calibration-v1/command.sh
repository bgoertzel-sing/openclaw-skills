#!/usr/bin/env bash
set -u
repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
ledger=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260719T171500Z-recurrence-determinism-calibration-v1
cd "$repo" || exit 97
/usr/bin/time -v -o "$ledger/timing.txt" env PYTHONPATH=src python3 -m chaoslang.benchmarks.recurrence_determinism_calibration > "$ledger/results.json" 2> "$ledger/stderr.txt"
status=$?
printf '%s\n' "$status" > "$ledger/exit-status.txt"
exit "$status"
