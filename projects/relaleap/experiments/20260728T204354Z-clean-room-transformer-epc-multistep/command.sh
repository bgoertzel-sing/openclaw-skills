#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src PATH=../.venv/bin:$PATH \
  bash scripts/run_cleanroom_epc_multistep_grid.sh results
