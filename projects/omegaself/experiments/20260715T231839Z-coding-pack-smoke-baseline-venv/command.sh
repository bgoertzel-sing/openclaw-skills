#!/usr/bin/env bash
set -euo pipefail
cd projects/omegaself/repos/omegaself-coding-agent-pack
env PATH=/home/openclaw/research-agent/projects/protomegabot2/repos/PeTTa/.venv/bin:/usr/bin:/bin bash ./scripts/smoke_test.sh 
