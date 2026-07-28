#!/usr/bin/env bash
set -euo pipefail
cd projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare
env PYTHONPATH=src python3 -m pytest tests/ -v 
