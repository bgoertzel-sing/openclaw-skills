#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/carom/repos/carom
/usr/bin/time -v python3 analyze_12k_collapse.py \
  --checkpoints ../../experiments/20260722T015200Z-carom-gpt2-12k/artifacts/checkpoints \
  --source-results ../../experiments/20260722T015200Z-carom-gpt2-12k/artifacts/results \
  --output ../../experiments/20260726T-forensics-12k-collapse/metrics.json \
  --plot ../../experiments/20260726T-forensics-12k-collapse/timeline.png \
  > ../../experiments/20260726T-forensics-12k-collapse/stdout.log \
  2> ../../experiments/20260726T-forensics-12k-collapse/stderr.log
