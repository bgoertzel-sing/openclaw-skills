#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "$0")/../.." && pwd)"
gate_dir="$project_dir/sealed/frame-oracle-v4"
worktree_dir="$project_dir/worktrees/frame-oracle-v2"
python_bin="$project_dir/repos/relaleap/.venv/bin/python"
exposed_artifact="$project_dir/experiments/20260801T161016Z-frame-oracle-offline-readout-v1/artifacts/offline_labels.json"

"$python_bin" "$gate_dir/validate_gate.py" \
  --public "$gate_dir/gate_public.json" \
  --answers "$gate_dir/gate_answers.json" \
  --worktree "$worktree_dir" \
  --exposed-artifact "$exposed_artifact"

cd "$worktree_dir"
"$python_bin" -m pytest -q \
  tests/test_frame_oracle.py \
  tests/test_frame_oracle_v2.py \
  tests/test_frame_oracle_v3.py
"$python_bin" -m pytest -q
git diff --check
