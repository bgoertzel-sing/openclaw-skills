# Tasks

## Active

- [ ] Add a persistent CLA formalization thread: study CLA-recognized emergent grammars via Hyperseed, language, emergent pattern, McBride derivatives, and pattern calculus; connect this to OmegaSim detector needs and Ben's linked `Weakness-Theory-10.pdf` sections on emergent pattern and pattern calculus.
- [ ] Draft a Hyperseed formalization note tentatively titled `SLT-Guided Residual Seeds`, using `library/slt-residual-layers/` and `library/slt-hyperseed-synthesis/` as sources; connect weakness-as-evidence, LLC/additivity deviation, refinement DAGs, causal fingerprints, transformer residual layers, and AGI adaptation.
- [ ] ProtomegaTron medium-term background task: formalize Ben's Substack posts (`https://bengoertzel.substack.com/`) in reverse chronological order, article by article, section by section, with each significant intellectual point represented via Hyperseed concepts in informal explanations plus formal mathematical formulations. Store results in GitHub under one subfolder per article, with import-friendly structure for later AtomSpace/PLN/semantic-chemistry use. Pause for urgent tasks, then resume relentlessly. Started with `substack/2026-06-26-tag-youre-not-it/`.
- [ ] Formalize the first `petta-chem` experiment records using the Hyperseed scientific-experiment annotation style.
- [ ] Formalize the OmegaClaw Telegram smoke test and idle-loop issue as agent-experience/research-event examples.
- [ ] Revise/extend note 0004 with the 2026-07-01 OmegaSim feedback: treat logistic response as bounded thresholded cognitive appraisal rather than arbitrary chaos injection; add latent motivational state, semantic/artifact fields, costly prediction, hysteresis/adaptive thresholds, residual-state lobe discovery, amplitude-matched linear controls, and A6/A7/A8 experiment families.
- [ ] Use revised note 0004 to drive a first OmegaSim phase-diagram experiment: lifted delayed state, boundedness gate, and sweeps over gain/delay/memory/leakage/noise ratios plus the new thresholded artifact-lifecycle/semantic-field variables. Initial A6 simulation scaffold and smoke runs now exist under `experiments/omegasim-a6/`; next step is longer controlled sweeps and shuffled/linearized controls.
- [ ] Encode one Telegram fresh-message episode and one idle/no-input episode using the new schema.
- [ ] Prototype `medium_memory.py` / `medium_memory.metta` append and bounded query functions in a local OmegaClaw experiment or branch.
- [ ] Keep the medium-memory schema PLN-ready: stable predicates, explicit truth values for interpretive claims, provenance links, and a later PLN inference test over loaded memory atoms.
- [ ] Decide how much MeTTa syntax should accompany each LaTeX formalization.
- [x] For the Substack background task, define the per-article folder/template: source metadata, retrieval date, outline, Hyperseed informal mapping, formal math mapping, candidate AtomSpace/PLN atoms, open questions. Initial template used in `substack/2026-06-26-tag-youre-not-it/`.

## Done

- [x] Create public GitHub repository `bgoertzel-sing/hyperseed-formalizations`.
- [x] Seed initial LaTeX/PDF orientation scaffold.
- [x] Preserve initial Hyperseed source bundle in `library/hyperseed-v2/`.
- [x] Draft a first declarative Hyperseed formalization of ProtomegaTron's own OmegaClaw design and dynamics in `papers/0002-protomegatron-agent-loop/protomegatron_agent_loop.tex`.
- [x] Write an ASCII-only LaTeX detailed design and implementation plan for medium-scale PeTTa memory in `papers/0003-medium-petta-memory-plan/medium_petta_memory_plan.tex`.
- [x] Draft note 0004, `OmegaSim/OmegaHive Strange-Attractor Tuning`, with S1-S4 formalization, theorems/proofs, OmegaHive1 specialization, and OmegaSim implementation guidance.
- [x] Install/configure a real LaTeX build path via local `tectonic`; `scripts/build.sh` now compiles the repository PDFs.
- [x] Draft note 0006, `Plain=>MeTTa/PeTTa and Rholang: Typed Atomspace Spec IR`, with ASCII LaTeX source and compiled PDF.
- [ ] Add a first substantive formalization note for ProtomegaTron prompt customization and the stale-update smoke-test observation.
