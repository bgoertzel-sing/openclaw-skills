# Tasks

- [x] 2026-07-23 20:15 PDT: complete the first bounded M-D implementation
  slice: deterministic unpruned `RePairInitializer` at active-repository clean
  commit `7b85c20`. It performs most-frequent-digram replacement with
  lexicographic tie-breaking, left-to-right non-overlap handling, hierarchical
  productions, a single `InitializeFromRePair` edit, immutable input, and exact
  reconstruction. Focused pytest passed 16 tests; required stdlib discovery
  passed 220 tests; `compileall` and `git diff --check` passed. The initializer
  is intentionally not exposed through `CLA.simple(init=...)` until official
  adaptive-score pruning and replay are complete. No scientific fixture or
  E0--E8 gate was run.

- [ ] Continue M-D with exact official-score rule pruning and replay support
  for `RePairInitializer`; prove reconstruction after every pruning decision
  and expose `init="repair"` only after this complete slice passes.

- [x] 2026-07-23: review and integrate the supplied mathematical foundations
  as explicit, independently checkable amendments to the adaptive-coding
  programme. Deliverable: preserve the 11-page PDF and extracted text; audit
  the recurrence ceiling, substitution separation, epsilon-machine MDL,
  category-congruence, and quantale/synergy claims; then propose a frozen
  amendment covering `LZ77SLPInitializer`, E5b Feigenbaum/Sturmian fixtures,
  and estimated-versus-realized mixed-second-difference ledger fields.
  Acceptance: source SHA-256 and library sidecar exist; every adopted theorem
  has assumptions/citations checked; existing M-A--M-C and frozen E0--E8 gates
  are not silently changed; any new measured fixture receives a separate
  preregistration with fresh seeds. Next command: compare Sections 2--10
  against the implementation/evaluation specs and upstream standard results.
  Evidence: `docs/cla_math_foundations_ascii_1.{pdf,txt}`,
  `library/cla-mathematical-foundations-2026/SOURCE.md`, and reviewed
  amendment `repos/chaoslang/docs/mathematical-foundations-amendment-v1.md`
  (active-worktree SHA-256
  `bb69556d64e3d893ba05f52f915ee41abe994afbc565d96d1d1a3ca69249f65d`).
  The amendment audits assumptions claim by claim, freezes the bounded M-D
  additions and a separately gated E5b proposal, and explicitly makes no new
  theorem, gate, or experiment claim. Focused pytest passed 17; required
  stdlib discovery passed 216; compileall and diff check passed. No E0--E8
  fixture was opened. Next: implement the M-D search interfaces and invariant
  tests from the governing spec plus this amendment.

- [ ] 2026-07-23: implement Ben's adaptive-coding CLA upgrade and execute its
  gated evaluation programme. Governing inputs:
  `media/inbound/openclaw-staged-20793f22-0cbe-4262-81c8-ff1f62a51080/chaoslang_upgrade_spec---ec616bc7-7315-4f58-a179-ff77fae99f93.md`
  and
  `media/inbound/openclaw-staged-20793f22-0cbe-4262-81c8-ff1f62a51080/chaoslang_eval_programme---4bd6da32-4c1b-4a6d-92e1-5ea255f5b16b.md`.
  Deliverable: preserve both documents under the project, implement milestones
  M-A through M-F in the stated order, and run E0 through E8 only as their
  dependency and promotion gates authorize. Acceptance: each milestone leaves
  the documented full suite green; coding/scorer/search/automata/ledger
  invariants pass; measured experiments have frozen ledgers and fresh suffixes;
  E3's representation and search gates control further work; OmegaSim remains
  paused until E7 resolves and E8a passes. Next command: preserve and hash both
  supplied specifications, inspect their fit against the current public API,
  then implement M-A (coding protocols, KT, adaptive Markov, LZ78 wrapper, and
  registry) with tests 1--4 and 6. Evidence:
  `repos/chaoslang/docs/chaoslang_upgrade_spec.md`,
  `repos/chaoslang/docs/chaoslang_eval_programme.md`, milestone commits/tests,
  and timestamped experiment ledgers. Progress: M-A commit `6145e1d`; M-B
  commit `46ffbfe`; M-C commit `9684701`. M-B acceptance evidence: focused pytest 17, full stdlib
  discovery 216, compileall/diff check, exact legacy `-6232/+6296/+64`
  rejection replay. M-C evidence: focused pytest 12, full stdlib discovery
  216, compileall/diff check, frozen-factory guard, adaptive member codes, and
  exact score/delta decomposition. Next command: prepare and review the
  reviewed mathematical-foundations amendment SHA-256 `bb69556d...`; next
  implement M-D in governing order; do not start E0-E8 yet. M-D slice 1 adds
  the frozen mixed-second-difference four-score identity, stable
  estimate/digest ranking, nullable estimates, and composite ledger fields
  including estimated-versus-realized residuals. Focused pytest passed 6;
  required stdlib discovery passed 220; compileall and diff check passed.
  Search remains disabled; next implement deterministic Re-Pair initialization
  and exact-score pruning, then LZ77-SLP under the reviewed amendment.

- [x] 2026-07-23: implement R0's first transparent complete-code
  decomposition subgate. Spec/implementation commits `2ec949e` / `bdbf0f6`;
  the constructed canonical 19-frame fixture reports `-6,232` data,
  `+6,296` model, and `+64` total bits with an explicit rejection reason.
  Focused pytest passed 11; full pytest 322 tests / 93 subtests; stdlib
  discovery 209 tests; `compileall` and `git diff --check` passed. No
  scientific fixture or held-out suffix was scored. Next: specify the
  candidate/iteration trace schema and integrate it without changing proposal
  selection.

- [x] 2026-07-23: make identity-guarded failed canonical-result deletion
  durable before returning failure. Spec/implementation commits `3d5224d` /
  `8e8b042`; constructed tests prove unlink-before-parent-`fsync` ordering and
  explicit cleanup-`fsync` failure reporting. Focused pytest passed 33; full
  pytest 320 tests / 93 subtests; stdlib discovery 209 tests; `compileall` and
  `git diff --check` passed. No scientific fixture or suffix was scored.

- [x] 2026-07-23: produce Ben's detailed CLA experiments and algorithm-repair
  PDF. Deliverable: an evidence-traceable report covering implementation,
  symbolic and high-dimensional studies, synthetic complete-code calibration,
  geometric detector calibration, OmegaSim A6 resweeps, quantitative results,
  failure decomposition, and a prioritized repair programme, plus the verified
  GitHub URL. Acceptance: every principal result cites its experiment ledger;
  LaTeX compiles; PDF text extraction, all-page visual inspection, ASCII/source
  checks, and SHA-256 hashing pass. Next command: extract a canonical results
  table from the project ledgers and write
  `repos/chaoslang/docs/cla_experiments_and_repair_diagnostic_20260723.tex`.
  Evidence:
  `repos/chaoslang/docs/cla_experiments_and_repair_diagnostic_20260723.{tex,pdf}`.
  Completed: 10-page PDF compiled and all pages visually inspected; extracted
  text contains the key results and verified GitHub URL; ASCII source check
  passed; no overfull boxes or undefined references remain. PDF SHA-256:
  `fdb6f48970165a27784d2c64c04eaa8744274f5a54c068bb1badbf710703b0f6`.

