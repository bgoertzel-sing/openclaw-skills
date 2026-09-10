#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 scripts/run_epc_distillation_gate.py --output /home/openclaw/research-agent/projects/relaleap/artifacts/epc_distillation_gate_local_20260715.json --device cpu --seeds 11\,29\,47 --lambdas 0\,0.001\,0.01\,0.05 --inference-steps 1\,2\,4\,8 --temperature 2 --seq-len 32 --batch-size 4 --teacher-d-model 32 --student-d-model 16 --nhead 2 --num-layers 2 --teacher-steps 12 --train-steps 6 --eval-batches 4 
