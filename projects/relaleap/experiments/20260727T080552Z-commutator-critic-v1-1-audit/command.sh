#!/usr/bin/env bash
set -euo pipefail

workspace=/home/openclaw/research-agent
source_dir="$workspace/library/commutator-critic-v1-1/extracted"
artifact_dir="$workspace/projects/relaleap/experiments/20260727T080552Z-commutator-critic-v1-1-audit/artifacts"
audit_tmp=$(mktemp -d /tmp/comcrit-audit.XXXXXX)
trap 'rm -rf "$audit_tmp"' EXIT

mkdir -p "$artifact_dir"
cp "$source_dir/quadratic_demo.py" "$audit_tmp/"
(
  cd "$audit_tmp"
  python3 quadratic_demo.py
)
cp "$audit_tmp/results_quadratic.json" "$artifact_dir/results_quadratic-reproduced.json"
if [[ -f "$audit_tmp/quadratic_demo.png" ]]; then
  cp "$audit_tmp/quadratic_demo.png" "$artifact_dir/quadratic_demo-reproduced.png"
fi

tar -xzf "$source_dir/comcrit_v0.1.1.tar.gz" -C "$audit_tmp"
(
  cd "$audit_tmp/comcrit"
  PYTHONPATH=src python3 -m pytest -q tests
  PYTHONPATH=src python3 -c "import comcrit; report = comcrit.selftest(verbose=False); print(report); assert report['passed']"
)

python3 - "$source_dir/results_quadratic.json" "$artifact_dir/results_quadratic-reproduced.json" <<'PY'
import json
import math
import sys

expected = json.load(open(sys.argv[1], encoding="utf-8"))
actual = json.load(open(sys.argv[2], encoding="utf-8"))

def compare(a, b, path="root"):
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            raise AssertionError(f"{path}: key mismatch")
        for key in a:
            compare(a[key], b[key], f"{path}.{key}")
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise AssertionError(f"{path}: length mismatch")
        for index, (left, right) in enumerate(zip(a, b)):
            compare(left, right, f"{path}[{index}]")
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if not math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-12):
            raise AssertionError(f"{path}: {a!r} != {b!r}")
    elif a != b:
        raise AssertionError(f"{path}: {a!r} != {b!r}")

compare(expected, actual)
print("quadratic_json_matches_checked_in_within_tolerance")
PY