- [x] 2026-07-23: reject an artifact-parent ancestor changed during
  persistence into a same-identity symlink alias. Spec/implementation commits
  `0b07cfa` / `8eabc2c`; a constructed regression proves the call fails and
  removes its artifact from the opened parent. Focused pytest passed 31; full
  pytest 318 tests / 93 subtests; stdlib discovery 209 tests; `compileall` and
  `git diff --check` passed. No scientific fixture or suffix was scored.

- [x] 2026-07-23: freeze and validate the lifecycle of the identity-bearing
  descriptor used for future measured-result emission. Spec/test commits
  `58c309d` / `11cd2b3` prove closure after success and read, stdout-write, and
  stdout-flush failures. Focused pytest passed 30; full pytest 317 tests / 93
  subtests; stdlib discovery 209 tests; `compileall` and `git diff --check`
  passed. Constructed provenance work only; no scientific fixture or suffix
  was generated or scored.

- [x] 2026-07-23: implement the pre-frozen identity-bound read-back seam for
  future measured-result emission. An internal open descriptor retains the
  created artifact identity through post-durability SHA-256 verification;
  constructed target- and parent-replacement regressions prove replacement
  bytes cannot reach stdout. Clean active-repository commit `a9c0bf2`;
  focused pytest 26, full pytest 313 tests / 93 subtests, stdlib discovery 209
  tests, `compileall`, and `git diff --check` passed. No scientific fixture,
  held-out suffix, or score was generated or inspected.

- [x] 2026-07-22: freeze an identity-bound read-back requirement for future
  measured-result emission. Clean active-repository spec commit `c3b9971`
  requires stdout bytes to come from the artifact created by that call, not a
  later lexical-path lookup. Focused pytest passed 24; full pytest 311 tests /
  93 subtests; stdlib discovery 209 tests; `compileall` and `git diff --check`
  passed. Constructed provenance work only; no scientific fixture was scored.
  Next: implement the internal identity-bound seam and constructed parent/
  target replacement tests before any new measured ledger.

- [x] 2026-07-22: independently reproduce the constructed parent-bound
  canonical-result checks at clean active-repository commit `e893704`.
  Focused pytest passed 24; full pytest passed 311 tests / 93 subtests;
  stdlib discovery passed 209 tests; `compileall` and `git diff --check`
  passed. No benchmark or scientific fixture was generated or scored; frozen
  Mackey--Glass/Lorenz--96 outcomes remain binding.

- [x] 2026-07-22: implement the pre-frozen parent-identity invariant for
  canonical measured-result publication. Creation, identity-guarded cleanup,
  and parent-directory `fsync` use one opened directory handle; a constructed
  replacement regression fails closed without publishing into the replacement.
  Clean active-repository commit `e893704`; focused pytest 24, full pytest 311
  tests / 93 subtests, stdlib discovery 209 tests, `compileall`, and `git diff
  --check` passed. No scientific fixture or held-out suffix was generated or
  scored.

- [x] 2026-07-22: freeze a parent-identity invariant for future canonical
  measured-result publication before implementation. Artifact creation and
  parent-directory durability must use the same opened directory handle and
  success must fail if the lexical parent is replaced. Clean active-repository
  spec commit `5c87cf5`; focused pytest 23, full pytest 310 tests / 93
  subtests, stdlib discovery 209 tests, `compileall`, and `git diff --check`
  passed. No scientific fixture or held-out suffix was generated or scored.

- [x] 2026-07-22: audit the current canonical-result provenance boundary at
  clean active-repository commit `aa5ab90` without reopening a measured
  ledger. Focused pytest passed 23, full pytest passed 310 tests / 93 subtests,
  stdlib discovery passed 209 tests, and `compileall`, `git diff --check`, and
  clean status passed. No scientific fixture or suffix was generated or
  scored; the frozen detector calibration and Stage-B coding null are
  unchanged.

- [x] 2026-07-22: make failed canonical-result cleanup conditional on the
  target retaining the created file's device/inode identity. Constructed
  replacement testing proves a foreign substituted target survives. Clean
  active-repository commits `66d1711` / `aa5ab90`; focused pytest 23, full
  pytest 310 tests / 93 subtests, stdlib discovery 209 tests, `compileall`, and
  `git diff --check` passed. No scientific fixture or suffix was scored.

- [x] 2026-07-22: prove that canonical-result publication refuses a
  pre-existing target symlink and preserves its referent. Clean active-repo
  commit `bd55fe2`; focused pytest 22, full pytest 309 tests / 93 subtests,
  stdlib 209, `compileall`, and `git diff --check` passed. Constructed data
  only; no scientific fixture or closed suffix was generated or scored.

- [x] 2026-07-22: reject symbolic links anywhere in a future canonical-result
  parent ancestry before artifact creation. Clean active-repository commit
  `ab2ba52`; a constructed nested-alias regression proves no artifact reaches
  the alias target. Focused pytest 21, full pytest 308 tests / 93 subtests,
  stdlib 209, `compileall`, and `git diff --check` passed. No scientific
  fixture or closed suffix was generated, rerun, or scored.

- [x] 2026-07-22: reject symlinked canonical-result parent directories before
  artifact creation, preventing a frozen path from publishing into an alias
  target. Spec/implementation commits `995903b` / `732cdb2`; focused pytest
  20, full pytest 307 tests / 93 subtests, stdlib 209, `compileall`, and `git
  diff --check` passed. Constructed data only; no scientific fixture or closed
  suffix was generated, rerun, or scored.

- [x] 2026-07-22: prove with constructed tests that both a stdout write
  exception and a rejected incomplete write preserve the already durable
  canonical result artifact. Clean active-repository commit `0a4a7da`;
  focused pytest 19, full pytest 306 tests / 93 subtests, stdlib 209,
  `compileall`, and `git diff --check` passed. No scientific fixture or closed
  suffix was generated, rerun, or scored.

- [x] 2026-07-22: make future measured-result command success conditional on
  flushing standard output after its complete write. Spec and implementation
  commits `2bfdfc5` / `af0f3c0`; focused pytest 18, full pytest 305 tests / 93
  subtests, stdlib 209, `compileall`, and `git diff --check` passed. A direct
  unittest module selector discovered zero pytest-style tests and is not used
  as evidence. Constructed data only; no closed scientific fixture was
  generated or scored.

- [x] 2026-07-21: make future measured-result stdout fail closed when durable
  artifact read-back differs from the writer digest or cannot be read. Spec and
  implementation commits `17a11ac` / `ecbeaa4`; focused 16, full pytest 303
  tests / 93 subtests, stdlib 209, `compileall`, and `git diff --check` passed.
  Constructed data only; no closed scientific fixture was generated or scored.

