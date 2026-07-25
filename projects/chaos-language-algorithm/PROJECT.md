# Chaos Language Algorithm

## 2026-07-25 10:15 PDT status

The bounded M-E causal-state coding slice is acceptance-tested at clean commit
`30357a1`. `CausalStateCoder` codes held-out symbols with one fresh empty KT
estimator per reconstructed state, synchronizes deterministically through the
history map, and then advances through frozen unifilar transitions. Training
emission counts are never seeded into the adaptive tables or transmitted in
the topology-only model charge; an explicit count-inflation regression proves
both properties. Focused unittest passed 6; required discovery passed 259 in
46.362 seconds; compileall and diff checks passed. No registry exposure or
E0--E8 fixture/score was opened.

## 2026-07-25 08:15 PDT status

The first bounded M-E CSSR reconstruction slice is acceptance-tested at clean
commit `5f8e836`.
The pure-Python reconstructor deterministically groups predictive suffix
distributions, refines them to a unifilar fixpoint, canonically labels states,
and reports raw training emission counts plus state-occupancy complexity.
Those counts remain diagnostics only; held-out coding has not been
implemented and must start from empty KT estimators. Focused unittest passed
3; required discovery passed 256 in 45.688 seconds; compileall and diff checks
passed. No E0--E8 fixture or score was opened. `CausalStateCoder` is the next
M-E slice.

## 2026-07-25 06:15 PDT status

M-E has begun at clean commit `759ba3f` with the deferred CTW control as a
bounded, non-measuring slice.
The direct-alphabet `ContextTreeWeightingCoder` updates an active suffix path,
is registered as `ctw-d8`, and retains fixed-vocabulary, reset, clone, and
deterministic-replay behavior. Focused unittest passed 4; required discovery
passed 253 in 47.277 seconds; compileall and diff checks passed. No E0--E8
fixture or score was opened. CSSR reconstruction remains the next M-E slice.

## 2026-07-25 02:15 PDT status

The public adaptive beam/composite path now has an end-to-end fixed-seed
deterministic replay regression at clean active-worktree commit `f948b70`.
Repeated fits produce identical `GrammarState`, exact reconstruction,
proposal-ledger bytes, and final-breakdown bytes. Focused unittest passed 12;
required discovery passed 249 in 47.081 seconds; compileall and diff checks
passed. No E0--E8 fixture or score was opened. The remaining M-D audit must
resolve the governing proposal-budget scope before M-E begins.

## 2026-07-24 22:15 PDT status

M-D public beam integration is acceptance-tested at clean active-worktree
commit `8471df2`. Adaptive beam search is opt-in, preserves exact
reconstruction and depth-stable ancestry, selects only under the exact
official scorer, and produces one final disposition per generated proposal.
Greedy and legacy behavior remain the defaults. Beam+composite expansion is
the next bounded M-D slice and currently fails closed. No E-series gate is
authorized by this implementation slice.

Update, 2026-07-24 18:15 PDT: ancestry-aware multi-depth M-D beam traversal is
acceptance-tested at clean active-worktree commit `98a1656`. Each transition
exact-scores and canonical-deduplicates children, partitions every proposal id,
and preserves parent/proposal ancestry for final-path and `beam_pruned` ledger
routing. Focused unittest passed 8; discovery passed 245 in 47.452 seconds;
compileall and diff checks passed. No E0--E8 fixture or score was opened.
Public-loop ledger emission and opt-in API integration remain next.

Update, 2026-07-24 16:15 PDT: the next M-D beam-accounting seam is
acceptance-tested at clean active-worktree commit `972b362`.
Proposal-addressable candidate selection now partitions
every generated candidate exactly once into retained or pruned identifiers,
deduplicates canonical states deterministically, and fails closed on duplicate
or empty ledger identifiers. Focused unittest passed 6; required discovery
passed 243 in 46.374 seconds; compileall and diff checks passed. No E0--E8
fixture or score was opened. Public multi-depth traversal remains next.

Update, 2026-07-24 14:15 PDT: opt-in adaptive composite-loop integration is
acceptance-tested at clean active-worktree commit `3c17035`. Single and
composite proposals compete under the same exact official scorer; atomic
reconstruction, deterministic replay, the frozen proposal budget, and one
ledger disposition per generated composite remain enforced. Defaults and
legacy objectives are unchanged. Focused unittest passed 21; required
discovery passed 241 in 46.581 seconds; compileall and diff checks passed. No
E0--E8 fixture or score was opened. Multi-depth beam traversal with
`beam_pruned` ledger routing remains in M-D.

Update, 2026-07-24 12:15 PDT: opt-in adaptive initializer integration is
acceptance-tested at clean active-worktree commit `a01c2c4`.
`search_objective="adaptive"` now constructs one frozen registry-backed
`AdaptiveTwoPartScorer`; `init="repair"` and `init="lz77-slp"` pass that same
scorer object through exact-score pruning and all later learner scoring.
Defaults remain the legacy empty/proxy path, invalid combinations fail closed,
and initialized models reconstruct and replay deterministically. Focused
unittest passed 17; required discovery passed 239 in 51.762 seconds; compileall
and diff checks passed. No E0--E8 fixture or score was opened. Composite/beam
public-loop integration with complete proposal-ledger routing remains in M-D.

Update, 2026-07-24 10:15 PDT: the isolated M-D deterministic beam-selection
policy is acceptance-tested at clean active-worktree commit `c6d7b96`.
It ranks only exact official scores, deduplicates semantically identical states
by canonical adaptive-scorer digest, uses digest tie-breaking, and returns all
cut states for subsequent `beam_pruned` ledger routing. The policy does not
generate proposals, alter public learner defaults, or bypass reconstruction,
budget, or one-record-per-proposal requirements. Focused stdlib passed 4,
required discovery passed 235 in 46.081 seconds, and compileall/diff checks
passed. No E0--E8 fixture or score was opened. Scorer-frozen public initializer
and search integration remain in M-D.

Update, 2026-07-24 06:15 PDT: M-D exact composite acceptance and ledger
accounting are acceptance-tested at clean active-worktree commit `2a064b1`.
Estimator values rank only; the exact official scorer and exact reconstruction
alone authorize one atomic accepted composite. One record is emitted per
generated composite. Compatible component edits receive exact four-state mixed
second-difference totals and estimator residuals; order-dependent components
correctly leave those fields null instead of fabricating evidence. Focused
unittest passed 11, required stdlib discovery passed 229 in 46.068 seconds,
and compileall/diff checks passed. No E0--E8 fixture or score was opened.
Proposal budgeting, deterministic beam search, and scorer-frozen initializer
integration remain in M-D.

