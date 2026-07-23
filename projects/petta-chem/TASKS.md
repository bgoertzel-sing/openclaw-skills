# Tasks

- [x] 2026-07-07 10:30: Added PeTTa-native cap-6 deterministic selection/generation seams in exp00. `src/chem_exp00.metta` now has `seeded-choice-6`, `select-candidate-6`, `selected-candidate-from-list-6`, `chamber-tick-generated-6`, `exp00-candidate-cap-6`, and cap-6 pool clauses for 6/8-candidate pools. Exp00 smoke covers seed/tick choice, cap construction/truncation, direct cap-6 chamber ticking from a six-rule generated pool, and deterministic selection of the productive second candidate for seed-7. Checks: `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `aecfab9` pushed to GitHub `main`. Commit `d3dde9f` pushed to GitHub `main`. Commit `3d476b6` pushed to GitHub `main`. Commit `db929ce` pushed to GitHub `main`.
- [x] 2026-07-06 22:30: Extended cap-4 rich exp03 dynamics to seed-11/Q-family six-rule source pools. Added six-rule cap/generation support for 12-molecule states, Q-family chamber tick clauses, seed-11 cap-4 run-record atoms, and exp03 smoke tests for productive random dynamics, controls, replay, discrimination, and completeness. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `db187ab` pushed to GitHub `main`.
Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] **Completed 2026-07-23 10:30:** complete bounded live generated ticking
  at the stable eight-candidate generation boundary. New
  `chamber-tick-generated-steps-8` consumes the seven-step final chamber,
  performs one more ordinary generated step, and retains eight outcomes plus
  the final chamber. Exp00 covers closed-cap
  `(no-op no-op no-op no-op no-op no-op no-op no-op)` and productive
  `(productive no-op no-op no-op no-op no-op no-op no-op)` paths with exact
  counts; 320 true results and `git diff --check` passed. Commit `4192438`
  pushed to GitHub `main`.

- [x] **Completed 2026-07-23 08:30:** extend bounded live generated ticking
  through a seventh checked state handoff. New
  `chamber-tick-generated-steps-7` consumes the six-step final chamber,
  performs one more ordinary generated step, and retains seven outcomes plus
  the final chamber. Exp00 covers closed-cap
  `(no-op no-op no-op no-op no-op no-op no-op)` and productive
  `(productive no-op no-op no-op no-op no-op no-op)` paths with exact counts;
  313 true results and `git diff --check` passed. Commit `81705be` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-23 06:30:** extend bounded live generated ticking
  through a sixth checked state handoff. New
  `chamber-tick-generated-steps-6` consumes the five-step final chamber,
  performs one more ordinary generated step, and retains six outcomes plus
  the final chamber. Exp00 covers closed-cap
  `(no-op no-op no-op no-op no-op no-op)` and productive
  `(productive no-op no-op no-op no-op no-op)` paths with exact counts; 306
  true results and `git diff --check` passed. Commit `4fdccfe` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-23 04:30:** extend bounded live generated ticking
  through a fifth checked state handoff. New
  `chamber-tick-generated-steps-5` consumes the four-step final chamber,
  performs one more ordinary generated step, and retains five outcomes plus
  the final chamber. Exp00 covers closed-cap
  `(no-op no-op no-op no-op no-op)` and productive
  `(productive no-op no-op no-op no-op)` paths with exact counts; 299 true
  results and `git diff --check` passed. Commit `f6daad7` pushed to GitHub
  `main`.

- [x] **Completed 2026-07-23 02:30:** extend bounded live generated ticking
  through a fourth checked state handoff. New
  `chamber-tick-generated-steps-4` consumes the three-step final chamber,
  performs one more ordinary generated step, and retains four outcomes plus
  the final chamber. Exp00 covers closed-cap
  `(no-op no-op no-op no-op)` and productive
  `(productive no-op no-op no-op)` paths with exact counts; 292 true results
  and `git diff --check` passed. Commit `317f23b` pushed to GitHub `main`.

- [x] **Completed 2026-07-23 00:30:** extend bounded live generated ticking
  through a third checked state handoff. New
  `chamber-tick-generated-steps-3` consumes the two-step final chamber,
  performs one more ordinary generated step, and retains three outcomes plus
  the final chamber. Exp00 covers closed-cap `(no-op no-op no-op)` and
  productive `(productive no-op no-op)` paths with exact counts; 285 true
  results and `git diff --check` passed. Commit `5a27e88` pushed to GitHub
  `main`.

- [x] **Completed 2026-07-22 22:30:** summarize bounded generated tick
  outcomes inside PeTTa. New `chamber-tick-steps-productive-count` and
  `chamber-tick-steps-no-op-count` accessors distinguish the closed-cap
  `(no-op no-op)` path from the productive `(productive no-op)` handoff
  without host-side list parsing. Exp00 passed with 277 true results and
  `git diff --check` passed. Commit `2da3f94` pushed to GitHub `main`.

- [x] **Completed 2026-07-22 20:30:** totalize fixed-position candidate
  applicability for regenerated productive chamber states. Four-molecule
  applicability now explicitly checks the selected rule against all four
  state positions, so an absent layout reduces to false and returns a checked
  no-op. The productive two-step regression returns `(productive no-op)` and
  preserves the first projected chamber. Exp00 passed with 274 true results
  and `git diff --check` passed. Commit `5e7661d` pushed to GitHub `main`.

- [x] **Completed 2026-07-22 18:30:** expose the exact width of a bounded
  generated tick sequence. New PeTTa-native `chamber-tick-steps-count`
  reports two for the initial `chamber-tick-steps` shape without host-side
  list destructuring. Exp00 passed with 272 true results and
  `git diff --check` passed. Commit `a7b127c` pushed to GitHub `main`.

- [x] **Completed 2026-07-22 14:30:** compose loop-facing generated tick
  steps into a bounded state handoff. New PeTTa-native
  `chamber-tick-generated-steps-2` passes the first checked step's projected
  chamber directly into the second and returns both outcomes plus the final
  chamber in `chamber-tick-steps`. Exp00 covers the deterministic closed-cap
  boundary and passed with 271 true results; `git diff --check` passed.
  Commit `c77b250` pushed to GitHub `main`.

- [x] **Completed 2026-07-22 12:30:** return a single loop-facing generated
  tick step. New PeTTa-native `chamber-tick-generated-step` evaluates the
  checked generation/selection/firing path once and packages its outcome and
  projected chamber in `chamber-tick-step`; direct accessors expose both
  fields. Exp00 covers productive and closed-cap no-op steps and passed with
  269 true results; `git diff --check` passed. Commit `276eba5` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-22 10:30:** expose checked outcome directly from a
  live generated chamber tick. New PeTTa-native
  `chamber-tick-generated-outcome` composes bounded generation, deterministic
  selection, checked firing, and outcome classification for tick-loop
  consumers. Exp00 covers productive and closed-cap no-op paths and passed
  with 265 true results; `git diff --check` passed. Commit `e082865` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-22 08:30:** expose one checked chamber-tick outcome.
  New PeTTa-native `chamber-tick-result-outcome` classifies a valid changed
  result as `productive`, a valid unchanged result as `no-op`, and preserves
  the exact invalid boundary for rejected provenance. Exp00 passed with 263
  true results and `git diff --check` passed; commit `41d0fc0` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-22 06:30:** expose direct chamber-change status
  from checked live tick results. New PeTTa-native
  `chamber-tick-result-changed?` distinguishes a productive valid tick from a
  valid cap-zero no-op and an invalid fail-closed no-op. Exp00 passed with 259
  true results and `git diff --check` passed; commit `80b4923` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-22 04:30:** expose a direct boolean query over
  checked live chamber-tick results. New PeTTa-native
  `chamber-tick-result-valid?` returns true only for the `valid` disposition;
  exp00 covers an ordinary live tick and a malformed over-cap result. Exp00
  passed with 256 true results and `git diff --check` passed; commit `c5f6502`
  pushed to GitHub `main`.

- [x] **Completed 2026-07-22 02:30:** expose the checked chamber-tick
  disposition directly. New PeTTa-native `chamber-tick-result-validity`
  access lets audit/report consumers query `valid` or the first failed
  boundary without positional destructuring. Exp00 passed with 254 true
  results and `git diff --check` passed; commit `8140999` pushed to GitHub
  `main`.

- [x] **Completed 2026-07-22 00:30:** retain chamber-tick validity disposition
  on the live ticking path. New PeTTa-native `chamber-tick-result` constructors
  pair `valid` or the first invalid boundary with the projected chamber, and
  the established chamber-only API now projects the same checked result.
  Exp00 passed with 252 true results and `git diff --check` passed; commit
  `f98be89` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 22:30:** verify every complete chamber-tick
  provenance disposition and its first-failure precedence. Focused exp00
  fixtures now cover `valid` plus invalid attrition, bounds, generation,
  selection, and firing labels without changing chemistry or checked ticking.
  Exp00 passed with 250 true results and `git diff --check` passed; commit
  `16c8707` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 20:30:** attribute complete chamber-tick
  provenance validity in PeTTa. The new
  `generated-selection-fire-record-validity` returns `valid` or the first
  failed attrition, bounds, generation, selection, or firing boundary;
  checked chamber ticking consumes this disposition without changing valid
  chemistry or fail-closed behavior. Exp00 passed with 246 true results and
  `git diff --check` passed; commit `e3cd363` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 18:30:** prove exact-generation rejection at the
  chamber-tick boundary. Exp00 now sends an internally consistent reordered
  equal-width generated pool through both the complete provenance gate and
  `chamber-tick-from-generated-record`; validation rejects it and the chamber
  remains unchanged. Exp00 passed with 244 true results and `git diff --check`
  passed; commit `ad56a61` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 16:30:** bind complete chamber-tick provenance to
  exact candidate generation. The new
  `generated-selection-fire-record-generation-valid?` reconstructs the pool
  from the input chamber and rejects an internally consistent equal-width
  reordered pool. Exp00 passed with 241 results and `git diff --check`
  passed; commit `8315c43` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 14:30:** bind complete chamber-tick provenance to
  the exact firing projection. The new
  `generated-selection-fire-record-firing-valid?` reconstructs the output
  chamber from the input chamber, generated pool envelope, and deterministic
  selected candidate. A forged output chamber now fails closed. Exp00 passed
  with 241 results and `git diff --check` passed; commit `6f2a64c` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-21 12:30:** bind complete chamber-tick provenance to
  the exact deterministic selection path. The new
  `generated-selection-fire-record-selection-valid?` reconstructs the
  bounded pool and selected candidate from the generated source, normalized
  cap, and chamber. A forged equal-cardinality pool now fails closed while
  ordinary productive ticking is unchanged. Exp00 passed with 238 results
  and `git diff --check` passed; implementation commit `f86e7dc`.

- [x] **Completed 2026-07-21 10:30:** route generated chamber ticking through
  complete provenance validation. `chamber-tick-from-generated-record`
  projects the fired chamber only when generation/selection attrition and
  both candidate caps validate; malformed over-cap provenance fails closed.
  Ordinary live generation, deterministic selection, and productive firing
  are unchanged. Exp00 passed with 235 results and `git diff --check` passed;
  commit `c2f8204` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 08:30:** validate both candidate boundaries in
  complete live chamber-tick provenance. The new
  `generated-selection-fire-record-valid?` combines attrition validity with
  the fixed generator cap, normalized selection cap, and embedded scalar-cap
  agreement. Exp00 accepts ordinary cap-2 and closed cap-0 paths and rejects
  a synthetic conservation-valid record whose bounded pool exceeds cap 2.
  Generation, deterministic selection, firing, and chemistry are unchanged.
  Exp00 passed with 233 results and `git diff --check` passed; commit
  `4f617d4` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 06:30:** expose direct validity for complete live
  generation/selection/fire provenance.
  `generated-selection-fire-record-attrition-valid?` derives and validates
  the compact summary inside PeTTa, so persistence/report consumers need not
  materialize it themselves. Exp00 covers ordinary cap-2 and closed cap-0
  chamber paths. Generation, deterministic selection, firing, and chemistry
  are unchanged. Exp00 passed with 229 results and `git diff --check` passed;
  commit `196b097` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 04:30:** reject impossible negative
  cardinalities in compact candidate-attrition provenance.
  `candidate-attrition-counts-nonnegative?` checks all six counts, and the
  complete validity gate now requires this domain check beside conservation
  and stage consistency. Exp00 rejects a negative but otherwise balanced
  record. Generation, deterministic selection, firing, and chemistry are
  unchanged. Exp00 passed with 227 results and `git diff --check` passed;
  commit `fd9fc71` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 02:30:** provide one complete PeTTa-native
  validity gate for compact candidate-attrition provenance.
  `candidate-attrition-valid?` requires both conservation accounting and
  stage attribution to agree. Exp00 accepts the live generated-selection/fire
  summary and rejects independently malformed arithmetic and stage records.
  Generation, deterministic selection, firing, and chemistry are unchanged.
  Exp00 passed with 224 results and `git diff --check` passed; commit
  `52b8945` pushed to GitHub `main`.

- [x] **Completed 2026-07-21 00:30:** validate compact candidate-attrition
  stage attribution directly in PeTTa. `candidate-attrition-stage-consistent?`
  derives the expected `none`, `generation`, `selection`, or `both` label
  from the two stage-specific omission counts. Exp00 covers all four valid
  labels and rejects a count-consistent record carrying a misleading label.
  Generation, deterministic selection, firing, and chemistry are unchanged.
  Exp00 passed with 220 results and `git diff --check` passed; commit
  `edd8d6e` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 22:30:** validate compact candidate-attrition
  accounting directly in PeTTa. `candidate-attrition-consistent?` checks the
  source-to-generated, generated-to-bounded, and source-to-bounded
  conservation identities. Exp00 covers live ordinary provenance, the
  supported twelve-rule boundary, and a deliberately inconsistent record.
  Generation, deterministic selection, firing, and chemistry are unchanged.
  Exp00 passed with 216 true results and `git diff --check` passed; commit
  `201febf` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 20:30:** make every field of the compact
  PeTTa-native `candidate-attrition` audit atom directly queryable. Seven
  accessors cover source/generated/bounded counts, generation/selection/total
  omissions, and attributed stage, avoiding host-side positional
  destructuring. Generation, deterministic selection, firing, and chemistry
  are unchanged. Exp00 passed with 213 true results and `git diff --check`
  passed; commit `bf65490` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 18:30:** package bounded-candidate attrition in
  one PeTTa-native audit atom. `candidate-attrition` carries source,
  generated, and bounded widths; generator, selector, and total omissions;
  and the already-tested causal stage. Focused exp00 coverage verifies the
  preserved and selection-truncated ordinary fixtures without changing
  chemistry or deterministic ticking. Exp00 passed with 206 true results and
  `git diff --check` passed; commit `2a9f71d` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 16:30:** attribute end-to-end candidate
  attrition directly in complete PeTTa-native provenance. Focused exp00
  fixtures classify loss as `none`, `selection`, `generation`, or `both`
  without host-side count comparisons. Generation, deterministic selection,
  firing, and chemistry are unchanged. Exp00 passed with 204 true results and
  `git diff --check` passed.

- [x] **Completed 2026-07-20 12:30:** reconciled the stale exp07 umbrella
  task after the registered diagnostic program and its bounded mechanism
  audit completed. The PeTTa-native program tested matched unguided, weak
  Doob-h, and shuffled controls through the frozen dual-bootstrap cohort;
  the final registered guided-uplift result was negative, the mechanism label
  was `applicability-loss`, and `emergence-claim none` remains. The previously
  open exp06 follow-up was also already completed by the July 10 three-tick
  stateful sweep and ACS boundary check. No chemistry or result changed.
  Exp00 passed with 200 true results and `git diff --check` passed.

- [x] **Completed 2026-07-20 10:30:** classify total source-to-bounded-pool
  retention directly in complete provenance. The ordinary three-rule fixture
  under cap 3 reports `preserved`, while the supported twelve-rule fixture at
  the stable eight-candidate generator boundary reports `truncated`.
  Deterministic firing and chemistry are unchanged. Exp00 passed with 200
  true results and `git diff --check` passed; commit `6c79443` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-20 08:30:** expose total source-to-bounded-pool
  candidate attrition directly in complete provenance. The ordinary
  three-rule fixture under cap 2 reports one omitted candidate; the supported
  twelve-rule fixture reports ten, combining four generator omissions with
  six selection-cap drops. Deterministic firing and chemistry are unchanged.
  Exp00 passed with 198 true results and `git diff --check` passed; commit
  `93b8bfc`.

- [x] **Completed 2026-07-20 06:30:** classify bounded-generator capacity
  directly in complete provenance. The ordinary three-rule fixture reports
  `open`, while the supported twelve-rule fixture reports `saturated` at the
  stable eight-candidate boundary. Selection caps, deterministic firing, and
  chemistry are unchanged. Exp00 passed with 196 true results and
  `git diff --check` passed; commit `538255d` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 04:30:** expose unused bounded-generator
  capacity directly in complete provenance. The ordinary three-rule fixture
  reports five remaining slots under generation cap 8, while the supported
  twelve-rule truncated fixture reports zero. Selection caps, deterministic
  firing, and chemistry are unchanged. Exp00 passed with 194 true results and
  `git diff --check` passed; commit `96ad214` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 02:30:** expose the stable generator boundary
  directly in complete provenance. A PeTTa-native accessor reports generation
  cap 8 for both the ordinary three-rule complete fixture and the supported
  twelve-rule truncated fixture. Selection caps, deterministic firing, and
  chemistry are unchanged. Exp00 passed with 192 true results and
  `git diff --check` passed; commit `017f9d5` pushed to GitHub `main`.

- [x] **Completed 2026-07-20 00:30:** expose bounded-generation disposition
  directly in complete provenance. PeTTa labels the ordinary three-rule
  fixture `complete` and the supported twelve-rule fixture `truncated` at the
  stable eight-candidate boundary. Selection caps, deterministic firing, and
  chemistry are unchanged. Exp00 passed with 190 true results and
  `git diff --check` passed; commit `ebcc70d` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 22:30:** distinguish source width from generated
  pool width in bounded-generation provenance. PeTTa-native accessors report
  3 source rules and 0 generation omissions for the ordinary fixture, versus
  4 omissions for the supported twelve-rule source at the stable
  eight-candidate generator boundary. Selection-stage dropped counts,
  deterministic firing, and chemistry are unchanged. Exp00 passed with 188
  true results and `git diff --check` passed; commit `2bb805e` pushed to
  GitHub `main`.

- [x] **Completed 2026-07-19 20:30:** expose dropped candidate count from
  complete selection/fire provenance. PeTTa derives generated minus bounded
  counts and reports 1 under cap 2, 0 under cap 3, and 3 for a nonpositive
  request over the three-rule fixture. Selection, firing, and chemistry are
  unchanged. Exp00 passed with 185 true results and `git diff --check` passed;
  commit `57bd83c` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 18:30:** expose generated and bounded candidate
  counts from complete selection/fire provenance. PeTTa reports 3 generated
  versus 2 bounded under cap 2, 3 versus 3 under cap 3, and bounded count 0
  for a nonpositive request. Selection, firing, and chemistry are unchanged.
  Exp00 passed with 182 true results and `git diff --check` passed; commit
  `a9093ac` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 16:30:** expose generated-pool cap disposition
  from complete selection/fire provenance. PeTTa reports `truncated` for a
  three-rule pool under cap 2 and `preserved` under cap 3 without host-side
  list inspection. Selection, firing, and chemistry are unchanged. Exp00
  passed with 178 true results and `git diff --check` passed; commit `964b36a`
  pushed to GitHub `main`.

- [x] **Completed 2026-07-19 14:30:** expose scalar requested/effective cap
  fields from complete generated-selection/fire provenance. PeTTa-native
  accessors report requested `(9 3)` and effective `(8 1)` without callers
  destructuring records. Generation, deterministic selection, and chemistry
  are unchanged. Exp00 passed with 176 true results and `git diff --check`
  passed; commit `4604599` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 12:30:** audit nonpositive per-tick requests
  through complete generated provenance. Requested `(-1 1)` and `(0 3)`
  remain visible, normalize to effective `(0 0)`, and cannot change the
  chamber. Selection, generation, and chemistry are unchanged. Exp00 passed
  with 172 true results and `git diff --check` passed; commit `c9dae0c`
  pushed to GitHub `main`.

- [x] **Completed 2026-07-19 10:30:** audit positive per-rule normalization.
  Requested `(2 3)` remains visible in complete generated provenance,
  normalizes to effective `(2 1)`, and produces the ordinary deterministic
  chamber tick. Selection, generation, and chemistry are unchanged. Exp00
  (168 true results) and `git diff --check` passed; commit `93ea3d4` pushed
  to GitHub `main`.

- [x] **Completed 2026-07-19 08:30:** close and audit the negative per-rule
  cap boundary. Requested `(2 -1)` remains visible in complete generated
  provenance, normalizes to effective `(0 0)`, and cannot change the chamber.
  Selection and chemistry are unchanged. Exp00 (165 true results) and
  `git diff --check` passed; commit `4013acf` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 06:30:** make complete effective cap provenance
  fail closed on a nonpositive per-tick boundary. Requested `(-1 1)` and
  `(0 3)` now normalize to `(0 0)`; deterministic selection and chamber
  chemistry are unchanged. Exp00 (162 true results) and `git diff --check`
  passed; commit `d744596` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 04:30:** expose the complete effective
  `candidate-cap` from generated-selection/fire provenance. Requested cap
  `(9 3)` normalizes to the supported `(8 1)` and `(2 0)` closes to `(0 0)`;
  requested provenance, deterministic selection, and chemistry are unchanged.
  Exp00 (160 true results) and `git diff --check` passed; commit `1df98e4`
  pushed to GitHub `main`.

- [x] **Completed 2026-07-19 02:30:** preserve the complete requested
  `candidate-cap` directly in generated-selection/fire provenance beside the
  effective bounded scalar. Tests distinguish requested cap 9/effective cap 8
  and requested per-rule-zero/effective cap 0 without changing deterministic
  selection or chamber chemistry. Exp00 (157) and `git diff --check` passed;
  commit `e26c74a` pushed to GitHub `main`.

- [x] **Completed 2026-07-19 00:30:** expose the effective bounded cap directly
  from PeTTa candidate-selection and generated-selection/fire provenance.
  Tests cover ordinary cap 2 and requested cap 9 clamped to effective cap 8;
  deterministic selection and chamber chemistry are unchanged. Exp00 and
  `git diff --check` passed; commit `fcde7b5` pushed to GitHub `main`.

- [x] **Priority experiment completed 2026-07-17:** froze proactive
  oversized-source-list hardening at twelve rules and ran the fixed exp07
  unguided / weak Doob-h / matched shuffled sequence through all registered
  endpoints and causal ablations. The corrected ordered-bootstrap fixture
  supports bounded guided causal RAF uplift; spontaneous emergence remains
  unclaimed because the chemistry and guidance target are designed.

- [x] **Completed 2026-07-17 20:30:** implement only the fail-closed pre-run gates for
  `PREREG_ORDERED_REPLICATION.md`: seed/hash calibration, identical cohort
  pools, cohort-B rule-identity selection under permutation, matched cost, and
  a synthetic direct tick. No seed-101--132 trajectory was constructed.

- [x] **Completed 2026-07-17 22:30:** execute and report cohort A exactly once over frozen
  seeds 101--116 and ticks 3--26, including replay and all registered endpoints
  and causal ablations. Complete its report before constructing cohort B; do
  not extend or replace the cohort after outcomes are visible.

- [x] **Completed 2026-07-18 00:30:** execute cohort B exactly once over frozen seeds
  117--132 and ticks 3--26 as order/hash robustness characterization. Report
  it separately and explicitly do not treat it as rescue of cohort A's failed
  primary replication.

- [x] **Completed 2026-07-18 02:30:** close the ordered-replication program as two
  preregistered negative gates, preserve the cohort-A/cohort-B distinction,
  and preregister any successor chemistry before implementing new outcomes.

- [x] **Completed 2026-07-18 04:30:** implement only the fail-closed pre-run gates in
  `PREREG_DUAL_BOOTSTRAP.md`: twelve-rule materialization, order-invariant
  identity-addressed cap-8 generation, initial applicability/RAF negativity,
  complete selector calibration, matched cost, shared arm pools, and one
  nonregistered direct tick. Do not construct a seed-201--232 trajectory.

- [x] **Completed 2026-07-18 06:30:** only after re-running the complete fail-closed gate,
  add the frozen seed-201--232 draw support and execute the preregistered
  three-arm tick-3--34 matrix exactly once. Report replay and every frozen
  endpoint/ablation without extending seeds, ticks, pool, or thresholds.

- [x] **Completed 2026-07-18 08:30:** closed the dual-bootstrap program as a
  preregistered negative result. No seeds, ticks, chemistry, selector, or
  endpoints were added. Updated the repository README and durable project
  records to agree with the completed protocol and report. Exp00 (154) and
  `git diff --check` passed; commit `56fda93` pushed to GitHub `main`.

- [x] **Completed 2026-07-18 10:30:** chose mechanism characterization as the
  next scientific objective and froze `PREREG_DUAL_MECHANISM_AUDIT.md` before
  implementing any derived diagnostic. The audit reuses only the completed
  seed-201--232 matrix and fixes trace fields, summaries, integrity gates, and
  a descriptive interpretation precedence. It cannot rescue or reinterpret
  the registered negative result.

- [x] **Completed 2026-07-18 12:30:** implement only the PeTTa-native trace and integrity
  gates in `PREREG_DUAL_MECHANISM_AUDIT.md`. First reproduce every registered
  endpoint exactly; do not inspect or report new mechanism aggregates until
  trace cardinality, uniqueness, replay, and endpoint equivalence all pass.
  Exp00 (154), exp07 (305), detector invariance, and `git diff --check`
  passed; commit `65cab25` pushed to GitHub `main`.

- [x] **Completed 2026-07-18 20:30:** derive the frozen mechanism diagnostics and
  paired summaries from the validated PeTTa trace, apply the preregistered
  interpretation precedence exactly once, and report without significance
  tests, adaptive subgroups, or reinterpretation of the negative outcome.
  **14:30 slice complete:** PeTTa now derives all twelve rule selected/fired
  counts, first-absent selected/fired counts, and pathway/distractor blocked
  partitions. Weak has 51 blocked first-absent selections versus unguided 38,
  decisively assigning the first eligible label, `applicability-loss`.
  **16:30 slice complete:** PeTTa now also derives each seed's first-complete
  tick for all six ordered pathway prefixes (99 when absent) and its 0--6
  prefix-depth occupancy over all 32 frozen trace rows, exposing all three arm
  summaries in the report query. **18:30 slice complete:** PeTTa now derives
  per-seed first exhaustion ticks for A--E, counts the three scheduled resets
  by prefix depth 0--5, and serializes seed-paired weak-minus-unguided prefix
  timing and occupancy differences. **20:30 completion:** PeTTa serializes
  ordinary 32-seed medians for all prefix and food-exhaustion ticks and
  seed-paired food/reset differences, retaining sentinel 99 unchanged. The
  fixed interpretation is `applicability-loss`; the negative guided-uplift
  result and emergence claim none remain unchanged. Exp00, exp07, the dual
  report, detector invariance, and `git diff --check` pass. Commit `a57f4e0`
  pushed to GitHub `main`.

- [x] 2026-07-18 06:30: executed the frozen dual-bootstrap matrix exactly once.
  RAF incidence was 13/32 unguided, 9/32 weak Doob-h, and 0/32 shuffled, so
  weak missed the ten-seed advantage over each control and underperformed
  unguided. All 96 trajectories replayed; persistence totals were 95/51/0,
  event totals 549/523/396, and diversity totals 336/278/219. Either bootstrap,
  all four cycle-catalyst edges, or any individual cycle rule ablated weak
  incidence to 0/32, but guiding-term removal retained unguided 13/32. The
  registered guided-uplift result is negative; no extension and emergence
  claim none. Checks: exp00 (154), exp07 (302), detector invariance, runnable
  full report, and `git diff --check`. Commit `48af89b` pushed to GitHub
  `main`.

- [x] 2026-07-18 04:30: closed the complete dual-bootstrap implementation
  gate using only seed-7 fixtures and synthetic draws. PeTTa materializes all
  seventeen species, twelve source rules, and twelve catalysis edges; derives
  initial applicability and RAF negativity; maps both frozen source orders to
  the same cap-8 identity set across all three distractor phases; exhaustively
  calibrates weak/shuffled masses across all six frontier identities and all
  phases at matched cost; verifies shared arm pools; and selects/ticks `db0`
  by identity through ordinary chamber ticking. No registered seed support,
  trajectory, or outcome exists. Checks: exp00 (153), exp07 (270), detector
  invariance, and `git diff --check`. Commit `6b3fc76` pushed to GitHub
  `main`; emergence claim none.

- [x] 2026-07-18 02:30: closed cohort A as a failed primary replication and
  cohort B as a separately failed order/hash gate; cohort B cannot rescue A.
  Froze `PREREG_DUAL_BOOTSTRAP.md` and matching PeTTa design-only atoms before
  implementation: dual bootstrap, four-rule RAF, twelve-rule source,
  order-invariant identity-addressed cap 8, fresh seeds 201--232, ticks 3--34,
  fixed hash/masses/thresholds/ablations, direct bounded ticking, and no
  adaptive extension. No successor trajectory or outcome evaluated; emergence
  claim none. Checks: exp00 (153), exp07 (252), detector invariance, and
  `git diff --check`. Commit `06c0f3c` pushed to GitHub `main`.

- [x] 2026-07-18 00:30: completed frozen cohort B. RAF incidence was 8/16
  unguided, 16/16 weak Doob-h, and 0/16 shuffled. The incidence advantage
  passed, but guiding-term removal retained unguided 8/16 and violated the
  prespecified maximum of two, so order/hash robustness is not supported and
  cannot rescue cohort A. All 48 trajectories replayed; persistence totals
  were 33/145/0, event totals 281/275/260, diversity totals 120/127/92, and
  structural ablations were 0/16. Matched guidance cost was 3,072 per guided
  arm; no extension; emergence claim none. Checks: exp00 (153), exp07 (250),
  detector invariance, and `git diff --check`. Commit `836ac36` pushed to
  GitHub `main`.

- [x] 2026-07-17 22:30: completed the frozen cohort-A exact-form replication.
  RAF incidence was 1/16 unguided, 4/16 weak Doob-h, and 0/16 shuffled, below
  the preregistered weak advantage of six over each control. All 48
  trajectories replayed; persistence totals were 1/15/0, event totals
  259/263/250, and distinct-rule totals 112/116/85 of 128. Matched guidance
  cost was 3,072 per guided arm. Bootstrap, full catalyst, and individual
  cycle-rule ablations were 0/16; guiding-term removal retained unguided 1/16.
  Primary replication not supported; cohort B unevaluated; emergence claim
  none. Checks: exp00 (153), exp07 (248), detector invariance, and
  `git diff --check`. Commit `1f237df` pushed to GitHub `main`.

- [x] 2026-07-17 20:30: closed the ordered-replication implementation gate.
  Explicit PeTTa seed support covers 101--132; both hashes pass exhaustive
  96-bin permutation calibration; all arms share the exact cohort-specific
  cap-8 pool; and cohort B maps selector bins to rule identities before
  searching its permuted candidates. Weak and shuffled identity checks cover
  all four frontier phases, their derived masses retain equal eight-unit cost,
  and a synthetic seed-7 draw selects and directly ticks `ob0` from cohort B's
  third pool position. Checks: exp00 (153), exp07 (246), detector invariance,
  and `git diff --check`. No registered trajectory or endpoint was evaluated;
  spontaneous-emergence claim remains none. Commit `0c078d2` pushed to
  GitHub `main`.

- [x] 2026-07-17 18:30: froze `PREREG_ORDERED_REPLICATION.md` without reusing
  or extending seeds 19--26. Cohort A fixes fresh seeds 101--116 and a new draw
  hash for exact-form replication. Cohort B holds out seeds 117--132, changes
  the hash, and permutes pool order while requiring rule-identity selection.
  Both cohorts retain the exact chemistry, ticks 3--26, cap 8, matched-cost
  controls, replay, and causal ablations, with fixed success thresholds and
  cohort-A-before-B execution. A PeTTa design-only atom is smoke-tested; no
  replication outcome was evaluated and spontaneous-emergence claim remains
  none. Checks: exp00 (153), exp07 (225), and `git diff --check`. Commit
  `07fed0d` pushed to GitHub `main`.

- [x] 2026-07-17 16:30: corrected a consequential detector-wiring error in the
  frozen ordered-bootstrap report: the ordered endpoint now calls its
  preregistered `op1/op2/op0` rolling detector rather than the historical
  `rp0/rp1/rp2` detector. Without changing seeds, ticks, draws, pool, or food
  schedule, incidence is 0/8 unguided, 6/8 weak Doob-h, and 0/8 shuffled;
  first-hit, persistence (0/41/0), diversity (42/59/39 of 64), replay, and all
  prespecified causal endpoints are PeTTa-tested. Guiding-term, bootstrap,
  full catalyst-edge, and each individual cycle-rule ablation reduce weak
  incidence to 0/8. The preregistered bounded guided causal RAF-uplift condition
  is supported; spontaneous emergence remains unclaimed. Checks: exp00, exp07,
  detector invariance, and `git diff --check`. Commit `7e1e677` pushed to
  GitHub `main`.

- [x] 2026-07-17 14:30: passed the ordered-bootstrap fail-closed gate, including the standing exp04 detector-invariance control, and executed the frozen three-arm seed-19--26, tick-3--26 matrix exactly once. Rolling RAF incidence was 0/8 in unguided, weak Doob-h, and shuffled-frontier guidance; every first-hit sentinel was 99. Productive-event totals were 103/119/104 and all 24 trajectories replay exactly. The run also exposed and fixed an imported-equation compiler boundary by making ordered cap-8 generation/applicability/firing executable PeTTa-local clauses and removing exp00 bounded generation's faulty intermediate `let`. No seeds or ticks were added; `emergence-claim none`. Checks: exp00 (153), exp07 (222), detector invariance, and `git diff --check`.

- [x] 2026-07-17 12:33: closed the ordered-bootstrap initial-negativity, four-frontier-phase, full 96-bin calibration, matched-cost, and direct bounded-tick gates without constructing a registered trajectory. The generic PeTTa named-molecule kernel now supports the frozen twelve-species chamber. Initial `ob0` is applicable while `op1/op2/op0` are not, the empty event history is event-derived RAF-negative, and all `AB/AC/CD` frontier phases resolve correctly. Unguided realizes `(12 12 12 12 12 12 12 12)` in every phase; weak guidance realizes phase-specific `20/4` frontier/distractor masses and shuffled guidance reverses the same pair, with identical eight-unit shifted mass. A synthetic draw selects `ob0` through the exact generated cap-8 pool and feeds it to ordinary chamber ticking. No seed-19--26 trajectory or RAF endpoint was evaluated; `emergence-claim none`. Checks: exp00 (153), exp07 (217), `git diff --check`.

- [x] 2026-07-17 10:33: materialized the ordered-bootstrap chemistry inputs without selection or chamber ticking. PeTTa constructs the frozen twelve-species initial chamber and exact ordered eight-rule candidate pool through shared bounded cap-8 generation for all arms. Eight Atomspace `(catalyzes Molecule RuleId)` facts are closed-world queryable; positive and negative smoke checks prevent structural/name inference. No selector, seed-19--26 trajectory, or RAF endpoint was evaluated and `emergence-claim none`. Checks: exp00 (153), exp07 (197), `git diff --check`. Commit `986c489` pushed to GitHub `main`.

- [x] 2026-07-17 08:34: closed the frozen rich-pool null as pool-composition evidence and preregistered `PREREG_ORDERED_BOOTSTRAP.md` before inspecting any new outcome. The prior cycle is necessary under ablation but guidance is unnecessary because controls remain positive. The successor removes initial `CD`, adds a non-RAF `ob0` bootstrap, freezes the ordered `op1 -> op2 -> op0` catalytic frontier, held-out seeds 19--26, ticks 3--26, cap 8, denominator 96, and equal-cost state-aware/shuffled policies. PeTTa smoke tests the closure interpretation and design-only contract; no ordered-bootstrap chamber, selector, or trajectory exists and `emergence-claim none`. Checks: exp00 (153), exp07 (187), `git diff --check`. Commit `65ef00a` pushed to GitHub `main`.

- [x] 2026-07-17 06:30: completed the prespecified frozen rich-pool guiding-term/catalyst/rule ablations with PeTTa-native counterfactual chamber ticks. Guiding-term removal retains unguided RAF incidence 5/8. Removing the three latent catalyst edges yields 0/8 RAF incidence in all arms, with productive-event totals 116/83/117; separately blocking `rp0`, `rp1`, or `rp2` also yields 0/8 in every arm. Counterfactuals preserve the exact seeds, ticks, eight-candidate pool, arm selector, and food schedule. The three-rule closure is necessary, guidance is not, both controls remain positive, and `emergence-claim none`. Checks: exp00 (153), exp07 (185), `git diff --check`. Commit `9824ed1` pushed to GitHub `main`.

- [x] 2026-07-17 04:30: completed the frozen rich-pool intervention-cost endpoint without new trajectories. PeTTa derives an exact total-variation shifted-mass numerator from the calibrated 88-bin selector distributions: unguided 0, weak Doob-h 15, and shuffled guidance 15 per draw. The matched guidance arms therefore each cost 360 mass units per 24-tick trajectory and 2,880 over eight trajectories. Chemistry outcomes are not inputs to the cost. Both controls remain RAF-positive and `emergence-claim none`. Checks: exp00 (154), exp07 (185), `git diff --check`. Causal ablations remain.

- [x] 2026-07-17 02:30: completed the frozen rich-pool diversity-collapse endpoint without new trajectories. PeTTa counts distinct fired rule IDs against the exact shared eight-rule pool. Diversity vectors were unguided `[6,8,8,8,8,7,8,8]`, weak Doob-h `[8,7,6,8,8,8,8,8]`, and shuffled `[7,7,5,5,7,7,8,8]`, totaling 61/61/54 of 64 possible seed-rule presences and collapse deficits 3/3/10. Weak and unguided diversity are equal in aggregate; shuffled is lower. Both controls remain RAF-positive and `emergence-claim none`. Checks: exp00 (153), exp07 (176), `git diff --check`. Commit `5b436eb` pushed to GitHub `main`. Cost and causal ablations remain.

- [x] 2026-07-17 00:30: completed the frozen rich-pool rolling-condition persistence endpoint without extending the registered matrix. A PeTTa-native tick recursion measures the longest consecutive ticks whose last eight productive events contain `rp0/rp1/rp2`, with blocked ticks correctly extending an unchanged positive window. Persistence vectors were unguided `[0,3,1,1,3,0,5,0]`, weak Doob-h `[7,7,0,6,11,7,4,7]`, and shuffled `[0,6,0,0,0,0,3,2]`, totaling 13/49/11. Both controls remain positive; `emergence-claim none`. Checks: exp00 (153), exp07 (174), `git diff --check`. Commit `e72b7fe` pushed to GitHub `main`.

- [x] 2026-07-16 22:30: executed the complete frozen rich-pool 3-arm x 8-seed matrix once without peek-and-extend. The PeTTa-native recursive constructor consumes ticks 3--26, resets A/B/C/D at 11/19, advances blocked selections, regenerates the exact cap-8 pool, and replays to state tick 27. Rolling eight-event three-rule RAF incidence was unguided 5/8, weak Doob-h 7/8, shuffled 3/8; first hits were `[99,14,22,13,23,99,22,99]`, `[15,20,99,19,16,15,23,14]`, and `[99,11,99,99,99,99,14,22]`; productive events totaled 130/120/123. Both controls are positive, so `emergence-claim none`. The run exposed and boundedly extended chamber event history from 9 to 24 entries. Checks: exp00 (153), exp07 (174), `git diff --check`.
  Commit `41fb965` pushed to GitHub `main`.

- [x] 2026-07-16 20:30: closed the frozen rich-pool pre-run implementation gate without constructing registered outcomes. PeTTa-native fired-event predicates report the initial empty history RAF-negative and distinguish complete `rp0/rp1/rp2` history from incomplete history. The gate record binds the exact eight catalysis facts, shared pool, calibrated arm masses, and direct ordinary chamber-tick path; canonical exp04 detector controls pass. Checks: exp00 (153), exp07 (167), detector invariance, and `git diff --check`. Commit `3d347d7` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-16 18:30: completed the frozen rich-pool denominator-88 sampler calibration without constructing registered outcomes. A PeTTa-native exhaustive recursion covers synthetic draw bins 0--87 and realizes the exact declared per-candidate masses for unguided `(11 11 11 11 11 11 11 11)`, weak Doob-h `(16 16 16 8 8 8 8 8)`, and shuffled guidance `(8 8 8 16 16 16 8 8)`. Checks: exp00 (153), exp07 (163), and `git diff --check`. Commit `2d34083` pushed to GitHub `main`. Initial RAF-negativity and detector controls remain before trajectories; `emergence-claim none`.

- [x] 2026-07-16 16:30: implemented the first rich-pool pre-run slice without evaluating outcomes. The shared PeTTa chamber now contains the frozen thirteen species and eight rules; named-molecule abundance/update and generated cap-8 paths support that shape. Eight explicit catalysis edges and the denominator-88 arm partitions select from one exact shared bounded pool, with provenance connected to ordinary event-producing chamber ticking. Smoke covers pool identity, selector boundaries, generated/bounded pools, all-arm seed-12 selections, and a productive tick. Full 88-bin calibration plus initial-negativity/detector gates remain before outcomes. Checks: exp00 (153), exp07 (159), `git diff --check`. Commit `712fa17` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-16 14:30: followed the preregistered all-arms-positive pivot by freezing `experiments/exp07/PREREG_RICH_POOL.md` and matching PeTTa contract atoms before outcome implementation. The design uses one shared cap-8 pool with a bootstrapped latent three-rule RAF, five productive food-competing distractors, explicit first-class catalysis, matched unguided/weak Doob-h/shuffled arms, seeds 11--18, a fixed 24-tick horizon, causal ablations, and fail-closed pre-run gates. No rich-pool outcome was evaluated; the implementation gate is pending and `emergence-claim none`. Checks: exp00 (153), exp07 (143), `git diff --check`. Commit `e3bbc41` pushed to GitHub `main`.

- [x] 2026-07-16 12:30: completed the frozen exp07 N=20 ticks 3--22 matrix without interim extension. All 12 PeTTa-native trajectories used the identical replenishment schedule, replayed exactly, and produced 8 events/seed (32/arm). RAF incidence was 4/4 in every arm; first-hit ticks were unguided `[5,3,8,10]`, weak Doob-h `[3,3,8,8]`, shuffled `[5,3,4,3]`. The all-arms-positive preregistered pivot applies: closure is attributable to the shared two-rule pool rather than guidance, guiding-term removal does not collapse controls, and `emergence-claim none` remains. Checks: exp00 153, exp07 141, `git diff --check`. Commit `04d7b02` pushed to GitHub `main`.

- [x] 2026-07-16 10:31: passed the mandatory exp07 pre-run pool-identity gate without evaluating registered outcomes. The N=20 constructors now give unguided, weak Doob-h, and shuffled guidance the exact same strength-1 affinity candidate pool for every seed/tick; arms differ only in categorical selection mass. The frozen historical pilot constructors are unchanged. Generic PeTTa equality plus seed-7/tick-3 and seed-10/tick-22 smoke guard the boundary. Checks: exp00 (153), exp07 (134), and `git diff --check`. Commit `05d6ea9` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-16 08:32: implemented the arm-independent PeTTa-native time/sustainment prerequisite for the N=20 exp07 run. Blocked candidate draws advance time with no fabricated event; ticks 8/13/18 reset A/B/C to the frozen 2/1/1 basal abundances while preserving accumulated chemistry and provenance. Unit smoke tests exercise schedule membership, non-schedule identity, blocked advance, and productive firing after replenishment without inspecting registered arm outcomes. Checks: `scripts/run_exp00.sh`, `scripts/run_exp07.sh`, `git diff --check`. Commit `3eb370e` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-16 08:25: added a separately labelled seed-31 dynamic positive-control fixture for exp07 detector invariance. The canonical `run_rich_raf.py` + committed `chem_exp04.metta` path passes A -> no-catalysis B -> A call-order invariance (RAF 15 -> 0 -> 15), direct-versus-advanced tick-history invariance (RAF 15, core `{lCD,lBCD2}`), and static single-result/mutation guards. No registered experimental arm was inspected; N=20, seeds, endpoints, and `emergence-claim none` are unchanged. Run: `experiments/20260716T152520Z-exp07-detector-invariance/`. Checks: exp04 80, exp07 129, Python compile, diff check.

- [x] 2026-07-16 06:30: expanded the matched two-tick stateful exp07 path across all three arms and seeds 7-10. Productive-event vectors are unguided `[1,2,1,2]`, weak Doob-h `[2,2,1,1]`, and shuffled guidance `[1,2,2,1]`; all arms total 6 and all 12 trajectories replay exactly. This is a short-horizon aggregate null, not an ACS/RAF outcome. Checks: `scripts/run_exp00.sh` (154 reported assertions), `scripts/run_exp07.sh` (128), `git diff --check`. Commit `28ddc28` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-16 04:30: ran the smallest stateful exp07 trajectory on the matched seven-molecule chamber. Weak Doob-h/seed-7 selects `e5r0` at tick 3 and `e5r1` at tick 4; the second tick consumes the first tick's mutated chamber, appends the second event, and records exact seed/tick/state-carry replay provenance. Checks: `scripts/run_exp00.sh` (153 reported assertions), `scripts/run_exp07.sh` (98), `git diff --check`. Commit `bc7f7de` pushed to GitHub `main`. Boundary: trajectory plumbing only; no ACS/RAF outcome and `emergence-claim none`.

- [x] 2026-07-16 02:30: implemented the matched PeTTa-native multi-molecule chamber applicability/update seam. All arms now share one seven-molecule initial chemistry; all 24 candidates in the 12 two-candidate arm/seed pools are applicable, and all 12 categorical selections fire through ordinary chamber ticking. The matched-fixture gate passes and the stateful ensemble is unblocked. Checks: `scripts/run_exp00.sh` (153 reported assertions), `scripts/run_exp07.sh` (96), `git diff --check`. Commit `817dc42` pushed to GitHub `main`. Scientific boundary: applicability/update infrastructure only; `emergence-claim none`.

- [x] 2026-07-16 00:30: audited all 12 exp07 pilot arm/seed first draws against their actual four-molecule chambers before running stateful outcomes. Productive ordinary ticks are unguided 0/4, weak Doob-h 3/4, and shuffled guidance 3/4. The matched-fixture gate therefore fails: exp05 fixtures only support the candidate chosen by their old deterministic selector, so these rates cannot be interpreted as guidance effects. Added total PeTTa-native applicability diagnostics and changed the pilot contract boundary to block the confounded ensemble. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (76), `git diff --check`. Commit `6f42e50` pushed to GitHub `main`; `emergence-claim none`.

- [x] 2026-07-15 22:30: calibrated exp07's replayable categorical sampler over the full four-bin cycle. Tick-parameterized PeTTa-native pools/selections for ticks 3-6 and fixed seeds 7-10 yield exact matched-arm first-candidate counts: unguided 8/16, weak Doob-h 12/16, shuffled guidance 4/16. This removes sampler miscalibration as a confound before the stateful ensemble; no ACS outcome or emergence claim yet. Checks: `scripts/run_exp00.sh`, `scripts/run_exp07.sh` (60 reported assertions), `git diff --check`. Commit `76d14eb` pushed to GitHub `main`.

- [x] 2026-07-15 20:30: added the first PeTTa-native stochastic-ensemble gate for exp07. A replayable four-bin categorical draw gives matched unguided, weak Doob-h, and shuffled-guidance arms first-candidate weights 2/4, 3/4, and 1/4 over fixed seeds 7-10; selected candidates fire through the ordinary exp00 chamber tick. The explicit contract preregisters all required outcome and ablation fields. Boundary: sampler/direct-tick gate only, not a multi-tick ensemble result or ACS claim. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (53), `git diff --check`. Commit `2c564b2` pushed to GitHub `main`.

- [x] 2026-07-15 19:22: made catalysis first-class for the exp04 RAF reference. Added 18 explicit binary PeTTa `(catalyzes Molecule RuleId)` edges, routed PeTTa RA checks through that relation, made ablation an empty relation over the same predicate, and changed `run_rich_raf.py` to load PeTTa facts rather than infer catalysis structurally. Gate `20260716T022154Z-first-class-catalysis-exp04`: 79 PeTTa assertions, Python compilation, and diff check passed; maximal RAF 15, core 2 (`lCD`, `lBCD2`), ablation 0. Next: use this relation in the exp07 emergence ensemble.

- [x] 2026-07-15 18:30 progress: extended the explicit oversized PeTTa-native source-list boundary from eleven to twelve rules. Twelve-rule four-molecule chambers now generate the stable first-eight candidate prefix, retain all twelve source rules, recognize an owned rewrite in the retained twelfth position, and complete cap-2 deterministic chamber ticking. Checks: `scripts/run_exp00.sh` (152 checks), `git diff --check`. Commit `7061403` pushed to GitHub `main`.

- [x] 2026-07-15 16:30 progress: extended the explicit oversized PeTTa-native source-list boundary from ten to eleven rules. Eleven-rule four-molecule chambers now generate the stable first-eight candidate prefix, retain all eleven source rules, recognize an owned rewrite in the retained eleventh position, and complete cap-2 deterministic chamber ticking. Checks: `scripts/run_exp00.sh` (149 checks), `git diff --check`. Commit `3353533` pushed to GitHub `main`.

- [x] 2026-07-15 14:30 progress: extended the explicit oversized PeTTa-native source-list boundary from nine to ten rules. Ten-rule four-molecule chambers now generate the stable first-eight candidate prefix, retain all ten source rules, satisfy the corresponding rewrite-ownership guard, and complete cap-2 deterministic chamber ticking. Checks: `scripts/run_exp00.sh` (146 checks), `git diff --check`. Commit `5ca80ee` pushed to GitHub `main`.

- [x] 2026-07-15 12:30 progress: bounded oversized PeTTa-native chamber generation at the explicit eight-candidate kernel maximum. A nine-rule chamber now produces the stable first-eight prefix, retains all source rules as provenance, and completes a smaller-cap deterministic chamber tick; the chamber ownership guard covers the same nine-rule shape. Checks: `scripts/run_exp00.sh` (143 checks), `git diff --check`. Commit `9d95a7a` pushed to GitHub `main`.

- [x] 2026-07-15 10:30 progress: clamped oversized positive per-tick candidate caps to the PeTTa base kernel's explicit eight-candidate maximum. A `(candidate-cap 9 1)` now records effective cap 8, preserves the smaller three-rule generated pool, deterministically selects through the supported cardinality seam, and fires the ordinary chamber tick instead of leaving cap 9 irreducible. Checks: `scripts/run_exp00.sh` (141 checks), `git diff --check`. Commit `02e5f15` pushed to GitHub `main`.

- [x] 2026-07-15 08:32 progress: clamped nonpositive candidate-cap inputs at the unified PeTTa-native bounded-generation/selection boundary. Negative per-tick or per-rule allowances now produce effective cap zero, an empty bounded pool, `no-candidate`, and an unchanged chamber instead of an irreducible negative cap. Checks: `scripts/run_exp00.sh` (137 checks), `git diff --check`. Commit `5b9c790` pushed to GitHub `main`.

- [x] 2026-07-15 08:04 progress: enforced zero per-rule candidate caps at the direct PeTTa-native bounded-generation boundary. `bounded-candidate-pool` now uses the same effective cap as deterministic selection, so `(candidate-cap 2 0)` yields `(candidate-pool 0 ())` immediately. Checks: `scripts/run_exp00.sh` (133 checks), `git diff --check`. Commit `638d8a4` pushed to GitHub `main`.

- [x] 2026-07-13 18:30 progress: enforced zero per-rule candidate caps in the unified PeTTa-native cap -> deterministic selection -> chamber-tick path. Generic generation emits at most one candidate per source rule, so `(candidate-cap 2 0)` now records effective cap zero, an empty bounded pool, and `no-candidate`, leaving the chamber unchanged. Checks: `scripts/run_exp00.sh` (133 checks), `scripts/run_exp05.sh`, `scripts/run_exp06.sh`, `scripts/run_exp07.sh`, `git diff --check`. Commit `11ea4e5` pushed to GitHub `main`.

- [x] 2026-07-13 16:30 progress: enforced source-rewrite integrity in unified deterministic chamber ticking. External/scored candidates may reassign catalysts but must preserve a chamber rule's stable ID, reactants, and product; a same-ID altered rewrite remains inspectable in bounded-selection provenance but cannot fire. Checks: `scripts/run_exp00.sh` (130 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `18ff8db` is pushed to GitHub `main`.

- [x] 2026-07-13 14:30 progress: preserved event history through unified deterministic chamber ticking. Successful selected-candidate firing now appends its event to the chamber's existing bounded event list rather than replacing prior provenance. Focused exp00 smoke covers firing with a non-empty history. Checks: `scripts/run_exp00.sh` (128 checks), `git diff --check`. Commit `445df9c` pushed to GitHub `main`.

- [x] 2026-07-13 12:30 progress: guarded unified deterministic chamber ticking with candidate-pool envelope tick provenance. A stale external/scored pool remains fully inspectable but cannot mutate a current chamber even if the selected candidate carries the current tick. Checks: `scripts/run_exp00.sh` (127 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `1ec8449` pushed to GitHub `main`.

- [x] 2026-07-13 10:30 progress: guarded unified deterministic candidate chamber ticks by chamber-owned rule identity. Foreign candidates selected from external pools retain complete bounded-selection provenance but cannot mutate the chamber. Stable ID membership preserves exp05 scored catalyst reassignment. Checks: `scripts/run_exp00.sh` (125 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `7d816b5` pushed to GitHub `main`.

- [x] 2026-07-13 08:30 progress: enforced tick-scoped candidate provenance in the unified PeTTa-native applicability guard. Candidates selected from stale pools remain inspectable but cannot fire against a later chamber, even when molecule abundance would otherwise permit the rule. Focused tests cover the predicate and direct selection/fire record path. Checks: `scripts/run_exp00.sh` (123 checks), `git diff --check`. Commit `e80974a` pushed to GitHub `main`.

- [x] 2026-07-13 06:30 progress: routed unified deterministic candidate chamber ticks through the existing PeTTa-native applicability guard. Inapplicable selected candidates remain inspectable in selection provenance but produce an unchanged chamber and no event, preventing negative abundance on the direct and generated bounded paths. Checks: `scripts/run_exp00.sh` (122 checks), `git diff --check`. Commit `6cf6e9f` pushed to GitHub `main`.

- [x] 2026-07-13 04:30 progress: closed zero-cap and empty-source boundaries in the generic PeTTa-native generation -> cap -> deterministic selection -> chamber-tick chain. Empty bounded pools retain provenance with `no-candidate` and leave chambers unchanged without events; empty-rule four-molecule chambers now generate empty pools, which positive caps preserve. Checks: `scripts/run_exp00.sh` (119 checks), `git diff --check`. Commit `ff58491` pushed to GitHub `main`.

- [x] 2026-07-13 02:30 progress: removed the remaining parallel cap-specific chamber-tick implementations. `chamber-tick-candidate-pool-1` through `-8` and `chamber-tick-generated-1` through `-8` now preserve compatibility as aliases of the generic provenance-backed operations, leaving one cap -> actual-cardinality deterministic selection -> firing implementation. Checks: `scripts/run_exp00.sh` (116 checks), `git diff --check`. Commit `4c45a5d` pushed to GitHub `main`.

- [x] 2026-07-13 00:30 progress: made bounded candidate generation and all cap-specific generated-tick compatibility paths single-pass. `bounded-candidate-pool` now generates once, while `chamber-tick-generated-1` through `-8` pass the raw generated pool to the existing cap -> deterministic selection -> firing path, eliminating redundant first caps. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`.

