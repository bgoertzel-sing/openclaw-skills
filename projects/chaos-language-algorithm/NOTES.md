# Notes

## 2026-07-27 01:15 PDT — E0 failed narrowly on uniform-v16 M2 redundancy

- The complete E0 ledger was declaration-tested without frozen-seed sampling
  and committed at notebook commit `200c2c0`; code remained clean at
  `096cbb1`. The exact `bash command.sh` then ran once, exit 0, empty stderr.
- Matching-order entropy convergence passed for every source/seed, every CTW
  band passed, Markov-source and smaller/Zipf iid M2 comparisons passed, and
  historical provenance plus four canonical-LZ78 continuity rows passed.
- All five uniform-v16 100k adaptive-Markov-2 redundancy predicates failed.
  Excesses beyond the fixed allowance were 274.625, 317.872, 318.820,
  417.373, and 438.455 bits. Aggregate E0 therefore failed.
- No tuning, threshold amendment, or rerun is permitted under v1. E1 is not
  promoted. This is coder-calibration evidence only and does not change the
  hierarchical-generativity/CSSR hypothesis, E3, or the OmegaSim pause.
- Evidence: `experiments/20260726T171500Z-e0-coder-calibration-v1/RUN.md`;
  result SHA-256
  `3f3b68b39425628f43e28f75758a7f722aba048a9d74aa4a254890dac8942f85`.

## 2026-07-26 08:30 PDT — E0 order-3 reference control authorized and added

- Ben approved the separately configured adaptive order-3 control in Telegram.
  Clean strict-replay commit `b1c501f` registers `adaptive-markov-3` with
  order 3 and standard KT `alpha=0.5`; the declared source vocabulary remains
  fixture-specific.
- The E0 programme now identifies it as the matching-order and CTW reference
  for source (d). It is explicitly E0-only: no learner default, E1--E8 base
  coder, fixture, seed, runner, ledger, or scientific result changed.
- Verification: focused coding unittest 8/8 and full stdlib discovery 278/278
  passed; `compileall` and `git diff --check` passed before commit.
- Next: freeze the still-unspecified E0 source matrices/distributions, seed
  list, CTW redundancy band, and LZ78 regression artifacts before generating
  any data or score. E3 remains binding and OmegaSim remains paused.

## 2026-07-26 08:15 PDT — E0 blocker re-audited; Ben decision still required

- The active implementation worktree
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay` remains clean
  at `4dc7304`; M-A through M-F remain closed in strict order.
- The frozen E0 text still pairs an order-3 Markov source with a requirement
  for an adaptive coder of matching order, but the frozen upgrade registry
  defines adaptive orders 0--2 only. The CTW comparison to the best matched
  Markov coder is consequently undefined for that source.
- No E0 runner, fixture, suffix, fresh seed output, experiment directory, or
  score was generated. Ben must approve and freeze either a separately named
  `adaptive-markov-3` E0 control with exact configuration or an amendment to
  the order-3 source/decision rule.
- The supplied PDF SHA-256 was reverified as
  `6969a095f1139d52fb64afa564cca7acbe40f2f79bf0f89cb4d4769fa385ebcb`.
  The main checkout's two pre-existing untracked diagnostic report files were
  left untouched. E3 remains binding; OmegaSim remains paused until E7
  resolves and E8a passes.

## 2026-07-26 04:15 PDT — E0 freezes on an undefined order-3 reference

- A post-M-F gate audit confirms M-A through M-F are closed in strict order at
  clean active-worktree commit `4dc7304`; the active worktree is clean.
- E0 is authorized by dependencies, but its frozen design contains an order-3
  Markov source while the governing upgrade registry and implementation expose
  only `adaptive-unigram`, `adaptive-markov-1`, and
  `adaptive-markov-2`. Its decision rule requires the adaptive coder of
  matching order and requires CTW to remain within its band of the best
  matched Markov coder. For source (d), both references are therefore
  undefined.
- No E0 runner, fixture, suffix, seed output, or score was generated. Adding
  an unlisted M3 arm or silently interpreting M2 as matching order would mutate
  the frozen gate. Ben's decision is required: explicitly freeze an
  `adaptive-markov-3` E0-only/control arm and its config, or amend the
  order-3 source/decision rule before measurement.
- The mathematical-foundations PDF hash was reverified as
  `6969a095f1139d52fb64afa564cca7acbe40f2f79bf0f89cb4d4769fa385ebcb`.
  Its hierarchical-generativity and sofic/CSSR statements remain hypotheses
  under assumption and citation audit. E3 remains binding; OmegaSim remains
  paused until E7 resolves and E8a passes.

## 2026-07-26 02:15 PDT — M-F public integration and closure

- The final M-F audit found that `PrequentialScorer` was implemented but not
  selectable by the public learner, and generic ledger accounting would have
  hidden inline definition costs inside data bits.
- Clean strict-replay commit `4dc7304` adds the opt-in
  `search_objective="prequential"` path without changing defaults. The same
  scorer instance is used by greedy search, Re-Pair/LZ77-SLP pruning,
  composites, and beam search; all tested paths reconstruct exactly.
- Nested initializer grammars are now defined dependency-first in the inline
  stream, with cycle detection. Ledger helpers separate parse/member/definition
  deltas without double counting and emit a seven-field breakdown whose sum
  equals the official score.
- Evidence: focused unittest passed 32 in 0.116 seconds; required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 278 in
  46.333 seconds (`47.19` seconds wall, `339348` KiB maximum RSS).
  `python3 -m compileall -q src tests` and `git diff --check` passed.
- This was unit-level implementation work only: no experiment ledger was
  required, no E0--E8 fixture or score was opened, and no remote compute ran.
  The claim that chunk CLA detects hierarchical generativity and should lose
  to CSSR on positive-entropy sofic regimes remains a hypothesis. E3 remains
  binding and OmegaSim remains paused until E7 resolves and E8a passes.

## 2026-07-25 22:15 PDT — M-F randomized inline round trips

- Added a deterministic 100-seed property test over nested ordinary chunks,
  categories, and generalized chunks. Each generated state forces the decoder
  through inner-chunk, outer-chunk, category, and generalized-chunk
  first-definition order without giving the decoder the source grammar.
- Every seed reconstructs the exact corpus, re-encodes to the identical
  decision stream, and exercises definition/member accounting across
  `alpha`/`member_alpha` values 0.25, 0.5, and 1.0.
- Evidence: focused `PYTHONPATH=src python3 -m unittest
  tests.test_inline_coder -v` passed 5/5; required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 272/272 in
  46.427 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed; clean local commit: `9402b07`.
- This is a non-measuring decoder calibration. No E0--E8 fixture, suffix, or
  scientific score was opened; the hierarchical-generativity/CSSR framing
  remains a hypothesis, E3 remains binding, and OmegaSim remains paused.
  Next is a separately frozen bounded `PrequentialScorer` contract.

## 2026-07-25 20:15 PDT — M-F inline encoder/decoder foundation

- Fresh gate audit found M-E closed at `40749d7`; governing order therefore
  permits M-F implementation but no E0--E8 measurement.
- Frozen `docs/inline-grammar-coder-contract-v1.md` in the active worktree.
- Commit `edcd8be` adds a one-part inline ideal decision stream and independent
  decoder together. Literal, ordinary chunk, and category paths use canonical
  definition-order identities, growing KT state, gamma-coded positive lengths,
  and fresh per-category member KT state. Decode exactly reconstructs the
  corpus; malformed/truncated and forward-reference inputs fail closed.
- Evidence: focused unittest 4/4; required
  `PYTHONPATH=src python3 -m unittest discover -s tests -q` 271/271;
  `python3 -m compileall -q src tests` and `git diff --check` passed.
- This is non-measuring implementation calibration. No scorer/registry/default
  changed, no E0--E8 fixture was opened, E3 remains binding, and OmegaSim
  remains paused. Before `PrequentialScorer`, add randomized generalized and
  nested-grammar round-trip coverage.

## 2026-07-25 18:18 PDT — M-E milestone closure

- Audited the governing upgrade/evaluation documents, the supplied
  mathematical-foundations source and assumption/citation sidecar, project
  records, recent run records, repository README/tests, git status, and log.
  The mathematical claims remain hypotheses under their stated source-class
  assumptions and do not amend any frozen evaluation gate.
- Clean active-worktree commit `40749d7` contains all three M-E components:
  deterministic pure-Python `CSSR`, leakage-free prefix-fitted
  `CausalStateCoder` with parameterized registry factories, and
  topology-equivalence `CSSRCategoryInducer`.
- Focused command covering the complete M-E surface passed 14 tests in 1.310
  seconds. Required `PYTHONPATH=src python3 -m unittest discover -s tests -v`
  passed 267 tests in 64.747 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No experiment ledger was required because this was a unit-level milestone
  audit with no generated scientific measurement. No E0--E8 fixture, suffix,
  score, remote compute, or OmegaSim work was opened. E3 remains binding.
  The claim that chunk CLA detects hierarchical generativity and should lose
  to CSSR on positive-entropy sofic regimes remains a scientific hypothesis.

## 2026-07-25 16:15 PDT — M-E planted automata acceptance invariants

- Froze `docs/automata-acceptance-invariants-v1.md` in the active
  `scratch/chaoslang-strict-replay` worktree at clean commit `40749d7`.
- Five deterministic, independent 10,000-symbol golden-mean fixtures all
  reconstructed exactly two causal states, exceeding the required 4/5 gate.
- CSSR fitted only on a 10,000-symbol even-process prefix; on a disjoint
  5,000-symbol suffix, a fresh causal-state KT coder used fewer adaptive data
  bits than a fresh adaptive Markov-1 coder under the same vocabulary and
  alpha. Model bits were excluded exactly as invariant 15 specifies.
- Focused unittest passed 14 tests in 0.589 seconds. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 267 tests.
  `python3 -m compileall -q src tests` and `git diff --check` passed.
- This was a unit calibration and required no experiment ledger. No E0--E8
  fixture, scientific suffix, or score was generated or inspected. E3 remains
  binding and OmegaSim remains paused. Chunk CLA as a detector of hierarchical
  generativity, with expected CSSR advantage on positive-entropy sofic
  regimes, remains a hypothesis rather than a promoted conclusion.

## 2026-07-25 14:15 PDT — M-E CSSR transition-equivalence categories

- Froze `docs/cssr-category-inducer-contract-v1.md` and added
  `chaoslang.automata.causal_categories.CSSRCategoryInducer` in the active
  `scratch/chaoslang-strict-replay` worktree at clean commit `f83e105`.
- Eligible causal states require total diagnostic support at least
  `min_support`. Candidate parse tokens must define transitions on every
  eligible state; equal ordered successor tuples form deterministic empirical
  categories. This complete-domain rule prevents missing transitions from
  producing vacuous equivalence.
- Ordinary `CategoryProposal` output preserves core semantics. Required
  `source=cssr` and canonical topology-only machine SHA-256 are exposed by
  `provenance_for`, ready for a later ledger integration slice.
- Focused unittest passed 10. Required discovery passed 265 tests in 46.705
  seconds; `python3 -m compileall -q src tests` and `git diff --check` passed.
- Contract/source/test SHA-256:
  `5e60e8ade4fd4489e3302c6eefcdc1f4e2649b4f5a6001ffd73f4a5f9afe942c`,
  `abf876eaf38266b80c5af7494b0dfdeeba913c85b5869d5927103204a2d620a2`,
  and `363cee2303534b402a67bd4f05818f2c3f9608ee08366d15f81993d655d65746`.
- No suffix, scientific score, E0--E8 fixture, remote compute, or OmegaSim work
  ran. Transition-monoid recovery and the expected CSSR advantage on
  positive-entropy sofic regimes remain hypotheses awaiting frozen gates.

## 2026-07-25 12:15 PDT — M-E prefix-fitted CSSR registry

- Clean active-worktree commit `f4b5595` freezes
  `docs/cssr-registry-factory-contract-v1.md` and exposes CSSR only through a
  distinct fitted-coder registry. The caller must supply the prefix,
  vocabulary, `max_history`, alpha, and seed; missing, unknown, empty, or
  out-of-vocabulary inputs fail closed.
- The fitted machine is passed to `CausalStateCoder`, whose held-out KT tables
  begin empty. Ordinary vocabulary-only `make_coder` remains unchanged, so
  grammar scoring cannot silently fit CSSR on the stream being coded.
- Focused unittest passed 8. Required discovery passed 261 tests in 46.233
  seconds; `python3 -m compileall -q src tests` and `git diff --check` passed.
- Contract/registry/test SHA-256:
  `2ff6d11a96060f7df802d55a7880dfb4447ade7d9b684b0deedb3e267a73b204`,
  `8bc26819e1d61c2783391318a47dff3f3787cb0268c08def67bd5ea87b39e395`,
  and `808ef70d226fc528722e5cdcffe8a727514924ad6eb1eb3ec86d26addf38ce7c`.
- No suffix, E0--E8 fixture, scientific score, remote compute, or OmegaSim
  work ran. CSSR superiority on positive-entropy sofic regimes and CLA
  sensitivity to hierarchical generativity remain hypotheses.

## 2026-07-25 08:15 PDT — M-E CSSR topology reconstruction

- Froze `docs/cssr-reconstruction-contract-v1.md` and added
  `chaoslang.automata.cssr.CSSR` plus immutable `CausalStateMachine` output.
  Training suffixes are compared with a two-sample likelihood-ratio statistic
  and an explicitly documented pure-Python Wilson--Hilferty chi-square
  threshold approximation, then refined to deterministic unifilar topology.
- The acceptance-tested active-worktree commit is `5f8e836`.
- Canonical type-qualified ordering removes hash-order dependence. The
  machine exposes transitions, suffix-to-state fallback, raw training
  emission counts, and state-occupancy entropy. The raw counts are diagnostic
  topology evidence only and are not wired into a coder.
- Focused unittest passed 3. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 256 tests in
  45.688 seconds; `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- Contract/source/test SHA-256:
  `0314959a6ddddbccadf5ffdb4922f31d7d0171569cce62dc2ef05d8ca5aec824`,
  `dd6e496c304087517990031c351da18d620cdb21145811ef3aa4e55831497db5`,
  and `f531a6bc604e1861f9eec1849ab6ef2c917ae88575fc52eda2c37644edd1aaf1`.
- No held-out code, registry control, E0--E8 fixture, suffix, scientific
  score, remote compute, or OmegaSim work ran. The claimed asymptotic CSSR
  recovery and sofic/chunk ordering remain hypotheses requiring the frozen
  evaluation gates.

## 2026-07-25 06:15 PDT — M-E direct-alphabet CTW control

- Clean active-worktree commit `759ba3f` adds a frozen bounded contract and a
  direct-alphabet context-tree weighting coder. Each suffix-tree node carries a
  KT likelihood; internal likelihoods
  mix the node KT with the product of observed child likelihoods, and only the
  active suffix path is updated.
- Registered the fixed configuration as `ctw-d8`. Tests cover deterministic
  replay, clone/reset, invalid configuration and symbols, registry exposure,
  and the governing generous redundancy sanity band against adaptive Markov-1.
- Contract/source/test SHA-256 values:
  `43163b46f0b4ee82dcedc8efbfc15b80942cfa2c9af64953f5554b0a753d5096`,
  `ae46dffb86c33d488a046442a65debeba2d51696e0d4479cb3f7b6d2ee792497`,
  and `55f87f9e1bf6e310766fd7f141e140e5e31916838ccb2ddf7624e4f580129983`.
- Focused unittest passed 4. Required discovery passed 253 in 47.277 seconds;
  compileall and `git diff --check` passed. The first full discovery attempt
  exposed the intentionally expanded exact registry tuple; updating that
  regression expectation and rerunning yielded the clean result above.
- No E0--E8 fixture, suffix, scientific score, CSSR comparison, remote
  compute, or OmegaSim work ran. Hierarchical generativity and the expected
  CSSR advantage on positive-entropy sofic regimes remain hypotheses.

## 2026-07-25 00:15 PDT — M-D composite-aware beam traversal

- Clean active-worktree commit `592df34` removes the temporary prohibition on
  combining opt-in adaptive beam search with atomic composite moves.
  Composite candidates now enter the same exact-score, digest-tied beam as
  ordinary proposals while retaining the frozen per-parent proposal budget,
  atomic reconstruction checks, mixed-second-difference evidence, ancestry,
  and one context-addressed ledger record per generated proposal.
- Budget cuts and invalid composites remain non-children with their original
  dispositions. An integration test exposed stale ordinary proposals on
  composite-derived states; these now fail closed as one
  `reconstruction_failure` record rather than aborting the traversal.