Update, 2026-07-24 04:15 PDT: the M-D category/frame generation sub-slice is
acceptance-tested at clean active-worktree commit `fec7244`.
`CategoryThenChunkProposer` deterministically emits atomic
category-plus-`left M right` proposals only when a frame has the frozen minimum
support and at least two distinct members; support-first ordering and chunk
names are stable, and application preserves exact reconstruction as one
durable `Composite` edit. Focused unittest passed 6, focused pytest passed 10
with 1 subtest, required stdlib discovery passed 226, and compileall/diff
checks passed. No scorer was changed and no E0--E8 fixture or score was opened.
Exact official-score acceptance/estimator residual wiring, proposal budgeting,
and beam search remain in M-D.

Update, 2026-07-24: M-D now has deterministic, exact-reconstructing Re-Pair
and non-self-referential LZ77-to-balanced-SLP initializers with exact-score
strict pruning and replay. The LZ77 slice is clean commit `4a05b5f`; focused
pytest passed 11, required stdlib discovery passed 220, and compileall/diff
checks passed. Public fit-time initializer selection remains deferred until
one frozen adaptive scorer/coder configuration can be reused throughout. No
E0--E8 gate or OmegaSim run was opened.

Update, 2026-07-23: the mathematical-foundations M-D/E5b amendment is
acceptance-tested at active-worktree commit `d640777` (document SHA-256
`bb69556d64e3d893ba05f52f915ee41abe994afbc565d96d1d1a3ca69249f65d`).
It audits theorem assumptions without promoting the supplied proof sketches,
adds deterministic exact-reconstructing LZ77-SLP initialization beside
Re-Pair, and freezes mixed-second-difference ranking with exact-score
acceptance plus estimator residuals. E5b is a separately frozen proposal only;
no fixture or E0--E8 score was opened. Focused pytest passed 17, required
stdlib discovery passed 216, and compileall/diff checks passed. M-D
implementation is next; E3 and the OmegaSim pause remain binding.

Update, 2026-07-23: milestone M-C adaptive two-part scoring is
acceptance-tested at clean active-worktree commit `9684701`. The new
`GrammarStreamCoder` freezes one base-coder factory across arms, codes parse
atoms with that coder, and charges direct and generalized category choices
with fresh per-category KT estimators. `AdaptiveTwoPartScorer` retains the
existing compact model transmission, exposes parse/member/definition
decomposition, caches by canonical state digest, and computes proposal deltas
by exact apply-and-rescore. Focused pytest passed 12; required full stdlib
discovery passed 216; `compileall` and `git diff --check` passed. No E0-E8
outcome, scientific fixture, or held-out suffix was run. M-D is next, preceded
by the explicit reviewed mathematical-foundations amendment.

Update, 2026-07-23: milestone M-B proposal-ledger instrumentation is
acceptance-tested at clean active-worktree commit `46ffbfe`. Optional
`ledger_dir` routing preserves the public CLA defaults while recording exactly
one JSONL record per generated proposal, acceptance/rejection reasons, stable
payload digests, score deltas, and a complete seven-field final breakdown.
The legacy 19-frame regression records `-6,232` data bits, `+6,296` model
bits, `+64` total bits, `accepted=false`, and `reason=positive_delta`.
Focused pytest passed 17; full stdlib discovery passed 216; `compileall` and
`git diff --check` passed. No E0-E8 outcome or scientific fixture was run.

Update, 2026-07-23: milestone M-A coding core is acceptance-tested at clean
active-worktree commit `6145e1d`. It adds prequential protocols, a growing
Krichevsky--Trofimov estimator, adaptive Markov orders 0/1/2, an unchanged
canonical-LZ78 adapter, and a string registry without changing core or CLA API
semantics. Focused tests passed 14; full stdlib discovery passed 216 tests;
`compileall` and `git diff --check` passed. Governing spec/evaluation copies
and their SHA-256 manifest are preserved under the requested named clone's
`docs/`. CTW test 2 and grammar-stream fairness test 6 remain correctly
deferred to M-E and M-C by the milestone dependency map; M-B is next. No E0-E8
outcome, scientific fixture, suffix, or OmegaSim A6 result was generated.

Update, 2026-07-23: the first algorithm-repair subgate now exposes a
machine-readable complete-code decomposition at clean active-repository commits
`2ec949e` / `bdbf0f6`. On the constructed 19-frame generalized fixture it
exactly reproduces the prior canonical result: `-6,232` data bits, `+6,296`
model bits, and `+64` total bits, hence explicit rejection. Focused pytest
passed 11; full pytest passed 322 tests / 93 subtests; stdlib discovery passed
209 tests; `compileall` and `git diff --check` passed. No Mackey--Glass,
Lorenz--96, held-out suffix, detector score, or proxy measurement was produced
or inspected.

Update, 2026-07-23: failed future canonical-result cleanup now durably commits
the identity-guarded deletion by `fsync`ing the same opened parent directory
before returning failure. Spec/implementation commits are `3d5224d` /
`8e8b042`; focused pytest passed 33, full pytest passed 320 tests / 93
subtests, stdlib discovery passed 209 tests, `compileall`, and `git diff
--check`. Constructed provenance validation only: no benchmark, Mackey--Glass,
Lorenz--96, held-out suffix, detector score, or coding score was generated or
inspected.

Update, 2026-07-23: a 10-page evidence synthesis and algorithm-repair
diagnostic now consolidates the symbolic/high-dimensional, complete-code,
synthetic-source, attractor, geometric Stage-A, Stage-B, and OmegaSim A6
results. It decomposes the current failure into representation, proposal/search,
model transmission, conditional data coding, objective, and sample-complexity
questions, and specifies three first repair experiments. LaTeX compilation,
PDF text extraction, ASCII source validation, and visual inspection of all ten
pages passed. PDF:
`repos/chaoslang/docs/cla_experiments_and_repair_diagnostic_20260723.pdf`;
SHA-256
`fdb6f48970165a27784d2c64c04eaa8744274f5a54c068bb1badbf710703b0f6`.

