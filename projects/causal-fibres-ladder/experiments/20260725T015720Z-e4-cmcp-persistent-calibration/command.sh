#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
bash -lc run_dir=\$\(find\ /home/openclaw/research-agent/projects/causal-fibres-ladder/experiments\ -maxdepth\ 1\ -type\ d\ -name\ \"\*-e4-cmcp-persistent-calibration\"\ -printf\ \"%T@\ %p\\n\"\ \|\ sort\ -nr\ \|\ head\ -1\ \|\ cut\ -d\"\ \"\ -f2-\)\;\ export\ PYTHONPATH=src\;\ /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python\ scripts/run_e4_cmcp_persistent_calibration.py\ --config\ configs/e4_cmcp_persistent_calibration_v1.json\ --output-dir\ \"\$run_dir/artifacts\" 
