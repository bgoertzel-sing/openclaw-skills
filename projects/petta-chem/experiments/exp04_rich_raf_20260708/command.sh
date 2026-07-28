#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/petta-chem/repos/petta-chem
python3 experiments/exp04/run_rich_raf.py --ticks 56 --out /home/openclaw/research-agent/projects/petta-chem/experiments/exp04_rich_raf_20260708/metrics.json