Update, 2026-07-23: future canonical measured-result publication now
revalidates the complete supplied parent ancestry before success, rejecting an
ancestor replaced during persistence by a symlink even when it resolves to the
same opened parent identity. Spec/implementation commits are `0b07cfa` /
`8eabc2c`; focused pytest passed 31, full pytest 318 tests / 93 subtests,
stdlib discovery 209 tests, `compileall`, and `git diff --check`. Constructed
provenance validation only: no benchmark, scientific fixture, held-out suffix,
or detector score was generated or inspected.

Update, 2026-07-23: constructed lifecycle validation now proves that the
identity-bearing descriptor used by future measured-result read-back closes
after success and after read, stdout-write, and stdout-flush failures. The
spec-first active-repository commits are `58c309d` / `11cd2b3`; focused pytest
passed 30, full pytest 317 tests / 93 subtests, stdlib discovery 209 tests,
`compileall`, and `git diff --check`. No benchmark, Mackey--Glass/Lorenz--96
fixture, held-out suffix, or score was generated or inspected; frozen outcomes
remain binding and untuned.

Update, 2026-07-23: future measured-result read-back is now bound to an open
descriptor for the artifact created by that call at clean active-repository
commit `a9c0bf2`. Constructed target- and parent-replacement regressions prove
that replacement bytes cannot reach stdout. Focused pytest passed 26, full
pytest 313 tests / 93 subtests, stdlib discovery 209 tests, `compileall`, and
`git diff --check`. No benchmark, scientific fixture, held-out suffix, or
score was generated or inspected; the frozen Mackey--Glass/Lorenz--96 outcomes
remain binding and untuned.

Update, 2026-07-22: an audit found and spec-first froze the remaining
persist/read-back identity race for future measured results at clean
active-repository commit `c3b9971`. Read-back must retain the created file's
identity rather than reopen its lexical path; matching hashes alone are not
identity evidence. Focused pytest passed 24, full pytest 311 tests / 93
subtests, stdlib discovery 209 tests, `compileall`, and `git diff --check`.
No benchmark or scientific fixture was generated or scored; all frozen
Mackey--Glass/Lorenz--96 outcomes remain binding.

Update, 2026-07-22: the parent-bound canonical-result implementation at clean
active-repository commit `e893704` passed an independent non-measuring
reproducibility audit: focused pytest 24, full pytest 311 tests / 93 subtests,
stdlib discovery 209 tests, `compileall`, and `git diff --check`. Source and
test hashes are recorded in `NOTES.md`. No benchmark, Mackey--Glass or
Lorenz--96 fixture, held-out suffix, or scientific score was generated or
inspected; the Stage-A pass and Stage-B complete-code null remain frozen.

Update, 2026-07-22: the frozen parent-identity invariant is implemented at
clean active-repository commit `e893704`. Canonical result creation, cleanup,
and directory durability now stay relative to one opened parent handle, and a
constructed parent-replacement race fails closed and removes the artifact from
the originally opened directory. Focused pytest passed 24, full pytest 311
tests / 93 subtests, stdlib discovery 209 tests, `compileall`, and `git diff
--check` passed. No benchmark, scientific fixture, or held-out suffix was
generated or scored; the Mackey--Glass/Lorenz--96 Stage-A pass and Stage-B
complete-code null remain frozen and untuned.

Update, 2026-07-22: a spec-first parent-identity invariant at clean
active-repository commit `5c87cf5` closes the design-level validation/create
race for future canonical results: creation and directory durability must stay
bound to one opened parent handle, and a replaced lexical parent must fail.
Focused pytest passed 23, full pytest 310 tests / 93 subtests, stdlib discovery
209 tests, `compileall`, and `git diff --check` passed. No scientific fixture
or held-out suffix was generated or scored; implementation remains a separate
constructed-data subgate and all frozen nulls remain binding.

Update, 2026-07-22: a clean non-measuring reproducibility audit at active-repo
commit `aa5ab90` passed focused pytest 23, full pytest 310 tests / 93 subtests,
stdlib discovery 209 tests, `compileall`, and `git diff --check`. No benchmark
or scientific fixture was run; the nearest-neighbor Stage-A pass and
prefix-quantized Stage-B complete-code null remain frozen and untuned.

Update, 2026-07-22: failed canonical-result cleanup now removes the target only
when its filesystem identity still matches the file created by that call, at
clean active-repository commits `66d1711` / `aa5ab90`. A constructed
replacement regression passed; focused pytest passed 23, full pytest passed
310 tests / 93 subtests, and stdlib discovery passed 209 tests. No scientific
fixture or held-out suffix was generated, rerun, or scored; frozen nulls remain
binding.

Update, 2026-07-22: a constructed regression now proves that future canonical
measured-result publication refuses a pre-existing target symlink without
altering either the link or its referent, at clean active-repository commit
`bd55fe2`. Focused pytest passed 22; full pytest passed 309 tests / 93
subtests and stdlib discovery passed 209 tests. No scientific fixture or
held-out suffix was generated, rerun, or scored; frozen nulls remain binding.

Update, 2026-07-22: future canonical measured-result publication now rejects
symbolic links anywhere in the supplied artifact-parent ancestry at clean
active-repository commit `ab2ba52`. A constructed nested-alias regression
proves no result reaches the alias target. Focused pytest passed 21; full
pytest passed 308 tests / 93 subtests and stdlib discovery passed 209 tests.
No scientific fixture or held-out suffix was generated, rerun, or scored;
frozen nulls remain binding.

Update, 2026-07-22: future canonical measured-result publication now rejects
a symlinked artifact parent before creation at clean active-repository commits
`995903b` / `732cdb2`. A constructed regression proves no result appears in
the alias target. Focused pytest passed 20; full pytest passed 307 tests / 93
subtests and stdlib discovery passed 209 tests. No scientific fixture or
held-out suffix was generated, rerun, or scored; frozen nulls remain binding.

Update, 2026-07-22: constructed tests now prove that stdout write exceptions
and rejected short writes preserve the already durable canonical result as the
authoritative outcome at clean active-repository commit `0a4a7da`. Focused
pytest passed 19; full pytest passed 306 tests / 93 subtests and stdlib
discovery passed 209 tests. No scientific fixture or held-out suffix was
generated, rerun, or scored; frozen ledgers and no-tuning boundaries remain
binding.

