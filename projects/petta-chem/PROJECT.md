# PeTTa Abstract Algorithmic Chemistry

- Slug: `petta-chem`
- Status: `active`
- Created: `2026-06-26`
- Last reviewed: `2026-07-25` (08:30)
- Owner: Benjamin Goertzel

## Purpose

Build a small, inspectable PeTTa-first abstract algorithmic chemistry substrate that can produce reproducible event logs and test whether autocatalytic organization emerges in symbolic rewrite soups.

The seed specification is `library/petta-abstract-algorithmic-chemistry/SOURCE.md`, preserving Benjamin's June 2026 PDF: *Initial Abstract Algorithmic Chemistry Experiments in PeTTa: A PeTTa-First, MORK-Ready Research and Implementation Plan*.

## Success criteria

Initial milestone:

> Demonstrate spontaneous, measurable, replayable, and intervention-relevant autocatalytic organization in a bounded abstract PeTTa chemistry.

Operational criteria:

- exp00 deterministic smoke test validates schemas, seeded execution, abundance updates, event logging, snapshots, and replay.
- exp01 planted ACS recovery validates the ACS/RAF-like detector and ablation protocol before emergence claims.
- exp02 random catalytic polymer chemistry finds candidate regimes where non-planted ACSs are more frequent, persistent, or causally relevant than shuffled/no-catalysis controls.
- Every consequential run has config, seed list, event logs, metrics, ACS candidates, ablation results when applicable, and a `RUN.md`/summary.
- Claims distinguish active ACS, useful ACS, causal ACS, degenerate loop, parasite, and false positive.

## Scope

### In scope

- PeTTa/Atomspace-shaped atom schemas for chambers, ticks, molecules, rules, candidates, events, catalysis, ACSs, and causal tests.
- Seeded chamber tick loop with bounded candidate generation, scoring, stochastic sampling, reaction firing, abundance updates, and event logging.
- Analytics for descriptive chemistry metrics, empirical catalysis mining, ACS/RAF-like closure, persistence/productivity, replay, and ablation.
- Replaceable seams for future MORK or host acceleration: matching, sampling, scoring, ACS scans, replay, canonical hashing, rule distance, structural mutation.
- Initial experiments 0-2, then rule molecules/ecology/predictive weighting only after replay and ACS detection are solid.

### Out of scope for now

- Semantic graph chemistry, music chemistry, PLN, MOSES, AIRIS, CENF, optimal transport, neural models, open-ended GUI, and full ActPC-MORK integration.
- Claims of AGI, semantic reasoning, musical creativity, or biological realism.
- Paid remote compute unless separately approved with a cleanup/cost plan.

## Current state

2026-07-25 08:30 progress: bounded PeTTa-native candidate generation is now
total for a 20-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 20
rules, the audit record reports twelve generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 459
terminal true results and zero failure markers; `git diff --check` passed.
Commit `84d70c7` pushed normally to GitHub `main`.

2026-07-25 06:30 progress: bounded PeTTa-native candidate generation is now
total for a 19-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 19
rules, the audit record reports eleven generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 453
terminal true results and zero failure markers; `git diff --check` passed.
Commit `2e78383` pushed normally to GitHub `main`.

2026-07-25 04:30 progress: bounded PeTTa-native candidate generation is now
total for an 18-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 18
rules, the audit record reports ten generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 449
terminal true results and zero failure markers; `git diff --check` passed.
Commit `71d4477` pushed normally to GitHub `main`.

2026-07-25 02:30 progress: bounded PeTTa-native candidate generation is now
total for a 17-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 17
rules, the audit record reports nine generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 444
terminal true results and zero failure markers; `git diff --check` passed.
Commit `2b4562d` pushed normally to GitHub `main`.

2026-07-25 00:30 progress: bounded PeTTa-native candidate generation is now
total for a 16-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 16
rules, the audit record reports eight generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 439
terminal true results and zero failure markers; `git diff --check` passed.
Commit `b6c79ee` pushed normally to GitHub `main`.

2026-07-24 22:30 progress: bounded PeTTa-native candidate generation is now
total for a 15-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 15
rules, the audit record reports seven generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 434
terminal true results and zero failure markers; `git diff --check` passed.
Commit `8e0bcb8` pushed normally to GitHub `main`.

2026-07-24 20:30 progress: bounded PeTTa-native candidate generation is now
total for a 14-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership/count seams cover all 14
rules, the audit record reports six generation omissions, and direct cap-2
deterministic selection still fires productive `r0`. Exp00 passed with 428
terminal true results and zero failure markers; `git diff --check` passed.
Commit `ea6f29b` pushed normally to GitHub `main`.

2026-07-24 18:30 progress: bounded PeTTa-native candidate generation is now
total for a 13-rule four-molecule chamber while retaining the stable
first-eight generated prefix. Source-rule ownership and source-count audit
seams also cover all 13 retained rules, and direct cap-2 deterministic
selection still fires the productive second candidate. Exp00 passed with 423
terminal true results and zero failure markers; `git diff --check` passed.
Commit `fa5fbd4` pushed normally to GitHub `main`.

2026-07-24 16:30 progress: PeTTa-native bounded chamber ticking now supports
a ninth live sweep that distinguishes driver-bound exhaustion from
resource-driven quiescence. The 64-reactant fixture remains productive through
eight sweeps, then retains a complete ninth sweep of eight checked no-ops,
returns `stop-quiescent`, preserves 64 events, and keeps the exact tick-64
chamber. Exp00 passed with 421 terminal true results and zero failure markers;
`git diff --check` passed. Commit `500172b` pushed normally to GitHub `main`.

2026-07-24 14:30 progress: PeTTa-native bounded chamber ticking now supports
eight live sweeps. `chamber-tick-generated-sweeps-8` advances only a
productive seven-sweep bound exhaustion, preserves one-/two-sweep early
stops, and retains exact run-wide accounting and the terminal chamber through
tick 64. The fixed event-history append boundary was extended from 56 to 64
events. Exp00 passed with 412 terminal true results and zero failure markers;
`git diff --check` passed. Commit `871fe0e` pushed normally to GitHub `main`.

2026-07-24 12:30 progress: PeTTa-native bounded chamber ticking now supports
seven live sweeps. `chamber-tick-generated-sweeps-7` advances only a
productive six-sweep bound exhaustion, preserves one-/two-sweep early stops,
and retains exact run-wide accounting and the terminal chamber through tick
56. The fixed event-history append boundary was extended from 48 to 56
events. Exp00 passed with 403 terminal true results and zero failure markers;
`git diff --check` passed. Commit `d1e5046` pushed normally to GitHub `main`.

2026-07-24 10:30 progress: PeTTa-native bounded chamber ticking now supports
six live sweeps. `chamber-tick-generated-sweeps-6` advances only a productive
five-sweep bound exhaustion, preserves one-/two-sweep early stops, and retains
exact run-wide accounting and the terminal chamber through tick 48. The fixed
event-history append boundary was extended from 40 to 48 events. Exp00 passed
with 394 true results and zero failure markers; `git diff --check` passed.
Commit `ba872a4` pushed normally to GitHub `main`.

2026-07-24 08:30 progress: PeTTa-native bounded chamber ticking now supports
five live sweeps. `chamber-tick-generated-sweeps-5` advances only a productive
four-sweep result from its exact projected chamber, preserves one-/two-sweep
early stops, and retains exact run-wide accounting through tick 40. The fixed
event-history append boundary was extended from 32 to 40 events. Exp00 passed
with 385 true results and zero failure markers; `git diff --check` passed.
Commit `587143d` pushed normally to GitHub `main`.

2026-07-24 06:30 progress: PeTTa-native bounded chamber ticking now supports
four live sweeps. The work exposed and extended the fixed event-history append
boundary from 24 to 32 events; deterministic generation, selection, checked
firing, and exact projected-chamber handoff now remain live through tick 32.
Closed-cap and productive-then-quiescent fixtures still stop after one and two
sweeps, while the sustained cap-1 fixture returns `stop-bounded` with 32
productive outcomes and the exact tick-32 chamber. Exp00 passed with 375 true
results and `git diff --check` passed. Commit `11d9598` pushed to GitHub
`main`.

2026-07-24 04:30 progress: PeTTa-native bounded chamber ticking now supports
three live sweeps while preserving early stop behavior. Closed-cap and
productive-then-quiescent fixtures retain one and two sweeps respectively;
a sustained cap-1 fixture reaches `stop-bounded` only after 24 productive
checked ticks and preserves its exact tick-24 chamber. Exp00 passed with 366
true results and `git diff --check` passed. Commit `c33537e` pushed to GitHub
`main`.

2026-07-24 02:30 progress: bounded PeTTa-native chamber ticking now reports
`stop-bounded` when its second and final allowed sweep remains productive,
rather than returning an unactionable `continue`. A sustained fixture retains
all 16 productive checked ticks and its exact tick-16 chamber. Exp00 passed
with 357 true results and `git diff --check` passed. Commit `6223b6e` pushed
to GitHub `main`.

2026-07-24 00:30 progress: bounded PeTTa-native tick runs now retain
run-wide outcome accounting across one or two live sweeps. Total, productive,
no-op, and unaccounted counts distinguish a productive first sweep followed
by quiescence from a run that was quiescent throughout, even though both
terminate with `stop-quiescent`. Exp00 passed with 351 true results and
`git diff --check` passed. Commit `52902f8` pushed to GitHub `main`.

2026-07-23 22:30 progress: PeTTa now consumes a live sweep's own control
action through `chamber-tick-generated-sweeps-2`. A productive first sweep
advances from its exact projected chamber into a second bounded sweep, while
a closed-cap first sweep stops without regenerating chemistry. The exp00
fixture reaches `stop-quiescent` after one or two sweeps as appropriate;
exp00 passed with 341 true results and `git diff --check` passed.
Commit `2630239` pushed to GitHub `main`.

2026-07-23 20:30 progress: one PeTTa-native
`chamber-tick-generated-sweep` now packages the complete eight-step live
history with the control action derived from that exact history. Direct
accessors expose the action, retained steps, and projected chamber; closed-cap
and productive paths return `stop-quiescent` and `continue`, respectively.
Exp00 passed with 336 true results and `git diff --check` passed.
Commit `80d41c6` pushed to GitHub `main`.

2026-07-23 18:30 progress: complete bounded live tick histories now drive a
PeTTa-native `chamber-tick-steps-next-action`. Productive histories return
`continue`, complete quiescent histories return `stop-quiescent`, and
malformed histories fail closed to `stop-invalid`. Exp00 passed with 332 true
results and `git diff --check` passed. Commit `602163c` pushed to GitHub
`main`.

2026-07-23 16:30 progress: bounded live tick histories now expose one
PeTTa-native `chamber-tick-steps-disposition`. Complete closed-cap,
productive-first, and malformed histories classify as `quiescent`,
`productive`, and `invalid-outcomes`, respectively, without host-side count
logic. Exp00 passed with 329 true results and `git diff --check` passed.
Commit `8b7e3a0` pushed to GitHub `main`.

2026-07-23 14:30 progress: bounded tick histories now expose the exact
PeTTa-native `chamber-tick-steps-unaccounted-count`. Complete closed-cap and
productive-first eight-step paths report zero, while a three-step history
containing `unknown` reports one; the existing accounting-validity gate now
consumes this count. Exp00 passed with 326 true results and
`git diff --check` passed. Commit `7999344` pushed to GitHub `main`.

2026-07-23 12:30 progress: bounded live generated tick histories now expose
a PeTTa-native outcome-accounting invariant. The complete eight-step
closed-cap and productive-first paths validate because every retained outcome
is classified as `productive` or `no-op`; an otherwise well-shaped history
containing `unknown` is rejected. Exp00 passed with 323 true results and
`git diff --check` passed. Commit `c8713af` pushed to GitHub `main`.

2026-07-23 10:30 progress: bounded live generated ticking now reaches the
stable eight-candidate generation boundary through eight checked PeTTa-native
state handoffs. Exp00 covers closed-cap
`(no-op no-op no-op no-op no-op no-op no-op no-op)` and productive
`(productive no-op no-op no-op no-op no-op no-op no-op)` paths, including
final chamber and exact outcome counts; 320 true results passed.
`git diff --check` passed; commit `4192438` pushed to GitHub `main`.

2026-07-23 08:30 progress: bounded live generated ticking now extends through
seven checked PeTTa-native state handoffs. Exp00 covers the closed-cap
`(no-op no-op no-op no-op no-op no-op no-op)` path and productive
`(productive no-op no-op no-op no-op no-op no-op)` path, including final
chamber and exact outcome counts; 313 true results and `git diff --check`
passed. Commit `81705be` pushed to GitHub `main`.

2026-07-23 06:30 progress: bounded live generated ticking now extends through
six checked PeTTa-native state handoffs. Exp00 covers the closed-cap
`(no-op no-op no-op no-op no-op no-op)` path and productive
`(productive no-op no-op no-op no-op no-op)` path, including final chamber
and exact outcome counts; 306 true results and `git diff --check` passed.
Commit `4fdccfe` pushed to GitHub `main`.

2026-07-23 04:30 progress: bounded live generated ticking now extends through
five checked PeTTa-native state handoffs. Exp00 covers the closed-cap
`(no-op no-op no-op no-op no-op)` path and productive
`(productive no-op no-op no-op no-op)` path, including final chamber and
exact outcome counts; 299 true results and `git diff --check` passed.
Commit `f6daad7` pushed to GitHub `main`.

2026-07-23 02:30 progress: bounded live generated ticking now extends through
four checked PeTTa-native state handoffs. Exp00 covers the closed-cap
`(no-op no-op no-op no-op)` path and productive
`(productive no-op no-op no-op)` path, including final chamber and exact
outcome counts; 292 true results and `git diff --check` passed.
Commit `317f23b` pushed to GitHub `main`.

2026-07-23 00:30 progress: bounded live generated ticking now extends through
three checked PeTTa-native state handoffs. Exp00 covers the closed-cap
`(no-op no-op no-op)` path and productive `(productive no-op no-op)` path,
including final chamber and exact outcome counts; 285 true results and
`git diff --check` passed. Commit `5a27e88` pushed to GitHub `main`.

2026-07-22 22:30 progress: bounded two-step generated tick sequences now
expose PeTTa-native productive and no-op counts. Exp00 covers the closed-cap
`(no-op no-op)` path and productive `(productive no-op)` handoff without
host-side outcome parsing; 277 true results and `git diff --check` passed.
Commit `2da3f94` pushed to GitHub `main`.

2026-07-22 20:30 progress: fixed-position four-molecule candidate
applicability is now total across regenerated chamber states. A selected rule
whose required layout is absent reduces to false and produces a checked
`no-op`, so the productive two-step loop returns `(productive no-op)` and the
first projected chamber instead of becoming partial. Exp00 passed with 274
true results and `git diff --check` passed. Commit `5e7661d` pushed to GitHub
`main`.

2026-07-22 18:30 progress: bounded generated tick sequences now expose their
exact PeTTa-native step count through `chamber-tick-steps-count`. Exp00 checks
the two-step closed-cap loop and passed with 272 true results;
`git diff --check` passed. A productive two-step probe also identified the
next bounded-generation issue: fixed-position applicability is partial when
the next selected rule does not match the state's molecule layout. Commit
`a7b127c` pushed to GitHub `main`.

2026-07-22 14:30 progress: the loop-facing generated tick step now composes
into a bounded two-step PeTTa-native state handoff. Each live checked step
receives the prior step's projected chamber, while `chamber-tick-steps`
retains both outcomes and the final chamber. Exp00 passed with 271 true
results and `git diff --check` passed. Commit `c77b250` pushed to GitHub
`main`.

2026-07-22 12:30 progress: live generated chamber ticks now return one
PeTTa-native `chamber-tick-step` containing both the checked outcome and the
projected chamber. Tick loops can advance and audit from a single evaluated
generation/selection/result path instead of issuing two live queries. Exp00
passed with 269 true results and `git diff --check` passed.
Commit `276eba5` pushed to GitHub `main`.

2026-07-22 10:30 progress: live generated chamber ticks now expose a direct
PeTTa-native `chamber-tick-generated-outcome` query. Tick loops can obtain
`productive`, `no-op`, or a validation boundary without manually composing
the checked-result constructor and outcome accessor. Exp00 passed with 265
true results and `git diff --check` passed. Commit `e082865` pushed to GitHub
`main`.

2026-07-22 08:30 progress: checked chamber-tick results now expose one
PeTTa-native `chamber-tick-result-outcome` query. Tick-loop consumers receive
`productive`, `no-op`, or the exact invalid boundary without duplicating
validity/change branching in host glue. Exp00 passed with 263 true results and
`git diff --check` passed. Commit `41d0fc0` pushed to GitHub `main`.

2026-07-22 06:30 progress: checked chamber-tick results now expose a direct
PeTTa-native `chamber-tick-result-changed?` query. Exp00 distinguishes a valid
productive tick from valid cap-zero and invalid fail-closed no-ops; exp00
passed with 259 true results and `git diff --check` passed. Commit `80b4923`
pushed to GitHub `main`.

2026-07-22 04:30 progress: checked live chamber-tick results now expose a
direct PeTTa-native boolean `chamber-tick-result-valid?` query. Focused valid
and malformed-over-cap tests passed; exp00 passed with 256 true results and
`git diff --check` passed. Commit `c5f6502` pushed to GitHub `main`.

2026-07-22 02:30 progress: live checked chamber-tick results now expose their
`valid` or first-failed-boundary disposition through a PeTTa-native
`chamber-tick-result-validity` accessor. Focused valid and malformed-over-cap
tests passed; exp00 passed with 254 true results and `git diff --check` passed.
Commit `8140999` pushed to GitHub `main`.

2026-07-22 00:30 progress: live generated chamber ticks now expose a
PeTTa-native `chamber-tick-result` carrying the complete validity disposition
beside the projected chamber. The established chamber-only API is an exact
projection of that checked result; valid chemistry is unchanged and malformed
provenance still fails closed. Exp00 passed with 252 true results and
`git diff --check` passed. Commit `f98be89` pushed to GitHub `main`.

2026-07-21 22:30 progress: exp00 now directly verifies every complete
chamber-tick provenance disposition: `valid`, `invalid-attrition`,
`invalid-bounds`, `invalid-generation`, `invalid-selection`, and
`invalid-firing`. The malformed fixtures also preserve the documented
first-failure precedence. Chemistry and checked ticking are unchanged. Exp00
passed with 250 true results and `git diff --check` passed.
Commit `16c8707` pushed to GitHub `main`.

2026-07-21 20:30 progress: complete chamber-tick provenance now attributes
validity to `valid` or the first failed accounting, bounds, generation,
selection, or firing boundary. Checked chamber ticking consumes that
PeTTa-native disposition and retains fail-closed behavior. Exp00 passed with
246 true results and `git diff --check` passed. Commit `e3cd363` pushed to
GitHub `main`.

2026-07-21 18:30 progress: reordered equal-width generated provenance now
fails closed through the complete validity gate and the chamber-tick
projection, not only the generation-specific predicate. Exp00 passed with 244
true results and `git diff --check` passed.
Commit `ad56a61` pushed to GitHub `main`.