- Focused unittest passed 22 tests. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 248 tests in
  46.975 seconds; `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No E0--E8 fixture, suffix, scientific score, CSSR comparison, remote
  compute, or OmegaSim work ran. Exact official scoring remains the sole
  acceptance authority; the hierarchical-generativity/CSSR framing remains a
  hypothesis.

## 2026-07-24 M-D public beam integration

- Clean active-worktree commit `8471df2` adds opt-in `search="beam"` with a
  positive `beam_width`, restricted to the already-frozen adaptive scorer.
- Every generated single proposal is exact-scored and reconstruction-checked.
  The final state is the exact-score/digest minimum of the initial state and
  final retained beam. Only its ancestry is accepted; pruned candidates use
  `beam_pruned`, retained off-path candidates are dominated, and every
  generated proposal has exactly one SHA-256-addressed ledger record.
- Depth-qualified node identifiers prevent a repeated canonical state at a
  later depth from overwriting ancestry. Greedy/default behavior is unchanged.
  Beam plus composite moves fails closed until the next M-D slice integrates
  composite children into this traversal.
- A first focused command named stale module
  `tests.test_adaptive_initializer_api` and failed before that module ran; the
  correct module is `tests.test_adaptive_initializer_integration`.
  The corrected focused command passed 16 tests. Required stdlib discovery
  passed 247 tests in 47.205 seconds; `compileall` and `git diff --check`
  passed.
- No E0--E8 fixture, suffix, detector comparison, or OmegaSim work ran. The
  hierarchical-generativity/CSSR scientific reframing remains a hypothesis.

## 2026-07-24 18:15 PDT — M-D multi-depth beam transition

- Froze `docs/beam-traversal-contract-v1.md` and implemented `BeamNode`,
  `BeamAdvance`, and `BeamSearchPolicy.advance` at clean commit `98a1656`.
- Parent/proposal ancestry is explicit; invalid parent frontiers fail closed;
  children are exact-scored, canonical-deduplicated, and completely
  partitioned for later final-path acceptance and `beam_pruned` routing.
- SHA-256: contract
  `69289d3c57e440ef5ea1fe7116f81ee85cba320eac3acecc4a66851496a86a76`;
  implementation
  `6c78c4261728e59d028c20e531e30e5284d8c4b6e9a67e27ecffca74afff2e44`;
  test `00eeeb94c4cf6e854d1cb74a488060d9bc54067869c8cb97d365236ef491d426`.
- Focused unittest passed 8; required discovery passed 245 in 47.452 seconds;
  compileall and diff checks passed. No fixture, E0--E8 score, remote compute,
  or OmegaSim run was opened.

## 2026-07-24 16:15 PDT — M-D proposal-addressable beam disposition

- Active worktree:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Clean implementation commit: `30357a1`.
- Clean implementation commit: `972b362`.
- `BeamSearchPolicy.select_candidates` exact-scores states, deduplicates by
  canonical digest, and returns a complete disjoint retained/pruned ID
  partition suitable for `beam_pruned` ledger routing.
- Focused unittest passed 6; required discovery passed 243 tests in 46.374
  seconds; compileall and `git diff --check` passed.
- This was non-measuring. No E0--E8 fixture, suffix, score, detector
  comparison, or OmegaSim run was opened. Public multi-depth traversal and
  final-path-aware ledger emission remain next.

## 2026-07-24 14:15 PDT — M-D adaptive composite-loop integration

- Clean active-worktree commit `3c17035` exposes opt-in
  `enable_composites=True` only with the adaptive objective.
- Ordinary and composite candidates compete under one frozen
  `AdaptiveTwoPartScorer`; exact total bits alone choose the step winner.
  Composite generation retains the frozen 512 default budget, exact
  reconstruction, atomic application, mixed-difference evidence, and one
  ledger record per generated proposal including budget cuts.
- Defaults and legacy proxy/indexed paths are unchanged. Focused unittest
  passed 21; full required discovery passed 241 tests in 46.581 seconds;
  `compileall` and `git diff --check` passed.
- No E0--E8 fixture, suffix, or score was opened. M-D next requires beam
  traversal integration and explicit `beam_pruned` ledger dispositions.

## 2026-07-24 12:15 PDT — M-D adaptive initializer integration

- Froze `docs/adaptive-initializer-integration-spec-v1.md` and implemented the
  opt-in learner seam at clean active-worktree commit `a01c2c4`.
- `search_objective="adaptive"` creates one registry-backed
  `AdaptiveTwoPartScorer`. `init="repair"` and `init="lz77-slp"` receive that
  exact object for official-score pruning, after which the learner retains it
  for every proposal and final score. Legacy `init="empty"` and proxy defaults
  are unchanged; unsupported coders, initializers, and objective combinations
  fail before fitting.
- Exact reconstruction, initialization/pruning replay, and deterministic
  fixed-config results are covered. A first focused run had one test-harness
  error because it passed a `Corpus` to `replay_edits`, whose documented input
  is a symbol iterable; changing the test to `corpus.symbols` resolved it
  without implementation changes.
- Focused command covering adaptive integration, both initializers, and the
  adaptive scorer passed 17 tests. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 239 tests in
  51.762 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- Spec/source/test SHA-256 values:
  `ef3eefa40685536651388c35dfaabd951c7b03526b22325c8cbabf136467a732`,
  `db420111f477cae3a1fbcefab720c5797a06704b4cd9e0bf91fb0171811e97be`,
  and `c3b0935b0cba58b7247b6bcbc22b08b71556f01f4af2f18265015a90eefd4981`.
- No scientific fixture, suffix, E0--E8 gate, CSSR comparison, or OmegaSim run
  was opened. The hierarchical-generativity interpretation and expected CSSR
  advantage on positive-entropy sofic regimes remain hypotheses.

## 2026-07-24 10:15 PDT — M-D deterministic beam selection

- Froze `docs/beam-search-policy-spec-v1.md` and implemented
  `induction.search.BeamSearchPolicy` at clean active-worktree commit
  `c6d7b96`.
- Each selection uses one supplied official scorer, exact finite totals, and
  the scorer's canonical state digest. Equal totals use digest ordering,
  duplicate semantic states consume one slot, and every cut/duplicate state is
  returned for later proposal-ledger disposition.
- The frozen seed is configuration/replay metadata only in v1. The slice does
  not generate proposals, write proposal records, or change `CLA.simple()`;
  integration must still emit exactly one record per generated proposal and
  label beam cuts explicitly.
- Focused command passed 4 tests. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 235 tests in
  46.081 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- Spec/source/test SHA-256 values:
  `1de15d1d51bcaf4e5113cbe0d7c6e6473421bf0113c4d09986907284d34edfff`,
  `6ba60a212c7bed9fc6f25098f74baec531e9af92fe9c1c94d98bdd244f90b03b`,
  and `6d038c81d62629b267963d2a6c2278de961aa5460b14c47100ab84b70cb14c83`.
- No scientific fixture, suffix, E0--E8 gate, CSSR comparison, or OmegaSim run
  was opened. The hierarchical-generativity interpretation and expected CSSR
  advantage on positive-entropy sofic regimes remain hypotheses.

## 2026-07-24 04:15 PDT — M-D category/frame composite generation

- Added `induction/compound_moves.py` at clean active-worktree commit
  `fec7244`. The
  proposer consumes ordinary category-inducer output, groups exact immediate
  `left member right` frames, requires support >= 3 and at least two distinct
  members, selects non-overlapping width-three occurrences, and emits
  `CompositeProposal(CategoryProposal, GeneralizedChunkProposal)`.
- Candidate ordering is decreasing realized support with canonical frame,
  category, member, and occurrence tie breaks; generated chunk names avoid
  existing numeric `N*` production names.
- The canonical `a x b / a y b / a x b` test applies through `EditApplier`,
  expands exactly to the source, and leaves one durable `Composite` edit.
- Evidence: focused unittest 6/6; focused pytest 10 passed plus 1 subtest;
  required `PYTHONPATH=src python3 -m unittest discover -s tests -v` 226/226
  in 47.418 seconds; `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No exact-score learner integration, experiment ledger, scientific fixture,
  suffix, E0--E8 gate, or OmegaSim run was opened. Next is exact official-score
  acceptance plus mixed-second-difference estimator/residual wiring.

## 2026-07-24 00:15 PDT — M-D deterministic LZ77-to-SLP initializer

Clean active-worktree commit `4a05b5f` adds the reviewed
`LZ77SLPInitializer` beside Re-Pair. Its version-1 parser is deterministic,
left-to-right, longest-match, non-self-referential, and uses smallest source
position for ties; unmatched symbols remain literals. Copied phrases use a
deterministic descending power-of-two decomposition and structurally interned
balanced binary productions allocated in first-use order. Construction and
every accepted exact-score pruning transition preserve reconstruction, and
the initializer plus pruning edit log replays deterministically.

Focused pytest passed 11 tests. Required `PYTHONPATH=src python3 -m unittest
discover -s tests -v` passed 220 tests in 47.267 seconds;
`python3 -m compileall -q src tests` and `git diff --check` passed. Code,
persistence, and test SHA-256 values are
`3bea8d7627c218b941ac3c214b44fbb2f57832c72d1711e09bb2f05fe8f4b8c7`,
`d767c08772a57ea74d67c6167cbf7e370da8aec0d2e95b99cfcdc8f7dd51a4ef`,
and
`1724b05f438966660288a994759f9c4617954c0bb0fe094e5387d56e9f6a4af9`.
No scientific fixture, suffix, E0--E8 gate, or OmegaSim run was opened.
Fit-time initializer selection and full run-ledger metadata remain deferred
until the public path can reuse one frozen adaptive scorer/coder
configuration.

## 2026-07-23 20:15 PDT — M-D deterministic Re-Pair construction

At clean active-repository commit `7b85c20`, the first bounded M-D slice adds
an unpruned `RePairInitializer`. It repeatedly chooses the highest-frequency
digram, breaks ties by canonical lexicographic entry order, replaces
non-overlapping occurrences left-to-right, creates first-use `R0`, `R1`, ...
chunk rules, and records one `InitializeFromRePair` edit. Constructed tests
cover deterministic hierarchical output, exact reconstruction, tie selection,
overlap behavior, immutable input, literals/end cases, limits, and fail-closed
inputs. Focused pytest passed 16; `PYTHONPATH=src python3 -m unittest discover
-s tests -v` passed 220; `python3 -m compileall -q src tests` and `git diff
--check` passed. Implementation/test hashes are
`f5b66987147748d94732082d73352902a765751c3ff83b1567e4e0fb1d1d9036`
and
`8b3581a12c37d2d422a9bc24e0f99aa517180d1631c8b2bce488cd337269b30f`.

This is construction plumbing only. It is not yet exposed as a fit-time mode:
M-D still requires official `AdaptiveTwoPartScorer` pruning, exact replay,
public opt-in integration, LZ77-SLP, composite application/search, proposal
budgeting, and beam search. No experimental ledger, frozen suffix, E0--E8
measurement, or OmegaSim run was opened. E3 and all promotion gates remain
binding.

## 2026-07-23 — adaptive upgrade M-B instrumentation

At clean active-worktree commit `46ffbfe`, the induction loop can write one
stable JSONL `ProposalRecord` per generated proposal plus
`final_breakdown.json`. Both proxy and indexed search preserve their prior
selection/tie semantics; the default public API remains ledger-free unless a
directory is supplied. The mandatory legacy complete-code regression records
data/model/total deltas `-6232/+6296/+64`, rejects the proposal, and labels it
`positive_delta`. Focused pytest passed 17; stdlib discovery passed all 216
tests; `compileall` and `git diff --check` passed. No experiment trajectory,
suffix, detector score, or OmegaSim A6 result was generated or inspected.

## 2026-07-23 — durable failed-artifact deletion

Applied Research Rules 1, 2, 5, 6, and 7 without reopening a measured ledger.
At active-repository commits `3d5224d` / `8e8b042`, failure cleanup now
`fsync`s the same opened parent directory after identity-guarded unlink, so a
possibly durable stale artifact entry cannot survive the reported cleanup
without an explicit durability failure. Constructed tests prove event ordering
and preserve the original failure as the cause when cleanup `fsync` fails.
The first focused run passed 30 and failed three old call-count assertions;
after updating those assertions to require the new cleanup barrier, focused
pytest passed 33, full pytest passed 320 tests / 93 subtests, stdlib discovery
passed 209 tests, and `compileall` plus `git diff --check` passed. Spec/code/
test SHA-256 values are
`27e08d89271b5f0cda7152467749f3ac75c10db465bed4d35364fc69b2dac5a4`,
`7d9e3de6c712ac0df5f0d19d4d584bea2cc7b9771d3e1f66b625b5296016baf9`,
and `b955100024aae55bc60133fb84e3437da941cce91914f09a9b84f8c8b725ab9b`.
No Mackey--Glass, Lorenz--96, held-out suffix, detector score, or coding score
was generated or inspected.

Hyperseed reading: a failed publication is a state transition from a transient
directory entry back to absence. Durability must cover that inverse transition
just as it covers successful creation; otherwise the evidence channel's
reported state and crash-recovered state can diverge. This is provenance
plumbing, not chaos, attractor/source-law, CLA/compression, or semantic-grammar
evidence.

## 2026-07-23 - CLA experiment synthesis and repair diagnostic

Applied Research Rules 1, 2, 4, 5, 6, and 7 to Ben's requested detailed CLA
status PDF. The report reconciles frozen ledgers through July 23 without
rerunning or rescoring any closed fixture. Direct conclusions: engineering
integrity and null handling are generally sound; low-cardinality symbolization
repairs Cartesian alphabet explosion; linear VAMP failed matched PCA controls;
synthetic complete-code wins are real but family- and horizon-limited;
attractor grammar coding remains negative; nearest-neighbor divergence Stage A
passed but the subsequent Stage-B CLA code lost to LZ78; and all 120 OmegaSim
A6 role-specific cells yielded trivial grammars. The proposed repair order is
transparent score decomposition, oracle representability, search ablations,
hybrid probabilistic residual coding, and only then fresh attractor/OmegaSim
calibration. Artifact:
`repos/chaoslang/docs/cla_experiments_and_repair_diagnostic_20260723.pdf`,
SHA-256
`fdb6f48970165a27784d2c64c04eaa8744274f5a54c068bb1badbf710703b0f6`.

## 2026-07-23 - Post-validation ancestor-alias rejection

Applied Research Rules 1, 2, 5, 6, and 7 without opening a measured ledger.
An audit found that initial ancestry validation plus final parent device/inode
identity did not reject an ancestor replaced during persistence by a symlink
to the same opened directory. The active repository first froze final
full-ancestry revalidation at commit `0b07cfa`, then implemented it with a
constructed replacement regression at clean commit `8eabc2c`. Exact
validation was `python3 -m pytest -q tests/test_experiment_artifacts.py &&
python3 -m pytest -q && python3 -m unittest discover -s tests -q && python3 -m
compileall -q src tests && git diff --check`: focused pytest passed 31, full
pytest passed 318 tests / 93 subtests, and stdlib discovery passed 209 tests.
Spec/emission/code/test SHA-256 values are
`071e1dc11f5e675b86a358961e3ed9194d5a3612341509b7ca5ecb17a03cfd2a`,
`ad694b9d1a0cb11bbea1e63b2569bc1c194c32dc7b168413b668862d6bff352a`,
`cdbe21a5e60112bed019ccb0dc00ed2aac532ae6e8c9c2bbc0a1181f8213405d`,
and `5566096dadb362de367b2ee48422b169557734f62a365fe1edf96633e0b26214`.
No Mackey--Glass, Lorenz--96, held-out suffix, benchmark, or scientific score
was generated or inspected. Hyperseed reading: lexical directness and object
identity are independent provenance predicates; satisfying one cannot stand
in for the other. This changes no detector or complete-code outcome.

## 2026-07-23 - Identity-descriptor reproducibility audit

Applied Research Rules 1, 2, 5, 6, and 7 without opening or rerunning a
measured ledger. At clean active-repository commit
`11cd2b3655f27671eb5d585a741dddf3bf46cb8d`, reran the constructed
identity-descriptor subgate and repository checks:
`python3 -m pytest -q tests/test_experiment_artifacts.py && python3 -m pytest
-q && python3 -m unittest discover -s tests -q && python3 -m compileall -q src
tests && git diff --check && git status --short`. Focused pytest passed 30,
full pytest passed 317 tests / 93 subtests, stdlib discovery passed 209 tests,
and compilation/diff/clean-status checks passed. The stdlib suite emitted its
existing diagnostic benchmark summaries; these were test diagnostics, not a
new experiment ledger or held-out outcome.

Canonical artifact spec, emission spec, implementation, and focused-test
SHA-256 values were respectively
`750276479b6c372f5e91e150ab6ca13e5debcea349e7d892c8dda06a844f51d0`,
`32da8c0d28079d7b05322ca547e626347d1a11096aa4e9e3c03a1f358dc789bf`,
`b56f9b7701e4939e4d017c64fe672e2aefe7a54c25d886253f723f1a29f98dcb`,
and `d051cd92afd2beebd8260c5d913e0e1901ac29b06fa071034ba4d3e984f1193f`.
No frozen held-out suffix was regenerated or rescored, and no detector,
complete-code, chaos, attractor/source-law, or semantic-grammar conclusion
changed. The Mackey--Glass/Lorenz--96 Stage-A pass and Stage-B null remain
binding and untuned.

## 2026-07-23 - Identity-bound descriptor lifecycle validation

Applied Research Rules 1, 2, 5, 6, and 7 without reopening a closed suffix.
The active repository
`/home/openclaw/research-agent/scratch/chaoslang-strict-replay` first froze the
descriptor-lifecycle invariant at commit `58c309d`, then constructed tests at
clean commit `11cd2b3655f27671eb5d585a741dddf3bf46cb8d` proved the internal
identity-bearing descriptor is closed after successful emission and after
read-back, stdout-write, and stdout-flush failures. Focused pytest passed 30;
full pytest passed 317 tests / 93 subtests; stdlib discovery passed 209 tests;
`python3 -m compileall -q src/chaoslang tests`, `git diff --check`, and clean
status passed. SHA-256 values for the measured-emission spec, canonical
artifact spec, and constructed test are
`32da8c0d28079d7b05322ca547e626347d1a11096aa4e9e3c03a1f358dc789bf`,
`750276479b6c372f5e91e150ab6ca13e5debcea349e7d892c8dda06a844f51d0`,
and `d051cd92afd2beebd8260c5d913e0e1901ac29b06fa071034ba4d3e984f1193f`.
No benchmark, Mackey--Glass/Lorenz--96 fixture, held-out suffix, or scientific
score was generated or inspected. The nearest-neighbor Stage-A pass and
prefix-quantized Stage-B complete-code null remain frozen and untuned.