Update, 2026-07-22: future measured-result emission now flushes standard output
after its complete write and reports success only after that flush succeeds, at
clean active-repository commits `2bfdfc5` / `af0f3c0`. Constructed focused
tests passed 18; full pytest passed 305 tests / 93 subtests and stdlib discovery
passed 209 tests. No scientific fixture or held-out suffix was generated,
rerun, or scored; frozen ledgers and no-tuning boundaries remain binding.

Update, 2026-07-21: future measured-result emission now verifies the persisted
artifact's read-back SHA-256 before stdout at clean active-repository commits
`17a11ac` / `ecbeaa4`. Constructed focused tests passed 16; full pytest passed
303 tests / 93 subtests and stdlib discovery passed 209 tests. No scientific
fixture or held-out suffix was generated, rerun, or scored; frozen ledgers and
no-tuning boundaries remain binding.

Update, 2026-07-21: future canonical measured-result writes now `fsync` the
parent-directory entry after the artifact itself at clean active-repository
commits `edbf285` / `898d1cb`. Constructed focused tests passed 14; full pytest
passed 301 tests / 93 subtests and stdlib discovery passed 209 tests. No
scientific fixture or held-out suffix was generated, rerun, or scored; frozen
ledgers and no-tuning boundaries remain binding.

Update, 2026-07-21: failed canonical result writes now remove only the newly
created incomplete artifact at clean active-repository commits `d04453a` /
`4ff7ab8`. Constructed focused tests passed 13; full pytest passed 300 tests /
93 subtests and stdlib discovery passed 209 tests. No scientific fixture or
held-out suffix was generated, rerun, or scored; frozen ledgers remain binding.

Update, 2026-07-21: canonical measured-result persistence now verifies the
complete artifact write and flushes plus `fsync`s it before any later stdout
emission at clean active-repository commits `037578f` / `500696f`. Constructed
focused tests passed 12; full pytest passed 299 tests / 93 subtests and stdlib
discovery passed 209 tests. No scientific fixture or held-out suffix was
generated, rerun, or scored; separately frozen ledgers remain mandatory.

Update, 2026-07-21: future measured commands now have a spec-first,
unit-validated persist-then-emit seam at clean active-repository commits
`b0db6ab` / `ac1bcc7`. Constructed tests prove that canonical result bytes are
written before identical stdout bytes, artifact failure leaves stdout
untouched, and incomplete output writes fail closed. Full pytest passed 297
tests / 93 subtests and stdlib discovery passed 209 tests. No scientific
fixture was generated, rerun, or scored; every future benchmark still needs a
separately frozen ledger.

Update, 2026-07-21: the separately frozen smallest prefix-quantized Stage-B
gate failed at clean active-repository commits `7bad170` / `22f1450`. All six
integrity gates passed and neither shuffled null was promoted, but compact CLA
lost to canonical LZ78 on both fresh positives: Mackey--Glass 8,824.829 vs 744
bits and full-state Lorenz--96 8,482.142 vs 1,240 bits. No tuning/rescoring;
this is a coding null, not chaos, attractor/source-law, or semantic evidence.

Update, 2026-07-20: the authorized Stage-B prefix-vector-quantizer unit subgate
is complete at clean active-repository commits `313452d` and `ca3e48f`, with a
README boundary at `21e9fdf`. Constructed tests cover deterministic fitting,
canonical labels, coordinate completeness, prefix-only immutability,
out-of-support assignment, scalar/tie behavior, and fail-closed inputs. Full
pytest passed 286 tests / 93 subtests and stdlib discovery passed 208 tests;
`compileall` and `git diff --check` passed. No scientific fixture or held-out
suffix was generated or scored. A separately frozen Stage-B ledger remains
mandatory before any Mackey--Glass or Lorenz--96 coding measurement.

Update, 2026-07-20: an outcome-independent Stage-B complete-code design now
separates the passed nearest-neighbor Stage-A relation from a prefix-fitted
discrete quotient and CLA coding decision. It requires new Mackey--Glass and
coordinate-complete Lorenz--96 fixtures, constructed-data quantizer validation,
complete external controls, exact replay/reconstruction, and an every-positive/
no-shuffled-null rule. No Stage-B fixture was generated or scored; the next
authorized subgate is quantizer specification and unit tests. See
`scratch/chaoslang-strict-replay/docs/nearest-neighbor-stage-b-design-spec-v1.md`.

Update, 2026-07-20: separately frozen nearest-neighbor divergence Stage-A v2
passed all six fresh Mackey--Glass/full-state Lorenz--96 positive, stable, and
shuffled decisions at clean active-repository commit `85667bd`. V2 preserved
all v1 scientific choices and added only an explicit pre-frozen degenerate
stable-control status. This is bounded detector calibration, not chaos proof
or CLA/compression/attractor/semantic-grammar evidence. Stage B remains closed
pending its own frozen protocol. See
`experiments/20260721T011500Z-nearest-neighbor-calibration-v2/RUN.md`.

Update, 2026-07-20: the exact frozen nearest-neighbor Stage-A v1 command exited
1 before any detector score because a stable fixture had no eligible
positive-distance neighbor pair. This is a harness/protocol failure, not a
calibration outcome. No tuning or v1 rerun; Stage B remains prohibited. See
`experiments/20260720T211500Z-nearest-neighbor-calibration-v1/RUN.md`.

Update, 2026-07-20: a fresh nearest-neighbor divergence Stage-A protocol is
frozen but unexecuted at clean active-repository commit `ee0485c`. It fixes
Mackey--Glass and coordinate-complete Lorenz--96 positives, stable/shuffled
controls, representations, prefix normalization, statistic choices, threshold,
seeds, hashes, command, and the strict rule before outcome inspection. No score
exists; Stage B remains prohibited. See
`experiments/20260720T211500Z-nearest-neighbor-calibration-v1/RUN.md`.

Update, 2026-07-20: an outcome-independent nearest-neighbor divergence
statistic is specified and unit-complete at clean active-repository commits
`fd9e4b0` and `ed53fb4`. Hand-constructed exponential divergence,
Theiler/tie behavior, scalar/vector and translation/scale invariants, and
fail-closed inputs passed; full pytest passed 278 tests / 84 subtests and
stdlib discovery passed 200 tests. No scientific fixture or threshold was
scored. A separately frozen untouched Mackey--Glass/full-state Lorenz--96
Stage-A ledger remains mandatory and Stage B stays prohibited.

Update, 2026-07-20: the active-repository README now preserves the frozen
conditional transition-entropy null and no-tuning boundary at clean commit
`f231844`. Full pytest, stdlib discovery, `compileall`, and `git diff --check`
exited successfully; no scientific fixture was scored.

