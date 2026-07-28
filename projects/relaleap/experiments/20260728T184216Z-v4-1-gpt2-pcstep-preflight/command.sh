#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/v4-gpt2-pcstep
python3 -m pytest -q tests/test_gpt2_epc.py tests/test_pcstep_adapter.py tests/test_gpt2_pilot_protocol.py tests/test_gpt2_pilot_dry_run.py tests/test_gpt2_pilot_gpu_runner.py tests/test_gpt2_full_pipeline.py 
