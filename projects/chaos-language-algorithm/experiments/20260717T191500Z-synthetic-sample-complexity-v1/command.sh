#!/usr/bin/env bash
set -euo pipefail

repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
run=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T191500Z-synthetic-sample-complexity-v1
expected=b3709d88412ed1ab97c09abc47803088996263df

test "$(git -C "$repo" rev-parse HEAD)" = "$expected"
test -z "$(git -C "$repo" status --porcelain)"
cd "$repo"
python3 -m chaoslang.benchmarks.synthetic_sample_complexity --manifest-only > "$run/actual-manifest.json"
cmp "$run/manifest.json" "$run/actual-manifest.json"
/usr/bin/time -f 'wall_seconds=%e\nmax_rss_kib=%M' -o "$run/timing.txt" \
  python3 -m chaoslang.benchmarks.synthetic_sample_complexity \
  > "$run/results.json" 2> "$run/stderr.txt"
printf '0\n' > "$run/exit-status.txt"
