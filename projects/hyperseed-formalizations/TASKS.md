# Tasks

## Active

- [x] Create paper 0014, `Causal Fibres as an Evidence-Gated Hypothesis
  Ladder`, on branch `agent/cf-hypothesis-ladder-formalization`. Acceptance:
  formalize H0--H6, the quantitative kill gates, five representation classes,
  teacher-gap closure and factor-specific counterfactual edits, the Hyperseed
  evidence/registration/conservativity/pluralism mapping, and proof sketches
  for the R9, amortization-gap, and orthogonal-fibre limitations; compile with
  Tectonic, inspect the PDF, and commit locally without pushing. Next command:
  inspect the causal-fibres release reports and papers 0009--0013 for source
  claims and house style. Completed 2026-07-23: nine-page source/PDF compiled
  individually and through the repository-wide build; all pages were visually
  inspected; text extraction and `git diff --check` passed; no remote push.
  Evidence: branch `agent/cf-hypothesis-ladder-formalization`, commit
  `e93983a`, path
  `repos/hyperseed-formalizations/papers/0014-causal-fibres-hypothesis-ladder/`.

- [x] Expand paper 0015 into `Emotion at the Edge of Self: OmegaClaw Affect,
  Radical Self-Modification, and Regenerative Goals`, as ASCII-safe LaTeX
  plus compiled PDF. Acceptance: integrate the 2026-07-19--21 Bot Philosophy
  contributions from Ben, Zar, Godel, Protomegabot, and Protocosmobot into a
  coherent essay covering OmegaSelf/ECAN emotion regimes, appraisal
  noncommutation and strong self-modification, somber versus joyous-bittersweet
  phenomenology, regenerative goal possession and meta-anchors, Hyperseed
  interpretation, corrected mathematical results, and practical OmegaClaw
  architecture/tests; preserve source provenance and epistemic status; compile
  successfully and visually inspect every page. Completed 2026-07-21: the
  ASCII-safe source compiles to a 23-page PDF; all pages were visually
  inspected. The existing paper 0015 was expanded because its first half is the
  canonical corrected foundation for the requested synthesis. Evidence: branch
  `agent/omegaclaw-emotion-selfmod-paper-0016`; paper path
  `worktrees/omegaclaw-emotion-selfmod-paper-0016/papers/0015-omegaself-emotion-regimes/`.

- [x] Write paper 0015, `OmegaSelf-Compatible Emotion: From Psi Modulation to
  Auditable Cognitive Regimes`, as ASCII-safe LaTeX plus compiled PDF.
  Acceptance: synthesize the Bot Philosophy discussion, OmegaSelf,
  Hyperseed regime formalization, Bach's Psi/MicroPsi tutorial, relevant
  psychological theories, corrected theorem statements/proofs, OmegaClaw
  MetaMo/OpenPsi architecture, safety constraints, and falsifiable rollout
  experiments; compile successfully, visually inspect every PDF page, and
  commit the coherent artifact on an isolated branch. Completed 2026-07-19:
  16-page ASCII-safe LaTeX and PDF compiled with Tectonic; all pages visually
  inspected; pinned MetaMo baseline passed all 16 upstream MeTTa test files.
  Evidence: branch `agent/omegaself-emotion-paper-0015`, commit `8f64710`,
  worktree `worktrees/omegaself-emotion-paper-0015/`, paper path
  `papers/0015-omegaself-emotion-regimes/`.

