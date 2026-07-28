#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e2_c2_dictionary.py --campaign /home/openclaw/research-agent/projects/causal-fibres-ladder/experiments/20260724T181805Z-e2-confirmation-5seed-v1-1-frozen/artifacts/campaign --criteria configs/e2_acceptance_v1_1_frozen.json --output-dir /home/openclaw/research-agent/scratch/e2-c2-dictionary-5seed-v1-1-vectorized 
