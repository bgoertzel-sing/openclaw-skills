# ProtoCosmo2 Migration — Pinned Target Commits

Frozen: 2026-08-02T21:50:00-07:00

## Baseline Runtime

| Component | Commit | Branch | Description |
|---|---|---|---|
| OmegaClaw-Core | `16d380d` + cherry-pick `b13b17e` | `main` + one fix | main tip + balance_parentheses multiline fix |
| PeTTa | `4ce1d0ea58855abb772b911278312c8846e5cc08` | `main` | Fix failed specialization memoization |
| SWI-Prolog | `V9.3.36` | local build | Installed at `local/swipl-9.3.36` |
| petta_lib_chromadb | *use current checkout* | `main` | ChromaDB embedding helper |

## Deferred (Phase 8)

| Component | Commit at freeze | Branch | Reason for deferral |
|---|---|---|---|
| ThreadKeeper | `0bcea38` | `agent/threadkeeper-hardening-next` | Active hardening; 80+ commits ahead of main |
| GoalChainer | `d993e49` | — | GGB gate work in progress |
| Late extensions | — | — | Deontic/directive add complexity to baseline |

## Environment

| Item | Value |
|---|---|
| Host OS | Pop!_OS / Linux 7.0.11 (x64) |
| Python | venv at `repos/PeTTa/.venv` |
| Node.js | v24.18.0 |
| Embedding model | `intfloat/e5-large-v2` (local, dim 1024) |
| LLM provider | OpenClaw Gateway (`http://127.0.0.1:18789/v1`) |
| Session user | `protocosmo2-telegram` |

## Rollback

If any Phase gate fails, revert to Protomegabot-only operation.
ProtoCosmo2's directory tree can be deleted without affecting Protomegabot.
