#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/time -v /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e1_homotopy_smoke.py --config configs/e1_homotopy_smoke.json --output /home/openclaw/research-agent/projects/causal-fibres-ladder/artifacts/e1_homotopy_smoke_results.json 
