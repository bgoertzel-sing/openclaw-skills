#!/usr/bin/env bash
set -euo pipefail

repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
run=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T231900Z-synthetic-uniform-morphism-v1
expected=d854bc7bb01d768878d202f84afc3a2a7ab86996

test "$(git -C "$repo" rev-parse HEAD)" = "$expected"
test -z "$(git -C "$repo" status --porcelain)"
cd "$repo"
python3 -m chaoslang.benchmarks.synthetic_uniform_morphism --manifest-only > "$run/actual-manifest.json"
python3 -c 'import json,sys; assert json.load(open(sys.argv[1])) == json.load(open(sys.argv[2]))' \
  "$run/manifest.json" "$run/actual-manifest.json"
/usr/bin/time -f 'wall_seconds=%e\nmax_rss_kib=%M' -o "$run/timing.txt" \
  python3 -m chaoslang.benchmarks.synthetic_uniform_morphism \
  > "$run/results.json" 2> "$run/stderr.txt"
printf '0\n' > "$run/exit-status.txt"
