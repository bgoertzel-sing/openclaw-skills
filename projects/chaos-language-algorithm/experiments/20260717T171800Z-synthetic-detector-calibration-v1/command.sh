#!/usr/bin/env bash
set -uo pipefail

repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay
run=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260717T171800Z-synthetic-detector-calibration-v1
expected_commit=64b3b333a92128220b6792c4dd2d502784ac3dc5

cd "$repo" || exit 90
test "$(git rev-parse HEAD)" = "$expected_commit" || exit 91
test -z "$(git status --porcelain)" || exit 92
tmp_manifest=$(mktemp)
trap 'rm -f "$tmp_manifest"' EXIT
python3 -m chaoslang.benchmarks.synthetic_detector_calibration --manifest-only > "$tmp_manifest" || exit 93
python3 - "$tmp_manifest" "$run/manifest.json" <<'PY' || exit 94
import json
import sys
with open(sys.argv[1], encoding="utf-8") as generated:
    left = json.load(generated)
with open(sys.argv[2], encoding="utf-8") as frozen:
    right = json.load(frozen)
if left != right:
    raise SystemExit(1)
PY

set +e
/usr/bin/time -v -o "$run/timing.txt" python3 -m chaoslang.benchmarks.synthetic_detector_calibration > "$run/results.json" 2> "$run/stderr.txt"
status=$?
set -e
printf '%s\n' "$status" > "$run/exit-status.txt"
exit "$status"
