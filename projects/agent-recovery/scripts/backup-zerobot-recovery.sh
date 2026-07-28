#!/usr/bin/env bash
set -euo pipefail

# Build a sanitized ZeroBot/OpenClaw disaster-recovery repo snapshot.
# Usage: backup-zerobot-recovery.sh /path/to/zerobot-recovery-repo

if [[ $# -ne 1 ]]; then
  echo "usage: $0 /path/to/zerobot-recovery-repo" >&2
  exit 2
fi

repo="$1"
workspace="/home/openclaw/research-agent"
mkdir -p "$repo"
cd "$workspace"

mkdir -p \
  "$repo/openclaw-context" \
  "$repo/memory" \
  "$repo/catalog" \
  "$repo/projects" \
  "$repo/scripts"

cat > "$repo/README.md" <<'EOF'
# ZeroBot Recovery

Private disaster-recovery snapshot for reconstructing ZeroBot / OpenClaw research-agent context on a replacement machine.

This repository intentionally excludes credentials and live OpenClaw state. Re-enter secrets through the normal OpenClaw/provider setup flow after restoration.
EOF

cat > "$repo/MANIFEST.md" <<'EOF'
# Manifest

## Included

- OpenClaw/research-agent operating context: `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `MEMORY.md`, `HEARTBEAT.md` when present.
- Daily memory logs under `memory/*.md`.
- Project catalog and setup report.
- Project notebooks: `PROJECT.md`, `TASKS.md`, `DECISIONS.md`, `NOTES.md`, selected docs/runbooks.
- Backup/restore scripts.

## Excluded

- `~/.openclaw` and all credential stores.
- API keys, Telegram tokens, SSH keys, provider credentials, recovery codes.
- Raw session logs unless separately curated and sanitized.
- `projects/*/repos/`, `.venv`, caches, model weights, build outputs, large artifacts.
- Experiment artifacts unless explicitly curated later.
EOF

cat > "$repo/RESTORE.md" <<'EOF'
# Restore Notes

1. Install OpenClaw on the replacement machine using current upstream docs.
2. Clone this private recovery repo.
3. Copy files from `openclaw-context/` into the new research-agent workspace after reviewing differences.
4. Copy `memory/`, `catalog/`, and `projects/` notebooks into the workspace.
5. Recreate credentials manually; do not expect this repo to contain tokens or `~/.openclaw` state.
6. Run OpenClaw status/smoke checks and inspect `catalog/SETUP_REPORT.md` plus active project records.
EOF

for f in AGENTS.md SOUL.md IDENTITY.md USER.md TOOLS.md MEMORY.md HEARTBEAT.md; do
  [[ -f "$f" ]] && cp -p "$f" "$repo/openclaw-context/$f"
done

if [[ -d memory ]]; then
  rsync -a --include='*/' --include='*.md' --exclude='*' memory/ "$repo/memory/"
fi

for f in catalog/PROJECTS.md catalog/SETUP_REPORT.md; do
  [[ -f "$f" ]] && cp -p "$f" "$repo/catalog/$(basename "$f")"
done

# Copy project notebooks and selected small docs/runbooks, never repos/artifacts/caches.
find projects -maxdepth 3 -type f \
  \( -name 'PROJECT.md' -o -name 'TASKS.md' -o -name 'DECISIONS.md' -o -name 'NOTES.md' -o -name 'RUNBOOK.md' \) \
  -not -path '*/repos/*' -not -path '*/artifacts/*' -not -path '*/experiments/*' \
  -print0 | while IFS= read -r -d '' src; do
    dest="$repo/$src"
    mkdir -p "$(dirname "$dest")"
    cp -p "$src" "$dest"
  done

cp -p projects/agent-recovery/scripts/backup-zerobot-recovery.sh "$repo/scripts/"
cp -p projects/agent-recovery/scripts/push-recovery-repos.sh "$repo/scripts/"

cat > "$repo/.gitignore" <<'EOF'
.env
*.env
*.pem
*.key
id_rsa*
id_ed25519*
.openclaw/
repos/
.venv/
node_modules/
__pycache__/
*.pyc
.DS_Store
EOF

# Lightweight fail-closed scan for obvious secret material in staged snapshot.
if grep -RInE '(BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY|bot[0-9]{8,}:[A-Za-z0-9_-]{30,}|sk-(proj-)?[A-Za-z0-9]{32,}|gh[pousr]_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{20,})' "$repo" \
  --exclude-dir=.git --exclude='backup-zerobot-recovery.sh'; then
  echo "Potential secret pattern found; inspect before committing." >&2
  exit 3
fi

echo "ZeroBot recovery snapshot prepared at $repo"
