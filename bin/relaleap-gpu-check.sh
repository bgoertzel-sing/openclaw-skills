#!/usr/bin/env bash
# Check if RelaLeap's AUTOMATION_STATUS.md indicates GPU is needed.
# Outputs "GPU_NEEDED" or "GPU_NOT_NEEDED" and exits 0.
set -euo pipefail
HOST="${MAC_CODEX_HOST:-bengoertzel@100.105.177.92}"
ROOT="/Users/bengoertzel/Documents/Codex/2026-06-17/i-want-to-have-you-work"
STATUS=$(ssh -o ConnectTimeout=10 "$HOST" "grep -i 'requires_gpu_now\|advance_to_gpu\|GPU' '$ROOT/relaleap/AUTOMATION_STATUS.md' 2>/dev/null || true")
if echo "$STATUS" | grep -qiE 'requires_gpu_now:\s*true|advance_to_gpu:\s*true'; then
  echo "GPU_NEEDED"
  exit 0
fi
echo "GPU_NOT_NEEDED"
