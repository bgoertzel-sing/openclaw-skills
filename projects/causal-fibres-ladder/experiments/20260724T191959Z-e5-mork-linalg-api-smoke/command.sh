#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/morkql/repos/MORK
/home/openclaw/.cargo/bin/cargo +nightly test -p linalg --lib 
