#!/usr/bin/env bash
# Provision only immutable, detached source trees.  This script never starts
# OmegaClaw, invokes PeTTa, contacts a provider, or configures a channel.
set -euo pipefail

project_root="/home/openclaw/research-agent/projects/omegaclaw"
target_root="$project_root/protocosmo2/phase2-checked-baseline"
core_source="$project_root/repos/OmegaClaw-Core"
petta_source="$project_root/repos/PeTTa"
chroma_source="$project_root/repos/petta_lib_chromadb"

core_commit="b13b17e13218ae08273b878b7e1f4cec55090ca2"
core_parent="16d380d9ff32675aa3f19bec7419229b99a7ae12"
petta_commit="4ce1d0ea58855abb772b911278312c8846e5cc08"
chroma_commit="456385457e4e99ee049c2c0966988a6cd7ff3705"
swipl="$project_root/local/swipl-9.3.36/bin/swipl"

[[ ! -e "$target_root" ]] || {
  echo "refusing to reuse target: $target_root" >&2
  exit 2
}

clone_detached() {
  local source="$1" dest="$2" commit="$3" canonical_origin="$4"
  git clone --no-local --no-checkout "$source" "$dest"
  git -C "$dest" checkout --detach "$commit"
  git -C "$dest" remote set-url origin "$canonical_origin"
  test "$(git -C "$dest" rev-parse HEAD)" = "$commit"
  test -z "$(git -C "$dest" symbolic-ref -q HEAD || true)"
  test -z "$(git -C "$dest" status --porcelain)"
  git -C "$dest" fsck --no-dangling --no-progress
}

mkdir -p "$target_root/repos" "$target_root/state" "$target_root/logs"
chmod 700 "$target_root" "$target_root/repos" "$target_root/state" "$target_root/logs"

# The local source repositories are used only as object stores because the two
# Ben-authored candidate commits are not advertised by their public upstreams.
# Tree equality below binds the detached targets to the frozen source objects.
clone_detached "$core_source" "$target_root/repos/OmegaClaw-Core" "$core_commit" \
  "https://github.com/asi-alliance/OmegaClaw-Core.git"
clone_detached "$petta_source" "$target_root/repos/PeTTa" "$petta_commit" \
  "https://github.com/trueagi-io/PeTTa.git"
clone_detached "$chroma_source" "$target_root/repos/petta_lib_chromadb" "$chroma_commit" \
  "https://github.com/patham9/petta_lib_chromadb.git"

test "$(git -C "$core_source" rev-parse "$core_commit^{tree}")" = \
  "$(git -C "$target_root/repos/OmegaClaw-Core" rev-parse HEAD^{tree})"
test "$(git -C "$petta_source" rev-parse "$petta_commit^{tree}")" = \
  "$(git -C "$target_root/repos/PeTTa" rev-parse HEAD^{tree})"
test "$(git -C "$chroma_source" rev-parse "$chroma_commit^{tree}")" = \
  "$(git -C "$target_root/repos/petta_lib_chromadb" rev-parse HEAD^{tree})"
test "$(git -C "$core_source" rev-parse "$core_commit^")" = "$core_parent"

{
  printf 'core_commit=%s\n' "$core_commit"
  printf 'core_parent=%s\n' "$core_parent"
  printf 'petta_commit=%s\n' "$petta_commit"
  printf 'chroma_commit=%s\n' "$chroma_commit"
  python3 --version
  if [[ -x "$swipl" ]]; then "$swipl" --version; else echo "SWI-Prolog V9.3.36 missing: $swipl" >&2; exit 3; fi
} | tee "$target_root/provision-receipt.txt"
