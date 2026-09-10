#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 scripts/run_epc_distillation_gate.py --output /home/openclaw/research-agent/projects/relaleap/artifacts/epc_distillation_gate_v2_20260715.json --device cpu --seeds 73\,89\,107 --lambdas 0\,0.001\,0.01\,0.05 --inference-steps 1\,2\,4\,8 --temperature 2 --seq-len 32 --batch-size 4 --teacher-d-model 32 --student-d-model 16 --nhead 2 --num-layers 2 --teacher-steps 12 --train-steps 6 --eval-batches 4 
