#!/usr/bin/env bash
set -euo pipefail

cd /home/openclaw/research-agent/projects/carom/repos/carom

/home/openclaw/research-agent/scratch/bridgelearn-carom-venv/bin/python \
    run_carom_stochastic_transition_v2.py \
    --output /home/openclaw/research-agent/projects/carom/experiments/20260723T224500Z-stochastic-transition-id-v2/artifacts/results.json \
    --seed 0 \
    --threads 4 \
    --device cpu