- [x] 2026-07-12 22:30 progress: bound the generated pool, bounded pool, and deterministic selection exactly once through the generic PeTTa-native generation -> cap -> selection -> chamber-fire path. Added complete-record accessors for the exact bounded pool and selected candidate consumed by firing. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`. Commit `5ecdacc` pushed to GitHub `main`.

- [x] 2026-07-12 20:30 progress: added PeTTa-native `generated-selection-fire-record-from-chamber`, retaining the uncapped generated pool beside bounded-selection provenance and the resulting fired chamber. Generic generated chamber ticking now projects from this complete generation -> cap -> deterministic selection -> firing chain. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `af49c98` pushed to GitHub `main`.

- [x] 2026-07-12 18:30 progress: added PeTTa-native `selection-fire-record-from-pool`, combining full bounded-selection provenance with the chamber produced by firing the exact selected candidate. Generic chamber ticking now projects from that record, preventing selection provenance and firing from silently following separate paths. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `6fa9ced` pushed to GitHub `main`.

- [x] 2026-07-12 16:30 progress: extended exp06’s PeTTa-native ACS boundary across all selected pairs in the stateful three-tick cap-1/cap-2 traces. This retains the bounded no-op tick-5 selection after reactant exhaustion in the closure evidence rather than silently truncating at tick 4. Both arms remain rejected; pairwise closure is not RAF enumeration and `emergence-claim none`. Checks: `scripts/run_exp06.sh` (61 checks), `scripts/run_exp00.sh`, `git diff --check`.

- [x] 2026-07-12 14:30 progress: completed `cap-candidate-pool` maximum semantics for every smaller non-empty source pool under requested caps 2-8. This fills 27 missing PeTTa-native clauses (for example cap-7 over two candidates) and keeps generic deterministic selection/chamber ticking valid across the full bounded matrix. Exp00 provenance coverage verifies exact cap-7/two-candidate preservation and selection by actual cardinality. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `4ef39b9` pushed to GitHub `main`.

- [x] 2026-07-12 12:30 progress: added PeTTa-native `candidate-selection-from-pool`, an inspectable provenance atom containing the requested cap, exact bounded list, and deterministic selected candidate consumed directly by generic chamber ticking. Its focused test exposed and fixed cap-8 over a smaller three-candidate external pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `8c68755` pushed to GitHub `main`.

- [x] 2026-07-12 10:30 progress: exposed generic PeTTa-native `selected-candidate-from-pool`, making the exact cap -> actual bounded cardinality -> deterministic seed/tick selection inspectable before chamber firing. Generic `chamber-tick-candidate-pool` now delegates through this seam; exp00 covers ordinary cap-2 and cap-8 over a smaller three-rule generated pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `e5b7502` pushed to GitHub `main`.

- [x] 2026-07-12 08:30 progress: added generic PeTTa-native `chamber-tick-candidate-pool` and `chamber-tick-generated` operations that dispatch deterministic selection by the actual bounded pool cardinality (1-8), removing the need for callers to choose cap-specific tick functions. Focused exp00 coverage proves ordinary cap-2 equivalence and cap-8 safely ticking a smaller generated three-rule pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `4477baf` pushed to GitHub `main`.

- [x] 2026-07-12 06:30 progress: completed base exp00 bounded candidate generation for five- and seven-rule chambers, filling the last source-pool cardinality gaps through eight rules. Added direct generation tests plus a productive generated cap-5 chamber tick; also corrected cap-1 smoke fixtures to use the two-field `candidate-cap` schema and an explicitly productive external pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `511a63f` pushed to GitHub `main`.

- [x] 2026-07-12 04:30 progress: completed direct candidate-pool chamber ticking for cap 1, closing the cap-specific operation matrix across caps 1-8. Added `chamber-tick-candidate-pool-1` and `chamber-tick-generated-1` plus focused external/generated pool tests. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

- [x] 2026-07-12 02:30 progress: completed `cap-candidate-pool` coverage for every valid cap/pool-size combination through eight candidates. This closes bounded-generation holes on the direct candidate-pool-to-chamber-tick path, including cap-1 over eight candidates and cap-6 over seven. Added focused exp00 boundary tests. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

- [x] 2026-07-12 00:30 progress: generalized the direct PeTTa-native candidate-pool-to-chamber-tick operation from cap 2 to caps 3 through 8. `src/chem_exp00.metta` now exposes `chamber-tick-candidate-pool-3` through `-8`, and every generated cap-specific tick delegates through the same cap -> deterministic seed/tick selection -> firing path. Added the missing exact seven-candidate cap clause discovered by the new delegation and direct exp00 tests for cap-3/cap-6 pool ticking. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

- [x] 2026-07-11 22:30 progress: added direct PeTTa-native `chamber-tick-candidate-pool-2`, combining candidate-pool cap, deterministic seed/tick selection, and chamber firing. `chamber-tick-generated-2` delegates to it, and exp05 affinity treatment/control ticks now hand scored pools directly into the kernel operation. Exp00 equivalence plus exp05/exp07 checks pass; no scientific claim changed. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `git diff --check`.

- [x] 2026-07-11 20:30 progress: broadened exp07 productive affinity selector provenance from eighteen to twenty seeds. Added seed-25/26 PeTTa fixtures spanning first/second candidate phases, bounded cap-2 deterministic selection, and direct ordinary exp00 chamber ticks with productive treatment/control catalysts. Boundary remains selector provenance only: no frequency/ACS uplift, terminal forcing, or emergence claim. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `git diff --check`.

- [x] 2026-07-11 16:30 progress: broadened exp07's productive affinity seed-variation provenance from sixteen seeds to eighteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-23` and `seed-24`; `src/chem_exp05.metta` adds seed-23/tick-3 first-candidate treatment/control fixtures and seed-24/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: eighteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ca52b37` pushed to GitHub `main`.

- [x] 2026-07-11 14:30 progress: broadened exp07's productive affinity seed-variation provenance from fourteen seeds to sixteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-21` and `seed-22`; `src/chem_exp05.metta` adds seed-21/tick-3 first-candidate treatment/control fixtures and seed-22/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: sixteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `23c236d` pushed to GitHub `main`.

