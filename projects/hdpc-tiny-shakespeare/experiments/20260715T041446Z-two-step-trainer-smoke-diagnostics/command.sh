#!/usr/bin/env bash
set -euo pipefail
cd projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare
/usr/bin/env PYTHONPATH=src python3 -m hdpc_tiny_shakespeare.train_distill --steps 2 --seq-len 64 --batch-size 2 --output /home/openclaw/research-agent/scratch/hdpc-two-step-metrics-v2.json 