2026-07-21 16:30 progress: complete chamber-tick provenance now validates
the exact generated candidate pool against the input chamber's stable
source-rule prefix. An internally consistent equal-width reordered pool is
rejected before it can claim chamber provenance. Exp00 passed with 241
results and `git diff --check` passed. Commit `8315c43` pushed to GitHub
`main`.

2026-07-21 14:30 progress: complete chamber-tick provenance now validates
the fired output chamber against the input chamber, generated pool envelope,
and deterministic selected candidate. A record with correct generation and
selection but a forged output chamber fails closed without mutation. Exp00
passed with 241 results and `git diff --check` passed. Commit `6f2a64c`
pushed to GitHub `main`.

2026-07-21 12:30 progress: complete chamber-tick provenance now validates
the exact bounded pool and deterministic selection against its generated
source, normalized cap, and input chamber. A forged equal-cardinality pool
fails closed without mutating the chamber; ordinary productive ticking is
unchanged. Exp00 passed with 238 results and `git diff --check` passed.
Implementation commit `f86e7dc`.

2026-07-21 10:30 progress: generated chamber ticking now projects through
the complete PeTTa-native provenance validity gate. A malformed over-cap
record fails closed to the input chamber, while ordinary live generation,
bounded deterministic selection, and productive firing retain the same
transition. Exp00 passed with 235 results and `git diff --check` passed.
Commit `c2f8204` pushed to GitHub `main`.

2026-07-21 08:30 progress: complete live PeTTa-native chamber-tick
provenance now exposes `generated-selection-fire-record-valid?`, combining
source/stage attrition validity with the fixed generation boundary, normalized
per-tick selection boundary, and embedded scalar-cap agreement. Exp00 rejects
a synthetic conservation-valid record whose three-candidate bounded pool
exceeds its effective cap of two. Generation, selection, firing, and chemistry
are unchanged. Exp00 passed with 233 results and `git diff --check` passed.
Commit `4f617d4` pushed to GitHub `main`.

2026-07-21 06:30 progress: complete live PeTTa-native
generation/selection/fire provenance now exposes a direct
`generated-selection-fire-record-attrition-valid?` gate. Ordinary cap-2 and
closed cap-0 chamber paths both validate without host-side summary
materialization. Generation, deterministic selection, firing, and chemistry
are unchanged. Exp00 passed with 229 results and `git diff --check` passed.
Commit `196b097` pushed to GitHub `main`.

2026-07-21 04:30 progress: compact PeTTa-native `candidate-attrition`
provenance now rejects impossible negative cardinalities even when their
conservation equations and stage attribution agree. The complete
`candidate-attrition-valid?` gate now requires nonnegative counts,
conservation, and stage consistency. Generation, deterministic selection,
firing, and chemistry are unchanged. Exp00 passed with 227 results and
`git diff --check` passed. Commit `fd9fc71` pushed to GitHub `main`.

2026-07-21 02:30 progress: compact PeTTa-native `candidate-attrition`
provenance now exposes one complete `candidate-attrition-valid?` gate that
requires both conservation accounting and stage attribution to agree. Exp00
covers live provenance plus independently malformed arithmetic and stage
records. Generation, deterministic selection, firing, and chemistry are
unchanged. Exp00 passed with 224 results and `git diff --check` passed.
Commit `52b8945` pushed to GitHub `main`.

2026-07-21 00:30 progress: compact PeTTa-native `candidate-attrition`
provenance now validates that its attributed `none`, `generation`,
`selection`, or `both` stage agrees with the two stage-specific omission
counts. Exp00 covers every valid label and rejects a count-consistent record
with a misleading label. Generation, deterministic selection, firing, and
chemistry are unchanged. Exp00 passed with 220 results and `git diff --check`
passed. Commit `edd8d6e` pushed to GitHub `main`.

2026-07-20 22:30 progress: compact PeTTa-native `candidate-attrition`
provenance now validates its source-to-generated, generated-to-bounded, and
source-to-bounded conservation identities directly via
`candidate-attrition-consistent?`. Exp00 covers live ordinary provenance, the
supported twelve-rule boundary, and a deliberately inconsistent rejection.
Generation, deterministic selection, firing, and chemistry are unchanged.
Exp00 passed with 216 true results and `git diff --check` passed.
Commit `201febf` pushed to GitHub `main`.

2026-07-20 20:30 progress: the compact PeTTa-native
`candidate-attrition` audit atom now has direct accessors for all seven
fields: source, generated, and bounded counts; generation, selection, and
total omissions; and attributed stage. Downstream persistence/report code no
longer needs host-side positional destructuring. Generation, selection,
firing, and chemistry are unchanged. Exp00 passed with 213 true results and
`git diff --check` passed. Commit `bf65490` pushed to GitHub `main`.

2026-07-20 18:30 progress: complete PeTTa-native generation/selection/fire
provenance now emits one `candidate-attrition` summary carrying source,
generated, and bounded counts; generation, selection, and total omissions;
and the attributed loss stage. Exp00 covers preserved and selection-truncated
ordinary fixtures. Chemistry and deterministic ticking are unchanged. Exp00
(206 true results) and `git diff --check` pass.
Commit `2a9f71d` pushed to GitHub `main`.

2026-07-20 16:30 progress: complete PeTTa-native generation/selection/fire
provenance now attributes source attrition to `none`, `generation`,
`selection`, or `both`. Exp00 covers all four cases across the ordinary
three-rule fixture and supported twelve-rule generator boundary. Candidate
generation, deterministic selection, firing, and chemistry are unchanged.
Exp00 (204 true results) and `git diff --check` pass.

2026-07-20 12:30 maintenance: reconciled two stale open task records with
completed, tested work. The exp07 diagnostic family is complete through the
frozen dual-bootstrap negative result and bounded `applicability-loss`
mechanism audit; the exp06 three-tick stateful candidate-cap sweep and ACS
boundary check were already completed on July 10. `emergence-claim none`
remains. No chemistry, trajectory, or scientific result changed. Exp00 (200
true results) and `git diff --check` pass.

2026-07-20 10:30 progress: complete PeTTa-native generation/selection/fire
provenance now directly classifies total source retention. A three-rule source
under cap 3 reports `preserved`; the supported twelve-rule source at the
eight-candidate generator boundary reports `truncated`. Deterministic firing
and chemistry are unchanged. Exp00 (200 true results) and `git diff --check`
pass. Commit `6c79443` pushed to GitHub `main`.

2026-07-20 08:30 progress: complete PeTTa-native generation/selection/fire
provenance now exposes total source-to-bounded-pool attrition. The ordinary
three-rule fixture under cap 2 reports one omitted candidate; the supported
twelve-rule fixture reports ten (four at generation and six at selection).
Deterministic firing and chemistry are unchanged. Exp00 (198 true results)
and `git diff --check` pass. Commit `93b8bfc`.

2026-07-20 06:30 progress: bounded-generator capacity is now directly
classified from complete PeTTa-native generation/selection/fire provenance.
The ordinary three-rule fixture reports `open`, while the supported
twelve-rule fixture at the eight-candidate boundary reports `saturated`.
Selection-stage caps, deterministic firing, and chemistry are unchanged.
Exp00 (196 true results) and `git diff --check` pass.
Commit `538255d` pushed to GitHub `main`.

2026-07-20 04:30 progress: unused generator capacity is now directly
queryable from complete PeTTa-native generation/selection/fire provenance.
The ordinary three-rule complete fixture reports five remaining slots under
the stable cap 8, while the twelve-rule truncated fixture reports zero.
Selection-stage caps, deterministic firing, and chemistry are unchanged.
Exp00 (194 true results) and `git diff --check` pass.
Commit `96ad214` pushed to GitHub `main`.

2026-07-20 02:30 progress: the stable bounded-generation limit is now
directly queryable from complete PeTTa-native generation/selection/fire
provenance. Both the ordinary three-rule complete fixture and the twelve-rule
truncated fixture report generation cap 8. Selection-stage caps,
deterministic firing, and chemistry are unchanged. Exp00 (192 true results)
and `git diff --check` pass. Commit `017f9d5` pushed to GitHub `main`.

2026-07-20 00:30 progress: bounded-generation provenance now directly labels
the generator stage `complete` or `truncated`. The ordinary three-rule fixture
is complete, while the supported twelve-rule fixture is truncated at the
stable eight-candidate boundary. Selection-stage caps, deterministic firing,
and chemistry are unchanged. Exp00 (190 true results) and `git diff --check`
pass. Commit `ebcc70d` pushed to GitHub `main`.

2026-07-19 22:30 progress: bounded generation provenance now distinguishes
the chamber source width from the generated pool width. PeTTa-native accessors
report 3 source rules and 0 generation omissions for the ordinary fixture,
and 4 omissions when the supported twelve-rule fixture reaches the stable
eight-candidate generator boundary. Selection-stage dropped counts and
chemistry are unchanged. Exp00 (188 true results) and `git diff --check` pass.
Commit `2bb805e` pushed to GitHub `main`.

2026-07-19 20:30 progress: complete PeTTa-native generated-selection/fire
provenance now exposes the exact number of candidates dropped by the effective
cap. The three-rule fixture reports one dropped under cap 2, none under cap 3,
and all three under a nonpositive request. Selection, firing, and chemistry
are unchanged. Exp00 (185 true results) and `git diff --check` pass.
Commit `57bd83c` pushed to GitHub `main`.

2026-07-19 18:30 progress: complete PeTTa-native generated-selection/fire
provenance now exposes generated and bounded candidate counts. The three-rule
fixture reports 3 generated versus 2 selectable under cap 2, 3 versus 3 under
cap 3, and a nonpositive request reports bounded count 0. Selection, firing,
and chemistry are unchanged. Exp00 (182 true results) and `git diff --check`
pass. Commit `a9093ac` pushed to GitHub `main`.

2026-07-19 16:30 progress: complete PeTTa-native generated-selection/fire
provenance now reports whether the effective candidate cap `preserved` or
`truncated` the generated pool. Focused smoke covers a three-rule pool under
caps 2 and 3; deterministic selection, firing, and chemistry are unchanged.
Exp00 (178 true results) and `git diff --check` pass. Commit `964b36a` pushed
to GitHub `main`.

2026-07-19 14:30 progress: added PeTTa-native scalar accessors for the
requested and effective per-tick/per-rule fields carried by complete
generated-selection/fire provenance. An oversized request `(9 3)` is directly
queryable beside its normalized `(8 1)` boundary without changing generation,
selection, or chemistry. Exp00 (176 true results) and `git diff --check` pass.
Commit `4604599` pushed to GitHub `main`.

2026-07-19 12:30 progress: completed nonpositive per-tick request audit
coverage across the full PeTTa-native generation/selection/fire record.
Requested caps `(-1 1)` and `(0 3)` remain visible, expose effective `(0 0)`,
and leave the chamber unchanged. No selector, generator, or chemistry changed.
Exp00 (172 true results) and `git diff --check` pass. Commit `c9dae0c`
pushed to GitHub `main`.

2026-07-19 10:30 progress: completed the positive per-rule normalization
boundary. Requested `(2 3)` remains visible in complete generated-selection/
fire provenance, exposes effective `(2 1)` under the one-candidate-per-source
contract, and produces the same deterministic chamber tick as `(2 1)`. No
selector, generator, or chemistry changed. Exp00 (168 true results) and
`git diff --check` pass. Commit `93ea3d4` pushed to GitHub `main`.

2026-07-19 08:30 progress: completed the symmetric malformed-cap boundary
for a positive per-tick and negative per-rule request. Requested `(2 -1)` is
retained in generated-selection/fire audit provenance, exposes effective
`(0 0)`, and leaves the chamber unchanged. No selector or chemistry changed.
Exp00 (165 true results) and `git diff --check` pass. Commit `4013acf`
pushed to GitHub `main`.

2026-07-19 06:30 progress: effective candidate-cap normalization now closes
both fields when the per-tick boundary is nonpositive. Requested caps `(-1 1)`
and `(0 3)` both expose effective `(0 0)` rather than retaining a misleading
positive per-rule allowance. Selection and chamber chemistry are unchanged.
Exp00 (162 true results) and `git diff --check` pass.
Commit `d744596` pushed to GitHub `main`.

2026-07-19 04:30 progress: the PeTTa-native generated-selection/fire record
now exposes the complete effective `candidate-cap`. A requested cap `(9 3)`
normalizes to the supported `(8 1)`, while `(2 0)` closes to `(0 0)`; requested
cap provenance, deterministic selection, and chamber chemistry are unchanged.
Exp00 (160 true results) and `git diff --check` pass.
Commit `1df98e4` pushed to GitHub `main`.

2026-07-19 02:30 progress: the complete PeTTa-native generated-selection/fire
record now preserves the originally requested `candidate-cap` beside the
effective bounded scalar. Smoke coverage distinguishes requested cap 9 from
effective cap 8 and retains a requested per-rule-zero cap even though it
closes selection at effective cap 0. Deterministic selection, generated pools,
and chamber chemistry are unchanged. Exp00 (157) and `git diff --check` pass.
Commit `e26c74a` pushed to GitHub `main`.

2026-07-19 00:30 progress: added PeTTa-native query accessors for the
effective candidate cap carried by both bounded selection records and the
complete generated-selection/fire provenance chain. Smoke coverage proves an
ordinary cap 2 remains visible and an oversized requested cap 9 is recorded
as the supported effective cap 8 before deterministic selection and chamber
ticking. Chemistry and trajectories are unchanged. Exp00 and
`git diff --check` pass; commit `fcde7b5` pushed to GitHub `main`.

2026-07-18 20:30 progress: completed the frozen dual-mechanism audit
serialization. PeTTa now reports 32-seed medians for all six first-prefix and
five first-food-exhaustion ticks in every arm, plus seed-paired
weak-minus-unguided food-exhaustion and reset-depth differences. Sentinel 99
remains uncensored. The fixed precedence still assigns `applicability-loss`
from 51 weak versus 38 unguided blocked first-absent selections. Exp00, exp07,
the dual report, detector invariance, and `git diff --check` pass. No
chemistry, trajectory, registered result, or emergence claim changed.
Commit `a57f4e0` pushed to GitHub `main`.

2026-07-18 18:30 progress: extended the frozen dual-mechanism audit with
food/reset and paired-prefix provenance derived entirely from the validated
PeTTa trace. Each arm/seed now exposes first exhaustion ticks for A--E and
counts scheduled resets reached at prefix depths 0--5; a paired table records
weak-minus-unguided first-prefix-tick and depth-occupancy differences for all
32 seeds. No chemistry, selector, seed, tick, trajectory, or interpretation
changed; `applicability-loss` remains decisive and emergence claim remains
none. Exp00, exp07, detector invariance, and `git diff --check` pass. Median
serialization and paired food/reset differences remain. Commit `a481dbc`
pushed to GitHub `main`.

2026-07-18 16:30 progress: added the next frozen dual-mechanism audit slice
directly over the validated PeTTa trace. Each arm/seed now exposes first ticks
for all six ordered pathway prefixes (99 if absent) and exact tick occupancy at
depths 0--6; every occupancy row is constrained to the frozen 32 ticks and the
report query serializes all three arms. No chemistry, selector, trajectory, or
interpretation changed; `applicability-loss` remains the decisive label and
emergence claim remains none. Food/reset, median, and paired summaries remain.
Exp00, exp07, detector invariance, and `git diff --check` pass; commit
`f839b27` pushed to GitHub `main`.

2026-07-18 14:30 progress: derived the first frozen dual-mechanism aggregates
directly from the validated PeTTa trace. Rule-level selected/fired and
first-absent selected/fired counts now cover all twelve identities, with
blocked selections partitioned by pathway/distractor. Weak guidance had 51
blocked first-absent selections versus 38 unguided, so the preregistered
precedence assigns `applicability-loss`; later interpretation branches are not
consulted. Exp00, exp07, detector invariance, and `git diff --check` pass.
Commit `ec04352` pushed to GitHub `main`. Remaining frozen prefix/resource
summaries still need serialization; the negative result and emergence claim
none are unchanged.

2026-07-18 12:30 progress: implemented the frozen dual-bootstrap mechanism
audit's PeTTa-native trace and fail-closed integrity gate without computing
any new mechanism aggregate. Every row is derived from the reset-prepared
pre-fire chamber and exact selected candidate, recording the registered key,
selection/applicability/firing, frontier, six product bits, and five food
abundances. Sequential key validation proves exactly 32 unique ticks for each
of 96 trajectories; RAF/event/persistence/diversity/replay totals reproduce
13/9/0, 549/523/396, 95/51/0, 336/278/219, and 32/32/32. Exp00 (154), exp07
(305), detector invariance, and `git diff --check` pass. No mechanism label or
new scientific outcome was inspected; the negative guided-uplift result and
emergence claim none remain unchanged. Commit `65cab25` pushed to GitHub
`main`.

2026-07-18 10:30 progress: selected a bounded mechanism audit, rather than a
new emergence experiment, as the next scientific objective. Froze
`experiments/exp07/PREREG_DUAL_MECHANISM_AUDIT.md` before implementing any new
derived diagnostic. It reuses only the completed seed-201--232 trajectories,
fixes tick-level trace fields, paired summaries, integrity gates, and a
descriptive interpretation precedence, and cannot rescue or reinterpret the
negative dual-bootstrap result. Baseline exp00 (154) passes; no chemistry,
seed support, trajectory, or new outcome was added; emergence claim remains
none.

2026-07-18 08:30 progress: formally closed the dual-bootstrap program as a
preregistered negative result without extending seeds, ticks, chemistry,
selector, or endpoints. The frozen matrix remains 13/32 unguided, 9/32 weak
Doob-h, and 0/32 shuffled; structural necessity of the six-step pathway does
not establish guidance causality because guiding-term removal retains 13/32.
Repository README and durable project records now agree with the completed
protocol/report. No successor outcome implementation is authorized until a
new scientific objective and protocol are chosen and preregistered. Exp00
(154) and `git diff --check` pass; commit `56fda93` pushed to GitHub `main`;
spontaneous-emergence claim remains none.

2026-07-18 06:30 progress: executed the frozen dual-bootstrap matrix exactly
once over seeds 201--232 and ticks 3--34 after all fail-closed gates passed.
Rolling four-rule RAF incidence was 13/32 unguided, 9/32 weak Doob-h, and 0/32
shuffled, so weak underperformed unguided and missed the required ten-seed
advantage. All 96 trajectories replayed; persistence totals were 95/51/0,
productive events 549/523/396, and rule diversity 336/278/219. Either
bootstrap, the full four-edge cycle catalyst set, or any individual cycle rule
ablated weak incidence to zero, but guiding-term removal retained unguided
13/32. The registered guided causal uplift result is negative; no extension
and no spontaneous-emergence claim. Checks: exp00 (154), exp07 (302),
detector invariance, runnable full report, and `git diff --check`.
Commit `48af89b` pushed to GitHub `main`.