- [x] 2026-07-21: Make new canonical result directory entries durable before
  measured stdout emission. Clean active-repository commits `edbf285` /
  `898d1cb`; the writer fsyncs artifact contents then the parent directory and
  removes only its new target on directory-fsync failure. Focused pytest 14,
  full pytest 301 / 93 subtests, stdlib 209, `compileall`, and `git diff
  --check` passed. Constructed data only; no scientific fixture was generated,
  rerun, or scored.

- [x] 2026-07-21: Make failed canonical artifact creation recoverable without
  weakening no-overwrite behavior. Clean active-repository commits `d04453a` /
  `4ff7ab8`; incomplete writes and artifact `fsync` failures remove only the
  newly created target. Focused pytest 13, full pytest 300 / 93 subtests,
  stdlib 209, `compileall`, and `git diff --check` passed. Constructed data
  only; no scientific fixture was generated, rerun, or scored.

- [x] 2026-07-21: Tighten canonical measured-result durability at clean
  active-repository commits `037578f` / `500696f`. The writer now rejects an
  incomplete artifact write and flushes plus `fsync`s the completed bytes
  before returning, preserving persist-before-emit ordering. Focused pytest 12,
  full pytest 299 / 93 subtests, stdlib 209, `compileall`, and `git diff
  --check` passed. Constructed data only; no scientific fixture was scored.

- [x] 2026-07-21: Specify and unit-implement a fail-closed persist-then-emit
  boundary for future measured commands. Clean active-repository commits
  `b0db6ab` / `ac1bcc7`; focused pytest 10, full pytest 297 / 93 subtests,
  stdlib 209, `compileall`, and `git diff --check` passed. Constructed tests
  verify byte identity, persist-before-output ordering, untouched stdout on
  artifact failure, and rejection of incomplete output writes. No scientific
  fixture was generated, rerun, or scored.

- [x] 2026-07-21: Specify and unit-implement a fail-closed canonical JSON
  result-artifact seam for future measured ledgers, without rerunning or
  reopening the failed Stage-B fixtures. Spec/code commits `e715eed` /
  `274529a`; focused pytest 5, full pytest 292 / 93 subtests, stdlib 209,
  `compileall`, and `git diff --check` passed. The writer preserves UTF-8,
  rejects non-finite JSON and overwrite attempts, and returns the exact byte
  SHA-256. A future benchmark must still separately freeze its artifact path,
  command, fixtures, config, seeds, hashes, controls, and decision rule.

- [x] 2026-07-21: Audit frozen Stage-B result artifacts without rerunning the
  closed benchmark. Source/test/command hashes match, but decisive JSON stdout
  was not retained separately. Commit `0356c73` records the limitation and
  makes a predeclared canonical result artifact plus committed SHA-256
  mandatory for future measured ledgers. Full pytest 287 / 93 subtests,
  stdlib 209, `compileall`, and `git diff --check` passed.

- [x] 2026-07-21: Freeze and execute the smallest fresh prefix-quantized
  Stage-B complete-code gate at clean active-repository commits `7bad170` and
  `22f1450`. All integrity checks passed and neither shuffled null was
  promoted, but compact CLA lost both positives to canonical LZ78:
  Mackey--Glass 8,824.829 vs 744 bits and full-state Lorenz--96 8,482.142 vs
  1,240 bits. No tuning or rescoring; this is a coding null only.

- [x] 2026-07-20: Specify and unit-implement the constructed-data-only
  prefix-fitted vector quantizer subgate. Clean active-repository spec/code
  commits `313452d` / `ca3e48f` and README commit `21e9fdf`; focused pytest 4
  tests / 9 subtests, full pytest 286 / 93 subtests, stdlib discovery 208,
  `compileall`, and `git diff --check` passed. No Mackey--Glass, Lorenz--96, or
  held-out suffix was generated or scored. Next: separately freeze the smallest
  valid Stage-B experiment ledger before any measurement.

- [x] 2026-07-20: Specify the outcome-independent Stage-B complete-code design
  after the nearest-neighbor Stage-A v2 pass. The design preserves six-delay
  Mackey--Glass and coordinate-complete Lorenz--96 state abstractions, requires
  a separately unit-validated prefix-only quantizer and entirely new fixtures,
  freezes complete CLA plus literal/unigram/Markov/LZ78 controls, and uses an
  every-positive/no-shuffled-null rule. It authorizes no scientific outcome;
  the next subgate is constructed-data quantizer specification and unit tests.
  Clean active-repository commit `33483b6`; full pytest passed 282 tests / 84
  subtests, stdlib discovery passed 204 tests, and `compileall` plus
  `git diff --check` passed. Spec SHA-256:
  `ed8e338064cafc5f46da8028653ce1bdf4abed22d9d4583d3785c32bbac7cb76`.
  See `scratch/chaoslang-strict-replay/docs/nearest-neighbor-stage-b-design-spec-v1.md`.

- [x] 2026-07-20: Freeze and execute corrective nearest-neighbor Stage-A v2
  without changing v1's fixtures, representations, thresholds, seeds, or pass
  rule. A pre-execution schema test fixed the exact degenerate stable-control
  contract; focused 8/4 subtests, full pytest 282/84 subtests, stdlib 204,
  `compileall`, and `git diff --check` passed at clean commit `85667bd`. Both
  Mackey--Glass and full-state Lorenz--96 positives were promoted and all four
  controls rejected, so Stage A passed. Stage B still requires a separate
  frozen untouched-data protocol; no tuning/rescoring or stronger claim.

## Next

- [x] 2026-07-20: Executed the separately frozen nearest-neighbor divergence
  Stage-A ledger at clean active-repository commit `ee0485c`. Protocol,
  benchmark, declaration test, fresh initial states, seeds, normalization,
  embedding, Theiler windows, fit interval, threshold, exact command, and
  all-positive/no-control rule are frozen in
  `experiments/20260720T211500Z-nearest-neighbor-calibration-v1/RUN.md`.
  The exact command exited 1 before emitting a score because a frozen stable
  fixture had no eligible positive-distance neighbor pair. No tuning or v1
  rerun; Stage B remains closed. A corrective v2 requires an independently
  frozen runner contract with unchanged scientific choices and an end-to-end
  stable-fixture schema test.

- [x] 2026-07-20: Specify then unit-implement an additive Rosenstein-inspired
  nearest-neighbor divergence seam at clean active-repository commits
  `fd9e4b0` and `ed53fb4`. It leaves embedding, Theiler window, horizon, fit
  interval, threshold, and promotion outside the statistic. Focused 4 tests /
  4 subtests, full pytest 278 tests / 84 subtests, stdlib discovery 200 tests,
  `compileall`, and `git diff --check` passed. Spec/code/test SHA-256 values:
  `0aeac9613f594c1b734fba4295afae53ba26bf882948a890f4e037521192a8cf`,
  `c064b1c037f5bcceff6c4d80e5ce5c8111425041629a1e82db7b8e14ca0c2b2e`,
  `361fc454eb7835f7c6d54d1f7129882012fff5c65297108917efc871d6bec4cf`.
  No scientific fixture or threshold was scored. Before Stage A, freeze a
  fresh untouched-data ledger with explicit Mackey--Glass and coordinate-
  complete full-state Lorenz--96 positives, stable and shuffled controls,
  embedding/normalization, all statistic choices, hashes, seeds, exact
  command, and an all-positive/no-control rule. Stage B remains prohibited.

