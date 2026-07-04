# OpenClaw configuration smoke test

- Slug: `openclaw-smoke`
- Status: `completed`
- Created: `2026-06-25`
- Last reviewed: `2026-06-25`
- Owner: Benjamin Goertzel

## Purpose

Verify that the research-agent workspace can create project records, run a local
test, index memory, and report setup status without touching paid services or
external repositories.

## Success criteria

- Workspace bootstrap verified.
- A tiny local Python test runs successfully.
- Memory index is clean.
- Remaining setup gaps are recorded in `catalog/SETUP_REPORT.md`.

## Scope

### In scope

- Local workspace structure.
- Local Python smoke test.
- OpenClaw config, memory, sandbox, Telegram, and skill readiness checks.

### Out of scope for now

- GitHub authentication, because `gh` is not installed yet.
- Docker, QMD, Runpod, ASI:Cloud, or paid/remote compute configuration.

## Current state

Smoke test completed on 2026-06-25. The local research workspace is installed
and indexed. Optional or approval-gated setup remains: install general
prerequisites such as `gh` and `tmux`, then authenticate GitHub if desired.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| smoke-test | none | `projects/openclaw-smoke/repos/tiny-python` | `main` | local-only |

## Environments

- Python 3.10.12 from system install.
- No remote compute resources.

## Key results

- `experiments/2026-06-25-tiny-python-test/RUN.md`

## Open questions

- Should the Pop!_OS prerequisite script be applied with `sudo apt-get` to
  install `gh`, `tmux`, `shellcheck`, `secret-tool`, and related tools?

## Related projects and concepts

- Research-agent setup and operational policy.

## Risks

Include correctness, reproducibility, security, cost, licensing, and semantic risks.

- GitHub workflows remain unavailable until `gh` is installed and authenticated.
- QMD, Docker, Runpod, and ASI:Cloud are intentionally not configured.