- 2026-07-23 00:15 PDT: implemented the already-frozen identity-bound
  read-back seam at clean active-repository commit
  `a9c0bf26e86dd4b6ab403b1467506efe58c0ff47`. Persistence duplicates the
  newly created artifact descriptor before the write stream closes, and
  emission seeks and reads that retained identity after durability rather
  than reopening the lexical path. Constructed target- and parent-replacement
  regressions prove replacement bytes cannot reach stdout. Exact validation:
  `python3 -m pytest -q tests/test_experiment_artifacts.py`; `python3 -m
  pytest -q`; `python3 -m unittest discover -s tests -v`; `python3 -m
  compileall -q src tests`; `git diff --check`. Results: focused pytest 26,
  full pytest 313 tests / 93 subtests, stdlib discovery 209 tests; compilation
  and diff check passed. Source/test/spec hashes:
  `b56f9b7701e4939e4d017c64fe672e2aefe7a54c25d886253f723f1a29f98dcb`,
  `c70d659f8c654af87bf3029dc15774993e050fd1a84a44745fd6128e2525c311`,
  `ad878daca89ecc9d3d2aea4c618bbcd138f954198c7948569f1fa944f7527d2a`,
  and `03ed98154797bedc845b253b80fd85b2dfecc58a7d97d6fe21e08ca49ae78a16`.
  No benchmark, Mackey--Glass/Lorenz--96 fixture, held-out suffix, or
  scientific score was generated or inspected. Under Research Rules 1, 2, 5,
  6, and 7, this is replaceable provenance plumbing: retaining an open
  descriptor preserves intensional object identity across mutable extensional
  names, but supplies no detector, coding, chaos, attractor/source-law, or
  semantic-grammar evidence.

- 2026-07-22 22:15 PDT: a read-only code/spec audit identified a remaining
  provenance race: `persist_and_emit_canonical_json` reopened the lexical
  artifact path after the parent-bound writer returned. Active-repository spec
  commit `c3b9971ac4791bc9b3d59f07bd3d0759b69d6895` now requires identity-bound
  read-back and constructed parent/target replacement tests before
  implementation. Exact validation command:
  `python3 -m pytest -q tests/test_experiment_artifacts.py && python3 -m
  pytest -q && python3 -m unittest discover -s tests -q && python3 -m
  compileall -q src tests && git diff --check && sha256sum
  docs/canonical-result-artifact-spec-v1.md
  docs/measured-result-emission-spec-v1.md && git status --short --branch`.
  Focused pytest passed 24, full pytest 311 tests / 93 subtests, and stdlib
  discovery 209 tests. Spec SHA-256 values are
  `ad878daca89ecc9d3d2aea4c618bbcd138f954198c7948569f1fa944f7527d2a`
  and `03ed98154797bedc845b253b80fd85b2dfecc58a7d97d6fe21e08ca49ae78a16`.
  No benchmark, Mackey--Glass/Lorenz--96 fixture, held-out suffix, or
  scientific score was generated or inspected.

- 2026-07-22 20:15 PDT: independently audited the parent-bound canonical
  result seam at clean active-repository commit
  `e893704e7a50b2ced32ff0cf4c42bd82714b2a26`. Exact command:
  `python3 -m pytest -q tests/test_experiment_artifacts.py && python3 -m
  pytest -q && python3 -m unittest discover -s tests -v && python3 -m
  compileall -q src tests && git diff --check && git status --short --branch`.
  Focused pytest passed 24, full pytest passed 311 tests / 93 subtests, and
  stdlib discovery passed 209 tests; compilation, diff check, and clean status
  passed. Canonical-artifact spec, emission spec, implementation, and test
  SHA-256 values were respectively
  `58dddff39803dbda1b7ac7a6f1a3af4163fca46e1e37b8ad2464d172e1a9c437`,
  `5a6854ccbb443de9a3a3677020c8cdc314aacb4f667bec86e73605ffddfb6268`,
  `9e3b846bdcae598fc1b89c4577d8879a94700d3d9694d39658a49603a93da6bf`,
  and
  `c6206258bac472ee2f634c72add181abae6054f5b387f78d26be6f5503e80d14`.
  This applied Research Rules 1, 2, 5, 6, and 7 to constructed provenance
  plumbing only. No benchmark command, Mackey--Glass or Lorenz--96 fixture,
  held-out suffix, or scientific score was generated or inspected. The
  nearest-neighbor Stage-A pass and prefix-quantized Stage-B complete-code null
  remain frozen and untuned.

- 2026-07-22: Implemented the already-frozen canonical-result parent-identity
  contract at clean active-repository commit `e893704`. The persistence seam
  opens the direct parent once, compares descriptor and lexical identities,
  creates/stat/unlinks the target relative to that descriptor, fsyncs the same
  descriptor, and rejects a replaced lexical parent before success. Constructed
  race coverage passed; focused pytest 24, full pytest 311 tests / 93 subtests,
  stdlib discovery 209 tests, `compileall`, and `git diff --check` passed. This
  is provenance plumbing only: no Mackey--Glass, Lorenz--96, scientific fixture,
  benchmark, or held-out suffix was generated or scored.

## 2026-07-22 — clean provenance-code reproducibility audit

At clean active-repository commit
`aa5ab900d3778c4e33109c2a5997d5187c66b63e`, reran only the constructed
artifact tests and code suites: focused pytest passed 23, full pytest passed
310 tests / 93 subtests, stdlib discovery passed 209 tests, and `compileall`,
`git diff --check`, and clean status passed. Spec/code/test SHA-256 values were
`12f230325fd5fb4bb003ceecee4d5d7dd83035cd08ffabca3f76daa2c7c20129`,
`e7c01f4144f5e802f69cf6e6c06c4c628e89dfca30113aad253a99ad7b5c70c0`, and
`dceb5162820be27ebbd53f1023362038f78141b9157e36354cec57df3a52e999`.
No benchmark command, Mackey--Glass or Lorenz--96 fixture, held-out suffix, or
scientific score was generated or inspected. The passed nearest-neighbor
Stage-A calibration and failed Stage-B complete-code decision remain frozen.

## 2026-07-22 — canonical result target-alias regression

- Active repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Clean local commit: `bd55fe2a2205aad5fd048c2f3035018b263d5671`.
- The artifact contract now explicitly includes target aliases in its
  no-overwrite boundary. A constructed test creates a result-path symlink,
  attempts publication, observes `FileExistsError`, and proves both the link
  and authoritative referent bytes are unchanged.
- Verification: focused pytest 22; full pytest 309 tests / 93 subtests;
  stdlib discovery 209; `compileall`; and `git diff --check`.
- No Mackey--Glass, Lorenz--96, scientific fixture, or held-out suffix was
  generated, rerun, or scored. This is provenance plumbing, not detector,
  coding, chaos, attractor/source-law, or semantic-grammar evidence.

## 2026-07-22 direct canonical-result ancestry boundary

Applied Research Rules 1, 2, 5, 6, and 7 without measuring a scientific
fixture. Clean active-repository commit `ab2ba52` extends the measured-result
contract and implementation to reject symbolic links in every supplied
artifact-parent ancestor before exclusive creation. A constructed nested-alias
regression proves no artifact is created in the alias target. The first focused
run exposed only an expected-error-message mismatch; after correcting that
constructed assertion, focused pytest passed 21, full pytest passed 308 tests /
93 subtests, stdlib discovery passed 209 tests, and `compileall` plus `git diff
--check` passed. Spec/code/test SHA-256 values are
`16321d8b730460ce47e20f63609fe64f667b3b7a23421f44389bccbdb24e565a`,
`9fd8c37800166de12cb318fe07835471ab67ebe3f991f7c9e6e38abd5f133f85`,
and `c14db27e6b348579c2b86507b732f0b35d823db8483ee5e89ef9e501cea68ee3`.
No Mackey--Glass, Lorenz--96, held-out suffix, or detector score was produced.

Hyperseed reading: evidence identity depends on the whole path relation, not
only the final parent/name pair; an ancestor alias changes that relation while
preserving the lexical suffix. This is provenance plumbing, not detector,
coding, chaos, attractor/source-law, or semantic-grammar evidence.

## 2026-07-22 direct canonical-result parent boundary

Applied Research Rules 1, 2, 5, 6, and 7 without measuring a scientific
fixture. Spec-first active-repository commits `995903b` / `732cdb2` require an
existing directly addressed artifact parent and reject a symbolic-link parent
before exclusive creation. A constructed regression proves no artifact is
created in the alias target. Focused pytest passed 20; full pytest passed 307
tests / 93 subtests; stdlib discovery passed 209 tests; `compileall` and `git
diff --check` passed. Spec/code/test SHA-256 values are
`5d9acd38aac5e07db3ee721b3c45cdc74cb477ba7804ce83295ae9a7a27d5191`,
`080231ca4c4f1e773fec5bbc71ce11ad65bc71814da9ce60366cc805d00dc13b`,
and `31a9973710c08797bbbf33e984d52157cc7d4af7021b4aebaef6842860ab94ae`.
No Mackey--Glass, Lorenz--96, held-out suffix, or detector score was produced.

Hyperseed reading: the preregistered artifact name denotes evidence only under
its frozen parent relation; a symlink alias changes that relation without
changing the spelling. Rejecting the alias preserves provenance identity. This
is publication plumbing, not detector, coding, chaos, attractor/source-law, or
semantic-grammar evidence.

## 2026-07-22 stdout write-failure artifact preservation tests

Applied Research Rules 1, 2, 5, 6, and 7 without measuring a scientific
fixture. Constructed tests at clean active-repository commit `0a4a7da` now
exercise a raised `BrokenPipeError` and incomplete/non-integer stdout writes,
proving that the canonical result artifact already persisted by the command
boundary remains byte-exact and authoritative. Focused pytest passed 19; full
pytest passed 306 tests / 93 subtests; stdlib discovery passed 209 tests;
`compileall` and `git diff --check` passed. Test SHA-256:
`9b285babfbe74c7c4f9bd733b6d77eb6f96e853dfba77d63757885e80424f765`.
No Mackey--Glass, Lorenz--96, held-out suffix, or detector score was produced.

Hyperseed reading: persistence and display are distinct evidence-channel
relations. Once canonical bytes are durable, a transport failure changes only
observability, not the measured fact, and therefore cannot license a rerun.
This is provenance validation, not detector, coding, chaos, attractor/source-
law, or semantic-grammar evidence.

## 2026-07-21 measured artifact read-back verification

Applied Research Rules 1, 2, 5, and 7 without measuring a scientific fixture.
The spec-first change at clean active-repository commits `17a11ac` / `ecbeaa4`
requires `persist_and_emit_canonical_json` to hash the durable artifact's
read-back bytes and compare them with the writer digest before stdout. Tests
cover changed bytes and read failure leaving stdout untouched. Focused pytest:
16 passed; full pytest: 303 tests / 93 subtests; stdlib discovery: 209 tests;
`compileall` and `git diff --check`: passed. Spec/code/test SHA-256:
`30128c8d449914098d4245b2044bda9bd315ae4b90ec0c8641e8ec2b10384abe`,
`28d05b9c7d6085dee1fb544a57979b49e98a2dae58b4508976c9c0062c545f9c`,
and `8db3b4ea64bc55f13d30f9793b8c17c32f9e0ddeb7e1e5595056084d8844b5ee`.
No Mackey--Glass, Lorenz--96, held-out suffix, or detector score was produced.

Hyperseed reading: this strengthens the evidence-channel identity relation
between durable bytes, their digest, and emitted bytes. It changes provenance
plumbing only, not the frozen detector or complete-code nulls.

## 2026-07-21 - Durable canonical artifact directory entry

Applied Research Rules 1, 2, 5, 6, and 7 without reopening a closed suffix.
Spec-first active-repository commits `edbf285` / `898d1cb` require canonical
result persistence to fsync the completed artifact and then its existing
parent directory before success can permit stdout. Constructed tests prove the
ordering, directory descriptor closure, and cleanup of only the newly created
target when directory fsync fails. Focused pytest passed 14; full pytest passed
301 tests / 93 subtests; stdlib discovery passed 209 tests; `compileall`, `git
diff --check`, and clean active-repository status passed. Spec/code/test
SHA-256 values are `518876086400fd1e0c044e9f67f2be8c913dd2ad33376ef7feddd28e2d763089`,
`5b09056368b948e32e630d7a28609a2901848ab7ccb54e75568d896a527fd9d4`,
and `17a0f389aa7d43c3f4250efdb3f62dfaf2eae6ba8b4c6d75085c607ab2397c2d`.
No Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
generated, rerun, or scored. This is provenance plumbing only.

## 2026-07-21 - Failed artifact cleanup boundary

Applied Research Rules 1, 2, 5, 6, and 7 without reopening a closed suffix.
Spec-first active-repository commits `d04453a` / `4ff7ab8` require a failed
write, flush, or artifact `fsync` to remove only the target created by that
call; pre-existing targets remain protected by exclusive creation. Constructed
tests cover incomplete writes and `fsync` failure. Focused pytest passed 13;
full pytest passed 300 tests / 93 subtests; stdlib discovery passed 209 tests;
`compileall`, `git diff --check`, and clean status passed. Spec/code/test
SHA-256 values are `259f2a26bf3737a5a1209af4b084cbaee2e93f31ce1faf9cd0c743e87f4d32e2`,
`af85e4fcea2474ed41dbb62fc7627ad58ac8aaa3b9d3002222757cb9c9c25110`, and
`1cb0d97362920d72e891e196e67cac7eb89b2e201679fe5cec2d6d1b5536cda4`.
No Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
generated, rerun, or scored. This is provenance plumbing only.

## 2026-07-21 - Durable canonical artifact boundary

Applied Research Rules 1, 2, 5, 6, and 7 without reopening any closed suffix.
The spec-first active-repository commits `037578f` / `500696f` strengthen the
canonical result writer: a complete byte count is mandatory, then the stream
is flushed and `fsync`ed before success can permit stdout emission. Constructed
tests cover the durability call and incomplete-write rejection. Focused pytest
passed 12 tests; full pytest passed 299 tests / 93 subtests; stdlib discovery
passed 209 tests; `compileall`, `git diff --check`, and clean status passed.
Spec/code/test SHA-256 values are
`020f29f3c201e387b4d23015db19842350563ab88602c16a75c11b304e4c43f5`,
`16352966a8c446f24835cf16a5d9ef5ddd3a0638b4ac3dafea89c2b08f525433`,
and `2e49543689806cbf6ada9cd45718445778b3a8e4a3cfdf27669ed1d2cb2da7d5`.
No Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
generated, rerun, or scored. This is provenance plumbing only.

## 2026-07-21 - Fail-closed measured-result emission boundary

Applied Research Rules 1, 2, 5, 6, and 7 without reopening any closed suffix.
Spec commit `b0db6ab` precedes implementation commit `ac1bcc7` in the clean
active worktree. `persist_and_emit_canonical_json` first uses the canonical
no-overwrite artifact writer, then reads and emits those exact persisted bytes;
artifact creation failure emits nothing, and non-integer, Boolean, or short
output writes fail closed. Focused pytest passed 10 tests; full pytest passed
297 tests / 93 subtests; stdlib discovery passed 209 tests; `compileall`,
`git diff --check`, and clean-status checks passed. Spec/code/test SHA-256 are
`ffd67c10f8a1039b906b898f9fb9a7ab191f688416cb70292b23a9342e0d8670`,
`81a30efec1e76ff9866f92af30105fef097a336b7e8f8c772f15878dc5942606`,
and `c7430a96336adfeaab9d816533096527301728fb8ca7a417b4dbe4db46f97e18`.
This is provenance plumbing only; no Mackey--Glass, Lorenz--96, held-out
suffix, or other scientific fixture was generated, rerun, or scored.

## 2026-07-21 - Canonical result-artifact persistence seam

Applied Research Rules 1, 2, 5, 6, and 7 to the Stage-B provenance limitation
without rerunning or inspecting any closed suffix. In the documented active
worktree, spec commit `e715eed` defines a replaceable canonical JSON artifact
contract; code commit `274529a` adds a fail-closed writer that uses sorted
compact UTF-8 JSON with a terminal newline, rejects non-finite values and
existing targets, requires an existing parent, and returns the exact byte
SHA-256. Focused pytest passed 5 tests; full pytest passed 292 tests / 93
subtests; stdlib discovery passed 209 tests; `compileall`, `git diff --check`,
and clean-status checks passed. Spec/code/test SHA-256 values are
`263c4825bd51874f504ae87d39106a56e27b63365a35f6c8be26bd12ce2758ba`,
`cbb9674867559440dca7c19a595ad91c0680db8e3cafff1d7a9508c843bf2831`,
and `9bac23c1948e5a3fce3e45327a04ffeebc24a3df4e9bc55090d22687190cfbd5`.
This is provenance plumbing only, not detector, coding, chaos,
attractor/source-law, or semantic-grammar evidence.

## 2026-07-21 - Stage-B result-artifact provenance limitation

