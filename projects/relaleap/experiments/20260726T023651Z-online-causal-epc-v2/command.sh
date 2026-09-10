#!/usr/bin/env bash
set -euo pipefail
cd projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding
env PYTHONPATH=src:. /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python scripts/run_online_causal_epc.py --output /home/openclaw/research-agent/projects/relaleap/experiments/20260726T023651Z-online-causal-epc-v2/artifacts/results.json
