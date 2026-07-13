#!/usr/bin/env bash
set -euo pipefail
KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE="${WORKSPACE:-$HOME/research-agent}"
OWNER_NAME="${OWNER_NAME:?Set OWNER_NAME}"
OWNER_SHORT_NAME="${OWNER_SHORT_NAME:-$OWNER_NAME}"
OPENCLAW_AGENT_NAME="${OPENCLAW_AGENT_NAME:-OpenClawAgent}"
OMEGACLAW_AGENT_NAME="${OMEGACLAW_AGENT_NAME:-OmegaClawAgent}"
TIMEZONE="${TIMEZONE:-UTC}"
LANGUAGES_AND_SYSTEMS="${LANGUAGES_AND_SYSTEMS:-Python, Rust, symbolic AI, and project-specific tools}"
HOST_DESCRIPTION="${HOST_DESCRIPTION:-dedicated research workstation}"
ROUTINE_MODEL_POLICY="${ROUTINE_MODEL_POLICY:-economical routine model; frontier models for hard work and explicit reviews}"
OWNER_PUBLIC_WRITING_URL="${OWNER_PUBLIC_WRITING_URL:-https://example.org/writing}"
export OWNER_NAME OWNER_SHORT_NAME OPENCLAW_AGENT_NAME OMEGACLAW_AGENT_NAME TIMEZONE LANGUAGES_AND_SYSTEMS HOST_DESCRIPTION ROUTINE_MODEL_POLICY OWNER_PUBLIC_WRITING_URL

if [[ -e "$WORKSPACE/AGENTS.md" && "${FORCE:-0}" != 1 ]]; then
  echo "Refusing to overwrite existing workspace $WORKSPACE. Set FORCE=1 only after backup/review." >&2; exit 2
fi
mkdir -p "$WORKSPACE"/{bin,catalog,memory,projects,library,archive,scratch,logs,plugins,skills}
cp -a "$KIT_ROOT/templates/openclaw-workspace/." "$WORKSPACE/"
cp -a "$KIT_ROOT/skills/." "$WORKSPACE/skills/"
cp -a "$KIT_ROOT/plugins/." "$WORKSPACE/plugins/"
cp "$KIT_ROOT/scripts/new-project" "$KIT_ROOT/scripts/new-experiment" "$KIT_ROOT/scripts/capture-environment" "$KIT_ROOT/scripts/verify-install" \
  "$KIT_ROOT/scripts/omegaclaw-watchdog.sh" "$KIT_ROOT/scripts/sanitized-recovery-backup.sh" "$KIT_ROOT/scripts/install-schedules.sh" \
  "$WORKSPACE/bin/"
chmod +x "$WORKSPACE/bin/"*

python3 - "$WORKSPACE" <<'PY'
from pathlib import Path
import os, sys
root=Path(sys.argv[1])
repl={
 '<WORKSPACE>':str(root), '<OWNER_NAME>':os.environ['OWNER_NAME'],
 '<OWNER_SHORT_NAME>':os.environ.get('OWNER_SHORT_NAME',os.environ['OWNER_NAME']),
 '<OPENCLAW_AGENT_NAME>':os.environ.get('OPENCLAW_AGENT_NAME','OpenClawAgent'),
 '<OMEGACLAW_AGENT_NAME>':os.environ.get('OMEGACLAW_AGENT_NAME','OmegaClawAgent'),
 '<TIMEZONE>':os.environ.get('TIMEZONE','UTC'),
 '<LANGUAGES_AND_SYSTEMS>':os.environ.get('LANGUAGES_AND_SYSTEMS','Python, Rust, symbolic AI, and project-specific tools'),
 '<HOST_DESCRIPTION>':os.environ.get('HOST_DESCRIPTION','dedicated research workstation'),
 '<ROUTINE_MODEL_POLICY>':os.environ.get('ROUTINE_MODEL_POLICY','economical routine model; frontier models for hard work and explicit reviews'),
 '<OWNER_PUBLIC_WRITING_URL>':os.environ.get('OWNER_PUBLIC_WRITING_URL','https://example.org/writing'),
}
for p in root.rglob('*'):
 if p.is_file() and p.suffix.lower() in {'.md','.txt','.json','.json5','.yaml','.yml','.sh','.py'}:
  try: s=p.read_text()
  except UnicodeDecodeError: continue
  for a,b in repl.items(): s=s.replace(a,b)
  p.write_text(s)
PY

echo "Workspace created at $WORKSPACE"
echo "Next: review every prompt/policy file, customize config template, and run openclaw config validate."
