#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src python3 scripts/run_e1_m0_dynamics_audit.py --config configs/e1_homotopy_smoke.json --output artifacts/e1_m0_dynamics_audit.json 
