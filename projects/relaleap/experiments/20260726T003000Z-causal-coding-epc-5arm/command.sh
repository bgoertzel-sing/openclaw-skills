#!/usr/bin/env bash
set -euo pipefail
repo=/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding
run=/home/openclaw/research-agent/projects/relaleap/experiments/20260726T003000Z-causal-coding-epc-5arm
cd "$repo"
/usr/bin/time -v env PYTHONPATH=src:. /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python \
  scripts/run_causal_coding_epc_5arm.py \
  --seeds 1729 3253 6421 \
  --teacher-updates 2000 \
  --student-updates 2000 \
  --adapt-updates 200 \
  --batch-size 128 \
  --eval-batch-size 64 \
  --eval-batches 8 \
  --teacher-learning-rate 0.002 \
  --student-learning-rate 0.0008 \
  --adaptation-learning-rate 0.0008 \
  --kd-coefficient 0.02 \
  --support-tau 0.35 \
  --clarity-coefficient 0.001 \
  --commutator-coefficient 0.001 \
  --commutator-interval 50 \
  --commutator-probe-learning-rate 0.0008 \
  --data-dir data/tinyshakespeare \
  --output "$run/artifacts/results.json" \
  --checkpoint-dir "$run/artifacts/checkpoints"