A read-only artifact audit confirmed the frozen runner, declaration-test, and
command SHA-256 values, but found that the decisive JSON stdout was summarized
in `RUN.md` rather than retained as a separate committed artifact. The closed
benchmark was not rerun and no output was reconstructed. Active-repository
commit `0356c73` records this limitation and requires future measured ledgers
to predeclare a canonical result path and commit its unchanged SHA-256.

Full pytest passed 287 tests / 93 subtests; stdlib discovery passed 209 tests;
`compileall` and `git diff --check` passed; the active worktree is clean. This
changes neither the failed Stage-B decision nor its bounded non-claim.

## 2026-07-21 - Post-result Stage-B integrity audit

Without rerunning the frozen benchmark or inspecting/tuning any suffix, audited
active-repository commit `cb31e74` after the recorded Stage-B null. Focused
Stage-B/quantizer pytest passed 5 tests / 9 subtests; full pytest passed 287
tests / 93 subtests; stdlib discovery passed 209 tests; `compileall` and
`git diff --check` passed; the worktree remained clean. Exact audit command:
`python3 -m pytest -q tests/test_prefix_vector_quantizer.py tests/test_nearest_neighbor_stage_b.py && python3 -m pytest -q && python3 -m unittest discover -s tests -q && python3 -m compileall -q chaoslang tests && git diff --check && git status --short`.
This verifies the recorded code/ledger state only and creates no new scientific
measurement or evidence.

## 2026-07-21 - Fresh prefix-quantized Stage-B complete-code null

Applied Research Rules 1, 2, 5, 6, and 7. The runner/schema commit `7bad170`
passed focused pytest (5 tests / 9 subtests), full pytest (287 / 93 subtests),
stdlib discovery (209 tests), `compileall`, and `git diff --check`. A declaration
test generated all fresh fixture and symbol hashes without fitting CLA or
scoring a suffix. The ledger/command were then frozen at clean commit `22f1450`
before the exact command ran once.

All six fixture integrity gates passed; both shuffled nulls were rejected and
compact CLA beat JSON CLA throughout. The strict gate failed because compact
CLA lost to canonical LZ78 on both positives: six-delay Mackey--Glass
8,824.829 vs 744 bits; coordinate-complete Lorenz--96 8,482.142 vs 1,240 bits.
No tuning, rescoring, remote compute, or remote mutation occurred. This tests
finite description length in a prefix-fitted extensional quotient; it does not
identify the intensional flow law or semantics.

## 2026-07-20 - Prefix-vector-quantizer unit subgate

Applied Research Rules 1, 2, 5, 6, and 7 in the documented active worktree.
The plain-language contract at commit `313452d` preceded the additive code and
constructed tests at `ca3e48f`; README guardrail commit `21e9fdf5e56e8adb3aa34eaea362d5b356697e9a`
keeps scientific Stage B behind a separate frozen ledger. The immutable
quantizer fits coordinate-wise population standardization on its supplied
prefix, uses deterministic farthest-first/Lloyd fitting, canonicalizes centers
lexicographically, and assigns same-dimensional later states without refit.

Focused pytest passed 4 tests / 9 subtests; full pytest passed 286 tests / 93
subtests; stdlib discovery passed 208 tests; `compileall` and `git diff
--check` passed. Spec/code/test/README SHA-256 values were respectively
`972c304a0250435fceac5a09a815e963cedf4bded44f955bdb9be0f78aa740fb`,
`bb2e7e70cc0b3506ee1e1327c7e6263b7230759b5b84cefa48d7570bd809ec47`,
`c2af43c66dd88cb0565383f6ea0c87a5bbd36cb10061b80400641fcbf5bc11c3`,
and `61ffada847eeb06f358ec31c2b6ca03ec896b8ad90e7d7930903ded1ffae209d`.
No Mackey--Glass, Lorenz--96, or held-out suffix was generated or scored.

Hyperseed reading: the quantizer defines a finite extensional quotient in
prefix-standardized observation geometry; it does not recover the intensional
flow law. Quantizer, detector, learner, and complete-code decision remain
replaceable seams. A timestamped frozen Stage-B ledger is still required.

## 2026-07-20 - Stage-B design boundary after nearest-neighbor calibration

Added `docs/nearest-neighbor-stage-b-design-spec-v1.md` in the documented
active worktree. The outcome-independent design retains Stage A's six-delay
Mackey--Glass and full eight-coordinate Lorenz--96 abstractions while placing a
replaceable prefix-only quantizer between continuous states and CLA. It closes
all inspected Stage-A and coding fixtures, requires new positive/stable/shuffled
fixtures plus canonical literal, unigram, Markov-1, Markov-2, and LZ78 controls,
and freezes an every-positive/no-shuffled-null complete-code rule. This is a
software/scientific boundary specification under Research Rules 1, 2, 5, 6,
and 7; no scientific fixture or held-out suffix was generated or scored. The
next authorized subgate is constructed-data quantizer specification and unit
validation before a separately frozen experiment ledger. Clean active-repo
commit `33483b6`; full pytest passed 282 tests / 84 subtests, stdlib discovery
passed 204 tests, and `compileall` plus `git diff --check` passed. Spec SHA-256:
`ed8e338064cafc5f46da8028653ce1bdf4abed22d9d4583d3785c32bbac7cb76`.

## 2026-07-20 - Nearest-neighbor Stage-A v2 passed

After v1's pre-score failure, v2 preserved every scientific choice and froze
only an explicit runner result for the exact no-positive-distance-pair stable
case. Clean commit `85667bd0937eef0de8023db8d7462c6d3afc73a5` passed focused
pytest 8 tests / 4 subtests, full pytest 282 / 84 subtests, stdlib discovery
204 tests, `compileall`, and `git diff --check` before measurement. The exact
`bash command.sh` run exited 0: Mackey--Glass positive 0.019656759765072553,
stable degenerate/non-promoted, shuffled -0.00016819136492626706; full-state
Lorenz--96 positive 0.013052857377956398, stable -0.0002188829856632411,
shuffled -0.000052087819800855637. The all-six Stage-A gate passed. Stage B
remains unauthorized until separately frozen. No tuning, rescoring, remote
compute, or remote mutation occurred.

## 2026-07-20 nearest-neighbor Stage-A v1 pre-score failure

Executed the exact frozen `bash command.sh` once. It exited 1 after about 13.5
seconds before emitting JSON or any detector score: the statistic raised
`ValueError: no eligible positive-distance neighbor pair exists` on a frozen
stable fixture. The command's `set -e` prevented result/timing/status artifact
creation. The active repository remained clean and `git diff --check` passed.
This is a harness/protocol failure, not a scientific calibration outcome. No
fixture or statistic choice may be tuned and v1 may not be rerun. Stage B stays
closed; any v2 must freeze unchanged scientific choices plus a synthetic
stable-fixture end-to-end schema gate before execution. Provenance:
`experiments/20260720T211500Z-nearest-neighbor-calibration-v1/RUN.md`.

## 2026-07-20 nearest-neighbor Stage-A freeze

Froze, but did not execute, the fresh nearest-neighbor divergence Stage-A gate
at clean active-repository commit `ee0485c18d77a02d4ee718d5760ade25e4d39793`.
The ledger fixes fresh Mackey--Glass/full-state Lorenz--96 positive, stable, and
shuffled fixtures; causal delay/full-vector representations; prefix-only
standardization; statistic settings; threshold; seeds; hashes; exact command;
and the all-positive/no-control rule. Focused pytest passed 6 tests / 4
subtests, full pytest 280 tests / 84 subtests, stdlib discovery 202 tests,
`compileall`, and `git diff --check` passed. No scientific score was produced.
Provenance: `experiments/20260720T211500Z-nearest-neighbor-calibration-v1/RUN.md`.

Hyperseed reading: this freezes an extensional finite-sample local-separation
test in an explicit observation geometry; it does not identify the intensional
flow law. Representation, statistic, decision policy, and any later CLA coding
gate remain modular seams. Stage B stays closed.

## 2026-07-20 nearest-neighbor divergence unit seam

Applied Research Rules 1, 2, 5, 6, and 7 without loading or scoring a
scientific trajectory. The plain-language contract at clean commit `fd9e4b0`
preceded the additive implementation at clean commit `ed53fb4`. The statistic
selects deterministic Euclidean nearest neighbors under an externally supplied
Theiler exclusion, averages evolved log distances, and fits only an externally
supplied lag interval. Focused pytest passed 4 tests / 4 subtests; full pytest
passed 278 tests / 84 subtests; stdlib discovery passed 200 tests; `compileall`
and `git diff --check` passed. The active worktree is clean.

Hyperseed reading: the statistic measures an extensional local-separation
relation in a chosen observation/embedding geometry. It neither identifies the
intensional evolution law nor distinguishes deterministic instability from all
stochastic spreading by itself. Its replaceable interface keeps embedding,
metric, neighbor selection, and promotion policy as explicit seams. A later
measurement must separately freeze fresh Mackey--Glass and coordinate-complete
full-state Lorenz--96 positives and matched stable/shuffled controls before any
outcome inspection; Stage B remains prohibited.

## 2026-07-20 repeated-renormalization statistic unit seam

Applied Research Rules 1, 2, 5, 6, and 7 without measuring a scientific
fixture. The plain-language specification preceded implementation at clean
active-repository commits `354e48b` and `3abebb1`. The additive statistic owns
only aggregation of externally supplied renormalization cycles:
`sum(log(final/initial)) / sum(elapsed_steps)`. It owns no generator,
perturbation, delay-state representation, renormalization operation, cycle
length, threshold, or promotion rule.

Focused pytest passed 3 tests / 8 subtests; focused stdlib passed 3 tests; full
pytest passed 267 tests / 75 subtests; stdlib discovery passed 189 tests;
`compileall` and `git diff --check` passed. Spec/code/test SHA-256 values were
`88b333b81b32426c38bd74fe48b9cc8ae73d19fcc7fed69ed56aaed472e1624c`,
`43766dd24ea353e21c7720981b1aab967df0a950ea200605c004414b0df21bc1`,
and `aaaa609af73c0e383f61abb8a915b0ae4b23591f3554dc99a64b48dbec70734e`.
The worktree was clean after commit. No Mackey--Glass, Lorenz--96, held-out
suffix, or threshold was scored.

Hyperseed reading: repeated renormalization estimates an average local
expansion relation while restoring infinitesimal scale, but finite results
still depend on state representation and perturbation transport. It is not a
validated Lyapunov estimator, chaos proof, attractor/source-law identifier,
CLA result, or semantic-grammar evidence. A separate untouched-data Stage-A
ledger remains mandatory; Stage B stays prohibited.

## 2026-07-19 correlation-form 0--1 Stage-A calibration null

Applied Research Rules 1, 2, 5, 6, and 7 with a separately frozen ledger at
clean active-repository commit `76d5deb`. Sixteen fixed frequencies, maximum
lag 100, threshold 0.5, fresh Mackey--Glass tau=17/tau=2, and all eight
coordinates of fresh Lorenz--96 F=8/F=1 were fixed before measurement. The
strict gate failed with false negatives on both positives and no false
positives. No tuning; Stage B remains closed. Hyperseed reading: the tested
finite-sample observable/frequency relation did not calibrate as a dynamical
classifier and does not identify the flow law. Provenance:
`experiments/20260720T031500Z-zero-one-calibration-v1/RUN.md`.

## 2026-07-19 median 0--1 statistic unit gate

Implemented the frozen correlation-form 0--1 contract at clean active-repo
commit `2d72a488126a43e87537c0f68c0a493de24492d6`. The dependency-free seam
preserves externally supplied frequency order, uses one-based translation
variables, applies the oscillatory correction, returns per-frequency Pearson
correlations plus their median, and fails closed on invalid or degenerate
inputs. Focused 6 tests / 18 subtests, full pytest 263 tests / 67 subtests,
stdlib discovery 185 tests, `compileall`, and `git diff --check` passed.
Spec/code/test SHA-256 values are `3537597a14af1c94cce6e0c33799629c3962ae4548856e2a106d8902f5e49e6b`,
`7b2e4749458d66e284aca820c58ace1b9ff2546c72b6b555ac24fdf18b1ca13d`,
and `777b36e92c947467726061e877a2eb9db78f91eba31a7b0350be6932ce6c63d9`.
No scientific fixture was scored and no threshold was selected. Mackey--Glass
and full-state Lorenz--96 require a separately frozen untouched-data Stage-A
ledger; Stage B remains prohibited.

## 2026-07-19 median 0--1 statistic specification gate

After accepting the paired-divergence null without tuning, selected the
established correlation form of the Gottwald--Melbourne 0--1 test as a new
outcome-independent Stage-A candidate. Clean active-repository commit
`9ca744e72bf6d1d600bc2e0d508411eedba56f30` freezes the plain-language contract
before implementation: externally supplied distinct frequencies and maximum
lag, one-based translation variables, mean-square displacement, oscillatory
correction, per-frequency Pearson correlation, median aggregation, and strict
fail-closed validation. Spec SHA-256:
`3537597a14af1c94cce6e0c33799629c3962ae4548856e2a106d8902f5e49e6b`.

No Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
scored; no threshold was selected and no experiment ledger was required for
this specification-only gate. Full pytest passed 257 tests / 49 subtests in
61.99 seconds; stdlib discovery passed 179 tests in 47.999 seconds;
`compileall` and `git diff --check` passed. Stage B remains prohibited.

Hyperseed reading: the statistic measures an extensional diffusion relation
across a frozen family of rotational views; its robust median does not identify
the intensional flow law. Observable selection, statistic, calibration, and CLA
coding remain separate replaceable seams under Research Rules 1, 2, 5, 6, and
7.

## 2026-07-19 paired log-separation unit seam

At clean active-repository commit `2be5f1b`, added a replaceable paired-
trajectory statistic that performs ordinary least squares on log Euclidean
separation versus sample index. The spec deliberately leaves generator,
perturbation, transient, sampling interval, fit window, saturation handling,
threshold, and decision rule to a separately frozen ledger. Hand-constructed
growth/contraction and scalar/vector invariants passed; malformed, mismatched,
zero-separation, and non-finite inputs fail closed. Focused 12 tests / 16
subtests, full pytest 256 tests / 49 subtests, stdlib discovery 178 tests,
`py_compile`, and `git diff --check` passed. No Mackey--Glass, Lorenz--96, or
other scientific fixture was scored.

Hyperseed reading: unlike recurrence determinism's extensional one-orbit
geometry, paired separation tests a local intensional relation between nearby
evolutions, but remains a finite-window observable rather than identification
of the flow law. It cannot by itself prove chaos or validate CLA grammar.

## 2026-07-19 Stage-A recurrence-determinism calibration null

Frozen ledger `experiments/20260719T171500Z-recurrence-determinism-calibration-v1/RUN.md`
passed integrity checks at clean commit `9aca50b` but failed: stable full-state
Lorenz--96 F=1 was a nondegenerate false positive at `DET=1.0`. Stage B is
prohibited and no inspected setting may be tuned. Post-run focused 9 and full
253 tests / 45 subtests, `py_compile`, and `git diff --check` passed.

## 2026-07-03

Received and ingested Ben's `chaos_language_algorithm_ascii.pdf`. Core implementation risk is semantic conflation: chunks are sequential nonterminals; meta-symbols are context-substitution categories whose parse occurrences must retain chosen members for exact reconstruction.


## 2026-07-03 - CLA new project lane

Ben declared CLA a new project lane and paused OmegaSim until CLA is robust enough to detect grammatical strange-attractor structure in simulated OmegaHive traces. He supplied a second architecture document specifying a Hyperon-ready but pure-Python-first `chaoslang` library design.

## 2026-07-03 - GitHub repo created and first slice pushed

Ben confirmed CLA should be its own GitHub repo with the usual credentials. Local repo exists at `projects/chaos-language-algorithm/repos/chaoslang` with Git identity `Benjamin Goertzel <ben@singularitynet.io>`. Created GitHub remote `https://github.com/bgoertzel-sing/chaos-language-algorithm` and pushed the tested sprint-1 implementation to `main` at commit `4a7399c`.

Spawned subagent `cla_chaoslang_impl` to implement the first tested pure-Python symbolic-string MVP locally; the sprint completed with 19 passing tests.

## 2026-07-03 - Hyperseed / pattern calculus subthread

Ben suggested keeping a persistent subthread on CLA from a Hyperseed perspective. Core questions: what kind of language is induced from chaotic trajectories; how emergent pattern becomes grammar rather than merely compression; whether CLA edits/categories can be interpreted using McBride derivatives and pattern calculus; and how such an analysis can inform OmegaSim detector design. Ben pointed to Google Drive source `Weakness-Theory-10.pdf` (`https://drive.google.com/file/d/1PNg6ywTWPtSixm1yQ10z0TQXR8_bpgEh/view?usp=drive_link`), especially sections on emergent pattern and pattern calculus. Initial web fetch saw the Drive title but did not retrieve PDF contents.

## 2026-07-03 - chaoslang sprint 1 local implementation

Implemented and committed the first local `chaoslang` prototype at `projects/chaos-language-algorithm/repos/chaoslang`, commit `4a7399c`. Scope: pure-Python package with immutable-ish core dataclasses (`Token`, `Production`, `Category`, `Corpus`, `Grammar`, `Score`, `GrammarState`, `Edit`, `Proposal`), symbolic-string `CLA.simple().fit_symbols(...)`, n-gram chunk mining with non-overlap selection, exact chunk/category expansion, rule use counts and dead-rule pruning, a deterministic hard context category proposal seam, simple MDL-like greedy acceptance, `Fact`/`FactStore`/`MemoryFactStore` projection round-trip, and a logistic-map/equal-width symbolization smoke scaffold. Verification from repo root: `python3 -m unittest discover -s tests -v` passed 19 tests; `git diff --check` passed. Next: add fixed-partition trajectory symbolization and recorded attractor benchmark experiments before resuming OmegaSim detector calibration.

