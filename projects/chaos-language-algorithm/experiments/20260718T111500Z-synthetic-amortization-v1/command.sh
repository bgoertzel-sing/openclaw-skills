#!/usr/bin/env bash
set -u

run_dir="$(cd "$(dirname "$0")" && pwd)"
repo_dir="/home/openclaw/research-agent/scratch/chaoslang-strict-replay"

cd "$repo_dir"
if [ "$(git rev-parse HEAD)" != "d299b2fa68bb15658a00291d1463c9d8d0ee4696" ]; then
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
  python3 -m chaoslang.benchmarks.synthetic_amortization \
  > "$run_dir/results.json" 2> "$run_dir/stderr.txt"
status=$?
set -e
echo "$status" > "$run_dir/exit-status.txt"
exit "$status"
