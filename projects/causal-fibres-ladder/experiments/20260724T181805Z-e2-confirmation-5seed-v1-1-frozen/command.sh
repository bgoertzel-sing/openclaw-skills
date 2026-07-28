#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/usr/bin/env PYTHONPATH=src /home/openclaw/research-agent/projects/causal-fibres-ladder/.venv/bin/python scripts/run_e2_multiseed_campaign.py --phase confirmation --seeds 6029\,7331\,8641\,9941\,11251 --base-config configs/e1_homotopy_smoke.json --m0-criteria configs/e1_e2_acceptance_v1_1.json --frozen-criteria configs/e2_acceptance_v1_1_frozen.json --prediction configs/e2_prediction_2_frozen_v1_1.json --output-dir /home/openclaw/research-agent/scratch/e2-confirmation-5seed-v1-1-frozen 
