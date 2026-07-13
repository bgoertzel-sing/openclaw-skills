# 01 — Prerequisites

## Recommended host

A dedicated, encrypted, patched Linux workstation/VM under a non-root account. Keep inbound firewall closed except what you deliberately require; Telegram and model APIs normally need outbound HTTPS only. Have tested backups before adding private research.

## Required

- Git
- Node.js 22.19+ (Node 24 recommended for the pinned OpenClaw release)
- npm
- Python 3 with `venv` and development headers
- SWI-Prolog 9.3+ with Janus/Python support
- `bash`, `flock`, `timeout`, `curl`, `tar`, `sha256sum`, `grep`, `awk`
- enough disk for Python/Torch/Transformers and optional local embedding models (several GB)
- two Telegram bot tokens and one human Telegram user ID
- at least one configured LLM route for OpenClaw

Example Ubuntu-family packages (review names for your distribution; administrative installation requires your explicit action):

```bash
sudo apt update
sudo apt install git curl build-essential python3 python3-venv python3-dev pkg-config jq unzip
```

Distribution SWI-Prolog may be too old. Install an official SWI 9.3+ package or build a pinned release after reviewing upstream instructions. Confirm:

```bash
node --version
python3 --version
git --version
swipl --version
```

## Optional

- `gh` for GitHub operations
- `rg`, `fd`, `jq`, `yq`, `tmux`
- Docker/Podman or a Linux VM for macOS isolation
- local Ollama-compatible models for low-cost routine traffic
- QMD/semantic-memory plugins; first use may download ~2 GB of embedding/reranking models

## Version policy

This archive is a reproducible snapshot, not a promise of compatibility with future OpenClaw/OmegaClaw. Start with pinned versions/commits. Upgrade one layer at a time, read release notes, validate config against the installed schema, rerun offline tests and both Telegram canaries, then record the new known-good versions.
