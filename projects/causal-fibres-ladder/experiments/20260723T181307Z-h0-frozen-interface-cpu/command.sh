#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent
projects/causal-fibres-ladder/.venv/bin/python projects/causal-fibres-ladder/scripts/run_h0_cpu.py --config projects/causal-fibres-ladder/configs/h0_cpu_smoke.json --output projects/causal-fibres-ladder/artifacts/h0_cpu_smoke_metrics.json 