- [x] 2026-07-20: Extend the active-repository README after the frozen
  conditional transition-entropy null. Clean commit `f231844` records the
  full-state Lorenz--96 false positives, preserves V1's pre-score failure and
  V2's unchanged scientific choices, prohibits tuning/rescoring, and keeps
  Stage B closed. Full pytest, stdlib discovery, `compileall`, and
  `git diff --check` exited successfully. README SHA-256:
  `2e7db869b747699c5ff8a9f6bf0b53a9a50e5222407337a56619f70ba6aa9322`.
  No scientific fixture was scored.

- [x] 2026-07-20: Frozen conditional transition-entropy Stage A at clean
  commit `ba510c3` failed: both positives passed, but stable and shuffled
  full-state Lorenz--96 were false positives. V1 failed before producing a
  score; v2 preserved all scientific choices. No tuning; Stage B remains closed.

- [x] 2026-07-20: Specify and unit-implement conditional transition entropy at
  clean active-repository commit `da52b36`. Focused 4 tests / 5 subtests, full
  pytest 272 tests / 80 subtests, stdlib 194 tests, `compileall`, and
  `git diff --check` passed. Spec/code/test SHA-256 values:
  `cf30032c3d51001cf7b0e74245481ae01dfa70b366bd0e77f54d46a78bccabee`,
  `7a313d60e802243dd0533d0a4fb2831eff766c5ecc7cc7be93a22b85f648bd61`,
  `72dfcbdb4c2f35ff87761855f9698e51cda6450a92f55aa37fbd7571e6aeec27`.
  No scientific fixture was scored. Freeze a causal prefix-only representation,
  fresh Mackey--Glass/full-state Lorenz--96 positives and controls, direction,
  threshold, hashes, seeds, exact command, and all-fixtures rule before Stage A.

- [x] 2026-07-20: Extend the active-repository README guardrail after the
  frozen repeated-renormalization Stage-A null. Clean commit `6737178` records
  the Mackey--Glass false negative, closes the inspected fixtures to tuning or
  rescoring, and preserves the bounded non-claim and Stage-B prohibition.
  Full pytest passed 268 tests / 75 subtests; stdlib discovery passed 190
  tests; `compileall` and `git diff --check` passed. README SHA-256:
  `420c6f42197e6448601a167c27781ccc019240c538df71cc0372313cb2a2e8f3`.

- [x] 2026-07-20: Specify then unit-implement an additive repeated-
  renormalization aggregation seam at clean active-repository commits
  `354e48b` and `3abebb1`. It reports time-weighted mean log growth from
  externally supplied `(initial, final, elapsed_steps)` cycles, with
  hand-calculated growth/contraction, unequal-duration weighting, scale/order
  invariance, and fail-closed tests. Focused 3 tests / 8 subtests, full pytest
  267 tests / 75 subtests, stdlib discovery 189 tests, `compileall`, and
  `git diff --check` passed. No scientific fixture or threshold was scored.
  Before Stage A, freeze fresh Mackey--Glass and full-state Lorenz--96
  positive/stable regimes, delay/vector perturbation and renormalization
  procedures, negative controls, thresholds, hashes, seeds, and exact command.
  Previously inspected fixtures remain closed; Stage B stays prohibited.

- [x] 2026-07-19: Extend the active-repository README guardrail after the
  frozen recurrence-determinism, paired-divergence, and correlation-form 0--1
  Stage-A nulls. It now records that all three predeclared gates failed,
  explicitly prohibits tuning/rescoring their fresh Mackey--Glass and
  full-state Lorenz--96 fixtures, and keeps Stage B closed pending a genuinely
  new outcome-independent detector hypothesis and separately frozen ledger.
  Clean active-repository commit `e7171fe`; README SHA-256
  `4c620dd865d611ebfb655655997c0d18ecc605a8f109bca775dee054f56ad005`.
  Documentation-only validation: full pytest (264 tests / 67 subtests), stdlib
  discovery (186 tests), `compileall`, and `git diff --check` passed; no
  scientific fixture was scored.

- [x] 2026-07-19: Freeze and run correlation-form 0--1 Stage A at clean commit
  `76d5deb` on fresh Mackey--Glass and coordinate-complete full-state 8D
  Lorenz--96 positive/stable pairs. Neither positive crossed the fixed 0.5
  threshold (scores `-0.376806` and `-0.094289`); both stable controls were
  rejected. No tuning; Stage B remains prohibited. Evidence:
  `experiments/20260720T031500Z-zero-one-calibration-v1/RUN.md`.

- [x] Implement the separately specified median correlation-form 0--1 chaos
  statistic without scoring any scientific fixture. Specification frozen at
  clean active-repository commit `9ca744e` with explicit externally supplied
  frequencies/max lag, oscillatory correction, fail-closed behavior, and a
  unit-only acceptance gate. Completed at clean active-repository commit
  `2d72a48`: focused 6 tests / 18 subtests, full pytest 263 tests / 67
  subtests, stdlib discovery 185 tests, `compileall`, and `git diff --check`
  passed. No scientific fixture was scored. A new frozen Stage-A ledger is
  required before any Mackey--Glass or full-state Lorenz--96 measurement;
  Stage B stays closed.

- [x] 2026-07-19: Frozen paired-divergence Stage A failed at clean commit
  `4cc2441`: Mackey--Glass tau=17 was a false negative and stable full-state
  Lorenz--96 F=1 was a false positive. No tuning; Stage B remains prohibited.
  See `experiments/20260719T211500Z-paired-divergence-calibration-v1/RUN.md`.

- [x] 2026-07-19: Specify and unit-implement an additive paired log-separation
  slope seam at clean active-repository commit `2be5f1b`, without scoring a
  scientific fixture. It recovers signed rates on hand-constructed exponential
  growth/contraction, supports scalar/vector trajectories, and fails closed on
  invalid pairs. Focused 12 tests / 16 subtests, full pytest 256 tests / 49
  subtests, stdlib discovery 178 tests, `py_compile`, and `git diff --check`
  passed. Before Stage A, freeze a new ledger with explicit fresh Mackey--Glass
  and full-state Lorenz--96 pairs, stable/negative controls, perturbations,
  fit windows, thresholds, hashes, seeds, exact command, and no-tuning rule.

- [x] 2026-07-19: Frozen Stage-A recurrence-determinism calibration failed on
  a stable Lorenz--96 false positive (`DET=1.0`); Stage B prohibited, no tuning.
  Evidence: `experiments/20260719T171500Z-recurrence-determinism-calibration-v1/RUN.md`.

