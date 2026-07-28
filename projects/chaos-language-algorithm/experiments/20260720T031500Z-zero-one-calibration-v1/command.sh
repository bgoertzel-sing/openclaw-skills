#!/bin/sh
set -eu
repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
test "$(git -C "$repo" rev-parse HEAD)" = 76d5deb02a717205bd133f2eb8bd4cb0ff87ce3d
test -z "$(git -C "$repo" status --porcelain)"
PYTHONPATH="$repo/src" /usr/bin/time -f '%e seconds %M KiB' -o timing.txt \
  python3 -m chaoslang.benchmarks.zero_one_calibration >results.json 2>stderr.txt
printf '%s\n' 0 >exit-status.txt
