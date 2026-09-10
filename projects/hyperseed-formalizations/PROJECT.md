# hyperseed-formalizations

## Purpose

Public repository and project notebook for Hyperseed-oriented formalizations arising from Ben Goertzel's interactions with OmegaClaw/ProtomegaTron, ZeroBot/OpenClaw, and related research experiments.

## Repository

- GitHub: https://github.com/bgoertzel-sing/hyperseed-formalizations
- Local clone: `projects/hyperseed-formalizations/repos/hyperseed-formalizations`
- Visibility: public

## Source library

- Initial Hyperseed v2 bundle: `library/hyperseed-v2/SOURCE.md`
- Preserved sources include the Hyperseed v2 Substack article, Hyperseed-1 article, and four linked PDFs, including the 1454-page Hyperseed ontology book.

## Current status

- 2026-06-27: Ben assigned ProtomegaTron a medium-term background task to formalize all posts from `https://bengoertzel.substack.com/` in reverse chronological order using Hyperseed informal explanations plus formal mathematical formulations, one GitHub subfolder per article, with later AtomSpace/PLN/semantic-chemistry import in mind. This is now tracked as a standing active task.
- Created 2026-06-27 after Ben approved the name `hyperseed-formalizations` and public GitHub repository direction.
- Initial repo scaffold contains LaTeX source and a generated PDF preview for orientation note 0001.
- Added note 0002, `ProtomegaTron as a Hyperseed-Scrutable Agent Loop`, as the first declarative code/design/dynamics formalization. It defines ProtomegaTron process state, the OmegaClaw turn transition, agency boundaries, three self-levels, and a proposed medium-scale PeTTa memory layer. Local/pushed branch: `agent/protomegatron-formalization-0002`, commit `33ed525`.
- Added ASCII-only note 0003, `Medium-Scale PeTTa Memory for ProtomegaTron`, with detailed design, atom schema, file layout, API design, prompt integration, validation plan, risks, and step-by-step implementation milestones. Updated revision now treats PLN-readiness as a design constraint and adds explicit `MemoryCluster` envelopes, epistemic role separation, append-only status/truth-value events, canonical/index/prompt/PLN views, and PLN validation criteria. Latest pushed branch `agent/protomegatron-formalization-0002`, commit `bfab423`.
- Added note 0004, `OmegaSim/OmegaHive Strange-Attractor Tuning: A Hyperseed-Dynamical Formalization`, in `papers/0004-omegasim-strange-attractor-tuning/`. It formalizes delayed hive dynamics, dimensionless control ratios, proved gates for well-posedness/boundedness/contraction/delay instability, an OmegaHive1 specialization, and concrete OmegaSim simulation instructions.
- Added note 0006, `From ***plain Specifications to MeTTa/PeTTa and Rholang: A Typed Atomspace IR Proposal`, in `papers/0006-plain-metta-rholang-spec-ir/`. It reviews Ben's 2026-06-29 Plain=>MeTTa/Rholang discussion, recommends an Atomspace-style typed logical Spec IR, and outlines MVPs for PeTTa/MeTTa, Rholang, and later PLN analysis.
- Local TeX builds now work through the locally installed `tectonic` binary; PDFs can be generated with `scripts/build.sh`.
- Revised note 0013 on 2026-07-15 after architectural review: Python is now specified as a narrow authenticated-I/O, deterministic-encoding/hash, durable-append, and OS-observation adapter; typed normalization, identity/provenance semantics, evidence admission, belief views, governance, and legal transitions remain in MeTTa/PeTTa. The capability-learning pattern now uses Patham9 PLN behind an OmegaPLN-compatible adapter instead of ingesting NACE/NAL machinery.
- Expanded paper 0015 on 2026-07-21 into the 23-page essay `Emotion at the Edge of Self: OmegaClaw Affect, Radical Self-Modification, and Regenerative Goals`. It integrates the Bot Philosophy discussion's OmegaSelf/ECAN emotion architecture, appraisal noncommutation, somber versus joyous-bittersweet self-transformation, regenerative goal possession, meta-anchors, Hyperseed interpretation, qualified results, and practical gate-plus-repair tests. Branch: `agent/omegaclaw-emotion-selfmod-paper-0016`.
- Added paper 0014 on 2026-07-23, `Causal Fibres as an Evidence-Gated
  Hypothesis Ladder`, formalizing H0--H6, teacher-gap and representation gates,
  deployment-honest settlement, the amortization gap, and Hyperseed
  evidence-registration/conservativity/pluralism connections. The nine-page
  PDF passed repository-wide Tectonic compilation and complete visual
  inspection. Local branch `agent/cf-hypothesis-ladder-formalization`, commit
  `e93983a`; not pushed.

## Working conventions

- Use LaTeX source under `papers/` for definitions, conjectures, theorems, proof sketches, and explanatory notes.
- Keep browser-viewable PDFs next to source files.
- Preserve provenance back to conversations, experiments, commits, papers, and source library records.
- Distinguish definitions, examples, conjectures, theorem statements, proof sketches, speculative analogies, and open questions.
