#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/calibrate_quantale_p.py --config configs/e4_quantale_calibration_v1.json --output /home/openclaw/research-agent/projects/causal-fibres-ladder/artifacts/e4-quantale-p-calibration-v1.json 
