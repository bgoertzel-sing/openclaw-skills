#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1
/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python -m pytest tests/ -q 
