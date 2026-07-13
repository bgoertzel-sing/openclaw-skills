# Tool and Environment Notes

This file records non-secret local conventions only.

## Paths

- Workspace: `<WORKSPACE>` (recommended: `~/research-agent`)
- Projects: `<WORKSPACE>/projects/<slug>`
- Library: `<WORKSPACE>/library/<slug>`
- Catalog: `<WORKSPACE>/catalog`
- Helpers: `<WORKSPACE>/bin`
- Temporary work: `<WORKSPACE>/scratch`
- Retired material: `<WORKSPACE>/archive`
- OpenClaw state/credentials: `~/.openclaw` — never commit or copy into bundles

## Preferred tools

- Source control: `git`, `gh`
- Search/structured text: `rg`, `fd`, `jq`, `yq`
- Long-running work: `tmux`
- Python: per-project venv
- Rust: repository-pinned `rustup` toolchain
- Containers: Docker/Podman when appropriate
- Exact code search: `rg`, `git grep`, symbol tools, tests, CI metadata

## Credentials

Use OpenClaw SecretRefs, provider CLIs, or OS secret stores. Never put credentials in this file, project records, commands, logs, Git, or model prompts.

## Git identity

Configure explicitly; never infer an email address. Check before committing:

```bash
git config --get user.name
git config --get user.email
gh auth status
```
