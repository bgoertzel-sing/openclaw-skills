#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-online-v3
PYTHONPATH=src:. /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python scripts/run_online_causal_epc.py --output /home/openclaw/research-agent/projects/relaleap/experiments/20260726T025745Z-online-causal-epc-v3/artifacts/results.json