Update, 2026-07-20: frozen conditional transition-entropy Stage A failed at
clean commit `ba510c3`. Both positives passed, but stable and shuffled
full-state Lorenz--96 were false positives. V1's pre-score command failure is
preserved. No tuning/rescoring; Stage B remains prohibited. See
`experiments/20260720T153000Z-conditional-entropy-calibration-v2/RUN.md`.

Update, 2026-07-20: a conditional transition-entropy detector candidate is
specified and unit-complete at clean active-repository commit `da52b36`. It
computes empirical one-step conditional entropy over externally supplied
discrete symbols. Focused 4 tests / 5 subtests, full pytest 272 tests / 80
subtests, stdlib discovery 194 tests, `compileall`, and `git diff --check`
passed. No scientific fixture was scored; a separately frozen untouched-data
Mackey--Glass/full-state Lorenz--96 Stage-A ledger remains mandatory and Stage
B stays prohibited.

Update, 2026-07-20: the active-repository README now preserves the frozen
repeated-renormalization null and no-tuning boundary at clean commit `6737178`.
Full pytest (268 tests / 75 subtests), stdlib discovery (190 tests),
`compileall`, and `git diff --check` passed; no scientific fixture was scored.

Update, 2026-07-20: frozen repeated-renormalization Stage A failed at clean
active-repository commit `793f10c`. Full-state Lorenz--96 was correctly
promoted and both stable controls rejected, but Mackey--Glass tau=17 was a
false negative (`-0.0009622967` mean log growth per step). No tuning or
rescoring is authorized; Stage B remains prohibited. See
`experiments/20260720T091500Z-renormalized-separation-calibration-v1/RUN.md`.

Update, 2026-07-20: a repeated-renormalization aggregation candidate is
specified and unit-complete at clean active-repository commits `354e48b` and
`3abebb1`. It computes the time-weighted mean log separation growth from
externally generated renormalization cycles and fails closed on invalid input.
Focused 3 tests / 8 subtests, full pytest 267 tests / 75 subtests, stdlib 189
tests, `compileall`, and `git diff --check` passed. No scientific fixture or
threshold was scored; a separately frozen fresh Mackey--Glass/full-state
Lorenz--96 Stage-A ledger remains mandatory and Stage B stays prohibited.

Update, 2026-07-19: frozen correlation-form 0--1 Stage A failed at clean
commit `76d5deb`: both Mackey--Glass and full-state Lorenz--96 positives were
false negatives, while both stable controls were rejected. No tuning; Stage B
remains prohibited. See
`experiments/20260720T031500Z-zero-one-calibration-v1/RUN.md`.

Update, 2026-07-19: the separately specified median correlation-form 0--1
statistic is unit-complete at clean active-repository commit `2d72a48`.
Hand-calculated indexing/correction, frequency-order, odd/even median,
repeatability, and fail-closed gates passed; full pytest passed 263 tests / 67
subtests and stdlib discovery passed 185 tests. No scientific fixture was
scored and no threshold selected. A separately frozen Stage-A Mackey--Glass
and full-state Lorenz--96 ledger remains mandatory; Stage B stays prohibited.

Update, 2026-07-19: a median correlation-form 0--1 chaos statistic is specified
before implementation at clean active-repository commit `9ca744e`. Frequencies
and maximum lag remain externally supplied and a unit gate may not score a
scientific fixture. This is a candidate detector contract, not calibration or
chaos/attractor/grammar evidence; Stage B remains prohibited.

Update, 2026-07-19: frozen paired-divergence Stage A failed at clean commit
`4cc2441`: Mackey--Glass tau=17 was a false negative and stable full-state
Lorenz--96 F=1 was a false positive. No tuning; Stage B remains prohibited.
See `experiments/20260719T211500Z-paired-divergence-calibration-v1/RUN.md`.

Update, 2026-07-19: an outcome-independent paired log-separation statistic is
unit-complete at clean active-repository commit `2be5f1b`. It fits log Euclidean
separation against sample index for externally supplied paired trajectories and
fails closed on zero/non-finite or mismatched inputs. Hand-constructed growth,
contraction, vector, and translation checks passed; focused 12 tests / 16
subtests, full pytest 256 tests / 49 subtests, stdlib discovery 178 tests,
`py_compile`, and `git diff --check` passed. No scientific fixture was scored.
A separate frozen Stage-A ledger must fix perturbations, windows, thresholds,
fresh Mackey--Glass/full-state Lorenz--96 data, and controls before measurement.

Update, 2026-07-19: frozen Stage-A recurrence determinism failed at clean
commit `9aca50b`: stable full-state Lorenz--96 was falsely promoted (`DET=1.0`).
Stage B remains prohibited; no tuning. See
`experiments/20260719T171500Z-recurrence-determinism-calibration-v1/RUN.md`.

Update, 2026-07-19: Stage-A recurrence-determinism instrumentation is unit-
complete at clean local active-repository commit `30f8650`. The additive
statistic reports the fraction of off-diagonal recurrence points in diagonal
runs under an externally fixed radius, with explicit Theiler exclusion and
fail-closed validation. Focused 7 tests, full pytest 251 tests / 45 subtests,
stdlib discovery 173 tests, `py_compile`, and `git diff --check` passed. No
scientific fixture was scored and no detector threshold was selected. A
timestamped untouched-data ledger with explicit Mackey--Glass, full-state
Lorenz--96, non-chaotic, and shuffled controls remains required before Stage A.

Update, 2026-07-19: the separately frozen full-vector recurrence calibration
completed at clean local commit `c667c02`. Every integrity gate passed and
neither shuffled null was promoted, but compact CLA lost both required fresh
positives: Mackey--Glass 9,933.113 versus LZ78 5,304 bits and full-state 8D
Lorenz--96 5,522.398 versus LZ78 2,000 bits. The strict gate failed. This is a
coding null, not chaos, attractor, or semantic-grammar evidence; no tuning is
authorized. See `experiments/20260719T071500Z-vector-recurrence-attractor-v1/RUN.md`.

