#!/usr/bin/env bash
set -euo pipefail
python3 run_carom_gpt2_schedule_diagnostic.py \
  --step3000 /workspace/input/step_3000.pt \
  --output-dir /workspace/output