2026-07-18 04:30 progress: closed every fail-closed dual-bootstrap pre-run
gate without adding seed-201--232 support or constructing a registered
trajectory. PeTTa materializes the frozen seventeen-species/twelve-rule
chemistry and twelve explicit catalysis edges; the initial state derives only
`db0` and its exposed distractors applicable and remains RAF-negative.
Canonical and frozen-permuted sources produce the same identity-addressed cap
8 in all three distractor phases. Exhaustive synthetic calibration covers all
six frontier identities crossed with all three phases and realizes the frozen
20/4/12 weak and 4/20/12 shuffled masses at matched eight-unit cost. All arms
share one pool, and a nonregistered seed-7 identity selection ticks `db0`
through the ordinary chamber path. Checks: exp00 (153), exp07 (270), detector
invariance, and `git diff --check`. No successor outcome was evaluated;
commit `6b3fc76` pushed to GitHub `main`; spontaneous-emergence claim remains
none.

2026-07-18 02:30 progress: closed the ordered-replication program as two
distinct preregistered negative gates and froze the next chemistry before any
new outcome implementation. Cohort A remains a failed primary replication;
cohort B remains a failed order/hash robustness gate because unguided incidence
survived guiding-term removal, and cannot rescue cohort A. The design-only
dual-bootstrap successor fixes a six-step pathway, four-rule RAF, twelve-rule
source, order-invariant identity-addressed cap 8, fresh seeds 201--232, ticks
3--34, matched-cost controls, causal thresholds, and direct bounded ticking.
No successor seed support, generator, selector, trajectory, or outcome exists.
Checks: exp00 (153), exp07 (252), detector invariance, and `git diff --check`.
Commit `06c0f3c` pushed to GitHub `main`; spontaneous-emergence claim remains
none.

2026-07-18 00:30 progress: executed and fully reported frozen cohort B exactly
once over seeds 117--132 and ticks 3--26 using the preregistered permuted pool
and draw hash. RAF incidence was 8/16 unguided, 16/16 weak Doob-h, and 0/16
shuffled. Although weak cleared the four-seed incidence advantage over both
controls, guiding-term removal retained unguided 8/16, violating the maximum
of two; order/hash robustness is not supported and cannot rescue cohort A's
failed primary replication. All 48 trajectories replayed; persistence totals
were 33/145/0, productive events 281/275/260, and distinct-rule totals
120/127/92 of 128. Structural ablations were all 0/16, matched guidance cost
was 3,072 per guided arm, no seeds/ticks were added, and emergence claim
remains none. Checks: exp00 (153), exp07 (250), detector invariance, and
`git diff --check`. Commit `836ac36` pushed to GitHub `main`.

2026-07-17 22:30 progress: executed and fully reported the frozen cohort-A
exact-form replication over exactly seeds 101--116 and ticks 3--26. RAF
incidence was 1/16 unguided, 4/16 weak Doob-h, and 0/16 shuffled, so weak
missed the preregistered six-seed advantage over both controls and primary
replication is not supported. All 48 trajectories replayed; persistence was
1/15/0, productive events 259/263/250, and distinct-rule totals 112/116/85 of
128. Matched-cost and every causal gate passed (structural ablations 0/16;
guiding-term removal 1/16). Cohort B remains unevaluated and cannot rescue the
failed primary result. No seeds or ticks were added; spontaneous-emergence
claim remains none.
Checks: exp00 (153), exp07 (248), detector invariance, and
`git diff --check`. Commit `1f237df` pushed to GitHub `main`.

2026-07-17 20:30 progress: closed the independent ordered-replication
fail-closed implementation gate without constructing a registered
seed-101--132 trajectory. PeTTa now supports all frozen seeds, calibrates each
new draw hash as a full 96-bin permutation, generates identical arm pools for
both cohorts, and attaches cohort-B selector mass to rule identity across the
permuted pool and all four frontier phases. Derived selector masses retain the
matched eight-unit guidance cost. A nonregistered seed-7 fixture selects
`ob0` by identity from cohort B's third pool position and feeds it directly to
ordinary chamber ticking. Initial applicability/RAF negativity remain covered
by the predecessor gate. Checks: exp00 (153), exp07 (246), exp04 detector
invariance, and `git diff --check`. No replication endpoint was evaluated;
spontaneous-emergence claim remains none. Commit `0c078d2` pushed to GitHub
`main`.

2026-07-17 18:30 progress: froze an independent two-cohort replication and
robustness protocol before adding any new seed support, selector, trajectory,
or outcome. Cohort A uses fresh seeds 101--116 and a new fixed draw hash for
exact-form replication; cohort B holds out seeds 117--132, changes the draw
hash, and permutes the cap-8 pool while requiring rule-identity-based frontier
selection. Both retain ticks 3--26, matched unguided/weak/shuffled arms,
equal-cost guidance, replay, and the complete causal ablation gate. Fixed
incidence-advantage and ablation thresholds prevent post-outcome reinterpretation.
The PeTTa design-only contract passes exp07 smoke; no replication endpoint was
evaluated and spontaneous-emergence claim remains none. Commit `07fed0d`
pushed to GitHub `main` after exp00 (153), exp07 (225), and
`git diff --check` passed.

2026-07-17 16:30 correction and completion: a secondary-endpoint audit found
that the frozen ordered-bootstrap report had accidentally reused the historical
rich-pool `rp0/rp1/rp2` rolling detector instead of its preregistered
`op1/op2/op0` detector. With the detector wired correctly and the exact same
seeds 19--26, ticks 3--26, draws, pool, and schedule, incidence is 0/8
unguided, 6/8 weak Doob-h, and 0/8 shuffled; weak first hits are
`[99,12,15,14,99,19,19,18]`. Persistence totals are 0/41/0 and distinct-rule
totals are 42/59/39 of 64. All 24 trajectories replay. Removing the guiding
term, `ob0`, all three cycle catalyst edges, or any individual `op1/op2/op0`
rule collapses weak incidence to 0/8. This meets the preregistered bounded
guided causal RAF-uplift condition; it is not spontaneous emergence. Checks:
exp00, exp07, detector invariance, and `git diff --check`.
Commit `7e1e677` pushed to GitHub `main`.

2026-07-17 14:30 progress: passed the complete ordered-bootstrap fail-closed
gate, including the standing exp04 detector-invariance control, then executed
the frozen three-arm seed-19--26 matrix exactly once over ticks 3--26. All
three arms were rolling-RAF-null (0/8; every first-hit sentinel 99), while
productive-event totals were 103 unguided, 119 weak Doob-h, and 104 shuffled;
all 24 trajectories replay exactly. The run exposed a PeTTa imported-equation
compiler boundary that had left the generic named-chamber generator/cap path
irreducible; exp07 now has executable local cap-8 generation, applicability,
and firing clauses mirroring the exp00 contracts, and exp00's generic bounded
pool no longer relies on the faulty intermediate `let`. No seeds or ticks were
added and `emergence-claim none`. Checks: exp00 (153), exp07 (222), detector
invariance, and `git diff --check`.

2026-07-17 12:33 progress: closed the remaining ordered-bootstrap fail-closed
selector gates without constructing a seed-19--26 trajectory. The shared
PeTTa named-molecule kernel now supports the frozen twelve-species state;
initial `ob0` applicability and `op1/op2/op0` inapplicability are derived from
abundances, and the empty event history is RAF-negative under an event-derived
three-rule check. All four `AB/AC/CD` frontier phases are unit-tested. Complete
96-bin calibration realizes unguided masses `(12x8)`, weak phase masses
`20/4/12x6`, and the exactly reversed shuffled control at matched eight-unit
cost. A synthetic draw selects `ob0` from the generated bounded cap-8 pool and
feeds it directly to ordinary chamber ticking, producing the expected event
and abundance transition. No registered trajectory or endpoint was evaluated;
`emergence-claim none`. Checks: exp00 (153), exp07 (217), and
`git diff --check`.

2026-07-17 10:33 progress: completed the first ordered-bootstrap pre-run
materialization slice without selecting or ticking any held-out chamber. PeTTa
now constructs the frozen twelve-species initial state and exact ordered
`ob0/op1/op2/op0/od0/od1/od2/od3` cap-8 candidate pool through the shared
exp00 generator for every arm. Eight `(catalyzes Molecule RuleId)` atoms are
materialized in the Atomspace and queried closed-world, with negative checks
guarding against name-based inference. No selector, seed-19--26 trajectory, or
RAF endpoint was evaluated; `emergence-claim none`. Checks: exp00 (153), exp07
(197), and `git diff --check`. Commit `986c489` pushed to GitHub `main`.

2026-07-17 08:34 progress: closed the frozen exp07 rich-pool experiment as
pool-composition evidence and preregistered its ordered-bootstrap successor
without constructing or inspecting a new trajectory. The prior cycle is
structurally necessary under catalyst/rule ablation, but guidance is not:
unguided and shuffled controls remain RAF-positive. The successor removes the
initial `CD` catalyst, uses a non-RAF `X`-catalyzed bootstrap rule to unlock the
ordered `op1 -> op2 -> op0` frontier, and freezes held-out seeds 19--26, ticks
3--26, cap 8, denominator 96, equal-cost state-aware/shuffled selectors, and
fail-closed pre-run gates. PeTTa exposes smoke-tested closure and
preregistration atoms; `emergence-claim none`. Checks: exp00 (153), exp07
(187), and `git diff --check`. Commit `65ef00a` pushed to GitHub `main`.

2026-07-17 06:30 progress: completed the frozen exp07 rich-pool causal
ablation gate without changing seeds, ticks, pool composition, selector, or
food schedule. PeTTa-native counterfactual ticks turn only a targeted
catalyst/rule draw into the registered blocked/no-event transition. Removing
guidance leaves unguided RAF incidence at 5/8, so guidance is not necessary.
Removing all three latent catalyst edges drives incidence to 0/8 in every arm;
individually removing `rp0`, `rp1`, or `rp2` also drives every arm to 0/8.
Catalyst-ablated productive-event totals are 116/83/117 for
unguided/weak/shuffled. The closure is structurally dependent on the planted
three-rule cycle but not specific to guidance; both controls remain positive
and `emergence-claim none`. Checks: exp00 (153), exp07 (185), and
`git diff --check`. Commit `9824ed1` pushed to GitHub `main`.

2026-07-17 04:30 progress: completed the frozen exp07 rich-pool
intervention-cost endpoint without adding seeds, ticks, or chemistry outcomes.
PeTTa computes the exact total-variation numerator directly from each arm's
calibrated 88-bin selector masses relative to unguided. Weak Doob-h and
shuffled guidance each shift 15/88 mass units per draw, or 360 over one
24-tick trajectory and 2,880 over each eight-trajectory arm; unguided cost is
zero. The matched cost budget confirms that outcome differences are not due to
different total guidance strength. Both controls remain RAF-positive, so
`emergence-claim none`. Checks: exp00 (154), exp07 (185), and
`git diff --check`. Prespecified guiding-term/catalyst/rule ablations remain.

2026-07-17 02:30 progress: completed the preregistered diversity-collapse
endpoint over the frozen exp07 rich-pool matrix without adding seeds or ticks.
PeTTa-native terminal event-history analysis counts which of the shared pool's
eight rule IDs fired at least once. Per-seed diversity vectors were
`[6,8,8,8,8,7,8,8]` unguided, `[8,7,6,8,8,8,8,8]` weak Doob-h, and
`[7,7,5,5,7,7,8,8]` shuffled, totaling 61/61/54 out of 64 possible
seed-rule presences; collapse deficits were 3/3/10. Weak guidance does not
reduce diversity relative to unguided, while shuffled guidance is less diverse.
Both controls remain RAF-positive, so `emergence-claim none`. Checks: exp00
(153), exp07 (176), and `git diff --check`. Intervention cost and causal
ablations remain next. Commit `5b436eb` pushed to GitHub `main`.

2026-07-17 00:30 progress: completed the preregistered rolling-condition
persistence endpoint over the already frozen exp07 rich-pool matrix, without
adding seeds or ticks. PeTTa-native tick-by-tick evaluation counts the longest
consecutive run for which the last eight productive events contain `rp0`,
`rp1`, and `rp2`, including blocked ticks whose unchanged window remains
positive. Per-arm totals were 13 unguided, 49 weak Doob-h, and 11 shuffled;
per-seed vectors were `[0,3,1,1,3,0,5,0]`, `[7,7,0,6,11,7,4,7]`, and
`[0,6,0,0,0,0,3,2]`. Both controls retain positive persistence, so
`emergence-claim none`. Checks: exp00 (153), exp07 (174), and
`git diff --check`. Commit `e72b7fe` pushed to GitHub `main`. Diversity, cost,
and causal ablations remain next.

2026-07-16 22:30 progress: executed the frozen exp07 rich-pool matrix exactly
once over all three arms, seeds 11--18, and ticks 3--26. PeTTa-native stateful
construction, tick-11/19 replenishment, blocked-tick advance, cap-8 selection,
and replay all pass. Rolling eight-event three-rule RAF incidence was 5/8
unguided, 7/8 weak Doob-h, and 3/8 shuffled; productive-event totals were
130/120/123. Both controls remain positive, so the preregistered uplift
condition is not satisfied and `emergence-claim none`. Persistence, diversity,
cost, and causal ablations remain next. Checks: exp00 (153), exp07 (174), and
`git diff --check`. Commit `41fb965` pushed to GitHub `main`.

2026-07-16 20:30 progress: closed every frozen exp07 rich-pool pre-run gate
without constructing a registered trajectory. A PeTTa-native event-history
detector reports the empty initial history RAF-negative, discriminates complete
and incomplete latent-cycle histories, and exposes a gate record binding the
eight catalysis facts, pool identity, calibrated masses, and direct tick path.
The canonical exp04 detector controls also pass. Checks: exp00 (153), exp07
(167), detector invariance, and `git diff --check`. Commit `3d347d7` pushed to
GitHub `main`; `emergence-claim none`.

2026-07-16 18:30 progress: calibrated the frozen exp07 rich-pool selector over
all synthetic draw bins 0--87 without constructing any registered outcome.
PeTTa-native exhaustive counts exactly realize the declared masses: unguided
`(11 11 11 11 11 11 11 11)`, weak Doob-h
`(16 16 16 8 8 8 8 8)`, and shuffled guidance
`(8 8 8 16 16 16 8 8)`. Exp07 now reports 163 passing assertions and
`git diff --check` passes. Commit `2d34083` was pushed to GitHub `main`.
Initial RAF-negativity and detector-control gates remain pending; no trajectory
or RAF outcome was evaluated and `emergence-claim none` remains.

2026-07-16 16:30 progress: materialized the frozen exp07 rich chamber as a
PeTTa-native thirteen-species/eight-rule state, extended named-molecule lookup
and reaction updates to that registered shape, and connected the denominator-88
arm selector through exact cap-8 generation to ordinary event-producing
chamber ticking. Eight explicit catalysis edges, shared-pool identity, selector
boundaries, bounded generation, and a productive seed-12 tick are covered. No
registered trajectory or RAF outcome was evaluated; sampler full-cycle,
initial-negativity, and detector-control gates remain pending, with
`emergence-claim none`. Checks: exp00 (153), exp07 (159), and
`git diff --check`. Commit `712fa17` pushed to GitHub `main`.

2026-07-16 14:30 progress: froze the exp07 all-arms-positive pivot before
implementing or inspecting any new outcomes. `PREREG_RICH_POOL.md` and matching
PeTTa smoke atoms specify one shared eight-rule cap-8 pool: a bootstrapped
latent three-rule RAF plus five productive food-competing distractors, explicit
first-class catalysis, seeds 11--18, a fixed 24-tick horizon, matched unguided /
weak Doob-h / shuffled arms, causal ablations, and fail-closed pre-run gates.
The implementation gate remains pending and `emergence-claim none`. Checks:
exp00 (153), exp07 (143), and `git diff --check`. Commit `e3bbc41` pushed to
GitHub `main`.

2026-07-16 12:30 progress: completed the frozen exp07 N=20 matrix without
peek-and-extend. All twelve PeTTa-native trajectories consumed ticks 3--22,
used identical food replenishment at ticks 8/13/18, replayed exactly, and
produced eight events per seed (32 per arm). Event-derived bounded RAF
incidence was 4/4 in unguided, weak Doob-h, and shuffled-guidance arms;
first-hit vectors were `[5,3,8,10]`, `[3,3,8,8]`, and `[5,3,4,3]`. This
triggers the preregistered all-arms-positive pivot: the shared two-rule pool,
not guidance, supports closure. Guiding-term removal does not collapse the
controls, so `emergence-claim none` remains. Checks: exp00 (153), exp07 (141),
and `git diff --check`. Commit `04d7b02` pushed to GitHub `main`.

2026-07-16 10:31 progress: passed the exp07 preregistration's mandatory
pre-run pool-identity gate without inspecting N=20 outcomes. The registered
longer-horizon arms now consume one exact shared PeTTa-native candidate-pool
constructor; only their categorical selection masses differ. The historical
pilot constructors remain unchanged as frozen evidence. Generic equality plus
seed-7/tick-3 and seed-10/tick-22 boundary smoke cover the registered horizon.
`emergence-claim none` remains unchanged. Checks: exp00 smoke (153), exp07
smoke (134), and `git diff --check`. Commit `05d6ea9` pushed to GitHub `main`.

2026-07-16 08:32 progress: added the PeTTa-native time/sustainment seam needed
before the frozen exp07 N=20 matrix can run. Blocked selections now advance one
tick without inventing an event, while a shared arm-independent preparation
step resets only food A/B/C to 2/1/1 immediately before ticks 8, 13, and 18,
preserving products, catalysts, rules, and history. Focused smoke covers the
three registered schedule points, a non-schedule tick, blocked advance, and a
productive replenished tick. No registered arm outcome was evaluated;
`emergence-claim none` is unchanged. Checks: exp00 smoke, exp07 smoke, and
`git diff --check`. Commit `3eb370e` pushed to GitHub `main`.

2026-07-16 08:25 progress: added the separately labelled seed-31 exp07
detector-invariance fixture without inspecting the registered experimental
arms. The canonical exp04 host detector and committed `chem_exp04.metta` facts
pass A -> no-catalysis B -> A call-order invariance, direct-versus-advanced
tick-history invariance, and committed PeTTa/host uniqueness and mutation
guards. Results remain RAF 15/core `{lCD,lBCD2}` for both positive evaluations
and RAF 0 for B. Checks: fixture gate, exp04 smoke (80 reported assertions),
exp07 smoke (129), Python compilation, and `git diff --check`. Run record:
`experiments/20260716T152520Z-exp07-detector-invariance/`. Boundary: detector
regression guard only; N=20, frozen seeds/endpoints, and `emergence-claim none`
are unchanged. Research Rules applied: 1, 2, 5, and 7.

