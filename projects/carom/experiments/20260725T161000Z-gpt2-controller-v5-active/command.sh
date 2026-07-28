#!/usr/bin/env bash
set -euo pipefail
cd /workspace/carom-gpt2-v5
mkdir -p artifacts /workspace/zerobot-runs/carom-gpt2-v5/results
python3 -m venv --system-site-packages /workspace/carom-gpt2-v5/.venv
/workspace/carom-gpt2-v5/.venv/bin/python -m pip install transformers -q
/workspace/carom-gpt2-v5/.venv/bin/python run_carom_gpt2_controller_v5.py \
  2>&1 | tee artifacts/experiment.log
/workspace/carom-gpt2-v5/.venv/bin/python - <<'PY'
import json
import platform
import torch
from pathlib import Path
Path("artifacts/environment.json").write_text(json.dumps({
    "python": platform.python_version(),
    "torch": torch.__version__,
    "cuda": torch.version.cuda,
    "gpu": torch.cuda.get_device_name(0),
}, indent=2) + "\n")
PY
cp /workspace/zerobot-runs/carom-gpt2-v5/results/results.json artifacts/results.json
sha256sum artifacts/results.json artifacts/experiment.log artifacts/environment.json \
  > artifacts/sha256.txt
