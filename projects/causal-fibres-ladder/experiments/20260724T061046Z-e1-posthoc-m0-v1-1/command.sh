#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src python3 scripts/run_e1_posthoc_m0.py --config configs/e1_homotopy_smoke.json --criteria configs/e1_e2_acceptance_v1_1.json --output artifacts/results.json 
