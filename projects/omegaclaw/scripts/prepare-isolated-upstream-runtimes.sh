#!/usr/bin/env bash
set -euo pipefail

base=/home/openclaw/research-agent/projects/omegaclaw/upstream-clean
source_runtime="$base/runtime-protomega"
expected_petta=7037f4c2ad378c52fc328004fe216d5118b674f0
expected_omega=2cdef059fe06d13e1fea7ea23b49825cb530c5b8
expected_chroma=218484875d5d1bfb217a9a03d3983dc1ed9d406c
stamp=20260814T102600Z

verify_commits() {
  local runtime=$1
  test "$(git -C "$runtime" rev-parse HEAD)" = "$expected_petta"
  test "$(git -C "$runtime/repos/OmegaClaw-Core" rev-parse HEAD)" = "$expected_omega"
  test "$(git -C "$runtime/repos/petta_lib_chromadb" rev-parse HEAD)" = "$expected_chroma"
}

verify_commits "$source_runtime"

for identity in protocosmo2 protomega2; do
  target="$base/runtime-$identity"
  test ! -e "$target"
  cp -a --reflink=auto "$source_runtime" "$target"
  verify_commits "$target"
done

for identity in protomega protocosmo2 protomega2; do
  runtime="$base/runtime-$identity"
  history="$runtime/repos/OmegaClaw-Core/memory/history.metta"
  backup="$history.pre-isolation-$stamp"
  test -f "$history"
  test ! -e "$backup"
  mv "$history" "$backup"
  install -m 0644 /dev/null "$history"
  mkdir -p "$runtime/state/chroma" "$runtime/state/workflow_space"
  verify_commits "$runtime"
  printf '%s\t' "$identity"
  stat -c 'history=%d:%i:%s runtime=%d:%i' "$history" "$runtime"
done

python3 - "$base" <<'PY'
from pathlib import Path
import os
import sys

base = Path(sys.argv[1])
identities = ("protomega", "protocosmo2", "protomega2")
histories = [base / f"runtime-{name}" / "repos/OmegaClaw-Core/memory/history.metta" for name in identities]
states = [base / f"runtime-{name}" / "state" for name in identities]
history_keys = {(os.stat(path).st_dev, os.stat(path).st_ino) for path in histories}
state_keys = {(os.stat(path).st_dev, os.stat(path).st_ino) for path in states}
assert len(history_keys) == len(identities), history_keys
assert len(state_keys) == len(identities), state_keys
assert all(path.stat().st_size == 0 for path in histories)
print("PASS distinct_histories=3 distinct_states=3 empty_histories=3")
PY

pgrep -af 'OmegaClaw|petta.py|swipl.*OmegaClaw' && exit 1 || true
printf 'PASS zero_attributable_descendants\n'
