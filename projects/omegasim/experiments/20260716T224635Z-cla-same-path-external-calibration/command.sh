#!/usr/bin/env bash
set -euo pipefail

omega=/home/openclaw/research-agent/projects/omegasim/repos/omegasim
cla=/home/openclaw/research-agent/projects/omegasim/repos/chaoslang-frozen-974af31
run=/home/openclaw/research-agent/projects/omegasim/experiments/20260716T224635Z-cla-same-path-external-calibration

test "$(git -C "$omega" rev-parse HEAD)" = 18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d
test -z "$(git -C "$omega" status --porcelain)"
test "$(git -C "$cla" rev-parse HEAD)" = 974af31efaf6e3cc239252f78367d20e657ac45c
test -z "$(git -C "$cla" status --porcelain)"
echo '29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c  scripts/run_cla_detector.py' | (cd "$omega" && sha256sum -c -)
echo '3d9f370c553cfba600461bbec92c705fdb29773fc6bc0376ff3dea37988c9437  src/chaoslang/benchmarks/attractors.py' | (cd "$cla" && sha256sum -c -)

cd "$run"
env PYTHONPATH="$omega/src:$omega:$cla/src" python3 run_benchmark.py
