#!/usr/bin/env bash
set -euo pipefail

omega=/home/openclaw/research-agent/projects/omegasim/repos/omegasim
cla=/home/openclaw/research-agent/projects/omegasim/repos/chaoslang-frozen-974af31
run=/home/openclaw/research-agent/projects/omegasim/experiments/20260716T204500Z-cla-roles8-bitwise-replay
original=/home/openclaw/research-agent/projects/omegasim/experiments/20260716T164500Z-cla-roles8-untouched-replication/artifacts/cla_roles8_untouched_20260716
replay="$run/artifacts/cla_roles8_replay_20260716"

test "$(git -C "$omega" rev-parse HEAD)" = 18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d
test -z "$(git -C "$omega" status --porcelain)"
test "$(git -C "$cla" rev-parse HEAD)" = 974af31efaf6e3cc239252f78367d20e657ac45c
test -z "$(git -C "$cla" status --porcelain)"
echo '29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c  scripts/run_cla_detector.py' | (cd "$omega" && sha256sum -c -)
echo '2b788fb95be7021bd875ce273d3530488e7ec9432edb4b278d48de7ab8e0db3d  src/omegasim/a6_model.py' | (cd "$omega" && sha256sum -c -)
echo '452f5e03c83770d4b34267ac38fcebd1417709b3c1be39ae9eb6daa8e471703d  src/chaoslang/evaluation.py' | (cd "$cla" && sha256sum -c -)
echo '1c53a4350c54e73031a6f938a8445644dd767365936079ee162387a17110451b  src/chaoslang/symbolization.py' | (cd "$cla" && sha256sum -c -)

mkdir -p "$run/artifacts"
cd "$omega"
env PYTHONPATH="src:$cla/src" python3 scripts/run_cla_detector.py \
  --output "$replay.json" \
  --seeds 101,103,107,109,113 \
  --couplings 0.60 \
  --delays 3 \
  --steps 1024 \
  --burn 128 \
  --surrogates 5

cmp "$original.csv" "$replay.csv"
env ORIGINAL="$original.json" REPLAY="$replay.json" python3 - <<'PY'
import json
import os

with open(os.environ["ORIGINAL"], encoding="utf-8") as handle:
    original = json.load(handle)
with open(os.environ["REPLAY"], encoding="utf-8") as handle:
    replay = json.load(handle)
original["config"].pop("output")
replay["config"].pop("output")
if original != replay:
    raise SystemExit("normalized JSON mismatch")
print(json.dumps({"csv_byte_identical": True, "normalized_json_identical": True}, sort_keys=True))
PY
