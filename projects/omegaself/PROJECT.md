# OmegaSelf — Project Record

## Purpose

Implement the OmegaSelf evidence-grounded self-theory and governance layer for OmegaClaw/ProtoMegaBot. OmegaSelf provides an immutable evidence ledger, substrate-neutral reasoner SPI (Patham9/OmegaPLN adapters), renewable SelfHereNow attestation, signed-policy proposal gates, and continuity certificates for high-impact mutation control.

## Status

**Active** — Phase 3 closure/dependence slice committed; renewable `SelfHereNow` next, 2026-07-15.

## Source

- Architecture and Deployment Guide: `library/omegaself/OmegaSelf_Architecture_and_Deployment_Guide.pdf`
- Source TeX: `library/omegaself/OmegaSelf_Architecture_and_Deployment_Guide.tex`
- Coding agent pack: `library/omegaself/OmegaSelf.zip`
- Provenance sidecar: `library/omegaself/SOURCE.md`
- Inspection copy: `scratch/omegaself-inspect/OmegaSelf/`

## Scope

- Integrate OmegaSelf into the OmegaClaw loop between parse and eval
- Test on ProtoMegaBot2 canary before any live ProtoMegaBot deployment
- Connect Patham9 PLN adapter to existing petta-memory PLN work
- Implement signed-policy governance gates
- Add MeTTa self-model files to OmegaClaw's MeTTa workspace
- 13 ADRs as governance decision records

## Repositories

- **OmegaClaw source (live ProtoMegaBot)**: `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/`
- **ProtoMegaBot2 canary**: `projects/protomegabot2/repos/PeTTa/repos/OmegaClaw-Core/`
- **petta-memory (Patham9 PLN)**: `projects/petta-memory/repos/petta-memory/`
- **OmegaSelf coding pack**: `projects/omegaself/repos/omegaself-coding-agent-pack/`

## Pinned baseline (2026-07-15)

- ProtoMegaBot2 PeTTa: `4ce1d0ea58855abb772b911278312c8846e5cc08`
- ProtoMegaBot2 OmegaClaw-Core: `9a030117e94f4069ea509f2555794f4fc251f20e`
- Live ProtoMegaBot OmegaClaw-Core (observation only): `93db08aa6690ea24ec37d96aeaec451f6d2e7929`
- petta-memory: `7724e5712178ac41506ce59e3d2ecf54fdb3a506`
- Python: 3.10.12; `jsonschema` 4.26.0; `pytest` 9.1.1
- Reasoner baseline: Patham9 PeTTa PLN rules in `lib/lib_pln.metta`, hash `6b980321bbe9b49e5b12e2fcee0479ab1d5c7550c2104a67b0722a5b473da4ee`; no explicit truth-semantics profile ID exists yet.
- Default OmegaClaw sandbox policy: unsigned OpenShell YAML, hash `e69b5549f683ba31a185856af5da7222b5bcaf905eacc734c5336e8a6c033b17`; the optional MeTTa policy guard is default-off and no signed OmegaSelf policy is active.
- Runtime limitation: SWI-Prolog is absent on the host, so the baseline is Python/provider-free rather than a full PeTTa boot.

## Baseline experiments

- `experiments/20260715T231839Z-coding-pack-smoke-baseline-venv/`
- `experiments/20260715T231941Z-coding-pack-schema-validation/`
- `experiments/20260715T231941Z-protomegabot2-provider-free-baseline/`

## Canary implementation branch

- Worktree: `projects/omegaself/repos/protomegabot2-omegaclaw-record-only/`
- Branch/commits: `agent/omegaself-record-only` at `f5add4b` (closure), following `2bfa244` (observation ledger)
- Mode: `OMEGASELF_RECORD_ONLY` default-off; enabled mode observes but does not gate or alter `(eval $s)`.
- Synthetic ledger root: `3e300753c800f7c225e0785b1d77fc264162fcd144c253b5f183f678a1d19a42`
- Rollback: leave `OMEGASELF_RECORD_ONLY` unset (runtime), or revert `f5add4b` then `2bfa244` on the isolated branch.
- No change has been merged into the ProtoMegaBot2 main canary worktree or the live ProtoMegaBot tree.

## Key links

- Core requirements: `scratch/omegaself-inspect/OmegaSelf/OMEGASELF_CORE_REQUIREMENTS.md`
- Quick start: `scratch/omegaself-inspect/OmegaSelf/omegaself-coding-agent-pack/OMEGASELF_CODING_AGENT_QUICKSTART.md`
- Skill definition: `scratch/omegaself-inspect/OmegaSelf/omegaself-coding-agent-pack/SKILL.md`
- ADRs: `scratch/omegaself-inspect/OmegaSelf/omegaself-coding-agent-pack/docs/ADR/`
- Test results: `scratch/omegaself-inspect/OmegaSelf/omegaself-coding-agent-pack/TEST_RESULTS.md`

## Related projects

- `omegaclaw` — parent project for ProtoMegaBot/OmegaClaw
- `protomegabot2` — isolated canary runtime
- `petta-memory` — Patham9 PLN, evidence packets, context selection
- Machintel v2 — chat-room identity and routing (complementary governance layer)

## Deferred successor layer

- **OMERA emotion regimes** — queued for implementation only after OmegaSelf is implemented and validated. The current architectural assumption is OMERA over OmegaSelf, with OmegaSelf itself using the PeTTa Memory/PLN substrate. Source specification: Ben's Telegram attachments `omegaself_emotion_regimes_extended` and `omera_implementation_plan`, messages 10378–10383, 2026-07-20. This dependency placement is provisional until the OmegaSelf–PeTTa Memory interface is stable.
