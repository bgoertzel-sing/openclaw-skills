#!/usr/bin/env bash
set -euo pipefail

repo="/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1"
output="/home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260725T001224Z-e4-cmcp-ledger-calibration"
cd "$repo"
scripts/run_e4_cmcp_calibration.sh "$output"
