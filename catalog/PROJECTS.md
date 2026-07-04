# Research Project Catalog

Update this table whenever a project is created, paused, resumed, completed, or archived.

| Slug | Title | Status | Primary repository | Current focus | Last reviewed |
|---|---|---|---|---|---|
| `agent-recovery` | Agent Disaster Recovery Repositories | `active` | proposed private GitHub repos | Prepare separate ZeroBot and Protomegabot recovery backups | 2026-06-28 |
| `openclaw-smoke` | OpenClaw configuration smoke test | `completed` | local-only `projects/openclaw-smoke/repos/tiny-python` | Setup verification complete; remaining gaps in `catalog/SETUP_REPORT.md` | 2026-06-25 |
| `petta-chem` | PeTTa Abstract Algorithmic Chemistry | `idea` | `https://github.com/bgoertzel-sing/petta-chem` | Public repo active; building deterministic PeTTa chemistry experiments | 2026-06-27 |
| `omegaclaw` | OmegaClaw Core Installation | `active` | local clones under `projects/omegaclaw/repos/` | ProtomegaTron Telegram/group setup and safe integration path | 2026-06-27 |
| `hyperseed-formalizations` | Hyperseed Formalizations | `active` | `https://github.com/bgoertzel-sing/hyperseed-formalizations` | Formalization notes for ProtomegaTron/OmegaClaw/PeTTa work | 2026-06-27 |
| `petta-memory` | PeTTa Intermediate Memory Store | `active` | `https://github.com/bgoertzel-sing/petta-memory` | v0 append-only PLN-ready memory store prototype | 2026-06-27 |
| `specatom-hs` | SpecAtom-HS Plain-to-MeTTa Compiler | `active` | local `projects/specatom-hs/repos/specatom-hs` | Python stdlib MVP emits source-preserving SpecAtom-HS JSON/MeTTa-ish atoms with crisp validators | 2026-06-29 |
| `omegasim` | OmegaSim Thresholded Appraisal Simulations | `paused` | local `projects/omegasim/repos/omegasim` | Paused pending robust CLA/attractor-grammar detector | 2026-07-03 |
| `relaleap` | RelaLeap SLT Residual-Layer Causal Factors | `active` | TBD | Preregister train-time causal factor learner after v0/v2 fail-closed results | 2026-07-03 |
| `chaos-language-algorithm` | Chaos Language Algorithm | `active` | `https://github.com/bgoertzel-sing/chaos-language-algorithm` (public; local `projects/chaos-language-algorithm/repos/chaoslang`) | Sprint-1 symbolic MVP implemented locally; next persistence + attractor benchmarks | 2026-07-03 |

Status vocabulary: `idea`, `active`, `blocked`, `paused`, `completed`, `archived`.

## Cross-project dependencies

Record shared libraries, datasets, concepts, or decisions that link projects. Use precise pointers.

- `petta-chem` depends conceptually on PeTTa/MeTTa/Atomspace and keeps MORK as a future migration seam, but v0.1 should not require MORK.
- `petta-memory` depends on the design note in `hyperseed-formalizations` and targets later integration with `omegaclaw` / ProtomegaTron.
- `specatom-hs` depends conceptually on `hyperseed-formalizations` notes 0005/0006, SUMO/EXPO/Hyperseed bridge design, and later PeTTa target-profile work.

## Recently closed loops

- 2026-07-03: Ingested Ben's Chaos Language Algorithm PDF and created the `chaos-language-algorithm` project notebook; see `library/chaos-language-algorithm/SOURCE.md` and `projects/chaos-language-algorithm/PROJECT.md`.

Keep only a compact rolling list. Detailed results belong in the relevant project.

- 2026-07-03: Created `relaleap` project notebook and preregistered the train-time causal factor learner design after v0/v2 failed promotion; see `projects/relaleap/docs/train_time_causal_factor_preregistration.md`.
- 2026-06-29: Created `specatom-hs` as the local project notebook for the revised Plain-to-MeTTa / SpecAtom-HS compiler lane; see `projects/specatom-hs/PROJECT.md`.
- 2026-06-27: Created `petta-memory` as a software project and local prototype repo; see `projects/petta-memory/PROJECT.md`.
- 2026-06-27: Created `hyperseed-formalizations` and added ProtomegaTron/medium-memory design notes.
- 2026-06-26: Ingested PeTTa abstract algorithmic chemistry PDF and created `projects/petta-chem`; see `library/petta-abstract-algorithmic-chemistry/SOURCE.md` and `projects/petta-chem/PROJECT.md`.
- 2026-06-25: Installed and verified the research-agent workspace bootstrap; see `catalog/SETUP_REPORT.md`.

- 2026-07-03: Ben paused OmegaSim and promoted Chaos Language Algorithm to the active prerequisite lane; preserved the Hyperon-ready Python architecture PDF in `library/chaos-language-algorithm/` and updated both project records.
| `openclaw-intent-model-router` | OpenClaw Intent Model Router | `active` | `https://github.com/bgoertzel-sing/openclaw-intent-model-router` | Public reusable cost-aware OpenClaw model router | 2026-07-04 |
