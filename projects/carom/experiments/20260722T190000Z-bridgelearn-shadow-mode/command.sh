#!/usr/bin/env bash
set -euo pipefail

/usr/bin/time -v /home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python \
  /home/openclaw/research-agent/projects/carom/repos/carom/run_carom_bridge_shadow.py \
  scheduled \
  --steps 1500 \
  --seed 0 \
  --device cpu \
  --output /home/openclaw/research-agent/projects/carom/experiments/20260722T190000Z-bridgelearn-shadow-mode/telemetry.json
