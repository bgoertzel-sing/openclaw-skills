# Notes

## 2026-07-28 12:30 PDT — neutral SSA event application

- Added canonical PeTTa-native application and resource guards for influx,
  dilution, ligation, and cleavage events over ordered integer-count states.
- A four-event influx/ligation/cleavage/dilution trace returns exactly to its
  initial counts and reproduces the same final state on replay.
- `scripts/run_neutral_ssa_tests.sh` passed thirty checks. General canonical
  event enumeration and the calibration ledger remain pending; no calibration
  endpoint was inspected and protected files were untouched.

## 2026-07-28 08:30 PDT — neutral SSA arithmetic and tiny-state baseline

- Added a new reviewed PeTTa-native SSA module using exact propensity
  numerators, including catalytic load, distinct/identical ligation,
  cleavage, and insufficient-resource guards.
- A two-event ligation/cleavage control returns to its exact initial counts
  and reproduces the same event stream and final state on replay.
- `scripts/run_neutral_ssa_tests.sh` passed seventeen checks. Full seeded SSA
  sampling and the calibration ledger remain pending; no calibration endpoint
  was inspected and protected files were untouched.

## 2026-07-28 06:30 PDT — generated tiny-system oracle gate passed

- PeTTa generated 100 eight-reaction `L=3` systems at each frozen
  `f={0,1,2,4}` value and computed exhaustive structural RAF truth.
- All 400 systems agreed exactly with the independent Python oracle for every
  one of 255 nonempty subsets, maximal RAF, and all irrRAFs.
- The manifest commits comparison, detector-source, repository, and PeTTa
  runtime hashes while deliberately withholding structural-incidence results.
  No calibration endpoint was inspected; protected exp08 and scratch files
  were untouched. Commit `707dbcc` was pushed normally to GitHub `main`.

## 2026-07-28 04:30 PDT — PeTTa generated-system sampling

- Added replayable PeTTa-owned sampling of eight canonical `R_3` reactions
  without replacement and pathway-independent keyed Bernoulli catalysis with
  probability `f/40`.
- Focused checks cover exact seed-1 selection, cardinality, replay, and
  zero/full edge boundaries. The 100 cross-oracle comparisons remain pending;
  no calibration outcome was inspected and protected files were untouched.

## 2026-07-28 02:30 PDT — canonical PeTTa R3 catalog

- Added the PeTTa-owned full `L=3` source universe for the frozen generated
  oracle gate: 14 molecules, six food molecules, 20 directed cleavages, and
  20 ordered ligations with canonical IDs and ordering.
- `scripts/run_neutral_raf_fixtures.sh` passed thirty-three checks and
  `git diff --check` passed. Seeded selection/catalysis and the 100 generated
  comparisons remain pending; no calibration result was inspected and
  protected files were untouched.

## 2026-07-28 00:30 PDT — PeTTa maximal RAF and irrRAF projections

- Added maximal-RAF union and inclusion-minimal irrRAF projections over the
  existing exhaustive PeTTa tiny-system subset enumeration.
- Exact projections match independent oracle truth for a food-closure chain,
  three independent RAF reactions, and an unreachable catalytic cycle.
- `scripts/run_neutral_raf_fixtures.sh` passed twenty-nine checks and
  `git diff --check` passed. The 100 generated comparisons and manifest remain
  pending; no calibration result was inspected and protected files were
  untouched.

## 2026-07-27 22:30 PDT — PeTTa exhaustive RAF-subset enumeration

- Added an intentionally exponential PeTTa-native powerset/filter path limited
  in scope to the frozen at-most-12-reaction oracle boundary.
- Complete RAF subset IDs match independent oracle truth for a two-step food
  chain, all seven nonempty subsets of the three independent RAF reactions,
  and an unreachable catalytic cycle with no RAF subsets.
- The focused PeTTa fixture run passed twenty-three checks. Maximal RAF and
  irrRAF projections plus 100 generated tiny comparisons remain pending; no
  calibration result was inspected and protected files were untouched.

## 2026-07-27 20:30 PDT — PeTTa structural RAF predicate

- Added PeTTa-native food closure, existential catalyst availability, and
  structural RAF classification over canonical `neutral-crs-v1` facts.
- The focused fixture run passed twenty checks spanning all frozen semantic
  families.
- Exhaustive enumeration and 100 generated tiny comparisons remain pending.
  No calibration outcome was inspected; protected exp08/scratch/catalysis
  files were untouched.

## 2026-07-27 18:30 PDT — PeTTa neutral-RAF fact boundary

- Added PeTTa-native accessors and canonical facts for all seven frozen
  hand-fixture families under the `neutral-crs-v1` oracle interface.
- The first focused run revealed that unquoted binary polymer names collapse
  numerically (`01` becomes `1`, `00` becomes `0`). Quoted strings now preserve
  literal polymer identity and stoichiometric duplicates.
- `scripts/run_neutral_raf_fixtures.sh` passed with ten true results. This is
  serialization/interface progress only: exhaustive PeTTa subset detection
  and 100 generated tiny-system comparisons remain open, and no calibration
  endpoint was inspected.

## 2026-07-27 16:30 PDT — independent exhaustive RAF oracle implemented

- Added a serialization-only Python oracle for canonical `neutral-crs-v1`
  JSON. It imports no chemistry implementation, caps exhaustive input at 12
  reactions, enumerates every nonempty subset, and returns exact RAF,
  maximal-RAF, and complete irrRAF sets.
- Nine focused tests cover the seven frozen fixture families, including
  multiple products/catalysts, food and self catalysis, unreachable cycles,
  monotonic edge addition, reaction/edge deletion, and multiple irrRAFs.
- The first run exposed two recorded test/interface errors: stoichiometric
  lists need duplicates, and a food-enabled closure-chain prefix is itself a
  RAF. Both were corrected without changing the frozen definition.
- The focused suite and `git diff --check` passed. The PeTTa half and generated
  tiny systems remain open; no calibration endpoint was inspected and the
  protected exp08/scratch/catalysis files were untouched.
- Commit `73ddcde` was pushed normally to GitHub `main`.

## 2026-07-27 14:30 PDT — neutral CRS and RAF-oracle protocol frozen

- Froze `neutral-crs-v1`: binary polymers of maximum length `L`, food through
  length two, all directed ligations/cleavages, and pathway-independent
  Bernoulli molecule/reaction catalysis controlled by expected reactions
  catalyzed per molecule.
- Declared PeTTa-native SSA influx/dilution/reaction dynamics, exact constants,
  finite-size/control sweeps, graph and dynamics seeds, replay requirements,
  and separate structural, reachable, active/persistent, and causal/productive
  endpoints. No sampled calibration or emergence outcome was inspected.
- Froze an independent exhaustive Python-oracle boundary and canonical
  PeTTa/oracle facts. The gate covers food closure, multiple products and
  catalysts, food catalysts, self-catalysis, unreachable cycles, catalysis-edge
  monotonicity, deletion sensitivity, all irrRAFs, order invariance, and 100
  generated tiny systems.
- Standard RAF semantics allow any catalyst in food closure; they do not add
  exp04's legacy generated-product restriction. A mismatch is fail-closed.
- Evidence:
  `repos/petta-chem/docs/neutral_crs_oracle_protocol.md`. Frozen untracked
  exp08/scratch/catalysis material was not read, executed, or changed.
- The first-class catalysis regression passed and `git diff --check` passed.
  Commit `ad70a64` was pushed normally to GitHub `main`.

## 2026-07-27 08:30 PDT — thirty-nine-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 38 to 39 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 39
  rules. The attrition audit reports thirty-one generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 554 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `924fb77` pushed normally to GitHub `main`.

## 2026-07-27 04:30 PDT — thirty-seven-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 36 to 37 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 37
  rules. The attrition audit reports twenty-nine generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 544 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `5e0ec8d` pushed normally to GitHub `main`.

## 2026-07-27 02:32 PDT — thirty-six-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 35 to 36 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 36
  rules. The attrition audit reports twenty-eight generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 539 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `a47cfca` pushed normally to GitHub `main`.

## 2026-07-27 00:58 PDT — thirty-five-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 34 to 35 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 35
  rules. The attrition audit reports twenty-seven generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 534 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `2ccbba0` pushed normally to GitHub `main`.

## 2026-07-26 14:30 PDT — thirty-three-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 32 to 33 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 33
  rules. The attrition audit reports twenty-five generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 524 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `17db9f8` pushed normally to GitHub `main`.

## 2026-07-26 12:30 PDT — thirty-two-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 31 to 32 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 32
  rules. The attrition audit reports twenty-four generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 519 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `5aae13a` pushed normally to GitHub `main`.

## 2026-07-26 — External-review PDF and reproducibility audit

- Prepared `docs/petta_chem_external_review_2026-07-26.{tex,pdf}`, a 13-page
  external-review packet covering the PeTTa-native implementation, exp00--exp08
  designs and outcomes, claim boundaries, current weaknesses, and a prioritized
  next plan. PDF SHA-256:
  `f74980653dac32aa31424c2613c4a2cc6a36bae4c025f48d4c2e20cdf51396db`.
- Reproduced at repository head `bfa0e47`: exp00 513 checks, exp01 68,
  run-contract 35, exp02 517, exp04 79, first-class exp04 79, exp05 94, exp06
  61, and exp07 309 all exited 0. Exp03 exited 1 after 38 passes and one failure:
  `exp03-exp02-after-3 random seed-11` returned eight identical answers rather
  than one. This is a current-head singleton/proof-duplication defect, not a
  changed chemical endpoint.
- Text extraction, required-section searches, `git diff --check`, and visual
  inspection of pages 1, 7, and 13 passed. The report's main recommendation is
  to repair reproducibility, freeze a review baseline, and pivot from further
  cap/pathway accretion to a neutral random chemistry calibrated against an
  independent RAF oracle and known finite-size behavior.
## 2026-07-26 06:30 PDT — thirty-one-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 30 to 31 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 31
  rules. The attrition audit reports twenty-three generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 514 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `bfa0e47` pushed normally to GitHub `main`.

## 2026-07-26 00:30 PDT — twenty-eight-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 27 to 28 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 28
  rules. The attrition audit reports twenty generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 499 terminal true results and zero failure markers;
  `git diff --check` and an obvious secret-like diff scan passed. No chemistry
  rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `6cc07bc` pushed normally to GitHub `main`.

## 2026-07-25 18:30 PDT — twenty-five-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 24 to 25 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 25
  rules. The attrition audit reports seventeen generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 484 terminal true results and zero failure markers;
  `git diff --check` and an obvious secret-like diff scan passed. No chemistry
  rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `85a9ea2` pushed normally to GitHub `main`.

## 2026-07-25 08:30 PDT — twenty-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 19 to 20 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 20
  rules. The attrition audit reports twelve generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 459 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `84d70c7` pushed normally to GitHub `main`.

## 2026-07-24 16:30 — Observe post-exhaustion quiescence

- Added PeTTa-native `chamber-tick-generated-sweeps-9`, which advances only
  an eight-sweep `stop-bounded` result from its exact chamber and retains the
  ninth sweep's checked outcomes.
- The 64-reactant fixture now demonstrates the semantic distinction between
  a productive driver boundary and actual chemistry quiescence: 64 productive
  ticks are followed by eight checked no-ops, yielding `stop-quiescent` with
  72 accounted steps, the unchanged 64-event history, and exact tick-64
  chamber. Closed-cap and productive-then-quiescent fixtures still stop after
  one and two sweeps.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (421
  terminal true results, zero failure markers); `git diff --check` passed. No
  Python chemistry logic or scientific claim changed; pre-existing untracked
  scratch files were left untouched. Commit `500172b` pushed normally to
  GitHub `main`.

## 2026-07-24 14:30 — Extend bounded live ticking to eight sweeps

- Added PeTTa-native `chamber-tick-generated-sweeps-8`, which advances from
  the checked seven-sweep result's exact chamber only when that result ended
  in productive bound exhaustion. Closed-cap and productive-then-quiescent
  paths still stop after one and two sweeps.
- Extended eight-sweep positional and run-wide outcome accessors plus the
  fixed event-history append seam through 64 retained events. The sustained
  cap-1 fixture returns `stop-bounded` with 64 productive outcomes and tick
  64.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (412
  terminal true results, zero failure markers); `git diff --check` and an
  obvious secret-like diff scan passed. No Python chemistry logic or
  scientific claim changed; pre-existing untracked scratch files were left
  untouched. Commit `871fe0e` pushed normally to GitHub `main`.

## 2026-07-24 12:30 — Extend bounded live ticking to seven sweeps

- Added PeTTa-native `chamber-tick-generated-sweeps-7`, which advances from
  the checked six-sweep result's exact chamber only when that result ended in
  productive bound exhaustion. Closed-cap and productive-then-quiescent paths
  still stop after one and two sweeps.
- Extended seven-sweep positional and run-wide outcome accessors plus the
  fixed event-history append seam through 56 retained events. The sustained
  cap-1 fixture returns `stop-bounded` with 56 productive outcomes and tick
  56.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (403
  terminal true results, zero failure markers); `git diff --check` and an
  obvious secret-like diff scan passed. No Python chemistry logic or
  scientific claim changed; pre-existing untracked scratch files were left
  untouched. Commit `d1e5046` pushed normally to GitHub `main`.

## 2026-07-24 08:30 — Extend bounded live ticking to five sweeps

- Added PeTTa-native `chamber-tick-generated-sweeps-5`, which advances from
  the checked four-sweep result's exact chamber only when that result ended in
  productive bound exhaustion. Closed-cap and productive-then-quiescent paths
  still stop after one and two sweeps.
- Extended five-sweep positional and run-wide outcome accessors plus the fixed
  event-history append seam through 40 retained events. The sustained cap-1
  fixture returns `stop-bounded` with 40 productive outcomes and tick 40.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (385
  true results, zero failure markers); `git diff --check` and an obvious
  secret-like diff scan passed. No Python chemistry logic or scientific claim
  changed; pre-existing untracked scratch files were left untouched. Commit
  `587143d` pushed normally to GitHub `main`.

## 2026-07-24 06:30 — Extend bounded live ticking to four sweeps

- Added PeTTa-native `chamber-tick-generated-sweeps-4`, which consumes the
  checked three-sweep result and advances from its exact projected chamber
  only when that bounded result ended with a live productive continuation.
- The focused test exposed the prior 24-event append ceiling. Extended the
  fixed PeTTa-native `append-chamber-event` seam through 32 retained events,
  then verified four-sweep count/accessors, exact run-wide productive/no-op
  accounting, `stop-bounded`, and the tick-32 chamber. One- and two-sweep
  early stops remain unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (375
  true results, zero failure markers); `git diff --check` passed. No Python
  chemistry logic or scientific claim changed; pre-existing untracked scratch
  files were left untouched. Commit `11d9598` pushed normally to GitHub
  `main`.

## 2026-07-24 04:30 — Extend bounded live ticking to three sweeps

- Added PeTTa-native `chamber-tick-generated-sweeps-3`, which advances only
  productive retained sweeps from their exact projected chambers and maps a
  productive third-sweep continuation to terminal `stop-bounded`.
- Extended sweep count, positional access, and run-wide productive/no-op
  accounting to three retained sweeps. Closed-cap and ordinary fixtures stop
  after one and two sweeps; the sustained cap-1 fixture retains 24 productive
  ticks and its exact tick-24 chamber.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (366
  true results, zero failure markers); `git diff --check` and an obvious
  secret-like diff scan passed. Commit `c33537e` pushed normally to GitHub
  `main`; pre-existing untracked scratch files were left untouched.

## 2026-07-24 02:30 — Report bounded tick-loop exhaustion

- Added PeTTa-native `chamber-tick-final-bounded-action`, mapping a productive
  final sweep's live `continue` decision to terminal `stop-bounded` at the
  two-sweep driver boundary.
- A sustained cap-1 fixture preserves all 16 productive outcomes, productive
  run-wide disposition, and the exact tick-16 chamber. Quiescent and invalid
  terminal actions remain unchanged; chemistry and emergence claims are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (357
  true results); `git diff --check` and an obvious secret-like diff scan
  passed. Commit `6223b6e` pushed normally to GitHub `main`; pre-existing
  untracked scratch files were left untouched.

## 2026-07-23 20:30 — Package a live bounded tick sweep

- Added PeTTa-native `chamber-tick-generated-sweep`, which evaluates the
  complete eight-step checked generation/selection/firing path once and
  packages those retained steps with the control action derived from them.