2026-07-16 06:30 progress: completed the matched two-tick exp07 matrix across all three arms and fixed seeds 7-10. PeTTa-native ordinary chamber ticking gives productive-event vectors unguided `[1,2,1,2]`, weak Doob-h `[2,2,1,1]`, and shuffled guidance `[1,2,2,1]`; every arm totals 6 events and all 12 trajectories replay exactly. This is a two-tick aggregate null with different seed-level paths, not an ACS/RAF outcome or emergence result. Checks: `scripts/run_exp00.sh` (154 reported assertions), `scripts/run_exp07.sh` (128), `git diff --check`. Commit `28ddc28` pushed to GitHub `main`; `emergence-claim none`.

2026-07-16 04:30 progress: exp07 now has its first stateful matched trajectory. For weak Doob-h/seed-7, the PeTTa-native categorical policy selects `e5r0` at tick 3 and `e5r1` at tick 4; ordinary chamber ticking carries the mutated seven-molecule state forward, appends both events, and exhausts the shared A/B/C reactants exactly. The record preserves initial state, both per-tick selections, both chamber states, exact seed/tick replay provenance, and `emergence-claim none`. Checks: `scripts/run_exp00.sh` (153 reported assertions), `scripts/run_exp07.sh` (98), `git diff --check`. Commit `bc7f7de` pushed to GitHub `main`. This is trajectory plumbing, not an ACS/RAF outcome; the matched arms/seeds remain to be expanded.

2026-07-16 02:30 progress: the exp07 matched-fixture applicability gate now passes. A PeTTa-native named-molecule state and update seam gives every arm the same seven-molecule initial chemistry; all 24 candidates in the 12 two-candidate arm/seed pools are applicable, and all 12 selected draws produce ordinary chamber ticks. This removes the prior fixture confound and opens the stateful ensemble gate, but is not an ACS/RAF outcome. Checks: `scripts/run_exp00.sh` (153 reported assertions), `scripts/run_exp07.sh` (96), `git diff --check`. Commit `817dc42` pushed to GitHub `main`; `emergence-claim none`.

2026-07-16 00:30 progress: the exp07 matched-fixture applicability gate failed before stateful ensemble execution. A PeTTa-native total audit over all 12 arm/seed first draws found productive ordinary chamber ticks of unguided 0/4, weak Doob-h 3/4, and shuffled guidance 3/4. This is a fixture confound, not guidance uplift: the old exp05 four-molecule chambers contain only the reactants/catalyst for their original deterministic selection. The preregistered stateful outcome run is paused until a matched multi-molecule chamber applicability seam supports every reachable candidate in every arm. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (76), `git diff --check`. Commit `6f42e50` pushed to GitHub `main`; `emergence-claim none`.

2026-07-15 22:30 progress: calibrated the exp07 categorical sampler across a complete four-draw cycle before using it for stateful chemistry outcomes. PeTTa-native tick-parameterized pools and selection now cover ticks 3-6 for fixed seeds 7-10; the matched arms realize their declared first-candidate masses exactly: unguided 8/16, weak Doob-h 12/16, shuffled guidance 4/16. Checks: `scripts/run_exp00.sh`, `scripts/run_exp07.sh` (60 reported assertions), `git diff --check`. Commit `76d14eb` pushed to GitHub `main`. Boundary remains sampler calibration, not a stateful ACS/RAF ensemble or emergence claim.

2026-07-15 20:30 progress: opened the exp07 emergence-ensemble implementation with a replayable PeTTa-native weighted categorical sampler and an explicit matched three-arm contract: unguided 2/4, weak Doob-h 3/4, and shuffled-guidance 1/4 first-candidate mass over fixed seeds 7-10. The selected ordinary candidate is handed directly to exp00 chamber ticking; the contract preregisters the required ACS/RAF, timing, persistence, productivity, diversity, replay, cost, and ablation outcomes. This is a sampler/direct-tick gate only, with `emergence-claim none`; multi-tick ensemble outcomes remain next. Checks: `scripts/run_exp00.sh` (151 reported assertions), `scripts/run_exp07.sh` (53), `git diff --check`. Commit `2c564b2` pushed to GitHub `main`.

2026-07-15 19:22 progress: catalysis is now a first-class binary PeTTa relation for the exp04 RAF reference. Eighteen explicit `(catalyzes Molecule RuleId)` edges are independently queryable and drive PeTTa RA checks; the host maximal-RAF reference reads those materialized facts instead of reconstructing catalysis from structural containment. Empty-relation ablation uses the same pruning/core/dynamics path. Recorded gate `20260716T022154Z-first-class-catalysis-exp04` passed 79 PeTTa assertions, Python compilation, and `git diff --check`, reproducing maximal RAF 15, greedy core 2 (`lCD`, `lBCD2`), core RAF true, and ablation 0. This validates the seeded reference interface, not unseeded emergence.

2026-07-15 priority pivot: Ben directed the project to stop treating further source-list boundary extension as the main line and return immediately to ACS-emergence experiments. The twelve-rule/152-check checkpoint is sufficient infrastructure for the next scientific gate. Further kernel hardening is now demand-driven: undertake it only when an emergence experiment exposes a concrete blocker. The active question is whether weak, non-terminal-forcing exp07 guidance changes reproducible ACS/RAF incidence, persistence, productivity, or causal-ablation outcomes relative to matched unguided and shuffled controls.

2026-07-15 18:30 progress: extended bounded PeTTa-native candidate generation through the twelve-rule source-list boundary. The chamber retains all twelve source rules, generates the stable first-eight candidate prefix, recognizes an owned rewrite in the retained twelfth position, and completes cap-2 deterministic selection and ordinary chamber ticking. Checks: `scripts/run_exp00.sh` (152 checks), `git diff --check`. Commit `7061403` pushed to GitHub `main`.

2026-07-15 16:30 progress: extended bounded PeTTa-native candidate generation through the eleven-rule source-list boundary. The chamber retains all eleven source rules, generates the stable first-eight candidate prefix, recognizes an owned rewrite in the retained eleventh position, and completes cap-2 deterministic selection and ordinary chamber ticking. Checks: `scripts/run_exp00.sh` (149 checks), `git diff --check`. Commit `3353533` pushed to GitHub `main`.

2026-07-15 14:30 progress: extended bounded PeTTa-native generation through the next oversized source-list boundary. A ten-rule exp00 chamber now generates the stable first-eight candidate prefix, retains all ten source rules as chamber provenance, passes the matching ownership guard, and fires through cap-2 deterministic selection and ordinary chamber ticking. Checks: `scripts/run_exp00.sh` (146 checks), `git diff --check`. Commit `5ca80ee` pushed to GitHub `main`.

2026-07-15 12:30 progress: bounded PeTTa-native generation for the first oversized chamber rule-list boundary. A nine-rule exp00 chamber now deterministically generates the stable first-eight candidate prefix, retains all nine source rules as chamber provenance, applies a smaller cap, and fires through the ordinary selection-to-tick path instead of becoming irreducible. The ownership guard now recognizes the retained nine-rule chamber shape. Checks: `scripts/run_exp00.sh` (143 checks), `git diff --check`. Commit `9d95a7a` pushed to GitHub `main`.

2026-07-15 10:30 progress: made the direct PeTTa-native candidate-cap boundary total over oversized positive per-tick inputs. Because the base kernel explicitly supports generated pools through eight candidates, allowances above eight now clamp to effective cap eight while retaining the exact smaller generated pool, deterministic selection provenance, and ordinary chamber tick. Checks: `scripts/run_exp00.sh` (141 checks), `git diff --check`. Commit `02e5f15` pushed to GitHub `main`.

2026-07-15 08:32 progress: made candidate-cap bounds total over nonpositive inputs in the direct PeTTa-native generation -> selection -> chamber-tick path. A nonpositive per-tick or per-rule allowance now resolves to effective cap zero, an empty bounded pool, explicit `no-candidate` provenance, and an unchanged chamber instead of leaving negative caps irreducible. Checks: `scripts/run_exp00.sh` (137 checks), `git diff --check`. Commit `5b9c790` pushed to GitHub `main`.

2026-07-15 08:04 progress: aligned direct PeTTa-native bounded generation with the unified candidate-cap semantics. `bounded-candidate-pool` now applies the effective cap, so `(candidate-cap 2 0)` produces an empty bounded pool instead of exposing candidates that selection would later reject. Focused exp00 coverage verifies the direct boundary. Checks: `scripts/run_exp00.sh` (133 checks), `git diff --check`. Commit `638d8a4` pushed to GitHub `main`.

2026-07-13 18:30 progress: enforced the previously inert per-rule side of the PeTTa-native candidate cap at the unified bounded-selection boundary. Because generic generation emits at most one candidate per source rule, a zero per-rule allowance now yields an explicit `no-candidate` selection and unchanged chamber even when the per-tick allowance is positive. Checks: `scripts/run_exp00.sh` (133 checks), `scripts/run_exp05.sh`, `scripts/run_exp06.sh`, `scripts/run_exp07.sh`, `git diff --check`. Commit `11ea4e5` pushed to GitHub `main`.

2026-07-13 16:30 progress: tightened chamber ownership on the unified PeTTa-native deterministic candidate path. Externally scored candidates must now preserve a chamber source rule's stable ID, reactants, and product; catalyst reassignment remains allowed for exp05. A same-ID candidate with an altered rewrite remains visible in bounded-selection provenance but cannot mutate the chamber. Checks: `scripts/run_exp00.sh` (130 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Committed and pushed to GitHub `main` as `18ff8db`.

2026-07-13 14:30 progress: fixed event-history loss in the unified PeTTa-native chamber tick. Successful selected-candidate firing now appends its event to the chamber's existing bounded event list instead of replacing prior provenance; focused smoke covers a non-empty history. Checks: `scripts/run_exp00.sh` (128 checks), `git diff --check`. Commit `445df9c` pushed to GitHub `main`.

