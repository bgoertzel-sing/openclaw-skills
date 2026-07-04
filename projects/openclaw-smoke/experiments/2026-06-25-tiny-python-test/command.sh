#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../repos/tiny-python"
python3 -m unittest discover -s tests
