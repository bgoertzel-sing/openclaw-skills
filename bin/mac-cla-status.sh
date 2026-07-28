#!/usr/bin/env bash
# Read-only status collector for CLA benchmark work on defective-mind-uploader.
set -euo pipefail
HOST="${MAC_CODEX_HOST:-bengoertzel@100.105.177.92}"
ssh -o ConnectTimeout=10 "$HOST" 'set -euo pipefail
ROOT="$HOME/Documents/Codex/2026-06-17/i-want-to-have-you-work"
echo "# Mac CLA status $(date "+%Y-%m-%d %H:%M:%S %Z")"
echo
printf "host: "; hostname
printf "user: "; whoami
echo

echo "## CLA repository"
cd "$ROOT/chaos-language-algorithm" 2>/dev/null || { echo "REPO_NOT_FOUND"; exit 1; }
echo "branch=$(git rev-parse --abbrev-ref HEAD)"
echo "head=$(git log -1 --oneline)"
echo "status:"
git status --short || true
echo
echo "## tests"
PYTHONPATH=src /usr/local/bin/python3.9 -m unittest discover -s tests -v 2>&1 | tail -10 || echo "TESTS_FAILED"
echo
echo "## AUTOMATION_STATUS excerpt"
if [ -f AUTOMATION_STATUS.md ]; then
  awk "/^## Current state/{flag=1; count=0; next} /^## Mandate/{flag=0} flag && count<30 {print; count++}" AUTOMATION_STATUS.md || true
fi
echo
echo "## recent experiments"
ls -la experiments/ 2>/dev/null || echo "no experiments dir"
echo
echo "## RelaLeap/OmegaSim (paused - brief check only)"
for repo in relaleap omegasim; do
  if [ -d "$ROOT/$repo" ]; then
    echo "### $repo (paused)"
    cd "$ROOT/$repo"
    echo "head=$(git log -1 --oneline 2>/dev/null || echo 'n/a')"
  fi
done
'
