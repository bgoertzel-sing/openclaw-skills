#!/usr/bin/env bash
set -euo pipefail

omega=/home/openclaw/research-agent/projects/omegasim/repos/omegasim
cla=/home/openclaw/research-agent/projects/omegasim/repos/chaoslang-frozen-974af31
out=/home/openclaw/research-agent/projects/omegasim/experiments/20260716T164500Z-cla-roles8-untouched-replication/artifacts/cla_roles8_untouched_20260716.json

test "$(git -C "$omega" rev-parse HEAD)" = 18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d
test -z "$(git -C "$omega" status --porcelain)"
test "$(git -C "$cla" rev-parse HEAD)" = 974af31efaf6e3cc239252f78367d20e657ac45c
test -z "$(git -C "$cla" status --porcelain)"
cd "$omega"
echo '29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c  scripts/run_cla_detector.py' | sha256sum -c -
echo '051cb1ff768ce9d093a229fcc0aabd15d751e500387fa5a5a22b5cc44ed898c9  docs/cla_detector_preregistration_20260715.md' | sha256sum -c -
echo '759f5f8a64cbf9edb065a1ec2e8830ff93c8aa4221d736a680987dddb2858f05  docs/cla_roles8_untouched_replication_preregistration_20260716.md' | sha256sum -c -

env PYTHONPATH="src:$cla/src" python3 scripts/run_cla_detector.py \
  --output "$out" \
  --seeds 101,103,107,109,113 \
  --couplings 0.60 \
  --delays 3 \
  --steps 1024 \
  --burn 128 \
  --surrogates 5
