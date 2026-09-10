#!/bin/sh
set -eu
repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
test "$(git -C "$repo" rev-parse HEAD)" = 4cc2441810f518f563a46eb63d4b2d352022dfd6
test -z "$(git -C "$repo" status --porcelain)"
PYTHONPATH="$repo/src" /usr/bin/time -f '%e seconds %M KiB' -o timing.txt \
  python3 -m chaoslang.benchmarks.paired_divergence_calibration >results.json 2>stderr.txt
printf '%s\n' 0 >exit-status.txt
