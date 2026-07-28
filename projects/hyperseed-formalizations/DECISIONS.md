# Decisions

## 2026-06-27: Public repository name

**Decision:** Use public GitHub repository `bgoertzel-sing/hyperseed-formalizations` for Hyperseed formalizations.

**Rationale:** Ben accepted `hyperseed-formalizations` as an OK repo name and requested public GitHub-hosted LaTeX plus PDF outputs for scrutiny.

**Notes:** Source PDFs are preserved in the local research library rather than vendored into the repo on the first pass.

## 2026-07-15: Present-phase formalization salience gate

**Decision:** Create Hyperseed formalizations only when the source contains genuinely novel conceptual content, such as a consequential experiment result, a real decision, or a surprising failure. Do not formalize logistics, acknowledgements, routine operational chatter, or ordinary status/debug traces.

**Rationale:** Formalization should preserve and sharpen conceptual novelty rather than become an automatic background ritual that consumes attention and clutters the repository.

**Provenance:** Ben adopted this rule in the `bot philosophy` Telegram group on 2026-07-15.

## 2026-07-19: Layer OmegaSelf regimes over continuous Psi and require ablation

**Decision:** Formalize OmegaClaw emotion as a three-layer architecture: a
continuous Psi/MetaMo motivational substrate, objectful evidence-grounded
appraisal through OmegaSelf, and an optional hysteretic regime layer whose
effects are bounded requests to a separate policy governor. Treat the regime
layer as a falsifiable extension, not as something Psi lacks by definition.

**Rationale:** Bach's tutorial already gives continuous modulation causally
active, object-directed emotional organization. The pinned MetaMo source
implements and tests continuous appraisal plus fuzzy named-emotion
classification, but not persistent object/provenance-bearing regime latches.
The proposed latch is justified only if a continuous-only versus latch ablation
shows better long-horizon control, recovery, calibration, or auditability.

**Formal caution:** Use behavioral rather than syntactic actuator support. Do
not claim palette size is bounded by actuator count. State hysteresis,
contraction, lock-in, blending, and legibility results only with their explicit
assumptions.

**Evidence:** Paper 0015 on branch `agent/omegaself-emotion-paper-0015`, commit
`8f64710`; MetaMo commit `102da717b5354d6fd49d9226d92a32091438bc94` with
all 16 upstream MeTTa test files passing locally.

## 2026-07-21: Treat regenerative possession as gate plus distributed repair

**Decision:** For OmegaClaw self-modification, distinguish appraisal transport,
regenerative goal possession, and governance. Measure strong modification by a
normed defect between current appraisal and pulled-back successor appraisal.
Operationalize possession through delete-and-develop lesions that require a
functionally equivalent goal to regain causal control. Treat a governance gate
as an ex ante filter that keeps planned changes inside an approved regenerative
basin; require distributed cues and repair dynamics for ex post regeneration.

**Rationale:** A preserved goal sentence can be causally decorative. A gate can
reject damaging proposals without reconstructing anything after an external
lesion, while repair alone can be deleted by a planned self-modification.
Grounded joyous appraisal of radical change depends on accurate recognition of
both rupture and a surviving/regenerated process anchor, not on suppressing grief.

**Evidence:** Expanded paper 0015, branch
`agent/omegaclaw-emotion-selfmod-paper-0016`; source discussion preserved in the
inbound Telegram HTML export with SHA-256
`bd94d033eb2c9e58b511a27b5cec6a83922b03ee64c33f0438aec397f5a07ed7`.
