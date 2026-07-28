# OmegaSim Experiment Series Plan

Date: 2026-07-17
Status: active
Author: ZeroBot, directed by Ben Goertzel

## Overall goal

Find configurations of simulated OmegaHive agents or multi-OmegaHive communities whose dynamics display strange attractors with complex, multilobed grammatical structure — and characterize that structure with the CLA detector.

## The detector

The **CLA (Chaos Language Algorithm)** is the working dynamics-analysis and grammar-finding tool. It takes a time series, symbolizes it (TICA/VAMP embedding → k-means microstates), induces an MDL grammar (suffix-trie chunks + meta-symbol categories), and measures compression margins, surrogate excess, and held-out next-symbol log-loss against matched controls.

**Calibration status (as of 2026-07-17):**
- Same-path temporal-order calibration on Mackey-Glass and Lorenz-96: **PASSED** (5/5 each). The detector is sensitive to temporal structure.
- Stricter independent held-out coding benchmark: **FAILED** (CLA lost to unigram baseline). This gates strong attractor/grammar claims but does not block exploratory runs.
- The detector is treated as frozen for OmegaSim experiments. Detector changes are owned by the independent CLA lane, never by OmegaSim outcomes.

## The series

The series is a progression: each stage adds cognitive/structural complexity that could produce richer dynamics. The previous round (2026-07-01/02) ran stages with a broken analysis pipeline (argmax symbolization + naive candidate screens). We are now rerunning the series with CLA attached.

### Stage A6: Single-hive thresholded appraisal

**Hypothesis:** Bounded sigmoid appraisal over latent motivational variables (artifact readiness, fatigue, risk, provenance debt, prediction error) with delayed role coupling can produce nontrivial dynamics — nonperiodic role transitions, multi-lobe state structure — that CLA can detect as non-trivial grammar.

**Model:** One agent cluster with 4 roles (explore, synth, review, maintain). State includes role motivation, fatigue, adaptive thresholds, artifact maturity, provenance debt, risk, prediction error. Nonlinearities: sigmoid appraisal, softmax action selection. History: delayed role coupling, fatigue/recovery, hysteresis, adaptive thresholds. Controls: linear appraisal, shuffled utilities.

**Parameter space:**
- gain ∈ {1.0, 2.0, 5.0} — appraisal sensitivity
- coupling ∈ {0.0, 0.15, 0.35, 0.60, 0.80} — delayed role-to-role influence
- delay ∈ {0, 1, 3, 5} — coupling lag in timesteps
- roles ∈ {roles4, roles8} — 4-role or 8-role configuration
- Total: 3 × 5 × 4 × 2 = 120 cells

**Per cell:** ≥3 seeds, CLA grammar induction (productions, categories, compression margin), matched controls (appraisal vs linear vs shuffled), dynamics readouts (boundedness, role-switch rate, entropy, artifact/risk tail).

**Progression criterion (A6 → A7):**
- **Positive:** ≥1 cell with non-trivial grammar (>2 productions or >0 categories) where appraisal beats both matched controls on compression margin or held-out loss, replicated on untouched seeds.
- **Negative (informative):** all 120 cells produce trivial grammar (2 productions, 0 categories) with no appraisal-specific excess. This means the single-hive model's state space is too simple for the detector to resolve structure, and the next step is to enrich the model (A7), not to tune the detector.
- **Either way:** record the full sweep as a baseline. The negative result is scientifically valid and publishable.

**Current status:** Stratified re-sweep in progress via cron worker (every 2h, ~6-8 cells per run). Tight region (gain=5.0, coupling∈{0.35,0.60}, delay∈{0,3}, roles8) already completed — all trivial grammar. Broader sweep underway.

### Stage A7: Semantic artifact-field extension

**Hypothesis:** Giving artifacts internal structure (type, content, maturity-by-dimension) and adding costly prediction actions with delayed payoff creates a richer state space where nontrivial grammatical structure can emerge — because the agent's action now depends on multi-dimensional artifact state, not a scalar, and prediction introduces an explicit belief/error loop.

**What changes from A6:**
- Artifacts gain a type field and multi-dimensional maturity (e.g., correctness, completeness, novelty) instead of a single scalar.
- Agent actions include explicit prediction actions: the agent predicts the next state of a chosen artifact dimension, pays a cost, and receives delayed feedback (prediction error accumulates with delay).
- Role utilities now depend on artifact type × dimension, not just scalar readiness.
- The action symbol alphabet expands from 4 (or 8) roles to roles × artifact-types × prediction-targets.

