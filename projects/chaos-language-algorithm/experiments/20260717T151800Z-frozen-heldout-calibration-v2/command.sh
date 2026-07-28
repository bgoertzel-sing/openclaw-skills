#!/usr/bin/env bash
set -euo pipefail

repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
run_dir=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T151800Z-frozen-heldout-calibration-v2
expected_commit=580f9170ff00876eba6aea0722770606804551cf

test "$(git -C "$repo" rev-parse HEAD)" = "$expected_commit"
test -z "$(git -C "$repo" status --porcelain)"

tmp_manifest=$(mktemp)
trap 'rm -f "$tmp_manifest"' EXIT
cd "$repo"
python3 -m chaoslang.benchmarks.frozen_heldout_v2 --manifest-only > "$tmp_manifest"
cmp "$tmp_manifest" "$run_dir/manifest.json"

/usr/bin/time -f 'wall_seconds=%e\nmax_rss_kib=%M' -o "$run_dir/timing.txt" \
  python3 -m chaoslang.benchmarks.frozen_heldout_v2 \
  > "$run_dir/results.json" 2> "$run_dir/stderr.txt"
printf '0\n' > "$run_dir/exit-status.txt"
