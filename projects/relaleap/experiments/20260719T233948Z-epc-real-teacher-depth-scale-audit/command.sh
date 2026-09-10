#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc
env PYTHONPATH=src python3 scripts/run_epc_real_teacher_scale_audit.py --checkpoint /home/openclaw/research-agent/projects/relaleap/experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/seed3253_epc_kd --output /home/openclaw/research-agent/projects/relaleap/experiments/epc-real-teacher-depth-scale-audit-output.json --device cpu --sequence 32 
