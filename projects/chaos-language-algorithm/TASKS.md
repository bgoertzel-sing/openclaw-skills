# Tasks

## Next

- [x] Create a local prototype repo under `projects/chaos-language-algorithm/repos/chaoslang` using package name `chaoslang`.
- [ ] Keep a persistent CLA/Hyperseed/pattern-calculus subthread: analyze CLA-recognized emergent grammars in terms of language, emergent pattern, McBride derivatives, and pattern calculus; use Ben's linked `Weakness-Theory-10.pdf` Google Drive source as a study input when accessible.
- [x] Implement domain core first: immutable typed IDs, tokens, corpus, grammar, categories, state, edits, proposals, scores.
- [x] Implement symbolic-string MVP before trajectory symbolization: `CLA.simple().fit_symbols(...)`, NGramPatternMiner, chunk rewriting, approximate MDL, greedy induction loop.
- [x] Implement M1 symbolization for fixed partitions with deterministic tests after the string MVP is stable. Added stdlib-only fixed rectangular M1 symbolization plus Lorenz-63/Rössler controls in `repos/chaoslang` on 2026-07-04.
- [x] Implement M2 chunk-only grammar: n-gram proposals, non-overlapping replacement, rule expansion, use counts, dead-rule pruning.
- [x] Implement M3 MDL scoring and reject overhead-dominated edits.
- [x] Implement M4 hard category induction with context histograms, deterministic hard clusters, `M[v]` parse entries, and exact reconstruction. JS divergence remains deferred.
- [x] Implement M5 unified greedy search choosing the best negative delta-L edit.
- [ ] Add persistence/reproducibility: JSON grammar/state format, edit-log replay, deterministic seeds, stable text rendering.
- [x] Add backend-neutral fact layer (`Fact`, `FactStore`, `MemoryFactStore`) as Hyperon migration seam, with state/fact round-trip for core fields.
- [x] Defer optional Hyperon adapter until pure-Python invariants and fact projection round-trip tests pass.

## Acceptance tests from the spec

- [x] Exact expansion after every accepted edit returns `S0`.
- [x] Chunk identity: `A -> abc` expands only to `abc`.
- [x] Category identity: `M={x,y}` expands to exactly the chosen member per occurrence, not `xy`/`yx`.
- [x] Frame generalization proposes `{x,y}` from `a x b / a y b / a x b` when MDL supports it.
- [x] MDL rejection rejects unrelated rare-symbol categories.
- [x] Rule pruning inlines/removes chunk rules whose use count drops below two.
- [x] Determinism with same seed and input.

## McBride / quantale / pattern-intensity engineering items

Based on the formal analysis in `docs/mcbride_cla_analysis.tex` (and compiled `.pdf`), bridging McBride derivatives, quantale structure, and pattern calculus to CLA implementation. The analysis document presents Theorems 1-2, Propositions 1-3, Definitions 1-3, and Conjectures 1-2 with proofs and practical implications.

### Implementation (near-term)

- [ ] **M-MD1: McBride derivative pre-ranking.** Compute cheap McBride-derivative proxies (block-frequency x length product for chunks; context-similarity x group-size for categories) for all candidates first, then only run full MDL evaluation on the top-k. Target: cut wasted MDL computations on long streams without losing the best edit. Requires an `approximate_delta` method on `TwoPartMDLScorer` that estimates -dL without full grammar re-encoding. (Theorem 1, Corollary 1 in the analysis.)
- [ ] **M-MD2: Emergent synergy detection for joint proposals.** Before greedy commit, check whether any pending chunk edit q_c and category edit q_m satisfy sigma_{y,z}(m) > e (joint MDL improvement exceeds sum of individual improvements). If so, propose as a joint move. Addresses the greedy-CLA failure mode where intermediate states show no improvement but pairs do. Start with the axb/ayb/axb pattern as a unit test. (Proposition 1, Conjecture 1 in the analysis.)
- [ ] **M-MD3: Log per-iteration MDL trajectory** (~10 lines). Append `L(t)` after each iteration in the greedy loop; gives convergence/oscillation diagnostics. Detect oscillation (edit accepted then reversed next round) -> widen beam or keep multiple grammar candidates alive (damping). Uses the delay-logistic ODE analogy from WT sec22.6 as a guide for when to expect instability vs convergence. (Proposition 2, Corollary 2 in the analysis.)
- [ ] **M-MD4: Log pattern intensities for accepted categories.** Compute I_{y,z}(m) = sigma - e alongside the existing JS-divergence in `ContextCategoryInducer`; compare rankings to validate whether intensity is a better proposal filter. (Definition 3 in the analysis.)
- [ ] Wire JS-divergence context clustering into category proposal generation (currently a seam only; needed for M-MD2 synergy detection on real data).

### Research (longer-term)

- [ ] **M-MD5: Quantale choice as domain-tunable knob.** Abstract scoring behind a `Quantale` protocol with `combine` and `aggregate`; provide `AdditiveQuantale` (current MDL) and `ProbabilityQuantale` implementations; run comparative benchmarks on logistic-map vs Lorenz trajectories. (Proposition 3 in the analysis.)
- [ ] **M-MD6: Natural-gradient edit search.** Replace uniform beam search with Fisher-metric-aware ranking that accounts for redundant edit directions (e.g., overlapping chunk proposals). Prototype after M-MD1-M-MD4 are validated.
- [ ] **M-MD7: Pattern-intensity ODE convergence criterion.** Use the quantale ODE relaxation to derive a principled stopping criterion for the greedy loop based on pattern-intensity decay rate rather than a fixed iteration budget.