- [x] 2026-07-19: Specify and unit-implement a replaceable Stage-A recurrence-
  determinism statistic without scoring a scientific fixture. Clean active-
  repository commit `30f8650` hand-validates diagonal-run accounting, isolated
  recurrences, scalar/vector agreement, invariance, and fail-closed inputs.
  Focused 7 tests, full pytest 251 tests / 45 subtests, stdlib discovery 173
  tests, `py_compile`, and `git diff --check` passed. The protocol, radius,
  embedding, threshold, Mackey--Glass/full-state Lorenz--96 positives, matched
  non-chaotic/shuffled controls, hashes, seeds, and command must still be frozen
  in a new experiment ledger before any Stage-A outcome is inspected.

- [x] 2026-07-19: Separate detector identification from CLA grammar coding in
  an outcome-independent validation-ladder spec. Clean active-repository commit
  `bc15f8f` requires a frozen Stage A discrimination gate before any separately
  frozen Stage B complete-code gate, retains explicit Mackey--Glass and full-
  state Lorenz--96 calibration, and keeps all inspected suffixes closed. No
  fixture was scored. Focused recurrence tests passed 13/13; full pytest passed
  244 tests / 33 subtests; `py_compile` and `git diff --check` passed. One stale
  focused selector failed before tests ran and is recorded in `NOTES.md`.

- [x] 2026-07-19: Make the active repository README fail-safe after the frozen
  scalar/vector calibration nulls. Commit `4973b7e` documents the recurrence
  APIs, clarifies that radius calibration is external and prefix-only, records
  the Mackey--Glass/Lorenz--96 complete-code nulls, and prohibits inspected-
  suffix tuning or proxy promotion. Focused recurrence checks passed 13 tests /
  23 subtests; the full suite passed 244 tests / 33 subtests; `py_compile` and
  `git diff --check` passed. No fixture was scored.

- [x] 2026-07-19: Freeze and run the full-vector recurrence gate on untouched
  full-state Lorenz--96 plus explicit fresh Mackey--Glass calibration. At clean
  commit `c667c02`, all integrity gates and 244 tests / 33 subtests passed, but
  compact CLA lost both positives to LZ78 (5,522.398 vs 2,000 bits and
  9,933.113 vs 5,304 bits). Neither shuffled null was promoted. No tuning; see
  `experiments/20260719T071500Z-vector-recurrence-attractor-v1/RUN.md`.

- [x] 2026-07-16: Created interim isolated cron worker `dce83d32-440a-4a6a-9305-04175f5ca50d`, scheduled every two hours at minute 15 of even hours (`America/Vancouver`). It advances the frozen held-out MDL/calibration gate and is intended to migrate to a task-specific ThreadKeeper persistent agent once that runtime is ready.

