#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e4_information.py --base-config configs/e3_partial_student_v1.json --criteria configs/e4_acceptance_v1_1_frozen.json --seed 12011 --output /home/openclaw/research-agent/scratch/e4-nonceiling-12011.json 
