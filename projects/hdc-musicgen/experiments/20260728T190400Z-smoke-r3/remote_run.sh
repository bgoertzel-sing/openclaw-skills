#!/usr/bin/env bash
set -euo pipefail
ROOT=/workspace/hdc-musicgen-r3
OUT=/workspace/hdc-musicgen-r3-results
python3 -m venv /workspace/hdc-musicgen-r3-venv
source /workspace/hdc-musicgen-r3-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
python -m pip install audiocraft==1.3.0 pytest librosa
cd "$ROOT/code"
python -m pytest -q test_hdc_musicgen_structural.py
python - <<'PY' > "$OUT/environment.txt"
import torch
import audiocraft
print('torch', torch.__version__)
print('cuda', torch.version.cuda)
print('audiocraft', getattr(audiocraft, '__version__', 'unknown'))
print('gpu', torch.cuda.get_device_name(0))
PY
python hdc_musicgen_structural.py stage0 --audio_dir "$ROOT/audio" --out_dir "$OUT" --limit 8
python hdc_musicgen_structural.py stageS --out_dir "$OUT"
python hdc_musicgen_structural.py stageA --out_dir "$OUT"
sha256sum "$ROOT/audio"/*.mp3 "$OUT"/*.json "$OUT"/environment.txt > "$OUT/SHA256SUMS"
