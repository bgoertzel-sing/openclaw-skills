#!/usr/bin/env bash
set -euo pipefail
cd projects/omegaself/repos/protomegabot2-omegaclaw-record-only
env PYTHONPATH=channels /home/openclaw/research-agent/projects/protomegabot2/repos/PeTTa/.venv/bin/python -m pytest -q Autotests/test_omegaself_bridge.py Autotests/test_chat_room_identity_v2.py Autotests/test_gateway_suppression_v2.py --noconftest 
