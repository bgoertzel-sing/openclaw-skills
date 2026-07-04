# Tasks

## Next

- [x] Create a local prototype repo under `projects/chaos-language-algorithm/repos/chaoslang` using package name `chaoslang`.
- [ ] Keep a persistent CLA/Hyperseed/pattern-calculus subthread: analyze CLA-recognized emergent grammars in terms of language, emergent pattern, McBride derivatives, and pattern calculus; use Ben's linked `Weakness-Theory-10.pdf` Google Drive source as a study input when accessible.
- [x] Implement domain core first: immutable typed IDs, tokens, corpus, grammar, categories, state, edits, proposals, scores.
- [x] Implement symbolic-string MVP before trajectory symbolization: `CLA.simple().fit_symbols(...)`, NGramPatternMiner, chunk rewriting, approximate MDL, greedy induction loop.
- [ ] Implement M1 symbolization for fixed partitions with deterministic tests after the string MVP is stable.
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


## Attractor benchmark sprint

- [ ] Implement dependency-light trajectory generators/symbolizers for logistic map, Lorenz-63, Rössler, Mackey-Glass, and Lorenz-96. Sprint 1 includes only a logistic-map/equal-width symbolization smoke scaffold.
- [ ] Run CLA on a small variety of strange attractors and non-chaotic controls with recorded seeds/parameters.
- [ ] Include benchmark dimensions up to the vector dimensionality relevant to OmegaSim starter traces.
- [ ] Defer much higher-dimensional traces until a dedicated dimension-reduction step exists.
- [ ] Record each benchmark run under `experiments/` with parameters, exact command, outputs, and conclusion.
