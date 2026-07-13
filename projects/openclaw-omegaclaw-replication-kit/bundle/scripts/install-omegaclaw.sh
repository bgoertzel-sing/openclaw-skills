#!/usr/bin/env bash
set -euo pipefail

ROOT="${RESEARCH_AGENT_ROOT:-$HOME/research-agent}"
PROJECT_ROOT="${OMEGACLAW_PROJECT_ROOT:-$ROOT/projects/omegaclaw}"
PETTA="$PROJECT_ROOT/repos/PeTTa"
KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PETTA_URL="${PETTA_URL:-https://github.com/bgoertzel-sing/PeTTa.git}"
PETTA_COMMIT="${PETTA_COMMIT:-4ce1d0ea58855abb772b911278312c8846e5cc08}"
OMEGA_URL="${OMEGA_URL:-https://github.com/asi-alliance/OmegaClaw-Core.git}"
OMEGA_BASE="${OMEGA_BASE:-16d380d9ff32675aa3f19bec7419229b99a7ae12}"
CHROMA_URL="${CHROMA_URL:-https://github.com/patham9/petta_lib_chromadb.git}"

command -v git >/dev/null && command -v python3 >/dev/null && command -v swipl >/dev/null || {
  echo "Install git, Python 3+venv, and SWI-Prolog >=9.3 first (see docs/01-prerequisites.md)." >&2; exit 2; }
SWI_VER="$(swipl --version | awk '{print $3}')"
python3 - "$SWI_VER" <<'PY'
import sys
v=tuple(int(x) for x in sys.argv[1].split('.')[:2])
if v < (9,3): raise SystemExit(f"SWI-Prolog >=9.3 required, found {sys.argv[1]}")
PY

mkdir -p "$PROJECT_ROOT/repos" "$PROJECT_ROOT/local" "$PROJECT_ROOT/artifacts"
if [[ ! -d "$PETTA/.git" ]]; then git clone "$PETTA_URL" "$PETTA"; fi
git -C "$PETTA" fetch --all --tags
git -C "$PETTA" checkout --detach "$PETTA_COMMIT"

OMEGA="$PETTA/repos/OmegaClaw-Core"
if [[ ! -d "$OMEGA/.git" ]]; then git clone "$OMEGA_URL" "$OMEGA"; fi
git -C "$OMEGA" fetch origin
git -C "$OMEGA" checkout --detach "$OMEGA_BASE"
if git -C "$OMEGA" apply --reverse --check "$KIT_ROOT/patches/omegaclaw/omega-runtime-botapi10.patch" 2>/dev/null; then
  echo "OmegaClaw runtime patch already applied."
else
  git -C "$OMEGA" apply --check "$KIT_ROOT/patches/omegaclaw/omega-runtime-botapi10.patch"
  git -C "$OMEGA" apply "$KIT_ROOT/patches/omegaclaw/omega-runtime-botapi10.patch"
fi
cp "$KIT_ROOT/patches/omegaclaw/test_botapi10_safeguards.py" "$OMEGA/Autotests/"

if [[ ! -d "$PETTA/repos/petta_lib_chromadb/.git" ]]; then git clone "$CHROMA_URL" "$PETTA/repos/petta_lib_chromadb"; fi
cp "$OMEGA/run.metta" "$PETTA/run.metta"
ln -sfn repos/OmegaClaw-Core "$PETTA/OmegaClaw-Core"
python3 -m venv "$PETTA/.venv"
"$PETTA/.venv/bin/python" -m pip install --upgrade pip wheel
if [[ "${CPU_ONLY_TORCH:-1}" == 1 ]]; then
  "$PETTA/.venv/bin/python" -m pip install --index-url https://download.pytorch.org/whl/cpu 'torch==2.5.1'
fi
"$PETTA/.venv/bin/python" -m pip install -r "$OMEGA/requirements.txt"
"$PETTA/.venv/bin/python" -m pip install -e "$PETTA"

mkdir -p "$PROJECT_ROOT/local" "$OMEGA/memory"
cp "$KIT_ROOT/scripts/run-omegaclaw-telegram.sh" "$PROJECT_ROOT/local/"
cp "$KIT_ROOT/scripts/omegaclaw-supervisor.sh" "$PROJECT_ROOT/local/"
cp "$KIT_ROOT/templates/omegaclaw/prompt_OpenClaw.txt" "$OMEGA/memory/"
chmod +x "$PROJECT_ROOT/local/"*.sh

echo "Installed OmegaClaw at $OMEGA"
echo "Next: customize prompt, create ~/.openclaw/omegaclaw-telegram.env (0600), configure gateway token, then run verify-kit.sh."
