#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e4_cmcp_persistent.py --config configs/e4_cmcp_persistent_calibration_v1.json --seed 61001 --output /tmp/e4-cmcp-persistent-smoke.json 