## 2026-07-04 - M1 controls slice

Implemented the next local `chaoslang` slice under `repos/chaoslang`: dependency-light deterministic Lorenz-63 and Rössler trajectory generators using fixed-step RK4; scalar/vector M1 fixed rectangular partition symbolization; a small JSON benchmark command (`python3 -m chaoslang.benchmarks.m1_controls`); and a Jensen-Shannon divergence clustering seam for future context/category clustering. Also fixed an n-gram chunk naming collision discovered by the Rössler M1 test: tie-breaking could accept `N2` before `N1`, then later reuse `N2` and overwrite the old rule, breaking exact reconstruction. Verification from repo root on 2026-07-04: `python3 -m unittest discover -s tests -v` passed 26 tests; `python3 -m chaoslang.benchmarks.m1_controls --system lorenz63 --steps 24 --discard 4 --bins 3 --iterations 3` emitted JSON with `exact_reconstruction: true`; `git diff --check` passed. Remaining next step: integrate JS-divergence context clustering into category proposal generation and record real attractor/control benchmark runs before attempting OmegaSim-level dimensionality.

## 2026-07-09 - suffix trie miner branch

Implemented a bounded suffix-trie chunk miner on branch `agent/suffix-trie-miner` in `projects/chaos-language-algorithm/repos/chaoslang`. The new `chaoslang.trie_miner.SuffixTrieMiner` builds suffix-prefix trie nodes keyed with `entry_key()` for `Token` and `CategoryOccurrence`, returns `ChunkProposal`s compatible with the existing n-gram miner, and can be selected via `CLA.simple(..., miner="suffix_trie")`. Added pytest coverage for smoke cases, equivalence with `NGramPatternMiner`, bounded O(N * max_ngram) node count, non-overlap behavior, and API switching. Verification: `PYTHONPATH=src python3 -m py_compile src/chaoslang/trie_miner.py`; `PYTHONPATH=src python3 -m pytest tests/ -v` passed 69 tests; `git diff --check` passed.

## 2026-07-09 - Suffix-trie n-gram miner for compound-symbol scaling

Ben approved replacing the brute-force `NGramPatternMiner` after OOM risk in high-cardinality compound-symbol CLA streams (e.g. 1024 steps × ~20D). Implemented a depth-bounded suffix-trie-backed miner in `repos/chaoslang/src/chaoslang/mining/ngram.py` on branch `agent/suffix-trie-miner`, preserving deterministic proposals and exact reconstruction. Added regression tests comparing trie output to a brute-force oracle for compound symbols and checking a high-cardinality repeated motif. Also added `docs/cla_expert_review_prompt.md` asking GPT-5.5-Pro/expert reviewers to explicitly audit algorithm/data-structure inefficiencies such as n-gram brute force, context histogram duplication, compound-symbol storage/copying, and repeated MDL re-encoding. Verification: focused chunk tests and full unittest suite passed; a 1024-step × 20D synthetic smoke completed locally with 1,710 proposals.

## 2026-07-16 - Interim progress worker

Ben requested a dedicated cron lane until ThreadKeeper persistent agents are ready. Created enabled isolated job `dce83d32-440a-4a6a-9305-04175f5ca50d` on a staggered two-hour cadence. Its contract preserves the frozen held-out predictive/MDL protocol, prioritizes Mackey-Glass and Lorenz-96 calibration, requires experiment-ledger provenance, and forbids outcome-sensitive held-out tuning.

## 2026-07-16 - Frozen held-out calibration null

Corrected the Mackey--Glass generator so conventional `tau=17` denotes 17
physical time units (170 steps at `dt=0.1`), not 17 integration steps. Added a
prefix-only Mackey--Glass/Lorenz--96 x0 frozen benchmark and integrity gates at
local commit `c8e9e91`. Before scoring, froze both trajectory/symbol hashes,
prefix bounds, 70/30 split, seed/config/baselines, exact command, and code hashes
in `experiments/20260716T172310Z-frozen-heldout-calibration-v1/RUN.md`.

Both trajectories passed deterministic state/fact/replay/refit and exact
reconstruction gates. CLA failed the aggregate code gate: 65,976.621 total bits
versus 6,588.443 for the strongest baseline (unigram). Canonical CLA model
transmission dominated at about 32.5 kbits per fixture; Lorenz--96 x0 also lost
on suffix data bits. This is a coding/calibration null, not chaos or semantic
grammar evidence. Do not tune on these suffixes; next preregister the protocol's
minimal joint chunk/category diagnostic.

## 2026-07-16 - Frozen joint chunk/category diagnostic

Preregistered and executed a separate 19-frame synthetic diagnostic without
using the failed Mackey--Glass/Lorenz--96 suffixes. Against clean local
chaoslang commit `6279604`, greedy CLA stayed at 76 proxy bits with zero edits,
while the frozen abstract joint category plus `N -> a M b` move scored 75 bits.
The exact-context inducer did not propose the 19 singleton middle members, and
the chunk miner still keyed `CategoryOccurrence`s by chosen member after manual
category application, so it exposed no member-agnostic generalized chunk.
Classification: `greedy_or_representation_blindness`. Exact reconstruction and
deterministic repeat passed; all 145 tests passed in bounded shards. This is a
local representation/proposal limitation, not predictive, chaos, attractor, or
semantic-grammar evidence. Provenance:
`experiments/20260716T191500Z-joint-chunk-category-diagnostic-v1/RUN.md`.

## 2026-07-16 - Generalized category-slot domain seam

Specified the member-agnostic matching/member-specific decoding split in
`docs/generalized-category-slot-spec-v1.md`, applying Research Rules 1, 2, 5,
6, and 7. Implemented the additive unit seam in the documented clean worktree
at local commit `46322123ec5a420a76680125e61b9e572982fde6`:
`CategorySlot` represents category identity in a production, while
`GeneralizedChunkOccurrence` retains ordered members for exact decoding. A
bounded generalized miner found `a M b` at all 19 starts in the frozen fixture;
application retained `m00` through `m18` and expanded exactly to all 76 source
tokens. Malformed/overlapping/category-mismatched proposals fail closed.
Focused tests passed 27/27, the full suite passed 150/150 in 45.11 seconds, and
`git diff --check` passed. This was unit validation, not a measured benchmark,
so no new outcome ledger or attractor claim was created. Persistence/facts,
joint greedy integration, and fair decodable transmission accounting remain
explicit blockers to another attractor run.

## 2026-07-16 - Generalized category-slot persistence and facts

Extended the additive generalized-slot seam through canonical persistence,
strict edit-log replay, and backend-neutral fact projection at clean local
chaoslang commit `bd7595c`. JSON now distinguishes category slots from ordinary
category occurrences and stores each generalized chunk occurrence's ordered
member side table. Replay reconstructs the slot pattern from the categorized
state, verifies the recorded pattern and occurrence invariants, then requires
the generated edit segment to match exactly. Fact projection uses explicit
generalized-chunk, member, and production-slot predicates and round-trips exact
expansion on the frozen 19-frame/76-token fixture.

Verification: focused persistence/core/category-slot tests passed 43/43; the
full suite passed 151/151 in bounded per-file shards; `py_compile` and
`git diff --check` passed. No measured benchmark or held-out suffix was run or
inspected. Joint greedy search and fair decodable model/member transmission
remain prerequisites to any new attractor benchmark.

## 2026-07-16 - Canonical generalized-state transmission code

Added the next Rule 1/2/5/6/7 unit subgate at clean local chaoslang commit
`fe32c4a737db775f937adecc7ef13cb2488ea19b`. The new
`chaoslang.scoring.state_code` emits distinct versioned canonical UTF-8 JSON
documents for the grammar/model and top-level parse/data and charges exactly
eight bits per byte. Categories, category slots, generalized chunk identities,
and each ordered occurrence-member side table are explicit. The decoder has no
stored corpus, history, edit log, or score input: it reconstructs the corpus by
exact expansion, rejects malformed/noncanonical documents, and re-encodes
byte-for-byte.

The frozen 19-frame/76-token synthetic fixture passed this complete model/member
code round trip. Focused state-code/category/persistence/frozen-suffix coverage
passed 43/43; all 157 collected tests passed in bounded per-file shards;
`py_compile` and `git diff --check` passed. This was implementation/unit
validation, not an outcome comparison or attractor benchmark; the failed
Mackey--Glass/Lorenz--96 suffixes were not inspected. Joint proposal/search
integration and a separately frozen measured synthetic decision gate remain
before any renewed attractor calibration.

## 2026-07-16 - Joint generalized proposal reachability seam

Extended `docs/generalized-category-slot-spec-v1.md` before coding with the
joint proposal invariants and the explicit boundary that the sprint-1 proxy is
not a fair generalized-member code. At clean local chaoslang commit
`871a0c66566a5b538a5ed58eae49cf037f543341`, the additive
`JointCategorySlotMiner` uses the existing exact-context inducer with a
joint-only per-member occurrence threshold of one, applies each category to a
temporary immutable state, and composes its generalized slot proposals. The
typed joint applier records the ordinary category and generalized-chunk edits
in order, so existing strict replay remains applicable.

On the frozen 19-frame fixture the miner deterministically reached the intended
`M={m00,...,m18}` plus `N -> a M b` move without mutating the input and exact
expansion recovered all 76 tokens. Focused category-slot tests passed 7/7; all
158 tests passed in bounded per-file shards; `py_compile` and
`git diff --check` passed. No measured benchmark ran, no held-out suffix was
inspected, and the joint seam is not enabled in `CLA.fit_symbols`. The next gate
is a preregistered synthetic accept/reject comparison using the complete
decodable state code; its result must not revise the Mackey--Glass/Lorenz--96
null or be promoted as chaos/semantic-grammar evidence.

## 2026-07-16 - Generalized complete-code decision null

Preregistered and executed the smallest complete-code decision gate on the
frozen 19-frame fixture. Attempt 1 failed before scoring because a harness
integrity assertion compared token objects to strings; the empty result and
stderr hash were preserved. After the one-line correction and refreeze at
clean local commit `8ffa31c`, the exact command passed every integrity gate.
The intended joint state cost 34,416 bits versus 34,352 initially (+64): data
fell by 6,232 bits while model transmission rose by 6,296. Classification was
`complete_code_rejects_joint`; the joint miner remains disabled. All 158 tests
passed in bounded per-file processes, with `py_compile` and `git diff --check`
clean. No attractor suffix was inspected or tuned. Provenance:
`experiments/20260717T051500Z-generalized-complete-code-gate-v1/RUN.md`.

## 2026-07-17 - Indexed generalized-state code unit subgate

Specified the outcome-independent accounting refinement before implementation
in `docs/indexed-state-code-spec-v1.md`. At clean local chaoslang commit
`8a46900fddbafa54e2d99fe429fc599ae4f2f869`, the additive indexed codec emits
separate canonical model/data JSON documents, transmits every `(kind, value)`
token once in a sorted shared table, and uses integer references uniformly for
literal parse tokens, productions, category members/slots/occurrences, and
ordered generalized-member side tables. The decoder has no corpus, history,
edit log, score, or external dictionary; exact expansion derives the corpus and
canonical re-encoding must match byte-for-byte. Invalid indices, tags,
duplicates, and unsorted tables fail closed.

Focused indexed/current-code/category-slot tests passed 20/20; all 165 tests
passed in bounded per-file processes; `py_compile` and `git diff --check`
passed. No 19-frame candidate codelength comparison ran, and no Mackey--Glass
or Lorenz--96 suffix was inspected. The joint miner remains disabled. The next
measured step requires a new preregistered ledger freezing the commit, fixture,
candidate states, exact command, acceptance rule, canonical-v1 control, indexed
literal control, and artifact hashes.

## 2026-07-17 - Frozen indexed complete-code gate

Preregistered the indexed comparison before outcome inspection, including the
clean implementation commit `29a52fd`, fixture/candidate, strict acceptance
rule, exact command, hashes, canonical-v1 continuity totals, and symmetric
indexed literal control. The exact local command passed every integrity gate.
The indexed joint state cost 9,760 bits versus 10,616 initially (-856): data
fell by 1,672 bits and model transmission rose by 816. The canonical-v1 control
exactly reproduced the prior rejection, 34,416 versus 34,352 (+64).

All 165 tests passed in bounded per-file processes; `py_compile` and
`git diff --check` passed; result/stderr hashes are recorded in
`experiments/20260717T091500Z-indexed-complete-code-gate-v1/RUN.md`. This is a
synthetic coding result only. It neither revises the Mackey--Glass/Lorenz--96
held-out null nor supports chaos/semantic-grammar claims or an attractor rerun.
The joint miner remains disabled pending a specified and unit-tested indexed
complete-code search scorer with positive and negative synthetic controls.

## 2026-07-17 - Indexed joint-search scorer unit gate

Specified the interface and invariants before implementation in
`scratch/chaoslang-strict-replay/docs/indexed-joint-search-scoring-spec-v1.md`.
At clean local chaoslang commit
`a5a0772e8ec89bf6a25c430f4b0fa51881484b13`, the additive
`IndexedJointSearchScorer` evaluates both the input and applied candidate with
the same complete indexed codec, fails closed unless both reconstruct the
unchanged corpus, accepts only a strictly negative delta, and resolves exact
ties independently of proposal iteration order. Proposal discovery remains a
separate abstraction seam.

Unit controls reproduce the already established 19-frame positive values
(10,616 to 9,760 bits, delta -856) and a two-frame negative control (1,944 to
2,200 bits, delta +256). The positive candidate also passes corpus-free decode,
strict edit replay, and exact expansion. Focused joint/indexed/category tests
passed 17/17; the full suite passed 168/168 in bounded per-file processes;
`py_compile` and `git diff --check` passed. This was unit validation, not a new
measured benchmark: no Mackey--Glass or Lorenz--96 suffix was inspected. The
scorer and joint miner are still not wired into `CLA.fit_symbols`; learner
integration requires a separate plain-language spec and unit gate before any
new frozen attractor calibration.

## 2026-07-17 - Indexed complete-code learner integration unit gate

Specified learner iteration, proposal competition, score-state semantics,
stopping, and fail-closed configuration before implementation in
`scratch/chaoslang-strict-replay/docs/indexed-learner-integration-spec-v1.md`.
At clean local chaoslang commit
`24d9771a006dc394a9d794f28511298e2a22d168`, `CLA.fit_symbols` now has an
explicit opt-in indexed objective. All enabled ordinary chunk, ordinary
category, and joint category/generalized-chunk proposals compete under the same
complete indexed state code; joint search under the sprint-1 proxy raises
before fitting. Accepted states store the independently re-encoded complete
score and retain exact source reconstruction.

The unchanged 19-frame synthetic positive control converged to the already
frozen 9,760-bit joint state, while the two-frame negative control accepted no
edit and remained the 1,944-bit literal state. Focused integration/scorer/
indexed/category checks passed 20/20; default learner regressions passed 38/38;
the final focused gate passed 11/11. The full suite passed 171/171 in bounded
per-file/class shards; `py_compile` and `git diff --check` passed. The initial
full-suite loops reached the execution-cell time boundary during the known
long parameter sweep, so its logistic, Lorenz--96, and high-dimensional classes
were rerun separately (7/7, 4/4, 3/3) and all remaining files were completed.

This was a synthetic unit gate, not a measured attractor benchmark. No
Mackey--Glass or Lorenz--96 suffix was inspected, no proxy result was promoted,
and the v1 held-out coding null remains binding. Any renewed calibration needs
a separately frozen v2 experiment ledger and untouched generated trajectories.

## 2026-07-17 - Frozen indexed held-out calibration v2 null

At clean local commit `580f9170ff00876eba6aea0722770606804551cf`, added a
decodable shared-token-table frozen CLA model code, generalized slot-member
suffix coding, and an additive v2 harness. Before outcome inspection, froze the
protocol, pass rule, controls, seed 1701, exact command, and hashes for new
Mackey--Glass initial 0.7 and Lorenz--96 x3 trajectories in
`experiments/20260717T151800Z-frozen-heldout-calibration-v2/`.

The exact local run completed exit 0 in 3.76 s. Every deterministic, canonical-
decode, replay, and exact-reconstruction gate passed. Indexed CLA nevertheless
failed aggregate coding at 21,989.324 bits versus 6,739.904 for unigram. The
canonical-v1 CLA control used 61,934.221 bits. No joint proposal was accepted,
so indexed joint/no-joint controls were identical. Focused 21 and full 176 tests,
`py_compile`, and `git diff --check` passed. This is a coding null and does not
validate chaos, attractor grammar, or semantics; no suffix tuning is allowed.

## 2026-07-17 - Synthetic detector calibration positive-condition null

Applied Research Rules 1, 2, 5, 6, and 7 by freezing a necessary detector
validation before another attractor run: one repeated binary order-5 de
Bruijn grammar-positive stream and a seed-1701 exact-marginal shuffled null,
with complete indexed CLA coding against literal/unigram/Markov controls.
Protocol, implementation, fixture hashes, seed, split, command, and decision
rule were frozen at clean local chaoslang commit `64b3b33` before scoring.