- [x] 2026-07-11 12:30 progress: broadened exp07's productive affinity seed-variation provenance from twelve seeds to fourteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-19` and `seed-20`; `src/chem_exp05.metta` adds seed-19/tick-3 first-candidate treatment/control fixtures and seed-20/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: fourteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `2f13a3e` pushed to GitHub `main`.

- [x] 2026-07-11 10:30 progress: broadened exp07's productive affinity seed-variation provenance from ten seeds to twelve while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-17` and `seed-18`; `src/chem_exp05.metta` adds seed-17/tick-3 first-candidate treatment/control fixtures and seed-18/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: twelve-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ae74ea0` pushed to GitHub `main`.

- [x] 2026-07-11 08:30 progress: broadened exp07's productive affinity seed-variation provenance from eight seeds to ten while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-15` and `seed-16`; `src/chem_exp05.metta` adds seed-15/tick-3 first-candidate treatment/control fixtures and seed-16/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: ten-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eb435e0` pushed to GitHub `main`.

- [x] 2026-07-11 06:30 progress: broadened exp07's productive affinity seed-variation provenance from six seeds to eight while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-13` and `seed-14`; `src/chem_exp05.metta` adds seed-13/tick-3 first-candidate treatment/control fixtures and seed-14/tick-3 second-candidate fixtures, all keeping the selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: eight-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `aecfab9` pushed to GitHub `main`.

