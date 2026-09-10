#!/usr/bin/env bash
set -euo pipefail
REPO=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
RUN=/home/openclaw/research-agent/projects/relaleap/experiments/20260725T231807Z-cmcp-epc-cl-phase1
cd "$REPO"
PYTHONPATH=src /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python \
  scripts/run_cmcp_epc_cl_phase1.py \
  --seeds 1729 3253 6421 \
  --teacher-updates 2000 \
  --student-updates 2000 \
  --adapt-updates 200 \
  --batch-size 128 \
  --output "$RUN/artifacts/results.json" \
  --checkpoint-dir "$RUN/artifacts/checkpoints"