The exact local run exited 0 and every deterministic, replay, canonical-decode,
and reconstruction gate passed. The shuffled null was correctly not promoted.
The positive condition nevertheless failed: indexed CLA encoded its untouched
suffix in 0.700 bits but required a 4,600-bit model, totaling 4,600.700 versus
2,608.721 for unigram. Pre-outcome focused 19/19, declaration 2/2, full 178/178,
`py_compile`, and `git diff --check` passed. Evidence and artifact hashes:
`experiments/20260717T171800Z-synthetic-detector-calibration-v1/RUN.md`.

This finite-sample synthetic coding null is not chaos or semantic evidence and
does not revise the two attractor nulls. From a Hyperseed/pattern perspective,
the learned repeated pattern is extensionally predictive but fails the current
finite two-part-code weakness threshold: pattern existence and economical
transmission remain distinct claims. Do not tune fixture length or code against
this suffix; require a new hypothesis and frozen synthetic gate.

## 2026-07-17 - Frozen Zimin sample-complexity competence gate

Applied Research Rules 1, 2, 5, 6, and 7 with a new outcome-independent
hypothesis: the unchanged indexed model may cross its complete two-part-code
weakness threshold when one-time grammar transmission is amortized over a new
hierarchical source. Froze repeated Zimin-5 and seed-260717 exact-marginal
shuffled fixtures, 64-repeat training prefix, cumulative suffix checkpoints
{32,64,128,256}, learner config, controls, hashes, and exact command at clean
local commit `b3709d8` before scoring.

The exact local run exited 0 and all integrity gates passed. The positive lost
at 32 repeats, first won at 64, and at the decisive 256-repeat horizon used
4,717.151 bits versus 8,515.866 for Markov-2. The shuffled null never won and
ended at 23,030.353 versus 16,040.265 for unigram. Focused 7/7, full 180/180,
`py_compile`, and `git diff --check` passed. Provenance:
`experiments/20260717T191500Z-synthetic-sample-complexity-v1/RUN.md`.

This is bounded one-family synthetic finite-sample competence, not chaos,
semantic grammar, or a revision of either attractor null. Hyperseed reading:
repeated application can eventually make a captured pattern's description
economical, but intensional meaning and cross-family generality remain
unshown. Next require a frozen non-Zimin source-family generalization gate.

## 2026-07-17: Non-Zimin morphic-family gate failed on Fibonacci word

Froze Thue--Morse and Fibonacci-word generators, 2,048/8,192 prefix/suffix
splits, exact-marginal shuffled nulls, learner config, seeds, controls, hashes,
and exact command at clean commit `e6e3ed2` before scoring. The exact local run
exited 0 and all integrity gates passed. CLA beat Markov-2 on Thue--Morse
(7,195.523 versus 8,700.081 bits) and rejected both nulls, but lost the
Fibonacci positive (6,131.278 versus 5,843.219). Full discovery passed 135
tests; `py_compile` and `git diff --check` passed. Provenance:
`experiments/20260717T211500Z-synthetic-family-generalization-v1/RUN.md`.

The Fibonacci suffix itself was compact under CLA, but complete model
transmission reversed the result. That decomposition is diagnostic only and
does not authorize suffix, horizon, split, or codec tuning. Hyperseed reading:
extensional chunks amortized under one substitution algebra but did not clear
the weakness threshold uniformly across two algebras; recovery of intensional
morphism laws remains unshown.

## 2026-07-17: Constant-length substitution mechanism gate passed

Applied Research Rules 1, 2, 5, 6, and 7 to a narrower post-result hypothesis
without modifying the learner or rescoring the Fibonacci/attractor suffixes:
bounded n-gram chunks should align with constant-length substitution blocks.
Froze new period-doubling and binary-coded Rudin--Shapiro sources, 2,048/8,192
prefix/suffix splits, exact-marginal shuffled nulls, seeds, controls, hashes,
and the exact command at clean commit `d854bc7` before scoring.

The exact local run exited 0 and every integrity gate passed. Indexed CLA beat
the strongest complete code on period-doubling (5,452.003 versus Markov-1 at
7,872.544 bits) and Rudin--Shapiro (9,602.305 versus unigram at 9,773.770),
while rejecting both shuffled nulls. The Rudin--Shapiro margin was a narrow
171.466 bits and remains explicit. Focused 2/2 and full 137/137 tests,
`py_compile`, and `git diff --check` passed. Provenance:
`experiments/20260717T231900Z-synthetic-uniform-morphism-v1/RUN.md`.

This is bounded synthetic representation competence, not a general detector,
chaos, attractor, or semantic-grammar result. The Fibonacci and both
Mackey--Glass/Lorenz--96 nulls remain binding. Next add a separately specified,
decodable universal-sequence-code control and test it only on new frozen data.

## 2026-07-17: Canonical LZ78 universal-control unit gate

Applied Research Rules 1, 2, 5, 6, and 7 without inspecting any scientific
suffix. Wrote the plain-language wire and decoder spec first, then added an
additive `lz78-canonical-v1` scoring seam in the documented clean worktree.
The byte stream fully transmits `CLZ1` framing, a sorted length-delimited UTF-8
token table, original sequence length, and greedy LZ78 parent/symbol records,
including an explicit terminal-parent record when needed. Every byte costs
eight bits; there is no omitted model, alphabet, framing, or padding cost.

At clean local commit `9737c37db770a3f9abb005eed126d688f7cc333b`, focused
round-trip/accounting/Unicode/terminal/malformed-input checks passed 14/14;
the full pytest suite passed 198/198 in 45.90 seconds; `py_compile` and
`git diff --check` passed. The decoder fails closed on invalid magic,
truncated/non-minimal varints, invalid UTF-8, unsorted/duplicate token tables,
bad references, invalid terminal records, length mismatch, duplicate phrases,
trailing bytes, and non-canonical encodings.

This was a unit-validation gate, not a measured benchmark, so no experiment
outcome was produced. Hyperseed reading: LZ78 is an extensional reuse
comparator that weakens any claim that CLA's chunk reuse is distinctive;
neither code by itself identifies intensional morphism laws, chaos, attractor
structure, or semantics. Next freeze a new untouched synthetic comparison in
its own experiment ledger before scoring.

## 2026-07-17: Universal-control synthetic calibration null

The separately frozen new-data gate at clean commit
`49418908b73bbdd49691707f55e608bbd2526b2e` ran Cantor ternary substitution
and regular paperfolding coding with 1,024-symbol training prefixes, untouched
4,096-symbol suffixes, exact-marginal shuffled nulls, and complete literal,
unigram, Markov-1/2, and canonical LZ78 controls. Every deterministic,
persistence/replay, decoding, byte-stability, and reconstruction gate passed.

Indexed CLA nevertheless lost both required positives to unigram: 7,219.814
versus 2,447.226 bits on Cantor and 7,380.844 versus 5,669.774 on
paperfolding. It beat LZ78 on paperfolding (8,056 bits) but not the strongest
control; neither shuffled null was promoted. The frozen rule failed. The
complete-model cost remains decisive, so short suffix codes or proxy gains
cannot be promoted. Provenance:
`experiments/20260718T031500Z-synthetic-universal-control-v1/RUN.md`.

## 2026-07-17: Compact indexed frozen-model unit gate

Applied Research Rules 1, 2, 5, 6, and 7 to the open finite-model-cost lane
without scoring any scientific fixture. Wrote the wire/decoder/scoring spec
first, then added an additive `frozen-cla-compact-indexed-v1` codec in the
documented worktree. The stream fully charges `CIM1` framing plus a recursively
tagged value domain of non-negative integers, strict UTF-8 strings, and lists;
all lengths and integers use minimal unsigned varints. The semantic payload is
the unchanged indexed CLA model: shared token table, grammar, fitted entry
counts, and category-member counts. Frozen parsing, suffix probabilities, ESC
handling, literal fallback, and exact reconstruction remain unchanged, and
canonical JSON v1 remains a continuity control.

At clean local commit `2feb70d2e9bea06d8aca090f2e33cea2baaf691d`, focused
model/scorer/malformed-input checks passed 12/12; the full pytest suite passed
209/209 in 46.19 seconds; `py_compile` and `git diff --check` passed. The code
worktree was clean. Spec/code/test SHA-256 values were respectively
`6b8f43dff48908d413ba07a6497e357bd5be6b084bd2f18caf97dc84afdd3a20`,
`8c20842859def73c0e4333d4d61a2caec65675de0d54d2f7cf813fee916887d7`,
and `c9088278286572ee87745d6de6a4bf7e8564fbd2e6eaf4c6cffa0e85178a5d2e`.
No benchmark result was produced, so no experiment ledger outcome exists.

Hyperseed reading: this seam reduces extensional description overhead only;
it does not identify an intensional generator, chaos, attractor structure, or
semantic grammar. A measured decision requires a separately frozen ledger on
new untouched data with canonical JSON CLA, canonical LZ78, and simple
parametric controls. Both Mackey--Glass/Lorenz--96 nulls remain binding.

## 2026-07-18: Compact-model frozen comparison null

Applied Research Rules 1, 2, 5, 6, and 7 with a new ledger frozen before
scoring at clean commit `4174095c290c89fb46375189acc940015cf9aaf0`.
The run used two untouched constant-length substitution sources, 1,024-symbol
training prefixes, 4,096-symbol suffixes, exact-marginal shuffled nulls, and
complete literal, unigram, Markov-1/2, canonical LZ78, JSON CLA, and compact
CLA accounting. Exact configs, seeds, commands, and hashes are in
`experiments/20260718T071500Z-synthetic-compact-model-v1/RUN.md`.

All integrity gates passed. Compact CLA saved 464--648 transmitted bits versus
JSON CLA with identical suffix bits. It beat Markov-2 on the four-state
2-uniform positive (5,146.362 vs 5,496.923 bits), lost the complementary
3-uniform positive to unigram by 195.269 bits (5,865.104 vs 5,669.836), and
correctly rejected both shuffled nulls. The required all-positive rule failed.
Focused 25/25 and full 211/211 pytest checks, `py_compile`, and
`git diff --check` passed; the worktree remained clean.

Hyperseed reading: compact transmission removes extensional syntax overhead
but does not identify the source morphism or an intensional grammar law. The
single positive is bounded coding competence, not detector calibration, chaos,
attractor, or semantic evidence. No inspected suffix may be tuned or rescored.

## 2026-07-18: Frozen phase-robustness calibration null

Applied Research Rules 1, 2, 5, 6, and 7 with the phase-robustness protocol,
implementation, source, two observation offsets, fixture hashes, seeds,
controls, and pass rule frozen before outcome inspection at clean commit
`a0801998b2b429a979397f1e96abe5edac817e55`. The new three-state 2-uniform
source used 1,024-symbol prefixes, untouched 4,096-symbol suffixes, and
exact-marginal shuffled nulls at offsets zero and one. Complete literal,
unigram, Markov-1/2, canonical LZ78, JSON CLA, and compact CLA codes were
retained.

All integrity gates passed. Compact CLA lost both positives to LZ78: 4,257
versus 2,760 bits at phase zero and 4,131 versus 2,760 at phase one; neither
shuffled null was promoted. Focused 2/2 and full 213/213 pytest checks,
`py_compile`, and `git diff --check` passed; the worktree remained clean.
Exact provenance is in
`experiments/20260718T091500Z-synthetic-phase-robustness-v1/RUN.md`.

Hyperseed reading: changing the observation origin is an extensional symmetry
test, not identification of the substitution operator. Similar complete-code
losses at both offsets do not rescue the detector or isolate phase as the
cause. No phase/suffix tuning, attractor calibration, chaos claim, or semantic
grammar claim is licensed.

## 2026-07-18: Frozen fixed-model amortization positive

A new ledger was frozen before scoring at clean commit `d299b2f`. On a new
five-state 2-uniform source with a 1,024-symbol prefix, compact CLA lost at the
4,096-symbol suffix checkpoint, first crossed at 16,384, and won at 65,536
(28,828.051 versus Markov-2 at 60,768.987 bits). The exact-marginal shuffled
null never crossed. All integrity gates, focused 2/2 and full 215/215 tests,
`py_compile`, and `git diff --check` passed. Provenance:
`experiments/20260718T111500Z-synthetic-amortization-v1/RUN.md`.

Hyperseed reading: this is extensional description-length amortization, not
identification of the substitution operator or semantic/dynamical structure.
Both Mackey--Glass/Lorenz--96 nulls remain binding.

## 2026-07-18: Frozen long-horizon attractor bridge null

Applied Research Rules 1, 2, 5, 6, and 7 with a new ledger frozen before
scoring at clean commit `cbbebfd`. Fresh Mackey--Glass initial 0.9 and
Lorenz--96 x5 trajectories used prefix-only eight-bin M1, a 1,024-symbol
frozen model, 4,096/16,384/65,536 suffix checkpoints, matched shuffled nulls,
and complete literal/unigram/Markov-1/2/LZ78/JSON-CLA/compact-CLA accounting.

All integrity gates passed, but neither positive crossed. At 65,536 symbols
compact CLA lost to Markov-1 on Mackey--Glass (72,723.386 vs 25,006.425 bits)
and Lorenz--96 x5 (103,647.803 vs 43,859.342); both nulls were correctly not
promoted. Focused 2/2 and full 217/217 pytest checks, `py_compile`, and
`git diff --check` passed. Hyperseed reading: synthetic morphism amortization
does not transfer through this scalar partition into an economical intensional
dynamics description. This is a coding null, not chaos or semantic evidence.
Provenance: `experiments/20260718T131500Z-attractor-amortization-v1/RUN.md`.

## 2026-07-18: Causal ordinal-pattern representation unit seam

Applied Research Rules 1, 2, 5, 6, and 7 after the frozen long-horizon scalar
M1 null. Before implementation, wrote
`docs/ordinal-pattern-symbolization-spec-v1.md`: finite scalar trailing windows
are encoded by their deterministic rank permutation, ties sort by earlier
window position, and order/delay are explicit. The representation is causal,
fit-free, and invariant under strictly increasing amplitude transforms.

Implemented `ordinal_pattern_symbols` as an additive dependency-free function
in `chaoslang.symbolization`, exported it from the public package, and added
fail-closed unit coverage. Clean local commit
`a7a7e7e25579ba592a75b0c28bb3250822e2a242` on branch
`agent/ordinal-pattern-symbolization-v1` passed focused 8 tests / 10 subtests,
full 225 tests / 10 subtests, `py_compile`, `git diff --check`, and the scoped
secret-pattern diff scan. The worktree was clean after commit. No benchmark,
attractor, scientific fixture, or inspected suffix was scored, so no measured
experiment ledger outcome exists.

Hyperseed reading: ordinal patterns quotient observations by strictly
increasing maps, retaining a finite local order relation while discarding
metric amplitude. A later coding win would establish recurrence only in this
quotient representation, not identify the flow law, strange attractor, chaos,
or semantic grammar. Any measurement requires a separately frozen ledger on
new untouched trajectories with complete model accounting and external
controls; both Mackey--Glass/Lorenz--96 M1 nulls remain binding.
## 2026-07-18: Frozen ordinal-pattern attractor coding null

Applied Research Rules 1, 2, 5, 6, and 7 with a separate ledger frozen before
scoring at clean commit `17a0778`. Fresh Mackey--Glass initial 1.1 and
Lorenz--96 x6 trajectories used causal order-3/delay-1 ordinal patterns, a
1,024-symbol prefix, untouched 4,096-symbol suffix, matched shuffled nulls,
and complete literal/unigram/Markov/LZ78/JSON-CLA/compact-CLA accounting.

All integrity gates passed and neither null was promoted, but compact CLA lost
both positives to LZ78: 9,235.184 versus 2,872 bits and 10,224.372 versus
3,928 bits. Focused 10 tests / 10 subtests and full 227 tests / 10 subtests
passed with compilation and diff checks. The execution ledger records one
deterministic duplicate invocation caused by an orchestration return before
the first child process completed. Provenance:
`experiments/20260718T171500Z-ordinal-attractor-v1/RUN.md`.

Hyperseed reading: the monotone-map quotient exposes local order recurrence,
but the complete extensional grammar is not economical against a universal
dictionary code here and does not identify the intensional dynamics. No
chaos, attractor, source-law, or semantic claim follows, and no tuning is
authorized.

## 2026-07-18: Causal recurrence-lag representation unit seam

Applied Research Rules 1, 2, 5, 6, and 7 after accepting the ordinal coding
null. Wrote `docs/causal-recurrence-symbolization-spec-v1.md` before code and
implemented an additive scalar symbolizer that emits the bounded lag class of
the most recent causal return within an explicit fixed radius. It is
deterministic, translation invariant, fail-closed, emits one symbol per sample,
and fits no state. Clean local commit `de6f85fbb92075d2ff8ef9e89d6d52de281ee160`
passed focused 8 tests / 13 subtests, full 235 tests / 23 subtests,
`py_compile`, and `git diff --check`. No scientific fixture was scored.

Hyperseed reading: this projects the trajectory onto a finite recurrence-time
relation. A later coding win would establish economical regularity only in
that projected relation, not identify the flow law, prove chaos, or establish
semantic/intensional grammar. Any measurement requires a separately frozen
ledger with a prefix-only radius rule and untouched Mackey--Glass/Lorenz--96
data plus complete-code controls and matched nulls.

## 2026-07-18: Recurrence calibration protocol integrity correction

## 2026-07-18: Causal full-vector recurrence unit seam

Applied Research Rules 1, 2, 5, 6, and 7 after accepting the scalar recurrence
coding null. The plain-language spec at
`docs/causal-vector-recurrence-symbolization-spec-v1.md` preceded an additive
dependency-free symbolizer for fixed-radius Euclidean returns in constant-
dimension vector trajectories. It is causal, deterministic, fit-free, emits
one symbol per observation, and is invariant under common translation and
orthogonal rotation.