- [x] 2026-07-18: Specify and unit-implement additive causal ordinal-pattern
  symbolization at clean local commit `a7a7e7e`. Acceptance evidence: known
  permutations and ties, causal delay alignment, monotone-transform invariance,
  deterministic/fail-closed behavior, exact CLA reconstruction, focused 8
  tests / 10 subtests, full 225 tests / 10 subtests, `py_compile`, and
  `git diff --check`. Evidence:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay/docs/ordinal-pattern-symbolization-spec-v1.md`
  in the documented active worktree.
- [x] Before any ordinal-pattern detector measurement, create a separate frozen
  experiment ledger on new untouched Mackey--Glass and Lorenz--96 trajectories.
  Freeze raw fixture hashes, order/delay, causal prefix/suffix alignment, seeds,
  exact commands, compact/JSON CLA, canonical LZ78, simple parametric controls,
  matched nulls, and an all-positive pass rule. Do not rescore prior suffixes.
  Completed at clean commit `17a0778` on fresh Mackey--Glass initial 1.1 and
  Lorenz--96 x6 trajectories. All gates passed, but compact CLA lost both
  positives to LZ78 (9,235.184 vs 2,872 bits; 10,224.372 vs 3,928 bits), so
  the strict rule failed. No tuning; see
  `experiments/20260718T171500Z-ordinal-attractor-v1/RUN.md`.

- [x] Create a local prototype repo under `projects/chaos-language-algorithm/repos/chaoslang` using package name `chaoslang`.
- [ ] Keep a persistent CLA/Hyperseed/pattern-calculus subthread: analyze CLA-recognized emergent grammars in terms of language, emergent pattern, McBride derivatives, and pattern calculus; use Ben's linked `Weakness-Theory-10.pdf` Google Drive source as a study input when accessible.
- [x] Implement domain core first: immutable typed IDs, tokens, corpus, grammar, categories, state, edits, proposals, scores.
- [x] Implement symbolic-string MVP before trajectory symbolization: `CLA.simple().fit_symbols(...)`, NGramPatternMiner, chunk rewriting, approximate MDL, greedy induction loop.
- [x] Implement M1 symbolization for fixed partitions with deterministic tests after the string MVP is stable. Added stdlib-only fixed rectangular M1 symbolization plus Lorenz-63/Rössler controls in `repos/chaoslang` on 2026-07-04.
- [x] Implement M2 chunk-only grammar: n-gram proposals, non-overlapping replacement, rule expansion, use counts, dead-rule pruning.
- [x] Implement M3 MDL scoring and reject overhead-dominated edits.
- [x] Implement M4 hard category induction with context histograms, deterministic hard clusters, `M[v]` parse entries, and exact reconstruction. JS divergence remains deferred.
- [x] Implement M5 unified greedy search choosing the best negative delta-L edit.
- [x] Add persistence/reproducibility: JSON grammar/state format, edit-log replay, deterministic seeds, stable text rendering. Strict replay hardening is committed on `agent/strict-persistence-replay` at `f53ed55`: malformed, reordered, stale, partially applicable, and mismatched generated edits fail with indexed diagnostics; canonical-byte, complete-state, category, and generated-prune replay tests pass.
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
- [x] Run leakage-free rank-conditioned Lorenz-63 follow-up: 3 independent 2,048-point trajectories; train-only PCA/VAMP/TICA/clustering; ranks {3,10}, dimensions {2,3}, lags {1,4,16}, matched k {8,16}; blocked validation VAMP-2; and 20 circular block surrogates at lengths {4,16}. Linear VAMP beat best matched PCA on both primary metrics in 0/3 trajectories at each k, triggering the preregistered stop criterion. See `experiments/20260713T153839Z-lorenz63-rank-conditioned-vamp-tica/RUN.md`.
- [x] Replace further linear-VAMP tuning with a decision on the next scientifically distinct lane: calibrated CLA predictive/MDL coding first; nonlinear or lift-invariance studies require a new preregistered hypothesis. Retain temporal-block controls and leakage-safe nested evaluation.
- [x] Freeze the v1 benchmark protocol before implementation/runs: deterministic canonical persistence/replay, frozen untouched-suffix coding, fair model/state transmission costs, literal/unigram/Markov/current-proxy controls, and aggregate pass criterion. See `docs/frozen-heldout-mdl-preregistration-v1.md`.
- [x] Before execution, create the experiment record and freeze trajectory hashes, symbolization, seeds, temporal splits, baseline orders/smoothing, exact commands, and implementation commit. Completed for v1 at `experiments/20260716T172310Z-frozen-heldout-calibration-v1/RUN.md` against clean commit `c8e9e91`.
- [x] Implement frozen-suffix CLA coding and equivalent deterministic model encodings without suffix refitting. Branch `agent/frozen-suffix-scoring`, commits `5be45e5` + corrective `ce0e476`; explicit normalized ESC mass, Unicode-safe canonical literal payloads, transmitted Markov initial context, and decodable CLA grammar/count model excluding training corpus/parse/history. Corrected verification: 14 focused and 140 full tests pass. This establishes implementation behavior, not external compression gains.
- [x] Run the preregistered frozen held-out benchmark; only afterward consider blockwise prequential adaptation. Mackey--Glass and Lorenz--96 x0 passed all integrity gates but CLA failed aggregate coding: 65,976.621 bits versus strongest unigram 6,588.443. No suffix tuning. See `experiments/20260716T172310Z-frozen-heldout-calibration-v1/RUN.md`.
- [x] Since CLA failed the aggregate held-out gate, preregister and run the minimal joint chunk/category diagnostic to distinguish coding/accounting inadequacy from greedy-search blindness. The frozen 19-frame synthetic fixture classified `greedy_or_representation_blindness`: abstract joint score 75 versus initial/greedy 76 proxy bits, zero greedy edits, no intended singleton-member category proposal, and no member-agnostic `a M b` chunk after manual category application. This is separate from the failed attractor suffixes and is not scientific validation. See `experiments/20260716T191500Z-joint-chunk-category-diagnostic-v1/RUN.md`.
- [x] Specify and implement a replaceable, exact-reconstructing generalized category-slot proposal/production seam. It retains per-occurrence members for decoding while allowing mining/scoring to match category identity independently of the member; synthetic representation, complete-code, indexed-code, scorer, and learner-integration gates are complete.
  - 2026-07-16 domain/unit subgate complete at clean local commit `4632212`: additive `CategorySlot`, `GeneralizedChunkOccurrence`, generalized proposal miner/applier, ordered member side-table decoding, fail-closed malformed proposal checks, and exact 19-frame/76-token reconstruction. Focused 27 and full 150 tests passed; `git diff --check` passed. Spec: `docs/generalized-category-slot-spec-v1.md`. Still open: persistence/edit replay, fact projection, greedy joint-search integration, and a fair decodable model/member code. No new attractor benchmark is authorized yet.
  - 2026-07-16 persistence/fact subgate complete at clean local commit `bd7595c`: canonical JSON round-trip, strict edit-log replay, and fact projection preserve generalized productions plus ordered member side tables. Focused 43 and full 151 tests passed; `py_compile` and `git diff --check` passed. Still open: greedy joint-search integration and a fair decodable model/member code. No new attractor benchmark is authorized yet.
  - 2026-07-16 canonical transmission subgate complete at clean local commit `fe32c4a`: separate versioned canonical JSON model and parse documents charge every byte, category/slot, and ordered occurrence-member side table; decoding derives the corpus solely by exact expansion and re-encodes byte-stably. The frozen 19-frame/76-token fixture passed the complete-code round trip. Focused 43 and full 157 tests passed in bounded shards; `py_compile` and `git diff --check` passed. Still open: integrate joint category/generalized-chunk proposals with search and decide/preregister the next measured synthetic gate. No attractor benchmark is authorized yet.
  - 2026-07-16 joint reachability subgate complete at clean local commit `871a0c6`: a replaceable joint miner composes an exact-context category candidate (with a joint-only singleton occurrence threshold) and generalized slot mining on the temporary categorized state. On the frozen fixture it deterministically reaches and applies the intended move as two explicit replayable edits with exact reconstruction. Focused 7 and full 158 tests passed in bounded per-file shards; `py_compile` and `git diff --check` passed. Still open: freeze and run a measured synthetic accept/reject gate using the complete decodable state code, then integrate only the justified scorer/search behavior. The sprint-1 proxy is explicitly insufficient for that decision, and no attractor benchmark is authorized yet.
  - 2026-07-16 complete-code decision gate completed at clean corrective commit `8ffa31c`: the intended joint move was rejected by 64 bits (34,416 versus 34,352), despite saving 6,232 data bits, because it added 6,296 model bits. All integrity gates and 158 tests passed. The joint miner remains disabled; see `experiments/20260717T051500Z-generalized-complete-code-gate-v1/RUN.md`.
- [x] Specify an outcome-independent, decodable generalized-state code refinement and preregister its acceptance rule plus controls. Do not optimize against the Mackey--Glass/Lorenz--96 suffixes or enable joint acceptance under the sprint-1 proxy; no new attractor benchmark is authorized yet.
  - 2026-07-17 specification/unit subgate complete at clean local commit `8a46900`: additive `indexed_state_code` transmits one sorted shared token table and uses integer references uniformly in literal and generalized grammar/parse/category/member records. It decodes without a stored corpus, re-encodes byte-identically, and fails closed on malformed tables/references. Focused 20 and full 165 tests passed; `py_compile` and `git diff --check` passed. Spec: `docs/indexed-state-code-spec-v1.md`. No candidate codelength comparison or attractor suffix inspection occurred. Still open: preregister acceptance rule and controls in a new experiment ledger before measuring the frozen synthetic fixture.
  - 2026-07-17 frozen indexed decision gate complete at clean local commit `29a52fd`: indexed joint state 9,760 bits versus indexed literal 10,616 (-856), while the canonical-v1 control exactly reproduced 34,416 versus 34,352 (+64). All integrity gates and 165 tests passed. This synthetic acceptance permits only a separately specified/unit-tested indexed joint-search scorer; it does not enable the learner or authorize attractor reruns. Provenance: `experiments/20260717T091500Z-indexed-complete-code-gate-v1/RUN.md`.
  - 2026-07-17 indexed joint-search scorer unit gate complete at clean local commit `a5a0772`: the replaceable scorer applies a proposal, requires unchanged exact reconstruction, charges both states with the same complete indexed codec, accepts only strictly negative deltas, and uses order-independent deterministic tie-breaking. Previously measured unit controls reproduce 19-frame acceptance (-856 bits) and two-frame rejection (+256 bits); replay and corpus-free decoding pass. Focused 17 and full 168 tests passed in bounded per-file processes; `py_compile` and `git diff --check` passed. Spec: `scratch/chaoslang-strict-replay/docs/indexed-joint-search-scoring-spec-v1.md`. The scorer and joint miner remain disabled in `CLA.fit_symbols`; next is a separate learner-integration spec/unit gate, not an attractor rerun.
  - 2026-07-17 indexed learner-integration unit gate complete at clean local commit `24d9771`: `search_objective="indexed"` makes every enabled ordinary/joint proposal compete under the same complete indexed code, while joint search under the sprint-1 proxy fails closed and defaults remain unchanged. The 19-frame positive control reaches the previously frozen 9,760-bit state and the two-frame negative remains literal at 1,944 bits, both with exact reconstruction and stored-score equality. Focused 20/38/11 checks and all 171 tests passed in bounded shards; `py_compile` and `git diff --check` passed. Spec: `scratch/chaoslang-strict-replay/docs/indexed-learner-integration-spec-v1.md`. This is synthetic plumbing only. Next is to preregister a genuinely untouched Mackey--Glass/Lorenz--96 calibration v2 with explicit controls, hashes, seeds, commands, and a strict no-tuning rule before any measured attractor run.
- [x] Preregister and run untouched indexed held-out calibration v2. At clean commit `580f917`, new Mackey--Glass initial 0.7 and Lorenz--96 x3 trajectories passed every integrity gate, but primary indexed CLA used 21,989.324 aggregate bits versus 6,739.904 for unigram. No joint move was accepted, so indexed joint/no-joint controls were identical. Full 176-test suite passed. This is a coding null; no suffix tuning or attractor/semantic claim. See `experiments/20260717T151800Z-frozen-heldout-calibration-v2/RUN.md`.
- [x] Preregister and run a necessary synthetic detector-validity gate before any further attractor calibration. At clean commit `64b3b33`, all integrity gates passed and the shuffled matched null was correctly rejected, but indexed CLA failed the repeated de Bruijn-5 positive: 4,600.700 total bits versus unigram at 2,608.721. Its suffix cost was only 0.700 bits, but complete model transmission dominated. No fixture-length/code tuning and no renewed attractor run. See `experiments/20260717T171800Z-synthetic-detector-calibration-v1/RUN.md`.
- [x] Specify and run a new outcome-independent synthetic sample-complexity hypothesis without reusing the de Bruijn-5 or attractor suffixes. At clean commit `b3709d8`, the frozen repeated Zimin-5 positive first beat the strongest complete-code baseline at 64 suffix repeats and remained ahead at the decisive 256-repeat horizon (4,717.151 versus Markov-2 at 8,515.866 bits); the exact-marginal shuffled null never crossed. All integrity gates and 180 tests passed. This is one-family synthetic finite-sample competence only; see `experiments/20260717T191500Z-synthetic-sample-complexity-v1/RUN.md`.
- [x] Preregister and run a source-family generalization gate using structurally distinct non-Zimin synthetic generators and matched nulls. At clean commit `e6e3ed2`, all gates passed, CLA beat Markov-2 on Thue--Morse (7,195.523 versus 8,700.081 bits), and both shuffled nulls were correctly rejected, but CLA lost on Fibonacci word (6,131.278 versus Markov-2 at 5,843.219). The all-family rule therefore failed. No suffix/split/code tuning and no renewed attractor run; see `experiments/20260717T211500Z-synthetic-family-generalization-v1/RUN.md`.
- [x] Require a new outcome-independent detector hypothesis before another measured gate. The mechanism-specific constant-length-substitution hypothesis was frozen on two new sources at clean commit `d854bc7`; CLA beat the strongest preregistered complete-code control on period-doubling (5,452.003 versus 7,872.544) and Rudin--Shapiro (9,602.305 versus 9,773.770), while rejecting both shuffled nulls. All gates and 137 tests passed. This bounded synthetic result does not revise the Fibonacci or attractor nulls; see `experiments/20260717T231900Z-synthetic-uniform-morphism-v1/RUN.md`.
- [x] Specify and unit-validate a fair decodable universal-sequence-code control before another measured detector claim. At clean local commit `9737c37`, additive canonical LZ78 v1 fully charges a magic/version header, sorted UTF-8 token table, original length, phrase records, and terminal record; exact decoding, byte-stable re-encoding, Unicode/empty/terminal cases, and fail-closed malformed inputs passed 14 focused and 198 full pytest checks. No benchmark fixture was scored. Spec: `scratch/chaoslang-strict-replay/docs/universal-sequence-code-control-spec-v1.md`.
- [x] Separately preregister and run a new untouched synthetic comparison including canonical LZ78 v1. At clean local commit `4941890`, all integrity gates passed on new Cantor and regular-paperfolding positives plus exact-marginal shuffled nulls, but CLA lost both required positives to unigram complete code (7,219.814 vs 2,447.226 bits; 7,380.844 vs 5,669.774). CLA beat LZ78 only on paperfolding, not the strongest control, and neither null was promoted. Focused 16/16 and full 200/200 pytest checks passed. See `experiments/20260718T031500Z-synthetic-universal-control-v1/RUN.md`; no inspected suffix may be tuned or rescored.
- [x] Specify and unit-validate an additive finite complete-model-cost seam without scoring an inspected fixture. At clean local commit `2feb70d`, compact indexed model code v1 canonically encodes the unchanged indexed frozen-model object with typed tags, minimal unsigned varints, strict UTF-8, and complete byte charging. It preserves canonical JSON model semantics and unchanged suffix bits, while failing closed on malformed/noncanonical input. Focused 12/12 and full pytest 209/209 checks passed with `py_compile` and `git diff --check`. Spec: `scratch/chaoslang-strict-replay/docs/compact-indexed-model-code-spec-v1.md`.
- [x] Before another measured detector gate, freeze a new experiment ledger for the compact-model hypothesis using untouched sources/splits/hashes/seeds/commands/pass criteria, retaining canonical JSON CLA, canonical LZ78, and simple parametric controls. At clean commit `4174095`, all integrity gates passed and compact transmission saved 464--648 bits versus JSON CLA, but the strict two-source gate failed: compact CLA beat Markov-2 on the four-state 2-uniform positive (5,146.362 vs 5,496.923 bits) and rejected both shuffled nulls, but lost the complementary 3-uniform positive to unigram (5,865.104 vs 5,669.836). See `experiments/20260718T071500Z-synthetic-compact-model-v1/RUN.md`; no new suffix may be tuned or rescored.
- [x] Freeze and run an outcome-independent phase-robustness gate on a new three-state 2-uniform source at offsets zero and one, retaining compact/JSON CLA continuity, canonical LZ78, simple parametric controls, and exact-marginal shuffled nulls. At clean commit `a080199`, every integrity gate passed, but compact CLA lost both positives to LZ78 (4,257 vs 2,760 bits; 4,131 vs 2,760) while rejecting both nulls. See `experiments/20260718T091500Z-synthetic-phase-robustness-v1/RUN.md`; no phase or suffix tuning and no renewed attractor calibration.
- [x] Require a genuinely new outcome-independent detector hypothesis and untouched-data protocol before any further measured gate. The frozen long-horizon bridge at clean commit `cbbebfd` used fresh Mackey--Glass initial 0.9 and Lorenz--96 x5 streams, explicit matched shuffled nulls, compact/JSON CLA, LZ78, and simple complete-code controls. All gates passed, but neither positive crossed at any horizon; at 65,536 symbols CLA lost 72,723.386 vs Markov-1 25,006.425 bits and 103,647.803 vs 43,859.342 bits. See `experiments/20260718T131500Z-attractor-amortization-v1/RUN.md`.
- [x] Compile a comprehensive July 15 CLA experiments report covering baseline, Lorenz--96 high-D failure, lifted R256 studies, rank-conditioned linear-VAMP null, current implementation status, and the fresh OmegaSim preregistered result: `repos/chaoslang/docs/cla_experiments_comprehensive_20260715.pdf`.

## Attractor benchmark sprint

- [x] Implement dependency-light trajectory generators/symbolizers for logistic map, Lorenz-63, Rössler, Mackey-Glass, and Lorenz-96. On 2026-07-16 corrected Mackey--Glass `tau` to physical time (`tau/dt` delay steps), added the prefix-only frozen calibration harness, and retained explicit Lorenz--96 x0/full-state scope limits at commit `c8e9e91`.
- [ ] Run CLA on a small variety of strange attractors and non-chaotic controls with recorded seeds/parameters. A small command exists (`python3 -m chaoslang.benchmarks.m1_controls`) for Lorenz-63/Rössler JSON summaries; no experiment record has been created yet.
- [ ] Include benchmark dimensions up to the vector dimensionality relevant to OmegaSim starter traces.
- [ ] Defer much higher-dimensional traces until a dedicated dimension-reduction step exists.
- [ ] Record each benchmark run under `experiments/` with parameters, exact command, outputs, and conclusion.

## Scaling / reviewer follow-up

- [x] Replace the brute-force n-gram window counter with a bounded suffix-trie-backed miner for high-cardinality compound-symbol streams; regression tests cover compound symbols and a high-cardinality repeated motif. Implemented on `agent/suffix-trie-miner` in `repos/chaoslang`.
- [x] Add/update the CLA expert-review prompt to ask explicitly for algorithmic/data-structure inefficiencies: n-gram brute force, context histogram duplication, compound-symbol storage/copying, repeated MDL re-encoding, and suitable trie/index/hash/sparse alternatives. See `docs/cla_expert_review_prompt.md`.
- [ ] Benchmark the bounded suffix-trie miner on real 1024-step × ~20D CLA streams after the JS/dimension-reduction symbolization path is available; compare wall time and peak memory against the old brute-force miner if preserved in a fixture.
  - 2026-07-09 local first slice: ran Lorenz-96 control at 1024 steps × 20D with `--miner suffix_trie --category-method js`; exact reconstruction true, 510 unique symbols, 8 chunk rules, score_total 1021.2, fit_wall_time_seconds ~2.55. Evidence: `experiments/20260709T192728Z-lorenz96-1024-dim20-suffix-trie/RUN.md`. Still needs real OmegaSim stream/dim-reduction path, peak-memory capture, and true brute-force comparison fixture.

## 2026-07-18 fixed-model amortization gate

- [x] 2026-07-18: Specify and unit-implement additive causal full-vector
  recurrence-lag symbolization at clean local commit `7c507b8`. The seam uses
  fixed-radius Euclidean returns, preserves one symbol per vector, fits no
  state, and is causal plus translation/rotation invariant. Focused 13 tests /
  23 subtests and full 242 tests / 33 subtests passed with `py_compile` and
  `git diff --check`. No trajectory or held-out suffix was scored. Any measured
  full-state Lorenz--96 gate requires a separate frozen new-data ledger with a
  prefix-only radius rule and all complete-code controls retained.

- [x] Freeze and run one new untouched long-horizon synthetic comparison. At
  clean commit `d299b2f`, compact CLA first crossed at 16,384 symbols and won
  the final 65,536-symbol positive (28,828.051 vs Markov-2 60,768.987 bits),
  while the shuffled null never crossed. All gates and 215 tests passed.
- [x] Specify and run a frozen bridge hypothesis connecting symbolic
  amortization to fresh chaotic trajectory symbol streams. The strict gate
  failed at clean commit `cbbebfd`; all 217 tests and integrity gates passed.
- [x] Specify and unit-validate a genuinely different outcome-independent
  dynamics representation before any further attractor measurement. Causal
  recurrence-lag symbols encode the nearest prior return within an explicit
  radius into bounded lag classes. Clean commit `de6f85f` passed 8 focused
  tests / 13 subtests and the full 235-test / 23-subtest suite, compilation,
  and `git diff --check`; no scientific fixture was scored. Spec:
  `scratch/chaoslang-strict-replay/docs/causal-recurrence-symbolization-spec-v1.md`.
- [x] Before measuring recurrence-lag symbols, freeze a separate ledger on new
  untouched Mackey--Glass and Lorenz--96 trajectories. Freeze a prefix-only
  radius rule, lag bins/max lag, fixture and split hashes, seeds, commands,
  compact/JSON CLA, LZ78 and parametric controls, matched nulls, and an
  all-positive rule. Do not tune or rescore any inspected stream.
  - 2026-07-18 protocol/harness subgate: commits `3a6ef3f` and corrective
    `9cd3cf0` add the written protocol, deterministic declarations, controls,
    and declaration tests. A pre-outcome integrity check rejected the original
    5%-of-prefix-range radius because both positive suffixes collapsed entirely
    to `rl0` and had identical hashes. The corrected frozen candidate uses the
    prefix-only nearest-rank 10th percentile of adjacent increments and yields
    nondegenerate, distinct symbol streams. Focused 10 tests / 13 subtests and
    full 237 tests / 23 subtests passed with compilation and `git diff --check`.
    No coding outcome was run or inspected before the freeze. The timestamped
    ledger then ran once at clean `9cd3cf0`; every integrity gate passed, but
    compact CLA lost both positives (Mackey--Glass 9,954.129 vs LZ78 5,008;
    Lorenz--96 x7 13,697.457 vs unigram 7,814.621). The frozen rule failed;
    no tuning. Evidence: `experiments/20260719T011500Z-recurrence-attractor-v1/RUN.md`.
# 2026-07-20 repeated-renormalization Stage-A outcome

- [x] Freeze fresh Mackey--Glass/full-state Lorenz--96 repeated-renormalization
  fixtures, stable controls, hashes, configuration, and exact command before
  score production.
- [x] Run the bounded local gate once at clean commit `793f10c`; integrity and
  test gates passed, but Mackey--Glass was a false negative, so the strict gate
  failed.
- [ ] Keep Stage B closed. Do not tune or rescore the inspected fixtures; any
  next detector must be genuinely outcome-independent and separately frozen.
# 2026-07-23 adaptive-coding upgrade

- [x] Preserve Ben's two governing documents verbatim with SHA-256 manifest in
  `repos/chaoslang/docs/`.
- [x] Complete M-A: protocols, growing KT estimator, adaptive Markov coder,
  unchanged LZ78 wrapper, registry, and applicable M-A tests. Evidence:
  active-worktree commit `6145e1d`; focused 14 tests and full 216-test stdlib
  discovery passed; `compileall` and `git diff --check` passed.
- [ ] Implement M-B instrumentation next: proposal ledger, legacy replay
  6,232/6,296/+64 regression, exactly-one-record invariant, and final
  breakdown reconciliation. Acceptance command:
  `PYTHONPATH=src python3 -m unittest discover -s tests -v`.
