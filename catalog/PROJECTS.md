# Research Project Catalog

Update this table whenever a project is created, paused, resumed, completed, or archived.

| Slug | Title | Status | Primary repository | Current focus | Last reviewed |
|---|---|---|---|---|---|
| `agent-recovery` | Agent Disaster Recovery Repositories | `active` | proposed private GitHub repos | Prepare separate ZeroBot and Protomegabot recovery backups | 2026-06-28 |
| `openclaw-smoke` | OpenClaw configuration smoke test | `completed` | local-only `projects/openclaw-smoke/repos/tiny-python` | Setup verification complete; remaining gaps in `catalog/SETUP_REPORT.md` | 2026-06-25 |
| `petta-chem` | PeTTa Abstract Algorithmic Chemistry | `idea` | `https://github.com/bgoertzel-sing/petta-chem` | Public repo active; building deterministic PeTTa chemistry experiments | 2026-06-27 |
| `omegaclaw` | OmegaClaw Core Installation | `active` | local clones under `projects/omegaclaw/repos/` | ProtomegaTron Telegram/group setup and safe integration path | 2026-06-27 |
| `goal-relevance-governor` | Goal Relevance Governor | `active` | local design project | Specify cross-project goal/task relevance control and LLM/PLN incarnations | 2026-08-14 |
| `hyperseed-formalizations` | Hyperseed Formalizations | `active` | `https://github.com/bgoertzel-sing/hyperseed-formalizations` | Formalization notes for ProtomegaTron/OmegaClaw/PeTTa work | 2026-06-27 |
| `petta-memory` | PeTTa Intermediate Memory Store | `active` | `https://github.com/bgoertzel-sing/petta-memory` | v0 append-only PLN-ready memory store prototype | 2026-06-27 |
| `specatom-hs` | Plain2Metta / SpecAtom-HS compiler | `active` | public `bgoertzel-sing/plain2metta`; local `projects/specatom-hs/repos/specatom-hs` | Source-preserving fail-closed Plain-like compiler; public name Plain2Metta, internal IR/package `specatom_hs` | 2026-06-29 |
| `omegasim` | OmegaSim Thresholded Appraisal Simulations | `paused` | local `projects/omegasim/repos/omegasim` | Paused pending robust CLA/attractor-grammar detector | 2026-07-03 |
| `relaleap` | RelaLeap SLT Residual-Layer Causal Factors | `active` | TBD | Preregister train-time causal factor learner after v0/v2 fail-closed results | 2026-07-03 |
| `hdpc-tiny-shakespeare` | HDPC Tiny Shakespeare | `idea` | local notebook; repo TBD | Plan and scaffold homotopy-distilled predictive-coding transformer experiment; Runpod gated pending approval | 2026-07-09 |
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

- 2026-07-31: Reconciled catalog: `causal-fibres-ladder` focus updated (GPT-2-small replication is downstream of CMCP Phase 3–4 validation, not the immediate next step); `hdc-cgcct-transformers` focus updated (typed CMCP geometry f848c97 is current bounded result, Phase 3–4 estimator work is active lane). Both changes reflect the sequential dependency: CMCP typed geometry (P0/P1) gates frozen-model probing (P2).
- 2026-07-03: Ben paused OmegaSim and promoted Chaos Language Algorithm to the active prerequisite lane; preserved the Hyperon-ready Python architecture PDF in `library/chaos-language-algorithm/` and updated both project records.
| `openclaw-intent-model-router` | OpenClaw Intent Model Router | `active` | `https://github.com/bgoertzel-sing/openclaw-intent-model-router` | Public reusable cost-aware OpenClaw model router | 2026-07-04 |
| `morkql` | Morkql: MeTTa-Shaped Query Language for MORK Path Spaces | `active` | local `projects/morkql/repos/morkql`; upstream MORK/PathMap pinned locally | Implement/test Base-profile frontend and reproduce MORK build | 2026-07-12 |
| openclaw-omegaclaw-replication-kit | OpenClaw + OmegaClaw Replication Kit | idea |  | define scope and first test | 2026-07-13 |
| protomegabot2 | ProtoMegaBot2 ClarityOmega Runtime | active | ClarityOmega, OmegaClaw | reconcile target commit, then agency telemetry | 2026-07-15 |
| carom | CAROM Execution Semantics | active |  | 12k collapse localized; piecewise rerun invalid operationally; provider-free schedule repair active; structural gain control deferred pending clean schedule evidence | 2026-07-30 |
| `causal-fibres-ladder` | Causal Fibres Evidence-Gated Hypothesis Ladder | `active` | local experiment project; causal-fibres 0.4.0 release | Toy H0 passed; GPT-2-small replication queued downstream of CMCP Phase 3–4 estimator validation | 2026-07-31 |
| `omegahive-conversation-governor` | OmegaHive Conversation Governor | `active` | implementation location pending runtime discovery | Shadow-first shared admission, response ownership, and egress governance | 2026-07-24 |
| omegahive-conversation-governor | OmegaHive Conversation Governor | idea |  | define scope and first test | 2026-07-24 |
| `hdc-musicgen` | HDC × MusicGen Experiments | `active` | local `projects/hdc-musicgen/repos/` | GPU preparation frozen at `59eade2`; awaiting explicit paid-run approval | 2026-07-25 |
| `hdc-cgcct-transformers` | HDC–CGCCT Transformer Programme | `active` | local project notebook + isolated P0 repository | Typed CMCP geometry at `f848c97` (305 tests); Phase 3 estimator comparison and Phase 4 assimilation-vs-maintenance are the active provider-free lane | 2026-07-31 |
| remote-job-bootstrap | SSH-Free RunPod Bootstrap Bundles | active |  | confirm public GitHub owner/name, then publish hash-pinned bundles | 2026-07-29 |
| pop-os-vm8-migration | Pop!_OS Proto-Hive Migration to VM8 | active | local project notebook; ASI:Cloud VM8 pending approved remote contract | local four-agent inventory; then bounded VM8 audit | 2026-08-11 |
| goal-relevance-governor | Goal Relevance Governor | idea |  | define scope and first test | 2026-08-14 |
