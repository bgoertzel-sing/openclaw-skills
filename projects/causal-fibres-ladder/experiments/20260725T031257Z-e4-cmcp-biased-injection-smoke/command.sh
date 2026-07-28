#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e4_cmcp_biased_injection.py --config configs/e4_cmcp_biased_injection_v1.json --seed 61001 --output /home/openclaw/research-agent/projects/causal-fibres-ladder/artifacts/e4-cmcp-biased-injection-smoke-v1.json 
