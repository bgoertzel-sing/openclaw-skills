# OpenClaw Research-Agent Setup Report

- Date: 2026-06-25
- OpenClaw version: 2026.6.10 (aa69b12)
- Host: Pop!_OS 22.04 LTS, Linux 5.16.19
- Workspace: `~/research-agent`
- Backup: `~/openclaw-backups/20260625T171431Z`

## Summary

The research-agent workspace bootstrap is installed and verified. The setup
preserved local identity customizations for ZeroBot and Benjamin, copied the
research skills, templates, setup-kit config examples, and helper scripts, and
set the live OpenClaw workspace to `~/research-agent`.

## Model And Auth

- Primary model route: `openai/gpt-5.5`
- Auth type: existing OpenClaw/OpenAI auth; no credentials inspected or recorded.

## Gateway And Telegram

- Gateway bind: loopback.
- Gateway port: 18789.
- Telegram: enabled, configured, running, connected, polling mode, bot probe
  successful.
- Telegram access posture: direct-message allowlist with one numeric user ID.
- Groups: not enabled in the summarized live config.
- Token handling: token not recorded in this workspace report.

## Sandbox And Exec Policy

- Sandbox mode: `non-main`.
- Sandbox scope: `agent`.
- Workspace access: read/write.
- Current main session sandboxed: no.
- Exec policy: approval-backed allowlist with ask-on-miss.
- Elevated execution: disabled.

## Memory

- Plain Markdown memory is present.
- Memory index status after rebuild: clean.
- Indexed files: 3/3 memory files, 3 chunks.
- QMD: installed and indexed as a local semantic search layer.
  - Version: `qmd 2.5.3`.
  - Index: `~/.cache/qmd/index.sqlite`.
  - Collections: `memory`, `projects`, `library`, `catalog`.
  - Indexed documents: 12 files, 13 embedded chunks.
  - Cached models: embedding model and query-expansion model downloaded.
- Dreaming: off.
- Memory-wiki: not configured.

## Skills

Ready bundled skills:

- `healthcheck`
- `skill-creator`

Ready workspace skills:

- `research-projects`
- `experiment-ledger`
- `repository-operations`
- `remote-compute-guardrails`
- `hyperon-workbench`
- `knowledge-curation`
- `research-library`

Needs setup:

- `github`: `gh` is installed and authenticated as `bgoertzel-sing`.
- `coding-agent`: configured but this OpenClaw doctor run reported no available
  coding-agent binary in its check path.
- `session-logs`: needs setup.
- `summarize`: blocked by missing `summarize` command.

Note: `openclaw healthcheck` is not a built-in CLI command in this install,
despite the bundled skill being ready. Use `openclaw doctor` and the
`healthcheck` skill instructions when applicable.

## Local Prerequisites

Present:

- `openclaw`
- `git`
- `python3`
- `node`
- `npm`
- `jq`
- `rg`
- `rsync`
- `ssh`
- `gcc`
- `cmake`
- `gh`
- `tmux`
- `secret-tool`
- `shellcheck`
- `fd`
- `pipx`
- `qmd`

Missing from current PATH:

- `docker`
- `runpodctl`

The Pop!_OS prerequisite script was reviewed and applied after explicit
administrative approval.

## GitHub

- GitHub CLI: installed.
- Authentication status: logged in to github.com as `bgoertzel-sing`.
- Git operations for github.com are configured to use HTTPS.
- No remote repository was created or modified.

## Remote Compute

- Runpod: not configured.
- ASI:Cloud: not configured.
- Paid cloud resources: none created.

## Smoke Tests

Completed:

- Workspace verifier found all required workspace files and local skills.
- `openclaw doctor --lint` ran; warnings are listed above.
- `openclaw memory status --index --agent main` rebuilt the memory index.
- `openclaw exec-policy show` confirmed approval-backed allowlist after restart.
- Local smoke project created at `projects/openclaw-smoke`.
- Tiny Python repository initialized and locally committed.
- Unit test command succeeded:

```bash
cd ~/research-agent/projects/openclaw-smoke
bash experiments/2026-06-25-tiny-python-test/command.sh
```

Result: 1 unit test passed.

- Targeted secret scan found 0 Telegram-token-shaped strings and 0 private key
  blocks under `~/research-agent`.
- QMD indexed the research-agent Markdown collections and passed lexical and
  semantic smoke searches for `research project decisions`.

Skipped or blocked:

- GitHub identity query succeeded as `bgoertzel-sing`.
- Docker/Runpod/ASI:Cloud checks skipped because they are optional or require
  explicit approval.

## Recommended Next Actions

1. Leave Runpod and ASI:Cloud unconfigured until a specific paid-compute task
   has an explicit cost and cleanup plan.
