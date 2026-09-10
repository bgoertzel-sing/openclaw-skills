#!/usr/bin/env bash
set -euo pipefail
export CAROM_RUN_ROOT=/workspace/zerobot-runs/carom
export CAROM_SOURCE_DIR=/workspace/zerobot-runs/carom
cd /workspace/zerobot-runs/carom
source /opt/zerobot-venv/bin/activate
python3 r9_carom_interventions.py --selftest
python3 r9_carom_interventions.py --steps 4000 --lm_steps 1500