## High-dimensional embedding / adaptive symbolization sprint

Based on Ben's 2026-07-10 design note `library/chaos-language-algorithm/cla_hd_embedding_extracted.txt`. This supersedes interpreting raw fixed-grid M1 high-D failures as evidence about CLA itself.

- [x] Add Phase-0 baseline MDL-to-bits calibration hook so results are comparable against shuffled surrogates. Implemented in `chaoslang.evaluation` as empirical iid baseline minus current two-part scorer; still not final CLA grammar likelihood.
- [x] Add a surrogate-shuffle harness: preserve marginal symbol frequencies, destroy temporal grammar, rerun CLA, and report `Delta_grammar = gain(real) - gain(shuffled)`.
- [x] Add held-out next-symbol log-loss / perplexity evaluation. Current implementation is a smoothed n-gram baseline diagnostic, not a CLA grammar predictive likelihood.
- [x] Add an adaptive low-cardinality symbolizer (initially k-means microstates with chosen `k`) alongside fixed rectangular M1.
- [x] Add an intrinsic-attractor-dimension diagnostic (spectral participation ratio / variance threshold) before choosing embedding dimension `d`; correlation dimension remains future work.
- [x] Implement a pure-Python Phase-0 TICA/VAMP-style kinetic-map embedding with shrinkage-regularized covariances; lagged covariance is not symmetrized, and singular values are clipped to [0,1] to avoid high-D rank-deficient whitening artifacts. Production-scale D≈200–300 should use a tested backend such as `deeptime`.
- [ ] Add PCCA+ soft-membership category seeding for CLA meta-symbol proposals after the microstate path is working.
- [x] Run the first bounded Phase-1 ground-truth test: Lorenz-63 lifted into R256 with small noise -> intrinsic dimension -> dependency-free kinetic map (`d=3`) -> k-means microstates -> CLA -> shuffled and held-out diagnostics, with matched raw-M1. Adaptive real-minus-shuffled proxy was 39.33 bits versus 2.10 for M1; n-gram perplexity 3.42 versus 433.18. This is one-seed diagnostic evidence, not calibrated MDL/CLA likelihood or proof of grammar preservation. See `experiments/20260712T200000Z-lorenz63-lift256-phase1/RUN.md`.
- [x] Run a preregistered multi-seed `d`/`k`/lag sweep over lifted Lorenz-63 R256 using deeptime VAMP, matched direct/raw k-means, raw compound M1, and dependency-free controls. All 36 deeptime settings had positive real-minus-shuffled proxy, but direct xyz k-means and the pure reference were as good or better; no categories emerged and near-unit singular values remain cautionary. See `experiments/20260712T200200Z-lorenz63-r256-deeptime-multiseed/RUN.md`.
- [ ] Extend rate-distortion validation with longer trajectories, lag selection from implied-timescale stability, temporal-block surrogates, and calibrated CLA predictive/MDL coding before OmegaSim-scale traces.

## Attractor benchmark sprint

- [ ] Implement dependency-light trajectory generators/symbolizers for logistic map, Lorenz-63, Rössler, Mackey-Glass, and Lorenz-96. Logistic/equal-width smoke plus deterministic Lorenz-63 and Rössler RK4 controls with M1 fixed-partition tests are in place; Mackey-Glass and Lorenz-96 remain.
- [ ] Run CLA on a small variety of strange attractors and non-chaotic controls with recorded seeds/parameters. A small command exists (`python3 -m chaoslang.benchmarks.m1_controls`) for Lorenz-63/Rössler JSON summaries; no experiment record has been created yet.
- [ ] Include benchmark dimensions up to the vector dimensionality relevant to OmegaSim starter traces.
- [ ] Defer much higher-dimensional traces until a dedicated dimension-reduction step exists.
- [ ] Record each benchmark run under `experiments/` with parameters, exact command, outputs, and conclusion.

## Scaling / reviewer follow-up

- [x] Replace the brute-force n-gram window counter with a bounded suffix-trie-backed miner for high-cardinality compound-symbol streams; regression tests cover compound symbols and a high-cardinality repeated motif. Implemented on `agent/suffix-trie-miner` in `repos/chaoslang`.
- [x] Add/update the CLA expert-review prompt to ask explicitly for algorithmic/data-structure inefficiencies: n-gram brute force, context histogram duplication, compound-symbol storage/copying, repeated MDL re-encoding, and suitable trie/index/hash/sparse alternatives. See `docs/cla_expert_review_prompt.md`.
- [ ] Benchmark the bounded suffix-trie miner on real 1024-step × ~20D CLA streams after the JS/dimension-reduction symbolization path is available; compare wall time and peak memory against the old brute-force miner if preserved in a fixture.
  - 2026-07-09 local first slice: ran Lorenz-96 control at 1024 steps × 20D with `--miner suffix_trie --category-method js`; exact reconstruction true, 510 unique symbols, 8 chunk rules, score_total 1021.2, fit_wall_time_seconds ~2.55. Evidence: `experiments/20260709T192728Z-lorenz96-1024-dim20-suffix-trie/RUN.md`. Still needs real OmegaSim stream/dim-reduction path, peak-memory capture, and true brute-force comparison fixture.
