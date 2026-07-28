#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap
bash -lc PYTHONPATH=src\ python3\ -m\ pytest\ tests/\ -v 
