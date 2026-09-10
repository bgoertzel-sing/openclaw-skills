#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v /home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python \
  run_carom_frozen_replica_calibration.py \
  --device cpu \
  --seed 0 \
  --threads 4 \
  --output /home/openclaw/research-agent/projects/carom/experiments/20260723T181323Z-frozen-state-replica-calibration-v1/artifacts/results.json
