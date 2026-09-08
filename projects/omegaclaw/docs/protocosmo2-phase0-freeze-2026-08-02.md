# ProtoCosmo2 Phase 0 Execution Freeze — 2026-08-02

## Decision boundary

Ben authorized execution of the migration plan on 2026-08-02. This freeze
authorizes only Phase 0 evidence capture and Phase 1's read-only, sanitized
source snapshot. It does **not** authorize a live OmegaClaw service, a
Telegram token or bot, provider credentials, network listeners, supervisors,
cross-agent bridges, paid compute, or importing the snapshot into a runtime.

## Pinned candidate baseline (observed 2026-08-02)

| Component | Candidate commit | Source state | Phase-2 use |
|---|---|---|---|
| OmegaClaw-Core | `b13b17e13218ae08273b878b7e1f4cec55090ca2` | local branch `agent/late-extension-registry`; dirty and one commit ahead of `origin/main` | Re-clone detached at this commit; do not use the dirty checkout. |
| PeTTa | `4ce1d0ea58855abb772b911278312c8846e5cc08` | local branch `agent/specializer-failed-memo-fable`; untracked local dependencies | Re-clone detached at this commit. |
| ThreadKeeper | `0bcea380cd8fe7b705b5e3c28105d8b4364b3ead` | local branch `agent/threadkeeper-hardening-next`; 183 commits ahead of its tracking branch | Re-clone detached at this commit only after ancestry/review confirmation. |
| petta_lib_chromadb | `456385457e4e99ee049c2c0966988a6cd7ff3705` | clean `master` | Re-clone detached at this commit. |

This is a candidate baseline, not a claim that the local working trees are
deployable. The Phase-2 instance must be built from clean detached checkouts
and independently record dependency versions.

## Capability mapping for the baseline

| Required ProtoCosmo2 function | Candidate OmegaClaw facility | Status |
|---|---|---|
| Runtime identity contract | `memory/prompt.txt` / provider-specific prompt | adapter required |
| Curated source corpus | Markdown `knowledge-priors` plus ChromaDB index | adapter required; immutable archive remains canonical |
| Episodic runtime history | `memory/history.metta` | separate ProtoCosmo2-only state |
| Working task state | `pin` | compatible, non-durable |
| Telegram transport | `channels/telegram.py` | deferred until new token/allowlists and mock checks |
| Provider/tool routing | MeTTa skills and Python bridges | adapter and refusal tests required |
| Long-running orchestration | ThreadKeeper candidate | deferred until isolated mock runtime and explicit feature gate |
| OpenClaw-only services (memory search, cron, sessions, gateways) | no established target equivalent | fail-closed stubs or explicit adapters required |

## Phase-1 acceptance criteria

1. The manifest is generated from an explicit include set and has SHA-256,
   size, source class, and source path for every included file.
2. Secret-bearing paths and secret-like content cause a refusal before a
   snapshot copy is created.
3. The snapshot contains only approved Markdown/text policy, memory, catalog,
   project-record, selected run-record, skill, and helper-script inputs.
4. The receipt includes exclusions, scan result, source digest, and restoration
   instructions. It does not print secret material.

## Deferred features

Telegram operation; all provider/API configuration; live ChromaDB import;
ThreadKeeper/GoalChainer activation; schedules; writable shared memory;
cross-agent control; autonomous learning; and any external network listener.

## Rollback

Delete no source material. If the Phase-1 scan fails, retain only the failure
receipt and do not create or use a snapshot. If a later phase fails, stop the
ProtoCosmo2 instance and return to ZeroBot without modifying ZeroBot state.

## Relevant research rules

Rules 2, 4, 5, and 7: this freeze fixes the behavioral/safety specification,
records an externally reviewable artifact, captures reproducible evidence, and
keeps target adapters separate from immutable source data.
