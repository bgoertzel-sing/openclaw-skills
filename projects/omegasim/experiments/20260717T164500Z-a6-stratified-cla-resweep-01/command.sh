#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegasim/repos/omegasim
export PYTHONPATH=/home/openclaw/research-agent/projects/omegasim/repos/omegasim/src:/home/openclaw/research-agent/projects/omegasim/repos/chaoslang-frozen-974af31/src
python3 /home/openclaw/research-agent/projects/omegasim/experiments/20260717T164500Z-a6-stratified-cla-resweep-01/run_experiment.py
