#!/usr/bin/env bash
set -euo pipefail

script_dir="$(dirname -- "$(realpath -- "${BASH_SOURCE[0]}")")"
repo_root="$(realpath -- "$script_dir/..")"
source_root="$(realpath -- "$repo_root/src")"
python_bin="${RELALEAP_FRAME_ORACLE_V9_PYTHON:?set RELALEAP_FRAME_ORACLE_V9_PYTHON to the frozen interpreter}"
: "${RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT:?set an absolute provenance sidecar path}"

if [[ "$RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT" != /* ]]; then
  echo "RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT must be absolute" >&2
  exit 2
fi

export PYTHONPATH="$source_root"
export RELALEAP_FRAME_ORACLE_V9_SOURCE_ROOT="$source_root"
exec "$python_bin" "$script_dir/run_frame_oracle_v9.py" "$@"

