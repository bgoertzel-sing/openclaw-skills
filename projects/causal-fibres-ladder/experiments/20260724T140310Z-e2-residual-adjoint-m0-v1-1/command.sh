#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e2_adjoint_m0.py --config configs/e1_homotopy_smoke.json --criteria configs/e1_e2_acceptance_v1_1.json --output artifacts/e2_residual_adjoint_m0_v1_1.json 
