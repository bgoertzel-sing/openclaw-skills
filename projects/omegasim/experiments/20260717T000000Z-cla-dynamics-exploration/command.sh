#!/usr/bin/env bash
set -euo pipefail

RUN_DIR=/home/openclaw/research-agent/projects/omegasim/experiments/20260717T000000Z-cla-dynamics-exploration
OMEGASIM_DIR=/home/openclaw/research-agent/projects/omegasim/repos/omegasim
CHAOSLANG_DIR=/home/openclaw/research-agent/scratch/chaoslang-974af31-cla-dynamics

cd "$OMEGASIM_DIR"
export PYTHONPATH="$OMEGASIM_DIR/src:$CHAOSLANG_DIR/src"
python3 "$RUN_DIR/run_experiment.py" \
  --run-dir "$RUN_DIR" \
  --omegasim "$OMEGASIM_DIR" \
  --chaoslang "$CHAOSLANG_DIR"
