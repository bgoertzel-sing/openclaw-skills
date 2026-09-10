#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegasim/repos/omegasim
env PYTHONPATH=src:/home/openclaw/research-agent/projects/chaos-language-algorithm/repos/chaoslang/src python3 scripts/run_cla_detector.py --output /home/openclaw/research-agent/projects/omegasim/artifacts/cla_detector_20260715.json --seeds 7\,17\,29\,43\,71 --couplings 0.35\,0.60 --delays 0\,3 --steps 1024 --burn 128 --surrogates 5 
