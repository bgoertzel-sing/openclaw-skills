#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e2_dual_battery.py --config configs/e1_homotopy_smoke.json --prediction configs/e2_prediction_2_frozen_v1_1.json --fields artifacts/e2_residual_adjoint_m0_v1_1.npz --m0 artifacts/e2_residual_adjoint_m0_v1_1.json --output artifacts/e2_dual_m1_m5_v1_1.json 