- [x] 2026-07-11 04:30: broadened exp07's productive affinity seed-variation provenance from four seeds to six. `src/chem_exp00.metta` now defines `seed-11` and `seed-12`; `src/chem_exp05.metta` adds seed-11/tick-3 first-candidate fixtures and seed-12/tick-3 second-candidate fixtures whose selected catalysts remain productive after cap-2 deterministic selection; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks for the new treatment/control arms. Boundary: six-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `cc56750` pushed to GitHub `main`.

- [x] 2026-07-11 02:30: broadened exp07's productive affinity seed-variation provenance from three seeds to four. `src/chem_exp00.metta` now defines `seed-10`; `src/chem_exp05.metta` adds seed-10/tick-3 treatment/control fixtures whose cap-2 deterministic selector repeats the second-candidate phase (`e5r1`) with a distinct productive rotated-control catalyst context (`BC`); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks for the new treatment/control arms. Boundary: four-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eabc1be` pushed to GitHub `main`.

- [x] 2026-07-11 00:30: broadened exp07's productive affinity seed-variation provenance from two seeds to three. `src/chem_exp00.metta` now defines `seed-9`; `src/chem_exp05.metta` adds seed-9/tick-3 treatment/control fixtures whose cap-2 deterministic selector repeats the first-candidate phase with different productive catalyst contexts (`AC`/`BC`); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9. Exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks for all three treatment/control arms. Boundary: three-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `b34eae4` pushed to GitHub `main`.

- [x] 2026-07-10 22:30: added exp07's first two-seed productive affinity selector-phase variation. `src/chem_exp05.metta` now includes matched seed-8/tick-3 treatment/control fixtures where cap-2 selection chooses the second affinity-assigned source rule (`e5r1`), and `src/chem_exp07.metta` exposes `exp07-affinity-seed-variation-row`, `exp07-affinity-seed-variation-table`, and `exp07-affinity-seed-variation-status`. Exp07 smoke verifies seed-7 first-candidate and seed-8 second-candidate selected candidates plus direct ordinary exp00 chamber ticks for both treatment/control arms. Boundary: two-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `358bfbc` pushed to GitHub `main`.

- [x] 2026-07-10 20:30: added exp07's productive affinity selection-to-tick provenance trace. `src/chem_exp07.metta` now exposes `exp07-affinity-selection-to-tick-trace` and `exp07-affinity-selection-to-tick-status`, expanding the strength-1 seed-7/tick-3 cap-2 treatment/control pools, bounded cap lists, deterministic selected candidates, and ordinary exp00 chamber ticks. This directly verifies the selected weak-guidance candidates are the ones handed to chamber ticking in the productive fixture. Boundary: single-fixture provenance only, no seed/frequency claim, no ACS uplift, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `27e70fd` pushed to GitHub `main`.

- [x] 2026-07-10 18:30: added exp07's first affinity-strength productivity-filter slice. `src/chem_exp07.metta` now exposes `exp07-affinity-strength-sweep-row`, `exp07-affinity-strength-sweep-table`, and `exp07-affinity-strength-sweep-status`, varying exp05 affinity strength `(0 1 2)` in the seed-7/tick-3 cap-2 fixture. Strength 1 is the only tested value whose deterministic treatment/control selected catalysts are both present/productive in the current chamber fixture; strengths 0 and 2 select absent catalysts, so this is a bounded fixture filter before seed/frequency/ACS-uplift claims. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `d667c2b` pushed to GitHub `main`.

- [x] 2026-07-10 16:30: added exp07's first deterministic weak-guidance comparison table. `src/chem_exp07.metta` now exposes `exp07-weak-guidance-comparison-row`, `exp07-weak-guidance-comparison-table`, and `exp07-weak-guidance-comparison-status`: affinity weight records treatment/control chamber-tick differences through exp05/exp00 deterministic selection, while candidate-pool cap records exp06's stateful cap sweep plus ACS-boundary rejection. This is checked comparison evidence for deterministic path differences only; no terminal forcing, no ACS-positive result, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `6c64348` pushed to GitHub `main`.

- [x] 2026-07-10 14:30: linked exp07's Doob-h weak-guidance policy to existing PeTTa-native dynamic evidence. `src/chem_exp07.metta` now exposes `exp07-weak-guidance-evidence-row`, `exp07-weak-guidance-evidence-table`, and `exp07-weak-guidance-probe-status`: affinity weight is connected to exp05 treatment/control chamber ticking through the exp00 selector, and candidate-pool cap is connected to exp06's three-tick stateful cap sweep plus ACS-boundary table. The boundary remains no terminal forcing, no ACS-positive result, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `0fe6f81` pushed to GitHub `main`.

