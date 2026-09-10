#!/usr/bin/env bash
set -u

run_dir="$(cd "$(dirname "$0")" && pwd)"
repo_dir="/home/openclaw/research-agent/scratch/chaoslang-strict-replay"

cd "$repo_dir"
if [ "$(git rev-parse HEAD)" != "4174095c290c89fb46375189acc940015cf9aaf0" ]; then
  echo "frozen commit mismatch" > "$run_dir/stderr.txt"
  echo 90 > "$run_dir/exit-status.txt"
  exit 90
fi
if [ -n "$(git status --porcelain)" ]; then
  echo "frozen worktree is dirty" > "$run_dir/stderr.txt"
  echo 91 > "$run_dir/exit-status.txt"
  exit 91
fi

set +e
PYTHONPATH=src /usr/bin/time -v -o "$run_dir/timing.txt" \
  python3 -m chaoslang.benchmarks.synthetic_compact_model \
  > "$run_dir/results.json" 2> "$run_dir/stderr.txt"
status=$?
set -e
echo "$status" > "$run_dir/exit-status.txt"
exit "$status"
