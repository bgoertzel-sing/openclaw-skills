#!/usr/bin/env bash
set -euo pipefail

cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v /home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python \
  run_carom_bridge_shadow_v2.py scheduled \
  --steps 1500 \
  --seed 0 \
  --device cpu \
  --output /home/openclaw/research-agent/projects/carom/experiments/20260722T200000Z-bridgelearn-shadow-mode-v2/telemetry.json
