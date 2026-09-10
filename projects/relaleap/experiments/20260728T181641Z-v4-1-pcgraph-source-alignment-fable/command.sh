#!/usr/bin/env bash
set -euo pipefail

run_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$run_dir"

python3 -m unittest discover -s work/tests -v
python3 -m py_compile work/pcgraph_adapter.py work/tests/test_pcgraph_adapter.py

for path in work/pcgraph_adapter.py work/tests/test_pcgraph_adapter.py work/SOURCE_ALIGNMENT.md; do
  set +e
  git diff --no-index --check /dev/null "$path"
  check_status=$?
  set -e
  if [[ "$check_status" -gt 1 ]]; then
    exit "$check_status"
  fi
done

if rg -n '(-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,})' \
  work command.sh; then
  echo "credential-pattern check failed" >&2
  exit 1
fi

echo "credential-pattern check passed"