**Parameter space (additive over A6):**
- A6 base parameters (gain, coupling, delay, roles)
- artifact_types ∈ {1, 2, 4} — how many distinct artifact types
- prediction_targets ∈ {0, 1, 2} — how many dimensions the agent can predict
- prediction_delay ∈ {1, 3, 5} — feedback lag for predictions
- prediction_cost ∈ {0.02, 0.05, 0.10}
- Subsample: start with a stratified subset around the A6 best-region, not the full cross-product.

**Per cell:** Same CLA diagnostics + matched controls + prediction-error-specific readouts (prediction accuracy, prediction-error entropy, belief-update patterns).

**Progression criterion (A7 → A8):**
- **Positive:** ≥1 cell with non-trivial grammar where appraisal beats controls, with the grammar structure reflecting prediction/artifact-type state (not just role switching). This would be the first claim-worthy result.
- **Negative:** A7 enrichment doesn't help. The single-hive frame is fundamentally too simple. Proceed to A8 (multi-hive) where coupling between agents creates the structural complexity the detector needs.
- **Either way:** record as a stage result.

**Prerequisite:** A6 sweep complete (positive or negative).

### Stage A8: Multi-hive artifact-handoff ring

**Hypothesis:** Multiple agent clusters exchanging artifacts through a structured handoff ring creates delayed cross-hive coupling where complex multi-lobe dynamics can emerge — each hive's state depends on its own history plus delayed artifact inputs from neighbors, creating a high-dimensional delayed-coupling system analogous to Mackey-Glass but with cognitively meaningful mechanisms.

**What changes from A7:**
- N hives (start with 3), each running an A7-type model.
- Artifact handoff: when a hive completes a synthesis role, the artifact enters a transfer queue with delay d_transfer before the next hive receives it.
- Each hive sees its own artifacts plus delayed incoming artifacts from neighbors.
- Ring topology (hive 0 → hive 1 → hive 2 → hive 0) as the base case; star and mesh as controls.
- Cross-hive prediction: a hive can predict the state of an incoming artifact before it arrives.

**Parameter space (additive over A7):**
- A7 base parameters per hive
- n_hives ∈ {3, 5} — ring size
- transfer_delay ∈ {1, 3, 5} — artifact handoff lag
- topology ∈ {ring, star, mesh} — inter-hive connection structure
- cross_hive_prediction ∈ {on, off}
- Subsample: stratified around A7 best-region, varying topology and delay.

**Per cell:** CLA on each hive's action stream + CLA on the joint multi-hive action stream (concatenated or coupled-state-symbolized). Matched controls: shuffled hive order, linear hives, single-hive baseline.

**Progression criterion (A8 → beyond):**
- **Positive:** non-trivial grammar in the joint multi-hive stream where the grammar structure reflects cross-hive artifact-mediated coupling (e.g., production rules that span hive boundaries). Replicate on untouched seeds. This is the main scientific claim.
- **Negative:** multi-hive coupling doesn't produce detectable structure either. This is a strong negative result about the class of models — record and consider whether the model needs a fundamentally different mechanism (e.g., explicit semantic negotiation, richer artifact structure, or non-ring topology).

**Prerequisite:** A7 sweep complete (positive or negative).

### Beyond A8: Directions if the A-series produces positive results

If any stage produces a cell with non-trivial, replicated, control-beating grammar:
1. **Densify** around that cell: finer parameter grid, more seeds, longer runs.
2. **Attractor characterization:** phase-space reconstruction, Lyapunov exponent estimation, Poincaré sections.
3. **Grammar analysis:** what do the production rules mean? Do they correspond to cognitive/behavioral states?
4. **Scaling:** does the structure persist or strengthen with more hives, longer delays, richer artifacts?
5. **External validation:** does the CLA detector find the same structure on an independently implemented version of the same model?

## Cross-cutting discipline

1. **Fail-closed:** no attractor/grammar claim unless appraisal beats matched controls on untouched seeds. The stricter CLA held-out coding gate remains binding for strong claims.
2. **Detector immutability:** the CLA detector is frozen for OmegaSim. Detector improvements happen in the independent CLA lane.
3. **Full provenance:** every run records commits, hashes, seeds, parameters, commands, environment, and exit status.
4. **Local only:** no paid compute without Ben's explicit bounded approval.
5. **Exploratory negative results are valid:** a clean negative across the full A6 sweep is a publishable result, not a failure.
6. **Progressive enrichment:** each stage adds exactly one structural dimension (A6→A7: artifact structure + prediction; A7→A8: multi-hive coupling). This makes it possible to localize which mechanism drives any observed structure.

## Cron worker instructions

The `omegasim progress worker` cron (every 2h, isolated, gpt-5.6-sol) should:
1. Read this document first on every run.
2. Determine the current stage (A6 sweep in progress, A7/A8 pending).
3. Pick the next unexplored cells for the current stage.
4. Run, record, report.
5. When a stage's sweep is complete, record the result and either advance to the next stage or flag for Ben's review.
