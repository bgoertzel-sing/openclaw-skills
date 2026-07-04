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
}

commit_and_push_if_changed() {
  local dir="$1"
  local msg="$2"
  git -C "$dir" add -A
  if git -C "$dir" diff --cached --quiet; then
    echo "No changes for $(basename "$dir")"
    return 0
  fi
  git -C "$dir" commit -m "$msg"
  git -C "$dir" push origin HEAD:main
}

setup_repo zerobot-recovery
setup_repo protomegabot-recovery

"$workspace/projects/agent-recovery/scripts/backup-zerobot-recovery.sh" "$base/zerobot-recovery"
"$workspace/projects/agent-recovery/scripts/backup-protomegabot-recovery.sh" "$base/protomegabot-recovery"

commit_and_push_if_changed "$base/zerobot-recovery" "Update ZeroBot recovery snapshot"
commit_and_push_if_changed "$base/protomegabot-recovery" "Update Protomegabot recovery snapshot"