- [x] 2026-07-10 12:30: Advanced exp07 from scaffold to a first PeTTa-native Doob-h diagnostic policy slice. `src/chem_exp07.metta` now exposes `exp07-doob-h-table`, ranked `exp07-doob-policy-order`, and `exp07-weak-guidance-test-plan`: catalyst assignment is the strongest terminal-fixture diagnostic; affinity weight and candidate-pool cap are weak-guidance variables to test without fixing the terminal state; basal replenishment and catalysis-map offset remain context/control variables. `experiments/exp07/smoke.metta` and README verify/document the policy and preserve `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `8bca457` pushed to GitHub `main`.

- [x] 2026-07-10 11:00: Completed exp06 bridge-to-ACS consolidation. `src/chem_exp06.metta` now exposes `exp06-consolidation-summary`: cap-1/cap-2 are rejected by two-rule product-catalyst closure across refreshed, stateful two-tick, and stateful three-tick sweeps; catalyst assignment is the cost-1 shortest RAF-positive path; basal-only is RAF-negative; candidate-cap is dynamic-test-required but consolidated as `not-acs-positive`; catalysis-map offsets are offset-sensitive; emergence claim remains none. Commit `06f7371` pushed to GitHub `main`.

- [x] exp07 Schrödinger-bridge/Doob-h-transform diagnostic experiment family
  (completed through the frozen dual-bootstrap result and bounded mechanism
  audit; final guided-uplift result negative, `emergence-claim none`):
  1. Treat exp02/exp04 no-catalysis controls as verified ACS-negative initial states.
  2. Treat the exp04 ACS-rich fixture as terminal state (maximal RAF 15, greedy core 2, `(lCD lBCD2)`).
  3. Search over intervention-cost vectors: catalyst assignment, basal-food replenishment, candidate-pool cap, catalysis-map offset, and exp05 affinity weight.
  4. Use Schrödinger-bridge/Doob-h-transform framing from Ben's "Let's Get Chemical" post as the main diagnostic search strategy.
  5. Keep old ACS scanners as validation/control infrastructure and preserve `emergence-claim none`.

- [x] 2026-07-10 10:30 progress: attached an ACS boundary check to exp06's PeTTa-native stateful candidate-cap sweep. `src/chem_exp06.metta` now checks selected tick-3/tick-4 rule pairs with `exp06-selected-candidate-pair-acs-status`, exposes cap-1/cap-2 `exp06-stateful-cap-sweep-acs-boundary` rows, and aggregates them in `exp06-stateful-cap-sweep-acs-boundary-table`. Both cap arms are rejected by two-rule product-catalyst closure, so this is dynamic bounded evidence for the candidate-cap intervention but not RAF enumeration or an emergence claim. `experiments/exp06/smoke.metta` and README verify/document the boundary. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and targeted secret-like diff scan. Commit `40aef6b` pushed to GitHub `main`.

- [x] 2026-07-10 08:30 progress: extended exp06's PeTTa-native stateful candidate-cap sweep from two selected ticks to three. `src/chem_exp06.metta` now carries the tick-3/tick-4 stateful cap-1 and cap-2 chambers into tick 5, adds a bounded no-op `chamber-tick-with-candidate` clause for exhausted `A`, and records `exp06-candidate-cap-stateful-three-tick-sweep`. Tick 5 selects `e5r0` in both arms but advances without negative abundance or new events; the cap-1/cap-2 divergence from tick 4 persists. `experiments/exp06/smoke.metta` verifies tick-5 selection, final no-op chambers, and the aggregate boundary (`three-tick-stateful-diagnostic-not-raf-status`, `emergence-claim none`); README documents the diagnostic. Checks: `scripts/run_exp00.sh`, `scripts/run_exp06.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `de84704` pushed to GitHub `main`.

- [x] 2026-07-10 06:30 progress: advanced exp06 from refreshed cap diagnostics to a PeTTa-native accumulated/stateful two-tick cap sweep. `src/chem_exp06.metta` now carries the seed-7 tick-3 chamber output into tick 4 for cap-1/cap-2 arms, using exp05 affinity-assigned source rules and ordinary exp00 candidate selection/ticking. Cap-1 repeats `e5r0` across ticks 3-4, while cap-2 exposes `e5r1` at tick 4, yielding distinct final abundance/event paths. `experiments/exp06/smoke.metta` verifies selected candidates, carried final chambers, and the aggregate `exp06-candidate-cap-stateful-two-tick-sweep` boundary: accumulated diagnostic only, not RAF status or an emergence claim. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `63ed5c3` pushed to GitHub `main`.

- [x] 2026-07-10 04:30 progress: Extended exp06's candidate-pool-cap dynamic probe into a PeTTa-native refreshed two-tick cap sweep. `src/chem_exp06.metta` now exposes tick-4 cap-1/cap-2 treatment and rotated-control diagnostic chambers, selected candidates, after-tick chambers, and an aggregate `exp06-candidate-cap-two-tick-sweep`; cap-2 deterministically exposes/fires the second exp05 source rule at seed-7/tick-4 while cap-1 stays pinned to the first rule. `experiments/exp06/smoke.metta` verifies the sweep and preserves the boundary `refreshed-two-tick-diagnostic-not-raf-status` with next target `accumulated-multi-tick-stateful-sweep`. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `5240172` pushed to GitHub `main`.

- [x] 2026-07-10 02:30 progress: Tightened exp06's candidate-pool-cap dynamic probe with matched rotated-control chamber ticking. `src/chem_exp06.metta` now exposes cap-1/cap-2 treatment and control selected candidates plus after-tick chambers, all routed through exp05 affinity assignment and ordinary exp00 `chamber-tick-with-candidate`; both arms remain productive for the first tick, and the comparison atom records `single-tick-productivity-not-raf-status` with next test `multi-tick-cap-sweep`. `experiments/exp06/smoke.metta` and README verify/document the treatment-control probe. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `e5a6285` pushed to GitHub `main`.

- [x] 2026-07-10 00:30 progress: Started evaluating exp06's candidate-pool-cap intervention dynamically while keeping the chemistry kernel PeTTa-native. `src/chem_exp06.metta` now exposes cap-1 and cap-2 candidate-cap dynamic probes that reuse exp05 affinity-assigned candidates and ordinary exp00 chamber ticking; both select the same `e5r0` affinity candidate at seed-7/tick-3 and preserve the same productive first tick. `experiments/exp06/smoke.metta` verifies selected candidates, after-tick chambers, probe atoms, and the comparison boundary (`raf-status not-yet-evaluated`, next test `multi-tick-cap-sweep`); README documents the boundary. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `7d047c9` pushed to GitHub `main`.

- [x] 2026-07-09 23:00 progress: Added a thin host-side Dijkstra/artifact slice over the PeTTa-exposed exp06 bounded intervention table. `scripts/write_exp06_bridge_path_files.py` queries the six `exp06-intervention-cost-row` atoms, uses them as path-search nodes/edges without implementing chemistry, and writes CONFIG/NODE_EVALUATIONS/PATHS/SUMMARY/RUN.md artifacts under `artifacts/exp06_bridge_path_search` by default. `scripts/test_exp06_bridge_path_files.sh` verifies the selected shortest strict RAF-positive path (`catalyst-assignment none->specific-template`), broad-template and shuffled-9 alternates, candidate-cap dynamic-test-required status, and no-emergence caveats. Checks: `python3 -m py_compile scripts/write_exp06_bridge_path_files.py`, `scripts/test_exp06_bridge_path_files.sh`, `scripts/write_exp06_bridge_path_files.sh`, `scripts/run_exp06.sh`, `git diff --check`, and obvious secret-like diff scan.

- [x] 2026-07-09 22:30 progress: Deepened exp06 from a single one-step witness into a PeTTa-queryable bounded cost/path table over the named intervention variables. `src/chem_exp06.metta` now exposes cost-1 rows for catalyst assignment (specific/broad positives), basal-food replenishment (RAF-negative alone), candidate-pool cap (dynamic-test-required/not-yet-evaluated), and catalysis-map offsets (shuffled-1 RAF-negative, shuffled-9 offset-sensitive RAF-like), plus aggregate bounded-path/status atoms. `experiments/exp06/smoke.metta` verifies the table while preserving `emergence-claim none`; README documents the bounded table. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d18bdb7` pushed to GitHub `main`.

- [x] 2026-07-09 20:30 progress: Started the exp06 bridge-to-ACS favorable-conditions scaffold in PeTTa atoms. `src/chem_exp06.metta` now names the initial verified no-ACS source row (`hand-designed/none/basal-4`) and terminal exp04 RAF-rich fixture (`hand-designed/specific/basal-4`, maximal RAF 15, greedy core `(lCD lBCD2)`), lists intervention variables spanning exp05 affinity assignment, basal replenishment, candidate-pool caps, and catalysis-map offset, and records a first deterministic one-step shortest-path witness from no catalysis to the specificity-template condition. Added `experiments/exp06/smoke.metta`, `scripts/run_exp06.sh`, and README coverage. No spontaneous-emergence claim is made; path construction is diagnostic bookkeeping. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `2d146d5` pushed to GitHub `main`.

- [x] 2026-07-09 16:30 progress: Triaged and advanced the pre-existing exp05 scaffold into tracked PeTTa-native smoke coverage. `src/chem_exp05.metta` now defines generic token-overlap catalyst affinity with a positive baseline, a rotated-weight control, source-rule catalyst assignment, and projection of affinity-assigned rules into ordinary exp00 `candidate`/`candidate-pool` atoms so bounded caps can be reused by later chamber-ticking slices. Added/verified `experiments/exp05/smoke.metta`, `scripts/run_exp05.sh`, and README coverage. No RAF scan or emergence claim is made. Checks: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan.

- [x] 2026-07-09 18:30 progress: Connected exp05 affinity-assigned candidate pools into a minimal chamber-ticking slice with matched rotated controls. The new PeTTa-native path is source rules -> affinity assignment -> cap-2 bounded pool -> existing exp00 seed/tick deterministic selector -> ordinary `chamber-tick-with-candidate`; smoke tests verify treatment/control selected candidates, chamber transitions, and a status atom preserving `raf-scan not-yet-run` / `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `f1fecec` pushed to GitHub `main`.

- [x] 2026-07-09 14:30 progress: Added the cap-8 productive bundle to the thin exp03 artifact writer. `scripts/write_exp03_productive_cap_files.py` now queries `(exp03-cap8-productive-file-bundle seed-13 random-polymer)` and emits `exp03-cap8-productive-seed-13-random`; `scripts/test_exp03_productive_cap_files.sh` verifies the new run directory, RUN.md source expression, config, first rr5 event, dynamic-event-count metric, and summary. README documents cap-8 writer coverage. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d9d5bc3` pushed to GitHub `main`. Pre-existing untracked exp05 scaffold files were left untouched.

- [x] 2026-07-09 12:30 progress: Carried the PeTTa-native cap-8 seam into exp03 accumulated chamber ticking and productive-cap records. `src/chem_dynamics.metta` now has `chamber-tick-generated-8-accum`, `chamber-run-8cap-*` through 16 ticks, a seed-13/R-family cap-8 fixture over all eight exp02 source rules, bounded rr7 no-op handling for the eighth candidate outside the 17-molecule state, and run-record/export/file-bundle atoms. Exp03 smoke verifies eight-candidate generation, deterministic rr5 initial selection, rr7 no-op ticks, 14 productive events over 16 ticks, replay/final-abundance/completeness, trace order, and export/file-bundle sections. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `bae69e6` pushed to GitHub `main`.

- [x] 2026-07-09 10:30 progress: Extended the PeTTa-native exp00 deterministic selection/generation seam to cap-8/full eight-rule pools. `src/chem_exp00.metta` now has `seeded-choice-8`, `select-candidate-8`, `selected-candidate-from-list-8`, `chamber-tick-generated-8`, `exp00-candidate-cap-8`, and a cap-8 clause preserving all eight generated candidates. Exp00 smoke covers seed/tick choice, cap construction, cap-8 candidate-pool preservation, direct eight-way selection, and generated chamber ticking where seed-7 selects the productive eighth candidate. Checks: `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `3506bc0` pushed to GitHub `main`.

- [x] 2026-07-09 08:30 progress: Added a thin exp04 offset-sensitivity report writer/test. `scripts/write_exp04_offset_report_files.py` queries the PeTTa-side offset report and summary file atoms and writes `OFFSET_SENSITIVITY_REPORT.metta`, `SUMMARY.metta`, and `RUN.md`; `scripts/test_exp04_offset_report_files.sh` verifies the generated offset partitions, representative cores, and no-unbiased-emergence claim. README now documents the writer. Checks: `python3 -m py_compile scripts/write_exp04_offset_report_files.py`, `scripts/test_exp04_offset_report_files.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `14d12f0` pushed to GitHub `main`.

- [x] 2026-07-09 06:30 progress: Added compact PeTTa-queryable exp04 offset-sensitivity report/export atoms for the full rotated-shuffle sweep. `src/chem_exp04.metta` now exposes `exp04-offset-sensitivity-report-row` rows for hand-designed, mechanically generated template, and cross-template pools; `exp04-offset-sensitivity-claim`; file-style report/summary atoms; and `exp04-offset-sensitivity-report-complete?`. Exp04 smoke verifies the exact negative/RAF-like offset partitions and report bundle, preserving the no-unbiased-emergence interpretation. Checks: `scripts/run_exp00.sh`, `scripts/run_exp04.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `2290218` pushed to GitHub `main`.

- [x] 2026-07-09 04:30 progress: Completed the exp04 rotated-shuffle offset sweep for offsets 1 through 9 by adding `shuffled-3`, `shuffled-4`, `shuffled-7`, and `shuffled-8`. The reduction artifact/report now has 108 rows; PeTTa report atoms expose all new rows, `exp04-reduction-shuffle-offsets-1-through-9-tested?`, and representative minimized-core atoms for new RAF-like controls. Result: hand-designed offsets 3/7 are RAF-negative at basal-4, while 4/8 are RAF-like; generated-template offset 4 is RAF-like; cross-template offsets 3/7 are RAF-like and 4/8 are RAF-negative, reinforcing the catalysis-map-sensitive/no-unbiased-emergence interpretation. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `c4f69db` pushed to GitHub `main`.

