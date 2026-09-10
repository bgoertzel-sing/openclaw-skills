#!/usr/bin/env bash
set -euo pipefail

repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
run=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T211500Z-synthetic-family-generalization-v1
expected=e6e3ed2183d22779ed44013d272d150a4f5961fa

test "$(git -C "$repo" rev-parse HEAD)" = "$expected"
test -z "$(git -C "$repo" status --porcelain)"
cd "$repo"
python3 -m chaoslang.benchmarks.synthetic_family_generalization --manifest-only > "$run/actual-manifest.json"
cmp "$run/manifest.json" "$run/actual-manifest.json"
/usr/bin/time -f 'wall_seconds=%e\nmax_rss_kib=%M' -o "$run/timing.txt" \
  python3 -m chaoslang.benchmarks.synthetic_family_generalization \
  > "$run/results.json" 2> "$run/stderr.txt"
printf '0\n' > "$run/exit-status.txt"
