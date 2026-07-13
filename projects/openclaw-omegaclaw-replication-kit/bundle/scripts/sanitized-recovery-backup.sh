#!/usr/bin/env bash
set -euo pipefail
ROOT="${RESEARCH_AGENT_ROOT:-$HOME/research-agent}"
DEST="${RECOVERY_BACKUP_DIR:-$HOME/recovery-backups}"
ts=$(date -u +%Y%m%dT%H%M%SZ); stage=$(mktemp -d); trap 'rm -rf "$stage"' EXIT
out="$DEST/research-agent-recovery-$ts.tar.gz"; mkdir -p "$DEST" "$stage/research-agent"

# Context, policies, catalogs, templates, local skills/plugins, and project notebooks.
for p in AGENTS.md SOUL.md IDENTITY.md USER.md TOOLS.md HEARTBEAT.md MEMORY.md catalog templates skills plugins bin; do
  [[ -e "$ROOT/$p" ]] && cp -a "$ROOT/$p" "$stage/research-agent/"
done
mkdir -p "$stage/research-agent/memory" "$stage/research-agent/projects"
find "$ROOT/memory" -maxdepth 1 -type f -name '*.md' -exec cp {} "$stage/research-agent/memory/" \; 2>/dev/null || true
# Project records only: never repos, artifacts, databases, caches, logs, or secrets.
while IFS= read -r -d '' p; do
  rel="${p#$ROOT/projects/}"; mkdir -p "$stage/research-agent/projects/$(dirname "$rel")"; cp "$p" "$stage/research-agent/projects/$rel"
done < <(find "$ROOT/projects" -type f \( -name PROJECT.md -o -name TASKS.md -o -name DECISIONS.md -o -name NOTES.md \) -print0 2>/dev/null)

# Refuse suspicious secret material. False positives should be reviewed, not bypassed silently.
if grep -RIlE '(BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY|[0-9]{8,12}:[A-Za-z0-9_-]{30,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})' "$stage" | grep -q .; then
  echo 'Secret-like material detected; backup aborted.' >&2; exit 1
fi
( cd "$stage" && find . -type f -print0 | sort -z | xargs -0 sha256sum > MANIFEST.sha256 )
tar -C "$stage" -czf "$out" .
tar -tzf "$out" >/dev/null
sha256sum "$out" >"$out.sha256"
echo "$out"
