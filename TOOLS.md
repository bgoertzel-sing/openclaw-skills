# Tool and Environment Notes

This file describes local conventions. It must not contain credentials.

## Paths

- OpenClaw workspace: `~/research-agent`
- Project notebooks: `~/research-agent/projects/<slug>`
- Searchable library: `~/research-agent/library/<slug>`
- Cross-project catalog: `~/research-agent/catalog`
- Local helper commands: `~/research-agent/bin`
- Temporary work: `~/research-agent/scratch`
- Retired material: `~/research-agent/archive`
- OpenClaw state and credentials: `~/.openclaw` (never commit)

## Preferred command-line tools

- Source control and GitHub: `git`, `gh`
- Search and structured text: `rg`, `fd`/`fdfind`, `jq`, `yq` when installed
- Long-running work: `tmux`
- Transfer: `rsync`, `scp`, `sftp`
- Python isolation: `python3 -m venv` or project-declared tool; do not assume one universal environment manager
- Rust: repository-pinned stable/nightly toolchain through `rustup`
- Containers: Docker when installed and appropriate
- Memory search: OpenClaw `memory_search`, QMD, and memory-wiki when enabled
- Exact code search: `rg`, `git grep`, language-aware tools, tests, and CI definitions

## Git identity

Configure Git identity interactively or through an approved existing setup. Never infer or publish an email address. Check before committing:

```bash
git config --get user.name
git config --get user.email
gh auth status
```

## Provider adapters

### Runpod

Use official `runpodctl` or provider-maintained skills. Keep the API key in the provider CLI/secret store, not this file. Use `remote-compute-guardrails` for every paid resource.

### ASI:Cloud

Store only non-secret metadata here after configuration:

```text
Inference base URL: <operator-provided, non-secret>
Model aliases: <verified list>
VM SSH naming convention: <verified convention>
```

Do not invent an endpoint from marketing material. Keys belong in a secret store.

## Hyperon-family notes

Do not hardcode global dependencies here. Each project record should identify repository URL, pinned commit, required SWI-Prolog/Python/Rust/CMake/Conan versions, and tested commands.
