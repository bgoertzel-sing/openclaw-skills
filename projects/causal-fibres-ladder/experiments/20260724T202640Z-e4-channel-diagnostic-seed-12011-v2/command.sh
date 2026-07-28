#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e4_channel_diagnostic.py --base-config configs/e3_partial_student_v1.json --diagnostic configs/e4_channel_diagnostic_v2.json --seed 12011 --output /home/openclaw/research-agent/scratch/e4-channel-v2-12011.json 