2026-07-13 12:30 progress: enforced candidate-pool envelope tick provenance in the unified PeTTa-native selection-to-tick path. A malformed external/scored pool whose own tick is stale cannot mutate the current chamber even when its selected candidate independently claims the current tick; complete bounded-selection provenance remains inspectable. Checks: `scripts/run_exp00.sh` (127 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `1ec8449` pushed to GitHub `main`.

2026-07-13 10:30 progress: added a chamber-ownership guard to the unified PeTTa-native selection-to-tick path. Externally supplied/scored candidates must now carry a rule identity present in the chamber before firing; foreign selections remain visible in provenance but leave the chamber unchanged. Membership uses stable rule IDs so exp05 catalyst reassignment remains compatible. Checks: `scripts/run_exp00.sh` (125 checks), `scripts/run_exp05.sh` (94), `scripts/run_exp06.sh` (61), `scripts/run_exp07.sh` (44), `git diff --check`. Commit `7d816b5` pushed to GitHub `main`.

2026-07-13 08:30 progress: made candidate applicability explicitly tick-scoped in the unified PeTTa-native selection-to-chamber path. A stale candidate from an earlier tick is now retained in bounded-selection provenance but cannot mutate a later chamber even when reactants and catalyst remain abundant. Focused coverage verifies both the applicability predicate and a direct provenance-backed pool tick returning the unchanged later chamber. Checks: `scripts/run_exp00.sh` (123 checks), `git diff --check`. Commit `e80974a` pushed to GitHub `main`.

2026-07-13 06:30 progress: connected the unified deterministic-selection path to PeTTa-native applicability guarding before chamber mutation. Selected candidates remain visible in provenance, but an inapplicable selected rule now leaves the chamber unchanged with no event instead of allowing negative abundance. Focused coverage exercises direct candidate ticking, selection/fire provenance, and generated cap-1 ticking on a starved chamber. Checks: `scripts/run_exp00.sh` (122 checks), `git diff --check`. Commit `6cf6e9f` pushed to GitHub `main`.

2026-07-13 04:30 progress: completed the generic PeTTa-native bounded candidate path for zero-cap and empty-source boundaries. Empty bounded lists now select explicit `no-candidate`; selection provenance is retained; chamber ticking returns the unchanged chamber without inventing an event. Four-molecule chambers with no rules generate an empty candidate pool, and empty pools remain empty under positive caps. Checks: `scripts/run_exp00.sh` (119 checks), `git diff --check`. Commit `ff58491` pushed to GitHub `main`.

2026-07-13 02:30 progress: collapsed all cap-specific candidate-pool and generated-tick compatibility operations (`-1` through `-8`) into aliases of the generic PeTTa-native provenance-backed paths. Capping, deterministic actual-cardinality selection, and firing now have one implementation while existing APIs remain available. Checks: `scripts/run_exp00.sh` (116 checks), `git diff --check`. Commit `4c45a5d` pushed to GitHub `main`.

2026-07-13 00:30 progress: removed duplicate PeTTa work from bounded candidate generation and cap-specific generated chamber ticks. `bounded-candidate-pool` now binds one generated pool for both tick provenance and capping; compatibility operations `chamber-tick-generated-1` through `-8` pass the raw generated pool downstream so capping occurs once before deterministic selection and firing. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`. Commit `c9fe6a4` pushed to GitHub `main`.

2026-07-12 22:30 progress: tightened the PeTTa-native generation-to-tick chain so each generated pool, bounded pool, and deterministic selection is bound exactly once before chamber firing, rather than reconstructed in parallel expressions. Added direct projections for the bounded pool and selected candidate from the complete generated record. Checks: `scripts/run_exp00.sh` (115 checks), `git diff --check`. Commit `5ecdacc` pushed to GitHub `main`.

2026-07-12 20:30 progress: extended the direct PeTTa-native generation-to-tick provenance chain with `generated-selection-fire-record-from-chamber`. It preserves the uncapped generated pool beside the exact bounded selection and chamber produced by firing that deterministic choice; generic `chamber-tick-generated` now projects from this complete chain. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `af49c98` pushed to GitHub `main`.

2026-07-12 18:30 progress: added PeTTa-native `selection-fire-record-from-pool`, retaining requested cap, exact bounded candidates, deterministic choice, and the chamber produced by firing that exact choice in one inspectable object. Generic `chamber-tick-candidate-pool` now projects from this combined record, tightening the direct deterministic-selection-to-tick connection. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `6fa9ced` pushed to GitHub `main`.

2026-07-12 16:30 progress: extended exp06’s PeTTa-native ACS boundary over the complete three-tick stateful cap trace. Every selected pair among ticks 3/4/5 is now checked for cap-1/cap-2, including the bounded no-op tick-5 selection after reactant exhaustion. Both arms remain rejected under pairwise product-catalyst closure; boundary remains diagnostic, not RAF enumeration, with no emergence claim. Checks: `scripts/run_exp06.sh` (61 checks), `scripts/run_exp00.sh`, `git diff --check`.

2026-07-12 14:30 progress: completed the PeTTa-native cap-as-maximum matrix for every non-empty source pool smaller than requested caps 2-8. Previously only cap-8 over three candidates was covered; shapes such as cap-7 over two candidates failed despite generic chamber-tick dispatch. Focused provenance coverage now proves cap-7 preserves a two-candidate external pool and deterministically selects by actual cardinality. Checks: `scripts/run_exp00.sh`, `git diff --check`. Commit `4ef39b9` pushed to GitHub `main`.

2026-07-12 12:30 progress: added PeTTa-native `candidate-selection-from-pool`, preserving requested cap, exact bounded candidate list, and deterministic selected candidate in one inspectable atom consumed directly by generic chamber ticking. Focused testing exposed and fixed a real bounded-cap omission: cap 8 now preserves a smaller three-candidate external pool instead of failing selection. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `8c68755` pushed to GitHub `main`.

2026-07-12 10:30 progress: exposed PeTTa-native `selected-candidate-from-pool` as the inspectable cap -> actual bounded cardinality -> deterministic seed/tick selection seam, and made generic `chamber-tick-candidate-pool` delegate through it before firing. Focused exp00 coverage proves exact selection for ordinary cap-2 and cap-8 over a smaller three-rule generated pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `e5b7502` pushed to GitHub `main`.

2026-07-12 08:30 progress: added generic PeTTa-native `chamber-tick-candidate-pool` and `chamber-tick-generated` operations that dispatch deterministic selection by the actual bounded pool cardinality (1-8), removing the need for callers to choose cap-specific tick functions. Focused exp00 coverage proves ordinary cap-2 equivalence and cap-8 safely ticking a smaller generated three-rule pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `4477baf` pushed to GitHub `main`.

2026-07-12 06:30 progress: completed base exp00 bounded candidate generation for every source-pool cardinality from one through eight rules by adding the missing five- and seven-rule clauses. Focused smoke verifies exact generated pools and a productive generated cap-5 tick through the direct cap -> deterministic selection -> firing path. Also corrected cap-1 smoke fixtures to the canonical two-field `candidate-cap` schema and a productive external pool. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`. Commit `511a63f` pushed to GitHub `main`.

2026-07-12 04:30 progress: completed direct candidate-pool-to-chamber-tick coverage for cap 1, closing the last cap-specific operation gap after caps 2-8. `chamber-tick-candidate-pool-1` and `chamber-tick-generated-1` now use the same PeTTa-native cap -> single-candidate selection -> firing path, with focused exp00 tests for external and generated pools. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

2026-07-12 02:30 progress: completed the bounded cap matrix used by direct candidate-pool chamber ticking. `cap-candidate-pool` now handles every pool size from the requested cap through eight candidates for caps 1-7, filling previously missing shapes such as cap-1 over eight candidates and cap-6 over seven. Exp00 adds focused boundary tests. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

2026-07-12 00:30 progress: generalized the direct PeTTa-native candidate-pool-to-chamber-tick operation from cap 2 to caps 3 through 8. `src/chem_exp00.metta` now exposes `chamber-tick-candidate-pool-3` through `-8`, and every generated cap-specific tick delegates through the same cap -> deterministic seed/tick selection -> firing path. Added the missing exact seven-candidate cap clause discovered by the new delegation and direct exp00 tests for cap-3/cap-6 pool ticking. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `git diff --check`.

2026-07-11 20:30 progress: broadened exp07 productive affinity selector provenance from eighteen to twenty seeds. Added seed-25/26 PeTTa fixtures spanning first/second candidate phases, bounded cap-2 deterministic selection, and direct ordinary exp00 chamber ticks with productive treatment/control catalysts. Boundary remains selector provenance only: no frequency/ACS uplift, terminal forcing, or emergence claim. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `git diff --check`.


2026-07-11 16:30 progress: broadened exp07's productive affinity seed-variation provenance from sixteen seeds to eighteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-23` and `seed-24`; `src/chem_exp05.metta` adds seed-23/tick-3 first-candidate treatment/control fixtures and seed-24/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: eighteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ca52b37` pushed to GitHub `main`.

2026-07-11 14:30 progress: broadened exp07's productive affinity seed-variation provenance from fourteen seeds to sixteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-21` and `seed-22`; `src/chem_exp05.metta` adds seed-21/tick-3 first-candidate treatment/control fixtures and seed-22/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: sixteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `23c236d` pushed to GitHub `main`.

2026-07-11 12:30 progress: broadened exp07's productive affinity seed-variation provenance from twelve seeds to fourteen while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-19` and `seed-20`; `src/chem_exp05.metta` adds seed-19/tick-3 first-candidate treatment/control fixtures and seed-20/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18/19/20. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: fourteen-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `2f13a3e` pushed to GitHub `main`.

2026-07-11 10:30 progress: broadened exp07's productive affinity seed-variation provenance from ten seeds to twelve while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-17` and `seed-18`; `src/chem_exp05.metta` adds seed-17/tick-3 first-candidate treatment/control fixtures and seed-18/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16/17/18. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: twelve-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, and `git diff --check`. Commit `ae74ea0` pushed to GitHub `main`.

2026-07-11 08:30 progress: broadened exp07's productive affinity seed-variation provenance from eight seeds to ten while preserving the PeTTa-native path from affinity-assigned candidate pools through cap-2 deterministic selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now defines `seed-15` and `seed-16`; `src/chem_exp05.metta` adds seed-15/tick-3 first-candidate treatment/control fixtures and seed-16/tick-3 second-candidate fixtures, all keeping selected catalysts present/productive; `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10/11/12/13/14/15/16. Exp05/exp07 smoke verifies selected candidates plus direct ordinary exp00 chamber ticks. Boundary: ten-seed selector-phase provenance only, no frequency/ACS-uplift claim, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp05.sh`, `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eb435e0` pushed to GitHub `main`.

2026-07-11 02:30 progress: broadened exp07's productive affinity seed-variation provenance from three seeds to four while preserving the direct PeTTa-native path from bounded affinity candidate generation/cap-2 selection into ordinary exp00 chamber ticking. `src/chem_exp00.metta` now names `seed-10`; `src/chem_exp05.metta` adds seed-10/tick-3 treatment/control fixtures whose cap-2 deterministic selector repeats the second-candidate phase (`e5r1`) with a distinct productive rotated-control catalyst (`BC`); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9/10. Exp05/exp07 smoke verifies selected candidates and ordinary exp00 chamber ticks. Boundary: four-seed selector-phase provenance only, no frequency claim, no ACS uplift, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `eabc1be` pushed to GitHub `main`.

2026-07-11 00:30 progress: broadened exp07's productive affinity seed-variation provenance from two seeds to three while keeping bounded candidate generation/caps and chamber ticking PeTTa-native. `src/chem_exp00.metta` now names `seed-9`; `src/chem_exp05.metta` adds seed-9/tick-3 treatment/control fixtures whose cap-2 deterministic selector repeats the first-candidate phase with different treatment/control catalyst contexts (`AC`/`BC`); `src/chem_exp07.metta` extends `exp07-affinity-seed-variation-row/table/status` to seeds 7/8/9. Smoke verifies selected candidates and ordinary exp00 chamber ticks for all three seeds. Boundary: three-seed selector-phase provenance only, no frequency claim, no ACS uplift, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `b34eae4` pushed to GitHub `main`.

2026-07-10 22:30 progress: added exp07's first two-seed productive affinity selector-phase variation while keeping the chamber path PeTTa-native. `src/chem_exp05.metta` now has matched seed-8/tick-3 treatment/control fixtures where cap-2 deterministic selection picks the second source rule (`e5r1`); `src/chem_exp07.metta` exposes `exp07-affinity-seed-variation-row`, `exp07-affinity-seed-variation-table`, and `exp07-affinity-seed-variation-status` covering seed-7 first-candidate and seed-8 second-candidate phases. Smoke tests verify selected candidates and ordinary exp00 chamber ticks for both treatment/control arms. Boundary: two-seed selector-phase provenance only, no frequency claim, no ACS uplift, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `358bfbc` pushed to GitHub `main`.

2026-07-10 20:30 progress: made exp07's productive affinity-strength path fully inspectable as a PeTTa-native selection-to-tick provenance trace. `src/chem_exp07.metta` now exposes `exp07-affinity-selection-to-tick-trace` and `exp07-affinity-selection-to-tick-status`, expanding the strength-1 seed-7/tick-3 cap-2 treatment/control pools, bounded cap lists, deterministic selected candidates, and ordinary exp00 chamber ticks. This directly connects bounded candidate generation/caps and deterministic selection to chamber ticking while preserving the boundary: single-fixture provenance only, no frequency claim, no ACS uplift, no terminal forcing, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `27e70fd` pushed to GitHub `main`.

2026-07-10 18:30 progress: added a PeTTa-native exp07 affinity-strength productivity-filter slice. `src/chem_exp07.metta` now exposes `exp07-affinity-strength-sweep-row`, `exp07-affinity-strength-sweep-table`, and `exp07-affinity-strength-sweep-status`, varying only exp05 affinity strength `(0 1 2)` in the existing seed-7/tick-3 cap-2 fixture. The slice records deterministic treatment/control selected candidates handed to chamber ticking and marks strength 1 as the only tested strength whose selected catalysts are present/productive in both arms; this is a fixture productivity filter before seed/frequency claims, not ACS uplift. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `d667c2b` pushed to GitHub `main`.

2026-07-10 16:30 progress: added a first PeTTa-native deterministic weak-guidance comparison table to exp07. `src/chem_exp07.metta` now exposes `exp07-weak-guidance-comparison-row`, `exp07-weak-guidance-comparison-table`, and `exp07-weak-guidance-comparison-status`: affinity weighting records observed treatment/control chamber-tick differences through exp05/exp00 selection, while candidate-pool cap records the exp06 stateful cap sweep plus ACS-boundary rejection. The boundary remains deterministic differences only, no terminal forcing, no ACS-positive result, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `6c64348` pushed to GitHub `main`.

2026-07-10 14:30 progress: linked exp07's Doob-h weak-guidance policy to existing PeTTa-native dynamic evidence. `src/chem_exp07.metta` now exposes `exp07-weak-guidance-evidence-row`, `exp07-weak-guidance-evidence-table`, and `exp07-weak-guidance-probe-status`: affinity weight is connected to exp05 treatment/control chamber ticking through the exp00 selector, and candidate-pool cap is connected to exp06's three-tick stateful cap sweep plus ACS-boundary table. The boundary remains no terminal forcing, no ACS-positive result, and `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `0fe6f81` pushed to GitHub `main`.

2026-07-10 12:30 progress: advanced exp07 from scaffold to a first PeTTa-native Doob-h diagnostic policy slice. `src/chem_exp07.metta` now exposes `exp07-doob-h-table`, ranked `exp07-doob-policy-order`, and `exp07-weak-guidance-test-plan`: catalyst assignment is the strongest terminal-fixture diagnostic; exp05 affinity weight and candidate-pool cap are weak-guidance variables to test without terminal forcing; basal replenishment and catalysis-map offset remain context/control variables. `experiments/exp07/smoke.metta` and README verify/document the policy while preserving `emergence-claim none`. Checks: `scripts/run_exp07.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `8bca457` pushed to GitHub `main`.

2026-07-10 11:00 progress: consolidated exp06 and staged the main pivot to exp07 Schrödinger-bridge/Doob-h-transform diagnostics. `src/chem_exp06.metta` now exposes `exp06-consolidation-summary`, recording that cap-1/cap-2 are rejected by two-rule product-catalyst closure across refreshed, stateful two-tick, and stateful three-tick sweeps; catalyst assignment remains the cost-1 shortest RAF-positive bridge row; basal-only is RAF-negative; catalysis-map offsets are offset-sensitive; and the consolidated boundary is `candidate-cap-route not-acs-positive` with `emergence-claim none`. Commit `06f7371` pushed to GitHub `main`.

The next main experiment family is exp07: a PeTTa-native diagnostic scaffold for Schrödinger-bridge/Doob-h-transform search inspired by Ben's "Let's Get Chemical" framing. It names exp02/exp04 no-catalysis controls as verified ACS-negative initial states, the exp04 ACS-rich fixture as terminal state (maximal RAF 15, greedy core 2, `(lCD lBCD2)`), and tracks intervention costs for catalyst assignment, basal-food replenishment, candidate-pool cap, catalysis-map offset, and exp05 affinity weight. Existing ACS scanners remain validation/control infrastructure; no emergence claim is made.

2026-07-10 10:30 progress: attached a PeTTa-native ACS boundary check to exp06's stateful candidate-cap sweep. `src/chem_exp06.metta` now compares the selected tick-3/tick-4 candidate rule pairs for two-rule product-catalyst closure via `exp06-selected-candidate-pair-acs-status`, exposes `exp06-stateful-cap-sweep-acs-boundary` rows for cap-1 and cap-2, and aggregates them in `exp06-stateful-cap-sweep-acs-boundary-table`. Both current cap arms are rejected by the closure check, so the candidate-cap intervention has dynamic bounded evidence but still no RAF/emergence claim. `experiments/exp06/smoke.metta` and README verify/document the boundary. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and targeted secret-like diff scan. Commit `40aef6b` pushed to GitHub `main`.

2026-07-10 08:30 progress: extended exp06's PeTTa-native stateful candidate-cap sweep from two selected ticks to three. `src/chem_exp06.metta` now carries the tick-3/tick-4 stateful cap-1 and cap-2 chambers into tick 5, adds a bounded no-op `chamber-tick-with-candidate` clause for exhausted `A`, and records `exp06-candidate-cap-stateful-three-tick-sweep`. Tick 5 selects `e5r0` in both arms but advances without negative abundance or new events; the cap-1/cap-2 divergence from tick 4 persists. `experiments/exp06/smoke.metta` verifies tick-5 selection, final no-op chambers, and the aggregate boundary (`three-tick-stateful-diagnostic-not-raf-status`, `emergence-claim none`); README documents the diagnostic. Checks: `scripts/run_exp00.sh`, `scripts/run_exp06.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `de84704` pushed to GitHub `main`.

2026-07-10 06:30 progress: advanced exp06 from refreshed cap diagnostics to a PeTTa-native accumulated/stateful two-tick cap sweep. `src/chem_exp06.metta` now carries the seed-7 tick-3 chamber output into tick 4 for cap-1/cap-2 arms, using exp05 affinity-assigned source rules and ordinary exp00 candidate selection/ticking. Cap-1 repeats `e5r0` across ticks 3-4, while cap-2 exposes `e5r1` at tick 4, yielding distinct final abundance/event paths. `experiments/exp06/smoke.metta` verifies selected candidates, carried final chambers, and the aggregate `exp06-candidate-cap-stateful-two-tick-sweep` boundary: accumulated diagnostic only, not RAF status or an emergence claim. Checks: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`. Commit `63ed5c3` pushed to GitHub `main`.

2026-07-10 04:30 progress: extended exp06's candidate-pool-cap dynamic probe into a PeTTa-native refreshed two-tick cap sweep. `src/chem_exp06.metta` now exposes tick-4 cap-1/cap-2 treatment and rotated-control selected candidates plus after-tick chambers, with cap-2 deterministically exposing/firing the second exp05 source rule at seed-7/tick-4 while cap-1 stays pinned to the first rule. `experiments/exp06/smoke.metta` verifies selected candidates, chamber transitions, and the aggregate `candidate-cap-two-tick-sweep` atom. Boundary remains explicit: this is a refreshed diagnostic, not accumulated RAF status or an emergence claim; next test is an accumulated stateful multi-tick sweep. Checks passed: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `5240172` pushed to GitHub `main`.

2026-07-10 02:30 progress: tightened exp06's candidate-pool-cap dynamic probe with a matched rotated-control path. `src/chem_exp06.metta` now exposes cap-1/cap-2 selected candidates and after-tick chambers for both exp05 affinity treatment and shuffled-affinity rotated control, all fired through ordinary exp00 `chamber-tick-with-candidate`; the first tick remains productive in both arms, but the comparison atom explicitly limits the result to single-tick productivity (`scientific-boundary single-tick-productivity-not-raf-status`) and points to `multi-tick-cap-sweep`. `experiments/exp06/smoke.metta` and README verify/document the treatment-control probe. Checks passed: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `e5a6285` pushed to GitHub `main`.

2026-07-09 22:30 progress: deepened exp06 bridge-to-ACS favorable-conditions analysis with a PeTTa-queryable bounded intervention cost/path table. `src/chem_exp06.metta` now compares catalyst assignment, basal-food replenishment, candidate-pool cap, and catalysis-map offset as cost-1 diagnostic interventions over existing exp04 evidence rows, including positive specificity/broad-template rows, RAF-negative basal-only and shuffled-1 controls, an offset-sensitive shuffled-9 positive control, and a candidate-cap row explicitly marked `not-yet-evaluated` / `dynamic-test-required`. `experiments/exp06/smoke.metta` verifies the rows, aggregate table, bounded shortest-path status, and preserves `emergence-claim none`; README documents the bounded path table. Checks passed: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d18bdb7` pushed to GitHub `main`.

2026-07-09 20:30 progress: started exp06 bridge-to-ACS favorable-conditions analysis as a PeTTa-native diagnostic scaffold. `src/chem_exp06.metta` names the verified ACS-negative exp04 no-catalysis source row and the exp04 RAF-rich terminal row/core, enumerates intervention variables (exp05 catalyst-affinity assignment, basal replenishment, candidate-pool cap, catalysis-map offset), and records a first deterministic one-step shortest-path witness from no catalysis to the specificity-template catalysis condition. `experiments/exp06/smoke.metta`, `scripts/run_exp06.sh`, and README coverage verify the scaffold while preserving `emergence-claim none`; host/path-search role is bookkeeping only. Checks passed: `scripts/run_exp06.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `2d146d5` pushed to GitHub `main`.

2026-07-09 18:30 progress: connected the exp05 catalyst-affinity scaffold directly into exp00 chamber ticking. `src/chem_exp05.metta` now builds treatment and rotated-control chambers from affinity-assigned source-rule pools, applies a cap-2 bounded pool, selects deterministically by seed/tick through the existing exp00 selector, and fires via ordinary `chamber-tick-with-candidate`; `experiments/exp05/smoke.metta` verifies selected candidates, treatment/control chamber transitions, and an explicit no-emergence-claim status atom. Checks passed: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. No RAF scan or emergence claim is made. Commit `f1fecec` pushed to GitHub `main`.

2026-07-09 16:30 progress: triaged and advanced the pre-existing exp05 scaffold into a tracked PeTTa smoke slice. `src/chem_exp05.metta` now keeps soft catalyst-affinity assignment PeTTa-native with generic token-overlap weights, a positive baseline, rotated-weight controls, and projection into ordinary exp00 `candidate`/`candidate-pool` atoms so bounded caps can be reused by later chamber ticking. `experiments/exp05/smoke.metta`, `scripts/run_exp05.sh`, and README document/verify the scaffold; no RAF scan or emergence claim is made. Checks passed: `scripts/run_exp05.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d3dde9f` pushed to GitHub `main`.

2026-07-09 14:30 progress: added the cap-8 productive run to the thin exp03 artifact writer without moving chemistry logic into Python. `scripts/write_exp03_productive_cap_files.py` now queries `(exp03-cap8-productive-file-bundle seed-13 random-polymer)` and emits `exp03-cap8-productive-seed-13-random`; the shell test verifies generated section files, RUN.md provenance, cap-8 config, first event, dynamic event-count metric, and summary. README now documents cap-8 artifact coverage. Checks passed: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `d9d5bc3` pushed to GitHub `main`. Note: pre-existing untracked exp05 scaffold files were observed and left untouched.

2026-07-09 12:30 progress: extended the cap-8 deterministic selection/generation seam into exp03 accumulated chamber ticking and productive-cap run exports. `src/chem_dynamics.metta` now exposes cap-8 accumulated tick/run wrappers through 16 ticks and a seed-13/R-family cap-8 productive fixture over the full eight-rule source pool; rr7 is generated/bounded/selected but advances as a safe no-op because R27 is outside the 17-molecule productive state. Exp03 smoke verifies eight-candidate generation, deterministic rr5 initial selection, rr7 no-op ticks, 14 productive events over 16 ticks, replay/final-abundance/run-record completeness, exact trace order, and run-export/file-bundle sections. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `bae69e6` pushed to GitHub `main`.

2026-07-09 10:30 progress: extended the PeTTa-native exp00 deterministic candidate seam to full eight-rule pools. `src/chem_exp00.metta` now has `seeded-choice-8`, `select-candidate-8`, a cap-8 clause for eight-candidate generated pools, `selected-candidate-from-list-8`, `chamber-tick-generated-8`, and `exp00-candidate-cap-8`; exp00 smoke verifies seeded choices, cap construction, cap-8 pool preservation, direct eight-way selection, and generated chamber ticking where seed-7 selects the productive eighth rule. Checks passed: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `3506bc0` pushed to GitHub `main`.

2026-07-09 08:30 progress: added a thin exp04 offset-sensitivity report artifact writer without moving chemistry logic into Python. New `scripts/write_exp04_offset_report_files.py`/`.sh` queries PeTTa-side `exp04-offset-sensitivity-report-file` and summary atoms and writes `OFFSET_SENSITIVITY_REPORT.metta`, `SUMMARY.metta`, and `RUN.md`; `scripts/test_exp04_offset_report_files.sh` verifies the generated report contains the tested offset partitions, representative cores, and `unbiased-emergence not-supported` claim. README documents the writer. Checks passed: `python3 -m py_compile scripts/write_exp04_offset_report_files.py`, `scripts/test_exp04_offset_report_files.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `14d12f0` pushed to GitHub `main`.

2026-07-09 04:30 progress: completed the exp04 rotated-shuffle offset sweep for offsets 1 through 9. `experiments/exp04/run_reduction_sweep.py` now includes shuffled offsets 3, 4, 7, and 8, expanding the deterministic artifact to 108 rows; `src/chem_exp04.metta` mirrors the added rows, exposes `exp04-reduction-shuffle-offsets-1-through-9-tested?`, and adds representative minimized-core atoms for the newly observed RAF-like controls. Key result: the full offset set is mixed rather than uniformly negative — hand-designed offsets 3/7 are RAF-negative at basal-4, while offsets 4/8 remain RAF-like; generated-template offset 4 is RAF-like; cross-template offsets 3/7 are RAF-like and offsets 4/8 are RAF-negative. This strengthens the interpretation that exp04 is a positive inspectable, catalysis-map-sensitive artifact, not an unbiased-emergence claim. Checks passed: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `c4f69db` pushed to GitHub `main`.

2026-07-09 02:30 progress: added two more exp04 rotated-shuffle negative controls and exposed minimized RAF cores for inspection. `experiments/exp04/run_reduction_sweep.py` now tests `shuffled-2` and `shuffled-6` in addition to `shuffled`, `shuffled-1`, and `shuffled-9`, expanding the deterministic artifact to 72 rows. `src/chem_exp04.metta` mirrors the added rows, exposes `exp04-reduction-shuffle-negative-offsets-tested?`, and adds `exp04-reduction-minimized-core-rules` atoms for representative baseline/shuffle cores. Key result: at basal-4, `shuffled-2` and `shuffled-6` are RAF-negative for all three rule pools (maximal RAF 0), while previous `shuffled`/`shuffled-9` positives remain offset-sensitive caveats; the baseline hand-designed/specific minimized core remains `(lCD lBCD2)`. Checks passed: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `6f7a5ba` pushed to GitHub `main`.

2026-07-09 00:30 progress: broadened exp04 reduction controls from one rotated shuffle to three deterministic shuffle offsets. `experiments/exp04/run_reduction_sweep.py` now tests `shuffled`, `shuffled-1`, and `shuffled-9`, expanding the deterministic artifact to 54 rows; `src/chem_exp04.metta` exposes all additional rows plus `exp04-reduction-alt-shuffle-offsets-tested?`, and exp04 smoke verifies representative offset-sensitive rows. Result: shuffle controls are highly offset-sensitive — e.g. hand-designed `shuffled-1` at basal-4 has maximal RAF 0, while `shuffled-9` keeps maximal RAF 7/core 3 and generated pools still show small RAF-like shuffle artifacts — so the interpretation remains catalysis-map-sensitive and not an unbiased-emergence claim. Checks passed: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `f65c430` pushed to GitHub `main`.

2026-07-08 22:30 progress: added a stricter cross-template mechanically generated exp04 reduction-control pool. `experiments/exp04/run_reduction_sweep.py` now includes `mechanically-generated-cross-template`, assigning pair catalysts to disjoint/cross pair products; the deterministic reduction artifact expands from 24 to 36 rows. `src/chem_exp04.metta` exposes the new rows plus predicates for cross-template broad RAF-negative controls and shuffled cross-template RAF-like signal creation; exp04 smoke verifies representative rows and the interpretation still rejects an unbiased-emergence claim. Key result: cross-template specific/broad/none controls remain maximal RAF 0, while shuffled cross-template catalysis creates a small maximal RAF 5/core 1, reinforcing catalysis-map sensitivity. Checks passed: `python3 -m py_compile experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `1a8b2c2` pushed to GitHub `main`.

2026-07-08 20:30 progress: moved the exp04 reduction-sweep summary into PeTTa-queryable report atoms. `src/chem_exp04.metta` now exposes the 24-row `exp04-reduction-sweep-row` table, baseline/control predicates, interpretation atom, and `exp04-reduction-sweep-report-complete?`; exp04 smoke verifies the baseline hand-designed/specific/basal-4 row, no-catalysis RAF-negative controls, generated-specific RAF-negative control, shuffled hand-designed caveat, and interpretation that unbiased emergence is not yet supported. Checks passed: `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `0ed265e` pushed to GitHub `main`.

2026-07-08 18:30 progress: ran the first exp04 reduction sweep around the rich RAF fixture. Added `experiments/exp04/run_reduction_sweep.py` and `scripts/run_exp04_reduction_sweep.sh`; artifact `experiments/exp04_reduction_sweep_20260708/` compares 24 deterministic variants across catalysis mode (specific/broad/shuffled/none), basal interval (0/4/8), and hand-designed versus mechanically generated template pools. Baseline hand-designed/specific/basal-4 remains maximal RAF 15, greedy core 2 (`lCD`, `lBCD2`), 56 events, and 15-rule event diversity. No-catalysis controls have maximal RAF 0; shuffled hand-designed catalysis still leaves a smaller RAF-like signal (maximal RAF 10/core 3), so exp04 remains success-biased and catalysis-map-sensitive rather than an unbiased emergence claim. Checks passed: `python3 -m py_compile experiments/exp04/run_rich_raf.py experiments/exp04/run_reduction_sweep.py`, `scripts/run_exp04_reduction_sweep.sh`, `scripts/run_exp04.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `1a8b2c2` pushed to GitHub `main`.

2026-07-08 exp04 exploratory result: created a rich chemistry experiment on branch `agent/exp04-rich-chemistry` combining ligation/cleavage/modification templates, specificity-filtered deterministic template catalysis, a 20-rule pool, 56-tick food-replenished dynamics, and bounded RAF pruning. The PeTTa smoke fixture reports a positive RAF candidate, and the host-computed harness `experiments/exp04/run_rich_raf.py` found a stricter 15-rule maximal RAF, greedy 2-rule core (`lCD`, `lBCD2`), zero no-catalysis RAF, and 56/56 dynamic events in artifact run `experiments/exp04_rich_raf_20260708/`. Interpretation: first positive exp04-style RAF artifact, deliberately success-biased rather than an unbiased emergence claim. Checks passed: `python3 -m py_compile experiments/exp04/run_rich_raf.py`, `scripts/run_exp04.sh`, host artifact rerun, and `git diff --check`.

2026-07-08 16:30 progress: broadened the productive-cap artifact/export coverage to include the cap-7 seed-13/R-family productive run. `src/chem_dynamics.metta` now exposes `exp03-cap7-productive-run-export` and `exp03-cap7-productive-file-bundle`, and includes cap-7 in the productive-cap export/bundle completeness predicates. Exp03 smoke verifies cap-7 export config, 14 exported events, ACS candidates, file-bundle id, events, metrics, ACS section, and summary. The thin writer now queries `(exp03-cap7-productive-file-bundle seed-13 random-polymer)` and the shell test verifies the generated `exp03-cap7-productive-seed-13-random` artifact directory, `RUN.md` provenance, config, first event, event-count metric, and summary. Checks passed: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `79f9090` pushed to GitHub `main`.

2026-07-08 14:30 progress: extended cap-7 from the exp00 kernel seam into an exp03 productive state shape while keeping the kernel PeTTa-native. `src/chem_exp00.metta` now supports 17-molecule state tick/seed access and generated eight-rule candidate pools. `src/chem_dynamics.metta` adds cap-7 accumulated chamber ticking/run wrappers plus a 17-molecule seed-13/R-family productive cap-7 chamber with R16 in-state, explicit rr0-rr6 accumulated tick clauses, final abundance/replay/run-record atoms, and seed-13 exp02 ACS provenance. Exp03 smoke verifies seven-candidate bounded generation, deterministic tick-0 rr6 selection via `(13+0)%7 = 6`, 14 productive events over 14 ticks, final abundance, replay, completeness, and exact trace order. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, and `git diff --check`. Commit `500b2c5` pushed to GitHub `main`.

2026-07-08 12:30 progress: extended the exp00 deterministic selection/cap seam to cap-7 while keeping the kernel PeTTa-native. `src/chem_exp00.metta` now has `seeded-choice-7`, `select-candidate-7`, `selected-candidate-from-list-7`, `chamber-tick-generated-7`, `exp00-candidate-cap-7`, and a cap-7 truncation clause for eight-candidate generated pools. Exp00 smoke verifies seed/tick choice, cap construction/truncation from eight candidates, direct seven-candidate selection, and cap-7 generated chamber ticking over an eight-rule pool. Checks passed: `scripts/run_exp00.sh` and `git diff --check`. Commit `9d5f89b` pushed to GitHub `main`.

2026-07-08 10:30 progress: packaged the compact exp02 cycle-scan report as PeTTa-queryable artifact exports. `src/chem_exp02.metta` now exposes `(exp02-cycle-scan-report-bundle)` with `CYCLE_SCAN_REPORT.metta` and `SUMMARY.metta` run-file atoms plus bundle accessors/completeness checks; exp02 smoke verifies the exact bundle. Added a thin writer/test pair (`scripts/write_exp02_cycle_report_files.py`, `.sh`, `scripts/test_exp02_cycle_report_files.sh`) that queries local PeTTa/SWI and writes only the returned report atoms plus `RUN.md` provenance. Checks passed: `scripts/run_exp02.sh`, `python3 -m py_compile scripts/write_exp02_cycle_report_files.py`, `scripts/test_exp02_cycle_report_files.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `1535435` pushed to GitHub `main`.

2026-07-08 08:30 progress: broadened the thin productive-cap artifact writer to include the seed-17/S-family cap-6 productive bundle. `scripts/write_exp03_productive_cap_files.py` now queries `(exp03-cap6-productive-file-bundle seed-17 random-polymer)` and emits `exp03-cap6-productive-seed-17-random`; `scripts/test_exp03_productive_cap_files.sh` verifies the new run directory, `RUN.md` provenance, config, first event, event-count metric, and summary section. Checks passed: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `147633d` pushed to GitHub `main`.

2026-07-08 06:30 progress: extended productive cap-6 to seed-17/S-family, adding a third PeTTa-tested productive cap-6 state shape. `src/chem_dynamics.metta` now carries a 16-molecule S-family cap-6 chamber with S89/S05 in-state, explicit rr0-rr5 accumulated ticking, final abundance/replay/run-record/export/file-bundle atoms, and source ACS provenance from `exp02-seed-17-acs-candidates`; exp03 smoke covers bounded six-candidate generation, deterministic tick-0 rr5 selection, 12 productive events over 12 ticks, exact trace order, and export/file-bundle sections. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`.

2026-07-08 04:30 progress: added a compact PeTTa-side cycle-scan provenance report for the generated-unplanted exp02 scans. `src/chem_exp02.metta` now exposes `exp02-cycle-scan-summary-report` over k=4..7 generated-unplanted controls (40 sweep points / 120 family records each, all 0 active cycles) plus a completeness predicate; exp02 smoke covers the exact report. `experiments/exp02_small_sweep_20260630/SUMMARY.md` now includes the compact k=4..7 human-readable table. Checks passed: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `5cc2d24` pushed to GitHub `main`.

2026-07-08 02:30 progress: broadened the productive-cap artifact/export bundle to include the new seed-13/R-family cap-6 productive run. `src/chem_dynamics.metta` now includes seed-13 in the compact productive-cap run-export list and PeTTa-side `run-file-bundle` projections; exp03 smoke verifies seed-13 export config/events/ACS plus file-bundle events/metrics/ACS/summary. The thin artifact writer now emits four bundles, adding `exp03-cap6-productive-seed-13-random` with tested `CONFIG.metta` through `SUMMARY.metta` sections and `RUN.md` provenance. Checks passed: `scripts/run_exp03.sh`, `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `2c04300` pushed to GitHub `main`.

2026-07-08 00:30 progress: extended productive cap-6 beyond the seed-11/Q-family fixture to seed-13/R-family while keeping the chemistry kernel PeTTa-native. `src/chem_exp00.metta` now supports tick/seed/candidate generation for 16-molecule, eight-rule states; `src/chem_dynamics.metta` adds a 16-molecule seed-13 productive cap-6 chamber with R89/R05 present, explicit rr0-rr5 accumulated ticking, final abundance/replay/run-record atoms, and source ACS provenance; exp03 smoke proves bounded six-candidate generation, deterministic selection, 12 productive events over 12 ticks, final abundance, replay, completeness, and exact trace order. Checks passed: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like diff scan. Commit `dd941d0` pushed to GitHub `main`.

2026-07-07 22:30 progress: added compact artifact provenance to the exp03 productive-cap file writer. `scripts/write_exp03_productive_cap_files.py` now writes an output-root `RUN.md` alongside queried PeTTa `run-file-bundle` sections, documenting the exact source bundle expressions, per-run file convention, and reproduction commands while keeping chemistry logic in PeTTa. `scripts/test_exp03_productive_cap_files.sh` now verifies the generated `RUN.md` plus cap-5/cap-6 section files. Checks passed: `python3 -m py_compile scripts/write_exp03_productive_cap_files.py`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `7521d09` pushed to GitHub `main`.

2026-07-07 20:30 progress: connected the PeTTa-side productive-cap file bundles to a thin artifact writer without moving chemistry logic into Python. `src/run_contract.metta` now exposes all v0.1 run-file sections via accessors (`CONFIG.metta` through `SUMMARY.metta`); run-contract and exp03 smoke cover manifest/abundance/metric/ACS/ablation file sections. Added `scripts/write_exp03_productive_cap_files.py` plus shell/test wrappers to query local PeTTa/SWI for the cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 bundles and write per-run files. Checks passed: `scripts/run_contract.sh`, `scripts/run_exp03.sh`, `scripts/test_exp03_productive_cap_files.sh`, `scripts/run_exp00.sh`, and `git diff --check`. Commit `948da77` pushed to GitHub `main`.

2026-07-07 18:30 progress: added PeTTa-side file-section/query hooks for v0.1 run-contract records. `src/run_contract.metta` now exposes `make-run-file-bundle`, named `run-file` sections (`CONFIG.metta` through `SUMMARY.metta`), and section accessors so host serializers can query PeTTa for file contents without reconstructing fields. `src/chem_dynamics.metta` projects cap-5 productive seed-13, cap-6 rich seed-11, and cap-6 productive seed-11 run records into file bundles. Smoke coverage grew to run-contract 32 checks and exp03 415 checks; `scripts/run_contract.sh`, `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check` passed. Commit `fa5cbd6` pushed to GitHub `main`.

On 2026-06-26, the PDF specification was received via Telegram, preserved in the local research library, text-extracted, hashed, and linked here. A public GitHub implementation repository was created at `https://github.com/bgoertzel-sing/petta-chem` and cloned locally to `projects/petta-chem/repos/petta-chem`.

Runtime choice is now settled for version 0.1: PeTTa running on SWI-Prolog 9.3.x, using the local stack validated during OmegaClaw setup. Python may be used only as an experimental harness for configuration, batch runs, data export, plotting, or filesystem logistics; it should not be the chemistry kernel.

A first PeTTa-native exp00 deterministic smoke scaffold has been added in the implementation repo. It defines molecule/rule/state/event atom shapes and proves a one-step deterministic transition `A + B --Cat--> AB` with replay checks. This is an executable kernel smoke test, not an emergence claim. On 2026-06-27, commit `ee60d539e95ec35bfce30a80d0683cab620aa7be` was pushed to GitHub `main` after re-running `scripts/run_exp00.sh` successfully and checking for obvious secret-like strings. Follow-up commit `2ae87353f4adee7ca4492ed27a03f2b70e86e688` generalized exp00 from a fully hard-coded reaction into a bounded binary catalytic transition with atom accessors, event construction, replay equality, and expanded smoke tests; `scripts/run_exp00.sh` passed before push. Commit `0b943c2a641d5d1f5e97ce17cee5d7f3bb1fca73` then added candidate, chamber, metric, trace accessors, and a one-candidate chamber tick; `scripts/run_exp00.sh` passed before push. Commit `f031ff9c0cf6582b7cc76ab34d8df356c9e51c04` added applicability/invariant checks: positive reactant/catalyst checks, safe blocked firing for starved candidates, state/trace nonnegative abundance checks, and expanded tests; `scripts/run_exp00.sh` passed before push. Commit `0f6e5cb09870ad037285ca95f775b31d9b78923e` added a seed/tick deterministic two-candidate selector seam using PeTTa `#mod`, with `seed-7` choosing the productive candidate and `seed-8` choosing a distractor; `scripts/run_exp00.sh` passed before push. Commit `6f2e25edb10288350b9003c1840b69d3371f7db6` then wired that deterministic selection into chamber ticking and added a first three-candidate pool with fixed caps; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push. Commit `205092f26e3def5e940ca9d29db610f67f9d664a` generalized candidate generation/caps from exp00 hard-coded candidates to chamber-rule-derived candidate pools, explicit `candidate-cap` atoms, bounded pools, and a generated chamber tick; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push. Commit `d3da831907d20f3739ac4233c9b516527c898c5d` added PeTTa-native deterministic molecule/rule hash seams plus exp00 unit tests for hashes, candidate-cap boundaries, and replay equivalence; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push. Commit `68fd5a4ec7fdd687aa0e8cfc25fcb21c2956eee1` added the first exp01 planted ACS recovery smoke: PeTTa-native `acs-candidate`/`ablation` atoms, a two-rule planted catalytic closure with distractors, non-catalytic-cycle rejection, and a single-rule productivity-drop ablation; `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed before commit. Commit `8dde7e8405260a4687e6cb972b73b0814b6bdc78` generalized exp01 recovery into a conservative PeTTa-native ACS pair/set scanner that enumerates all rule pairs in the planted fixture, marks only reciprocal product-as-catalyst closure active, and keeps rejected distractor pairs explicit; `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed before commit. Commit `912c5cee7964b466e66c770ad9425d87cb9bf381` extended exp01 ablation from fixture counts to replayed PeTTa productivity traces: baseline planted ACS replay records two transition traces, single-rule ablation records one, and the ablation drop is computed from trace counts; `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push to GitHub `main`. Commit `4dbf4b5454cf19b536c1019950e42c19541a6359` defined the version-0.1 consequential-run output contract in PeTTa-shaped atoms, adding `run-config`, `run-manifest`, `abundance-snapshot`, `run-summary`, and `run-record` atoms plus a runnable `scripts/run_contract.sh` smoke fixture over exp01 outputs; checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `git diff --check`, and an obvious secret-like scan. Commit `3d476b6` pushed to GitHub `main`. Commit `a3ddf9e63faf90c4a4b1a9a09b8b1e7eeeba6be2` added the first tiny deterministic exp02 random-polymer control sweep: a seed-derived four-rule polymer fixture with one reciprocal product-as-catalyst ACS pair, shuffled-catalyst and no-catalysis controls with zero active pairs, PeTTa run-contract records for all three runs, `scripts/run_exp02.sh`, and `experiments/exp02_small_sweep_20260630/RUN.md`; checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan.

Commit `b83d97b70940c590c6d485743460e91380c454e0` parameterized exp02 beyond the original tiny fixture with a seed-11/six-rule PeTTa sweep point, preserving shuffled-catalyst/no-catalysis controls, run-contract records, and RUN.md provenance; checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan. Commit `4c39d90f6a0a8ce8cd84cb6896ba571c6874f920` broadened exp02 again with a component-generated seed-13/eight-rule PeTTa family, shuffled/no-catalysis controls, 28-pair conservative ACS scan/counts, run-contract records, and updated RUN.md hashes/provenance; checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan.

Commit `4a80388299cb94814bd73dc3a49094afb07b955e` made exp02 sweep provenance more systematic by adding PeTTa `exp02-sweep-point` atoms for seed/rule-count/family coverage and extending the run-contract file harness/test from the original three seed-7 directories to all nine seed-7/seed-11/seed-13 random/control records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Commit `3404d9d0d5b250357d9e7bc79c81001060a45708` added a PeTTa-side seed-to-component generation seam and broadened exp02 to a fourth seed-17/eight-rule parameter point with random/shuffled/no-catalysis records, 12-run serialization, and smoke coverage. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Commit `484c55dfdb21f937f7db0a93b66d07448416674a` then used that seam for the first generated non-planted seed-to-component control: seed-19/eight-rule random-polymer, shuffled-catalyst, and no-catalysis families all scan to zero active reciprocal pairs, are tagged with `sweep-kind generated-unplanted-control`, and expand run-contract serialization to fifteen records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

Commit `a5dbc04d8a4f7d070f0915282d634874b440006f` added a second generated non-planted exp02 seed-to-component point, seed-23/eight rules, with random-polymer, shuffled-catalyst, and no-catalysis families all scanning to zero active reciprocal pairs. It also added PeTTa `exp02-sweep-kind-summary` and `active-pair-rate` atoms separating planted reciprocal-pair controls (4/12 family records active; 7 active pairs total) from generated-unplanted controls (0/6 active; 0 pairs) and expanded run-contract serialization to eighteen records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

Commit `2c7a15b39ea00348fe19cad59efa5ac9ca9f2c2b` added a concise exp02 sweep-kind report: PeTTa `exp02-summary-row`/`exp02-sweep-kind-summary-report` atoms plus `experiments/exp02_small_sweep_20260630/SUMMARY.md`, preserving the conservative no-emergence-claim interpretation. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan. Commit `745d433c29089cc19588704c8d88feaa10982379` added the first factored-template generated-unplanted seed-29 point; commit `f83cd62c43afbf0db3965aab2955284b5d25aa1f` added seed-31 through the same compact token/product dictionary pattern. Commit `09ff9559cf03d3077c5cf5504c6e10c21576ee02` then moved exp02 sweep-kind summaries toward PeTTa-side folds over tested run-record lists, deriving family-record counts, active-family counts, active-pair totals, and active random-polymer points while preserving the current planted 4/12 with 7 active pairs versus generated-unplanted 0/12 result. Commit `e033bac47929a9f7652d3c81ef82c14157f0849a` used that seam for seed-37/eight-rule factored-template generated-unplanted random/shuffled/no-catalysis records, deriving generated-unplanted controls as 0/15 active family records and expanding serialization to twenty-seven records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

Commit `1eff1d9bac864d550c26b48321c188dcb35e49b7` continued the factored-template exp02 generated-unplanted batch with seed-97/eight-rule random/shuffled/no-catalysis records through the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/54 family records with 0 active pairs, and run-contract serialization/testing covers sixty-six records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

Commit `f0a45a4` added exp03 multi-tick soup dynamics in PeTTa: `src/chem_dynamics.metta` layers a recursive/bounded multi-tick chamber runner over exp00, accumulates event logs, advances ticks safely through blocked/no-op steps, exposes abundance snapshots and trace/event helpers, and adds a five-tick productive fixture plus a starved no-op fixture. `experiments/exp03/smoke.metta` checks 5-tick evolution, event accumulation/counting, tick advancement, reactant exhaustion/no-op behavior, and replay equivalence; `scripts/run_exp03.sh` runs the smoke. Parent review re-ran `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and an obvious secret-like scan.

Immediate next step: cap-7 now has a PeTTa-tested exp03 productive state shape; next likely add export/file-bundle coverage for the cap-7 productive run or continue another bounded-cap/state shape.

- 2026-07-07 14:30: Made the cap-6 sixth candidate productive in-state for seed-11/Q-family. Added 15-molecule six-rule candidate generation in exp00 plus a wider Q-family productive bridge with Q05/Q16/Q99, explicit rr0-rr5 accumulated ticks, run-record/replay/metrics atoms, and exp03 smoke proof of 12 productive events over 12 ticks with final Q05/Q16 abundance. Checks: `scripts/run_exp03.sh` (404 ✅), `scripts/run_exp00.sh` (82 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `3d476b6` pushed to GitHub `main`. Commit `0d03f4c` pushed to GitHub `main`.

- 2026-07-07 12:30: Extended cap-6 from the exp00 seam into exp03 rich dynamics over seed-11/Q-family. Added cap-6 accumulated chamber ticking/run wrappers, safe rr5/sr5/nr5 no-op handling for the sixth source-rule candidate outside the 12-molecule rich-state shape, and run-record/replay/metrics atoms. Exp03 smoke verifies the six-rule capped pool, deterministic tick-0 rr5 selection via `(11+0)%6 = 5`, 12-tick random dynamics with 7 productive events, final abundances, replay, completeness, and exact trace order. Checks: `scripts/run_exp03.sh` (390 ✅), `scripts/run_exp00.sh` (81 ✅), `git diff --check`, and an obvious secret-like diff scan. Commit `e31bc31` pushed to GitHub `main`.

- 2026-07-07 10:30: Added the first cap-6 exp00 kernel seam: deterministic seed/tick selection, cap-6 candidate-pool truncation for 6/8-candidate pools, `chamber-tick-generated-6`, and smoke coverage for direct generated ticking over a six-rule pool. Checks: `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `db929ce` pushed to GitHub `main`.
- 2026-07-07: Made the cap-5 fifth candidate productive in-state for seed-13/R-family. Added 15-molecule state support, a productive R8/R9/R89 cap-5 chamber, explicit rr0-rr4 accumulated dynamics, and exp03 smoke/run-record coverage proving rr4 fires productively at ticks 1 and 6 under deterministic cap-5 selection. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `db6cff6` pushed to GitHub `main`.

- 2026-07-07: Extended cap-5 beyond the seed-11/Q-family bridge into seed-17/S-family 12-molecule rich dynamics. Added seed-17 cap-5 rich run-record atoms, bounded five-candidate source-pool coverage, rr4 no-op handling for fifth candidates outside the state shape, and exp03 smoke tests for deterministic selection, event counts (random 11, shuffled 8, no-catalysis 0), abundance snapshots, replay, discrimination, completeness, and trace events. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan. Commit `129c170` pushed to GitHub `main`.

- 2026-07-07: Extended the cap-5 seed-11/Q-family seam into multi-tick rich dynamics. Added cap-5 accumulated ticking/run wrappers, Q-family rr4/sr4/nr4 no-op distractor handling for the 12-molecule rich state, 15-tick cap-5 run-config/manifest/metrics/summary/ACS/run-record atoms, and exp03 smoke tests for event counts (random 10, shuffled 8, no-catalysis 0), abundance snapshots, replay, discrimination, completeness, and trace events. Checks: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and an obvious secret-like diff scan.

Commit `ee77e30` continued the factored-template generated-unplanted exp02 batch with seed-167/eight-rule random/shuffled/no-catalysis records. All three remain zero-active; generated-unplanted folded summaries are now 0/96 family records with 0 active pairs, and serialization/testing covers one hundred eight records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

Commit `0ec6d5c` continued the same factored-template generated-unplanted exp02 batch with seed-173/eight-rule random/shuffled/no-catalysis records. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/99 family records with 0 active pairs, and serialization/testing covers one hundred eleven records. Checks passed locally before commit/push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

Commit `9829ccc` continued the factored-template generated-unplanted exp02 batch with seed-179/eight-rule random/shuffled/no-catalysis records via the same PeTTa token/product dictionary seam. All three remain zero-active; generated-unplanted folded summaries are now 0/102 family records with 0 active pairs, and serialization/testing covers one hundred fourteen records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-07: Added PeTTa-native cap-5 deterministic selection/generation seams in exp00 (`seeded-choice-5`, `select-candidate-5`, list selection, generated ticking, cap atom, and cap clauses for 5/6/8-rule pools) plus an exp03 seed-11/Q-family cap-5 exploratory check over the six-rule rich source pool. Checks: `scripts/run_exp00.sh` (75 ✅), `scripts/run_exp03.sh` (354 ✅), `git diff --check`, and an obvious secret-like scan. Commit `39cc96d` pushed to GitHub `main`.
- 2026-07-04: Commit `b6492c4` continued the host-swept factored-template generated-unplanted exp02 batch with seed-149/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/84 family records with 0 active pairs, and run-contract serialization/testing covers ninety-six records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).
- 2026-07-04: Commit `d17ce7a` continued the host-swept factored-template generated-unplanted exp02 batch with seed-139/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/81 family records with 0 active pairs, and run-contract serialization/testing covers ninety-three records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).
- 2026-07-04: Commit `7db19ca` continued the host-swept factored-template generated-unplanted exp02 batch with seed-137/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/78 family records with 0 active pairs, and run-contract serialization/testing covers ninety records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- 2026-07-04: Commit `070ddce` continued the factored-template generated-unplanted exp02 batch with seed-113/eight-rule random/shuffled/no-catalysis records. The conservative scanner remains zero-active for all three families; generated-unplanted folded summaries are now 0/69 family records with 0 active pairs, and run-contract serialization/testing covers eighty-one records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-03: Commit `bb1f320` added compact exp03 dynamic aggregate/report atoms over tested seed-7, seed-13, and seed-17 full-source exports. `src/chem_dynamics.metta` now exposes per-seed `exp03-dynamic-summary-row` atoms and an `exp03-dynamic-aggregate-report` summarizing 9 family records, 3 active random-family records, 6 zero-event controls, 6 total random events, and candidate cap 2. Checks before commit/push: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-03: Commit `e6aee9f` continued the factored-template generated-unplanted exp02 batch with seed-101/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/57 family records with 0 active pairs, and run-contract serialization/testing covers sixty-nine records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-03: Commit `467a6f6` added richer exp03 dynamic run-record/export coverage over the full-source bridges. `src/chem_dynamics.metta` now gives seed-7 full-source random, shuffled, and no-catalysis families v0.1 run-records, defines a PeTTa `run-export` projection over run-record fields, and exposes export projections for seed-7/13/17 full-source dynamic records. `experiments/exp03/smoke.metta` covers seed-7 control records/abundances plus export events, metrics, and summaries across the covered seeds. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-03: Commit `9b82112` added a seed-17/eight-rule generated full-source exp03 dynamic bridge using the exp02 seed-to-components seam. The chamber carries all eight generated source rules, caps deterministic ticking to the first two candidates, records two replayable random-polymer `rr0` events over three ticks, and keeps shuffled-catalysts/no-catalysis controls at zero events; run-record metrics include the seed-to-components provenance. Checks before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.


- 2026-07-03: Commit `395c10c` generalized the exp03/exp02 dynamic bridge beyond the seed-7 window. `src/chem_dynamics.metta` now adds a seed-11/six-rule-source dynamic fixture with bounded Q-state transitions, random/shuffled/no-catalysis chambers, and v0.1 run-contract records; the random family produces two events over three ticks while both controls remain zero-event. Checks before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-03: Commit `9b02a60` extended exp03 full-source dynamics to the seed-13/eight-rule exp02 family. `src/chem_exp00.metta` now caps eight-rule candidate pools; `src/chem_dynamics.metta` adds bounded seed-13 random/shuffled/no-catalysis full-source chambers, deterministic rr0 replay over three ticks, v0.1 run-records for all three dynamic families, and completeness/discrimination predicates. The random family records two productive events while both controls remain zero-event. Checks before commit/push: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-03: Commit `9a37c59` broadened exp03 beyond two-rule dynamic source windows by adding four-rule candidate-pool generation support and a seed-7 full-source exp02 chamber. The chamber carries rr0-rr3/sr0-sr3/nr0-nr3 source rules, caps per-tick selection to two candidates, preserves deterministic rr0 event replay at ticks 0 and 2, and keeps shuffled/no-catalysis controls at zero events. Checks before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-03: Commit `fd90ca0` added the first exp03-to-exp02 dynamic bridge. `src/chem_dynamics.metta` now sources seed-7 random-polymer, shuffled-catalyst, and no-catalysis rule identities from exp02 and runs them through bounded three-tick exp03 dynamics; the random family records two productive events while both controls record zero. Checks before commit: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan.

- 2026-07-03: Commit `2acdd39` lifted exp03 from the duplicated-`r0` productive fixture into a selectable two-rule pool. `src/chem_dynamics.metta` now uses `(r1 r0)` as the exp03 rule pool, exposes deterministic selected-candidate checks at ticks 0 and 1, and the five-tick smoke alternates productive `r0` firings with `r1` distractor/no-op ticks while preserving replay and starved no-op checks. Checks before push: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, and `git diff --check`.

- 2026-07-02: Commit `f0a45a4` adds exp03 multi-tick soup dynamics with accumulated event logs, safe blocked/no-op tick advancement, abundance snapshots, trace helpers, a five-tick productive fixture, and a starved no-op fixture. Checks passed after parent review: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and an obvious secret-like scan (only expected `seed-7` strings matched).

- 2026-07-02: Commit `1eff1d9` continues the factored-template generated-unplanted exp02 batch with seed-97/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/54 family records with 0 active pairs, and run-contract serialization/testing covers sixty-six records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-04: Commit `4162be7` continued the factored-template generated-unplanted exp02 batch with seed-127/eight-rule random/shuffled/no-catalysis records through the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/72 family records with 0 active pairs, and run-contract serialization/testing covers eighty-four records. Checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.


- 2026-07-05: Commit `c0e6762` continued the host-swept factored-template generated-unplanted exp02 batch with seed-211/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/120 family records with 0 active pairs, and run-contract serialization/testing covers 132 records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- 2026-07-05: Commit `c53077e` added a 3-rule catalytic cycle scanner to `src/chem_exp01.metta`: `product-catalyst-closed-3?` checks product(r0)=catalyst(r1), product(r1)=catalyst(r2), product(r2)=catalyst(r0); `scan-rule-triple`/`scan-rule-triples-4` enumerate triples; a planted 3-cycle fixture validates the scanner with 13 new exp01 smoke tests. Checks: exp00 (70 ✅), exp01 (41 ✅), exp02 (400 ✅), exp03 (77 ✅). Pushed to GitHub `main`.

- 2026-07-05: Commit `b77a50e` added 3-rule catalytic cycle scanning to exp02 8-rule families: `exp02-scan-triples-8` enumerates all C(8,3)=56 triples, recursive `exp02-active-triple-count` helper counts active triples, planted 3-cycle fixture (ptc0/ptc1/ptc2 + 5 distractors) validates the scanner finds exactly 1 active triple, and convenience atoms run triple scanning on seed-13 planted and seed-17/29/31/37/211 generated-unplanted 8-rule families — all have 0 active triples, confirming the pair scanner's conservative result extends to 3-rule cycles. 17 new exp02 smoke tests. Checks: exp00 (71 ✅), exp01 (42 ✅), exp02 (417 ✅), `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-05: Commit `f1ce038` added comprehensive 3-rule catalytic cycle scanning across ALL 40 generated-unplanted exp02 seeds: `exp02-generated-unplanted-seeds-8` PeTTa list, `exp02-fold-seed-triple-total` recursive fold, `exp02-generated-unplanted-triple-total` (0 active triples across 40 seeds × 3 families = 120 family records), `exp02-triple-scan-summary` constructor, and 16 new smoke tests including fold total, seed count, and spot-checks across 9 representative seeds. Checks: exp00 (70 ✅), exp01 (41 ✅), exp02 (430 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-05: Commit `cfb1be1` added 5-rule catalytic cycle scanner to exp01 and exp02. In `src/chem_exp01.metta`: `product-catalyst-closed-5?`, `useful-acs-5?`, `acs-status-for-quintuple`, `scan-rule-quintuple`, `scan-rule-quintuples-6` (C(6,5)=6), `active-quintuple-count-6`, planted 5-cycle fixture (qc0→qc1→qc2→qc3→qc4→qc0 with distractor qd0), and 9 exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-quintuples-8` enumerating all C(8,5)=56 quintuples, recursive `exp02-active-quintuple-count`, planted 5-cycle fixture in 8-rule format (pqq0→pqq1→pqq2→pqq3→pqq4→pqq0 with 3 distractors), comprehensive fold/summary across all 40 generated-unplanted seeds, and 20 exp02 smoke tests. Result: 0 active 5-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple scanner's zero-active result extends to 5-rule cycles. Also updated SUMMARY.md with quadruple and quintuple scan provenance. Checks: exp00, exp01, exp02, exp03, contract files, py_compile, `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-05: Commit `77e3426` added 4-rule catalytic cycle scanner to exp01 and exp02. In `src/chem_exp01.metta`: `product-catalyst-closed-4?`, `useful-acs-4?`, `acs-status-for-quadruple`, `scan-rule-quadruple`, `scan-rule-quadruples-5` (C(5,4)=5), `active-quadruple-count-5`, planted 4-cycle fixture (qc0→qc1→qc2→qc3→qc0 with distractor qd0), and 9 exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-quadruples-8` enumerating all C(8,4)=70 quadruples, recursive `exp02-active-quadruple-count`, planted 4-cycle fixture in 8-rule format (pqc0→pqc1→pqc2→pqc3→pqc0 with 4 distractors), comprehensive fold/summary across all 40 generated-unplanted seeds, and 20 exp02 smoke tests. Result: 0 active 4-rule cycles across all 120 generated-unplanted family records, confirming pair/triple scanner's conservative zero-active result extends to 4-rule cycles. Also updated SUMMARY.md with triple-scan provenance. Checks: exp00 (70 ✅), exp01 (50 ✅), exp02 (450 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan.

- 2026-07-05: Commit `35cfb19` continued the host-swept generated-unplanted exp02 batch with seed-199/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the factored PeTTa token/product dictionary seam. Initial checks passed before commit: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched). Pushed `35cfb19` to GitHub `main`.

Commit `4a46c78` continued the host-swept generated-unplanted exp02 batch with seed-193/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/111 family records with 0 active pairs, and run-contract serialization/testing covers one hundred twenty-three records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

Commit `9bdc31b` continued the host-swept generated-unplanted exp02 batch with seed-197/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records through the factored PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries are now 0/114 family records with 0 active pairs, and run-contract serialization/testing covers one hundred twenty-six records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

## GitHub workflow

Benjamin has given standing permission to push ordinary `petta-chem` work to GitHub without asking first, because mistakes can be rolled back. Continue to run relevant checks and keep commits focused before pushing. He also wants active forward progress on `petta-chem` by default: do not pause after each step; proceed to the next useful technical task unless there is a major blocker needing his technical/sysadmin intervention or scientific input. This does not waive safeguards for destructive operations such as force-pushes, deleting branches/tags/repos, changing visibility/access/secrets, merging PRs, or publishing releases.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| implementation | `https://github.com/bgoertzel-sing/petta-chem` | `projects/petta-chem/repos/petta-chem` | `main` | `db929ce` pushed 2026-07-07 |

## Environments

- Runtime: PeTTa on SWI-Prolog 9.3.x.
- Current local PeTTa checkout: `projects/omegaclaw/repos/PeTTa`.
- Current local SWI-Prolog: `projects/omegaclaw/local/swipl-9.3.36`.
- `petta-chem` runners: `projects/petta-chem/repos/petta-chem/scripts/run_exp00.sh`, `projects/petta-chem/repos/petta-chem/scripts/run_exp01.sh`, `projects/petta-chem/repos/petta-chem/scripts/run_contract.sh`, `projects/petta-chem/repos/petta-chem/scripts/run_exp02.sh`, `projects/petta-chem/repos/petta-chem/scripts/run_exp03.sh`.
- Local-first; no paid compute approved.

## Key results

- 2026-07-09: Added compact PeTTa-side exp04 offset-sensitivity report/export atoms over the 108-row rotated-shuffle reduction sweep. Commit `2290218` added the compact PeTTa-side exp04 offset-sensitivity report/export atoms over the 108-row rotated-shuffle reduction sweep. The report partitions basal-4 offsets by pool into RAF-negative versus RAF-like rotations, exposes representative minimized cores and a file-style bundle, and keeps the claim as `unbiased-emergence not-supported`. Checks: `scripts/run_exp00.sh`, `scripts/run_exp04.sh`, `git diff --check`, and obvious secret-like diff scan.
- 2026-06-26: Source PDF ingested and sidecar created: `library/petta-abstract-algorithmic-chemistry/SOURCE.md`.
- 2026-06-26: Public GitHub repository created and cloned: `https://github.com/bgoertzel-sing/petta-chem` → `projects/petta-chem/repos/petta-chem`.
- 2026-06-26: Runtime decision accepted: PeTTa on SWI-Prolog 9.3.x; see `projects/petta-chem/repos/petta-chem/docs/runtime.md`.
- 2026-06-26: exp00 deterministic PeTTa smoke scaffold passed locally via `scripts/run_exp00.sh`.
- 2026-06-27: Commit `ee60d539e95ec35bfce30a80d0683cab620aa7be` pushed to GitHub `main`; `scripts/run_exp00.sh` re-passed before push.
- 2026-06-27: Commit `2ae87353f4adee7ca4492ed27a03f2b70e86e688` generalized exp00 with atom accessors, event construction, a bounded generic binary catalytic state transformer, replay equality, and expanded PeTTa smoke tests; `scripts/run_exp00.sh` passed before push.
- 2026-06-27: Commit `0b943c2a641d5d1f5e97ce17cee5d7f3bb1fca73` added candidate, chamber, metric, trace accessors, and a one-candidate chamber tick; `scripts/run_exp00.sh` passed before push.
- 2026-06-27: Commit `f031ff9c0cf6582b7cc76ab34d8df356c9e51c04` added applicability/invariant checks for candidate firing and nonnegative abundance preservation; `scripts/run_exp00.sh` passed before push.
- 2026-06-27: Commit `0f6e5cb09870ad037285ca95f775b31d9b78923e` added a seed/tick deterministic two-candidate selector seam; `scripts/run_exp00.sh` passed before push.
- 2026-06-28: Commit `6f2e25edb10288350b9003c1840b69d3371f7db6` wired deterministic candidate selection directly into chamber ticking and added a bounded three-candidate pool/cap seam; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push.
- 2026-06-28: Commit `205092f26e3def5e940ca9d29db610f67f9d664a` generalized candidate generation/caps beyond hard-coded exp00 candidates: chamber rules now generate candidate pools, `candidate-cap` atoms bound per-tick pools, and a generated chamber tick reuses deterministic selection; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push.
- 2026-06-29: Commit `d3da831907d20f3739ac4233c9b516527c898c5d` added exp00 unit coverage for deterministic PeTTa-native molecule/rule hash seams, candidate-cap boundary preservation, and replay equivalence between generated chamber ticking and direct one-tick replay; `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan passed before push.
- 2026-06-29: Commit `68fd5a4ec7fdd687aa0e8cfc25fcb21c2956eee1` added the first exp01 planted ACS recovery smoke with PeTTa-native ACS and ablation atoms, planted two-rule catalytic closure among distractors, non-catalytic-cycle rejection, and productivity-drop ablation; `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed before commit.
- 2026-06-29: Commit `8dde7e8405260a4687e6cb972b73b0814b6bdc78` generalized exp01 recovery into a conservative PeTTa-native ACS pair/set scanner with explicit active/rejected statuses across all rule pairs in the planted four-rule fixture; `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan passed before commit.
- 2026-06-30: Commit `912c5cee7964b466e66c770ad9425d87cb9bf381` extended exp01 ablation from fixture counts to replayed PeTTa productivity traces; baseline recovery now stores two transition traces, single-rule ablation stores one, and the ablation drop is computed from trace counts. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `git diff --check`, and an obvious secret-like diff scan.
- 2026-06-30: Commit `4dbf4b5454cf19b536c1019950e42c19541a6359` defined the version-0.1 run output contract in PeTTa-shaped atoms and a smoke fixture: config, manifest/provenance, events, abundance snapshots, metrics, ACS candidates, ablations, and summary/replay status. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp01.sh`, `scripts/run_contract.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-06-30: Commit `b83d97b70940c590c6d485743460e91380c454e0` parameterized exp02 beyond the first tiny seed-7/four-rule fixture by adding a seed-11/six-rule PeTTa sweep point with two active reciprocal product-as-catalyst pairs in the random fixture and zero active pairs in shuffled/no-catalysis controls; run-contract records and RUN.md provenance were updated. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-01: Commit `745d433c29089cc19588704c8d88feaa10982379` factored exp02 generated-unplanted control generation one step further with seed-29/eight-rule PeTTa token/product dictionaries plus reusable `exp02-factored-unplanted-rule-components`; all random/shuffled/no-catalysis families remain zero-active, generated-unplanted summary is now 0/9 family records, and run-contract serialization covers twenty-one records. Checks passed locally before commit/push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).
- 2026-07-01: Commit `f83cd62c43afbf0db3965aab2955284b5d25aa1f` added factored-template generated-unplanted seed-31/eight-rule random/shuffled/no-catalysis records. The PeTTa ACS scanner finds zero active reciprocal product-as-catalyst pairs for all three families; generated-unplanted controls summarize as 0/12 family records, and run-contract serialization covers twenty-four records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `09ff9559cf03d3077c5cf5504c6e10c21576ee02` added PeTTa recursive list/metric helpers that fold exp02 sweep-kind summaries from tested run-record lists instead of hand-maintained totals. Folded summaries preserve the current planted reciprocal-pair control result (4/12 family records active, 7 active pairs) and generated-unplanted result (0/12 active, 0 active pairs). Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `e033bac47929a9f7652d3c81ef82c14157f0849a` added factored-template seed-37/eight-rule exp02 generated-unplanted random/shuffled/no-catalysis records. The PeTTa ACS scanner finds zero active reciprocal product-as-catalyst pairs for all three families; generated-unplanted controls now summarize as 0/15 family records and 0 active pairs, and the summary report rows are derived from folded summary atoms rather than hand-maintained active-pair totals. Serialization/testing covers twenty-seven records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).


- 2026-07-02: Commit `7931be2ef6b0c723b9d86db6a9239b445dba6ec6` added factored-template seed-43/eight-rule exp02 generated-unplanted random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. The conservative PeTTa ACS scanner finds zero active reciprocal product-as-catalyst pairs for all three families; generated-unplanted controls now summarize as 0/21 family records and 0 active pairs, and serialization/testing covers thirty-three records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).
- 2026-07-02: Commit `7d9ef1a` added factored-template seed-47/eight-rule exp02 generated-unplanted random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative scanner; generated-unplanted folded summaries now stand at 0/24 family records with 0 active pairs, and run-contract serialization/testing covers thirty-six records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).
- 2026-07-02: Commit `cc2d3c9bd7b288c5aa9f379a63a38d9d6d826a8e` added factored-template seed-53/eight-rule exp02 generated-unplanted random/shuffled/no-catalysis records via the same PeTTa token/product dictionary seam. All three remain zero-active under the conservative scanner; generated-unplanted folded summaries are now 0/27 family records with 0 active pairs, and run-contract serialization/testing covers thirty-nine records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched). Commit `cc2d3c9bd7b288c5aa9f379a63a38d9d6d826a8e` continued the factored-template exp02 generated-unplanted batch with seed-53/eight-rule random/shuffled/no-catalysis records through the same PeTTa token/product dictionary seam. All three remain zero-active under the conservative reciprocal product-as-catalyst scanner; generated-unplanted folded summaries now stand at 0/27 family records with 0 active pairs, and run-contract serialization/testing covers thirty-nine records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-02: Commit `74d44e13592fbea1bae4db327addf03fc46fa2d1` added factored-template seed-59/eight-rule exp02 generated-unplanted random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three remain zero-active under the conservative scanner; generated-unplanted folded summaries are now 0/30 family records with 0 active pairs, and run-contract serialization/testing covers forty-two records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-02: Commit `67aebddd2cd64b8d3a5229918c91d0c3f9ed8c48` continued the factored-template generated-unplanted exp02 batch with seed-67/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/36 family records with 0 active pairs, and run-contract serialization/testing covers forty-eight records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched).

- 2026-07-02: Commit `43f23adf063585b31d3136cdd5d9c5ea532f604d` continued the factored-template generated-unplanted exp02 batch with seed-71/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/39 family records with 0 active pairs, and run-contract serialization/testing covers fifty-one records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token/product strings matched).


- 2026-07-02: Commit `879ad44` continues the factored-template generated-unplanted exp02 batch with seed-79/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/45 family records with 0 active pairs, and run-contract serialization/testing covers fifty-seven records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected token strings matched).

- 2026-07-02: Commit `e7567124d95b18602d87f63b1634fb82922b1cb7` continues the factored-template generated-unplanted exp02 batch with seed-83/eight-rule random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/48 family records with 0 active pairs, and run-contract serialization/testing covers sixty records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-03: Commit `a9deba1` continued the host-swept factored-template generated-unplanted exp02 batch with seed-109/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/66 family records with 0 active pairs, and run-contract serialization/testing covers seventy-eight records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).

- 2026-07-04: Commit `dec8208` added factored-template generated-unplanted exp02 seed-131/eight-rule random/shuffled/no-catalysis records through the PeTTa token/product dictionary seam. Conservative ACS scanning remains zero-active for all three, generated-unplanted folded summaries are now 0/75 family records with 0 active pairs, and run-contract serialization/testing covers eighty-seven records.

- 2026-07-04: Commit `3bdea91` continued the host-swept factored-template generated-unplanted exp02 batch with seed-163/eight-rule random/shuffled/no-catalysis records. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/93 family records with 0 active pairs, and run-contract serialization/testing covers one hundred five records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.

## Open questions

- How broad should the first conservative ACS/RAF-like scanner be before moving from planted exp01 fixtures to exp02 random chemistry?
- What parameter ranges should be considered scientifically meaningful for exp02 before large sweeps?

## Related projects and concepts

- PeTTa, MeTTa, Atomspace, Hyperon-family systems.
- MORK as future acceleration/integration seam, not a version-0.1 dependency.
- Python as optional experiment harness/glue only, not as the algorithmic chemistry kernel.
- ActPC-style predictive weighting as experiment 5, after replay/ACS foundations.
- Semantic chemistry and music chemistry as later bridge prototypes after causal ACS archive.

## Risks

- **False emergence:** cyclic or copy-rule artifacts mislabeled as ACSs. Mitigation: planted tests, minimum size, catalyst closure, shuffled/no-catalysis controls, ablation.
- **Unreplayable stochasticity:** same seed/config produces different logs. Mitigation: stop on replay failure and snapshot all RNG/state paths.
- **Candidate explosion:** matching grows too quickly. Mitigation: active signatures and hard per-rule/per-family/per-tick caps from the start.
- **Premature integration burden:** MORK/semantic/music coupling delays the abstract substrate. Mitigation: keep seams explicit but out of the first milestone.
- **Rule bloat / novelty addiction / frozen attractor:** use costs, retirement, entropy/temperature floors, decay, and controls.

- 2026-06-30: Commit `ce6da96da5f6c797dff2f9941bc529e88e487f9f` added a thin host harness for exp02 run-contract file serialization and test coverage.
- 2026-06-30: Commit `b83d97b70940c590c6d485743460e91380c454e0` parameterized exp02 with a seed-11/six-rule sweep point and controls.
- 2026-07-01: Commit `4c39d90f6a0a8ce8cd84cb6896ba571c6874f920` broadened exp02 with a component-generated seed-13/eight-rule PeTTa family plus shuffled/no-catalysis controls; conservative 28-pair ACS scanning finds two active reciprocal product-as-catalyst pairs in random-polymer and zero in both controls. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `4a80388299cb94814bd73dc3a49094afb07b955e` added PeTTa `exp02-sweep-point` atoms over the seed-7/seed-11/seed-13 families and extended run-contract file serialization/testing to all nine exp02 random/control records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `3404d9d0d5b250357d9e7bc79c81001060a45708` added a less fixture-like PeTTa seed-to-component generation seam for exp02, broadened the sweep to seed-17/eight rules, and extended serialization/tests from nine to twelve run-contract records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-01: Commit `484c55dfdb21f937f7db0a93b66d07448416674a` added a generated non-planted seed-to-component exp02 control point. Seed-19/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records all have zero active reciprocal product-as-catalyst pairs, carry `sweep-kind generated-unplanted-control`, and increase serialized run-contract coverage from twelve to fifteen records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-01: Commit `a5dbc04d8a4f7d070f0915282d634874b440006f` added generated non-planted seed-23/eight-rule exp02 controls and PeTTa sweep-kind active-pair summaries. Generated-unplanted controls now have 0/6 active family records versus planted reciprocal-pair controls at 4/12, with run-contract serialization expanded to eighteen records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `2c7a15b39ea00348fe19cad59efa5ac9ca9f2c2b` added a concise exp02 sweep-kind report: tested PeTTa `exp02-summary-row`/`exp02-sweep-kind-summary-report` atoms and `experiments/exp02_small_sweep_20260630/SUMMARY.md`, explicitly preserving the no-spontaneous-emergence-claim caveat. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.
- 2026-07-01: Commit `3a69fe3bcc023908e4dad8f722b8050c03e38e99` added factored-template seed-41/eight-rule generated-unplanted random/shuffled/no-catalysis records via the existing PeTTa token/product dictionary seam. All three remain zero-active; generated-unplanted folded summaries are now 0/18 active family records with 0 active pairs; run-contract serialization/testing covers thirty records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).
- 2026-07-02: Commit `0628dabb8459b27ec0f9b3d4c8d52958719b2419` continued the host-swept factored-template generated-unplanted exp02 batch with seed-61/eight-rule random/shuffled/no-catalysis records. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/33 family records with 0 active pairs; run-contract serialization/testing covers forty-five records. Checks passed before push: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `git diff --check`, and an obvious secret-like scan.

- 2026-07-02: Commit `de29b83` continued the host-swept factored-template generated-unplanted exp02 batch with seed-73/eight-rule random/shuffled/no-catalysis records. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/42 family records with 0 active pairs; run-contract serialization/testing covers fifty-four records. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).

- 2026-07-02: Commit `dc925509d4e0d2d2f160d5e6c86e5c83117a1a2e` continued the host-swept factored-template generated-unplanted exp02 batch with seed-89/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/51 family records with 0 active pairs, and run-contract serialization/testing covers sixty-three records. Checks: `scripts/run_exp00.sh`, `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `git diff --check`, and an obvious secret-like scan (only expected seed-token strings matched).
- 2026-07-03: Commit `ba01c3a` continued the host-swept factored-template generated-unplanted exp02 batch with seed-103/eight-rule random-polymer, shuffled-catalyst, and no-catalysis records via the existing PeTTa token/product dictionary seam. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/60 family records with 0 active pairs, and run-contract serialization/testing covers seventy-two records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).
- 2026-07-04: Commit `8695e6d` continued the host-swept factored-template generated-unplanted exp02 batch with seed-151/eight-rule random/shuffled/no-catalysis records. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/87 family records with 0 active pairs, and run-contract serialization/testing covers ninety-nine records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, and `git diff --check`.

- 2026-07-06: Commit `8b848db` added the first 10-tick exp02-family dynamic bridge for seed-7, connecting longer multi-tick evolution to the exp02-style family bridge structure. The seed-7 random family produces 5 productive rr0 events over 10 ticks (ticks 0,2,4,6,8) with reactant exhaustion at tick 8; shuffled/no-catalysis controls remain zero-event. Added run-config/manifest/metrics/summary/run-record atoms and 21 new smoke tests. Checks: exp03 (111 ✅), exp00 (70 ✅), `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-06: Extended the 10-tick exp02-family dynamic bridge to seed-13 and seed-17. Both bridges use 8-rule full-source chambers with candidate cap 2 and higher initial abundances (R0=5/R1=5 for seed-13, S0=5/S1=5 for seed-17). Each produces 5 productive rr0 events at even ticks (0,2,4,6,8) with reactant exhaustion at tick 8; shuffled/no-catalysis controls remain zero-event. 42 new smoke tests (153 total, was 111). Checks: exp03 (153 ✅), exp00 (71 ✅), `git diff --check`, and secret-like scan.

- 2026-07-06: Commit `eca2af8` added 7-rule catalytic cycle (septuple) scanner to exp01 and exp02, completing systematic cycle-size coverage for 8-rule families (k=2..7). In `src/chem_exp01.metta`: `product-catalyst-closed-7?`, `scan-rule-septuple`/`scan-rule-septuples-8` (C(8,7)=8), `active-septuple-count-8` using a split-4 approach to stay within PeTTa's nested-operation compilation limit, planted 7-cycle fixture (sp0→sp1→sp2→sp3→sp4→sp5→sp6→sp0 with distractor spd0), and 6 new exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-septuples-8`, recursive `exp02-active-septuple-count`, planted 7-cycle fixture in 8-rule format (psp0→psp1→psp2→psp3→psp4→psp5→psp6 with 1 distractor), comprehensive fold/summary across all 40 generated-unplanted seeds, and 20 new exp02 smoke tests. Result: 0 active 7-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple/quintuple/sextuple scanner's zero-active result extends to 7-rule cycles. Also updated SUMMARY.md with septuple scan provenance. Checks: exp00 (70 ✅), exp01 (68 ✅), exp02 (510 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-05: Commit `bf68c71` added 6-rule catalytic cycle scanner to exp01 and exp02. In `src/chem_exp01.metta`: `product-catalyst-closed-6?`, `useful-acs-6?`, `acs-status-for-sextuple`, `scan-rule-sextuple`, `scan-rule-sextuples-7` (C(7,6)=7), `active-sextuple-count-7`, planted 6-cycle fixture (sc0→sc1→sc2→sc3→sc4→sc5→sc0 with distractor sd0), and 9 exp01 smoke tests. In `src/chem_exp02.metta`: `exp02-scan-sextuples-8` enumerating all C(8,6)=28 sextuples, recursive `exp02-active-sextuple-count`, planted 6-cycle fixture in 8-rule format (psq0→psq1→psq2→psq3→psq4→psq5 with 2 distractors), comprehensive fold/summary across all 40 generated-unplanted seeds, and 20 exp02 smoke tests. Result: 0 active 6-rule cycles across all 120 generated-unplanted family records, confirming pair/triple/quadruple/quintuple scanner's zero-active result extends to 6-rule cycles. Also updated SUMMARY.md with sextuple scan provenance. Checks: exp00 (70 ✅), exp01 (62 ✅), exp02 (490 ✅), exp03 (77 ✅), contract files, py_compile, `git diff --check`, and secret-like scan. Pushed to GitHub `main`.

- 2026-07-04: Commit `7b12aee` continued the host-swept factored-template generated-unplanted exp02 batch with seed-157/eight-rule random/shuffled/no-catalysis records. All three scan to zero active reciprocal product-as-catalyst pairs; generated-unplanted folded summaries are now 0/90 family records with 0 active pairs, and run-contract serialization/testing covers one hundred two records. Checks passed before push: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, `python3 -m py_compile scripts/write_exp02_contract_files.py`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like diff scan (only expected seed-token strings matched).


2026-07-06 22:30 progress: cap-4 rich bridge now covers seed-11/Q-family six-rule source pools. exp00 candidate generation/capping handles 12-molecule/six-rule pools, exp03 adds Q-family rich chamber tick clauses plus seed-11 run-record atoms, and exp03 smoke tests validate 12 random events, no-catalysis zero events, replay, discrimination, and run-record completeness. Checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and an obvious secret-like scan.


2026-07-11 22:30: Added direct bounded candidate-pool-to-chamber ticking in PeTTa and routed exp05 scored affinity pools through it; exp00/exp05/exp07 checks pass.
