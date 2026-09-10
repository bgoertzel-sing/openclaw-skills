#!/usr/bin/env bash
set -u

run_dir="$(cd "$(dirname "$0")" && pwd)"
repo_dir="/home/openclaw/research-agent/scratch/chaoslang-strict-replay"

cd "$repo_dir"
if [ "$(git rev-parse HEAD)" != "cbbebfd655d24a385fb16546aa3c26cdfb78b427" ]; then
  echo "frozen commit mismatch" > "$run_dir/stderr.txt"
  echo 90 > "$run_dir/exit-status.txt"
  exit 90
fi
if [ -n "$(git status --porcelain)" ]; then
  echo "frozen worktree is dirty" > "$run_dir/stderr.txt"
  echo 91 > "$run_dir/exit-status.txt"
  exit 91
fi

tmp_manifest="$(mktemp)"
trap 'rm -f "$tmp_manifest"' EXIT
PYTHONPATH=src python3 -m chaoslang.benchmarks.attractor_amortization --manifest-only > "$tmp_manifest"
if ! cmp "$tmp_manifest" "$run_dir/manifest.json"; then
  echo "frozen manifest mismatch" > "$run_dir/stderr.txt"
  echo 92 > "$run_dir/exit-status.txt"
  exit 92
fi

set +e
PYTHONPATH=src /usr/bin/time -v -o "$run_dir/timing.txt" \
  python3 -m chaoslang.benchmarks.attractor_amortization \
  > "$run_dir/results.json" 2> "$run_dir/stderr.txt"
status=$?
set -e
echo "$status" > "$run_dir/exit-status.txt"
exit "$status"

