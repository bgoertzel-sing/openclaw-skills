#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "$0")/../.." && pwd)"
gate_dir="$project_dir/sealed/frame-oracle-v14"
python_bin="$project_dir/repos/relaleap/.venv/bin/python"

"$python_bin" -m py_compile "$gate_dir/validate_gate.py"
bash -n "$gate_dir/run_integrity.sh"
prior_args=()
for version in {4..13}; do
  prior_args+=(--prior-public "$project_dir/sealed/frame-oracle-v${version}/gate_public.json")
done
"$python_bin" "$gate_dir/validate_gate.py" \
  --public "$gate_dir/gate_public.json" \
  --answers "$gate_dir/gate_answers.json" \
  --worktree "$project_dir/worktrees/frame-oracle-v2" \
  --exposed-artifact "$project_dir/experiments/20260801T161016Z-frame-oracle-offline-readout-v1/artifacts/offline_labels.json" \
  "${prior_args[@]}"
sha256sum "$gate_dir/gate_public.json" "$gate_dir/gate_answers.json" \
  "$gate_dir/validate_gate.py" "$project_dir/docs/frame_oracle_v14_fresh_gate_contract_20260807.md"
