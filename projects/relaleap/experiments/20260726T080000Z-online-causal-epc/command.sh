#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding
venv=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260726T080000Z-online-causal-epc
cd "$repo"
PYTHONPATH=src:. "$venv" scripts/run_online_causal_epc.py --output "$run/artifacts/results.json"
