#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e3_student_calibration.py --base-config configs/e1_homotopy_smoke.json --calibration configs/e3_partial_student_calibration_v1.json --output /home/openclaw/research-agent/scratch/e3-partial-student-calibration.json --checkpoint-dir /home/openclaw/research-agent/scratch/e3-partial-student-checkpoints 