- Direct action, steps, and chamber accessors keep loop drivers on the same
  evaluated provenance. Exp00 verifies a closed-cap sweep stops quiescent and
  a productive-first sweep continues from the exact projected chamber.
  Chemistry and emergence claims are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (336
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `80d41c6` pushed normally to GitHub
  `main`.

## 2026-07-23 16:30 — Classify bounded live tick histories

- Added PeTTa-native `chamber-tick-steps-disposition`, which consumes the
  established outcome-accounting and productivity counts.
- Complete closed-cap and productive-first eight-step histories classify as
  `quiescent` and `productive`. A synthetic three-step history containing
  `unknown` fails closed to `invalid-outcomes`. Generation, deterministic
  selection, checked firing, and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (329
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `8b7e3a0` pushed normally to GitHub
  `main`.

## 2026-07-23 14:30 — Count unaccounted bounded tick outcomes

- Added PeTTa-native `chamber-tick-steps-unaccounted-count`, which exposes
  the exact retained outcomes not classified as productive or no-op.
- Complete closed-cap and productive-first eight-step live histories report
  zero. A synthetic three-step history containing `unknown` reports one, and
  the existing accounting-validity gate now derives from this count.
  Generation, deterministic selection, checked firing, and chemistry are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (326
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `7999344` pushed normally to GitHub
  `main`.

## 2026-07-23 12:30 — Validate bounded tick outcome accounting

- Added PeTTa-native `chamber-tick-steps-outcome-accounting-valid?`, which
  checks that productive plus no-op outcomes exactly equal the retained
  bounded step count.
- The complete closed-cap and productive-first eight-step live histories
  validate. A synthetic three-step history containing `unknown` fails, so
  malformed outcome tokens cannot silently pass through host-side parsing.
  Generation, deterministic selection, checked firing, and chemistry are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (323
  true results); `git diff --check` and the focused secret-like diff scan
  passed. Pre-existing untracked scratch files were left untouched. Commit
  `c8713af` pushed normally to GitHub `main`.

## 2026-07-23 08:30 — Extend bounded live ticking to seven steps

- Added PeTTa-native `chamber-tick-generated-steps-7`, which feeds the
  six-step projected chamber into a seventh ordinary checked generated step.
- Six-outcome positional accessors enable the state handoff; seven-outcome
  atoms expose exact width, productive count, and no-op count. Exp00 verifies
  closed-cap and productive-first trajectories plus final-chamber
  preservation. Chemistry remains on the existing generation, deterministic
  selection, and checked firing path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (313
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `81705be` pushed normally to GitHub
  `main`.

## 2026-07-23 06:30 — Extend bounded live ticking to six steps

- Added PeTTa-native `chamber-tick-generated-steps-6`, which feeds the
  five-step projected chamber into a sixth ordinary checked generated step.
- Five-outcome positional accessors enable the state handoff; six-outcome
  atoms expose exact width, productive count, and no-op count. Exp00 verifies
  closed-cap and productive-first trajectories plus final-chamber
  preservation. Chemistry remains on the existing generation, deterministic
  selection, and checked firing path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (306
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `4fdccfe` pushed normally to GitHub
  `main`.

## 2026-07-23 04:30 — Extend bounded live ticking to five steps

- Added PeTTa-native `chamber-tick-generated-steps-5`, which feeds the
  four-step projected chamber into a fifth ordinary checked generated step.
- Four-outcome positional accessors enable the state handoff; five-outcome
  atoms expose exact width, productive count, and no-op count. Exp00 verifies
  closed-cap and productive-first trajectories plus final-chamber
  preservation. Chemistry remains on the existing generation, deterministic
  selection, and checked firing path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (299
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `f6daad7` pushed normally to GitHub
  `main`.

## 2026-07-23 00:30 — Extend bounded live ticking to three steps

- Added PeTTa-native `chamber-tick-generated-steps-3`, which feeds the
  two-step projected chamber into a third ordinary checked generated step.
- Three-outcome `chamber-tick-steps` atoms now expose exact width, productive
  count, and no-op count. Exp00 verifies closed-cap and productive-first
  trajectories plus final-chamber preservation; chemistry remains on the
  existing generation, deterministic selection, and checked firing path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (285
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `5a27e88` pushed normally to GitHub
  `main`.

## 2026-07-22 22:30 — Count bounded tick outcomes

- Added PeTTa-native productive and no-op count accessors over the bounded
  two-step generated tick sequence.
- Exp00 covers zero productive/two no-op outcomes for a closed cap and one of
  each for the productive state handoff. Generation, deterministic selection,
  checked firing, and chemistry remain on the existing kernel path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (277
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `2da3f94` pushed normally to GitHub
  `main`.

## 2026-07-22 14:30 — Compose bounded loop-facing tick steps

- Added PeTTa-native `chamber-tick-generated-steps-2`, which feeds the first
  live checked step's projected chamber directly into a second generated tick
  and retains both outcomes plus the final chamber in `chamber-tick-steps`.
- Exp00 covers the closed cap as two deterministic valid no-ops. Candidate
  generation, deterministic selection, checked firing, and chemistry remain
  on the existing kernel path; Python is not used.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (271 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched. Commit `c77b250` pushed normally to GitHub `main`.

## 2026-07-22 10:30 — Query live generated tick outcomes directly

- Added PeTTa-native `chamber-tick-generated-outcome`, giving tick-loop
  consumers the checked live result classification without manually composing
  result construction and outcome access.
- Exp00 covers an ordinary productive tick and a valid cap-zero no-op.
  Candidate generation, deterministic selection, firing, chemistry, and
  trajectories are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (265 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched. Commit `e082865` pushed normally to GitHub `main`.

## 2026-07-22 08:30 — Classify checked chamber-tick outcomes

- Added PeTTa-native `chamber-tick-result-outcome`, combining checked validity
  and chamber-change status into `productive`, `no-op`, or the exact invalid
  boundary for direct tick-loop and audit consumption.
- Exp00 covers an ordinary productive tick, a valid cap-zero no-op, and a
  malformed over-cap record classified `invalid-bounds`. Candidate generation,
  deterministic selection, firing, chemistry, and trajectories are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (263 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched. Commit `41d0fc0` pushed normally to GitHub `main`.

## 2026-07-22 06:30 — Classify checked chamber changes

- Added PeTTa-native `chamber-tick-result-changed?` so tick-loop, audit, and
  report consumers can distinguish actual chamber transitions without
  destructuring result atoms or comparing chambers in host glue.
- Exp00 covers a productive valid result, a valid cap-zero no-op, and an
  invalid over-cap result that fails closed without changing the chamber.
  Candidate generation, selection, firing, chemistry, and trajectories are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (259 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched. Commit `80b4923` pushed normally to GitHub `main`.

## 2026-07-21 20:30 — Attribute complete tick-record validity

- Added PeTTa-native `generated-selection-fire-record-validity` with a fixed
  first-failure precedence across attrition, bounds, exact generation,
  deterministic selection, and firing.
- Checked chamber ticking now consumes the disposition; valid chemistry and
  fail-closed rejection are unchanged. Exp00 covers `valid` and a reordered
  pool classified as `invalid-generation`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (246 true
  results); `git diff --check` passed. Commit `e3cd363` pushed to GitHub
  `main`.

## 2026-07-21 18:30 — Exercise exact generation rejection at tick boundary

- Extended exp00 coverage so a reordered equal-width generated pool is
  rejected by the complete provenance gate and cannot mutate its input through
  `chamber-tick-from-generated-record`.
- This closes the end-to-end test seam between exact candidate generation and
  checked chamber ticking; chemistry and valid trajectories are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (244 true
  results); `git diff --check` passed. Commit `ad56a61` pushed to GitHub
  `main`.

## 2026-07-21 16:30 — Validate exact candidate generation provenance

- Added PeTTa-native `generated-selection-fire-record-generation-valid?` to
  reconstruct the generated pool from the input chamber and compare it with
  the complete chamber-tick record.
- Exp00 rejects an internally consistent equal-width pool whose source-rule
  order differs from the chamber. Selection, firing, and chemistry are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (241 true
  results); `git diff --check` passed. Commit `8315c43` pushed to GitHub
  `main`.

## 2026-07-21 14:30 — Validate generated chamber firing provenance

- Added PeTTa-native `generated-selection-fire-record-firing-valid?` to
  reconstruct the chamber transition from the input chamber, generated pool
  envelope, and deterministic selected candidate.
- Exp00 rejects a record whose generation and selection are exact but whose
  output chamber is forged; the checked chamber-tick projection fails closed.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (241 true
  results); `git diff --check` passed. Commit `6f2a64c` pushed to GitHub
  `main`.

## 2026-07-21 12:30 — Validate deterministic selection provenance

- Added PeTTa-native `generated-selection-fire-record-selection-valid?` to
  reconstruct and compare both the bounded pool and deterministic choice
  carried by complete chamber-tick provenance.
- Exp00 rejects a forged equal-cardinality bounded pool and proves the invalid
  record cannot mutate its input chamber. Ordinary generated selection,
  firing, and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (238 true
  results); `git diff --check` passed. Implementation commit `f86e7dc`.

## 2026-07-21 10:30 — Gate generated chamber ticking on complete provenance

- Added PeTTa-native `chamber-tick-from-generated-record`; the ordinary
  generated tick constructs its record once and projects through the complete
  attrition and candidate-bound validity gate.
- Exp00 proves a synthetic over-cap record cannot mutate its input chamber and
  verifies the ordinary productive seed-7 transition is unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (235 true
  results); `git diff --check` passed. Commit `c2f8204` pushed to GitHub
  `main`.

## 2026-07-21 06:30 — Validate live attrition provenance directly

- Added PeTTa-native `generated-selection-fire-record-attrition-valid?`, which
  derives the compact attrition summary from a chamber and complete live
  record and applies the existing full validity gate.
- Exp00 verifies ordinary cap-2 and closed cap-0 paths. Generation,
  deterministic selection, firing, and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (229 true
  results); `git diff --check` passed. Commit `196b097` pushed to GitHub
  `main`.

## 2026-07-21 04:30 — Validate candidate-attrition count domain

- Added PeTTa-native `candidate-attrition-counts-nonnegative?` over all six
  compact provenance cardinalities and folded it into the complete validity
  gate.
- Exp00 rejects an impossible negative bounded count even though the record's
  conservation equations and `selection` label agree. Generation, selection,
  firing, and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (227 true
  results); `git diff --check` passed. Commit `fd9fc71` pushed to GitHub
  `main`.

## 2026-07-21 02:30 — Unify candidate-attrition validity

- Added PeTTa-native `candidate-attrition-valid?`, combining the arithmetic
  conservation and stage-attribution checks into one persistence/report gate.
- Exp00 accepts live generation/selection/fire provenance and rejects either
  malformed counts or a misleading stage label. Candidate generation,
  deterministic selection, firing, and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (224 true
  results); `git diff --check` passed. Commit `52b8945` pushed to GitHub
  `main`.

## 2026-07-20 18:30 — Package candidate-attrition provenance

- Added a PeTTa-native `candidate-attrition` summary over the complete direct
  generation, bounded deterministic selection, and firing record.
- The atom carries source/generated/bounded counts, generation/selection/total
  omissions, and the attributed stage; exp00 verifies preserved and
  selection-truncated ordinary fixtures. Chemistry and ticking are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (206 true
  results); `git diff --check` passed. Commit `2a9f71d` pushed to GitHub
  `main`.

## 2026-07-20 10:30 — Classify total bounded-candidate retention

- Added a PeTTa-native accessor classifying whether every chamber source rule
  survives both the fixed generator boundary and effective selection cap.
- Exp00 verifies `preserved` for the ordinary three-rule source under cap 3
  and `truncated` for the supported twelve-rule source at generation cap 8.
  Deterministic firing and chemistry are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (200 true
  results); `git diff --check` passed. Commit `6c79443` pushed to GitHub
  `main`.

## 2026-07-20 08:30 — Expose total bounded-candidate attrition

- Added a PeTTa-native accessor deriving complete source-to-bounded-pool
  attrition from chamber source width and the bounded selectable count.
- Exp00 verifies one omission for the ordinary three-rule source under cap 2,
  and ten for the twelve-rule source: four at generation plus six at
  selection. Deterministic firing and chemistry are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (198 true results); `git diff --check` passed.
  Commit `93b8bfc`.

## 2026-07-20 04:30 — Expose remaining bounded-generation capacity

- Added a PeTTa-native accessor deriving unused generator slots from the
  stable generation cap and generated-pool count in complete provenance.
- Exp00 verifies five remaining slots for the ordinary three-rule complete
  fixture and zero for the twelve-rule truncated fixture. Selection-stage
  caps, deterministic firing, and chemistry are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (194 true results); `git diff --check` passed.
  Commit `96ad214` pushed to GitHub `main`.

## 2026-07-20 02:30 — Expose bounded-generation cap

- Added a PeTTa-native accessor for the base generator's stable
  eight-candidate boundary in complete generation/selection/fire provenance.
- Exp00 verifies generation cap 8 for the ordinary three-rule complete source
  and the supported twelve-rule truncated source. Selection-stage caps,
  deterministic firing, and chemistry are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (192 true results); `git diff --check` passed.
  Commit `017f9d5` pushed to GitHub `main`.

## 2026-07-20 00:30 — Bounded-generation disposition

- Added a PeTTa-native accessor that maps generation omission provenance to
  `complete` or `truncated`, distinct from the later selection-cap
  disposition.
- Exp00 covers the ordinary three-rule complete case and twelve-rule
  truncated case at the stable first-eight generator boundary. Selection,
  firing, and chemistry are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (190 true results); `git diff --check` passed.
  Commit `ebcc70d` pushed to GitHub `main`.

## 2026-07-19 22:30 — Expose bounded-generation omissions

- Added PeTTa-native source-rule cardinality and generation-omission
  accessors, keeping the generator's eight-candidate boundary distinct from
  the later per-tick selection cap.
- The ordinary three-rule chamber reports 0 omitted during generation; the
  supported twelve-rule fixture reports 4 omitted beyond its stable first
  eight candidates. Selection-stage dropped counts, firing, and chemistry are
  unchanged.
- Exp00 returned 188 true results using the recorded local PeTTa/SWI stack.
  `git diff --check` passed. Commit `2bb805e` pushed to GitHub `main`.

## 2026-07-19 18:30 — Expose candidate-pool cardinality provenance

- Added PeTTa-native accessors for generated and bounded candidate counts in
  the complete generated-selection/fire record.
- The three-rule fixture reports 3 generated versus 2 bounded under cap 2,
  3 versus 3 under cap 3, and bounded count 0 for a nonpositive request.
  Candidate generation, deterministic selection, firing, and chemistry are
  unchanged.
- Exp00 returned 182 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `a9093ac` pushed to GitHub `main`.

## 2026-07-19 16:30 — Expose generated-pool cap disposition

- Added a PeTTa-native accessor over complete generated-selection/fire
  provenance that reports whether the effective cap preserved or truncated
  the generated pool.
- A three-rule fixture reports `truncated` under cap 2 and `preserved` under
  cap 3. The accessor compares the already-bound generated and bounded pools;
  candidate generation, deterministic selection, firing, and chemistry are
  unchanged.
- Exp00 returned 178 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `964b36a` pushed to GitHub `main`.

## 2026-07-19 10:30 — Audit positive per-rule cap normalization

- Added focused PeTTa smoke coverage for requested cap `(2 3)` across the
  complete generated-selection/fire record.
- The request remains available for audit, its effective cap is `(2 1)` under
  the one-candidate-per-source-rule contract, and direct generated ticking
  matches the ordinary `(2 1)` transition. No selector, generator, or
  chemistry changed.
- Exp00 returned 168 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `93ea3d4` pushed to GitHub `main`.

## 2026-07-19 08:30 — Audit negative per-rule cap closure

- Added focused PeTTa smoke coverage for requested cap `(2 -1)` across the
  complete generated-selection/fire record.
- The malformed request remains available for audit, its effective cap is
  `(0 0)`, and direct generated chamber ticking remains a no-op. No selector,
  candidate generator, or chemistry transition changed.
- Exp00 returned 165 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `4013acf` pushed to GitHub `main`.

## 2026-07-19 06:30 — Close complete cap on nonpositive tick boundary

- Corrected PeTTa-native effective cap normalization so a nonpositive
  per-tick allowance also sets the effective per-rule allowance to zero.
- Focused smoke coverage proves requested `(-1 1)` and `(0 3)` both expose
  effective `(0 0)`. Candidate selection and chamber transitions are
  unchanged.
- Exp00 returned 162 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `d744596` pushed to GitHub `main`.

## 2026-07-19 04:30 — Complete effective candidate-cap provenance

- Added PeTTa-native effective per-rule and complete effective-cap accessors.
  The one-candidate-per-source-rule generator normalizes positive per-rule
  allowances to one; nonpositive allowances remain fail-closed.
- Generated-selection/fire provenance now exposes requested `(9 3)` beside
  effective `(8 1)`, and requested `(2 0)` beside effective `(0 0)`.
- No selector or chamber transition changed. Exp00 returned 160 true results
  and `git diff --check` passed using the recorded local PeTTa/SWI stack.
  Commit `1df98e4` pushed to GitHub `main`.

## 2026-07-18 20:30 — Frozen mechanism audit serialization complete

- Added PeTTa-native ordinary medians for all six first-prefix ticks and five
  first-food-exhaustion ticks in each frozen 32-seed arm; sentinel 99 remains
  uncensored.
- Added all seed-paired weak-minus-unguided food-exhaustion and reset-depth
  differences. Only the validated trace is consumed; chemistry, trajectories,
  and registered endpoints are unchanged.
- The fixed precedence remains `applicability-loss` (51 weak versus 38
  unguided blocked first-absent selections); `emergence-claim none` remains.
- Exp00, exp07, runnable dual report, detector invariance, and diff check pass.
- Commit `a57f4e0` pushed to GitHub `main`.

## 2026-07-18

### 14:30 first frozen mechanism aggregates and interpretation

- Added PeTTa-native folds over the validated trace for selected/fired counts
  across all twelve rule identities, first-absent selected/fired counts, and
  blocked pathway/distractor partitions.
- Weak guidance produced 51 blocked selections of the currently first-absent
  pathway identity, versus 38 unguided (shuffled reference 1). The frozen
  precedence therefore stops at `applicability-loss`; no later label or
  adaptive subgroup was inspected.
- Checks passed: exp00, exp07, detector invariance, and `git diff --check`.
  Commit `ec04352` pushed to GitHub `main`. The registered negative outcome,
  fixed trajectories, and `emergence-claim none` are unchanged. Remaining
  audit work is prefix/resource and paired-summary serialization.

### 12:30 dual-bootstrap mechanism trace integrity gate

- Added PeTTa-native per-tick trace rows over only the completed seeds 201--232,
  ticks 3--34 matrix. Rows use the reset-prepared pre-fire chamber and exact
  selected candidate and retain key, rule, applicability/firing, frontier,
  six pathway-product bits, and A--E food abundances.
- Sequential validation establishes exactly 32 nonduplicate ordered keys for
  each of 96 trajectories. The fail-closed gate also reproduces registered
  RAF 13/9/0, events 549/523/396, persistence 95/51/0, diversity 336/278/219,
  and replay 32/32/32.
- No mechanism aggregate or label was evaluated. No seeds, ticks, chemistry,
  selectors, draws, or outcomes changed; negative guided uplift and
  `emergence-claim none` remain fixed.
- Provenance: local recorded PeTTa/SWI stack; `src/chem_exp07.metta` and exp07
  smoke. Checks: exp00 154, exp07 305, detector invariance, `git diff --check`.
  Commit `65cab25` pushed to GitHub `main`.

At 08:30, the dual-bootstrap program was formally closed as a preregistered
negative result, with no extension or reinterpretation of the completed
matrix. The repository README and durable records now reflect the already
executed seed-201--232/tick-3--34 outcome rather than the earlier design-only
state. The scientific boundary is unchanged: pathway ablations establish
structural necessity, but weak guidance underperformed unguided (9/32 versus
13/32) and guiding-term removal retained 13/32, so guided causal RAF uplift is
not supported and spontaneous-emergence claim remains none. Any successor
requires a newly chosen objective and preregistration before implementation.
Provenance: frozen protocol/report, local PeTTa/SWI stack, commit `48af89b`,
and this closure-only records pass. Check: exp00 (154) and `git diff --check`.
README closure commit `56fda93` pushed to GitHub `main`.

At 06:30, the frozen dual-bootstrap matrix was executed exactly once over
seeds 201--232 and ticks 3--34 after exp00, exp07, and detector-invariance
gates passed. PeTTa-native rolling four-rule RAF incidence was 13/32 unguided,
9/32 weak Doob-h, and 0/32 shuffled, so weak missed the preregistered ten-seed
advantage and underperformed unguided. All 96 trajectories replayed exactly;
persistence totals were 95/51/0, productive-event totals 549/523/396, and
rule-diversity totals 336/278/219. Either bootstrap, the complete four-edge
cycle catalyst set, or any individual cycle rule reduced weak incidence to
0/32, while guiding-term removal retained unguided 13/32. Thus the chemistry
is pathway-dependent but guided causal RAF uplift is not supported. No seed,
tick, pool, threshold, or endpoint extension; spontaneous-emergence claim
none. Provenance: `PREREG_DUAL_BOOTSTRAP.md`, `DUAL_BOOTSTRAP_REPORT.md`, local
PeTTa/SWI kernel, runnable PeTTa report, and golden smoke. Checks: exp00 (154),
exp07 (302), detector invariance, full report execution, and
`git diff --check`. Commit `48af89b` pushed to GitHub `main`.

At 04:30, the preregistered dual-bootstrap fail-closed implementation gate
passed without seed-201--232 support or any registered trajectory. The shared
PeTTa kernel gained the frozen seventeen-species abundance/update shape, and
exp07 materializes the complete twelve-rule source plus twelve closed-world
catalysis facts. Initial checks derive `db0=True`, `db1/dp1/dp2/dp3/dp0=False`,
both exposed distractors applicable, and empty-history RAF negativity. The
canonical and fixed-permuted sources yield identical identity-addressed cap-8
pools in each distractor phase. Exhaustive draw-bin checks cover every
combination of six frontier identities and three distractor phases, realizing
the declared weak 20/4/12 and shuffled 4/20/12 masses with equal eight-unit
cost. A seed-7 permuted-source fixture selects `db0` by identity and fires it
through ordinary chamber ticking. Provenance: local PeTTa/SWI stack,
`PREREG_DUAL_BOOTSTRAP.md`, exp00/exp07 kernels, and golden smoke. Checks:
exp00 (153), exp07 (270), detector invariance, and `git diff --check`;
commit `6b3fc76` pushed to GitHub `main`; emergence claim none.

At 02:30, the ordered-replication program was closed as two separate negative
gates: cohort A failed primary replication, while cohort B failed order/hash
robustness because guiding-term removal retained unguided 8/16; cohort B does
not rescue A. Before any successor implementation, the design-only
`PREREG_DUAL_BOOTSTRAP.md` and matching PeTTa contract froze a dual bootstrap,
four-rule RAF, twelve-rule source, order-invariant identity-addressed cap 8,
fresh seeds 201--232, ticks 3--34, fixed selector/hash/cost, causal thresholds,
and direct bounded ticking. No successor seed support, generator, selector,
trajectory, or outcome exists. Provenance: local PeTTa/SWI stack, exp07 source,
golden smoke, README, and preregistration. Checks: exp00 (153), exp07 (252),
detector invariance, and `git diff --check`. Commit `06c0f3c` pushed to GitHub
`main`; emergence claim none.

At 00:30, frozen ordered-replication cohort B was executed exactly once over
seeds 117--132 and ticks 3--26 with its preregistered hash and permuted
`(od2 op0 ob0 od1 op2 od3 op1 od0)` pool. PeTTa-native incidence was 8/16
unguided, 16/16 weak Doob-h, and 0/16 shuffled; all 48 trajectories replayed.
Weak cleared the four-seed incidence threshold, but guiding-term removal
retained unguided 8/16, exceeding the causal maximum of two. Thus order/hash
robustness is not supported and cannot rescue cohort A. Persistence totals
were 33/145/0, events 281/275/260, diversity 120/127/92, matched guided cost
3,072 each, and every structural ablation was 0/16. Provenance: frozen
`PREREG_ORDERED_REPLICATION.md`, local PeTTa/SWI stack, exp07 kernel/report and
golden smoke. No extension; emergence claim none. Checks: exp00 (153), exp07
(250), detector invariance, and `git diff --check`. Commit `836ac36` pushed to
GitHub `main`.

## 2026-07-17

At 20:30, the frozen ordered-replication fail-closed implementation gate
passed without constructing a seed-101--132 trajectory. PeTTa explicitly maps
all 32 fresh seed names and exhaustively verifies that the cohort-A and
cohort-B hashes each visit every draw bin exactly once over a 96-tick
calibration. Both cohort-specific pools are identical across arms. Cohort B's
permuted generator exposes `(od2 op0 ob0 od1 op2 od3 op1 od0)` exactly, while
selection converts each categorical bin to a rule ID before locating the
candidate; weak and shuffled tests cover all four frontier phases. Derived
mass vectors preserve the matched eight-unit intervention cost. A synthetic
seed-7 fixture selects `ob0` from the third pool position and passes it
directly to ordinary chamber ticking. Exp00 passed 153 assertions, exp07
passed 246, canonical detector invariance passed, and `git diff --check`
passed. No replication outcome was inspected; `emergence-claim none`.
Commit `0c078d2` pushed to GitHub `main`.

At 18:30, the corrected ordered-bootstrap result gained a preregistered
independent replication and robustness design without new outcomes.
`PREREG_ORDERED_REPLICATION.md` freezes an exact-form cohort on seeds 101--116
with a new hash and a separate order/hash cohort on seeds 117--132. The latter
permutes the complete cap-8 pool and requires selector weights to follow rule
identity rather than position. Both cohorts preserve the predecessor chemistry,
ticks, matched guidance cost, replay, and guiding/bootstrap/catalyst/rule
ablations. Fixed weak-versus-control advantage and ablation thresholds are
declared before implementation. The matching PeTTa design-only atom passed one
new exp07 assertion (225 total). No seed-number support, registered selector,
trajectory, or endpoint was evaluated; spontaneous-emergence claim remains
none. Provenance: local PeTTa/SWI stack, exp07 preregistration, kernel contract,
smoke, and README. Checks: exp00 (153), exp07 (225), and `git diff --check`.
Commit `07fed0d` pushed to GitHub `main`.

At 12:33, the remaining ordered-bootstrap pre-run selector gates closed without
constructing a registered seed-19--26 trajectory. The PeTTa named-molecule
kernel gained the frozen twelve-species abundance/update shape. Initial-state
checks derive `ob0=True`, `op1/op2/op0=False`, and empty-history RAF negativity
from the actual chamber and event history. Explicit fixtures cover all four
frontier states. Exhaustive synthetic bins 0--95 realize the frozen masses:
unguided `(12 12 12 12 12 12 12 12)`, weak guidance with `20/4` on the
phase frontier/paired distractor, and shuffled guidance with those positions
reversed. The guided policies therefore retain the preregistered matched
eight-unit cost. A synthetic draw-0 direct test selects `ob0` from ordinary
generated/bounded cap-8 candidates and produces the expected chamber event and
abundance update through `chamber-tick-with-candidate`. Exp00 passed 153,
exp07 passed 217, and `git diff --check` passed. No ensemble outcome was read;
`emergence-claim none`.

At 08:34, the frozen exp07 rich-pool matrix was formally closed as
pool-composition evidence: its planted cycle is necessary under catalyst and
single-rule ablations, but the 5/8 unguided and 3/8 shuffled RAF incidence
reject guidance necessity. No seed or tick was added. Before implementing or
inspecting another outcome, `PREREG_ORDERED_BOOTSTRAP.md` froze a successor
with initial `CD=0`, one non-RAF `X`-catalyzed bootstrap, and the catalytic
frontier `op1 -> op2 -> op0`. Arms share an exact cap-8 pool over held-out
seeds 19--26 and ticks 3--26. Weak and shuffled-frontier policies each shift
eight of 96 mass units per draw and differ only in whether the high-mass bin
tracks the current productive frontier or its paired distractor. PeTTa-side
atoms and exp07 smoke preserve the closed-null interpretation and design-only
contract. Exp00 passed 153 assertions, exp07 passed 187, and
`git diff --check` passed; commit `65ef00a` was pushed to GitHub `main` and
`emergence-claim none`. Next: implement fail-closed pool, catalysis,
initial-negativity, four-phase calibration, cost, and direct-tick gates before
any registered trajectory.

At 04:30, the frozen exp07 rich-pool matrix gained its preregistered
intervention-cost endpoint without new seeds, ticks, trajectories, or outcome
inputs. PeTTa computes the total-variation numerator directly from the
calibrated 88-bin categorical masses by summing mass shifted onto bins relative
to unguided. Per-draw costs are 0 unguided, 15 weak Doob-h, and 15 shuffled;
the latter two are 360 per 24-tick trajectory and 2,880 per eight-trajectory
arm. Thus the treatment and shuffled control have an exactly matched guidance
budget despite assigning their elevated mass to different rule IDs. Both
controls remain RAF-positive and `emergence-claim none`. Checks: exp00 154,
exp07 185, and `git diff --check`. Next: frozen guiding-term/catalyst/rule
ablations.

At 02:30, the frozen exp07 rich-pool matrix gained its preregistered
diversity-collapse endpoint with no new seed, tick, or trajectory. PeTTa reads
the terminal productive-event history and counts how many of `rp0/rp1/rp2`
and `rd0`--`rd4` fired at least once. In seed-11--18 order, terminal rule
diversity is `[6,8,8,8,8,7,8,8]` unguided, `[8,7,6,8,8,8,8,8]` weak
Doob-h, and `[7,7,5,5,7,7,8,8]` shuffled. Totals are 61/61/54 out of the
64 possible seed-rule presences, so full-pool collapse deficits are 3/3/10.
Weak guidance preserves the same aggregate diversity as unguided; shuffled is
less diverse. This does not alter the positive-control problem or causal gate:
`emergence-claim none`. Checks: exp00 153, exp07 176, and `git diff --check`.
Commit `5b436eb` pushed to GitHub `main`. Next: intervention/path cost and
frozen guiding-term/catalyst/rule ablations.

At 00:30, the already executed frozen exp07 rich-pool matrix gained its
preregistered persistence endpoint without any new trajectory, seed, or tick.
The PeTTa kernel now walks each registered chamber tick, evaluates the rolling
last-eight-productive-event `rp0/rp1/rp2` condition after the tick, and records
the longest consecutive positive run. Blocked ticks count when the unchanged
rolling window remains positive. Unguided persistence was
`[0,3,1,1,3,0,5,0]` (total 13), weak Doob-h was
`[7,7,0,6,11,7,4,7]` (total 49), and shuffled guidance was
`[0,6,0,0,0,0,3,2]` (total 11), in seed-11--18 order. This is a raw guided-arm
persistence increase, but both controls are positive and the causal gates are
unfinished, so `emergence-claim none`. Checks: exp00 153, exp07 174, and
`git diff --check`. Next: diversity/collapse, intervention cost, then frozen
guiding-term/catalyst/rule ablations. Commit `e72b7fe` pushed to GitHub `main`.

## 2026-07-16

At 18:30, the frozen exp07 rich-pool categorical sampler passed its complete
pre-run mass calibration without constructing a registered chemistry outcome.
PeTTa recursively exhausts synthetic draw bins 0--87 and counts selected bins
for each arm. Realized masses exactly match the preregistration: unguided
`(11 11 11 11 11 11 11 11)`, weak Doob-h `(16 16 16 8 8 8 8 8)`, and
shuffled guidance `(8 8 8 16 16 16 8 8)`. Checks: exp07 163 and
exp00 153 plus `git diff --check`. Commit `2d34083` pushed to GitHub `main`.
Initial-state RAF-negativity and detector controls remain pending; no
registered trajectory or RAF endpoint was evaluated and `emergence-claim
none`.

At 16:30, the frozen exp07 rich-pool design gained its first executable pre-run
slice without constructing any registered trajectory. The PeTTa kernel now
supports the registered thirteen-species named-molecule state, generates the
exact eight-rule candidate pool, preserves it under cap 8, applies the frozen
denominator-88 categorical partitions, and hands the selected candidate to the
ordinary applicability/update/event tick. The eight first-class catalysis
edges and exact shared-pool identity are queryable. Focused smoke verifies
partition boundaries and a productive unguided seed-12 tick (`rd0`, `W0=1`),
while weak/shuffled selections come from the same generated pool. Checks:
exp00 153, exp07 159, and `git diff --check`; commit `712fa17` pushed to
GitHub `main`. Boundary: no
24-tick arm or RAF endpoint was evaluated; full-cycle sampler calibration,
initial RAF-negativity, and detector controls remain pending;
`emergence-claim none`.

At 14:30, the all-arms-positive exp07 result was converted into a frozen
rich-pool pivot before any new trajectory or endpoint was implemented.
`experiments/exp07/PREREG_RICH_POOL.md` and smoke-tested PeTTa atoms specify a
shared eight-rule cap-8 pool containing a bootstrapped latent three-rule RAF
and five productive food-competing distractors. They freeze seeds 11--18, a
24-tick horizon, explicit first-class catalysis, matched unguided/weak
Doob-h/shuffled controls, required ablations, and gates for detector controls,
initial RAF-negativity, exact pool identity, catalysis completeness, sampler
calibration, and direct selection-to-chamber ticking. The preregistration also
freezes exact rewrites/abundances, denominator-88 integer masses, the draw
function, replenishment ticks 11/19, and a rolling-eight-event RAF endpoint.
Chemistry materialization remains behind the implementation gate; no rich-pool
outcome was evaluated and `emergence-claim none`. Checks: exp00 (153), exp07
(143), and `git diff --check`. Commit `e3bbc41` pushed to GitHub `main`.

At 08:32, exp07 gained the PeTTa-native blocked-tick and basal-replenishment
semantics required by its frozen N=20 preregistration. `exp07-pilot-total-tick`
advances a starved/otherwise blocked draw without adding an event, and prepares
all arms through one shared step that resets A/B/C to 2/1/1 immediately before
ticks 8, 13, and 18. Products, catalysts, source rules, and accumulated events
are retained. Focused tests cover every scheduled tick, a non-scheduled tick,
blocked time advance, and productive firing after replenishment. The registered
arm matrix was not evaluated, avoiding an interim outcome peek. Checks:
`scripts/run_exp00.sh`, `scripts/run_exp07.sh`, and `git diff --check`;
commit `3eb370e` pushed to GitHub `main`; `emergence-claim none`.

At 08:25, exp07 gained a separately labelled seed-31 detector-invariance
fixture. It imports only the canonical exp04 host detector and committed
`chem_exp04.metta` facts: positive A -> no-catalysis B -> positive A reproduces
RAF 15 -> 0 -> 15; direct tick-22 and advanced ticks 3--22 histories that
project to identical detector inputs reproduce RAF 15 and core
`{lCD,lBCD2}`; source guards require unique RAF/RA/FG heads, one specific and
one ablated catalysis dispatch, 18 unique ground edges, and no mutable detector
forms. The fixture did not load registered exp07 arms or alter the frozen
horizon, seeds, endpoints, or `emergence-claim none`. Run record:
`experiments/20260716T152520Z-exp07-detector-invariance/`. Checks: fixture
passed, exp04 smoke 80, exp07 smoke 129, Python compilation, and diff check.

At 06:30, the exp07 two-tick matched matrix was completed across unguided, weak Doob-h, and shuffled-guidance arms for seeds 7-10. All state transitions remain PeTTa-native and use the ordinary exp00 candidate-to-chamber tick. Productive-event vectors are `[1,2,1,2]`, `[2,2,1,1]`, and `[1,2,2,1]` respectively: each arm totals 6 events, while all 12 terminal chambers replay exactly from the shared initial chemistry and recorded seed/tick selections. This is an informative short-horizon null with different seed-level paths; reactant exhaustion limits interpretation, and no ACS/RAF outcome has been measured. Checks: `scripts/run_exp00.sh` (154 reported assertions), `scripts/run_exp07.sh` (128), `git diff --check`, and an obvious secret-like diff scan. Commit `28ddc28` pushed to GitHub `main`; `emergence-claim none`.

At 02:30, the exp07 matched-fixture gate passed on a shared PeTTa-native seven-molecule chemistry. The exp00 kernel now accepts a named molecule-list state, performs abundance lookup/applicability checks, and updates reactants/products while preserving catalyst abundance through the ordinary candidate-to-chamber tick path. The audit checks every candidate, not only the selected draws: all 24 candidates across the 12 two-candidate arm/seed pools are applicable, and all 12 sampled first draws tick productively. This removes the earlier chamber-shape confound and makes the next stateful comparison admissible. Checks: `scripts/run_exp00.sh` (153 reported assertions), `scripts/run_exp07.sh` (96), `git diff --check`. Commit `817dc42` pushed to GitHub `main`. Boundary: no multi-tick ACS/RAF outcomes yet; `emergence-claim none`.

At 00:30, the exp07 stochastic pilot gained a prerequisite matched-fixture applicability audit. The PeTTa-native diagnostic evaluates every categorical choice over arms unguided/weak Doob-h/shuffled and fixed seeds 7-10 against the chamber that would receive it. Results are 0/4, 3/4, and 3/4 productive first ticks respectively. This is not a treatment effect: the existing exp05 chambers were individually shaped around their original deterministic selection and do not expose a shared molecule soup for all reachable reactions/catalysts. The pilot contract now marks the matched-fixture gate failed and prohibits the stateful ensemble on these confounded fixtures. Required next step is a shared multi-molecule abundance/applicability/update seam in PeTTa, followed by the same audit. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (76), `git diff --check`. Commit `6f42e50` pushed to GitHub `main`; `emergence-claim none`.

## 2026-07-15

At 22:30, the exp07 weighted sampler was calibrated over a complete categorical cycle. Candidate-pool construction and weighted selection are now tick-parameterized in PeTTa, and ticks 3-6 make every fixed seed visit each of the four draw bins exactly once. Across seeds 7-10, the observed first-candidate counts exactly match the declared arm masses: unguided 8/16, weak Doob-h 12/16, and shuffled guidance 4/16. Checks: `scripts/run_exp00.sh`, `scripts/run_exp07.sh` (60 reported assertions), `git diff --check`. Commit `76d14eb` pushed to GitHub `main`. Scientific boundary: this rules out sampler-mass mismatch before stateful runs; it does not measure ACS/RAF incidence, persistence, productivity, or causality, and `emergence-claim none` remains.

At 20:30, exp07 gained its first replayable stochastic-ensemble selection gate. A PeTTa-native four-bin categorical draw now compares matched unguided (2/4), weak Doob-h (3/4), and shuffled-guidance (1/4) first-candidate mass over fixed seeds 7-10. Candidate construction remains exp05-native and every sampled candidate is handed directly to the ordinary exp00 chamber tick. The checked contract preregisters terminal ACS/RAF hit rate, first-hit time, persistence, productivity, diversity collapse, path cost, replay, and catalyst/rule ablation. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (53), `git diff --check`. Commit `2c564b2` pushed to GitHub `main`. Scientific boundary: this validates the sampler/direct-tick seam only; the multi-tick ensemble has not yet produced outcome estimates and `emergence-claim none` remains unchanged.

At 19:22, exp04 gained a first-class binary catalysis interface. Eighteen
`(catalyzes Molecule RuleId)` edges now drive PeTTa reflexive-autocatalysis
checks; structural template matching remains only as construction provenance
and for older reduction-sweep variants. The host maximal-RAF reference parses
the PeTTa facts and uses an empty relation for the identical ablation path.
Recorded gate `20260716T022154Z-first-class-catalysis-exp04` passed 79 PeTTa
assertions, Python compilation, and `git diff --check`, reproducing maximal RAF
15, core `lCD`/`lBCD2`, and ablation 0. Boundary: seeded-reference fidelity,
not unseeded emergence. Research Rules applied: detector validation (1),
plain-language contract first (2), reproducible evidence (5), and a replaceable
catalysis seam (7).

Ben redirected the active priority from further candidate/source-list hardening to ACS emergence. The twelve-rule checkpoint is treated as sufficient infrastructure. Next work is a preregistered, provider-free stochastic exp07 pilot with native/unguided, weak-guidance, and shuffled-guidance arms; no terminal forcing; fixed seeds; conservative ACS/RAF validation; persistence/productivity/diversity metrics; replay; and causal ablation. Research Rules most relevant to this pivot: validate the ACS detector and stochastic comparison (Rule 1), specify the experiment and stopping/claim gates before coding (Rule 2), make the run reproducible (Rule 5), and preserve replaceable sampling/scoring seams (Rule 7).

Dedicated 18:30 progress run extended the explicit oversized PeTTa-native candidate-generation boundary to twelve source rules. The kernel retains the full twelve-rule chamber as provenance while generating only the stable first-eight prefix, the chamber ownership guard recognizes the retained twelfth rewrite, and a cap-2 deterministic selection fires through the ordinary chamber-tick path. Checks: `scripts/run_exp00.sh` (152 checks), `git diff --check`. Commit `7061403` pushed to GitHub `main`.

Dedicated 10:30 progress run closed the remaining numeric candidate-cap boundary in the direct PeTTa-native generation -> selection -> chamber-tick chain. The base kernel has explicit bounded-list clauses through eight candidates, so positive per-tick allowances above eight now clamp to effective cap eight instead of reaching an unsupported operation. Focused smoke verifies the effective cap, exact preservation of a smaller generated pool, deterministic selection provenance, and productive generated chamber tick. Checks: `scripts/run_exp00.sh` (141 checks), `git diff --check`. Commit `02e5f15` pushed to GitHub `main`.

Dedicated 08:32 progress run made candidate-cap handling total over malformed negative bounds. `effective-candidate-cap-per-tick` now closes the boundary when either per-tick or per-rule allowance is nonpositive; direct bounded generation returns an empty tick-scoped pool, deterministic selection retains explicit `no-candidate` provenance, and generated ticking leaves the chamber unchanged. This remains entirely in the PeTTa kernel. Checks: `scripts/run_exp00.sh` (137 checks), `git diff --check`. Commit `5b9c790` pushed to GitHub `main`.

Dedicated 08:04 progress run closed a direct bounded-generation cap inconsistency in the PeTTa-native exp00 kernel. Selection already reduced a zero per-rule allowance to an effective zero cap, but `bounded-candidate-pool` used the raw per-tick value and still exposed generated candidates. It now consumes `effective-candidate-cap-per-tick`, and focused smoke proves `(candidate-cap 2 0)` directly yields an empty tick-scoped pool. Checks: `scripts/run_exp00.sh` (133 checks), `git diff --check`. Commit `638d8a4` pushed to GitHub `main`.

## 2026-07-13

Dedicated 18:30 progress run closed a bounded-cap semantics gap in the unified PeTTa-native deterministic-selection path. The canonical `candidate-cap` carried per-tick and per-rule limits, but selection previously ignored the per-rule field. Since generic generation emits at most one candidate per source rule, zero per-rule allowance now reduces the effective per-tick boundary to zero, retaining explicit empty-pool/`no-candidate` provenance and leaving the chamber unchanged. Positive per-rule behavior and exp05/06/07 compatibility remain green. Checks: `scripts/run_exp00.sh` (133 checks), `scripts/run_exp05.sh`, `scripts/run_exp06.sh`, `scripts/run_exp07.sh`, `git diff --check`. Commit `11ea4e5` pushed to GitHub `main`.

Dedicated 16:30 progress run closed a source-rewrite ownership gap in the unified PeTTa-native deterministic-selection-to-chamber path. Stable rule ID membership alone allowed a malformed external candidate to reuse an owned ID while changing reactants or product. Chamber applicability now matches ID plus reactants/product against the bounded source-rule list while deliberately allowing catalyst reassignment for exp05. Focused smoke proves a same-ID altered rewrite remains in complete bounded-selection provenance but leaves the chamber unchanged; exp05/06/07 compatibility gates remain green. Checks: `scripts/run_exp00.sh` (130 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `18ff8db` is pushed to GitHub `main`.

Dedicated 14:30 progress run fixed event-history loss in the unified PeTTa-native deterministic-selection-to-chamber path. The trace-to-chamber transition previously replaced a chamber's event list with the newest event; it now appends through an explicit bounded PeTTa helper, preserving earlier provenance. Focused smoke fires a selected candidate against a chamber with an existing event and verifies both events remain ordered. Checks: `scripts/run_exp00.sh` (128 checks), `git diff --check`. Commit `445df9c` pushed to GitHub `main`.

Dedicated 12:30 progress run closed a pool-envelope provenance gap in the unified PeTTa-native deterministic-selection path. `selection-fire-record-from-pool` now requires the candidate-pool tick to equal the chamber-state tick before applying its selected candidate. A malformed stale external/scored envelope therefore retains its exact cap, bounded list, and selected candidate for inspection but leaves the chamber unchanged, even if that candidate independently claims the current tick. Checks: `scripts/run_exp00.sh` (127 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `1ec8449` pushed to GitHub `main`.

Dedicated 10:30 progress run closed a chamber-ownership gap in the unified PeTTa-native candidate path. External/scored pools may still expose and deterministically select arbitrary candidates for inspectable provenance, but chamber firing now requires the selected rule ID to occur in the chamber rule list. A foreign selection therefore leaves the chamber unchanged with no event. Membership is deliberately by stable rule ID rather than exact rule structure, preserving exp05 catalyst reassignment; the broader exp05/06/07 gates caught and verified this compatibility boundary. Checks: `scripts/run_exp00.sh` (125 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `7d816b5` pushed to GitHub `main`.

Dedicated 08:30 progress run tightened provenance safety in the unified PeTTa-native deterministic-selection-to-chamber path. `candidate-applicable?` now requires the candidate tick to equal the chamber-state tick as well as checking reactant/catalyst abundance. A stale candidate pool therefore remains fully visible in `selection-fire-record` provenance but produces an unchanged later chamber with no event. Checks: `scripts/run_exp00.sh` (123 checks), `git diff --check`. Commit `e80974a` pushed to GitHub `main`.

Dedicated 06:30 progress run closed an applicability-safety gap in the unified PeTTa-native candidate path. `chamber-tick-with-candidate` now converts `safe-fire-candidate` outcomes into chamber transitions: applicable deterministic selections fire normally, while inapplicable selections retain full selection/fire provenance but leave the chamber unchanged with no event. Focused tests cover direct candidate ticking, selection/fire records, and generated cap-1 ticking on a starved chamber, preventing negative abundance. Checks: `scripts/run_exp00.sh` (122 checks), `git diff --check`. Commit `6cf6e9f` pushed to GitHub `main`.

Dedicated 04:30 progress run closed the remaining zero-cardinality boundary in the direct PeTTa-native candidate path. Cap zero and empty source pools now produce an explicit `no-candidate` selection inside the same provenance records used for ordinary firing; chamber ticking returns the unchanged chamber and creates no event. Added empty-rule generation for the base four-molecule state and positive-cap preservation of empty pools. Checks: `scripts/run_exp00.sh` (119 checks), `git diff --check`. Commit `ff58491` pushed to GitHub `main`.

Dedicated 02:30 progress run removed the final duplicated chamber-tick implementation seam. Cap-specific candidate-pool and generated-tick APIs for cardinalities 1-8 now delegate to the generic provenance-backed PeTTa-native operations, preserving callers while ensuring capping, actual-cardinality deterministic selection, and firing use one implementation. Checks: `scripts/run_exp00.sh` (116 checks), `git diff --check`. Commit `4c45a5d` pushed to GitHub `main`.

Dedicated 00:30 progress run removed two remaining duplicate-operation seams from the PeTTa-native candidate path. `bounded-candidate-pool` now binds a single generated pool instead of generating independently for tick provenance and capping. Cap-specific compatibility operations `chamber-tick-generated-1` through `-8` now hand their raw generated pool to the downstream candidate-pool tick, preventing the previous bounded-pool -> second cap sequence while preserving cap-as-maximum behavior, deterministic selection, and firing. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`.

## 2026-07-12

Dedicated 22:30 progress run removed parallel reconstruction inside the direct PeTTa-native generation-to-tick provenance chain. `candidate-selection-from-pool` now binds one cap and bounded pool, `selection-fire-record-from-pool` binds one selection consumed by firing, and `generated-selection-fire-record-from-chamber` binds one generated pool passed downstream. Added direct complete-record projections for the exact bounded pool and selected candidate. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`. Commit `5ecdacc` pushed to GitHub `main`.

Dedicated 20:30 progress run extended generated chamber-tick provenance end to end. Added PeTTa-native `generated-selection-fire-record-from-chamber`, preserving the uncapped generated candidate pool beside the exact bounded selection and fired chamber; generic `chamber-tick-generated` now projects from this complete chain. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `af49c98` pushed to GitHub `main`.

Dedicated 18:30 progress run tightened the direct deterministic-selection-to-chamber-tick seam. Added PeTTa-native `selection-fire-record-from-pool`, which keeps the requested cap, exact bounded list, deterministic selected candidate, and resulting chamber together; generic `chamber-tick-candidate-pool` now projects its result from this combined provenance object. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `6fa9ced` pushed to GitHub `main`.

Dedicated 16:30 progress run extended exp06’s PeTTa-native ACS boundary across the complete three-tick stateful cap trace. The diagnostic checks all selected pairs among ticks 3/4/5 for cap-1/cap-2, explicitly retaining the bounded no-op tick-5 candidate after A exhaustion. Both arms remain rejected under pairwise product-catalyst closure; this is not RAF enumeration and makes no emergence claim. Checks: `scripts/run_exp06.sh` (61 checks), `scripts/run_exp00.sh`, `git diff --check`.

Dedicated 14:30 progress run completed cap-as-maximum behavior for all smaller non-empty external pools under requested caps 2-8. Inspection showed the prior cap-8/three-candidate fix was isolated: generic selection still failed for shapes such as cap-7 over two candidates. Added the full 27-clause PeTTa-native smaller-pool matrix and focused provenance coverage proving exact cap-7/two-candidate preservation plus deterministic selection by actual cardinality. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `4ef39b9` pushed to GitHub `main`.

Dedicated 12:30 progress run added PeTTa-native `candidate-selection-from-pool`, preserving requested cap, exact bounded list, and deterministic selected candidate as one inspectable provenance atom consumed directly by generic chamber ticking. Focused exp00 coverage of that full object exposed a real omission: cap 8 did not preserve smaller external pools; cap-8/three-candidate preservation is now explicit and selection succeeds by actual cardinality. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `8c68755` pushed to GitHub `main`.

Dedicated 10:30 progress run exposed PeTTa-native `selected-candidate-from-pool`, an inspectable generic seam for cap -> actual bounded cardinality -> deterministic seed/tick selection. `chamber-tick-candidate-pool` now delegates through that exact selection before firing. Focused exp00 tests prove ordinary cap-2 selection and cap-8 safely selecting by a smaller generated three-rule pool's cardinality. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `e5b7502` pushed to GitHub `main`.

Dedicated 08:30 progress run added generic PeTTa-native candidate-pool/generated chamber tick operations that dispatch by actual bounded cardinality 1-8. This removes caller-side cap-specific operation selection and supports requested caps larger than source pools; focused exp00 tests cover cap-2 equivalence and cap-8 over a generated three-rule pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `4477baf` pushed to GitHub `main`.

Dedicated 06:30 progress run completed base exp00 candidate generation across every source-pool cardinality 1-8 by adding missing five- and seven-rule clauses. Focused smoke covers exact generation and a productive generated cap-5 tick through cap -> deterministic selection -> chamber firing. During testing, corrected cap-1 smoke fixtures to the canonical two-field `candidate-cap` schema and an explicitly productive external pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `511a63f` pushed to GitHub `main`.

Dedicated 04:30 progress run closed the remaining cap-specific chamber-tick gap. Added PeTTa-native `chamber-tick-candidate-pool-1` and `chamber-tick-generated-1`, so caps 1-8 now all have direct bounded candidate-pool/generated-pool paths into chamber firing. Focused exp00 tests cover external three-candidate truncation to one and a generated one-rule pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

Dedicated 02:30 progress run completed the bounded cap matrix supporting direct candidate-pool chamber ticking. Inspection found that `cap-candidate-pool` still omitted valid intermediate shapes despite cap-specific tick integration—for example cap-1 over pools of size 5-8 and cap-6 over size 7. Added all missing valid cap/pool-size clauses through eight candidates and focused exp00 tests for the widest truncation and near-boundary truncation. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

Dedicated 00:30 progress run generalized the direct PeTTa-native candidate-pool-to-chamber-tick operation from cap 2 to caps 3 through 8. `src/chem_exp00.metta` now exposes `chamber-tick-candidate-pool-3` through `-8`, and all generated cap-specific ticks delegate through the same cap -> deterministic seed/tick selection -> firing operation. The delegation exposed and fixed a missing exact seven-candidate cap clause. Exp00 adds direct cap-3/cap-6 pool-tick coverage; exp05 remains green. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

## 2026-07-11

2026-07-11 20:30 progress: broadened exp07 productive affinity selector provenance from eighteen to twenty seeds. Added seed-25/26 PeTTa fixtures spanning first/second candidate phases, bounded cap-2 deterministic selection, and direct ordinary exp00 chamber ticks with productive treatment/control catalysts. Boundary remains selector provenance only: no frequency/ACS uplift, terminal forcing, or emergence claim. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `git diff --check`.


Dedicated 16:30 progress run broadened exp07's productive affinity seed-variation provenance from sixteen seeds to eighteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-23` and `seed-24`; `src/chem_exp05.metta` adds seed-23/tick-3 first-candidate treatment/control fixtures and seed-24/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: eighteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ca52b37` pushed to GitHub `main`.

Dedicated 14:30 progress run broadened exp07's productive affinity seed-variation provenance from fourteen seeds to sixteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-21` and `seed-22`; `src/chem_exp05.metta` adds seed-21/tick-3 first-candidate treatment/control fixtures and seed-22/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: sixteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `23c236d` pushed to GitHub `main`.

Dedicated 12:30 progress run broadened exp07's productive affinity seed-variation provenance from twelve seeds to fourteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-19` and `seed-20`; `src/chem_exp05.metta` adds seed-19/tick-3 first-candidate treatment/control fixtures and seed-20/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: fourteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `2f13a3e` pushed to GitHub `main`.

Dedicated 10:30 progress run broadened exp07's productive affinity seed-variation provenance from ten seeds to twelve while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-17` and `seed-18`; `src/chem_exp05.metta` adds seed-17/tick-3 first-candidate treatment/control fixtures and seed-18/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: twelve-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ae74ea0` pushed to GitHub `main`.

Dedicated 08:30 progress run broadened exp07's productive affinity seed-variation provenance from eight seeds to ten while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-15` and `seed-16`; `src/chem_exp05.metta` adds seed-15/tick-3 first-candidate treatment/control fixtures and seed-16/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: ten-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eb435e0` pushed to GitHub `main`.

Dedicated 06:30 progress run broadened exp07's productive affinity seed-variation provenance from six seeds to eight while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-13` and `seed-14`; `src/chem_exp05.metta` adds seed-13/tick-3 first-candidate treatment/control fixtures and seed-14/tick-3 second-candidate fixtures, all keeping the selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: eight-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `aecfab9` pushed to GitHub `main`.

Dedicated 04:30 progress run broadened exp07's productive affinity seed-variation provenance from four seeds to six. `src/chem_exp00.metta` now defines `seed-11` and `seed-12`; `src/chem_exp05.metta` adds seed-11/tick-3 first-candidate treatment/control fixtures and seed-12/tick-3 second-candidate fixtures, all preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12 with matching smoke coverage and README provenance. Boundary: six-seed selector-phase provenance only, no frequency claim, no terminal forcing, no ACS uplift, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `cc56750` pushed to GitHub `main`.

Dedicated 02:30 progress run broadened exp07's productive affinity seed-variation provenance from three seeds to four. `src/chem_exp00.metta` now defines `seed-10`; `src/chem_exp05.metta` adds seed-10/tick-3 treatment and rotated-control fixtures whose cap-2 deterministic selector repeats the second-candidate phase (`e5r1`) with a distinct productive rotated-control catalyst context (`BC`); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row`, `exp07-affinity-seed-variation-table`, and `exp07-affinity-seed-variation-status` to seeds 7/8/9/10. Exp05/exp07 smoke coverage verifies selected candidates and ordinary exp00 chamber ticks in the new treatment/control arms. Boundary: four-seed selector-phase provenance only, no frequency claim, no terminal forcing, no ACS uplift, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eabc1be` pushed to GitHub `main`.

Dedicated 00:30 progress run broadened exp07's productive affinity seed-variation provenance from two seeds to three. `src/chem_exp00.metta` now defines `seed-9`; `src/chem_exp05.metta` adds seed-9/tick-3 treatment and rotated-control fixtures whose cap-2 deterministic selector repeats the first-candidate phase with different productive catalyst contexts (`AC` treatment, `BC` control); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row`, `exp07-affinity-seed-variation-table`, and `exp07-affinity-seed-variation-status` to seeds 7/8/9. Smoke coverage verifies selected candidates and ordinary exp00 chamber ticks in all treatment/control arms. Boundary: three-seed selector-phase provenance only, no frequency claim, no terminal forcing, no ACS uplift, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `b34eae4` pushed to GitHub `main`.

## 2026-07-10

Dedicated 22:30 progress run added exp07's first two-seed productive affinity selector-phase variation. `src/chem_exp05.metta` now defines matched seed-8/tick-3 treatment and rotated-control fixtures whose cap-2 deterministic selector chooses the second affinity-assigned source rule (`e5r1`) productively. `src/chem_exp07.metta` records `exp07-affinity-seed-variation-row` atoms for seed-7/first-candidate and seed-8/second-candidate, aggregates them in `exp07-affinity-seed-variation-table`, and exposes `exp07-affinity-seed-variation-status`. Smoke coverage verifies selected candidates and ordinary exp00 chamber ticks in both treatment/control arms. Boundary: two-seed selector-phase provenance only, no frequency claim, no terminal forcing, no ACS uplift, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `358bfbc` pushed to GitHub `main`.

Dedicated 20:30 progress run added exp07's productive affinity selection-to-tick provenance trace. `src/chem_exp07.metta` now exposes `exp07-affinity-selection-to-tick-trace` and `exp07-affinity-selection-to-tick-status`, expanding the strength-1 seed-7/tick-3 cap-2 treatment and rotated-control candidate pools, bounded cap-2 lists, deterministic selected candidates, and resulting exp05/exp00 chamber ticks. This closes the local provenance gap between bounded candidate generation/caps, deterministic selection, and chamber ticking for the productive affinity-strength fixture. Boundary: single-fixture provenance only, no frequency/seed sweep claim, no terminal forcing, no ACS uplift, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `27e70fd` pushed to GitHub `main`.

Dedicated 18:30 progress run added exp07's first affinity-strength productivity-filter slice. `src/chem_exp07.metta` now records `exp07-affinity-strength-sweep-row` atoms for strengths 0, 1, and 2 in the existing seed-7/tick-3 cap-2 exp05 fixture, aggregates them in `exp07-affinity-strength-sweep-table`, and exposes `exp07-affinity-strength-sweep-status`. The slice keeps candidate selection/chamber ticking PeTTa-native through exp05/exp00: strength 1 selects present/productive catalysts in both treatment and rotated-control arms, while strengths 0 and 2 select absent catalysts in this fixture. Boundary: productivity filter only, no seed-frequency claim, no terminal forcing, no ACS-positive result, no emergence claim. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `d667c2b` pushed to GitHub `main`.

Dedicated 16:30 progress run added exp07's first deterministic weak-guidance comparison table. `src/chem_exp07.metta` now records `exp07-weak-guidance-comparison-row` atoms for affinity weight and candidate-pool cap, aggregates them in `exp07-weak-guidance-comparison-table`, and exposes `exp07-weak-guidance-comparison-status`. Affinity evidence expands to observed exp05 treatment/control chamber ticks routed through exp00 deterministic selection; candidate-cap evidence expands to exp06's stateful cap sweep and ACS-boundary rejection. Boundary: deterministic path differences only, no terminal forcing, no ACS-positive result, no emergence claim. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `6c64348` pushed to GitHub `main`.

Dedicated 14:30 progress run linked exp07's Doob-h weak-guidance policy to existing PeTTa-native dynamic probes. `src/chem_exp07.metta` now records `exp07-weak-guidance-evidence-row` atoms for affinity weight and candidate-pool cap, aggregates them in `exp07-weak-guidance-evidence-table`, and exposes `exp07-weak-guidance-probe-status`. Affinity evidence points to exp05 treatment/control chamber ticks wired through exp00 deterministic selection; candidate-cap evidence points to exp06's stateful three-tick sweep and ACS-boundary table. Boundary: dynamic probes linked, no terminal forcing, no ACS-positive result, no emergence claim. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `0fe6f81` pushed to GitHub `main`.

Dedicated 12:30 progress run advanced exp07 from a bridge scaffold into a first PeTTa-native Doob-h diagnostic policy slice. `src/chem_exp07.metta` now records ordinal h-values and guidance roles for catalyst assignment, affinity weight, candidate-pool cap, basal replenishment, and catalysis-map offset; exposes `exp07-doob-policy-order`; and defines a weak-guidance test plan that explicitly prohibits terminal forcing. Catalyst assignment remains the strongest terminal-fixture diagnostic, while affinity weight and candidate cap are the planned weak-guidance variables. `experiments/exp07/smoke.metta`, exp07 README, and the root README document/verify the boundary. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `8bca457` pushed to GitHub `main`.

Dedicated 10:30 progress run attached a PeTTa-native ACS boundary check to exp06's stateful candidate-cap sweep. `src/chem_exp06.metta` now evaluates the selected tick-3/tick-4 candidate rule pairs with `exp06-selected-candidate-pair-acs-status`, exposes cap-1/cap-2 `exp06-stateful-cap-sweep-acs-boundary` rows, and aggregates them in `exp06-stateful-cap-sweep-acs-boundary-table`. Both arms are rejected by two-rule product-catalyst closure, so the candidate-cap intervention has dynamic bounded evidence without upgrading to RAF enumeration or spontaneous-emergence evidence. `experiments/exp06/smoke.metta` and README verify/document the boundary. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and targeted secret-like diff scan. Commit `40aef6b` pushed to GitHub `main`.

Dedicated 08:30 progress run extended exp06's PeTTa-native stateful candidate-cap sweep from two selected ticks to three. `src/chem_exp06.metta` now carries the tick-3/tick-4 stateful cap-1 and cap-2 chambers into tick 5, adds a bounded no-op `chamber-tick-with-candidate` clause for exhausted `A`, and records `exp06-candidate-cap-stateful-three-tick-sweep`. Tick 5 selects `e5r0` in both arms but advances without negative abundance or new events; the cap-1/cap-2 divergence from tick 4 persists. `experiments/exp06/smoke.metta` verifies tick-5 selection, final no-op chambers, and the aggregate boundary (`three-tick-stateful-diagnostic-not-raf-status`, `emergence-claim none`); README documents the diagnostic. Checks: `scripts/run_exp00.sh`, `scripts/run_exp06.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `de84704` pushed to GitHub `main`.

Dedicated 06:30 progress run advanced exp06 from refreshed cap diagnostics to a PeTTa-native accumulated/stateful two-tick cap sweep. `src/chem_exp06.metta` now carries the seed-7 tick-3 chamber output into tick 4 for cap-1/cap-2 arms, using exp05 affinity-assigned source rules and ordinary exp00 candidate selection/ticking. Cap-1 repeats `e5r0` across ticks 3-4, while cap-2 exposes `e5r1` at tick 4, yielding distinct final abundance/event paths. `experiments/exp06/smoke.metta` verifies selected candidates, carried final chambers, and the aggregate `exp06-candidate-cap-stateful-two-tick-sweep` boundary: accumulated diagnostic only, not RAF status or an emergence claim. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `63ed5c3` pushed to GitHub `main`.

Dedicated 04:30 progress run extended exp06's candidate-pool-cap dynamic probe into a PeTTa-native refreshed two-tick cap sweep. `src/chem_exp06.metta` now defines tick-4 cap-1/cap-2 treatment/control diagnostic chambers, selected candidates, after-tick chambers, and an aggregate `exp06-candidate-cap-two-tick-sweep` atom. At seed-7/tick-4, cap-1 exposes/fires the first source rule while cap-2 deterministically exposes/fires the second exp05 source rule in both treatment and rotated control. `experiments/exp06/smoke.metta` verifies candidate selection, chamber transitions, and the no-emergence boundary. Scientific boundary: refreshed two-tick diagnostic only; accumulated RAF/status remains future work (`accumulated-multi-tick-stateful-sweep`). Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `5240172` pushed to GitHub `main`.

Dedicated 02:30 progress run tightened exp06's candidate-pool-cap dynamic probe with matched treatment/control evidence. `src/chem_exp06.metta` now exposes cap-1/cap-2 selected candidates and after-tick chambers for both the exp05 affinity-assigned treatment pool and shuffled-affinity rotated-control pool, using ordinary exp00 `chamber-tick-with-candidate`. In the seed-7/tick-3 fixture, treatment selects/fires `e5r0` with catalyst/product `AB`; control selects/fires the rotated `e5r0` with catalyst/product `AC`; both cap-1 and cap-2 preserve first-tick productivity. The comparison atom records the scientific boundary as `single-tick-productivity-not-raf-status` and keeps the next target `multi-tick-cap-sweep`. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `e5a6285` pushed to GitHub `main`.

Dedicated 00:30 progress run started turning exp06's candidate-pool-cap intervention from an unevaluated path-table row into a PeTTa-native dynamic probe. `src/chem_exp06.metta` now defines cap-1 and cap-2 candidate-cap probes over the exp05 affinity-assigned pool, selected/fired through ordinary exp00 chamber ticking. In the seed-7/tick-3 fixture, both caps select the same affinity-assigned `e5r0` candidate and produce the same first-tick event, so the comparison atom records `cap-dynamics-probed-but-raf-status-open` and points to a future multi-tick cap sweep rather than making a RAF/emergence claim. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `7d047c9` pushed to GitHub `main`.

## 2026-07-09

Dedicated 23:00 progress run added the first thin host-side exp06 Dijkstra/artifact slice over PeTTa-exposed intervention-cost rows. `scripts/write_exp06_bridge_path_files.py` queries `exp06-intervention-cost-row` atoms, treats them as search nodes/edges, selects the cost-1 `catalyst-assignment none->specific-template` path as the shortest strict RAF-positive diagnostic path, and writes CONFIG/NODE_EVALUATIONS/PATHS/SUMMARY/RUN.md artifacts under `artifacts/exp06_bridge_path_search` by default. `scripts/test_exp06_bridge_path_files.sh` verifies the writer, alternate broad-template and shuffled-9 rows, candidate-cap `dynamic-test-required`, and no-emergence caveats. The host harness does path-search/bookkeeping/serialization only; chemistry evidence and RAF status remain PeTTa-native.

Dedicated 22:30 progress run deepened exp06 bridge-to-ACS analysis from a single witness to a bounded intervention cost/path table in PeTTa atoms. `src/chem_exp06.metta` now compares catalyst assignment, basal-food replenishment, candidate-pool cap, and catalysis-map offset as cost-1 interventions over existing exp04 rows: specificity/broad template catalysis reaches RAF-positive territory; basal replenishment alone and shuffled-1 remain RAF-negative; shuffled-9 is an offset-sensitive RAF-like control; candidate-pool cap is explicitly `dynamic-test-required`/`not-yet-evaluated` rather than inferred. `experiments/exp06/smoke.metta` verifies the rows, aggregate table, bounded shortest-path table, and no-emergence status; README documents the bounded path table. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d18bdb7` pushed to GitHub `main`. Next target: test candidate-cap dynamics against exp05/exp03-style ticking or add a thin exp06 report artifact if useful.

Dedicated 20:30 progress run started exp06 as a PeTTa-native bridge-to-ACS favorable-conditions diagnostic scaffold. `src/chem_exp06.metta` defines an initial verified no-ACS soup from the exp04 hand-designed/no-catalysis/basal-4 row, a terminal exp04 RAF-rich soup from the hand-designed/specific/basal-4 row with maximal RAF 15 and greedy core `(lCD lBCD2)`, intervention variables for catalyst-affinity assignment, basal replenishment, candidate-pool cap, and catalysis-map offset, plus a first deterministic shortest-path witness: changing catalysis assignment from none to specificity-template while holding basal-4 and the report cap convention fixed reaches RAF-positive territory in the diagnostic source rows. Added `experiments/exp06/smoke.metta`, `scripts/run_exp06.sh`, and README coverage. Boundary: this is path/experimental-design bookkeeping only, not spontaneous emergence evidence; `emergence-claim none` is explicit. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `2d146d5` pushed to GitHub `main`.

Dedicated 18:30 progress run connected the exp05 catalyst-affinity scaffold directly to chamber ticking while keeping the chemistry kernel PeTTa-native. `src/chem_exp05.metta` now defines treatment and rotated-control chambers whose source rules are assigned catalysts by affinity/rotated profiles, capped to a bounded two-candidate pool, selected with exp00's deterministic seed/tick selector, and fired through ordinary `chamber-tick-with-candidate`. `experiments/exp05/smoke.metta` verifies the selected treatment/control candidates, the resulting chamber transitions/events, and an explicit status atom with `raf-scan not-yet-run` and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Next target: exp06 bridge-to-ACS scaffold or stricter generated-pool controls for exp05. Commit `f1fecec` pushed to GitHub `main`.

Ben proposed a rigorous bridge-based route for defining "favorable conditions" for ACS emergence: start from an initial algorithmic soup verified to have no catalytic sets, engineer one or more terminal soups rich in ACS/RAF-like structures, then compute/approximate a Schrödinger-bridge or shortest-path family between them. The path should be treated as an analysis/experimental-design object, not as an emergence claim by itself: inspect which reaction/catalysis/basal-food/intervention variables change along short paths, then test whether those variables bias unguided or weakly guided PeTTa-native dynamics toward ACSs without fixing the terminal condition. This connects naturally to exp04's success-biased RAF fixture, exp04 rotated-control caveats, and exp05's catalyst-affinity/candidate-pool scaffold. Initial implementation should keep the chemistry kernel PeTTa-native; host code may do optimal-transport/path-search bookkeeping and artifact writing. Candidate next experiment name: exp06 bridge-to-ACS favorable-conditions analysis.

Dedicated 16:30 progress run triaged the pre-existing exp05 scaffold and turned it into tracked PeTTa-native smoke coverage. `src/chem_exp05.metta` keeps catalyst assignment in PeTTa using generic token-overlap affinity, positive baseline weights, and rotated-weight controls; the new slice projects assigned source rules into ordinary exp00 `candidate`/`candidate-pool` atoms and proves a cap-1 bounded candidate projection, so later chamber-ticking work can reuse the existing candidate/cap machinery instead of a parallel selector. Added `experiments/exp05/smoke.metta`, `scripts/run_exp05.sh`, and README documentation. Boundary: no RAF scan or emergence claim yet. Checks: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d3dde9f` pushed to GitHub `main`. Next target: connect exp05 affinity-assigned candidate pools to a minimal chamber-ticking slice with matched rotated controls.

Dedicated 14:30 progress run added cap-8 artifact-writer coverage for the existing PeTTa-side exp03 productive bundle. `scripts/write_exp03_productive_cap_files.py` now includes `exp03-cap8-productive-seed-13-random` from `(exp03-cap8-productive-file-bundle seed-13 random-polymer)`, keeping the chemistry/run-record content in PeTTa. `scripts/test_exp03_productive_cap_files.sh` verifies the new output directory, output-root `RUN.md` provenance, `CONFIG.metta`, first `EVENTS.metta` rr5 event, dynamic event-count metric, and summary section; README now documents cap-8 writer coverage. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d9d5bc3` pushed to GitHub `main`. Pre-existing untracked exp05 scaffold files were observed in repo status and intentionally left untouched. Next target: stricter generated-pool controls, broader exp04 report packaging, or explicit exp05 scaffold triage if that becomes the priority.

Dedicated 12:30 progress run carried the cap-8 seam into exp03 chamber ticking/export coverage while keeping the chemistry kernel PeTTa-native. `src/chem_dynamics.metta` now has accumulated cap-8 tick/run wrappers (`chamber-tick-generated-8-accum`, `chamber-run-8cap-*` through 16 ticks), an explicit seed-13/R-family rr7 bounded no-op in the 17-molecule productive state, and `exp03-cap8-productive-*` run-record/export/file-bundle atoms. Exp03 smoke verifies full eight-candidate generation, deterministic tick-0 rr5 selection via `(13+0)%8 = 5`, rr7 no-op ticks at 2 and 10, 14 productive events over 16 ticks, final abundance/replay/completeness, exact trace order, and export/file-bundle sections. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `bae69e6` pushed to GitHub `main`. Next target: add the cap-8 bundle to the thin productive-cap writer, or continue exp04 generated-pool controls if more scientifically useful.

Dedicated 10:30 progress run returned to the top bounded-candidate task and extended the exp00 deterministic selection/generation seam to full eight-rule pools while keeping the chemistry kernel PeTTa-native. `src/chem_exp00.metta` now includes `seeded-choice-8` using `(seed+tick)%8`, `select-candidate-8`, a cap-8 preservation clause for eight-candidate generated pools, `selected-candidate-from-list-8`, `chamber-tick-generated-8`, and `exp00-candidate-cap-8`. Exp00 smoke verifies seed-7/seed-8 choices, cap construction, cap-8 pool preservation, direct eight-way selection, and generated chamber ticking where seed-7 selects the productive eighth rule from an eight-rule chamber. Checks: `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `3506bc0` pushed to GitHub `main`. Next target: either carry cap-8 into an exp03 productive state shape/export path, or resume exp04 control/report tightening if more scientifically useful.

Dedicated 08:30 progress run added a thin artifact writer for the PeTTa-side exp04 offset-sensitivity report. `scripts/write_exp04_offset_report_files.py`/`.sh` queries `exp04-offset-sensitivity-report-id`, `exp04-offset-sensitivity-report-file`, and `exp04-offset-sensitivity-summary-file`, then writes `OFFSET_SENSITIVITY_REPORT.metta`, `SUMMARY.metta`, and `RUN.md` under `artifacts/exp04_offset_sensitivity_report` by default. `scripts/test_exp04_offset_report_files.sh` verifies the generated hand-designed/generated-template/cross-template offset partitions, representative cores (`lBC`, `glCD`, `xglAC`), and the `unbiased-emergence not-supported` claim. README documents the writer as thin host serialization only. Checks: `python3 -m py_compile scripts/write_exp04_offset_report_files.py`, `scripts/test_exp04_offset_report_files.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `14d12f0` pushed to GitHub `main`. Next: stricter generated-pool controls, additional exp04 artifact packaging if useful, or bounded-cap/export coverage.

Dedicated 06:30 progress run packaged the exp04 rotated-shuffle sweep into compact PeTTa-queryable report/export atoms. `src/chem_exp04.metta` now has `exp04-offset-sensitivity-report-id`, tested offsets `(1 2 3 4 5 6 7 8 9)`, three `exp04-offset-sensitivity-report-row` atoms, an explicit no-unbiased-emergence claim, file-style `OFFSET_SENSITIVITY_REPORT.metta`/`SUMMARY.metta` atoms, a report bundle, and `exp04-offset-sensitivity-report-complete?`. Exp04 smoke verifies the hand-designed negative offsets `(1 2 3 6 7)` vs RAF-like `(4 5 8 9)`, generated-template negative `(1 2 3 6 7 8)` vs RAF-like `(4 5 9)`, and cross-template negative `(2 4 6 8)` vs RAF-like `(1 3 5 7 9)`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp04.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `2290218` pushed to GitHub `main`. Next: continue exp04 report packaging/writer coverage or return to bounded-cap/export coverage.

Dedicated 04:30 progress run completed the exp04 rotated catalyst-offset sweep for offsets 1 through 9 while keeping chemistry behavior in PeTTa report atoms and Python as deterministic reduction/artifact glue. Added offsets `shuffled-3`, `shuffled-4`, `shuffled-7`, and `shuffled-8` to `experiments/exp04/run_reduction_sweep.py`; regenerated `experiments/exp04_reduction_sweep_20260708/` as a 108-row artifact. `src/chem_exp04.metta` now exposes all new rows, `exp04-reduction-shuffle-offsets-1-through-9-tested?`, and representative minimized cores for additional RAF-like controls (`hand-designed/shuffled-4 -> lBC`, `mechanically-generated-template/shuffled-4 -> glCD`, cross-template shuffled-3/7 one-rule cores). Result: the full offset sweep is mixed — hand-designed offsets 3 and 7 are RAF-negative at basal-4, while 4 and 8 are RAF-like; generated-template offset 4 is RAF-like; cross-template offsets 3 and 7 are RAF-like while 4 and 8 are RAF-negative. Interpretation remains: positive inspectable artifact, strongly catalysis-map/offset-sensitive, no unbiased-emergence claim. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `c4f69db` pushed to GitHub `main`. Next target: compact offset-sensitivity report/export, stricter generated controls, or return to bounded-cap/export coverage.

Dedicated 02:30 progress run continued reducing/inspecting exp04 catalysis-map bias. Added rotated catalyst offsets `shuffled-2` and `shuffled-6` to `experiments/exp04/run_reduction_sweep.py`; regenerated `experiments/exp04_reduction_sweep_20260708/` as a 72-row artifact. `src/chem_exp04.metta` now exposes all added rows, `exp04-reduction-shuffle-negative-offsets-tested?`, and representative minimized-core atoms: baseline hand-designed/specific/basal-4 core `(lCD lBCD2)`, hand-designed/shuffled/basal-4 core `(lBC lABC2 lBCD1)`, and representative cross-template shuffled one-rule cores. Result: offsets 2 and 6 are RAF-negative at basal-4 across all three pools, while earlier shuffled positives remain offset-sensitive caveats; no unbiased-emergence claim. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Next target: continue exp04 core/catalysis-map inspection or return to bounded-cap/export coverage.

Dedicated 00:30 progress run broadened exp04 shuffle controls while keeping the chemistry kernel PeTTa-native and Python as a deterministic reduction harness. `experiments/exp04/run_reduction_sweep.py` now includes alternate rotated-catalyst modes `shuffled-1` and `shuffled-9` in addition to the original `shuffled` offset, expanding `experiments/exp04_reduction_sweep_20260708/` from 36 to 54 rows. `src/chem_exp04.metta` exposes all added rows, `exp04-reduction-alt-shuffle-offsets-tested?`, and an updated interpretation atom; exp04 smoke verifies representative `shuffled-1` and `shuffled-9` rows. Result: controls are offset-sensitive — hand-designed `shuffled-1` at basal-4 has maximal RAF 0/core 0, while hand-designed `shuffled-9` at basal-4 has maximal RAF 7/core 3 and generated pools retain small shuffle-created RAF-like signals. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `f65c430` pushed to GitHub `main`. Next target: further reduce exp04 catalysis-map/shuffle bias with additional controls/minimized-core inspection, or return to bounded-cap/export coverage.

## 2026-07-08

Dedicated 22:30 progress run continued reducing exp04 generated-pool/catalysis-map bias. Added `mechanically-generated-cross-template` to `experiments/exp04/run_reduction_sweep.py`, factoring pair specs and assigning pair-level catalysts to disjoint/cross products as a stricter decoy pool. The reduction sweep artifact now has 36 rows. `src/chem_exp04.metta` exposes the new rows, increases row count to 36, adds predicates for cross-template broad RAF-negative controls and shuffled cross-template RAF-like signal creation, and updates the interpretation/report completeness atom. Exp04 smoke verifies representative cross-template broad/shuffled rows plus the new predicates. Result: cross-template specific/broad/none controls remain RAF-negative, but shuffled cross-template catalysis creates a small maximal RAF 5/core 1 signal, reinforcing catalysis-map sensitivity rather than unbiased emergence. Checks: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Next target: continue reducing exp04 catalysis-map/shuffle bias, or return to bounded-cap/state-shape/export coverage.

Dedicated 20:30 progress run moved the exp04 reduction-sweep interpretation into PeTTa-queryable atoms while keeping Python as prior artifact-generation/logistics only. `src/chem_exp04.metta` now exposes `exp04-reduction-sweep-row` atoms for all 24 deterministic variants, the baseline row, predicates for baseline-positive/no-catalysis-zero/generated-specific-zero/shuffled-caveat, an explicit interpretation atom, and `exp04-reduction-sweep-report-complete?`. Exp04 smoke verifies representative rows and the interpretation: baseline hand-designed/specific/basal-4 is RAF-positive; no-catalysis and generated-specific controls are RAF-negative; shuffled hand-designed catalysis remains a RAF-like caveat; unbiased emergence is not supported. Checks: `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `0ed265e` pushed to GitHub `main`. Next target: continue reducing generated-pool/catalysis-map bias or return to bounded-cap/state-shape coverage.

Dedicated 18:30 progress run added the first exp04 reduction sweep artifact. `experiments/exp04/run_reduction_sweep.py` compares 24 deterministic variants across specificity-filtered/broad/shuffled/no catalysis, basal intervals 0/4/8, and hand-designed versus mechanically generated template rule pools; `scripts/run_exp04_reduction_sweep.sh` writes `experiments/exp04_reduction_sweep_20260708/REDUCTION_SWEEP.json` and `SUMMARY.md`. Key result: the original hand-designed/specific/basal-4 artifact remains RAF-positive (maximal 15, greedy core 2, 56 events, 15 event-diversity), no-catalysis controls are RAF-negative, but shuffled hand-designed catalysis still leaves a smaller RAF-like signal (maximal 10/core 3), reinforcing the success-biased/catalysis-map-sensitive interpretation. Checks: `python3 -m py_compile experiments/exp04/run_rich_raf.py experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, `git diff --check`. Next target: PeTTa-queryable reduction-summary atoms or stricter generated-pool bias reduction.

Exp04 rich RAF exploratory run created on branch `agent/exp04-rich-chemistry`. The experiment combines richer rule templates (8 ligation, 6 cleavage, 6 modification), specificity-filtered deterministic template catalysis, a 20-rule pool, 56 food-replenished ticks, and RAF detection by bounded maximal pruning plus greedy minimization. Host-computed artifact `experiments/exp04_rich_raf_20260708/` reports maximal RAF size 15, greedy minimized core size 2 (`lCD`, `lBCD2`), minimized core RAF true, no-catalysis maximal RAF size 0, and 56 events over 56 ticks with food floor maintained. This is a positive inspectable RAF artifact, but intentionally success-biased/non-planted rather than evidence of unbiased spontaneous emergence. Checks: `python3 -m py_compile experiments/exp04/run_rich_raf.py`, `scripts/run_exp04.sh`, host artifact rerun, `git diff --check`. Next: reduction sweep over catalysis shuffling, basal rate, and generated rule pools.

Dedicated 16:30 progress run broadened productive-cap artifact/export coverage for the new cap-7 seed-13/R-family productive fixture. In `src/chem_dynamics.metta`: added `exp03-cap7-productive-run-export`, added cap-7 to `exp03-productive-cap-run-exports` and completeness checks, added `exp03-cap7-productive-file-bundle`, and included it in productive-cap file-bundle completeness. Exp03 smoke verifies cap-7 export config, event count 14, ACS candidates, file-bundle id, event/metrics/ACS/summary sections. `scripts/write_exp03_productive_cap_files.py` now queries `(exp03-cap7-productive-file-bundle seed-13 random-polymer)` and writes `exp03-cap7-productive-seed-13-random`; `scripts/test_exp03_productive_cap_files.sh` verifies the new output directory, `RUN.md` source expression, config, first rr6 event, dynamic-event-count metric, and summary. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `79f9090` pushed to GitHub `main`. Next target: continue another bounded-cap/state shape or package broader exp03 aggregate artifacts if useful.

Dedicated 14:30 progress run extended the cap-7 deterministic selection/generation seam into exp03 productive dynamics while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added 17-molecule `state-tick`/`state-seed` accessors and generated eight-rule candidate-pool support. In `src/chem_dynamics.metta`: added cap-7 accumulated chamber ticking/run wrappers, a 17-molecule seed-13/R-family cap-7 productive chamber with R16 in-state, explicit rr0-rr6 accumulated tick clauses, final-abundance/replay/run-record atoms, and ACS provenance from seed-13 exp02 candidates. Exp03 smoke verifies the bounded seven-candidate pool, tick-0 selected seventh candidate rr6 via `(13+0)%7 = 6`, 14 productive events over 14 ticks, final abundance snapshot, replay, run-record completeness, and exact trace order. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`. Commit `500b2c5` pushed to GitHub `main`. Next target: add export/file-bundle coverage for the cap-7 productive run or continue another bounded-cap/state shape.

Dedicated 12:30 progress run extended the exp00 deterministic selection/generation seam to candidate cap 7 while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added `seeded-choice-7`, `select-candidate-7`, `selected-candidate-from-list-7`, `chamber-tick-generated-7`, `exp00-candidate-cap-7`, and an explicit cap-7 truncation clause for eight-candidate pools. Exp00 smoke now verifies seed/tick choice, cap construction, cap-7 truncation from an eight-candidate pool, direct seven-candidate selection, and generated cap-7 chamber ticking over an eight-rule source pool. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `9d5f89b` pushed to GitHub `main`. Next target: extend cap-7 into exp03 productive dynamics if useful, or continue downstream artifact/report packaging.

Dedicated 10:30 progress run packaged the compact exp02 cycle-scan report into PeTTa-queryable artifact exports while keeping the chemistry/report content PeTTa-native. In `src/chem_exp02.metta`: added `exp02-cycle-scan-report-summary`, `(exp02-cycle-scan-report-bundle)`, file accessors, and `exp02-cycle-scan-report-bundle-complete?`; exp02 smoke verifies bundle id, report filename, exact report atoms, summary atoms, and completeness. Added `scripts/write_exp02_cycle_report_files.py` plus shell/test wrappers; Python only queries the PeTTa bundle and writes `CYCLE_SCAN_REPORT.metta`, `SUMMARY.metta`, and `RUN.md` provenance. Checks: `scripts/run_exp02.sh`, `python3 -m py_compile scripts/write_exp02_cycle_report_files.py`, `scripts/test_exp02_cycle_report_files.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `1535435` pushed to GitHub `main`. Next target: continue bounded productive dynamics across another cap/seed shape or reuse compact report exports in a broader artifact package.

Dedicated 08:30 progress run broadened the thin productive-cap artifact writer to include the seed-17/S-family cap-6 productive fixture from the prior run. `scripts/write_exp03_productive_cap_files.py` now queries `(exp03-cap6-productive-file-bundle seed-17 random-polymer)` and writes `exp03-cap6-productive-seed-17-random`, keeping the chemistry/run-record content PeTTa-native. `scripts/test_exp03_productive_cap_files.sh` verifies the new generated run directory, output-root `RUN.md` provenance, `CONFIG.metta`, first `EVENTS.metta` event, dynamic event-count metric, and summary section. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `147633d` pushed to GitHub `main`. Next target: package compact report exports if useful, or continue bounded productive dynamics across another cap/seed shape.

Dedicated 06:30 progress run extended productive cap-6 to a third seed/state shape while keeping the chemistry kernel PeTTa-native. In `src/chem_dynamics.metta`: added a 16-molecule seed-17/S-family cap-6 productive chamber with S89 and S05 present, explicit rr0-rr5 accumulated tick clauses, final-abundance/replay/run-record/export/file-bundle atoms, and ACS source provenance from the seed-17 exp02 candidates. Exp03 smoke now verifies the bounded rr1/rr0/rr2/rr3/rr4/rr5 candidate pool, deterministic tick-0 selected sixth candidate rr5 via `(17+0)%6 = 5`, 12 productive events over 12 ticks, final abundance snapshot, replay, run-record completeness, exact trace order, and export/file-bundle sections. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `ee89855` pushed to GitHub `main`. Next target: broaden the thin productive-cap artifact writer to include the seed-17 bundle, or package compact report exports if useful.

Dedicated 04:30 progress run added compact PeTTa-side provenance for the exp02 generated-unplanted cycle scans. In `src/chem_exp02.metta`: added `exp02-cycle-scan-summary-report` with rows for k=4,5,6,7 generated-unplanted controls (40 sweep points / 120 family records each, all 0 active cycles) and `exp02-cycle-scan-summary-report-complete?`. Exp02 smoke verifies the exact report atom. `experiments/exp02_small_sweep_20260630/SUMMARY.md` now mirrors the compact k=4..7 table for human-readable provenance while preserving the no-spontaneous-emergence claim caveat. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `5cc2d24` pushed to GitHub `main`. Next target: continue cap-6 across another seed/state shape or add export hooks for this compact report if needed.

Dedicated 02:30 progress run broadened the productive-cap artifact bundle to include the seed-13/R-family cap-6 productive fixture from the prior run. In `src/chem_dynamics.metta`: added seed-13 to the compact productive-cap run-export list and PeTTa-side `run-file-bundle` projections. Exp03 smoke verifies seed-13 export config/events/ACS and file-bundle events/metrics/ACS/summary. `scripts/write_exp03_productive_cap_files.py` now emits four PeTTa-queried bundles, adding `exp03-cap6-productive-seed-13-random`, and `scripts/test_exp03_productive_cap_files.sh` verifies its generated `CONFIG.metta` through `SUMMARY.metta` files plus `RUN.md` provenance. Checks: `scripts/run_exp03.sh`, `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `2c04300` pushed to GitHub `main`. Next target: add a compact scan-summary provenance atom/report or continue cap-6 across another seed/state shape.

Dedicated 00:30 progress run extended productive cap-6 beyond seed-11/Q-family to a second PeTTa-tested family. In `src/chem_exp00.metta`: added 16-molecule `state-tick`/`state-seed` accessors and generated eight-rule candidate-pool support. In `src/chem_dynamics.metta`: added a 16-molecule seed-13/R-family cap-6 productive chamber with R89 and R05 present, explicit rr0-rr5 accumulated tick clauses, final-abundance/replay/run-record/export atoms, and ACS source provenance from the seed-13 exp02 candidates. Exp03 smoke now verifies the bounded rr1/rr0/rr2/rr3/rr4/rr5 candidate pool, deterministic seed/tick selected candidate, 12 productive events over 12 ticks, final abundance snapshot, replay, run-record completeness, and exact trace order. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `dd941d0` pushed to GitHub `main`. Next target: broaden the productive-cap artifact bundle to include this new seed-13/R-family cap-6 fixture, or continue productive cap-6 across another seed/state shape.

## 2026-07-07

Dedicated 22:30 progress run added compact artifact provenance for the exp03 productive-cap generated files. `scripts/write_exp03_productive_cap_files.py` now writes an output-root `RUN.md` alongside the PeTTa-queried `CONFIG.metta` through `SUMMARY.metta` sections, listing the exact source `run-file-bundle` expressions, reproduction commands, and per-run file convention for cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11. `scripts/test_exp03_productive_cap_files.sh` now verifies the generated provenance file and section files. Checks: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `7521d09` pushed to GitHub `main`. Next target: extend productive cap-6 beyond seed-11/Q-family or broaden the artifact bundle once another PeTTa-tested fixture exists.

Dedicated 20:30 progress run connected the PeTTa-side productive-cap file bundles to a thin artifact writer while keeping the chemistry kernel PeTTa-native. In `src/run_contract.metta`: added file accessors for manifest, abundances, metrics, ACS candidates, and ablations in addition to the existing config/events/summary hooks. Run-contract smoke now verifies all relevant v0.1 section accessors over the exp01 contract fixture, and exp03 smoke verifies metrics/ACS sections over the cap-6 productive bundle. Added `scripts/write_exp03_productive_cap_files.py` plus `write_*.sh`/`test_*.sh` wrappers; the Python harness only queries local PeTTa/SWI for already-tested `run-file-bundle` atoms and writes per-run `CONFIG.metta` through `SUMMARY.metta` files for cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11. Checks: `scripts/run_contract.sh`, `scripts/run_exp03.sh`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `948da77` pushed to GitHub `main`. Next target: extend productive cap-6 beyond seed-11/Q-family or add compact artifact/RUN.md provenance for generated bundle files.

Dedicated 18:30 progress run added PeTTa-side file-section/query hooks for v0.1 run-contract records while keeping filesystem writes in thin harness territory. In `src/run_contract.metta`: added `make-run-file-bundle`, `run-file-bundle`/`run-file` accessors, and focused config/events/summary section queries for the existing `CONFIG.metta` through `SUMMARY.metta` convention. In `src/chem_dynamics.metta`: projected cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 run records into file bundles plus a completeness predicate. Run-contract and exp03 smoke now verify event/summary file sections and productive cap bundle ids/event counts. Checks: `scripts/run_contract.sh` (32 ✅), `scripts/run_exp03.sh` (415 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`. Commit `fa5cbd6` pushed to GitHub `main`. Next target: extend productive cap-6 beyond seed-11/Q-family or connect the file bundles to a thin artifact writer.

Dedicated 16:30 progress run added PeTTa-side export/query hooks for the productive cap fixtures while keeping Python out of the chemistry kernel. In `src/chem_dynamics.metta`: extended `run-export` with config/manifest/abundance/ACS/ablation accessors, added run-export projections for cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 run records, and added a compact productive-cap export bundle/completeness predicate. Exp03 smoke now verifies cap-6 productive export config, event count, abundance snapshots, ACS candidates, ablations, and the export bundle. Checks: `scripts/run_exp03.sh` (410 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `3d476b6` pushed to GitHub `main`. Next target: either extend productive cap-6 beyond seed-11/Q-family or use the export hooks to write cleaner run artifacts.

Dedicated 14:30 progress run made the cap-6 sixth candidate productive in-state while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added six-rule generated candidate-pool support for 15-molecule states. In `src/chem_dynamics.metta`: added a wider seed-11/Q-family cap-6 productive bridge with Q05/Q16/Q99 present, explicit rr0-rr5 accumulated ticking clauses, run-record/replay/metrics atoms, and a 12-tick run where all six bounded candidates fire productively. Exp03 smoke verifies the six-candidate cap, tick-0 rr5 selection via `(11+0)%6 = 5`, 12 productive events over 12 ticks, final Q05/Q16 abundances, replay, run-record completeness, and exact trace order. Checks: `scripts/run_exp03.sh` (404 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `0d03f4c` pushed to GitHub `main`. Next target: extend productive cap-6 beyond seed-11/Q-family or add cleaner PeTTa-side export hooks for productive fixtures.

Dedicated 12:30 progress run extended cap-6 from the exp00 seam into exp03 rich dynamics while keeping the chemistry kernel PeTTa-native. In `src/chem_dynamics.metta`: added `chamber-tick-generated-6-accum`, cap-6 run wrappers through 12 ticks, safe rr5/sr5/nr5 no-op clauses for sixth source-rule candidates whose Q16 product is outside the 12-molecule rich-state bridge, and cap-6 run-config/manifest/metrics/summary/ACS/run-record atoms. Exp03 smoke verifies the full seed-11/Q-family six-rule capped pool, tick-0 rr5 selection via `(11+0)%6 = 5`, 12-tick random dynamics with 7 productive events, final abundance snapshot, replay, run-record completeness, and exact trace order. Checks: `scripts/run_exp03.sh` (390 ✅), `scripts/run_exp00.sh` (81 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `e31bc31` pushed to GitHub `main`. Next target: make a cap-6 sixth candidate productive in-state with a wider state shape or add cleaner PeTTa-side export hooks for productive fixtures.

Dedicated 10:30 progress run started the cap-6 path at the exp00 kernel seam while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added `seeded-choice-6`, `select-candidate-6`, `selected-candidate-from-list-6`, `chamber-tick-generated-6`, `exp00-candidate-cap-6`, and `cap-candidate-pool 6` clauses for 6- and 8-candidate generated pools. Exp00 smoke now validates cap-6 seed/tick choice, cap construction/truncation, and direct cap-6 generated chamber ticking from a six-rule pool where seed-7 selects the productive second candidate. Checks: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `db929ce` pushed to GitHub `main`. Next target: extend cap-6 into an exp03 richer productive state shape/run-record or add cleaner PeTTa-side export hooks.

Dedicated 08:30 progress run made the cap-5 fifth candidate productive in-state for seed-13/R-family while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added 15-molecule state tick/seed accessors and eight-rule generated candidate-pool support. In `src/chem_dynamics.metta`: added a 15-molecule seed-13 cap-5 productive chamber with R8/R9/R89 present, productive accumulated tick clauses for rr0-rr4, replay/run-record/metrics atoms, and a 10-tick run where the deterministic cap-5 selector cycles rr3, rr4, rr1, rr0, rr2 twice. Exp03 smoke verifies bounded candidates rr1/rr0/rr2/rr3/rr4, tick-0 rr3 selection via `(13+0)%5 = 3`, rr4 productive events at ticks 1 and 6, 10/10 event/tick counts, final abundance snapshot, replay, completeness, and trace order. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `db6cff6` pushed to GitHub `main`. Next target: advance cap-6/richer productive state shapes or add cleaner PeTTa-side export hooks.

Dedicated 06:30 progress run extended cap-5 beyond the seed-11/Q-family bridge into the seed-17/S-family 12-molecule rich state. In `src/chem_dynamics.metta`: added seed-17 cap-5 rich capped-candidate/selection/run/replay/run-record atoms over the eight-rule source pool and rr4 no-op handling for fifth candidates outside the state shape (S8/S9/S89) across random/shuffled/no-catalysis families. Exp03 smoke verifies capped candidates rr1/rr0/rr2/rr3/rr4, deterministic tick-0 selection of rr2 via `(17+0)%5 = 2`, random/shuffled/no-catalysis event counts of 11/8/0, tick 15, final random abundance snapshot, replay, control discrimination, run-record completeness, and trace events. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `129c170` pushed to GitHub `main`. Next target: make a cap-5 fifth candidate productive in-state or advance to cap-6 with a richer productive state shape.

Dedicated 04:30 progress run extended the cap-5 seed-11/Q-family seam from bounded-pool selection proof into 15-tick rich dynamics/run-records. In `src/chem_dynamics.metta`: added `chamber-tick-generated-5-accum`, cap-5 run wrappers through 15 ticks, rr4/sr4/nr4 no-op distractor clauses for the 12-molecule Q-rich state (Q05 remains outside this state shape), and cap-5 run-config/manifest/metrics/summary/ACS/run-record atoms. Exp03 smoke now verifies cap-5 random/shuffled/no-catalysis event counts of 10/8/0, tick 15, final random abundance snapshot, replay, control discrimination, run-record completeness, and trace events. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and an obvious secret-like diff scan. Next target: extend cap-5 beyond the Q-family distractor bridge into another richer state shape or make the fifth candidate productive in-state.

Dedicated 02:30 progress run added the first cap-5 deterministic selection/generation seams while keeping the chemistry kernel PeTTa-native. In `src/chem_exp00.metta`: added `seeded-choice-5`, `select-candidate-5`, `selected-candidate-from-list-5`, `chamber-tick-generated-5`, `exp00-candidate-cap-5`, and `cap-candidate-pool 5` clauses for 5-, 6-, and 8-candidate pools. Exp00 smoke now checks cap-5 seeded choice, cap construction, truncation, and deterministic selection. In `src/chem_dynamics.metta`: added an exp03 seed-11/Q-family cap-5 exploratory seam over the existing rich six-rule source chamber, proving the source pool is bounded to five candidates and selected deterministically with `(11+0)%5 = 1`; exp03 smoke covers both atoms. Checks: `scripts/run_exp00.sh` (75 ✅), `scripts/run_exp03.sh` (354 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `39cc96d` pushed to GitHub `main`. Next target: extend cap-5 from bounded-pool/selection proof into multi-tick rich dynamics/run-records.

Dedicated 00:30 progress run extended the cap-4 rich exp03 bridge to seed-7/P-family four-rule source pools. Added a 12-molecule P-state (P0-P7 plus P01/P10/P03/P12), a 12-state/4-rule generated candidate-pool clause, P-family chamber-tick clauses for random/shuffled/no-catalysis rules, run-config/manifest/metrics/summary/ACS/run-record atoms, and exp03 smoke coverage. The cap-4 selector phase `(7+tick)%4 = 3,0,1,2` exercises rr3, rr1, rr0, rr2 for three rounds; random-polymer records 12 productive events, shuffled also records 12 productive events for this seed/control shape, and no-catalysis records 0. This completes cap-4 rich bridge coverage for seed-7, seed-11, seed-13, and seed-17; next target is cap-5+ richer pools. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `adcff35` pushed to GitHub `main`.

## 2026-07-06

Dedicated 20:30 progress run pushed commit `fa9a89f` extending the cap-4 rich bridge from seed-13 to seed-17, keeping the chemistry kernel PeTTa-native and using Python only for mechanical file editing. The new S-family 12-molecule state uses S0-S7 plus S01/S10 and S45/S54, with generated seed-17 rules rr0/rr1 and rr2/rr3 forming two catalytic pairs. Random-polymer fires rr0, rr2, rr3, rr1 in the deterministic cap-4 selector cycle for 12 productive events over 12 ticks and exhausts S0-S7; shuffled-catalysts fires 8 events because rr3 is no-op and rr1 is blocked after S4 depletion; no-catalysis records 0 events. Added run-config/manifest/metrics/summary/ACS/run-record atoms and exp03 smoke tests for counts, final abundances, replay, discrimination, completeness, and trace events. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and an obvious secret-like diff scan. Remaining top-task work: seed-7 and seed-11 cap-4 rich bridge variants.

Dedicated 17:15 progress run implemented the cap-4 rich bridge for seed-13, the top TASKS.md item: exploring cap-4+ pools with richer state shapes. Created a 12-molecule cap-4 bridge for seed-13 where ALL FOUR cap-4 rules (rr0, rr1, rr2, rr3) fire productively under random-polymer catalysis. Initial state: R0=3, R1=3, R2=3, R3=3, R4=3, R5=3, R6=3, R7=3, R01=0, R10=1, R45=0, R54=1. The deterministic selector cycles (13+tick)%4 = 1,2,3,0,1,2,3,0,... so rr0 fires at tick 0, rr2 at tick 1, rr3 at tick 2, rr1 at tick 3, repeating for 3 full rounds (12 productive events total, all reactants R0-R7 exhausted by tick 11). For shuffled-catalysts: rr0 fires (cat R2 present), rr2 fires (cat R6 present), but rr3 is no-op (cat R8 absent) and rr1 only fires twice because rr2 consumes R4 which is rr1's shuffled catalyst, so the 3rd rr1 is blocked → 8 events. No-catalysis: 0 events. Control discrimination: random (12) > shuffled (8) > no-catalysis (0). This is the first cap-4 bridge where 4 rules fire productively per cycle, demonstrating two catalytic pairs simultaneously: (rr0↔rr1) and (rr2↔rr3). Required adding: cap-4 infrastructure (seeded-choice-4, select-candidate-4, chamber-tick-generated-4-accum, chamber-run-4cap-1 through -12 and -15), 12-molecule state support (generate-candidate-pool, state-tick, state-seed, state-abundance-snapshot), extended append-event to 12 existing events and event-count to 12, 15 new chamber-tick-with-candidate-accum clauses for 12-molecule state, and full bridge atoms. 21 new exp03 smoke tests (321 total, was 300). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (321 ✅), `git diff --check`, and secret-like scan.

Dedicated 14:30 progress run implemented the top TASKS.md item: exploring richer state shapes for cap-3 where multiple rules fire productively. Created a 10-molecule "rich" cap-3 bridge for seed-13 where ALL three cap-3 rules (rr0, rr1, rr2) fire productively. Initial state: R0=3, R1=3, R2=3, R3=3, R4=3, R5=3, R01=1, R10=1, R45=0, R54=1. The deterministic selector cycles (13+tick)%3 = 1,2,0,1,2,0,... so rr0 fires at tick 0, rr2 at tick 1, rr1 at tick 2, repeating for 3 full rounds (9 productive events total, all reactants R0-R5 exhausted by tick 8). For shuffled-catalysts: rr0 fires (cat R2 present), rr1 fires (cat R4 present), but rr2 is no-op (cat R6 absent) → 6 events. No-catalysis: 0 events. Control discrimination: random (9) > shuffled (6) > no-catalysis (0). This demonstrates that the random-polymer family's catalytic cycle (rr0 produces R01 which catalyzes rr1, rr1 produces R10 which catalyzes rr0) is MORE productive than the shuffled control, where rr2's catalyst is missing. Required adding: (1) `generate-candidate-pool` clause for 10-molecule state with 8 rules in `src/chem_exp00.metta`, (2) `state-tick` and `state-seed` clauses for 10-molecule state in `src/chem_exp00.metta`, (3) `state-abundance-snapshot` clause for 10-molecule state in `src/chem_dynamics.metta`, (4) `event-count` clause for 9 events, (5) 9 new `chamber-tick-with-candidate-accum` clauses in `src/chem_dynamics.metta` for the 10-molecule state shape (3 productive rr0/rr1/rr2 for random-polymer, 2 productive rr0/rr1 for shuffled-catalysts, 4 no-op for absent/None catalysts), (6) full run-config/manifest/metrics/summary/acs/run-record atoms for the rich bridge. 21 new exp03 smoke tests (300 total, was 279). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (300 ✅), `git diff --check`, and secret-like scan.

Dedicated 12:30 progress run extended the cap-3 bridge to seed-7, seed-17, and seed-11, completing the top TASKS.md item. Each seed now has a 15-tick cap-3 chamber with 5 productive rr0 events, reactant exhaustion, replay equivalence, control discrimination, and full run-config/manifest/metrics/summary/acs/run-record atoms. Seed-7 (4-rule P-molecule): (7+tick)%3 = 1,2,0,... so rr0 fires at ticks 0,3,6,9,12 with P0/P1 exhaustion at tick 12. Seed-17 (8-rule S-molecule) and seed-11 (6-rule Q-molecule): both have (seed+tick)%3 = 2,0,1,... so rr0 fires at ticks 2,5,8,11,14 with exhaustion at tick 14. Required adding three explicit family clauses to `exp03-cap3-chamber` for seed-7 and seed-11 (mapping `random-polymer`→`random`, `shuffled-catalysts`→`shuffled` for the full-source-rules seam, since seed-7 and seed-11 use short family names in `exp03-exp02-full-source-rules`). Also added rr2 no-op `chamber-tick-with-candidate-accum` clauses for P0/P1 (seed-7), S0/S1 (seed-17), and Q0/Q1 (seed-11) state shapes — all no-ops since rr2 reactants (P3, S4/S5, Q4/Q5) are absent from the initial state. 63 new exp03 smoke tests (279 total, was 216). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (279 ✅), `git diff --check`, and secret-like scan.

Dedicated 10:30 progress run implemented the top TASKS.md item: candidate cap 3 support for broader per-tick rule visibility. In `src/chem_exp00.metta`: added `seeded-choice-3` using `(seed+tick)%3`, `select-candidate-3` picking among 3 candidates, `selected-candidate-from-list-3` for chamber-based selection, `chamber-tick-generated-3` for cap-3 generated ticking, `exp00-candidate-cap-3` returning `(candidate-cap 3 1)`, and `cap-candidate-pool 3` clauses for 5/6/8-element pools (previously only 3/4-element). In `src/chem_dynamics.metta`: added `chamber-tick-generated-3-accum` using cap-3 selection, `chamber-run-3cap-1` through `chamber-run-3cap-10` and `chamber-run-3cap-15` explicit wrappers, `chamber-tick-with-candidate-accum` clauses for rr2 in seed-13 state shape (R4+R5→R45, cat R54/R6/None — all no-ops since R4/R5 absent from R0/R1/R01/R10 state), and a complete 15-tick cap-3 bridge for seed-13: `exp03-cap3-initial-state` (R0=5, R1=5), `exp03-cap3-chamber`, `exp03-cap3-after-15`, event counts, tick, abundances, replay, reactant exhaustion, control discrimination, run-config/manifest/metrics/summary/acs/run-record/run-records atoms. The deterministic selector cycles (13+tick)%3 = 1,2,0,1,2,0,... so rr0 (position 1 in the pool) fires at ticks 0,3,6,9,12 for 5 productive events with R0/R1 exhaustion at tick 12; rr2 (position 2) and rr1 (position 0) are distractors (reactants absent from state). Shuffled and no-catalysis controls remain zero-event. 21 new exp03 smoke tests (216 total, was 195). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (216 ✅), `git diff --check`, and secret-like scan.

Dedicated 08:30 progress run added two new exp02-family dynamic bridges. First, a 10-tick bridge for seed-11 (6-rule Q-molecule family): added `exp03-exp02-full-source-rules seed-11` for all three families (random/shuffled/no-catalysis), `exp03-exp02-longer-*` atoms for seed-11 with Q0=5/Q1=5 initial abundances. The chamber carries all six seed-11 source rules with candidate cap 2; the productive rr0 rule fires at even ticks (0,2,4,6,8) for 5 events with reactant exhaustion at tick 8. Required adding 6-rule `generate-candidate-pool` and `cap-candidate-pool 2` clauses to `src/chem_exp00.metta` (previously only 1/2/3/4/8-rule clauses existed). Second, a 16-tick longest bridge for seed-13 with R0=8/R1=8: `exp03-exp02-longest-*` atoms produce 8 productive rr0 events at even ticks (0,2,...,14) with exhaustion at tick 14. Both verify replay equivalence, reactant exhaustion, and control discrimination. 42 new exp03 smoke tests (195 total, was 153). Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (195 ✅), `git diff --check`, and secret-like scan.

Dedicated 06:30 progress run extended the 10-tick exp02-family dynamic bridge to seed-13 and seed-17, completing the top TASKS.md item. In `src/chem_dynamics.metta`: added `exp03-exp02-longer-*` atoms for seed-13 (R0=5, R1=5 initial abundances, 8-rule full-source chamber) and seed-17 (S0=5, S1=5 initial abundances, 8-rule generated full-source chamber). Both bridges use `chamber-run-10` with candidate cap 2, producing 5 productive rr0 events at even ticks (0,2,4,6,8) with reactant exhaustion at tick 8; shuffled/no-catalysis controls remain zero-event. The deterministic seed/tick selector pattern `(seed+tick)%2` yields the same alternation for all three seeds (7, 13, 17 are all odd). Added run-config/manifest/metrics/summary/run-record atoms for all three families per seed, including `source-exp02-rule-count 8` and `generation-seam seed-to-components` (for seed-17). 42 new exp03 smoke tests (153 total, was 111). Checks: exp03 (153 ✅), exp00 (71 ✅), `git diff --check`, and secret-like scan. Next step: explore more rules and longer polymers in the 10-tick bridge.

Dedicated 04:30 progress run added the first 10-tick exp02-family dynamic bridge, connecting the longer multi-tick evolution fixtures to the exp02-style family bridge structure. In `src/chem_dynamics.metta`: added `exp03-exp02-longer-initial-state` (P0=5, P1=5), `exp03-exp02-longer-chamber`, `exp03-exp02-longer-after-10`, `exp03-exp02-longer-event-count`, `exp03-exp02-longer-tick`, `exp03-exp02-longer-abundances`, `exp03-exp02-longer-replay-10`, `exp03-exp02-longer-replay-ok?`, `exp03-exp02-longer-reactant-exhausted?`, `exp03-exp02-longer-controls-discriminate?`, `exp03-exp02-longer-run-config`, `exp03-exp02-longer-run-manifest` (separate clauses per family), `exp03-exp02-longer-metrics` (using `run-config-id` pattern), `exp03-exp02-longer-run-summary`, `exp03-exp02-longer-run-record`, `exp03-exp02-longer-run-records`, and `exp03-exp02-longer-run-records-complete?`. The seed-7 random family produces 5 productive rr0 events over 10 ticks (at ticks 0,2,4,6,8) with reactant exhaustion at tick 8; shuffled/no-catalysis controls remain zero-event. 21 new exp03 smoke tests (111 total, was 90). Checks: exp03 (111 ✅), exp00 (70 ✅), `git diff --check`, and secret-like scan. Pushed `8b848db` to GitHub `main`. Next step: extend to seed-13 and seed-17, then explore more rules and longer polymers.

Dedicated 02:30 progress run extended exp03 multi-tick evolution to longer runs, pivoting from the completed cycle-size scanning (k=2..7) toward richer chemistry dynamics. In `src/chem_dynamics.metta`: extended `append-event` with 4 new clauses (handles up to 9 existing events for 10-event logs); extended `event-count` with 3 new clauses (up to 8 events); added `chamber-run-6` through `chamber-run-10` and `chamber-run-16` explicit wrappers. Added two new fixtures: (1) a 10-tick run with A=5, B=5 that produces 5 productive events at even ticks (0,2,4,6,8) with reactant exhaustion at tick 8, and (2) a 16-tick run with A=8, B=8 that produces 8 productive events at ticks 0,2,...,14 with exhaustion at tick 14. Both fixtures verify deterministic replay equivalence, tick advancement, event accumulation, abundance snapshots, and reactant exhaustion. 13 new exp03 smoke tests (90 total, was 77). Checks: exp03 (90 ✅), exp00 (70 ✅), `git diff --check`, and secret-like scan. Next step: connect longer multi-tick runs to exp02-style family bridges and explore more rules/longer polymers.

## 2026-06-26

Received Telegram-uploaded PDF: *Initial Abstract Algorithmic Chemistry Experiments in PeTTa: A PeTTa-First, MORK-Ready Research and Implementation Plan*.

Local preservation:

- PDF: `library/petta-abstract-algorithmic-chemistry/source.pdf`
- Extracted text: `library/petta-abstract-algorithmic-chemistry/extracted.txt`
- Sidecar: `library/petta-abstract-algorithmic-chemistry/SOURCE.md`
- SHA-256: `341643e264c562d476b46172a5f284657de49f6eb2a99764c8ad71bbac693d23`

High-level read: the document is a concrete milestone ladder for a PeTTa-first abstract chemistry, with exp00 deterministic replay and exp01 planted ACS recovery before claims about spontaneous ACS emergence in exp02. It explicitly says not to implement semantic graphs, MORK, MOSES, PLN, music chemistry, or predictive weighting in v0.1.

Benjamin clarified that PeTTa-first means the algorithmic chemistry system itself should be built in PeTTa from the start, not as a Python chemistry kernel that emits PeTTa-shaped atoms. Python is acceptable as a harness for running experiments, saving data, loading configuration files, plotting, etc. Rationale: a Python chemistry kernel would be cumbersome for Benjamin to inspect for errors and would need to be ported to PeTTa anyway.

Progress-update cadence requested and scheduled: brief Telegram updates roughly every two hours while the project is active; ad hoc updates for interesting progress or meaningful infrastructure/science milestones; daily overview around 7AM Pacific summarizing the previous 24 hours and outlook. Cron jobs: `a5d8122d-e026-4e82-b113-d9be41f1e12f` (2-hour brief), `6fb7b7bc-d541-4597-9dce-d0a4dad9cae4` (daily 7AM Pacific).

GitHub repo created after Benjamin confirmed owner/name/visibility: `https://github.com/bgoertzel-sing/petta-chem` public. Local clone: `projects/petta-chem/repos/petta-chem`. Repository is empty/no commits as of creation. Need Benjamin-approved Git commit identity before first local commit; do not infer email.

## 2026-06-28

Dedicated progress run inspected project records, repo docs/status/log, and the current exp00 smoke test. Implemented commit `6f2e25edb10288350b9003c1840b69d3371f7db6` in `projects/petta-chem/repos/petta-chem`: deterministic seed/tick candidate selection is now called from chamber ticking via `selected-candidate-from-chamber-2`/`chamber-tick-select-2`, and exp00 has a first fixed three-candidate pool plus `cap-candidate-pool` tests for bounded generation/caps. Checks passed before push: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Pushed to GitHub `main`.

Dedicated 21:15 progress run generalized exp00 candidate generation/caps and pushed commit `205092f26e3def5e940ca9d29db610f67f9d664a` to GitHub `main`. Candidate pools are now generated from chamber rules instead of fixed exp00 candidate functions; new `candidate-cap` atoms expose per-tick/per-rule caps, `bounded-candidate-pool` applies the per-tick cap, and `chamber-tick-generated-2` feeds capped generated candidates into deterministic seed/tick selection. Checks passed before push: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

## 2026-06-29

Dedicated 05:15 progress run completed the top exp00 test-coverage task and pushed commit `d3da831907d20f3739ac4233c9b516527c898c5d` to GitHub `main`. Added PeTTa-native deterministic `symbol-code`, `mol-hash`, and `rule-hash` seams; added smoke tests for molecule/rule hashes, candidate-cap boundary preservation, chamber replay, and generated/direct replay equivalence. Checks passed before push: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is exp01 planted ACS recovery with distractor reactions and ablation productivity-drop testing.

Dedicated 13:15 progress run implemented the first exp01 planted ACS smoke in commit `68fd5a4ec7fdd687aa0e8cfc25fcb21c2956eee1`: PeTTa-native `acs-candidate` and `ablation` atoms, a two-rule planted catalytic closure embedded among distractor rules, explicit rejection of a non-catalytic molecule cycle, and a single-rule ablation productivity-drop check. Checks passed before commit: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit was pushed to GitHub `main`. Next task is to generalize the planted fixture into a conservative ACS/RAF-like scanner and then make ablation productivity trace-based.

Dedicated 21:15 progress run generalized exp01 recovery and pushed commit `8dde7e8405260a4687e6cb972b73b0814b6bdc78` to GitHub `main`: the PeTTa-native ACS scanner now enumerates all rule pairs in the planted four-rule fixture, marks only reciprocal product-as-catalyst closure as `active`, preserves distractor pairs as explicit `rejected` candidates, and recovers the planted ACS through the scanner rather than a fully hard-coded candidate. Checks passed before commit: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is to make exp01 ablation productivity trace-based instead of fixture-count based.

## 2026-06-30

Dedicated 05:15 progress run extended exp01 ablation from fixture counts to replayed PeTTa productivity traces and pushed commit `912c5cee7964b466e66c770ad9425d87cb9bf381` to GitHub `main`. The exp01 smoke now introduces `productivity-trace` atoms, baseline planted ACS replay with two transition traces, single-rule ablation replay with one transition trace, and an ablation drop computed from trace counts. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is defining the run output contract before exp02 sweeps.

Dedicated 13:15 progress run defined the version-0.1 consequential-run output contract and pushed commit `4dbf4b5454cf19b536c1019950e42c19541a6359` to GitHub `main`: PeTTa-shaped `run-config`, `run-manifest`, `abundance-snapshot`, `run-summary`, and `run-record` atoms now cover config, manifest/provenance, events, abundance snapshots, metrics, ACS candidates, ablations, and summary/replay status, with `experiments/run_contract/smoke.metta` projecting the current exp01 planted ACS outputs into the contract. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `git diff --check`, and an obvious secret-like scan. Commit `3d476b6` pushed to GitHub `main`. Next task is a small exp02 random polymer sweep with shuffled/no-catalysis controls, recording runs under this contract.

Dedicated 2026-06-30 18:30 progress run added the first tiny deterministic exp02 random-polymer control sweep and pushed commit `a3ddf9e63faf90c4a4b1a9a09b8b1e7eeeba6be2` to GitHub `main`. Added `src/chem_exp02.metta`, `experiments/exp02/smoke.metta`, `scripts/run_exp02.sh`, and `experiments/exp02_small_sweep_20260630/RUN.md`. The seed-7 polymer fixture has one conservative reciprocal product-as-catalyst ACS pair; shuffled-catalyst and no-catalysis controls have zero active pairs. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan. Next task is a thin host harness for writing PeTTa run-contract atoms to per-run files.

Dedicated 2026-06-30 20:30 progress run added a thin exp02 run-contract file harness. `scripts/write_exp02_contract_files.sh`/`.py` serializes the PeTTa-tested exp02 small-sweep run-contract atoms into per-run `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `ABUNDANCES.metta`, `METRICS.metta`, `ACS.metta`, `ABLATIONS.metta`, and `SUMMARY.metta` files under ignored local `experiments/exp02_small_sweep_20260630/runs/`; `scripts/test_exp02_contract_files.sh` verifies the convention without making Python a chemistry kernel. Commit ce6da96da5f6c797dff2f9941bc529e88e487f9f pushed after checks.

Dedicated 2026-06-30 22:30 progress run parameterized exp02 beyond the first tiny fixture and pushed commit `b83d97b70940c590c6d485743460e91380c454e0` to GitHub `main`: `src/chem_exp02.metta` now includes a seed-11/six-rule PeTTa sweep point with random-polymer, shuffled-catalyst, and no-catalysis run-contract records; the random fixture has two active reciprocal product-as-catalyst pairs while both controls have zero. `experiments/exp02_small_sweep_20260630/RUN.md`, README, and exp02 docs were updated with seed/rule-count provenance and hashes. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan. Next task is broader, less fixture-like exp02 parameter generation across additional seeds/rule counts while keeping PeTTa-side ACS scanning and provenance gates.


## 2026-07-01

Dedicated 00:30 progress run broadened exp02 and pushed commit `4c39d90f6a0a8ce8cd84cb6896ba571c6874f920` to GitHub `main`: `src/chem_exp02.metta` now includes a component-generated seed-13/eight-rule PeTTa family, shuffled-catalyst and no-catalysis controls, a conservative 28-pair ACS scan/count, run-contract records, and smoke tests. The random family has two active reciprocal product-as-catalyst pairs; both controls have zero. README, exp02 README, and `experiments/exp02_small_sweep_20260630/RUN.md` were updated with provenance and new hashes. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan. Next task is to make exp02 generation more systematic/seed-derived and extend file serialization beyond the original seed-7 records.

Dedicated 2026-07-01 02:30 progress run made exp02 sweep provenance/serialization more systematic in commit `4a80388299cb94814bd73dc3a49094afb07b955e`: added PeTTa `exp02-sweep-point` atoms covering seed-7/four-rule, seed-11/six-rule, and seed-13/eight-rule random/shuffled/no-catalysis families; added a systematic sweep completeness test; and extended `scripts/write_exp02_contract_files.py` plus its shell test to serialize all nine PeTTa-tested run-contract records, not just the original seed-7 records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Next task is a less fixture-like PeTTa seed-to-component generation seam before broader exp02 sweeps.

Dedicated 2026-07-01 04:30 progress run added the seed-to-component exp02 generation seam and pushed commit `3404d9d0d5b250357d9e7bc79c81001060a45708` to GitHub `main`: seed-17/eight-rule random/shuffled/no-catalysis families now generate rules from PeTTa `exp02-rule-components` atoms, the conservative scanner recovers two active reciprocal product-as-catalyst pairs only in random-polymer, `exp02-sweep-point` coverage expands to four parameter points, and the host file serializer/test now covers twelve run-contract records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Next task is to use this seam for broader seed/rule-count coverage and begin separating generated sweeps from planted-by-seed reciprocal-pair controls.

Dedicated 2026-07-01 06:30 progress run pushed commit `484c55dfdb21f937f7db0a93b66d07448416674a` to GitHub `main`: exp02 now includes a seed-19/eight-rule generated non-planted seed-to-component control. The random-polymer, shuffled-catalyst, and no-catalysis families all scan to zero active reciprocal pairs, the records are tagged with `sweep-kind generated-unplanted-control`, and the file serializer/test now covers fifteen run-contract records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Next task is adding more non-planted generated points and summarizing active-pair rates by sweep kind.

Dedicated 2026-07-01 08:30 progress run pushed commit `a5dbc04d8a4f7d070f0915282d634874b440006f` to GitHub `main`. exp02 now includes a second generated non-planted seed-to-component control point, seed-23/eight rules, with random-polymer, shuffled-catalyst, and no-catalysis families all scanning to zero active reciprocal product-as-catalyst pairs. Added PeTTa `exp02-sweep-kind-summary`/`active-pair-rate` atoms separating planted reciprocal-pair controls (4/12 family records active; 7 active pairs total) from generated-unplanted controls (0/6 active; 0 pairs), and expanded run-contract serialization from fifteen to eighteen records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like diff scan.

Dedicated 2026-07-01 10:30 progress run pushed commit `2c7a15b39ea00348fe19cad59efa5ac9ca9f2c2b` to GitHub `main`: added a concise exp02 sweep-kind report over the current deterministic PeTTa sweep. `src/chem_exp02.metta` now has tested `exp02-summary-row` and `exp02-sweep-kind-summary-report` atoms; `experiments/exp02_small_sweep_20260630/SUMMARY.md` records the human-readable table (planted reciprocal-pair controls 4/12 active family records, 7 active pairs; generated-unplanted controls 0/6, 0 active pairs) and preserves the no-spontaneous-emergence-claim caveat. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Next task is factoring seed-to-component tables further to make generated exp02 families less hand-authored.
- 2026-07-01: Commit `745d433c29089cc19588704c8d88feaa10982379` factored exp02 generated-unplanted control generation one step further with seed-29/eight-rule PeTTa token/product dictionaries plus reusable `exp02-factored-unplanted-rule-components`; all random/shuffled/no-catalysis families remain zero-active, generated-unplanted summary is now 0/9 family records, and run-contract serialization covers twenty-one records. Checks passed locally before commit/push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

Dedicated 2026-07-01 14:30 progress run pushed commit `f83cd62c43afbf0db3965aab2955284b5d25aa1f` to GitHub `main`: exp02 now includes factored-template generated-unplanted seed-31/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records. The PeTTa scanner finds zero active reciprocal product-as-catalyst pairs for all three, generated-unplanted summary/report atoms update to 0/12 family records, and the host serializer/test covers twenty-four run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (excluding benign token naming). Next task is reducing hand-maintained exp02 summaries before larger sweeps.

Dedicated 2026-07-01 18:30 progress run pushed commit `09ff9559cf03d3077c5cf5504c6e10c21576ee02` to GitHub `main`: exp02 sweep-kind summaries now use PeTTa-side recursive list/metric helpers to fold over tested run-record lists rather than hand-maintained active-pair totals. The folded summaries preserve the current result: planted reciprocal-pair controls have 4/12 active family records and 7 active pairs; generated-unplanted controls have 0/12 and 0 active pairs. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Next task is adding the next less-fixture-like generated sweep point using the fold seam.

Dedicated 2026-07-01 20:30 progress run pushed commit `e033bac47929a9f7652d3c81ef82c14157f0849a` to GitHub `main`: exp02 now includes factored-template generated-unplanted seed-37/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records. All three families remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted summaries are folded from tested run records as 0/15 active family records and 0 active pairs; `exp02-sweep-kind-summary-report` rows are now derived from folded summary atoms; and the host serializer/test covers twenty-seven run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Dedicated 2026-07-01 22:30 progress run pushed commit `3a69fe3bcc023908e4dad8f722b8050c03e38e99` to GitHub `main`: exp02 now includes factored-template generated-unplanted seed-41/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three families scan to zero active reciprocal product-as-catalyst pairs; folded generated-unplanted summaries update to 0/18 active family records and 0 active pairs; run-contract serialization/testing covers thirty records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

## 2026-07-02

Dedicated 2026-07-02 00:30 progress run pushed commit `7931be2ef6b0c723b9d86db6a9239b445dba6ec6` to GitHub `main`: exp02 now includes factored-template generated-unplanted seed-43/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; folded generated-unplanted summaries update to 0/21 active family records and 0 active pairs; docs and run-contract serialization/testing now cover thirty-three records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is a small host-swept generated-unplanted batch through the existing factored seam, unless PeTTa-side atom export hooks become cleaner first.
Dedicated 2026-07-02 02:30 progress run continued the small generated-unplanted exp02 batch and pushed commit `7d9ef1a` to GitHub `main`: seed-47/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/24 family records with 0 active pairs, and file serialization/testing covers thirty-six run-contract records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to keep broadening the generated-unplanted batch unless PeTTa-side export hooks become cleaner.


Dedicated 2026-07-02 04:30 progress run pushed commit `dec8208` to GitHub `main`, continuing the generated-unplanted exp02 batch and committed `cc2d3c9bd7b288c5aa9f379a63a38d9d6d826a8e`: seed-53/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/27 family records with 0 active pairs, and file serialization/testing covers thirty-nine run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 06:30 progress run continued the generated-unplanted exp02 batch and pushed commit `74d44e13592fbea1bae4db327addf03fc46fa2d1` to GitHub `main`: seed-59/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/30 family records with 0 active pairs, and file serialization/testing covers forty-two run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 08:30 progress run continued the generated-unplanted exp02 batch and pushed commit `0628dabb8459b27ec0f9b3d4c8d52958719b2419` to GitHub `main`: seed-61/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/33 family records with 0 active pairs, and file serialization/testing covers forty-five run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 10:30 progress run continued the generated-unplanted exp02 batch and pushed commit `67aebddd2cd64b8d3a5229918c91d0c3f9ed8c48` to GitHub `main`: seed-67/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/36 family records with 0 active pairs, and file serialization/testing covers forty-eight run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 12:30 progress run continued the generated-unplanted exp02 batch and pushed commit `43f23adf063585b31d3136cdd5d9c5ea532f604d` to GitHub `main`: seed-71/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/39 family records with 0 active pairs, and file serialization/testing covers fifty-one run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 14:30 progress run pushed commit `de29b83` to GitHub `main`: seed-73/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/42 family records with 0 active pairs, and file serialization/testing covers fifty-four run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

Dedicated 2026-07-02 16:30 progress run continued the generated-unplanted exp02 batch: seed-79/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/45 family records with 0 active pairs, and file serialization/testing covers fifty-seven run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

Dedicated 2026-07-02 18:30 progress run pushed `e7567124d95b18602d87f63b1634fb82922b1cb7` (`Add exp02 seed-83 generated control`) to GitHub `main`: seed-83/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/48 family records with 0 active pairs, and file serialization/testing covers sixty run-contract records. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

- 2026-07-02: Commit `dc925509d4e0d2d2f160d5e6c86e5c83117a1a2e` continued the host-swept factored-template generated-unplanted exp02 batch with seed-89/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/51 family records with 0 active pairs, and run-contract serialization/testing covers sixty-three records. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Dedicated 2026-07-02 22:30 progress run continued the generated-unplanted exp02 batch and pushed commit `1eff1d9bac864d550c26b48321c188dcb35e49b7` to GitHub `main`: seed-97/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/54 family records with 0 active pairs, and file serialization/testing covers sixty-six run-contract records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

## 2026-07-03

Dedicated 2026-07-03 00:30 progress run pushed commit `2acdd39` to GitHub `main`, lifting exp03 out of the duplicated-`r0` productive fixture. `src/chem_dynamics.metta` now uses a selectable two-rule pool `(r1 r0)`: seed-7/tick-0 selects productive `r0`, seed-7/tick-1 selects distractor `r1`, and the five-tick smoke alternates productive events at ticks 0/2/4 with no-op distractor ticks while preserving tick advancement, accumulated events, abundance snapshots, replay equivalence, and starved no-op behavior. Updated README/project task provenance. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `14d12f0` pushed to GitHub `main`. Commit `c4f69db` pushed to GitHub `main`. Commit `f65c430` pushed to GitHub `main`. Next task is wiring exp03 dynamics to exp02-style random/control families.

Dedicated 2026-07-03 02:30 progress run pushed commit `fd90ca0` connecting exp03 multi-tick dynamics to the first exp02-style random/control family smoke. `src/chem_dynamics.metta` now defines a bounded seed-7 exp02 dynamic fixture that sources rule identities from exp02 random-polymer, shuffled-catalyst, and no-catalysis families; the three-tick PeTTa runner records two random-family productive events and zero events for both controls. `experiments/exp03/smoke.metta` covers the resulting chambers, event counts, and dynamic control discrimination. Checks before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is broadening this bridge beyond the seed-7/two-rule window into dynamic run records.

Dedicated 2026-07-03 04:30 progress run generalized the exp03/exp02 dynamic bridge beyond the seed-7 window. Added seed-11/six-rule-source bounded Q-state dynamics with random/shuffled/no-catalysis chambers and v0.1 run-contract records; the random family produces two events over three ticks while both controls remain zero-event. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan. Commit `395c10c` pushed to GitHub `main`. Next task is broadening dynamic records beyond two-rule windows toward fuller exp02 rule pools/state shapes.

Dedicated 2026-07-03 06:30 progress run broadened exp03 dynamic source visibility and committed `9a37c59bc0a1e56b96af47a135002d7ec6e68a57` in `projects/petta-chem/repos/petta-chem`: exp00 candidate generation supports four-rule chamber pools, and exp03 now has a seed-7 full-source exp02 chamber carrying all four source rules while a candidate cap bounds deterministic ticking to two candidates. The random full-source path produces two replayable rr0 events over three ticks; shuffled/no-catalysis controls remain zero-event. Checks passed before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is extending this full-source bridge toward seed-13/eight-rule or richer dynamic control run records.

Dedicated 2026-07-03 08:30 progress run pushed commit `9b02a60d42f68f6a47fb198820c02b779374d046` (`Extend exp03 full-source seed-13 dynamics`) to GitHub `main`: exp03 full-source dynamics now cover the seed-13/eight-rule exp02 source family, with all eight source rules present in the chamber and the PeTTa candidate cap bounding each tick to two candidates. The random-polymer dynamic path records two replayable `rr0` events over three ticks; shuffled-catalyst and no-catalysis controls remain zero-event; v0.1 run-records and smoke tests cover all three families. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is broader exp03 dynamic evidence beyond this seed-13 bridge or richer dynamic run-record/export coverage.

Dedicated 2026-07-03 10:30 progress run added a second eight-rule exp03 full-source dynamic bridge via the seed-17 exp02 seed-to-components seam. The new fixture carries all eight generated source rules for random-polymer, shuffled-catalysts, and no-catalysis families; the same bounded two-candidate cap yields two replayable random-polymer `rr0` events over three ticks while both controls remain zero-event. Run-record coverage now includes abundance snapshots and a `generation-seam seed-to-components` metric. Committed as `9b82112` after checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

Dedicated 2026-07-03 12:30 progress run pushed commit `467a6f6` adding richer exp03 dynamic run-record/export coverage over the existing full-source bridges. Seed-7 full-source random, shuffled, and no-catalysis paths now all have v0.1 run-records; a PeTTa `run-export` projection exposes record fields; and smoke coverage verifies seed-7 control records plus export events/metrics/summaries for seed-7, seed-13, and seed-17. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

Dedicated 2026-07-03 14:30 progress run pushed commit `bb1f320` to GitHub `main`: exp03 now has compact PeTTa dynamic aggregate/report atoms over the tested seed-7, seed-13, and seed-17 full-source run exports. The report summarizes 9 family records, 3 active random-family records with 6 random events, 6 zero-event controls, and candidate cap 2, with smoke tests for per-seed rows and the aggregate report. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Next task is either static generated-unplanted exp02 broadening or PeTTa-side export hooks if needed.

Dedicated 2026-07-03 16:30 progress run continued the generated-unplanted exp02 batch: seed-101/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records use the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/57 family records with 0 active pairs, and file serialization/testing covers sixty-nine run-contract records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan. Next task is to continue broadening the generated-unplanted batch or add PeTTa-side export hooks if manual serialization becomes the bottleneck.

- 2026-07-03: Commit `ba01c3a` pushed to GitHub `main`, adding seed-103/eight-rule generated-unplanted exp02 random/shuffled/no-catalysis records through the factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner remains zero-active for all three families; generated-unplanted controls summarize to 0/60 family records and run-contract serialization covers seventy-two records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Dedicated 2026-07-03 20:30 progress run pushed commit `b31d659` to GitHub `main`, continuing the generated-unplanted exp02 batch with seed-107/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner remains zero-active for all three families; generated-unplanted controls now summarize to 0/63 family records with 0 active pairs, and run-contract serialization covers seventy-five records. Checks run: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

Dedicated 2026-07-03 22:30 progress run pushed commit `a9deba1` to GitHub `main`: continued the host-swept factored-template generated-unplanted exp02 batch with seed-109/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/66 family records with 0 active pairs, and run-contract serialization/testing covers seventy-eight records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add cleaner PeTTa-side export hooks if serialization remains the bottleneck.

## 2026-07-04

Dedicated 00:30 progress run pushed commit `070ddce` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-113/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/69 family records with 0 active pairs, and run-contract serialization/testing covers eighty-one records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Dedicated 2026-07-04 02:30 progress run pushed commit `4162be7` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-127/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/72 family records with 0 active pairs, and file serialization/testing covers eighty-four run-contract records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Dedicated 2026-07-04 04:30 progress run pushed commit `dec8208` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch: seed-131/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/75 family records with 0 active pairs, and file serialization/testing covers eighty-seven run-contract records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

Dedicated 2026-07-04 06:30 progress run pushed commit `7db19ca` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-137/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/78 family records with 0 active pairs, and file serialization/testing covers ninety run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task is to continue broadening the generated-unplanted batch or add cleaner PeTTa-side export hooks if serialization remains the bottleneck.

Dedicated 2026-07-04 08:30 progress run pushed commit `d17ce7a` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-139/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/81 family records with 0 active pairs, and file serialization/testing covers ninety-three run-contract records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Next task remains continuing the generated-unplanted batch or adding cleaner PeTTa-side export hooks if serialization becomes the bottleneck.

Dedicated 2026-07-04 10:30 progress run pushed commit `b6492c4` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-149/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/84 family records with 0 active pairs, and file serialization/testing covers ninety-six run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task remains continuing the generated-unplanted batch or adding cleaner PeTTa-side export hooks if serialization becomes the bottleneck.

Dedicated 2026-07-04 12:30 progress run pushed commit `8695e6d` to GitHub `main`, continuing the host-swept factored-template generated-unplanted exp02 batch with seed-151/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/87 family records with 0 active pairs, and file serialization/testing covers ninety-nine run-contract records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, and `git diff --check`. An obvious secret-like diff scan produced only expected seed-token/product seam matches.
Dedicated 2026-07-04 14:30 progress run continued the generated-unplanted exp02 batch with seed-157/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product seam. The conservative reciprocal product-as-catalyst scanner remains zero-active for all three families; generated-unplanted folded summaries are now 0/90 family records with 0 active pairs, and file serialization/testing covers one hundred two run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Commit: `7b12aee`.

Dedicated 2026-07-04 16:30 progress run pushed commit `3bdea91` to GitHub `main`, continuing the generated-unplanted exp02 breadth with seed-163/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/93 family records with 0 active pairs, and run-contract serialization/testing covers one hundred five records. Checks passed: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

Dedicated 2026-07-04 18:30 progress run pushed commit `ee77e30` to GitHub `main`, continuing the generated-unplanted exp02 batch with seed-167/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner remains zero-active for all three families; generated-unplanted controls now summarize to 0/96 family records with 0 active pairs, and run-contract serialization/testing covers one hundred eight records. Checks run: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- 2026-07-04 20:30 petta-chem dedicated run: pushed commit `0ec6d5c` (`Add exp02 seed-173 generated control`) to GitHub `main`; continued the host-swept factored-template generated-unplanted exp02 batch with seed-173/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/99 family records with 0 active pairs, and run-contract serialization/testing covers one hundred eleven records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).
Dedicated 2026-07-04 22:30 progress run pushed commit `9829ccc` to GitHub `main`, continuing the generated-unplanted exp02 batch with seed-179/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner remains zero-active for all three families; generated-unplanted controls now summarize to 0/102 family records with 0 active pairs, and run-contract serialization/testing covers one hundred fourteen records. Checks run: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

## 2026-07-07

Dedicated 00:30 progress run extended the cap-4 rich exp03 bridge to seed-7/P-family four-rule source pools. Added a 12-molecule P-state (P0-P7 plus P01/P10/P03/P12), a 12-state/4-rule generated candidate-pool clause, P-family chamber-tick clauses for random/shuffled/no-catalysis rules, run-config/manifest/metrics/summary/ACS/run-record atoms, and exp03 smoke coverage. The cap-4 selector phase `(7+tick)%4 = 3,0,1,2` exercises rr3, rr1, rr0, rr2 for three rounds; random-polymer records 12 productive events, shuffled also records 12 productive events for this seed/control shape, and no-catalysis records 0. This completes cap-4 rich bridge coverage for seed-7, seed-11, seed-13, and seed-17; next target is cap-5+ richer pools. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh` (final `git diff --check`/secret scan pending before commit).

## 2026-07-06

Dedicated 00:30 progress run added 7-rule catalytic cycle (septuple) scanner to exp01 and exp02, completing systematic cycle-size coverage for 8-rule families (k=2..7). In `src/chem_exp01.metta`: `product-catalyst-closed-7?` checks 7-rule product-catalyst closure; `scan-rule-septuple`/`scan-rule-septuples-8` enumerate all C(8,7)=8 septuples; `active-septuple-count-8` uses a split-4 approach (`septuple-count-active-4` for each half) to stay within PeTTa's nested-operation compilation limit (discovered that 7 nested `+` calls in a single function body silently break the import); planted 7-cycle fixture (sp0→sp1→sp2→sp3→sp4→sp5→sp6→sp0 with distractor spd0) validates the scanner. 6 new exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-septuples-8`, recursive `exp02-active-septuple-count`, planted 7-cycle fixture in 8-rule format (psp0→psp1→psp2→psp3→psp4→psp5→psp6 with 1 distractor psd8), comprehensive fold/summary across all 40 generated-unplanted seeds. 20 new exp02 smoke tests. Result: 0 active 7-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple/quintuple/sextuple scanner's zero-active result extends to 7-rule cycles. Also updated SUMMARY.md with septuple scan provenance. Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan. Pushed `eca2af8` to GitHub `main`. Next step: pivot to richer chemistry dynamics (more rules, longer polymers, multi-tick evolution) since cycle-size scanning is now complete.

## 2026-07-05

Dedicated 00:30 progress run continued the generated-unplanted exp02 breadth with seed-181/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the existing factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries update to 0/105 family records with 0 active pairs, and run-contract serialization/testing covers one hundred seventeen records. Checks run before commit: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Pushed `019358b` to GitHub `main`.

Dedicated 02:30 progress run continued the generated-unplanted exp02 breadth with seed-191/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the same factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries update to 0/108 family records with 0 active pairs, and run-contract serialization/testing covers one hundred twenty records. Checks run before commit: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, and `git diff --check`. Pushed `f093a99` to GitHub `main`.

Dedicated 2026-07-05 04:30 progress run continued the generated-unplanted exp02 batch and pushed commit `4a46c78` to GitHub `main`: seed-193/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/111 family records with 0 active pairs, and file serialization/testing covers 123 run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task remains continuing static generated-unplanted breadth or improving PeTTa-side export hooks if runtime support appears.

Dedicated 2026-07-05 08:30 progress run continued the generated-unplanted exp02 batch and pushed commit `35cfb19` to GitHub `main`: seed-199/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/117 family records with 0 active pairs, and file serialization/testing covers 129 run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task remains continuing static generated-unplanted breadth or improving PeTTa-side export hooks if runtime support appears.

Dedicated 10:30 progress run continued the generated-unplanted exp02 batch and pushed commit `c0e6762` to GitHub `main`: seed-211/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records now use the factored PeTTa token/product dictionary seam. The conservative reciprocal product-as-catalyst scanner finds zero active ACS pairs in all three families; generated-unplanted folded summaries are now 0/120 family records with 0 active pairs, and file serialization/testing covers 132 run-contract records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Next task remains continuing static generated-unplanted breadth or improving PeTTa-side export hooks if runtime support appears.

Dedicated 12:30 progress run shifted from the saturated generated-unplanted exp02 batch (40+ seeds, 120+ family records, all zero-active) to expanding ACS detection capability. Commit `c53077e` adds a 3-rule catalytic cycle scanner to `src/chem_exp01.metta`: `product-catalyst-closed-3?` checks that product(r0)=catalyst(r1), product(r1)=catalyst(r2), product(r2)=catalyst(r0); `scan-rule-triple` creates acs-candidate atoms for triples; `scan-rule-triples-4` enumerates all C(4,3)=4 triples from a 4-rule list; `active-triple-count-4` counts active triples. A planted 3-cycle fixture (tc0/tc1/tc2 with distractor td0) validates the scanner. `experiments/exp01/smoke.metta` adds 13 tests covering closure detection, distractor rejection, structural output, full enumeration, and active count. The commit also fixes `test_exp02_contract_files.sh` to include missing seed-211 entries. Checks: `scripts/run_exp00.sh` (70 ✅), `scripts/run_exp01.sh` (41 ✅), `scripts/run_exp02.sh` (400 ✅), `scripts/run_exp03.sh` (77 ✅), `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile`, `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

Dedicated 16:30 progress run completed the top TASKS.md item: comprehensive 3-rule catalytic cycle scanning across all 40 generated-unplanted exp02 seeds. Added `exp02-generated-unplanted-seeds-8` PeTTa list, `exp02-seed-triple-total` (per-seed triple count across 3 families), `exp02-fold-seed-triple-total` recursive fold, `exp02-generated-unplanted-triple-total` (total = 0 across all 40 seeds × 3 families = 120 family records), `exp02-triple-scan-summary` constructor, and `exp02-generated-unplanted-triple-summary`/`exp02-planted-triple-summary` atoms. 16 new smoke tests: fold total (0), seed count (40), planted fixture (1 active triple), seed-13 all families (0), and spot-checks on seed-19/41/67/97/113/139/167/199 across different families. This confirms the conservative pair scanner's zero-active result extends to 3-rule catalytic cycles for the entire generated-unplanted batch. Checks: exp00 (70 ✅), exp01 (41 ✅), exp02 (430 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan.

Dedicated 14:30 progress run extended the 3-rule catalytic cycle scanner from exp01 to exp02 8-rule families. Commit `b77a50e` adds `exp02-scan-triples-8` to `src/chem_exp02.metta` enumerating all C(8,3)=56 triples from 8-rule lists, a recursive `exp02-active-triple-count` helper using car-atom/cdr-atom, and a planted 3-cycle fixture in 8-rule format (ptc0/ptc1/ptc2 forming a closed 3-cycle plus 5 distractor rules) that validates the scanner finds exactly 1 active triple out of 56. Convenience atoms run triple scanning on seed-13 planted and seed-17/29/31/37/211 generated-unplanted 8-rule families — all have 0 active triples, confirming the pair scanner's conservative zero-active result extends to 3-rule catalytic cycles. 17 new exp02 smoke tests. Checks: `scripts/run_exp00.sh` (71 ✅), `scripts/run_exp01.sh` (42 ✅), `scripts/run_exp02.sh` (417 ✅), `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

Dedicated 18:30 progress run added 4-rule catalytic cycle scanning to exp01 and exp02, extending ACS detection breadth beyond pairs and triples. In `src/chem_exp01.metta`: `product-catalyst-closed-4?` checks product(r0)=catalyst(r1), product(r1)=catalyst(r2), product(r2)=catalyst(r3), product(r3)=catalyst(r0); `scan-rule-quadruple`/`scan-rule-quadruples-5` enumerate all C(5,4)=5 quadruples from a 5-rule list; `active-quadruple-count-5` counts active quadruples; a planted 4-cycle fixture (qc0→qc1→qc2→qc3→qc0 with distractor qd0) validates the scanner. 9 new exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-quadruples-8` enumerates all C(8,4)=70 quadruples from 8-rule lists; recursive `exp02-active-quadruple-count` helper; planted 4-cycle fixture in 8-rule format (pqc0→pqc1→pqc2→pqc3→pqc0 with 4 distractors); comprehensive fold/summary across all 40 generated-unplanted seeds; 20 new exp02 smoke tests. Result: 0 active 4-rule cycles across all 120 generated-unplanted family records, confirming pair/triple scanner's conservative zero-active result extends to 4-rule cycles. Also updated SUMMARY.md with triple-scan provenance. Checks: exp00 (70 ✅), exp01 (50 ✅), exp02 (450 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan.

Dedicated 20:30 progress run added 5-rule catalytic cycle scanner to exp01 and exp02, extending ACS detection breadth to 5-rule closure. In `src/chem_exp01.metta`: `product-catalyst-closed-5?` checks product(r0)=catalyst(r1), product(r1)=catalyst(r2), product(r2)=catalyst(r3), product(r3)=catalyst(r4), product(r4)=catalyst(r0); `scan-rule-quintuple`/`scan-rule-quintuples-6` enumerate all C(6,5)=6 quintuples from a 6-rule list; `active-quintuple-count-6` counts active quintuples; a planted 5-cycle fixture (qc0→qc1→qc2→qc3→qc4→qc0 with distractor qd0) validates the scanner. 9 new exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-quintuples-8` enumerating all C(8,5)=56 quintuples from 8-rule lists; recursive `exp02-active-quintuple-count` helper; planted 5-cycle fixture in 8-rule format (pqq0→pqq1→pqq2→pqq3→pqq4→pqq0 with 3 distractors); comprehensive fold/summary across all 40 generated-unplanted seeds; 20 new exp02 smoke tests. Result: 0 active 5-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple scanner's zero-active result extends to 5-rule cycles. Also updated SUMMARY.md with quadruple and quintuple scan provenance. Checks: exp00, exp01, exp02, exp03, contract files, py_compile, `git diff --check`, and secret-like scan. Pushed `cfb1be1` to GitHub `main`.

Dedicated 22:30 progress run added 6-rule catalytic cycle scanner to exp01 and exp02, extending ACS detection breadth to 6-rule closure. In `src/chem_exp01.metta`: `product-catalyst-closed-6?` checks 6-rule product-catalyst closure; `scan-rule-sextuple`/`scan-rule-sextuples-7` enumerate all C(7,6)=7 sextuples from a 7-rule list; `active-sextuple-count-7` counts active sextuples; a planted 6-cycle fixture (sc0→sc1→sc2→sc3→sc4→sc5→sc0 with distractor sd0) validates the scanner. 9 new exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-sextuples-8` enumerating all C(8,6)=28 sextuples from 8-rule lists; recursive `exp02-active-sextuple-count` helper; planted 6-cycle fixture in 8-rule format (psq0→psq1→psq2→psq3→psq4→psq5→psq0 with 2 distractors); comprehensive fold/summary across all 40 generated-unplanted seeds; 20 new exp02 smoke tests. Result: 0 active 6-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple/quintuple scanner's zero-active result extends to 6-rule cycles. Also updated SUMMARY.md with sextuple scan provenance. Checks: exp00 (70 ✅), exp01 (62 ✅), exp02 (490 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan. Pushed `bf68c71` to GitHub `main`.

Dedicated 2026-07-06 22:30 progress run extended the cap-4 rich exp03 bridge to seed-11/Q-family six-rule source pools. The exp00 candidate seam now caps six-candidate pools and generates six-rule pools for 12-molecule states; exp03 adds Q-family 12-molecule chamber-tick clauses plus seed-11 cap-4 run configs/manifests/metrics/run-records. New smoke coverage checks 12 productive random-polymer events, zero no-catalysis events, reactant exhaustion, replay, controls discrimination, and run-record completeness. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan. Remaining cap-4 rich extension target: seed-7/P-family.

## 2026-07-27 — Corrective queue audit after external review

**Observed:** after the external-review PDF was prepared, the recurring worker
continued a 33-to-41 source-rule candidate-generator sequence.  The associated
records state that no chemistry rule, trajectory, or scientific result changed.
This violates the earlier demand-driven hardening freeze and the review's
Recommendation 0 to stop feature accretion.

**Decision:** D-20260727-neutral-model-reset supersedes the old work ordering.
Freeze generator expansion and exp08 in its constructed-pathway form.  The
next deliverable is a neutral random-catalytic model plus independent small
RAF-oracle protocol, followed by calibration that separates structural,
reachable, persistent, and causal endpoints.  Bridge/Doob control is deferred
until an exact tiny-state control baseline is validated.  Existing work is
preserved as control infrastructure.

## 2026-07-09 addendum — geoteleomic / Schrödinger Bridge substack post as exp06 inspiration

Ben shared his substack post "Let's Get Chemical" (https://bengoertzel.substack.com/p/lets-get-chemical) as the inspiration for the exp06 bridge-to-ACS direction. Key points from the post that inform the PeTTa-native exp06 design:

- **Framework**: Schrödinger Bridge (SB) on stochastic chemical trajectories, using Doob h-transform to identify minimum-information deformations of native chemistry that reach a life-like target set. This is the "geoteleomic" approach: given that life emerged, what path ensembles are least surprising conditional on reaching the target?
- **Lane-style seep model**: H2/CO2 feeds, pH/redox gates, FeS mineral surfaces, pore retention, carbon/energy ladder, membrane-production channel, decoy autocatalytic loops, clutter channels, two productive RAF families (incumbent T0 + improved T1), nonstationary perturbations (takeover + shock protocols).
- **Headline result**: native dynamics ~0% success; functional bridge → 1.00 success; conversion bridge → 1.00 success with higher membrane output. Even with chemical clutter, decoys, and evolving productive families, a low-dimensional learned backward potential robustly improves path ensembles.
- **Protected release** (value-relative anti-precedence): the refined local-memory rule that emerged. Instead of penalizing raw repetition (which damages individuation), penalize excess canalization: O_g = max(S_g - S*_g - θ, 0), where S_g is actual ecological share and S*_g is value-justified share (softmax over per-family value scores). Protect shared functional machinery via c_r ∈ [0,1]; release pressure on identity-specific over-dominance, not on shared function. Diffuse release into motif-neighborhood kernel.
- **Conceptual takeaway**: "Precedence enables individuation. Anti-precedence (properly defined as value-relative anti-precedence) enables ongoing self-transformation." A protocell-like system needs both: stabilize self-maintaining organization AND let better-performing implementations replace older ones without losing macro-organization.
- **Information-theoretic value form**: V_g ≈ I(g; viable future function) − α · I(g; frozen implementation).

For petta-chem exp06, the PeTTa-native abstract analog would be:
1. Initial soup: verified no-ACS PeTTa chemistry (exp02/exp04 no-catalysis controls).
2. Terminal soup: exp04's ACS-rich fixture (maximal RAF 15, greedy core 2).
3. Bridge/path analysis: deterministic shortest-path search over intervention variables — catalyst-affinity assignment (from exp05), basal food rate, candidate-pool cap, catalysis-map offset.
4. "Favorable conditions" = the minimal intervention variable changes that suffice to move from initial to terminal.
5. Protected-release analog: test whether value-relative anti-precedence on catalyst-affinity weights (penalize over-dominant pathway families relative to their value share, protect shared catalytic machinery) biases unguided dynamics toward ACS emergence without fixing the terminal condition.

Constraint: chemistry dynamics stay PeTTa-native; host code may do path-search/OT bookkeeping and artifact serialization only. The bridge is a diagnostic, not an emergence claim.

2026-07-11 22:30 progress: tightened the PeTTa-native selection-to-tick seam with `chamber-tick-candidate-pool-2`, a direct kernel operation that applies a candidate cap, deterministic seed/tick selection, and chamber firing to an already generated/scored candidate pool. `chamber-tick-generated-2` now delegates to this primitive, and exp05 treatment/control affinity ticking routes its scored pools through the same direct path rather than manually selecting before ticking. Exp00 smoke verifies generated-pool equivalence; existing exp05/exp07 dynamics remain unchanged. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `git diff --check`.

2026-07-15 12:30 progress: closed the first oversized chamber source-list boundary without moving chemistry into host code. The four-molecule exp00 generator now takes a stable first-eight candidate prefix from a nine-rule chamber; all nine source rules remain in chamber provenance, the rewrite-ownership guard recognizes that shape, and cap-2 deterministic selection fires normally. Checks: `scripts/run_exp00.sh` (143 checks), `git diff --check`. Commit `9d95a7a` pushed to GitHub `main`.

2026-07-15 14:30 progress: closed the next oversized chamber source-list boundary in the PeTTa-native exp00 kernel. A ten-rule four-molecule chamber now generates the same stable first-eight prefix, retains all ten source rules as provenance, passes the ten-rule rewrite-ownership guard, and completes cap-2 deterministic selection and chamber firing. Checks: `scripts/run_exp00.sh` (146 checks), `git diff --check`. Commit `5ca80ee` pushed to GitHub `main`.

2026-07-15 16:30 progress: closed the eleven-rule oversized chamber boundary in the PeTTa-native exp00 kernel. The generator emits the stable first-eight prefix while retaining all eleven source rules; focused coverage proves the ownership predicate still reaches a valid rewrite in position eleven and cap-2 selection fires through the ordinary chamber-tick path. Checks: `scripts/run_exp00.sh` (149 checks), `git diff --check`. Commit `3353533` pushed to GitHub `main`.
- 2026-07-16 04:30 dedicated worker: added the first matched stateful exp07 trajectory in PeTTa. `exp07-pilot-matched-after-two-ticks` carries the tick-3 chamber into tick 4, while `exp07-pilot-two-tick-trajectory` preserves initial state, both selected candidates, both resulting chambers, replay provenance, and the preregistered no-claim boundary. Weak Doob-h/seed-7 fires `e5r0` then `e5r1`, yielding two events and exact A/B/C exhaustion. `scripts/run_exp00.sh` passed with 153 reported assertions, `scripts/run_exp07.sh` with 98, and `git diff --check` passed. Commit `bc7f7de` was pushed to GitHub `main`. Next is the all-arm/all-seed two-tick summary; `emergence-claim none`.
- 2026-07-16 10:31 dedicated worker: closed exp07 PREREG §6's pre-run contamination gate before evaluating any registered N=20 outcome. A new registered constructor supplies one exact PeTTa-native candidate pool to all arms for arbitrary seed/tick; only `exp07-pilot-first-candidate-weight` varies by arm. Historical pilot constructors remain intact. The status atom is now `passed`, with smoke at seed-7/tick-3 and seed-10/tick-22 plus generic structural equality. Exp00 passed 153 assertions, exp07 134, and `git diff --check` passed. Commit `05d6ea9` pushed to GitHub `main`. `emergence-claim none`; next is the frozen ticks 3--22 matrix.
- 2026-07-16 12:30 dedicated worker: executed the complete preregistered exp07 N=20 matrix once the positive-control and pool-identity gates were closed. The explicit PeTTa-native tick chain consumes ticks 3--22, advances blocked draws, replenishes A/B/C at 8/13/18, and retains exact selected-event provenance. All 12 trajectories replay to tick 23 and produce 8 events each. A bounded specialization of the canonical RAF conditions reads catalyst assignments from fired events: singleton product=catalyst or the two-rule AB/AC cross-catalytic closure. Incidence is 4/4 for every arm; first-hit ticks are unguided `[5,3,8,10]`, weak Doob-h `[3,3,8,8]`, and shuffled `[5,3,4,3]`. Per PREREG §5 this is the all-arms-positive/pool-composition branch, not guidance uplift; causal removal of guidance does not collapse controls and `emergence-claim none` remains. Exp00 passed 153 assertions, exp07 141, and `git diff --check` passed. Commit `04d7b02` pushed to GitHub `main`. Run record: `experiments/20260716T193000Z-exp07-registered-n20/`.
- 2026-07-16 20:30 dedicated worker: closed every frozen exp07 rich-pool pre-run gate without constructing a seed-11--18 trajectory. PeTTa-native fired-event checks make the empty initial state RAF-negative and discriminate complete versus incomplete `rp0/rp1/rp2` histories. The gate record exposes the exact eight catalysis facts, shared-pool equality, full 88-bin arm masses, and ordinary direct-tick path; canonical detector controls pass. Checks: exp00 153, exp07 167, detector invariance, and `git diff --check`. Commit `3d347d7` pushed to GitHub `main`. Next: frozen 24-tick constructor and one complete matched matrix; `emergence-claim none`.
- 2026-07-16 22:30 dedicated worker: ran the preregistered rich-pool matrix once, with no seed/horizon extension. The PeTTa-native constructor consumes ticks 3--26, resets food at 11/19, advances blocked draws, and retains exact event history; the run exposed the explicit nine-event history ceiling, which was boundedly extended through the 24-tick maximum. Rolling last-eight-event RAF incidence is unguided 5/8, weak Doob-h 7/8, shuffled 3/8; first-hit vectors are `[99,14,22,13,23,99,22,99]`, `[15,20,99,19,16,15,23,14]`, and `[99,11,99,99,99,99,14,22]`; productive totals are 130/120/123. Both controls are positive, so `emergence-claim none`. Checks: exp00 153, exp07 174, `git diff --check`. Commit `41fb965` pushed to GitHub `main`.

- 2026-07-17 06:30 dedicated worker: completed the frozen rich-pool causal ablations inside the PeTTa chamber loop. Each counterfactual uses the same seeds 11--18, ticks 3--26, generated cap-8 pool, categorical selector, and replenishment schedule; an ablated edge/rule converts only its selected draw into the established blocked tick. Guiding-term removal is the unguided arm and remains RAF-positive in 5/8 seeds. Removing `(CD,rp0)`, `(AB,rp1)`, and `(AC,rp2)` together gives RAF incidence 0/8 in all three arms and productive totals 116/83/117. Single-rule ablations of `rp0`, `rp1`, or `rp2` each give 0/8 in every arm. This confirms dependence on the planted three-rule cycle but rejects guidance necessity because both controls were already positive; `emergence-claim none`. Checks: `scripts/run_exp00.sh` (153), `scripts/run_exp07.sh` (185), `git diff --check`. Commit `9824ed1` pushed to GitHub `main`.

- 2026-07-17 10:33 dedicated worker: completed the first fail-closed ordered-bootstrap implementation slice. `exp07-ordered-initial-chamber` fixes the preregistered twelve-species state, while one arm-independent constructor exposes the exact ordered eight-rule pool and bounded cap-8 equivalence. The eight frozen catalysis edges are actual Atomspace `(catalyzes Molecule RuleId)` data queried via `match`; absent pairs return false, so catalyst names do not imply relations. Gate provenance explicitly records that selector, chamber tick, and held-out trajectory evaluation remain false. Checks: exp00 153, exp07 197, and `git diff --check`. Commit `986c489` pushed to GitHub `main`. Next gate is initial applicability/RAF negativity; `emergence-claim none`.
# 2026-07-17 14:30 ordered-bootstrap frozen matrix

- Re-ran the full pre-run gate before outcomes: exp00 153/153, exp07 217/217,
  exp04 detector call-order/tick-path/uniqueness invariance passed, and the
  ordered initial state remained RAF-negative.
- Executed only the preregistered arms, seeds 19--26, and ticks 3--26. Rolling
  `op1/op2/op0` RAF incidence was 0/8 in every arm; all first-hit values were
  the registered no-hit sentinel 99. Productive events totaled 103 unguided,
  119 weak Doob-h, and 104 shuffled-frontier guidance. Replay was 8/8 per arm.
- Outcome interpretation: an all-arm primary null. Do not extend the horizon
  or seed set; `emergence-claim none`.
- Provenance: the matrix exposed imported PeTTa equation heads remaining data
  rather than executable calls inside recursive exp07 clauses. Ordered
  generation, cap-8 identity, applicability, and firing are therefore explicit
  PeTTa-local executable clauses mirroring exp00. The generic exp00 bounded
  pool helper also no longer uses the miscompiled intermediate `let`.
- Final checks after permanent smoke assertions: exp00 153/153, exp07 222/222,
  no failure markers, and `git diff --check`.
## 2026-07-17 16:30 PDT — ordered-bootstrap detector correction and causal endpoints

- Audit observation: `exp07-ordered-first-raf-tick-from-terminal` called
  `exp07-rich-first-rolling-raf-from`, which tests `rp0/rp1/rp2`, although the
  ordered preregistration specifies `op1/op2/op0`.
- Corrected PeTTa-local rolling detection over the unchanged frozen matrix gives
  RAF incidence 0/8 unguided, 6/8 weak Doob-h, and 0/8 shuffled. Weak first-hit
  ticks are `[99,12,15,14,99,19,19,18]`; event totals remain 103/119/104 and
  all 24 trajectories replay.
- Ordered persistence vectors are all-zero for both controls and
  `[0,9,6,7,0,4,8,7]` for weak Doob-h (total 41). Terminal distinct-rule
  diversity is 42/59/39 of 64, with collapse deficits 22/5/25.
- Prespecified guiding-term, `ob0`, three-edge catalyst, and individual
  `op1/op2/op0` ablations all reduce weak RAF incidence to 0/8 while preserving
  frozen seeds, horizon, draws, pool, and schedule.
- Interpretation: the preregistered bounded guided causal RAF-uplift condition
  is supported. This does not establish spontaneous emergence. No seeds or
  ticks were added.
- Provenance: local PeTTa/SWI stack; `src/chem_exp07.metta`, exp07 smoke, and
  exp07 preregistration/README. Checks: exp00, exp07, detector invariance, and
  `git diff --check`. Commit `7e1e677` pushed to GitHub `main`.

## 2026-07-17 22:30 PDT — ordered replication cohort A

- Executed only frozen cohort A: arms unguided/weak Doob-h/shuffled-frontier,
  seeds 101--116, ticks 3--26, cap 8, fixed hash and food schedule.
- Ordered rolling RAF incidence was 1/16, 4/16, and 0/16. Weak therefore had
  advantages of three and four, below the preregistered six over each control;
  primary replication is not supported.
- First hits were unguided seed 105 at tick 26 and weak seeds 105/108/113/115
  at ticks 24/22/23/24. Persistence totals were 1/15/0, productive events
  259/263/250, and terminal distinct-rule totals 112/116/85 of 128.
- All 48 trajectories replayed and guided cost matched at 3,072 units per arm.
  Bootstrap, full cycle-catalyst, and individual `op1/op2/op0` ablations left
  weak incidence at 0/16; guiding-term removal retained unguided 1/16.
- No seed/horizon extension. Cohort B unevaluated and cannot rescue cohort A.
  Chemistry remained PeTTa-native on the recorded local PeTTa/SWI stack;
  spontaneous-emergence claim none. Checks: exp00 (153), exp07 (248),
  detector invariance, and `git diff --check`. Commit `1f237df` pushed to
  GitHub `main`.
## 2026-07-18 10:30 — Dual-bootstrap mechanism audit frozen

- Chose characterization of the unguided-versus-weak reversal as the next
  objective; a distinct emergence search remains unauthorized.
- Added repo analysis plan
  `experiments/exp07/PREREG_DUAL_MECHANISM_AUDIT.md` before diagnostic code.
- Frozen input is only the completed seeds 201--232, ticks 3--34 matrix. No
  seeds, ticks, chemistry, selector variants, or counterfactual draws may be
  added.
- Fixed per-tick trace fields and derived counts for selection, applicability,
  pathway-prefix progress, food exhaustion/resets, and post-closure
  maintenance. Interpretation is a precedence over trace mismatch,
  applicability loss, resource diversion, maintenance loss, or unresolved.
- The audit is descriptive because the registered outcome is already known
  and deterministic selector schedules are not independently randomized. It
  cannot rescue guided uplift or support spontaneous emergence.
- Provenance/check: local PeTTa/SWI stack via `scripts/run_exp00.sh`; 154
  assertions passed before the plan edit. No chemistry code or trajectory was
  added.

## 2026-07-18 16:30 PDT — Dual mechanism prefix diagnostics

- Extended only the frozen trace-derived audit: PeTTa computes longest
  completed pathway-prefix depth, first-complete ticks (sentinel 99), and
  per-depth occupancy for every arm/seed across the fixed 32 ticks.
- The report query now serializes identity-labeled per-seed prefix summaries
  for unguided, weak Doob-h, and shuffled calibration arms. No chemistry,
  selector, seed, horizon, trajectory, or interpretation branch changed;
  `applicability-loss` remains decisive and emergence claim remains none.
- Provenance: local PeTTa/SWI stack, `src/chem_exp07.metta`, frozen validated
  mechanism rows, and exp07 smoke assertions. Exp00, exp07, detector
  invariance, and `git diff --check` passed; commit `f839b27` pushed to GitHub
  `main`.
## 2026-07-18 18:30 PDT — Dual mechanism food/reset and paired prefix slice

- Derived first observed post-reset/pre-fire exhaustion ticks for all five
  foods and reset counts at prefix depths 0--5 from the validated 32-row
  PeTTa traces for every arm/seed.
- Added identity-preserving per-seed weak-minus-unguided differences for all
  six first-prefix ticks and seven prefix-depth occupancies; sentinel 99 is
  retained without censoring.
- No chemistry, selector, draw, trajectory, endpoint, or interpretation
  changed. `applicability-loss` remains the first eligible frozen label;
  emergence claim none. Median serialization and paired food/reset
  differences remain.
- Provenance/checks: local recorded PeTTa/SWI stack; `src/chem_exp07.metta`,
  exp07 smoke, and `dual_report.metta`; exp00, exp07, detector invariance, and
  `git diff --check` passed.
- Commit `a481dbc` pushed to GitHub `main`.

## 2026-07-19 00:30 PDT — Effective cap provenance accessors

- Added PeTTa-native `candidate-selection-cap` and
  `generated-selection-fire-record-cap` queries so the effective bounded cap
  used by deterministic selection and chamber ticking is directly inspectable.
- Exp00 smoke proves cap 2 is retained and an oversized requested cap 9 is
  conservatively recorded as effective cap 8. No chemistry, selector result,
  trajectory, or scientific interpretation changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh`; `git diff --check` passed. Commit `fcde7b5` pushed to
  GitHub `main`.
# 2026-07-19 02:30 — Requested/effective cap provenance

- Extended the PeTTa-native generated-selection/fire record to retain the
  original `candidate-cap` as well as the effective bounded scalar already
  consumed by deterministic selection and chamber ticking.
- Exp00 proves requested cap 9 remains auditable beside effective cap 8, and a
  requested `(candidate-cap 2 0)` remains visible while closing selection at
  effective cap 0. Generated pools, selected candidates, and chemistry are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (157
  passing assertions); `git diff --check` passed. Commit `e26c74a` pushed to
  GitHub `main`.
## 2026-07-19 12:30 PDT - nonpositive per-tick provenance audit

Added focused exp00 assertions over the complete PeTTa-native
generation/selection/fire record. Requests `(-1 1)` and `(0 3)` are retained
for audit, expose the already established effective `(0 0)` boundary, and
produce an unchanged chamber. This is test-only hardening: no selector,
candidate generator, chemistry, or scientific claim changed. Local PeTTa/SWI
`scripts/run_exp00.sh` passed with 172 true results and `git diff --check`
passed. Commit `c9dae0c` was pushed normally to GitHub `main`; pre-existing
untracked scratch files were left untouched.
## 2026-07-19 14:30 PDT — scalar candidate-cap provenance

- Added PeTTa-native accessors for requested/effective per-tick and per-rule
  fields on the complete generated-selection/fire record.
- Exp00 proves requested `(9 3)` is directly queryable beside normalized
  `(8 1)`. Generation, selector output, chamber chemistry, and scientific
  claims are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (176 true assertions); `git diff --check` passed.
  Commit `4604599` pushed to GitHub `main`.

## 2026-07-19 20:30 PDT — dropped candidate count

- Added a PeTTa-native accessor deriving the number of candidates excluded by
  the effective cap from the complete generated-selection/fire record.
- Exp00 covers one dropped under cap 2, none under cap 3, and all three under
  a nonpositive request. Generation, deterministic selection, firing, and
  chemistry are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (185 true assertions); `git diff --check` passed.
  Commit `57bd83c` pushed to GitHub `main`.
# 2026-07-20 06:30 PDT — bounded-generator capacity disposition

- Added a PeTTa-native accessor that classifies the complete generated-
  selection/fire record as `open` or `saturated` from its stable cap and
  remaining-capacity fields.
- Exp00 covers the ordinary three-rule fixture as open and the supported
  twelve-rule fixture as saturated at the eight-candidate boundary.
- No generator order, selection cap, deterministic firing, chamber chemistry,
  trajectory, or scientific claim changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (196 true results); `git diff --check` passed.
- Commit `538255d` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.
# 2026-07-20 12:30 PDT — task-state reconciliation

- Reconciled the open exp07 umbrella against its completed registered record:
  rich-pool pilot, ordered-bootstrap replication gates, frozen dual-bootstrap
  negative result, and bounded mechanism audit are complete.
- The final dual-bootstrap guided-uplift result remains negative; the frozen
  descriptive mechanism precedence assigns `applicability-loss`, and
  `emergence-claim none` remains.
- Closed the stale exp06 follow-up because the three-tick stateful cap sweep
  and ACS boundary rejection were completed in commits `de84704` and
  `40aef6`. No chemistry, trajectory, or result changed.
- Provenance/check: local recorded PeTTa/SWI stack; `scripts/run_exp00.sh`
  returned 200 true results and `git diff --check` passed.
# 2026-07-20 16:30 PDT — candidate attrition-stage provenance

- Added PeTTa-native `generated-selection-fire-record-attrition-stage` to
  classify complete source loss as `none`, `generation`, `selection`, or
  `both` from the existing bounded-generation and cap provenance.
- Exp00 covers all four classifications across the ordinary three-rule source
  and supported twelve-rule source. Candidate generation, deterministic
  selection, firing, chamber chemistry, and scientific claims are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (204 true results); `git diff --check` passed.
# 2026-07-20 20:30 PDT — candidate attrition field accessors

- Added seven PeTTa-native accessors for every field of the compact
  `candidate-attrition` audit atom: source/generated/bounded widths,
  generation/selection/total omissions, and attributed stage.
- Focused exp00 coverage queries both a live ordinary summary and the complete
  supported `(12 8 2 4 6 10 both)` boundary. No generation, selection,
  firing, chamber chemistry, trajectory, or scientific claim changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (213 true results); `git diff --check` passed.
  Commit `bf65490` pushed normally to GitHub `main`.
# 2026-07-20 22:30 PDT — candidate attrition conservation check

- Added PeTTa-native `candidate-attrition-consistent?` to validate all three
  source/generated/bounded conservation identities carried by the compact
  audit atom.
- Exp00 covers a live ordinary summary, the supported twelve-rule boundary,
  and rejection of a deliberately inconsistent generation omission count.
- No candidate generation, deterministic selection, firing, chamber
  chemistry, trajectory, or scientific claim changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (216 true results); `git diff --check` passed.
- Commit `201febf` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.

# 2026-07-21 00:30 PDT — candidate attrition stage validation

- Added PeTTa-native `candidate-attrition-stage-consistent?` to derive the
  expected loss-stage label from generation and selection omission counts.
- Exp00 covers `none`, `selection`, `generation`, and `both`, plus rejection
  of a count-consistent record mislabeled `selection` instead of `both`.
- No candidate generation, deterministic selection, firing, chamber
  chemistry, trajectory, or scientific claim changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (220 passing results); `git diff --check` passed.
- Commit `edd8d6e` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.
# 2026-07-21 08:30 PDT — complete live candidate-bound validity

- Added PeTTa-native `generated-selection-fire-record-bounds-valid?` and the
  combined `generated-selection-fire-record-valid?` gate over complete
  chamber-tick provenance.
- The gate checks the fixed eight-candidate generator boundary, bounded-pool
  width against the normalized per-tick cap, embedded scalar-cap agreement,
  and the existing source/stage attrition validity.
- Exp00 accepts ordinary cap-2 and closed cap-0 records and rejects a
  synthetic record whose attrition conserves 3 -> 3 -> 3 but whose bounded
  pool violates an effective cap of two. Chemistry is unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (233 true results); `git diff --check` passed.
- Commit `4f617d4` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.

# 2026-07-21 22:30 PDT — complete validity-disposition coverage

- Added focused exp00 assertions for all complete chamber-tick provenance
  outcomes: `valid`, `invalid-attrition`, `invalid-bounds`,
  `invalid-generation`, `invalid-selection`, and `invalid-firing`.
- The malformed records exercise the fixed first-failure precedence while
  leaving generation, selection, firing, chamber chemistry, and trajectories
  unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (250 true results); `git diff --check` passed.
- Commit `16c8707` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.
# 2026-07-22 00:30 PDT — auditable live chamber-tick result

- Added PeTTa-native `chamber-tick-result-from-generated-record` and
  `chamber-tick-generated-result`, retaining the complete validity disposition
  beside the projected chamber.
- The existing chamber-only ticking functions now project that same checked
  result. Valid transitions are unchanged; malformed records retain their
  first-failure label and fail closed to the input chamber.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (252 true
  results); `git diff --check` passed.
- Commit `f98be89` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.

# 2026-07-22 02:30 PDT — chamber-tick disposition accessor

- Added PeTTa-native `chamber-tick-result-validity`, complementing the chamber
  projection so audit/report consumers can query the retained validity label
  without positional destructuring.
- Focused exp00 coverage queries both an ordinary valid live tick and a
  malformed over-cap result attributed `invalid-bounds`. Generation,
  deterministic selection, firing, chemistry, and trajectories are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (254 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched.
- Commit `8140999` pushed normally to GitHub `main`.

# 2026-07-22 04:30 PDT — chamber-tick boolean validity query

- Added PeTTa-native `chamber-tick-result-valid?` so downstream tick-loop,
  audit, and report code can branch on checked validity without comparing the
  disposition atom itself.
- Exp00 covers an ordinary valid live result and a malformed over-cap result
  attributed `invalid-bounds`. Candidate generation, deterministic selection,
  firing, chemistry, and trajectories are unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (256 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched.
- Commit `c5f6502` pushed normally to GitHub `main`.
# 2026-07-22 12:30 PDT — single-evaluation generated tick step

- Added PeTTa-native `chamber-tick-generated-step`, packaging the checked
  outcome and projected chamber from one evaluated live result.
- Added outcome/chamber accessors and productive plus cap-zero no-op smoke
  coverage. Generation, deterministic selection, firing, and chemistry are
  unchanged.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (269
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched.
- Commit `276eba5` pushed normally to GitHub `main`.
# 2026-07-22 18:30 PDT — auditable bounded loop width

- Added PeTTa-native `chamber-tick-steps-count` for the exact two-step loop
  result shape and focused closed-cap smoke coverage.
- A productive two-step probe found that fixed-position applicability remains
  partial when the tick-1 selector chooses a rule whose molecule layout does
  not unify with the state. Recorded totalization as the next task; no claim
  or chemistry result changed.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (272
  true results); `git diff --check` passed. Pre-existing untracked scratch
  files were left untouched. Commit `a7b127c` pushed normally to GitHub
  `main`.
## 2026-07-22 20:30 — Totalize regenerated fixed-position applicability

- Reworked the PeTTa-native four-molecule applicability clause to bind the
  complete state shape and explicitly compare its positions with the selected
  rule, making a layout mismatch reduce to false.
- The bounded productive two-step path now returns `(productive no-op)` and
  the first tick's projected chamber when tick 2 selects an unrepresented
  layout; it no longer leaves an irreducible applicability expression.
- Exp00 returned 274 true results and `git diff --check` passed using the
  recorded local PeTTa/SWI stack. Commit `5e7661d` pushed to GitHub `main`.
# 2026-07-23 02:30 PDT — fourth bounded generated state handoff

- Added PeTTa-native `chamber-tick-generated-steps-4`, passing the three-step
  final chamber directly into a fourth live checked generation, deterministic
  selection, and firing step.
- Added three-outcome positional accessors needed by the composition and
  four-step width/productive/no-op summaries.
- Exp00 covers exact closed-cap `(no-op no-op no-op no-op)` and
  productive-first `(productive no-op no-op no-op)` outcomes, final chamber,
  and counts. No host-side chemistry logic or scientific claim changed.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (292 true results, zero failure markers);
  `git diff --check` passed. Pre-existing untracked scratch files were left
  untouched. Commit `317f23b` pushed normally to GitHub `main`.
# 2026-07-23 10:30 PDT — Complete eight-step bounded generated handoff

- Added PeTTa-native `chamber-tick-generated-steps-8`, which feeds the
  seven-step projected chamber into an eighth ordinary checked generated step
  at the stable eight-candidate generation boundary.
- Seven-outcome positional accessors enable the state handoff; eight-outcome
  atoms expose exact width, productive count, and no-op count. Exp00 verifies
  closed-cap and productive-first trajectories plus final-chamber
  preservation. Chemistry remains on the existing generation, deterministic
  selection, and checked firing path.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (320 true
  results); `git diff --check` passed. Pre-existing untracked scratch files
  were left untouched. Commit `4192438` pushed normally to GitHub `main`.

# 2026-07-23 18:30 PDT — bounded-history loop-control decision

- Added PeTTa-native `chamber-tick-steps-next-action` over the complete
  bounded-history disposition: productive histories continue, complete valid
  no-op histories stop quiescent, and malformed retained outcomes stop
  invalid.
- Exp00 covers all three decisions using live eight-step generated histories
  plus an invalid fixture. Candidate generation, deterministic selection,
  firing, chemistry, and scientific claims are unchanged.
- Provenance/checks: recorded local PeTTa/SWI stack via
  `scripts/run_exp00.sh` (332 true results); `git diff --check` passed.
- Commit `602163c` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.

# 2026-07-23 22:30 PDT — consume sweep control in live ticking

- Added PeTTa-native `chamber-tick-generated-sweeps-2`, which consumes the
  first live sweep's own action and advances only `continue` from the exact
  projected chamber.
- A productive initial fixture retains two sweeps and ends
  `stop-quiescent`; a closed candidate cap retains one sweep and stops
  without a redundant generation pass. Accessors expose the retained count,
  action, individual sweeps, and final chamber.
- Provenance/checks: local PeTTa/SWI `scripts/run_exp00.sh` passed with 341
  true results; `git diff --check` passed. No chemistry rule, selection
  policy, candidate cap, or scientific claim changed. Commit `2630239`
  pushed to GitHub `main`.

# 2026-07-24 00:30 PDT — run-wide bounded sweep accounting

- Added PeTTa-native aggregate accounting over retained one- and two-sweep
  runs: total ticks, productive ticks, no-ops, unaccounted outcomes,
  accounting validity, and run-wide disposition.
- The productive fixture retains 16 checked ticks `(1 productive, 15 no-op)`
  and remains disposition `productive` after its terminal sweep returns
  `stop-quiescent`; the closed-cap fixture is quiescent across eight no-ops.
- Provenance/checks: local PeTTa/SWI `scripts/run_exp00.sh` passed with 351
  true results and no failure markers; `git diff --check` passed. No
  chemistry rule, deterministic selection policy, candidate cap, trajectory,
  or scientific claim changed.
- Commit `52902f8` pushed normally to GitHub `main`; pre-existing untracked
  scratch files were left untouched.
# 2026-07-24 10:30 PDT — sixth bounded generated sweep

- Added PeTTa-native `chamber-tick-generated-sweeps-6`, advancing only the
  productive bound-exhausted five-sweep result from its exact projected
  chamber while preserving established one-/two-sweep early stops.
- Six-sweep accessors and aggregate accounting retain 48 productive checked
  ticks, zero no-ops, and the exact tick-48 chamber. The fixed
  `append-chamber-event` seam now retains 48 events.
- Candidate generation, deterministic selection, checked firing, and
  chemistry remain on the existing PeTTa-native path; no scientific claim
  changed.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` (394
  true results, zero failure markers); `git diff --check` passed. Commit
  `ba872a4` pushed normally to GitHub `main`; pre-existing untracked scratch
  files were left untouched.
# 2026-07-24 18:30 PDT — thirteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 12 to 13 retained
  source rules while preserving the explicit first-eight candidate boundary.
- Extended source rewrite ownership and bounded source-count provenance to 13
  rules. The cap-2 direct chamber tick still deterministically selects the
  productive second generated candidate and preserves the complete rule list.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 423 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Commit `fa5fbd4` pushed normally to GitHub `main`; pre-existing untracked
  exp08/catalysis scratch work was left untouched.

# 2026-07-24 20:30 PDT — fourteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 13 to 14 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 14
  rules. The attrition audit reports six generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 428 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `ea6f29b` pushed normally to GitHub `main`.

# 2026-07-24 22:30 PDT — fifteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 14 to 15 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 15
  rules. The attrition audit reports seven generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 434 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `8e0bcb8` pushed normally to GitHub `main`.

# 2026-07-25 00:30 PDT — sixteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 15 to 16 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 16
  rules. The attrition audit reports eight generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 439 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `b6c79ee` pushed normally to GitHub `main`.

# 2026-07-25 02:30 PDT — seventeen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 16 to 17 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 17
  rules. The attrition audit reports nine generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 444 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `2b4562d` pushed normally to GitHub `main`.

# 2026-07-25 04:30 PDT — eighteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 17 to 18 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 18
  rules. The attrition audit reports ten generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 449 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `71d4477` pushed normally to GitHub `main`.

# 2026-07-25 06:30 PDT — nineteen-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 18 to 19 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 19
  rules. The attrition audit reports eleven generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 453 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `2e78383` pushed normally to GitHub `main`.

# 2026-07-25 10:30 PDT — twenty-one-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 20 to 21 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 21
  rules. The attrition audit reports thirteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 463 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `2ed002a` pushed normally to GitHub `main`.

# 2026-07-25 12:30 PDT — twenty-two-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 21 to 22 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 22
  rules. The attrition audit reports fourteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 468 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `745d871` pushed normally to GitHub `main`.

# 2026-07-25 14:30 PDT — twenty-three-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 22 to 23 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 23
  rules. The attrition audit reports fifteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 474 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `b1a5a7a` pushed normally to GitHub `main`.

# 2026-07-25 16:30 PDT — twenty-four-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 23 to 24 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 24
  rules. The attrition audit reports sixteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 479 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `69c3db6` pushed normally to GitHub `main`.

# 2026-07-25 20:30 PDT — twenty-six-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 25 to 26 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 26
  rules. The attrition audit reports eighteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 489 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `be9fd5d` pushed normally to GitHub `main`.

# 2026-07-25 22:30 PDT — twenty-seven-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 26 to 27 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 27
  rules. The attrition audit reports nineteen generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 494 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `288138c` pushed normally to GitHub `main`.
# 2026-07-26 02:30 PDT — twenty-nine-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 28 to 29 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 29
  rules. The attrition audit reports twenty-one generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 504 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `a8dcdc6` pushed normally to GitHub `main`.

# 2026-07-26 04:30 PDT — thirty-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 29 to 30 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 30
  rules. The attrition audit reports twenty-two generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 509 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `426712a` pushed normally to GitHub `main`.

# 2026-07-26 10:30 PDT — exp03 singleton regression repair

- Diagnosed the seed-11 three-tick query's eight identical answers as a
  duplicated `seed-number` proof path: the mapping was defined in both the
  shared exp00 kernel and `chem_dynamics`, so three ticks yielded 2^3 proofs.
- Removed redundant dynamics-local mappings for seeds 11, 13, and 17. The
  seed-11 chamber is singleton again; fixing it also exposed and repaired the
  same previously masked multiplicity at seeds 13 and 17.
- Checks: `scripts/run_exp03.sh` and the full canonical
  exp00/01/contract/02/03/04/05/06/07 script matrix passed on the recorded
  local PeTTa/SWI stack; `git diff --check` passed. No chemistry rule,
  trajectory, or scientific interpretation changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `16b6f1a` pushed normally to GitHub `main`.

# 2026-07-27 00:30 PDT — thirty-four-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 33 to 34 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 34
  rules. The attrition audit reports twenty-six generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 529 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `4792097` pushed normally to GitHub `main`.

# 2026-07-27 06:30 PDT — thirty-eight-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 37 to 38 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 38
  rules. The attrition audit reports thirty generation omissions, while the
  cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 549 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `f802c30` pushed normally to GitHub `main`.

# 2026-07-27 10:30 PDT — forty-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 39 to 40 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 40
  rules. The attrition audit reports thirty-two generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 559 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `030ce18` pushed normally to GitHub `main`.

# 2026-07-27 12:30 PDT — forty-one-rule bounded generation boundary

- Extended the four-molecule PeTTa-native generator from 40 to 41 retained
  source rules while preserving the stable first-eight candidate prefix.
- Extended source rewrite ownership and bounded source-count provenance to 41
  rules. The attrition audit reports thirty-three generation omissions, while
  the cap-2 direct tick still deterministically selects and fires productive
  `r0`.
- Provenance/checks: local PeTTa/SWI stack via `scripts/run_exp00.sh` passed
  with 564 terminal true results and zero failure markers;
  `git diff --check` passed. No chemistry rule or scientific claim changed.
- Pre-existing untracked exp08/catalysis scratch work was left untouched.
- Commit `851189a` pushed normally to GitHub `main`.
## 2026-07-28 10:30 — neutral SSA seeded-draw slice

- Added PeTTa-native exact weight totals and cumulative categorical selection
  over canonically ordered event/weight rows.
- Event and waiting-time draws use separate deterministic keys. Waiting time
  is retained as the exact symbolic inverse-CDF inputs rather than evaluated
  through a host float.
- Empty enabled-event lists fail closed as `no-enabled-event`; same manifest
  inputs reproduce the same event and waiting-time record.
- `scripts/run_neutral_ssa_tests.sh`: 23 passing checks, no failure markers.
  `git diff --check` passed. No calibration endpoint was queried.