Update, 2026-07-18: the separately frozen causal recurrence-lag calibration
completed at clean local commit `9cd3cf0`. Every integrity gate passed, compact
CLA beat its JSON continuity control, and neither shuffled null was promoted,
but it lost both required fresh positives: Mackey--Glass 9,954.129 versus LZ78
5,008 bits and Lorenz--96 x7 13,697.457 versus unigram 7,814.621 bits. The
strict gate failed. This is a recurrence-projection coding null, not chaos,
attractor, or semantic-grammar evidence; no inspected-stream tuning is
authorized. See
`experiments/20260719T011500Z-recurrence-attractor-v1/RUN.md`.

## Purpose

Implement and test the Chaos Language Algorithm (CLA): symbolize continuous chaotic trajectories and induce exact-reconstructing grammars using joint chunk and category compression under MDL.

## Source specification

- Library sidecar: `../../library/chaos-language-algorithm/SOURCE.md`
- Algorithm spec PDF: `../../library/chaos-language-algorithm/chaos_language_algorithm_ascii.pdf`
- Algorithm spec extracted text: `../../library/chaos-language-algorithm/extracted.txt`
- Algorithm spec SHA-256: `468c5f49ec7d484bb58a6bc53e28a13f2bba1512be898791ddaea2e96c8af510`
- Python architecture PDF: `../../library/chaos-language-algorithm/cla_python_library_architecture_ascii.pdf`
- Python architecture extracted text: `../../library/chaos-language-algorithm/cla_python_library_architecture_extracted.txt`
- Python architecture SHA-256: `3beacd7855f2fa3912d43d026f175b5518ba08216e19f741540a5de7d20d97c4`
- High-dimensional embedding design PDF: Telegram attachment `cla_hd_embedding---56acc870-3e99-49c0-9c6b-427875c32b57.pdf`
- High-dimensional embedding working text: `../../library/chaos-language-algorithm/cla_hd_embedding_extracted.txt`
- High-dimensional embedding PDF SHA-256: unavailable; media URI was not exposed as a stable local file during ingestion

## Current status

`active` / local-only. Ben promoted CLA on 2026-07-03 as the prerequisite for resuming OmegaSim: build a general toolkit for recognizing grammars of strange attractors, strange transients, and related structures. Sprint-1 local pure-Python `chaoslang` prototype now implements exact-reconstructing symbolic-string grammar induction with chunks, categories, approximate MDL, fact projection, and tests. A 2026-07-09 Lorenz-96 1024-step × 20D fixed-grid M1 smoke run exposed the high-dimensional symbolization failure mode: many unique compound symbols, little recurrence, and no strong basis for grammar claims; see `experiments/20260709T192728Z-lorenz96-1024-dim20-suffix-trie/RUN.md`. Ben's 2026-07-10 high-dimensional embedding design reframed the target as instrumentation plus adaptive/kinetic symbolization. A preregistered 2026-07-12 R256 sweep found positive proxy deltas but no advantage over direct controls, and the leakage-free 2026-07-13 follow-up found linear VAMP beat matched PCA on both primary metrics in 0/3 trajectories at either k, triggering the frozen stop rule. On 2026-07-15, train-fitted k-means support was added at commit `974af31`, the 126-test suite passed, and a comprehensive report was compiled as `repos/chaoslang/docs/cla_experiments_comprehensive_20260715.pdf`. The fresh OmegaSim detector run promoted one of 12 predeclared cells (`coupling=0.60`, `delay=3`, `roles8`, four of five seed wins), which is bounded proxy evidence requiring untouched replication. The independent calibrated frozen held-out CLA coding benchmark remains open.

Update, 2026-07-16: the first independent frozen held-out calibration completed.
Mackey--Glass and Lorenz--96 x0 passed every integrity gate, but CLA failed
aggregate codelength (65,976.621 bits versus frozen unigram at 6,588.443),
dominated by canonical model transmission. This is a coding null, not
chaos/semantic-grammar evidence. Suffix tuning is prohibited; the next gate is
a separate preregistered minimal joint chunk/category diagnostic.

That synthetic failure-branch diagnostic subsequently completed against clean
local commit `6279604`. On the frozen minimal 19-frame fixture, the prescribed
generalized category/chunk move improved the current proxy by 1 bit, while
greedy CLA accepted no edit. The category inducer did not propose the
singleton-member category, and member-specific `CategoryOccurrence` mining
keys could not expose a generalized `a M b` chunk even after manual category
application. This is a bounded representation/proposal diagnosis, not a rescue
of the held-out coding null or evidence of chaos/semantic grammar. The next
gate is a decodable generalized category-slot design and unit implementation
before any new attractor benchmark.

The first domain/unit gate is now implemented at clean local commit `4632212`.
A generalized production stores category identity as `CategorySlot(M)`, while
each rewritten chunk occurrence carries its ordered observed members as a
decoding side table. On the frozen 19-frame fixture the bounded miner found all
19 `a M b` occurrences and exact expansion recovered all 76 tokens; the full
150-test suite passed. Persistence/fact projection and strict replay followed
at clean local commit `bd7595c`; canonical JSON, edit-log replay, and
backend-neutral facts now preserve generalized productions and ordered member
side tables, with 151 full-suite tests passing. This remains representation
plumbing only. A canonical two-document state code followed at clean local
commit `fe32c4a`; it charges the complete grammar plus parse/member side tables
and reconstructs the frozen 19-frame fixture without a stored corpus, with 157
full-suite tests passing. A bounded joint category/generalized-chunk proposal
seam followed at clean local commit `871a0c6`; it reaches the intended frozen
fixture move deterministically, applies the two explicit replayable edits, and
preserves exact reconstruction, with all 158 tests passing. This is reachability
plumbing only: the joint miner is not enabled in the learner, and a separately
frozen synthetic decision gate using the complete decodable code remains
required before another attractor benchmark.

That separately frozen complete-code gate rejected the intended joint move by
64 bits: 34,416 versus 34,352 for the literal initial state. The joint state
saved 6,232 parse/data bits but added 6,296 model bits. All integrity gates and
158 tests passed after a recorded harness-only failed attempt and one-line
correction at clean commit `8ffa31c`. The joint miner remains disabled. This is
a synthetic coding null, not attractor or semantic-grammar evidence; the next
gate is an outcome-independent decodable code refinement, not another
attractor run or suffix tuning.

An additive indexed-code unit subgate followed at clean local commit `8a46900`.
It transmits each token spelling once in a shared sorted table and uses integer
references symmetrically across literal and generalized states, while retaining
complete exact decoding and byte-stable canonical re-encoding. All 165 tests
passed in bounded per-file processes. No candidate codelength was compared and
no attractor suffix was inspected. At that unit stage, a new synthetic
comparison remained blocked on a separately frozen experiment ledger with an
acceptance rule and controls.

