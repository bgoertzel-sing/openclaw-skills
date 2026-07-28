#!/usr/bin/env bash
set -euo pipefail

# CAROM GPT-2 distributional controller v4 rerun
# Fix: branches no longer call scheduler.step() on terminal parent OneCycleLR
# Budget: 2 hours / USD 3.00 hard cap (within $10 max)

cd /workspace

# Upload required files to /workspace
# exp2_compiled_channel.py  — model + task code
# run_carom_gpt2_controller_v4.py — v4 runner with scheduler fix

pip install transformers -q

python3 run_carom_gpt2_controller_v4.py 2>&1 | tee artifacts/experiment.log

echo "=== RUN COMPLETE ==="