- [x] ThreadKeeper hyperseed-formalizations worker: config drafted and first bounded queue-only run completed for `note-0004-revision` on 2026-07-09. Worker used GLM-5.2 route via OpenClaw, committed local revision `06b10e4`, and stopped after one task. Next: continue queue with `note-slt-residual-seeds` only after reviewing note 0004 and confirming worker policy.
- [x] Proximal CLA theory interpretation task: explore connections between CLA and the McBride-derivative-based pattern calculus in `library/weakness-theory-10/`, especially chapters 21-22. Formalized as paper 0007 (`papers/0007-cla-mcbride-derivative-bridge/`), committed `9b1228b`, pushed to `agent/protomegatron-formalization-0002`. Covers: CLA grammar as quantale predicate, chunk edits as McBride one-hole contexts, category edits as quantale patterns, emergent synergy in nested grammars, McBride derivative as CLA proposal ranking, dynamical pattern-intensity ODEs over grammar trajectories, Hyperseed interpretation. Next: instrument chaoslang prototype to test emergent synergy conjecture empirically.
- [ ] Draft a Hyperseed formalization note tentatively titled `SLT-Guided Residual Seeds`, using `library/slt-residual-layers/` and `library/slt-hyperseed-synthesis/` as sources; connect weakness-as-evidence, LLC/additivity deviation, refinement DAGs, causal fingerprints, transformer residual layers, and AGI adaptation.
- [ ] ProtomegaTron medium-term background task: formalize Ben's Substack posts (`https://bengoertzel.substack.com/`) in reverse chronological order, article by article, section by section, with each significant intellectual point represented via Hyperseed concepts in informal explanations plus formal mathematical formulations. Store results in GitHub under one subfolder per article, with import-friendly structure for later AtomSpace/PLN/semantic-chemistry use. Pause for urgent tasks, then resume relentlessly. Started with `substack/2026-06-26-tag-youre-not-it/`.
- [ ] Formalize the first `petta-chem` experiment records using the Hyperseed scientific-experiment annotation style.
- [ ] Formalize the OmegaClaw Telegram smoke test and idle-loop issue as agent-experience/research-event examples.
- [x] Revise/extend note 0004 with the 2026-07-01 OmegaSim feedback: treat logistic response as bounded thresholded cognitive appraisal rather than arbitrary chaos injection; add latent motivational state, semantic/artifact fields, costly prediction, hysteresis/adaptive thresholds, residual-state lobe discovery, amplitude-matched linear controls, and A6/A7/A8 experiment families. First worker commit `06b10e4`; follow-up local correction pass weakens overstrong propositions and fixes the sigmoid derivative/amplitude statement.
- [ ] Use revised note 0004 to drive a first OmegaSim phase-diagram experiment: lifted delayed state, boundedness gate, and sweeps over gain/delay/memory/leakage/noise ratios plus the new thresholded artifact-lifecycle/semantic-field variables. Initial A6 simulation scaffold and smoke runs now exist under `experiments/omegasim-a6/`; next step is longer controlled sweeps and shuffled/linearized controls.
- [ ] Encode one Telegram fresh-message episode and one idle/no-input episode using the new schema.
- [ ] Prototype `medium_memory.py` / `medium_memory.metta` append and bounded query functions in a local OmegaClaw experiment or branch.
- [ ] Keep the medium-memory schema PLN-ready: stable predicates, explicit truth values for interpretive claims, provenance links, and a later PLN inference test over loaded memory atoms.
- [ ] Decide how much MeTTa syntax should accompany each LaTeX formalization.
- [x] For the Substack background task, define the per-article folder/template: source metadata, retrieval date, outline, Hyperseed informal mapping, formal math mapping, candidate AtomSpace/PLN atoms, open questions. Initial template used in `substack/2026-06-26-tag-youre-not-it/`.

## Done

- [x] Revise note 0013, `ClarityOmega: Critical Architecture Review and Ingestion Guide for OmegaClaw`, to specify a narrow typed Python effects boundary, MeTTa-native semantic normalization/governance, Patham9 PLN capability inference, immutable contextual evidence, separate dispatch policy, and an OmegaPLN migration seam. Rebuilt and visually checked the 16-page PDF on 2026-07-15.
- [x] Create public GitHub repository `bgoertzel-sing/hyperseed-formalizations`.
- [x] Seed initial LaTeX/PDF orientation scaffold.
- [x] Preserve initial Hyperseed source bundle in `library/hyperseed-v2/`.
- [x] Draft a first declarative Hyperseed formalization of ProtomegaTron's own OmegaClaw design and dynamics in `papers/0002-protomegatron-agent-loop/protomegatron_agent_loop.tex`.
- [x] Write an ASCII-only LaTeX detailed design and implementation plan for medium-scale PeTTa memory in `papers/0003-medium-petta-memory-plan/medium_petta_memory_plan.tex`.
- [x] Draft note 0004, `OmegaSim/OmegaHive Strange-Attractor Tuning`, with S1-S4 formalization, theorems/proofs, OmegaHive1 specialization, and OmegaSim implementation guidance.
- [x] Install/configure a real LaTeX build path via local `tectonic`; `scripts/build.sh` now compiles the repository PDFs.
- [x] Draft note 0006, `Plain=>MeTTa/PeTTa and Rholang: Typed Atomspace Spec IR`, with ASCII LaTeX source and compiled PDF.
- [ ] Add a first substantive formalization note for ProtomegaTron prompt customization and the stale-update smoke-test observation.
