#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e1_m0_depth_sweep.py --config configs/e1_homotopy_smoke.json --criteria configs/e1_e2_acceptance_v1_1.json --architecture residual --output artifacts/e1_residual_p1_m0_v1_1.json 
