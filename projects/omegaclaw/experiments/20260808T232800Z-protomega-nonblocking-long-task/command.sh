#!/usr/bin/env bash
set -euo pipefail

# Commands are appended here before each recorded execution.

python3 -m py_compile \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary.py \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary_telegram.py \
  projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py

PYTHONPATH=projects/omegaclaw/worktrees/protocosmo2-phase6-live:. \
  python3 -m pytest -q \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary.py \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary_telegram.py

bash -n projects/omegaclaw/local/protomega2-outer-telegram-supervisor.sh
git diff --check