That indexed comparison was separately preregistered and completed at clean
local commit `29a52fd`. On the unchanged 19-frame fixture, the complete indexed
joint state cost 9,760 bits versus 10,616 for the indexed literal state (-856),
while canonical JSON v1 exactly reproduced its prior +64-bit rejection. Every
integrity gate and all 165 tests passed. This is a synthetic coding acceptance,
not chaos/semantic-grammar evidence and not a revision of the failed
Mackey--Glass/Lorenz--96 calibration. The joint miner remains disabled pending
a specified and unit-tested indexed complete-code search scorer; no attractor
rerun is authorized.

The indexed joint-search scorer is now separately specified and unit-validated
at clean local commit `a5a0772`. It reproduces the frozen synthetic positive
decision and a short negative control while preserving complete decoding,
exact replay, and order-independent selection; all 168 tests pass. Neither the
scorer nor joint miner is enabled in `CLA.fit_symbols`. The next gate is a
plain-language learner-integration spec and synthetic unit validation, not an
attractor rerun; the Mackey--Glass/Lorenz--96 coding null remains unchanged.

The learner-integration unit gate is now complete at clean local commit
`24d9771`. An explicit opt-in indexed objective scores ordinary and joint
proposals with the same complete code, rejects joint search under the sprint-1
proxy, preserves exact reconstruction, and stores the accepted complete score.
The 19-frame positive control converges to 9,760 bits; the two-frame negative
control remains literal at 1,944 bits. All 171 tests passed in bounded shards.
This enables only synthetic learner plumbing. A new attractor calibration is
still prohibited until its own protocol is frozen; the Mackey--Glass and
Lorenz--96 null remains binding.

The separately frozen compact-model comparison then completed at clean local
commit `4174095`. Every integrity gate passed, and compact transmission saved
464--648 bits versus canonical JSON CLA with identical suffix probabilities.
It produced one bounded positive on a new four-state 2-uniform source
(5,146.362 versus Markov-2 at 5,496.923 bits) and correctly rejected both
shuffled nulls, but missed the required complementary 3-uniform positive
(5,865.104 versus unigram at 5,669.836). The strict two-source gate therefore
failed. This is a synthetic finite-model-cost null, not chaos/semantic evidence;
no suffix tuning or renewed Mackey--Glass/Lorenz--96 calibration is authorized.

## Implementation principles

Update, 2026-07-18: the separately frozen ordinal-pattern attractor gate
completed at clean commit `17a0778`. Every integrity gate passed on new
Mackey--Glass initial 1.1 and Lorenz--96 x6 streams, and both shuffled nulls
were rejected, but compact CLA lost both positives to canonical LZ78:
9,235.184 versus 2,872 bits and 10,224.372 versus 3,928 bits. The all-positive
rule failed. This is an ordinal-representation coding null, not chaos,
attractor, or semantic evidence; no inspected configuration may be tuned.

Update, 2026-07-18: an additive causal ordinal-pattern symbolization seam is
unit-complete at clean local commit `a7a7e7e`. It maps finite scalar trailing
windows to deterministic order-type symbols, with explicit stable tie handling,
configurable order/delay, strictly increasing rescaling invariance, and no
fitted or suffix-informed state. Focused 8 tests / 10 subtests and the full
225-test / 10-subtest suite passed, with `py_compile` and `git diff --check`.
No scientific fixture was scored. This is representation plumbing only and
does not revise the scalar M1 Mackey--Glass/Lorenz--96 nulls. Any comparison
requires its own frozen experiment ledger on untouched trajectories with
complete-code and matched controls.

Update, 2026-07-18: an additive causal recurrence-lag symbolization seam is
unit-complete at clean local commit `de6f85f`. It encodes the most recent prior
return within an explicit radius into bounded lag classes, causally and without
fitting. Focused 8 tests / 13 subtests and the full 235-test / 23-subtest suite
passed with compilation and `git diff --check`. No trajectory was scored; a
separate frozen new-data ledger is required before any calibration.

Update, 2026-07-17: separately preregistered untouched calibration v2 completed
at clean local commit `580f917`. Every integrity gate passed on new Mackey--Glass
and Lorenz--96 x3 trajectories, but indexed CLA failed aggregate coding:
21,989.324 bits versus 6,739.904 for unigram. Joint search accepted no joint
move, so indexed joint/no-joint totals were identical. This is a coding null,
not chaos/semantic-grammar evidence; no suffix tuning or promotion is authorized.

The subsequent separately frozen necessary synthetic detector gate also failed
its positive condition at clean commit `64b3b33`: indexed CLA nearly perfectly
coded the untouched suffix of a repeated de Bruijn-5 stream (0.700 bits), but
complete model transmission brought its total to 4,600.700 bits versus
2,608.721 for unigram. The exact-marginal shuffled null was correctly not
promoted and every integrity gate passed. This blocks renewed attractor
calibration pending a new outcome-independent detector hypothesis and frozen
synthetic validation design; no fixture/code tuning is allowed.

A new hypothesis was then frozen and tested at clean commit `b3709d8` without
reusing that fixture or either attractor suffix. On a repeated Zimin-5
hierarchical source, complete indexed CLA first beat the strongest baseline at
64 suffix repeats and passed the decisive 256-repeat horizon (4,717.151 bits
versus Markov-2 at 8,515.866); the exact-marginal shuffled null never crossed.
All integrity gates and 180 tests passed. This establishes only a bounded
one-family synthetic sample-complexity region. Both Mackey--Glass/Lorenz--96
nulls remain binding, and another attractor run is not authorized; the next
gate is frozen source-family generalization on structurally distinct synthetic
generators without Zimin tuning.

That non-Zimin gate completed at clean local commit `e6e3ed2`. Every integrity
gate passed, CLA beat the strongest complete-code baseline on Thue--Morse and
correctly rejected both matched shuffled nulls, but it lost on Fibonacci word
by 288.059 bits (6,131.278 versus Markov-2 at 5,843.219). The preregistered
all-family rule therefore failed. This is a synthetic generalization null, not
chaos or semantic-grammar evidence; the Fibonacci suffix may not be tuned and
both Mackey--Glass/Lorenz--96 coding nulls remain binding.

