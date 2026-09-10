#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers
bash -lc python3\ -m\ unittest\ tests.test_persistent_worker_lifecycle\ \&\&\ python3\ -m\ py_compile\ src/persistent_worker.py\ tests/test_persistent_worker_lifecycle.py\ \&\&\ git\ diff\ --check 
