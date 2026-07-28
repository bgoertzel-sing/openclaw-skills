#!/usr/bin/env bash
set -euo pipefail

workspace="/home/openclaw/research-agent"
base="$workspace/projects/agent-recovery/repos"
mkdir -p "$base"

setup_repo() {
  local name="$1"
  local url="https://github.com/bgoertzel-sing/${name}.git"
  local dir="$base/$name"
  if [[ ! -d "$dir/.git" ]]; then
    rm -rf "$dir"
    git clone "$url" "$dir"
  fi
  git -C "$dir" remote set-url origin "$url"
  git -C "$dir" fetch origin main --quiet
}

write_last_backup_marker() {
  local dir="$1"
  local ts status short_hash file_count
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  short_hash="$(git -C "$dir" rev-parse --short HEAD)"
  file_count="$(find "$dir" -not -path '*/.git/*' -type f | wc -l)"
  printf '%s|ok|%s|%d files\n' "$ts" "$short_hash" "$file_count" > "$dir/LAST_BACKUP"
}

commit_and_push_if_changed() {
  local dir="$1"
  local msg="$2"
  git -C "$dir" add -A
  if git -C "$dir" diff --cached --quiet; then
    echo "No new snapshot changes for $(basename "$dir")"
  else
    git -C "$dir" commit -m "$msg"
  fi
  git -C "$dir" pull --rebase --autostash origin main
  if [[ "$(git -C "$dir" rev-list --count origin/main..HEAD)" != "0" ]]; then
    git -C "$dir" push origin HEAD:main
  else
    echo "No unpushed commits for $(basename "$dir")"
  fi
  write_last_backup_marker "$dir"
  git -C "$dir" add LAST_BACKUP
  if ! git -C "$dir" diff --cached --quiet; then
    git -C "$dir" commit -m "Update LAST_BACKUP marker"
    git -C "$dir" push origin HEAD:main
  fi
}

setup_repo zerobot-recovery
setup_repo protomegabot-recovery

"$workspace/projects/agent-recovery/scripts/backup-zerobot-recovery.sh" "$base/zerobot-recovery"
"$workspace/projects/agent-recovery/scripts/backup-protomegabot-recovery.sh" "$base/protomegabot-recovery"

commit_and_push_if_changed "$base/zerobot-recovery" "Update ZeroBot recovery snapshot"
commit_and_push_if_changed "$base/protomegabot-recovery" "Update Protomegabot recovery snapshot"
