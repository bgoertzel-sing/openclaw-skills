#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent
env PYTHONPATH=/home/openclaw/research-agent/projects/carom/repos/carom /home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python repos/carom/run_carom_controller_activation_v3.py --output artifacts/results.json --seed 0 --threads 4 --device cpu 
