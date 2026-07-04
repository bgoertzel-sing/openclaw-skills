#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegasim/repos/omegasim
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-smoke-sweep-20260701 