Clean local commit `7c507b8` passed focused 13 tests / 23 subtests, the full
242-test / 33-subtest suite, `py_compile`, and `git diff --check`; the worktree
was clean. No Mackey--Glass, Lorenz--96, scientific fixture, or held-out suffix
was scored. Hyperseed reading: the seam exposes a finite metric-neighborhood
relation in the full observation space, not the intensional flow law, chaos,
an attractor proof, or semantic grammar. Measurement remains blocked on a
separately frozen untouched-data experiment ledger.

Clean commit `3a6ef3f` added the separate recurrence-attractor protocol,
deterministic fresh-data declarations, complete controls, matched nulls, and
an all-positive rule. Before any coding score was run, a Rule-1 declaration
audit found the proposed 5%-of-prefix-range radius made both positive suffixes
entirely `rl0` with identical hashes. The degenerate detector input was
rejected rather than measured.

Corrective clean commit `9cd3cf0` uses the prefix-only nearest-rank 10th
percentile of adjacent increments. The two suffixes are now distinct and
multi-symbol. Focused 10 tests / 13 subtests, full 237 tests / 23 subtests,
compilation, and `git diff --check` passed. No coding outcome was produced or
inspected. Next: freeze the timestamped ledger, manifest, and command hashes at
`9cd3cf0`, then execute the single decisive local command.
## 2026-07-18 recurrence-lag attractor calibration

The separately frozen local benchmark at clean `9cd3cf0` completed with all
integrity gates passing. Compact CLA lost both fresh positives to complete
external controls: Mackey--Glass initial 1.3 used 9,954.129 bits versus LZ78
at 5,008, and Lorenz--96 x7 used 13,697.457 versus unigram at 7,814.621.
Neither matched shuffled null was promoted. This is a recurrence-projection
coding null; it does not assess chaos or semantic grammar and authorizes no
radius, lag, stream, suffix, learner, or codec tuning. Provenance:
`experiments/20260719T011500Z-recurrence-attractor-v1/RUN.md`.

## 2026-07-19 full-vector recurrence calibration

Applied Research Rules 1, 2, 5, 6, and 7 with a separate ledger frozen before
scoring at clean commit `c667c02`. Fresh full-state 8D Lorenz--96 and an
explicit fresh scalar Mackey--Glass control used prefix-only recurrence radii,
untouched suffixes, matched shuffled nulls, and complete CLA/LZ78/parametric
accounting. Every integrity gate passed, but compact CLA lost both positives to
LZ78: 5,522.398 versus 2,000 bits and 9,933.113 versus 5,304 bits. Neither null
was promoted. Hyperseed reading: full observation-space recurrence exposes a
finite metric-neighborhood relation, but its extensional grammar remains less
economical than the universal dictionary code here; it does not identify the
flow law, chaos, an attractor, or semantics. No tuning is authorized. Evidence:
`experiments/20260719T071500Z-vector-recurrence-attractor-v1/RUN.md`.

## 2026-07-19 detector-calibration README guardrail

Applied Research Rules 1, 2, 5, 6, and 7 without running another measured
gate. Active-repository commit `4973b7e0cc4de49abb0ca58107f042baec84cbc7`
documents the additive scalar/vector recurrence APIs and makes the calibration
boundary explicit: the API's `prefix` argument is a symbol namespace, while
the recurrence radius must be calibrated externally on prefix/training data
only. The README now records that scalar ordinal, scalar recurrence, and
full-vector recurrence all remain complete-code nulls on fresh Mackey--Glass
and Lorenz--96 fixtures, prohibits inspected-suffix tuning and proxy promotion,
and requires a separately frozen untouched-data ledger plus matched nulls and
complete controls for another measurement. Focused recurrence checks passed 13
tests / 23 subtests; the full suite passed 244 tests / 33 subtests;
`py_compile` and `git diff --check` passed. No scientific fixture was scored.
## 2026-07-19 staged detector-validation contract

Applied Research Rules 1, 2, 5, 6, and 7 without inspecting or scoring a new
fixture. Active-repository commit
`bc15f8f0603377fa467a49e4d9e26017f227f1ef` adds
`docs/detector-validation-ladder-spec-v1.md` (SHA-256
`a74d58d4aeb67ea1a5c15f8a215e09b823ec7be601fbafaff89d0269f636d4ed`).
It separates Stage A calibrated dynamical discrimination from Stage B CLA
complete-code comparison, requires explicit Mackey--Glass and full-state
Lorenz--96 positives plus matched non-chaotic/shuffled controls, and preserves
all inspected suffixes as closed.

Focused recurrence tests passed 13/13; stdlib discovery passed 166/166; full
pytest passed 244 tests / 33 subtests in 52.66 seconds; `py_compile` and
`git diff --check` passed. The first focused command used the nonexistent stale
selector `tests.test_symbolization` and failed at import before running tests;
it was corrected to `tests.test_recurrence_symbolization` and
`tests.test_vector_recurrence_symbolization`. No benchmark ledger was needed
because no measured scientific claim was produced.

Hyperseed reading: Stage A tests an extensional invariant of a representation;
Stage B tests whether CLA economically describes strings in that quotient.
Neither identifies the intensional flow law or licenses chaos, attractor, or
semantic-grammar claims.

## 2026-07-19 Stage-A recurrence-determinism unit seam

Applied Research Rules 1, 2, 5, 6, and 7 without running a measured detector
gate. The plain-language spec at
`docs/recurrence-determinism-statistic-spec-v1.md` preceded an additive,
dependency-free statistic in the active worktree. For an externally fixed
radius it counts eligible off-diagonal recurrence points and the points in
maximal diagonal runs, with an explicit Theiler exclusion, configurable
minimum run length, scalar/fixed-vector support, deterministic output, and
fail-closed finite/shape/configuration validation.

Clean local commit `30f86505f837a51c56aa7a40bd1bb90ff7971f97` passed
focused 7/7, full pytest 251 tests / 45 subtests, stdlib discovery 173/173,
`py_compile`, and `git diff --check`; the worktree was clean. Spec/code/test
SHA-256 values were respectively
`91ab286490b665ca0892bdd0424e7bc5c439f79ae14e9a4f15d0e33744b74dcd`,
`84559c01630167585daf8baed88d694dd6493ba8a0769c8dbfa4670f48e8791d`,
and `c6c5a5a37e46690ca5e48972221dc3522c0527c9dc607da780cc2e8885c5d732`.
No Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
scored and no threshold was selected.

Hyperseed reading: recurrence determinism is an extensional persistence
statistic on a radius-defined relation. Periodic dynamics can also score high,
so it cannot identify the intensional flow law or prove chaos. A later Stage-A
measurement remains blocked on a separately frozen untouched-data ledger with
explicit Mackey--Glass and full-state Lorenz--96 positives, matched non-chaotic
and shuffled controls, false-positive/false-negative reporting, and an all-
fixtures rule. Stage B CLA coding remains separate.
## 2026-07-19 paired-divergence Stage-A calibration null

Applied Research Rules 1, 2, 5, 6, and 7 with a ledger frozen before
measurement at clean active-worktree commit `4cc2441`. Fixed `1e-8` paired
perturbations, samples `[32:256]`, threshold `1e-4` per sample, fresh
Mackey--Glass initial 1.9, full-state Lorenz--96, and stable tau=2/F=1 controls
were recorded before the exact command. The strict gate failed: Mackey--Glass
tau=17 was a false negative (-0.0067585), while stable Lorenz--96 F=1 was a
false positive (+0.0106748). Focused 4 tests / 4 subtests, full pytest 257 tests
/ 49 subtests, stdlib 179 tests, compilation, and `git diff --check` passed.
Hyperseed reading: finite-window separation is closer to local intensional
evolution than recurrence geometry, but without validated state preparation
and linear-regime selection it does not identify the flow law or chaos. No
tuning; Stage B remains prohibited. Provenance:
`experiments/20260719T211500Z-paired-divergence-calibration-v1/RUN.md`.
# 2026-07-19 Stage-A null README guardrail

Applied Research Rules 1, 2, 5, 6, and 7 without running another measured
gate. The active-repository README now records that the separately frozen
recurrence-determinism, paired-divergence, and correlation-form 0--1 Stage-A
calibrations all failed their predeclared Mackey--Glass/full-state Lorenz--96
positive/stable gates. It prohibits tuning or rescoring those inspected
fixtures and keeps Stage B closed until a genuinely new outcome-independent
detector hypothesis passes a separately frozen untouched-data ledger.

The guardrail is clean active-repository commit
`e7171fea8096f1bd47740df0028363614c405bc5`; README SHA-256 is
`4c620dd865d611ebfb655655997c0d18ecc605a8f109bca775dee054f56ad005`.
Full pytest passed 264 tests / 67 subtests, stdlib discovery passed 186 tests,
and `compileall` plus `git diff --check` passed. The worktree was clean.

This is a documentation guardrail, not a detector result or a new hypothesis.
No scientific fixture or held-out suffix was scored. Hyperseed reading: the
three failures reject the frozen extensional statistics as calibrated
discriminators on their declared fixtures; they neither refute chaos nor
identify an intensional flow law, attractor, source law, or semantic grammar.
# 2026-07-20 repeated-renormalization calibration

The fresh, separately frozen Stage-A ledger at clean active-repository commit
`793f10c` completed with exit 0. Lorenz--96 F=8 scored `0.0219147658` and was
promoted; Lorenz--96 F=1 (`-0.0006357785`) and Mackey--Glass tau=2
(`-0.0293053833`) were rejected. Mackey--Glass tau=17 scored `-0.0009622967`
and was a false negative, so the gate failed. This is a finite-protocol
detector-calibration null, not chaos, attractor, CLA, compression, source-law,
or semantic-grammar evidence. Stage B remains prohibited and the fixture is
closed to tuning/rescoring.

## 2026-07-20 repeated-renormalization README guardrail

Applied Research Rules 1, 2, 5, 6, and 7 without a new measured benchmark.
The active-repository README now includes the frozen repeated-renormalization
null, its Mackey--Glass false negative, the prohibition on tuning/rescoring,
and the bounded non-claim. Clean commit `6737178`; README SHA-256
`420c6f42197e6448601a167c27781ccc019240c538df71cc0372313cb2a2e8f3`.
Full pytest passed 268 tests / 75 subtests, stdlib discovery passed 190 tests,
and `compileall` plus `git diff --check` passed. The worktree was clean. No
scientific fixture, held-out suffix, detector score, or proxy was produced.
## 2026-07-20 conditional transition-entropy unit seam

Applied Research Rules 1, 2, 5, 6, and 7 after preserving the frozen
repeated-renormalization null. The spec at
`docs/conditional-transition-entropy-statistic-spec-v1.md` preceded an
additive dependency-free statistic. Clean commit `da52b36` passed focused 4
tests / 5 subtests, full pytest 272 tests / 80 subtests, stdlib 194 tests,
`compileall`, and `git diff --check`. Spec/code/test SHA-256 values are
`cf30032c3d51001cf7b0e74245481ae01dfa70b366bd0e77f54d46a78bccabee`,
`7a313d60e802243dd0533d0a4fb2831eff766c5ecc7cc7be93a22b85f648bd61`,
and `72dfcbdb4c2f35ff87761855f9698e51cda6450a92f55aa37fbd7571e6aeec27`.
No scientific fixture was scored. Hyperseed reading: this is an extensional
one-step branching relation in a chosen quotient, not the intensional flow
law. Stage A requires a separate frozen untouched-data ledger; Stage B remains
prohibited.

## 2026-07-20 conditional transition-entropy calibration null

Applied Research Rules 1, 2, 5, 6, and 7. V1 failed before any score on an API
field typo; v2 at clean `ba510c3` preserved all scientific choices. Both
positives passed, but stable (`0.0250289065`) and shuffled (`0.5845559857`)
full-state Lorenz--96 were false positives. This rejects the frozen finite
direction quotient, not chaos or grammar evidence. No tuning; Stage B closed.
Provenance: `experiments/20260720T153000Z-conditional-entropy-calibration-v2/RUN.md`.

## 2026-07-20 conditional transition-entropy README guardrail

Applied Research Rules 1, 2, 5, 6, and 7 without another measured benchmark.
The active-repository README now records V1's pre-score runner failure, V2's
unchanged scientific choices, the stable and shuffled full-state Lorenz--96
false positives, the prohibition on tuning/rescoring, and the bounded
non-claim. Clean commit `f231844`; README SHA-256
`2e7db869b747699c5ff8a9f6bf0b53a9a50e5222407337a56619f70ba6aa9322`.
Full pytest, stdlib discovery, `compileall`, and `git diff --check` exited
successfully; the worktree was clean. No scientific fixture, held-out suffix,
detector score, or proxy was produced.
# 2026-07-22 measured stdout flush boundary

Applied Research Rules 1, 2, 5, 6, and 7 without running a measured scientific
gate. The spec-first command seam now flushes stdout after the complete verified
artifact-byte write and returns success only after the flush succeeds. A flush
failure preserves the already durable result artifact as authoritative, so it
does not license rerunning a closed benchmark. Clean active-repository spec/code
commits are `2bfdfc5` / `af0f3c0`; spec/code/test SHA-256 values are
`f730952020fb72e45ff3e67981fb5b2c8627c53a08af41499589a9d5bdc86dce`,
`d6e6786bac051df8266c2edc0d394b567e0a1211174692792dedd9606d39d21d`, and
`1984e3538c68dc3614684a60c2f823475901308265233d75cea7373d303452c7`.
Focused pytest passed 18 tests; full pytest passed 305 tests / 93 subtests;
stdlib discovery passed 209 tests; `compileall` and `git diff --check` passed.
The direct `python3 -m unittest tests.test_experiment_artifacts -v` selector ran
zero tests because the module uses pytest functions and is not evidence. No
Mackey--Glass, Lorenz--96, held-out suffix, or other scientific fixture was
generated, rerun, or scored. Hyperseed reading: this strengthens the provenance
boundary between a durable measured fact and its transport; it adds no detector,
coding, chaos, attractor/source-law, or semantic-grammar evidence.

## 2026-07-22 identity-safe failed-artifact cleanup

Applied Research Rules 1, 2, 5, 6, and 7 without opening a measured ledger.
The persistence seam now records the created file's device/inode identity and
unlinks on failure only if the target still has that identity. A constructed
write-failure regression replaces the open artifact and proves the foreign
replacement survives cleanup. Clean active-repository spec/code commits are
`66d1711` / `aa5ab90`; focused pytest passed 23, full pytest passed 310 tests /
93 subtests, stdlib discovery passed 209 tests, `compileall`, and `git diff
--check` passed. No Mackey--Glass, Lorenz--96, held-out suffix, detector score,
or compression proxy was generated or inspected. Conceptually, cleanup is now
conditioned on object identity rather than path coincidence; this strengthens
provenance plumbing but supplies no chaos, attractor/source-law, coding, or
semantic-grammar evidence.
# 2026-07-22 parent-bound artifact creation specification

Applied Research Rules 1, 2, 5, 6, and 7 without opening a measured ledger.
Audit found that pre-creation ancestry checks alone do not bind the later
lexical file open to the directory that was checked. Clean active-repository
commit `5c87cf5` now specifies that artifact creation and parent `fsync` use the
same opened parent-directory identity, target creation must not follow a
symlink, and success must reject a renamed/replaced lexical parent. Canonical
artifact and emission spec SHA-256 values are respectively
`58dddff39803dbda1b7ac7a6f1a3af4163fca46e1e37b8ad2464d172e1a9c437`
and `5a6854ccbb443de9a3a3677020c8cdc314aacb4f667bec86e73605ffddfb6268`.
Focused pytest passed 23, full pytest passed 310 tests / 93 subtests, stdlib
discovery passed 209 tests, and `compileall` plus `git diff --check` passed.
No Mackey--Glass, Lorenz--96, held-out suffix, detector score, or compression
proxy was generated or inspected. Hyperseed reading: the directory handle is
an intensional capability to one filesystem object, whereas a lexical path is
only a mutable extensional name; binding publication to object identity
strengthens provenance but provides no chaos, coding, attractor/source-law, or
semantic-grammar evidence.
# 2026-07-23 complete-code score decomposition subgate

Applied Research Rules 1, 2, 5, 6, and 7 to the diagnostic report's R0 repair
lane. The active repository first froze
`docs/score-decomposition-spec-v1.md` at `2ec949e`, then implemented the
replaceable `decompose_state_code_delta` seam at clean commit `bdbf0f6`.
The existing constructed 19-frame generalized category-slot fixture exactly
reproduced the canonical complete-code mechanism: data `-6,232` bits, model
`+6,296` bits, total `+64` bits, rejected with
`complete_code_does_not_improve`. Focused pytest passed 11; full pytest passed
322 tests / 93 subtests; stdlib discovery passed 209 tests; `compileall` and
`git diff --check` passed. Spec/source/joint-search/test SHA-256 values:
`cd6d8e086f74baa272f8c73ea637656ff0fc3aba69f397a4315838518a3b7911`,
`efa3a44b92892dd5e4434a124420428fd77d0ef0c18cd77ffbe6890b05f7a7cc`,
`8c4a15c37ba9d2c7618993d8411e090286e4f03b88e4949c6aa52257860ece3b`,
and `2527989d2bd8021eb4810411e4ac5e14ca8a150bc54a0aa4b1e8a84c16b3cfd9`.
No scientific fixture or suffix was generated or inspected.

