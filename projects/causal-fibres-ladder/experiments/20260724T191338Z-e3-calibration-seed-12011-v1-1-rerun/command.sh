#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e3_campaign.py --base-config configs/e1_homotopy_smoke.json --criteria configs/e3_acceptance_v1_1_frozen.json --seed 12011 --output /home/openclaw/research-agent/scratch/e3-seed-12011-v1-1.json 