- [x] 2026-07-09 02:30 progress: Added exp04 rotated-shuffle negative controls `shuffled-2` and `shuffled-6`, expanding the reduction artifact/report from 54 to 72 rows. PeTTa report atoms now expose the added rows, `exp04-reduction-shuffle-negative-offsets-tested?`, and representative `exp04-reduction-minimized-core-rules` for baseline and shuffled RAF-like controls. Result: offsets 2 and 6 are RAF-negative at basal-4 across hand-designed, mechanically generated template, and cross-template pools (maximal RAF 0), sharpening the catalysis-map/offset-sensitivity caveat while preserving the positive inspectable baseline. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `6f7a5ba` pushed to GitHub `main`.
- [x] 2026-07-09 00:30 progress: Broadened exp04 catalysis-map shuffle controls from one rotated offset to three (`shuffled`, `shuffled-1`, `shuffled-9`). The reduction sweep artifact now has 54 rows; PeTTa-side report atoms expose all new rows, `exp04-reduction-alt-shuffle-offsets-tested?`, and an offset-sensitive interpretation. Key result: hand-designed `shuffled-1`/basal-4 is RAF-negative (0/core 0) while `shuffled-9`/basal-4 remains RAF-like (7/core 3), and generated pools still show offset-dependent small RAF-like shuffle artifacts, so the positive exp04 fixture remains catalysis-map-sensitive rather than an unbiased emergence claim. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `f65c430` pushed to GitHub `main`.
- [x] 2026-07-08 22:30 progress: Added a stricter `mechanically-generated-cross-template` exp04 reduction-control pool to test generated-pool/catalysis-map bias. The reduction sweep now has 36 rows; cross-template specific/broad/none controls stay RAF-negative (maximal RAF 0), but shuffled cross-template catalysis creates a small RAF-like signal (maximal RAF 5/core 1), so the PeTTa-side interpretation explicitly records both cross-template broad RAF-negative and shuffled cross-template RAF-like-created findings while preserving the no-unbiased-emergence claim. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `1a8b2c2` pushed to GitHub `main`.
- [x] 2026-07-08 20:30 progress: Moved exp04 reduction-sweep summaries into PeTTa-queryable report atoms. `src/chem_exp04.metta` now exposes the 24-row reduction table, baseline/control predicates, interpretation atom, and report completeness check; exp04 smoke verifies baseline positive, no-catalysis controls RAF-negative, generated-specific controls RAF-negative, shuffled hand-designed RAF-like caveat, and the explicit no-unbiased-emergence interpretation. Checks: `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `0ed265e` pushed to GitHub `main`.
- [x] 2026-07-08 18:30 progress: Ran the first exp04 reduction sweep around the rich RAF fixture. Added `experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, and artifact `experiments/exp04_reduction_sweep_20260708/` with 24 deterministic variants over catalysis mode, basal interval, and hand-designed versus mechanically generated template pools. Baseline hand-designed/specific/basal-4 remains maximal RAF 15/core 2/56 events/15-rule event diversity; no-catalysis controls have maximal RAF 0; shuffled hand-designed catalysis still leaves maximal RAF 10/core 3, preserving the success-biased/catalysis-map-sensitive caveat. Checks: `python3 -m py_compile experiments/exp04/run_rich_raf.py experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`.
- [x] 2026-07-08 exp04: Created and verified a deliberately success-biased rich RAF chemistry on branch `agent/exp04-rich-chemistry`. Exp04 combines 8 ligation, 6 cleavage, and 6 modification rules over food `A/B/C/D`, specificity-filtered template catalysis, 56 ticks with food floor 3, PeTTa smoke coverage, and a host-computed RAF/dynamics harness. Artifact `experiments/exp04_rich_raf_20260708/` reports maximal RAF size 15, greedy core size 2 (`lCD`, `lBCD2`), core RAF true, no-catalysis RAF size 0, and 56 events over 56 ticks. Checks: `python3 -m py_compile experiments/exp04/run_rich_raf.py`, `scripts/run_exp04.sh`, host rerun, `git diff --check`.
- [x] 2026-07-08 16:30 progress: broadened productive-cap artifact/export coverage to include the cap-7 seed-13/R-family productive run. `src/chem_dynamics.metta` now exposes `exp03-cap7-productive-run-export` and `exp03-cap7-productive-file-bundle` and includes cap-7 in productive-cap export/bundle completeness checks; exp03 smoke verifies config, 14 events, ACS candidates, file-bundle id, metrics, ACS section, and summary. The thin writer emits `exp03-cap7-productive-seed-13-random` from `(exp03-cap7-productive-file-bundle seed-13 random-polymer)`, and the shell test verifies generated files plus provenance. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `79f9090` pushed to GitHub `main`.
- [x] 2026-07-08 14:30 progress: extended cap-7 from the exp00 kernel seam into exp03 productive dynamics. `src/chem_exp00.metta` now supports 17-molecule state tick/seed access and eight-rule generated candidate pools; `src/chem_dynamics.metta` adds cap-7 accumulated chamber ticking/run wrappers plus a seed-13/R-family productive cap-7 chamber with R16 in-state and explicit rr0-rr6 tick clauses. Exp03 smoke verifies bounded seven-candidate generation, deterministic tick-0 rr6 selection via `(13+0)%7 = 6`, 14 productive events over 14 ticks, final abundance/replay/completeness, and exact trace order. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`. Commit `500b2c5` pushed to GitHub `main`.
- [x] 2026-07-08 12:30 progress: extended the PeTTa-native exp00 deterministic selection/generation seam to cap-7. `src/chem_exp00.metta` now has `seeded-choice-7`, `select-candidate-7`, `selected-candidate-from-list-7`, `chamber-tick-generated-7`, `exp00-candidate-cap-7`, and cap-7 truncation from eight-candidate pools. Exp00 smoke covers seed/tick choice, cap atom construction, truncation, direct seven-candidate selection, and generated cap-7 chamber ticking over an eight-rule pool. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `9d5f89b` pushed to GitHub `main`.
- [x] 2026-07-08 10:30 progress: packaged the compact exp02 cycle-scan report as PeTTa-queryable artifact exports. `src/chem_exp02.metta` now exposes `(exp02-cycle-scan-report-bundle)` with `CYCLE_SCAN_REPORT.metta` and `SUMMARY.metta` run-file atoms plus bundle accessors/completeness checks; exp02 smoke verifies the exact bundle. Added a thin writer/test pair (`scripts/write_exp02_cycle_report_files.py`, `.sh`, `scripts/test_exp02_cycle_report_files.sh`) that queries local PeTTa/SWI and writes only the returned report atoms plus `RUN.md` provenance. Checks passed: `scripts/run_exp02.sh`, `python3 -m py_compile scripts/write_exp02_cycle_report_files.py`, `scripts/test_exp02_cycle_report_files.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `1535435` pushed to GitHub `main`.
- [x] 2026-07-08 08:30 progress: broadened the thin productive-cap artifact writer to include the seed-17/S-family cap-6 productive run. `scripts/write_exp03_productive_cap_files.py` now emits five PeTTa-queried bundles, adding `exp03-cap6-productive-seed-17-random` from `(exp03-cap6-productive-file-bundle seed-17 random-polymer)`. `scripts/test_exp03_productive_cap_files.sh` verifies the generated run directory, output-root `RUN.md` provenance, `CONFIG.metta`, first `EVENTS.metta` event, dynamic event-count metric, and summary. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `147633d` pushed to GitHub `main`.
- [x] 2026-07-08 06:30 progress: extended productive cap-6 to a third PeTTa-tested seed/state shape, seed-17/S-family. `src/chem_dynamics.metta` now has a 16-molecule seed-17 productive cap-6 chamber with S89/S05 in-state, explicit rr0-rr5 accumulated ticking clauses, final abundance/replay/run-record/export/file-bundle atoms, and ACS provenance from `exp02-seed-17-acs-candidates`. Exp03 smoke verifies bounded six-candidate generation, tick-0 sixth-candidate selection via `(17+0)%6 = 5`, 12 productive events over 12 ticks, final abundance/replay/completeness, exact trace order, and export/file-bundle sections. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `ee89855` pushed to GitHub `main`.
- [x] 2026-07-08 04:30 progress: added a compact cycle-scan summary report atom for human-readable exp02 provenance. `src/chem_exp02.metta` now has `exp02-cycle-scan-summary-report` rows for generated-unplanted k=4..7 scans (40 sweep points, 120 family records, 0 active cycles for each size) plus `exp02-cycle-scan-summary-report-complete?`; exp02 smoke verifies the exact atom. `experiments/exp02_small_sweep_20260630/SUMMARY.md` now mirrors the compact k=4..7 table. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `5cc2d24` pushed to GitHub `main`.
- [x] 2026-07-08 02:30 progress: broadened the productive-cap artifact/export bundle to include the seed-13/R-family cap-6 productive run. `src/chem_dynamics.metta` now includes seed-13 in `exp03-productive-cap-run-exports` and PeTTa-side `run-file-bundle` projections; exp03 smoke verifies seed-13 export config/events/ACS and file-bundle events/metrics/ACS/summary. `scripts/write_exp03_productive_cap_files.py` now emits four bundles, adding `exp03-cap6-productive-seed-13-random`, and the shell test verifies its generated section files plus `RUN.md` provenance. Checks: `scripts/run_exp03.sh`, `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `2c04300` pushed to GitHub `main`.
- [x] 2026-07-08 00:30 progress: extended productive cap-6 beyond the seed-11/Q-family fixture to seed-13/R-family while keeping the chemistry kernel PeTTa-native. `src/chem_exp00.metta` now supports tick/seed/candidate generation for 16-molecule, eight-rule states; `src/chem_dynamics.metta` adds a 16-molecule seed-13 productive cap-6 chamber with R89/R05 present, explicit rr0-rr5 accumulated ticking, final abundance/replay/run-record atoms, and source ACS provenance; exp03 smoke proves bounded six-candidate generation, deterministic selection, 12 productive events over 12 ticks, final abundance, replay, completeness, and exact trace order. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `dd941d0` pushed to GitHub `main`.
- [x] 2026-07-07 22:30: Added compact artifact `RUN.md` provenance to the exp03 productive-cap file writer. The thin Python harness now writes an output-root `RUN.md` documenting source PeTTa run-file bundle expressions, reproduction commands, and the v0.1 per-run file sections for cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11; the shell test verifies the provenance file and generated section files. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `7521d09` pushed to GitHub `main`.
- [x] 2026-07-07 20:30: Connected productive-cap file bundles to a thin artifact writer. `src/run_contract.metta` now exposes all v0.1 run-file sections via PeTTa-side accessors; run-contract smoke covers manifest/abundances/metrics/ablations and exp03 smoke covers metrics/ACS file sections for the cap-6 productive bundle. Added `scripts/write_exp03_productive_cap_files.py` plus shell/test wrappers to query local PeTTa/SWI for cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 bundles and write per-run `CONFIG.metta` through `SUMMARY.metta` files. Checks: `scripts/run_contract.sh`, `scripts/run_exp03.sh`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `948da77` pushed to GitHub `main`.
- [x] 2026-07-07 18:30: Added PeTTa-side file-section/query hooks for v0.1 run-contract records. `make-run-file-bundle` now turns any run-record into named `run-file` sections (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `ABUNDANCES.metta`, `METRICS.metta`, `ACS.metta`, `ABLATIONS.metta`, `SUMMARY.metta`) with accessors for bundle id/files and focused config/events/summary file queries. Productive cap fixtures now expose cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 file bundles. Checks: `scripts/run_contract.sh` (32 ✅), `scripts/run_exp03.sh` (415 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`. Commit `fa5cbd6` pushed to GitHub `main`.
- [x] 2026-07-07 16:30: Added PeTTa-side export/query hooks for productive cap fixtures. `make-run-export` now has field accessors for config, manifest, abundances, ACS candidates, and ablations in addition to events/metrics/summary; cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 run records now expose run-export projections plus a compact productive-cap export bundle/completeness predicate. Exp03 smoke covers config/event/abundance/ACS/ablation export fields and the bundle. Checks: `scripts/run_exp03.sh` (410 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`, and obvious secret-like diff scan. Commit `3d476b6` pushed to GitHub `main`.
- [x] 2026-07-07 14:30: Made the cap-6 sixth candidate productive in-state for seed-11/Q-family. Added 15-molecule six-rule candidate-pool support in exp00 plus a wider Q-family productive cap-6 bridge with Q05/Q16/Q99, explicit rr0-rr5 accumulated ticking clauses, run-record/replay/metrics atoms, and exp03 smoke coverage proving tick-0 rr5 selection via `(11+0)%6 = 5`, 12 productive events over 12 ticks, final Q05/Q16 abundances, replay, completeness, and exact trace order. Checks: `scripts/run_exp03.sh` (404 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`, and obvious secret-like diff scan. Commit `0d03f4c` pushed to GitHub `main`.
- [x] 2026-07-07 12:30: Extended cap-6 from the exp00 seam into exp03 rich dynamics over seed-11/Q-family. Added `chamber-tick-generated-6-accum`, 6-cap run wrappers through 12 ticks, rr5/sr5/nr5 no-op handling for the sixth source-rule candidate outside the 12-molecule rich state, and cap-6 run-record/replay/metrics atoms. Exp03 smoke proves a full six-rule capped pool, tick-0 rr5 selection via `(11+0)%6 = 5`, 7 productive events over 12 ticks, final abundance snapshot, replay, completeness, and trace order. Checks: `scripts/run_exp03.sh` (390 ✅), `scripts/run_exp00.sh` (81 ✅), `git diff --check`, and obvious secret-like diff scan. Commit `e31bc31` pushed to GitHub `main`.
- [x] 2026-07-07 08:30: Made the cap-5 fifth candidate productive in-state for seed-13/R-family. Added 15-molecule state support for generated eight-rule candidate pools, a seed-13 productive cap-5 chamber with R8/R9/R89 present, explicit rr0-rr4 accumulated ticking clauses, run-record/replay/metrics atoms, and exp03 smoke coverage proving bounded candidates rr1/rr0/rr2/rr3/rr4, tick-0 rr3 selection via `(13+0)%5 = 3`, productive rr4 events at ticks 1 and 6, 10 total events over 10 ticks, final abundance snapshot, replay, completeness, and trace order. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `db6cff6` pushed to GitHub `main`.
- [x] 2026-07-07 06:30: Extended cap-5 beyond the seed-11/Q-family bridge into the seed-17/S-family richer 12-molecule state. Added seed-17 cap-5 rich chamber/run-record atoms over the eight-rule source pool, bounded candidates rr1/rr0/rr2/rr3/rr4, deterministic tick-0 selection of rr2 via `(17+0)%5 = 2`, rr4 no-op handling for random/shuffled/no-catalysis fifth candidates outside the state shape, and exp03 smoke coverage for random/shuffled/no-catalysis event counts (11/8/0), tick 15, abundances, replay, discrimination, completeness, and trace events. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `129c170` pushed to GitHub `main`.
- [x] 2026-07-07 04:30: Extended the cap-5 seed-11/Q-family exploratory seam into PeTTa-native multi-tick rich dynamics. Added `chamber-tick-generated-5-accum`, cap-5 run wrappers through 15 ticks, Q-family rr4/sr4/nr4 no-op distractor clauses for the 12-molecule rich state, 15-tick cap-5 run-config/manifest/metrics/summary/ACS/run-record atoms, and exp03 smoke coverage for random/shuffled/no-catalysis event counts (10/8/0), abundance snapshots, replay, discrimination, completeness, and trace events. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and obvious secret-like diff scan.
- [x] 2026-07-07 02:30: Added PeTTa-native cap-5 deterministic selection/generation seams. `src/chem_exp00.metta` now has `seeded-choice-5`, `select-candidate-5`, `selected-candidate-from-list-5`, `chamber-tick-generated-5`, `exp00-candidate-cap-5`, and 5-candidate cap clauses for 5/6/8-rule pools; exp00 smoke covers seeded choice, cap construction/truncation, and deterministic cap-5 selection. Added an exp03 seed-11/Q-family cap-5 exploratory seam proving a six-rule rich source pool is bounded to five candidates and selects index 1 at tick 0. Checks: `scripts/run_exp00.sh` (75 ✅), `scripts/run_exp03.sh` (354 ✅), `git diff --check`, and obvious secret-like diff scan. Commit `39cc96d` pushed to GitHub `main`.
- [x] 2026-07-07 10:30: Started cap-6 by wiring deterministic selection/caps directly into exp00 chamber ticking over generated six-rule pools.
- [x] Extend productive cap-6 beyond seed-11/Q-family or add PeTTa-side export hooks for the cap-5/cap-6 productive fixtures. Completed with PeTTa-side run-export projections/accessors for cap-5/cap-6 productive fixtures on 2026-07-07 16:30.
- [x] Add PeTTa-side file-emission/query hooks if the runtime exposes a cleaner non-verbose atom export path. Completed with PeTTa-side run-file bundles on 2026-07-07 18:30 and a tested thin exp03 productive-cap artifact writer on 2026-07-07 20:30.

## Recently completed

- [x] 2026-07-06 20:30 — Commit `fa9a89f` extended the cap-4 rich bridge to seed-17 using the generated S-family 12-molecule state (S0-S7, S01/S10, S45/S54). The random-polymer path exercises all four cap-4 rules for 12 productive events over 12 ticks; shuffled-catalysts records 8 events due to catalyst depletion/blocking, and no-catalysis stays at 0 events. Added seed-17 bridge/run-record atoms plus exp03 smoke coverage for event counts, abundances, replay, control discrimination, and run-record completeness. Checks: exp00 ✅, exp03 ✅, `git diff --check`, and obvious secret-like scan. Commit `3d476b6` pushed to GitHub `main`.

- [x] 2026-07-06 17:15 — Added cap-4 rich bridge for seed-13: a 12-molecule multi-rule productive state where ALL FOUR cap-4 rules (rr0, rr1, rr2, rr3) fire productively under random-polymer catalysis. Initial state: R0=3, R1=3, R2=3, R3=3, R4=3, R5=3, R6=3, R7=3, R01=0, R10=1, R45=0, R54=1. The deterministic selector cycles (13+tick)%4 = 1,2,3,0,1,2,3,0,... so rr0 fires at tick 0, rr2 at tick 1, rr3 at tick 2, rr1 at tick 3, repeating for 3 full rounds (12 productive events total, all reactants R0-R7 exhausted by tick 11). For shuffled-catalysts: rr0 fires (cat R2 present), rr2 fires (cat R6 present), but rr3 is no-op (cat R8 absent) and rr1 only fires twice (cat R4 is consumed by rr2, so the 3rd rr1 is blocked) → 8 events. No-catalysis: 0 events. Control discrimination: random (12) > shuffled (8) > no-catalysis (0). Required adding: (1) `seeded-choice-4`, `select-candidate-4`, `selected-candidate-from-list-4`, `chamber-tick-generated-4`, `chamber-tick-generated-4-accum`, `exp00-candidate-cap-4` in chem_exp00.metta, (2) `cap-candidate-pool 4` clause for 8-element pools, (3) 12-molecule `generate-candidate-pool`, `state-tick`, `state-seed`, `state-abundance-snapshot` clauses, (4) extended `append-event` to 12 existing events and `event-count` to 12 events, (5) `chamber-run-4cap-1` through `chamber-run-4cap-12` and `chamber-run-4cap-15` wrappers, (6) 15 new `chamber-tick-with-candidate-accum` clauses for the 12-molecule state (3 productive + 3 productive + 3 no-op + 3 productive + 3 no-op for rr0/rr1/rr2/rr3 × random/shuffled/no-catalysis), (7) full run-config/manifest/metrics/summary/acs/run-record atoms. 21 new exp03 smoke tests (321 total, was 300). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (321 ✅), `git diff --check`, and secret-like scan.

- [x] 2026-07-06 14:30 — Added cap-3 rich bridge for seed-13: a 10-molecule multi-rule productive state where ALL three cap-3 rules (rr0, rr1, rr2) fire productively. Initial state: R0=3, R1=3, R2=3, R3=3, R4=3, R5=3, R01=1, R10=1, R45=0, R54=1. The deterministic selector cycles (13+tick)%3 = 1,2,0,1,2,0,... so rr0 fires at tick 0, rr2 at tick 1, rr1 at tick 2, repeating for 3 rounds (9 productive events total, all reactants exhausted by tick 8). Shuffled-catalysts control: rr0 fires (cat R2 present), rr1 fires (cat R4 present), but rr2 is no-op (cat R6 absent) → 6 events. No-catalysis: 0 events. Control discrimination: random (9) > shuffled (6) > no-catalysis (0). Required adding: (1) `generate-candidate-pool` clause for 10-molecule state with 8 rules in chem_exp00.metta, (2) `state-tick` and `state-seed` clauses for 10-molecule state, (3) `state-abundance-snapshot` clause for 10-molecule state, (4) `event-count` clause for 9 events, (5) 9 new `chamber-tick-with-candidate-accum` clauses for the 10-molecule state (3 productive rr0/rr1/rr2 for random, 2 productive rr0/rr1 for shuffled, 4 no-op for absent/None catalysts), (6) full run-config/manifest/metrics/summary/acs/run-record atoms. 21 new exp03 smoke tests (300 total, was 279). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (300 ✅), `git diff --check`, and secret-like scan.

- [x] 2026-07-06 12:30 — Extended cap-3 bridge to seed-7, seed-17, and seed-11. Each seed gets a 15-tick cap-3 chamber with 5 productive rr0 events, reactant exhaustion, replay equivalence, control discrimination, and full run-config/manifest/metrics/summary/acs/run-record atoms. Seed-7 (4-rule P-molecule): (7+tick)%3 = 1,2,0,... so rr0 fires at ticks 0,3,6,9,12 with P0/P1 exhaustion at tick 12. Seed-17 (8-rule S-molecule) and seed-11 (6-rule Q-molecule): both have (seed+tick)%3 = 2,0,1,... so rr0 fires at ticks 2,5,8,11,14 with exhaustion at tick 14. Required adding three explicit family clauses to exp03-cap3-chamber for seed-7 and seed-11 (mapping random-polymer→random, shuffled-catalysts→shuffled for the full-source-rules seam). 63 new exp03 smoke tests (279 total, was 216). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (279 ✅), `git diff --check`, and secret-like scan.
- [x] 2026-07-06 10:30 — Added candidate cap 3 support: `seeded-choice-3`, `select-candidate-3`, `selected-candidate-from-list-3`, `chamber-tick-generated-3`, `chamber-tick-generated-3-accum`, `chamber-run-3cap-*` wrappers (1-10, 15), and `exp00-candidate-cap-3`. Added `cap-candidate-pool 3` clauses for 5/6/8-element pools. Created a 15-tick cap-3 bridge for seed-13 (8-rule full-source, R0=5/R1=5): the deterministic selector cycles (13+tick)%3 = 1,2,0,1,2,0,... so rr0 fires at ticks 0,3,6,9,12 for 5 productive events with exhaustion at tick 12; rr2 and rr1 are distractors (absent reactants). Added `chamber-tick-with-candidate-accum` clauses for rr2 in seed-13 state shape (random/shuffled/no-catalysis, all no-ops). Run-config/manifest/metrics/summary/record atoms for all 3 families. 21 new exp03 smoke tests (216 total, was 195). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (216 ✅), `git diff --check`, and secret-like scan.

- [x] 2026-07-06 08:30 — Added 10-tick exp02-family bridge for seed-11 (6-rule Q-molecule family) and 16-tick longest bridge for seed-13 (8-rule R-molecule, R0=8/R1=8). Added 6-rule candidate-pool generation and cap clauses to exp00. Seed-11 produces 5 productive rr0 events over 10 ticks; seed-13 produces 8 productive rr0 events over 16 ticks. Both verify replay, reactant exhaustion, and control discrimination. 42 new exp03 smoke tests (195 total, was 153). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (195 ✅), `git diff --check`, and secret-like scan.

- [x] 2026-07-06 06:30 — Extended the 10-tick exp02-family dynamic bridge to seed-13 and seed-17. Both bridges use the same 8-rule full-source chamber with candidate cap 2, higher initial abundances (R0=5/R1=5 for seed-13, S0=5/S1=5 for seed-17), and 10-tick evolution. Each produces 5 productive rr0 events at even ticks (0,2,4,6,8) with reactant exhaustion at tick 8; shuffled/no-catalysis controls remain zero-event. Added run-config/manifest/metrics/summary/run-record atoms for all three families per seed and 42 new smoke tests (153 total, was 111). Checks: exp03 (153 ✅), exp00 (71 ✅), `git diff --check`, and secret-like scan.

- [x] 2026-07-06 02:30 — Extended exp03 multi-tick evolution to 10-tick and 16-tick runs. Added `chamber-run-6` through `chamber-run-10` and `chamber-run-16` wrappers, extended `append-event` (up to 9 existing events) and `event-count` (up to 8). The 10-tick fixture (A=5, B=5) produces 5 productive events at even ticks with reactant exhaustion at tick 8; the 16-tick fixture (A=8, B=8) produces 8 events with exhaustion at tick 14. Both verify deterministic replay equivalence, tick advancement, event accumulation, abundance snapshots, and reactant exhaustion. 13 new exp03 smoke tests (90 total, was 77). Pushed after checks.

- [x] 2026-07-06 00:30 (septuple) scanner to exp01 and exp02, completing systematic cycle-size coverage for 8-rule families (k=2..7). `product-catalyst-closed-7?`, `scan-rule-septuples-8` (C(8,7)=8), `active-septuple-count-8` (split-4 approach to work around PeTTa nested-op limit), planted 7-cycle fixtures, comprehensive fold/summary across all 40 generated-unplanted seeds. Result: 0 active 7-rule cycles across all 120 family records. 6 new exp01 tests, 20 new exp02 tests. Pushed `eca2af8` after checks.

- [x] 2026-07-05 22:30 — Added 6-rule catalytic cycle scanner to exp01 (`product-catalyst-closed-6?`, `scan-rule-sextuple`, `scan-rule-sextuples-7` (C(7,6)=7), `active-sextuple-count-7`, planted 6-cycle fixture with distractor) and exp02 (`exp02-scan-sextuples-8` enumerating all C(8,6)=28 sextuples, recursive `exp02-active-sextuple-count`, planted 6-cycle fixture in 8-rule format, comprehensive fold/summary across all 40 generated-unplanted seeds). Result: 0 active 6-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple/quintuple scanner's zero-active result extends to 6-rule cycles. Also updated SUMMARY.md with sextuple scan provenance. 9 new exp01 tests, 20 new exp02 tests. Pushed `bf68c71` after checks.

- [x] 2026-07-05 20:30 — Added 5-rule catalytic cycle scanner to exp01 (`product-catalyst-closed-5?`, `scan-rule-quintuple`, `scan-rule-quintuples-6`, planted 5-cycle fixture with distractor) and exp02 (`exp02-scan-quintuples-8` enumerating all C(8,5)=56 quintuples, recursive `exp02-active-quintuple-count`, planted 5-cycle fixture in 8-rule format, comprehensive fold/summary across all 40 generated-unplanted seeds). Result: 0 active 5-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple scanner's zero-active result extends to 5-rule cycles. Also updated SUMMARY.md with quadruple and quintuple scan provenance. 9 new exp01 tests, 20 new exp02 tests. Pushed `cfb1be1` after checks.

- [x] 2026-07-05 18:30 — Added 4-rule catalytic cycle scanner to exp01 (`product-catalyst-closed-4?`, `scan-rule-quadruple`, `scan-rule-quadruples-5`, planted 4-cycle fixture with distractor) and exp02 (`exp02-scan-quadruples-8` enumerating all C(8,4)=70 quadruples, recursive `exp02-active-quadruple-count`, planted 4-cycle fixture in 8-rule format, comprehensive fold/summary across all 40 generated-unplanted seeds). Result: 0 active 4-rule cycles across all 120 generated-unplanted family records, confirming pair/triple scanner's conservative zero-active result extends to 4-rule cycles. Also updated SUMMARY.md with triple-scan provenance. 50 exp01 tests (was 41), 450 exp02 tests (was 430). Pushed after checks.

- [x] 2026-07-05 14:30 — Added 3-rule catalytic cycle scanning to exp02 8-rule families: `scan-rule-triples-8` enumerates all C(8,3)=56 triples, recursive `exp02-active-triple-count` helper, planted 3-cycle fixture (1 active triple), and 17 smoke tests. Seed-13 planted and seed-17/29/31/37/211 generated-unplanted families all have 0 active triples, confirming the pair scanner's conservative result extends to 3-rule cycles. Pushed `b77a50e` after checks.

- [x] 2026-07-05 10:30 — Continued generated-unplanted exp02 breadth with seed-211/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `c0e6762` after checks.

- [x] 2026-07-05 08:30 — Continued generated-unplanted exp02 breadth with seed-199/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `35cfb19` after checks.

- [x] 2026-07-05 06:30 — Continued generated-unplanted exp02 breadth with seed-197/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `9bdc31b` after checks.

- [x] 2026-07-05 04:30 — Continued generated-unplanted exp02 breadth with seed-193/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `4a46c78` after checks.
- [x] 2026-07-05 02:30 — Continued generated-unplanted exp02 breadth with seed-191/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `f093a99` after checks.
- [x] 2026-07-05 00:30 — Continued generated-unplanted exp02 breadth with seed-181/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `019358b` after checks.
- [x] 2026-07-04 22:30 — Continued generated-unplanted exp02 breadth with seed-179/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `9829ccc` after checks.
- [x] 2026-07-04 20:30 — Continued generated-unplanted exp02 breadth with seed-173/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `0ec6d5c` after checks.
- [x] 2026-07-04 18:30 — Continued generated-unplanted exp02 breadth with seed-167/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `ee77e30` after checks.
- [x] 2026-07-04 16:30 — Continued generated-unplanted exp02 breadth with seed-163/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `3bdea91` after checks.
- [x] 2026-07-04 14:30 — Continued generated-unplanted exp02 breadth with seed-157/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `7b12aee` after checks.
- [x] 2026-07-04 12:30 — Continued generated-unplanted exp02 breadth with seed-151/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `8695e6d` after checks.
- [x] 2026-07-04 10:30 — Continued generated-unplanted exp02 breadth with seed-149/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `b6492c4` after checks.
- [x] 2026-07-04 08:30 — Continued generated-unplanted exp02 breadth with seed-139/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `d17ce7a` after checks.
- [x] 2026-07-04 06:30 — Continued generated-unplanted exp02 breadth with seed-137/eight-rule random/shuffled/no-catalysis records via the factored PeTTa token/product seam; pushed `7db19ca` after checks.

- [x] 2026-07-04: Commit `9829ccc` continued the host-swept factored-template generated-unplanted exp02 batch with seed-179/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/102 active family records with 0 active pairs, and run-contract serialization/testing covers one hundred fourteen records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `0ec6d5c` continued the host-swept factored-template generated-unplanted exp02 batch with seed-173/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/99 active family records with 0 active pairs, and run-contract serialization/testing covers one hundred eleven records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-04: Commit `ee77e30` continued the host-swept factored-template generated-unplanted exp02 batch with seed-167/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/96 active family records with 0 active pairs, and run-contract serialization/testing covers one hundred eight records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

## Next

- [x] Extend productive cap-6 beyond seed-11/Q-family. Completed 2026-07-08 00:30 with a PeTTa-tested seed-13/R-family 16-molecule productive cap-6 fixture.
- [x] Broaden the productive-cap artifact bundle to include the seed-13/R-family cap-6 productive run once the file writer is extended. Completed 2026-07-08 02:30 with a tested fourth bundle in the PeTTa-side file-bundle projection and thin artifact writer; commit `2c04300` pushed to GitHub `main`.
- [x] Add a quadruple/quintuple/sextuple-scan summary report atom to SUMMARY.md for human-readable provenance. Completed 2026-07-08 04:30 with `exp02-cycle-scan-summary-report` covering generated-unplanted k=4..7 cycle scans and a mirrored SUMMARY.md table.
- [x] Continue cap-6 across another seed/state shape. Completed 2026-07-08 06:30 with a PeTTa-tested seed-17/S-family 16-molecule productive cap-6 fixture.
- [x] Broaden artifact writer coverage for the seed-17 productive cap-6 bundle. Completed 2026-07-08 08:30 with a tested fifth bundle in the thin PeTTa-query writer.
- [x] Package the compact exp02 cycle-scan report into an artifact/export bundle. Completed 2026-07-08 10:30 with PeTTa-side report-file bundle atoms and a tested thin artifact writer.
- [x] Extend cap-7 from the exp00 kernel seam into an exp03 productive state shape. Completed 2026-07-08 14:30 with a PeTTa-tested seed-13/R-family 17-molecule productive cap-7 fixture.
- [x] Run exp04 reduction sweep: vary/shuffle template catalysis, basal interval, and generated-vs-hand-designed rule pools; compare maximal RAF size, minimized core size, event diversity, and no-catalysis/shuffled controls. Completed 2026-07-08 18:30 with a 24-row deterministic artifact.
- [x] Move exp04 reduction-sweep summaries into PeTTa-queryable report atoms or continue reducing bias in generated rule pools. Completed 2026-07-08 20:30 with PeTTa-side reduction rows/report/interpretion atoms and exp04 smoke coverage.
- [x] Continue reducing bias in generated exp04 rule pools with stricter cross-template controls. Completed 2026-07-08 22:30 with a 36-row sweep and PeTTa-side interpretation atoms.
- [x] Continue reducing exp04 catalysis-map/shuffle bias further with additional negative controls/minimized cores, or return to bounded-cap state-shape/export coverage. Completed 2026-07-09 04:30 with a full shuffled-offset 1-through-9 sweep and representative minimized-core atoms.
- [x] Extend exp05 from affinity-assigned candidate pools into a minimal chamber-ticking slice with matched rotated controls. Completed 2026-07-09 18:30 with PeTTa-native cap-2 selection/ticking smoke coverage.
- [x] Extend the exp06 stateful candidate-cap sweep beyond two ticks and add
  an ACS/RAF scan boundary check. Completed 2026-07-10 with the three-tick
  stateful sweep (`de84704`) and pairwise ACS boundary rejection (`40aef6`).

## Waiting or blocked

None for current cap-8 productive fixture.

## Someday or exploratory

- [ ] Rule molecules and endogenous rule evolution after exp00-exp02 are reproducible.
- [ ] Multi-chamber ecology, migration, and parasites.
- [ ] Active-predictive weighting with diversity-collapse guardrails.
- [ ] Trace-guided structural mutation versus random mutation comparison.
- [ ] Causal ACS validation archive across seeds.
- [ ] Semantic graph bridge prototype after causal ACS archive.
- [ ] Music motif chemistry bridge prototype after causal ACS archive.

## Done recently

- [x] 2026-07-04: Commit `3bdea91` continued the host-swept factored-template generated-unplanted exp02 batch with seed-163/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/93 active family records with 0 active pairs, and run-contract serialization/testing covers one hundred five records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `7b12aee` continued the host-swept factored-template generated-unplanted exp02 batch with seed-157/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/90 active family records with 0 active pairs, and run-contract serialization/testing covers one hundred two records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `8695e6d` continued the host-swept factored-template generated-unplanted exp02 batch with seed-151/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/87 active family records with 0 active pairs, and run-contract serialization/testing covers ninety-nine records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, and `git diff --check` passed; pushed to GitHub `main`.

- [x] 2026-07-04: Commit `b6492c4` continued the host-swept factored-template generated-unplanted exp02 batch with seed-149/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/84 active family records with 0 active pairs, and run-contract serialization/testing covers ninety-six records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `dec8208` continued the host-swept factored-template generated-unplanted exp02 batch with seed-131/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/75 active family records with 0 active pairs, and run-contract serialization/testing covers eighty-seven records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `4162be7` continued the host-swept factored-template generated-unplanted exp02 batch with seed-127/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/72 active family records with 0 active pairs, and run-contract serialization/testing covers eighty-four records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-04: Commit `070ddce` continued the host-swept factored-template generated-unplanted exp02 batch with seed-113/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/69 active family records with 0 active pairs, and run-contract serialization/testing covers eighty-one records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `a9deba1` continued the host-swept factored-template generated-unplanted exp02 batch with seed-109/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/66 active family records with 0 active pairs, and run-contract serialization/testing covers seventy-eight records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `b31d659` continued the host-swept factored-template generated-unplanted exp02 batch with seed-107/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/63 active family records with 0 active pairs, and run-contract serialization/testing covers seventy-five records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `ba01c3a` continued the host-swept factored-template generated-unplanted exp02 batch with seed-103/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/60 active family records with 0 active pairs, and run-contract serialization/testing covers seventy-two records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `e6aee9f` continued the host-swept factored-template generated-unplanted exp02 batch with seed-101/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/57 active family records with 0 active pairs, and run-contract serialization/testing covers sixty-nine records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `bb1f320` added compact PeTTa exp03 dynamic aggregate/report atoms over tested seed-7, seed-13, and seed-17 full-source run exports. The report records 9 tested family records, 3 active random-family records with 6 total random events, 6 zero-event control records, common candidate cap 2, and per-seed summary rows; smoke coverage verifies the report. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `467a6f6` added richer exp03 dynamic run-record/export coverage over the full-source bridges. Seed-7 full-source random, shuffled, and no-catalysis families now all have v0.1 run-records; a PeTTa `run-export` projection exposes config/manifest/events/abundances/metrics/ACS/ablations/summary fields, and smoke tests cover export projections for seed-7, seed-13, and seed-17. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `9b82112` added a second eight-rule exp03 full-source dynamic bridge through the seed-17 seed-to-components exp02 generation seam. The chamber carries all eight generated source rules for random-polymer, shuffled-catalysts, and no-catalysis families; the same two-candidate cap/order yields two replayable `rr0` random events over three ticks while controls stay zero-event. Smoke tests cover capped pools, event counts, replay, run-record abundances, and the seed-to-components metric. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `9b02a60` extended exp03 full-source dynamics to seed-13/eight-rule source families. exp00 candidate generation now caps eight-rule pools to the first two candidates; exp03 adds seed-13 random-polymer, shuffled-catalyst, and no-catalysis full-source chambers and v0.1 run-records. The random family produces two replayable `rr0` events over three ticks while both controls remain zero-event, and smoke tests cover capped pools, event counts, replay, abundances, and run-record completeness. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `9a37c59` broadened exp03 dynamic source visibility beyond two-rule windows. exp00 candidate generation now handles four-rule chamber pools; exp03 adds a seed-7 full-source exp02 chamber carrying all four random/shuffled/no-catalysis source rules, with per-tick caps bounding deterministic selection to two candidates. The random full-source run records two replayable rr0 events over three ticks, controls remain zero-event, and a v0.1 run-record covers the random full-source path. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- [x] 2026-07-03: Commit `395c10c` generalized the exp03/exp02 dynamic bridge from the seed-7 two-rule smoke to seed-11/six-rule-source dynamic run records. The new PeTTa fixture adds bounded Q-state dynamics, random/shuffled/no-catalysis seed-11 chambers, v0.1 run-contract records for the three dynamic runs, and smoke checks showing two random-family events versus zero-event controls. Checks before push: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

- [x] 2026-07-03: Commit `fd90ca0` connected exp03 multi-tick soup dynamics to the first exp02-style random/control family smoke. The new PeTTa fixture sources seed-7 random-polymer, shuffled-catalyst, and no-catalysis rule identities from exp02; deterministic three-tick dynamics produce two events for the random family and zero for both controls, with smoke coverage in `experiments/exp03/smoke.metta`. Checks before push: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

- [x] 2026-07-03: Commit `2acdd39` lifted exp03 from the duplicated-`r0` productive fixture into a nontrivial selectable two-rule pool. The multi-tick fixture now alternates deterministic seed/tick selection between a productive `r0` candidate and an `r1` distractor/no-op, preserving tick advancement, event accumulation, abundance snapshots, replay equivalence, and starved no-op behavior. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `14d12f0` pushed to GitHub `main`. Commit `c4f69db` pushed to GitHub `main`. Commit `f65c430` pushed to GitHub `main`. Commit `1a8b2c2` pushed to GitHub `main`.

- [x] 2026-07-02: Commit `f0a45a4` added exp03 multi-tick soup dynamics: `src/chem_dynamics.metta` layers a PeTTa multi-tick chamber runner over exp00, accumulates event logs, advances ticks safely through blocked/no-op steps, exposes abundance snapshots and trace helpers, and adds a bounded five-tick productive fixture plus starved no-op fixture. `experiments/exp03/smoke.metta` checks 5-tick evolution, event accumulation/counting, tick advancement, reactant exhaustion/no-op behavior, and replay equivalence; `scripts/run_exp03.sh` runs the smoke. Verified after parent review: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and obvious secret-like scan (only expected `seed-7` strings matched).

- [x] 2026-07-02: Commit `1eff1d9` continued the host-swept factored-template generated-unplanted exp02 batch with seed-97/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/54 active family records with 0 active pairs, and run-contract serialization/testing covers sixty-six records. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-02: Commit `dc92550` continued the host-swept factored-template generated-unplanted exp02 batch with seed-89/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/51 active family records with 0 active pairs, and run-contract serialization/testing covers sixty-three records. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `e7567124d95b18602d87f63b1634fb82922b1cb7` adds seed-83/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/48 active family records with 0 active pairs, and run-contract serialization/testing covers sixty records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `879ad44` adds seed-79/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/45 active family records with 0 active pairs, and run-contract serialization/testing covers fifty-seven records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `de29b83` adds seed-73/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/42 active family records with 0 active pairs, and run-contract serialization/testing covers fifty-four records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `43f23adf063585b31d3136cdd5d9c5ea532f604d` adds seed-71/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/39 active family records with 0 active pairs, and run-contract serialization/testing covers fifty-one records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `67aebddd2cd64b8d3a5229918c91d0c3f9ed8c48` adds seed-67/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/36 active family records with 0 active pairs, and run-contract serialization/testing covers forty-eight records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `0628dabb8459b27ec0f9b3d4c8d52958719b2419` adds seed-61/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/33 active family records with 0 active pairs, and run-contract serialization/testing covers forty-five records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `74d44e13592fbea1bae4db327addf03fc46fa2d1` adds seed-59/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/30 active family records with 0 active pairs, and run-contract serialization/testing covers forty-two records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-02: Continued the host-swept factored-template generated-unplanted exp02 batch. Commit `cc2d3c9bd7b288c5aa9f379a63a38d9d6d826a8e` adds seed-53/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/27 active family records with 0 active pairs, and run-contract serialization/testing covers thirty-nine records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-02: Added the next host-swept factored-template generated-unplanted exp02 point. Commit `7d9ef1a` adds seed-47/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/24 active family records with 0 active pairs, and run-contract serialization/testing covers thirty-six records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-02: Added the next factored-template generated-unplanted exp02 point. Commit `7931be2ef6b0c723b9d86db6a9239b445dba6ec6` adds seed-43/eight-rule random/shuffled/no-catalysis records through the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/21 active family records, and run-contract serialization/testing covers thirty-three records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-01: Added the next factored-template generated-unplanted exp02 point. Commit `3a69fe3bcc023908e4dad8f722b8050c03e38e99` adds seed-41/eight-rule random/shuffled/no-catalysis records through the existing PeTTa token/product dictionary seam; all three scan to zero active reciprocal product-as-catalyst pairs, generated-unplanted folded summaries update to 0/18 active family records, and run-contract serialization/testing covers thirty records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-01: Used the folded exp02 summary seam for the next less-fixture-like generated point. Commit `e033bac47929a9f7652d3c81ef82c14157f0849a` adds factored-template seed-37/eight-rule random/shuffled/no-catalysis records, derives the generated-unplanted summary as 0/15 active family records through PeTTa folds, derives report rows from folded summaries, and expands run-contract serialization/testing to twenty-seven records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- [x] 2026-07-01: Moved exp02 sweep-kind summaries toward PeTTa-side folds over tested run records. Commit `09ff9559cf03d3077c5cf5504c6e10c21576ee02` adds recursive PeTTa list/metric helpers, derives family-record counts, active-family counts, active-pair totals, and active random-polymer points from planted/generated run-record lists, and keeps the current planted 4/12, 7-active-pair versus generated-unplanted 0/12 summary unchanged. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

- [x] 2026-07-01: Added another compact generated exp02 point with the factored seed-token/product schema. Commit `f83cd62c43afbf0db3965aab2955284b5d25aa1f` adds seed-31/eight-rule factored-template random/shuffled/no-catalysis records; all remain zero-active, generated-unplanted controls summarize as 0/12 family records, and serialization covers twenty-four records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

- [x] 2026-07-01: Commit `745d433c29089cc19588704c8d88feaa10982379` factored generated exp02 tables further with a reusable PeTTa `exp02-factored-unplanted-rule-components` template and seed-29 token/product dictionaries. The new random/shuffled/no-catalysis seed-29 point has zero active reciprocal pairs, generated-unplanted controls summarize as 0/9 family records, and run-contract serialization now covers twenty-one records. Checks passed locally: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- [x] 2026-07-01: Added a concise exp02 sweep-kind report before larger sweeps: PeTTa `exp02-summary-row`/`exp02-sweep-kind-summary-report` atoms and `experiments/exp02_small_sweep_20260630/SUMMARY.md` summarize planted reciprocal-pair controls (4/12 active family records; 7 active pairs) versus generated-unplanted controls (0/6; 0 active pairs), with explicit no-spontaneous-emergence-claim caveats. Commit `2c7a15b39ea00348fe19cad59efa5ac9ca9f2c2b` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan passed. Commit `3d476b6` pushed to GitHub `main`.

- [x] 2026-07-01: Added a second generated non-planted exp02 seed-to-component point: seed-23/eight-rule random-polymer, shuffled-catalyst, and no-catalysis families all scan to zero active reciprocal pairs. Added PeTTa `exp02-sweep-kind-summary`/`active-pair-rate` atoms separating planted reciprocal-pair controls (4/12 family records active; 7 active pairs total) from generated-unplanted controls (0/6 active; 0 pairs), and expanded run-contract serialization from fifteen to eighteen records. Commit `a5dbc04d8a4f7d070f0915282d634874b440006f` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan passed.

- [x] 2026-07-01: Added a generated non-planted exp02 seed-to-component control point: seed-19/eight-rule random-polymer, shuffled-catalyst, and no-catalysis families now all scan to zero active reciprocal pairs, are tagged with `sweep-kind generated-unplanted-control`, and expand run-contract serialization from twelve to fifteen records. Commit `484c55dfdb21f937f7db0a93b66d07448416674a` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-07-01: Added a PeTTa-side seed-to-component generation seam for exp02 and broadened the deterministic sweep beyond three parameter points: seed-17/eight-rule random/shuffled/no-catalysis families now flow through generated `rule-components` atoms, smoke tests cover active-pair discrimination, and the file harness serializes all twelve run-contract records. Commit `3404d9d0d5b250357d9e7bc79c81001060a45708` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-07-01: Made exp02 sweep provenance more systematic with PeTTa `exp02-sweep-point` atoms for seed-7/four-rule, seed-11/six-rule, and seed-13/eight-rule families, and extended the run-contract file serialization harness/test from the original three seed-7 runs to all nine random/control records. Commit `4a80388299cb94814bd73dc3a49094afb07b955e` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-07-01: Broadened exp02 with a component-generated seed-13/eight-rule PeTTa family, shuffled-catalyst and no-catalysis controls, 28-pair conservative ACS scanning/counts, run-contract records, and updated RUN.md hashes/provenance. Commit `4c39d90f6a0a8ce8cd84cb6896ba571c6874f920` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-06-30: Parameterized exp02 beyond the first seed-7/four-rule fixture: added a seed-11/six-rule PeTTa sweep point with random-polymer, shuffled-catalyst, and no-catalysis run-contract records; the random fixture has two active reciprocal product-as-catalyst pairs and both controls have zero; `experiments/exp02_small_sweep_20260630/RUN.md` provenance was updated. Commit `b83d97b70940c590c6d485743460e91380c454e0` pushed after `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-06-30: Added a thin host harness for writing PeTTa run-contract atoms to per-run files: `scripts/write_exp02_contract_files.sh`/`.py` serializes the PeTTa-tested exp02 records under `experiments/exp02_small_sweep_20260630/runs/`, with `scripts/test_exp02_contract_files.sh` covering the file convention; commit ce6da96da5f6c797dff2f9941bc529e88e487f9f pushed after checks.
- [x] 2026-06-30: Added the first tiny deterministic exp02 random-polymer control sweep and recorded it under the v0.1 run contract: seed-derived polymer fixture has one active reciprocal product-as-catalyst pair, shuffled-catalyst and no-catalysis controls have zero active pairs, and `experiments/exp02_small_sweep_20260630/RUN.md` captures commands/hashes/seed/exit/conclusion; commit `a3ddf9e63faf90c4a4b1a9a09b8b1e7eeeba6be2` pushed to GitHub `main` after `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-06-30: Defined the version-0.1 run output contract in PeTTa-shaped atoms: `run-config`, `run-manifest`, `abundance-snapshot`, `run-summary`, and `run-record`, plus a runnable `experiments/run_contract` smoke projected over exp01 outputs; commit `4dbf4b5454cf19b536c1019950e42c19541a6359` pushed to GitHub `main` after `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `git diff --check`, and an obvious secret-like scan passed.
- [x] 2026-06-30: Extended exp01 ablation from fixture counts to replayed PeTTa productivity traces: baseline planted ACS replay records two transition traces, single-rule ablation records one, and the ablation drop is computed from trace counts; commit `912c5cee7964b466e66c770ad9425d87cb9bf381` pushed to GitHub `main` after `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-29: Generalized exp01 recovery into a conservative PeTTa-native ACS pair/set scanner: all rule pairs in the planted four-rule fixture are enumerated, reciprocal product-as-catalyst closure is marked `active`, distractor pairs remain explicit `rejected` candidates, and the planted pair is recovered through the scanner; commit `8dde7e8405260a4687e6cb972b73b0814b6bdc78` pushed to GitHub `main` after `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-29: Added first exp01 planted ACS recovery smoke: PeTTa-native `acs-candidate`/`ablation` atoms, a two-rule planted catalytic closure with distractors, non-catalytic-cycle rejection, and single-rule productivity-drop ablation; commit `68fd5a4ec7fdd687aa0e8cfc25fcb21c2956eee1` pushed to GitHub `main` after `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-29: Added exp00 unit tests for deterministic PeTTa-native molecule/rule hash seams, candidate-cap boundary preservation, and replay equivalence between generated chamber ticking and direct one-tick replay; commit `d3da831907d20f3739ac4233c9b516527c898c5d` pushed to GitHub `main` after `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-28: Generalized exp00 candidate generation/caps beyond fixed hard-coded candidates: chamber rules now generate candidate pools, `candidate-cap` atoms bound per-tick pools, and generated chamber ticking reuses deterministic selection; commit `205092f26e3def5e940ca9d29db610f67f9d664a` pushed to GitHub `main` after `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-28: Wired deterministic candidate selection directly into chamber ticking and added a first bounded three-candidate pool/cap seam; commit `6f2e25edb10288350b9003c1840b69d3371f7db6` pushed to GitHub `main` after `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed.
- [x] 2026-06-27: Added seed/tick deterministic two-candidate selection seam; commit `0f6e5cb09870ad037285ca95f775b31d9b78923e` pushed to GitHub `main` after `scripts/run_exp00.sh` passed.
- [x] 2026-06-27: Added explicit precondition/invariant checks for candidate applicability, starved-candidate blocking, and nonnegative abundance traces; commit `f031ff9c0cf6582b7cc76ab34d8df356c9e51c04` pushed to GitHub `main` after `scripts/run_exp00.sh` passed.
- [x] 2026-06-27: Added candidate, chamber, metric, trace accessors, and a one-candidate chamber tick to exp00; commit `0b943c2a641d5d1f5e97ce17cee5d7f3bb1fca73` pushed to GitHub `main` after `scripts/run_exp00.sh` passed.
- [x] 2026-06-27: Generalized exp00 from one hard-coded deterministic reaction into a bounded generic PeTTa binary catalytic transition with atom accessors, event construction, replay equality, and expanded smoke tests; commit `2ae87353f4adee7ca4492ed27a03f2b70e86e688` pushed to GitHub `main` after `scripts/run_exp00.sh` passed.
- [x] 2026-06-27: Pushed first exp00 scaffold commit `ee60d539e95ec35bfce30a80d0683cab620aa7be` to GitHub `main` after re-running `scripts/run_exp00.sh` successfully.
- [x] 2026-06-26: Settled runtime choice for version 0.1: PeTTa on SWI-Prolog 9.3.x, using the locally validated PeTTa/SWI stack.
- [x] 2026-06-26: Added first PeTTa-native exp00 deterministic smoke scaffold and runner in the implementation repo; smoke test passed locally.
- [x] 2026-06-26: Configured local Git identity for `projects/petta-chem/repos/petta-chem` as Benjamin Goertzel `<ben@singularitynet.io>`.
- [x] 2026-06-26: Created public GitHub repo `https://github.com/bgoertzel-sing/petta-chem` and cloned it to `projects/petta-chem/repos/petta-chem`.
- [x] 2026-06-26: Benjamin clarified that the algorithmic chemistry system should be built in PeTTa from the start; Python is acceptable only for experiment wrapping/harness work.
- [x] 2026-06-26: Ingested PDF specification and created library sidecar at `library/petta-abstract-algorithmic-chemistry/SOURCE.md`.
- [x] 2026-06-26: Created project notebook at `projects/petta-chem/`.