Hyperseed reading: this is an additive evidence projection from a complete
code decision into model and data components. It can explain a rejection but
cannot replace the complete decision. The abstraction seam admits later
residual or probabilistic codes without coupling diagnostics to the current
miner. It is not detector, chaos, attractor/source-law, or semantic-grammar
evidence.
# 2026-07-23 M-A adaptive coding evidence

- Governing document hashes:
  `chaoslang_upgrade_spec.md` =
  `afd2b189d578a2122a4e4ddf060ff8cdfc28e57b3c311281053a88013bf4d4e8`;
  `chaoslang_eval_programme.md` =
  `fe052ea685da8a888ea1b5d6d2b81b88b07a1e1d202e3b2f1be1e04908ccd132`.
- Active implementation worktree:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`, clean commit
  `6145e1d` after commit.
- Focused command:
  `PYTHONPATH=src python3 -m unittest tests.test_coding_core tests.test_lz78_control -v`
  passed 14 tests. Full required discovery passed 216 tests in 51.793 seconds.
  `python3 -m compileall -q src tests` and `git diff --check` passed.
- The first focused run exposed one incorrect test expectation (expected
  3.415 bits instead of the direct KT value 4.0); implementation behavior was
  correct, the expectation was corrected, and all acceptance checks then
  passed.
- No benchmark or E0-E8 outcome was inspected. CTW is explicitly permitted to
  land in M-E, and GrammarStreamCoder/fairness belongs to M-C, so invariants 2
  and 6 were not falsely pulled into M-A.

# 2026-07-23 M-C adaptive two-part scoring evidence

- Spec: `scratch/chaoslang-strict-replay/docs/adaptive-two-part-scorer-spec-v1.md`.
- Clean active-worktree commit: `9684701`.
- `GrammarStreamCoder` freezes one callable factory, codes the rewritten atom
  stream under that factory, and uses empty per-category KT estimators for
  both direct category occurrences and generalized-production slot members.
- `AdaptiveTwoPartScorer` charges the existing compact indexed model bytes,
  exposes parse/member/zero-definition diagnostics, caches canonical state
  scores, and deliberately uses full apply-and-rescore deltas.
- Focused command covering M-A through M-C and the proposal ledger passed 12
  pytest checks. The required full command passed 216 stdlib tests in 48.663
  seconds. `compileall` and `git diff --check` passed.
- No E0-E8 measurement, scientific fixture, held-out suffix, or OmegaSim run
  was opened. The mathematical-foundations additions remain hypotheses
  pending an explicit reviewed amendment before M-D.
# 2026-07-23 mathematical-foundations source intake

Ben supplied the 11-page PDF *Mathematical Foundations for the Upgraded Chaos
Language Algorithm*. It is preserved at
`docs/cla_math_foundations_ascii_1.pdf` with extracted text beside it. PDF
SHA-256:
`6969a095f1139d52fb64afa564cca7acbe40f2f79bf0f89cb4d4769fa385ebcb`.
Pages 1, 6, and 11 were visually checked after full text extraction; the file
is readable, complete, and has no embedded JavaScript or encryption.

Observed proposal-level implications:

- interpret CLA as a hierarchical-generativity detector rather than a generic
  chaos detector;
- expect CSSR/causal-state coding to dominate chunk CLA on positive-entropy
  sofic dynamics;
- add an LZ77-to-balanced-SLP initializer beside Re-Pair in M-D;
- add fresh Feigenbaum/Sturmian E5b fixtures with length scaling;
- rank composite edits by an estimated mixed MDL second difference while
  retaining exact-score acceptance;
- use two-part versus inline-code slack as a consistency diagnostic.

These are hypotheses and proposed amendments, not measured results. Research
Rules 1, 2, 4, 5, 6, and 7 are most relevant: validate theorem assumptions and
detectors, amend the spec before coding, obtain strategic review, preserve
reproducibility, retain the Hyperseed/quantale interpretation, and keep the
coder/search interfaces modular.
# 2026-07-23 mathematical-foundations amendment evidence

- Governing documents were restored onto the accepted M-C worktree by
  preservation commit `6bf962b`; their hashes remain
  `afd2b189d578a2122a4e4ddf060ff8cdfc28e57b3c311281053a88013bf4d4e8`
  and `fe052ea685da8a888ea1b5d6d2b81b88b07a1e1d202e3b2f1be1e04908ccd132`.
- Reviewed amendment:
  `repos/chaoslang/docs/mathematical-foundations-amendment-v1.md`, SHA-256
  `bb69556d64e3d893ba05f52f915ee41abe994afbc565d96d1d1a3ca69249f65d`.
- The audit states the source-class, identifiability, finite-presentation, and
  exact-action assumptions behind the recurrence, substitution,
  epsilon-machine, category-congruence, and synergy claims. It rejects
  theorem-level extrapolation to finite continuous-system symbolizations.
- M-D is amended with deterministic non-self-referential LZ77 parsing,
  balanced SLP conversion, exact reconstruction/MDL pruning, and composite
  ledger residuals. Exact official scoring remains the sole acceptance
  authority.
- E5b is frozen as a proposal only. Fresh seeds, exact generators, hashes,
  commands, thresholds, and a run-specific ledger remain prerequisites; E3
  must authorize it, and no fixture was generated or scored.
- Validation: focused pytest 17 passed in 0.28 seconds; required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 216 tests
  in 91.483 seconds; `python3 -m compileall -q src tests` and
  `git diff --check` passed.

# 2026-07-23 M-D composite-accounting slice

- Added additive composite evidence fields to `ProposalRecord` without
  changing existing proposal records or learner selection.
- `CompositeScoreEvidence` computes the exact official four-score mixed
  difference and estimated-versus-realized residual; missing estimates remain
  JSON null. `rank_composites` orders by frozen estimate then stable proposal
  digest, with missing estimates last.
- Focused pytest passed 6 tests / 1 subtest; required stdlib discovery passed
  220 tests in 45.932 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No search path was enabled and no E0--E8 fixture, suffix, or score was
  generated. Next M-D slice is deterministic Re-Pair construction and
  exact-official-score pruning; LZ77-SLP follows under the reviewed amendment.

# 2026-07-23 M-D exact-score Re-Pair pruning and replay

- Clean active-worktree commit `4c5d466` adds an explicit immutable
  inline-and-remove transition and exact-score fixpoint pruning to
  `RePairInitializer`.
- Candidate rules are tried in stable token order. A rule is accepted only
  when the supplied official scorer's exact total is strictly lower; ties and
  non-improvements retain the rule. Reconstruction is asserted on every
  accepted transition.
- Persistence replay now reconstructs the deterministic
  `InitializeFromRePair` state and replays live as well as unused rule-removal
  edits one at a time, then optionally reproduces the derived score.
- Focused pytest passed 37 tests. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 220 tests in
  48.034 seconds. `python3 -m compileall -q src tests` and `git diff --check`
  passed.
- No scientific fixture, suffix, E0--E8 gate, or OmegaSim run was opened.
  Public initializer selection remains deferred until the fit path uses one
  frozen adaptive scorer/configuration throughout. Next implement the reviewed
  deterministic LZ77-to-balanced-SLP initializer.

## 2026-07-24 M-D atomic composite move evidence

- Active worktree:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`
- Commit: `3a1f2e8` (`Add atomic composite move replay`), clean after commit.
- Successful ordered sub-proposals collapse to one durable `Composite` edit;
  replay restores the same parse, grammar, and atomic edit boundary.
- A deliberately stale second generalized-chunk sub-edit raises without
  mutating the immutable input state or leaving grammar/edit-log traces.
- Evidence: 34 focused unittest tests passed; 14 focused pytest tests passed;
  required stdlib discovery passed 222 tests in 47.044 s; compileall and
  `git diff --check` passed.
- No E0--E8 fixture, suffix, detector, coder comparison, or scientific score
  was produced or inspected.

## 2026-07-24 M-D exact composite acceptance and residual wiring

- Clean active-worktree commit `2a064b1` adds an exact composite evaluation
  seam. Frozen estimates determine evaluation order only; the lowest exact
  improving official score wins, and exact reconstruction is checked before a
  candidate can be accepted.
- Every generated composite yields exactly one `ProposalRecord`, including
  component digests, estimator identity/configuration fields, exact
  model/data/total deltas, and an explicit acceptance or rejection reason.
- When both component edits apply independently, the record contains all four
  official totals, the realized mixed second difference, and the
  estimated-versus-realized residual. The category-then-generalized-chunk case
  is order-dependent, so its mixed fields are JSON null as required by the
  reviewed amendment; its exact atomic composite delta remains authoritative.
- Focused unittest passed 11. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 229 tests in
  46.068 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No scientific fixture, suffix, E0--E8 gate, detector comparison, or OmegaSim
  run was opened. The scientific framing remains a hypothesis: chunk CLA may
  detect hierarchical generativity and should likely lose to CSSR on
  positive-entropy sofic regimes.
# 2026-07-24 M-D proposal-budget accounting

- Clean active-worktree commit `73f56d6` makes the composite evaluation seam
  enforce the frozen default budget of 512
  proposals per step and rejects negative budgets.
- Frozen mixed-delta estimates and stable digests determine admission order
  only. Cut composites are neither applied nor officially scored and cannot
  be accepted.
- Every generated composite still yields exactly one accounting result and,
  when a ledger is supplied, exactly one record. Cut records carry
  `reason="budget_cut"`, component digests, estimator identity/version, and
  the nullable frozen estimate; uncomputed score deltas remain zero.
- Focused unittest passed 13. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 231 tests
  in 48.379 seconds. `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- No scientific fixture, suffix, E0--E8 gate, detector comparison, or
  OmegaSim run was opened. Exact official scoring remains the sole acceptance
  authority. The hierarchical-generativity/CSSR framing remains a hypothesis.

# 2026-07-25 M-D public beam deterministic replay

- Clean active-worktree commit `f948b70` adds the missing end-to-end fixed-seed
  replay regression for the opt-in public adaptive beam/composite path.
- Two independent ledger directories produce identical fitted
  `GrammarState`, exact expansion, `proposals.jsonl` bytes, and
  `final_breakdown.json` bytes.
- Focused `PYTHONPATH=src python3 -m unittest tests.test_beam_search -v`
  passed 12 tests. Required discovery passed 249 tests in 47.081 seconds.
  `python3 -m compileall -q src tests` and `git diff --check` passed.
- No experiment ledger was required because this was a deterministic unit
  regression, not a measurement. No E0--E8 fixture or scientific score was
  generated. E3 and the OmegaSim pause remain binding.
- Audit follow-up: governing §4.3 describes `max_proposals_per_step` without
  limiting it to composites, while the current public loops apply it to
  composite proposals only. Resolve and test a joint single/composite budget
  before declaring M-D complete or starting M-E.

## 2026-07-25 M-D joint proposal-budget closure

Clean active-worktree commit `db4273f` applies one proposal budget across
single and composite moves for each greedy step or beam parent. Admission is
ranked deterministically by support times structural length, then stable
digest. Cut candidates are not applied or officially scored and receive
exactly one `budget_cut` record. Exact official score and exact reconstruction
remain the sole acceptance requirements.

Focused unittest passed 23 tests. Required discovery passed 249 tests in
45.535 seconds; compileall and `git diff --check` passed. This was a unit-level
search/accounting invariant, so no experiment ledger, E0--E8 fixture, suffix,
or scientific score was opened. The hierarchical-generativity framing and
expected CSSR advantage on positive-entropy sofic regimes remain hypotheses.
# 2026-07-25 10:15 PDT — M-E leakage-free causal-state coder

- Active worktree:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Froze `docs/causal-state-coder-contract-v1.md` and implemented
  `automata.unifilar_coder.CausalStateCoder`.
- Every causal state receives a fresh empty KT table over the declared
  vocabulary. State synchronization uses the longest known held-out suffix
  until a frozen transition exists; missing transitions return to suffix
  synchronization. Reset and clone preserve deterministic replay.
- The compact v1 machine charge covers ordered state identifiers and canonical
  transition triples only. A regression replaces all diagnostic training
  emission counts with values scaled by 10,000 plus 7 and obtains exactly the
  same held-out code length and model charge, ruling out the specified leakage
  path.
- Focused unittest passed 6; required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 259 tests in
  46.362 seconds; `python3 -m compileall -q src tests` and
  `git diff --check` passed.
- Contract/source/test SHA-256:
  `5b05c0f9111d3701d2ccb725976a1a8668aa06d671108d79723192837031a6d9`,
  `95c171c0331d872fc2e3f0c2f9757dd831e0ad56104c928173855d9414905263`,
  `ac4f70173fd0e967bcd5dbe9e3a9c3cb2cc4c38c761b04e01b51972ab5986e14`.
- This was non-measuring: no registry exposure, E0--E8 fixture, held-out
  scientific score, remote compute, or OmegaSim work ran. Exact official
  scoring and the hierarchical-generativity/CSSR framing remain unchanged.
## 2026-07-26 00:15 PDT — M-F prequential scorer contract

The next bounded M-F slice was frozen at
`scratch/chaoslang-strict-replay/docs/prequential-scorer-contract-v1.md`
(SHA-256 `da823a203e1d13b75175b099b433ccd1e5d4d722df2c70550d135f1c0124d2d1`).
`PrequentialScorer` wraps the independently decodable inline coder without a
separate model charge, reports exact parse/member/definition components, caches
immutable scores by the complete-state digest, and defines delta only as full
immutable apply-and-rescore. The focused inline+scorer suite passed 9 tests;
`PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 276 in 48.219
seconds; compileall and `git diff --check` passed. This was non-measuring: no
registry/default exposure, E0--E8 fixture, held-out suffix, or OmegaSim run was
opened. The mathematical-foundations claims remain assumption/citation-audited
hypotheses and did not alter any frozen gate.
The coherent code slice was committed locally as `1f7e7b5`.
## 2026-07-26 10:15 PDT — E0 source and threshold design frozen

- Clean strict-replay commit `37d634e` adds
  `docs/e0-coder-calibration-preregistration-v1.md` (SHA-256
  `f9f4200b657844597c53a15cf1d9ca1320eda99c30697aa993ec1882bd399c1d`).
- It freezes five fresh seeds, three lengths, exact iid uniform/Zipf,
  Markov-1, Markov-3, and periodic laws, analytical entropy calculation, the
  periodic absolute tolerance, M2/CTW redundancy bands, and the four LZ78
  continuity values from historical manifest SHA-256
  `88b4a4ca0920fd8a1ad80f28efa3bb855148913caf8f7dd558021fed37abf9e3`
  and results SHA-256
  `f638887f0868490011332fb035bd7ee6856106cf7bfaddc641fe21e1614252e1`.
- Focused coding tests passed 12; full stdlib discovery passed 279 in 45.049
  seconds; compileall and `git diff --check` passed. This slice generated no
  fixture, suffix, score, or experiment outcome. E0 awaits a separately
  declaration-tested, hashed, cleanly committed runner before its sole
  execution. E3 remains binding and OmegaSim remains paused.
## 2026-07-26 12:15 PDT — E0 runner implemented without measurement

- Clean strict-replay commit `096cbb1` adds the E0 runner and declaration
  tests. Import/declaration is non-measuring; the tests use only seed `7`, not
  any frozen E0 seed.
- The runner records raw bits and bits/symbol for every frozen source/seed/
  length/coder cell, analytical entropy, stream hashes, every convergence/M2/
  CTW predicate, aggregate disposition, and historical LZ78 exact-decode,
  byte-stability, expected-bit, manifest-hash, results-hash, and regenerated
  declaration checks.
- Focused unittest passed 4. Required
  `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 283 in
  49.110 seconds. `compileall` and `git diff --check` passed.
- No frozen seed stream, fixture hash, coder score, suffix, or outcome was
  generated or inspected. Next is the separately declaration-tested ledger
  wrapper and hash freeze at the preregistered `20260726T171500Z` path.

## 2026-07-27 08:15 PDT — E0 v2 amendment proposed, not authorized

The completed E0 v1 result remains a binding aggregate failure. Its sole
failed family was iid-uniform-v16 under the order-2-versus-unigram redundancy
predicate. A review-only proposal at
`scratch/chaoslang-strict-replay/docs/e0-coder-calibration-amendment-proposal-v2.md`
records that the v1 allowance `2*K^2*log2(n)` counts order-2 contexts but
omits the `K-1` free parameters in each K-way KT multinomial. The proposal
does not select a replacement constant from the burned excess. It requires a
derived or cited per-context finite-sample KT-regret predicate, independent
non-measuring unit checks, five fresh seeds, a fresh ledger suffix, and
separate review before execution. No fixture, score, rerun, or E1 promotion
was opened. Ben's decision is required.

## 2026-07-27 18:15 PDT — gate audit: E1 remains closed

Rechecked the governing upgrade/evaluation specifications, the supplied
mathematical-foundations source (PDF SHA-256
`6969a095f1139d52fb64afa564cca7acbe40f2f79bf0f89cb4d4769fa385ebcb`),
the completed E0 v1 ledger, and the clean strict-replay worktree at
`f5a2b7b`. E0 v1 remains a binding aggregate failure, so E1 and all dependent
measurements remain unauthorized. The reviewed M-D amendment and separately
frozen, non-executable E5b proposal already satisfy the requested preparation
work. No fixture, score, test, source change, or experiment was opened.
Ben's explicit review of
`docs/e0-coder-calibration-amendment-proposal-v2.md` is still the next
critical-path decision.
