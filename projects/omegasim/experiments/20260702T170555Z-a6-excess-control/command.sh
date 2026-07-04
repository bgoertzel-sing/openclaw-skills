#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegasim/repos/omegasim
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-excess-control-20260702T170555Z
git diff --check
