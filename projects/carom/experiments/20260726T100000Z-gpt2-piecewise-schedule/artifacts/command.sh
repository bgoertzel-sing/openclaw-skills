#!/usr/bin/env bash
set -euo pipefail
cd /workspace
PYTHONPATH=. python3 run_carom_gpt2_piecewise_schedule.py --output-dir /workspace/output