A subsequent mechanism-specific gate was frozen before scoring at clean local
commit `d854bc7`. On two previously unscored constant-length substitutions,
indexed CLA beat the strongest preregistered complete-code baseline for both
period-doubling (5,452.003 versus 7,872.544 bits) and binary-coded
Rudin--Shapiro (9,602.305 versus 9,773.770), while both exact-marginal shuffled
nulls were correctly rejected. All integrity gates and 137 tests passed. This
supports only bounded competence aligned with uniform substitution blocks; it
does not recover the morphisms, revise the Fibonacci or attractor nulls, or
authorize renewed Mackey--Glass/Lorenz--96 calibration. The next calibration
seam is a fair decodable universal-sequence-code control on new untouched data.

The additive universal-control unit gate is now complete at clean local commit
`9737c37`. A canonical LZ78 v1 byte stream transmits its magic/version, sorted
UTF-8 token table, original length, phrase references, and terminal record;
the decoder reconstructs without external state and rejects non-canonical or
malformed inputs. Focused 14/14 and full pytest 198/198 checks passed, along
with `py_compile` and `git diff --check`. No scientific fixture was scored.
The next gate is a separately preregistered comparison on new untouched
synthetic data; the prior synthetic and attractor suffixes remain prohibited.

That universal-control comparison completed at clean local commit `4941890`.
All integrity gates passed on new Cantor and regular-paperfolding sources and
their exact-marginal shuffled nulls, but indexed CLA failed both required
positive complete-code decisions: 7,219.814 versus unigram at 2,447.226 bits,
and 7,380.844 versus unigram at 5,669.774 bits. CLA beat canonical LZ78 only on
paperfolding, not the strongest control; neither shuffled null was promoted.
This is a synthetic calibration null, not chaos/semantic evidence. No suffix
tuning or renewed Mackey--Glass/Lorenz--96 run is authorized; the next gate
requires a new outcome-independent finite-model-cost hypothesis and untouched
data with universal and simple parametric controls retained.

An additive finite-model-cost unit seam is now complete at clean local commit
`2feb70d`. Compact indexed model code v1 replaces only the verbose JSON wire
representation with a canonical tagged binary tree using minimal unsigned
varints; it retains the same shared token table, grammar, fitted counts,
category-member counts, frozen parser, ESC convention, and suffix
probabilities. Canonical JSON v1 remains available as a continuity control.
Focused 12/12 and full pytest 209/209 checks passed, along with `py_compile`
and `git diff --check`. No scientific fixture or inspected suffix was scored.
The next gate is a separately frozen new-data comparison retaining canonical
LZ78 and simple parametric controls; both Mackey--Glass/Lorenz--96 nulls remain
binding.

- Preserve the chunk/meta-symbol distinction.
- Accept edits by MDL reduction, not frequency alone.
- Preserve exact reconstruction after every accepted edit.
- Store category occurrences as `M[v]` or an equivalent explicit member side table.
- Start with hard/disjoint categories and deterministic tests.

Update, 2026-07-18: a separately frozen phase-robustness gate completed at
clean commit `a080199`. On a new three-state 2-uniform source observed at
offsets zero and one, every integrity gate passed and both shuffled nulls were
rejected, but compact CLA lost both positives to canonical LZ78: 4,257 versus
2,760 bits and 4,131 versus 2,760. The frozen rule failed. This is a synthetic
phase-robustness null, not chaos/semantic evidence; neither phase may be tuned
or rescored and the Mackey--Glass/Lorenz--96 nulls remain binding.

## Repository

Local prototype: `projects/chaos-language-algorithm/repos/chaoslang`.
Remote: `https://github.com/bgoertzel-sing/chaos-language-algorithm` (public as of 2026-07-03; sprint-1 implementation pushed to `main` at `4a7399c`).

## Relationship to OmegaSim

Ben paused OmegaSim on 2026-07-03 until CLA or a similar grammar-of-attractors detector is robust enough to evaluate whether simulated OmegaHive dynamics actually contain complex strange-attractor structure. CLA therefore becomes the current prerequisite lane for OmegaSim detector calibration.

Update, 2026-07-18: the frozen fixed-model amortization gate passed at clean
commit `d299b2f`. On a new five-state 2-uniform source compact CLA first crossed
the strongest complete-code control at 16,384 suffix symbols and won at 65,536
(28,828.051 versus Markov-2 at 60,768.987 bits); the matched shuffled null
never crossed. This bounded synthetic result does not revise the Mackey--Glass/
Lorenz--96 coding nulls or authorize attractor or semantic claims.

Update, 2026-07-18: the separately frozen long-horizon bridge failed at clean
commit `cbbebfd`. On fresh Mackey--Glass initial 0.9 and Lorenz--96 x5 scalar
streams, compact CLA never beat the strongest complete-code control at any
4,096/16,384/65,536 suffix checkpoint; both matched shuffled nulls were
correctly rejected and all integrity gates passed. The synthetic amortization
positive therefore does not transfer under this scalar M1 protocol. No tuning,
renewed scalar calibration, chaos claim, or semantic-grammar claim is licensed.

Update, 2026-07-24: the next M-D search sub-slice is acceptance-tested at
clean active-worktree commit `3a1f2e8`. Ordered composite proposals now apply
transactionally, emit one durable `Composite` edit, replay deterministically,
and leave the input state untouched when a later sub-edit fails exact
reconstruction. Focused unittest passed 34, focused pytest passed 14, required
stdlib discovery passed 222, and compileall/diff checks passed. No E0--E8
fixture or score was opened. Category/frame proposal generation, exact
official-score acceptance, proposal budgeting, and beam search remain in M-D.

Update, 2026-07-25: M-D's joint proposal-budget gap is closed at clean
active-worktree commit `db4273f`. One deterministic
`max_proposals_per_step` pool now covers singles and composites per greedy
step or beam parent; cut proposals are unscored and ledgered once. Focused
unittest passed 23, required discovery passed 249 in 45.535 seconds, and
compileall/diff checks passed. No E0--E8 measurement was opened.

Update, 2026-07-25: the prefix-fitted CSSR registry seam is acceptance-tested
at clean active-worktree commit `f4b5595`. CSSR topology fitting requires an
explicit non-empty prefix and stays separate from ordinary vocabulary-only
coders; held-out per-state KT estimators remain fresh. Focused unittest passed
8, required discovery passed 261 in 46.233 seconds, and compileall/diff checks
passed. No E0--E8 measurement was opened. The next M-E slice is the
transition-equivalence category inducer.
