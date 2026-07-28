#!/usr/bin/env bash
set -euo pipefail
cd projects/carom/repos/carom
env PYTHONPATH=/home/openclaw/research-agent/projects/carom/repos/carom /home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python run_carom_controller_activation_v3.py --output artifacts/results.json --seed 0 --threads 4 --device cpu 
