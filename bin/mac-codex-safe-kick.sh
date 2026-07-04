#!/usr/bin/env bash
# Safe kick helper for existing Codex launchd loops on defective-mind-uploader.
# It does not provision/stop RunPod and does not bypass repo guards.
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo "usage: $0 relaleap|omegasim|git-auto-push" >&2
  exit 2
fi
case "$1" in
  relaleap) LABEL="com.bengoertzel.codex.relaleap-cli-loop" ;;
  omegasim) LABEL="com.bengoertzel.codex.omegasim-cli-loop" ;;
  git-auto-push) LABEL="com.bengoertzel.codex.git-auto-push" ;;
  *) echo "unknown loop: $1" >&2; exit 2 ;;
esac
HOST="${MAC_CODEX_HOST:-bengoertzel@100.105.177.92}"
ssh -o ConnectTimeout=10 "$HOST" "launchctl kickstart -k gui/\$(id -u)/$LABEL && launchctl list | grep '$LABEL' || true"
