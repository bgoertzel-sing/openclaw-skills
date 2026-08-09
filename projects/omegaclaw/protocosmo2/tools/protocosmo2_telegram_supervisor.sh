#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/openclaw/research-agent/projects/omegaclaw
RUNNER="$ROOT/protocosmo2/tools/phase6_private_canary_runner.py"
CORE="$ROOT/worktrees/protocosmo2-phase6-live"
PETTA="$ROOT/protocosmo2/phase2-checked-baseline/repos/PeTTa"
DRIVER="$ROOT/protocosmo2/tools/phase5_omegaclaw_case.py"
PID_FILE=/home/openclaw/.openclaw/protocosmo2-supervisor.pid
CUTOVER_LOCK="$ROOT/local/run-state/protocosmo2-cutover.lock"

if [[ "${1:-}" == "stop-pre-sidecar" || "${1:-}" == "validate-pre-sidecar" ]]; then
  [[ $# -eq 4 && "$2" =~ ^[1-9][0-9]*$ && "$3" =~ ^[0-9]+$ && "$4" =~ ^[0-9a-f]{64}$ ]] || {
    echo "usage: $0 {validate-pre-sidecar|stop-pre-sidecar} EXPECTED_PID EXPECTED_START EXPECTED_CMDLINE_SHA256" >&2; exit 2;
  }
  mkdir -p "$(dirname "$CUTOVER_LOCK")"
  [[ ! -L "$CUTOVER_LOCK" ]] || { echo UNSAFE_CUTOVER_LOCK >&2; exit 2; }
  exec 9>"$CUTOVER_LOCK"
  flock -n 9 || { echo "cutover in progress" >&2; exit 1; }
  LEGACY_PID_FILE="$PID_FILE" EXPECTED_PID="$2" EXPECTED_START="$3" EXPECTED_HASH="$4" \
    EXPECTED_SCRIPT="$(realpath "$0")" EXPECTED_RUNNER="$RUNNER" EXPECTED_CORE="$CORE" \
    EXPECTED_PETTA="$PETTA" EXPECTED_DRIVER="$DRIVER" python3 - <<'PY'
import hashlib, os
from pathlib import Path

pid_path = Path(os.environ["LEGACY_PID_FILE"])
if not pid_path.is_file() or pid_path.is_symlink() or Path(str(pid_path) + ".identity").exists():
    raise SystemExit("legacy ownership boundary absent or ambiguous")
pid = int(pid_path.read_text().strip())
if pid != int(os.environ["EXPECTED_PID"]):
    raise SystemExit("legacy pid changed")
proc = Path(f"/proc/{pid}")
start = (proc / "stat").read_text().split()[21]
raw = (proc / "cmdline").read_bytes()
if start != os.environ["EXPECTED_START"] or hashlib.sha256(raw).hexdigest() != os.environ["EXPECTED_HASH"]:
    raise SystemExit("legacy process identity changed")
args = [x.decode() for x in raw.split(b"\0") if x]
script = os.environ["EXPECTED_SCRIPT"]
if not any(os.path.realpath(args[i]) == script and args[i + 1] == "run" for i in range(len(args) - 1)):
    raise SystemExit("legacy owner command mismatch")
if os.getpgid(pid) != pid:
    raise SystemExit("legacy owner is not its process-group leader")
children = []
for candidate in Path("/proc").glob("[0-9]*/stat"):
    try:
        fields = candidate.read_text().split()
        if int(fields[3]) != pid:
            continue
        child_args = [x.decode() for x in candidate.with_name("cmdline").read_bytes().split(b"\0") if x]
    except (OSError, ValueError):
        continue
    required = [os.environ["EXPECTED_RUNNER"], os.environ["EXPECTED_CORE"], os.environ["EXPECTED_PETTA"], os.environ["EXPECTED_DRIVER"]]
    if not all(value in child_args for value in required):
        raise SystemExit("legacy child command mismatch")
    children.append(int(candidate.parent.name))
if len(children) != 1:
    raise SystemExit(f"expected one legacy receiver child, found {len(children)}")
print(children[0])
PY
  if [[ "$1" == "validate-pre-sidecar" ]]; then
    echo "legacy owner validation passed pid=$2"
    exit 0
  fi
  child_pid=$(LEGACY_PID_FILE="$PID_FILE" EXPECTED_PID="$2" EXPECTED_START="$3" EXPECTED_HASH="$4" \
    EXPECTED_SCRIPT="$(realpath "$0")" EXPECTED_RUNNER="$RUNNER" EXPECTED_CORE="$CORE" \
    EXPECTED_PETTA="$PETTA" EXPECTED_DRIVER="$DRIVER" python3 - <<'PY'
from pathlib import Path
import os
pid=int(os.environ['EXPECTED_PID'])
kids=[]
for p in Path('/proc').glob('[0-9]*/stat'):
 try:
  if int(p.read_text().split()[3]) == pid: kids.append(p.parent.name)
 except (OSError,ValueError): pass
print(kids[0])
PY
  )
  kill -TERM "-$2"
  for _ in $(seq 1 200); do
    [[ ! -e "/proc/$2" && ! -e "/proc/$child_pid" ]] && break
    sleep 0.1
  done
  [[ ! -e "/proc/$2" && ! -e "/proc/$child_pid" ]] || { echo "legacy drain timeout" >&2; exit 1; }
  [[ "$(cat "$PID_FILE" 2>/dev/null || true)" == "$2" ]] || { echo "legacy pid file changed during drain" >&2; exit 1; }
  rm -f "$PID_FILE"
  echo "legacy owner drained pid=$2 child=$child_pid"
  exit 0
fi

export OMEGACLAW_OUTER_RUNNER="$RUNNER"
export OMEGACLAW_OUTER_CORE="$CORE"
export OMEGACLAW_OUTER_TRANSPORT_CORE="$CORE"
export OMEGACLAW_OUTER_PETTA="$PETTA"
export OMEGACLAW_OUTER_DRIVER="$DRIVER"
export OMEGACLAW_OUTER_ENV_FILE=/home/openclaw/.openclaw/protocosmo2.env
export OMEGACLAW_OUTER_CONFIG=/home/openclaw/.openclaw/protocosmo2-canary.json
export OMEGACLAW_OUTER_STATE_DIR=/home/openclaw/.openclaw/protocosmo2-canary-state
export OMEGACLAW_OUTER_WORKER_STATE_DIR=/home/openclaw/.openclaw/protocosmo2-worker-state
export OMEGACLAW_OUTER_PID_FILE="$PID_FILE"
export OMEGACLAW_OUTER_START_LOCK=/home/openclaw/.openclaw/protocosmo2-supervisor.pid.start.lock
export OMEGACLAW_CUTOVER_LOCK="$CUTOVER_LOCK"
export OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER=/home/openclaw/.openclaw/protocosmo2-deferred-disabled
export OMEGACLAW_OUTER_LOG=/home/openclaw/.openclaw/protocosmo2-supervisor.log
export OMEGACLAW_OUTER_IDENTITY=ProtoCosmo2
export OMEGACLAW_OUTER_BOT_ID=8716054285
export OMEGACLAW_OUTER_BOT_USERNAME=@protocosmo2bot
export OMEGACLAW_OUTER_SESSION_PREFIX=protocosmo2-canary
export OMEGACLAW_OUTER_AGENT_ID=main
export OMEGACLAW_OUTER_MODEL=openai/gpt-5.6-sol
export OMEGACLAW_OUTER_PROVIDER_TIMEOUT=240
export OMEGACLAW_OUTER_POLL_TIMEOUT=15

exec "$ROOT/local/protomega-outer-telegram-supervisor.sh" "$@"
