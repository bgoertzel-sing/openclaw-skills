#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers
bash -lc export\ PATH=/home/openclaw/research-agent/projects/omegaclaw/local/swipl-9.3.36/bin:\$PATH\;\ export\ SWI_HOME_DIR=/home/openclaw/research-agent/projects/omegaclaw/local/swipl-9.3.36/lib/swipl\;\ export\ LD_LIBRARY_PATH=/home/openclaw/research-agent/projects/omegaclaw/local/swipl-9.3.36/lib/swipl/lib/x86_64-linux\;\ timeout\ 20\ swipl\ --stack_limit=8g\ -q\ -s\ /home/openclaw/research-agent/projects/omegaclaw/repos/PeTTa/src/main.pl\ --\ src/persistent_worker_lifecycle.metta 
