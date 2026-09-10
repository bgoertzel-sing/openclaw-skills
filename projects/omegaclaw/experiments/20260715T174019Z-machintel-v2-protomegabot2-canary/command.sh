#!/usr/bin/env bash
set -euo pipefail
cd projects/protomegabot2/repos/PeTTa/repos/OmegaClaw-Core
env PYTHONPATH=channels python3 -m pytest -q Autotests/test_chat_room_identity_v2.py Autotests/test_gateway_suppression_v2.py --noconftest 
