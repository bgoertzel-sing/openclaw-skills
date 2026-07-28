# chaoslang Upgrade Specification: Adaptive Coding, Instrumented Search, Re-Pair Initialization, and the Automata Track

**Status:** implementation spec for coding agents
**Target repo:** `bgoertzel-sing/chaos-language-algorithm` (package `chaoslang`)
**Prerequisite reading:** `A Hyperon-Ready Python Architecture for the CLA` (2026-07-03) and `CLA Experiments, Results, Failure Diagnosis, and Repair Programme` (2026-07-23)
**Companion document:** `chaoslang_eval_programme.md` (the experiment protocol; do not invent your own evaluation — the gates live there)

---

## 0. Rationale in one paragraph (read this before coding)

The July 2026 diagnostic shows that CLA's data code prices parse atoms with an essentially static token code while its controls (Markov-1, LZ78) are adaptive. On chaotic symbol streams — which have statistical, not verbatim, regularity — a deterministic chunk grammar with a static data code cannot beat an adaptive Markov coder even with model cost fully amortized (the 65,536-symbol failures). This upgrade therefore (A) replaces the data code with a **shared adaptive (prequential) coder** used identically in the baseline and grammar arms, so a grammar edit is credited only with its *incremental* saving over that coder; (B) adds full **per-proposal instrumentation** so coding failure, search failure, and model-cost failure are observationally separable; (C) adds **Re-Pair initialization** and **compound chunk+category moves** to fix greedy myopia; (D) adds an **ε-machine / CSSR automata track** as both a control coder and a category-proposal source, because the symbolic dynamics of an attractor is a sofic (regular) process, not a context-free one. Nothing in `chaoslang.core` changes semantically; everything below slots in behind the existing `Scorer`, `PatternMiner`, `CategoryInducer`, `GrammarSearcher`, and `AcceptancePolicy` protocols.

**Non-negotiable invariants carried over from the existing spec:** chunk/category type separation; exact reconstruction after every accepted edit; proposals-not-mutations; all state changes through `EditApplier` and the edit log; deterministic seeds; core imports no backends.

---

## 1. New package: `chaoslang/coding/`

All sequence coders live here. This package may import numpy but nothing from `chaoslang.hyperon`, sklearn, or scipy.

### 1.1 `coding/protocols.py`

```python
from typing import Protocol, Sequence
from chaoslang.core.ids import TokenId

class SequenceCoder(Protocol):
    """A prequential (predict-then-update) coder over token streams.

    Contract: push() returns the ideal code length -log2 p(symbol | all
    previously pushed symbols) under the coder's CURRENT state, and then
    updates the state with the symbol. Code lengths are exact ideal bits
    (floats); no actual bitstream is produced except by DecodableCoder
    subclasses used in round-trip tests.
    """
    def reset(self) -> None: ...
    def push(self, symbol: TokenId) -> float: ...
    def total_bits(self) -> float: ...
    def clone(self) -> "SequenceCoder":
        """Deep copy of adaptive state. Needed for lookahead scoring."""
    def code_stream(self, stream: Sequence[TokenId]) -> float:
        """reset(); sum(push(s) for s in stream). Provided as a mixin/helper."""

class VocabularyDeclaringCoder(SequenceCoder, Protocol):
    """A coder whose alphabet is declared up front (two-part regime)."""
    def declare_vocabulary(self, vocab: Sequence[TokenId]) -> None: ...

class OpenVocabularyCoder(SequenceCoder, Protocol):
    """A coder that handles first-seen symbols via an escape mechanism
    (one-part / inline regime). push() on an unseen symbol returns
    escape bits + identity bits."""
```

### 1.2 `coding/kt.py` — `KTEstimator`

Adaptive multinomial with Krichevsky–Trofimov smoothing.

```python
class KTEstimator:
    def __init__(self, vocab_size: int, alpha: float = 0.5): ...
    def bits(self, symbol_index: int) -> float:
        # -log2( (count[i] + alpha) / (total + alpha * vocab_size) )
    def update(self, symbol_index: int) -> None: ...
    def push(self, symbol_index: int) -> float:  # bits then update
```

Requirements:

* `alpha` configurable; default 0.5 (KT). `alpha=1.0` gives Laplace.
* Must support **growing vocabularies**: `grow(new_size)` extends the table with zero counts (needed when grammar edits add tokens mid-run in the one-part regime).
* Unit test: total prequential bits over a stream must equal `-log2` of the exact KT sequential probability, cross-checked against a direct product-of-probabilities computation on streams of length ≤ 20 over alphabets of size ≤ 4 (closed-form check).

### 1.3 `coding/markov.py` — `AdaptiveMarkovCoder`

```python
class AdaptiveMarkovCoder:
    """Order-k adaptive Markov coder: one KTEstimator per k-gram context.

    order=0 reproduces an adaptive unigram coder. Contexts are created
    lazily; the first symbol(s) of a stream are coded by lower-order
    fallback: context of length min(k, position).
    """
    def __init__(self, order: int, vocab: Sequence[TokenId], alpha: float = 0.5): ...
```

* Implements `VocabularyDeclaringCoder`.
* This replaces the *role* of the static unigram/Markov-1/Markov-2 controls in new experiments. **Do not delete the legacy static controls** — they remain for continuity comparisons and regression tests. Register both under distinct names: `static-unigram`, `adaptive-unigram` (= order 0), `adaptive-markov-1`, `adaptive-markov-2`.

### 1.4 `coding/ctw.py` — `ContextTreeWeightingCoder`

Standard binary-decomposed or direct multi-alphabet CTW, depth `D` configurable (default 8).

* Implements `VocabularyDeclaringCoder`.
* Pure Python is acceptable for v1; document O(D) per symbol.
* Unit test: on an order-1 Markov source, CTW total bits must be within the theoretical redundancy bound of the adaptive Markov-1 coder's bits (assert within a generous constant, e.g. ≤ Markov-1 bits + 2·|V|·D·log2(n) — this is a sanity band, not a tight bound; the test's purpose is catching sign/normalization bugs).

### 1.5 `coding/lz78.py`

Move (or re-export) the existing canonical LZ78 control here unchanged, wrapped in the `SequenceCoder` interface. Bit-for-bit output on the frozen fixtures must match the existing implementation — regression test against stored ledger values.

### 1.6 `coding/grammar_stream.py` — `GrammarStreamCoder`

The heart of the R3 hybrid code. Codes a parse stream (sequence of `Atom`s: terminals, chunk nonterminals, category uses) given a `GrammarState`, using a pluggable base coder.

```python
class GrammarStreamCoder:
    def __init__(
        self,
        base_coder_factory: Callable[[Sequence[TokenId]], SequenceCoder],
        member_alpha: float = 0.5,
    ):
        """base_coder_factory builds the coder over the WORKING vocabulary
        V = base symbols + chunk tokens + category tokens of the state."""

    def data_bits(self, state: GrammarState) -> CodeBreakdown: ...
```

Coding rule:

1. Build `V` from `state.grammar.tokens` (all kinds). Instantiate `base = base_coder_factory(V)`.
2. Walk the parse stream. A `Terminal(t)` or `Nonterminal(N)` atom costs `base.push(token_id)`.
3. A `CategoryUse(M, v)` atom costs `base.push(M_token_id)` **plus** the member code: an adaptive per-category `KTEstimator` over `Ext(M)` (one estimator per category, created lazily, `alpha=member_alpha`). This replaces any static `-log2 p(v|M)` table. No member-distribution parameters are ever transmitted: the member code is prequential too.
4. Return a `CodeBreakdown` dataclass:

```python
@dataclass(frozen=True)
class CodeBreakdown:
    parse_bits: float          # base coder over atoms
    member_bits: float         # sum of category member codes
    total_bits: float          # parse + member
    per_atom: tuple[float, ...] | None = None   # optional, for diagnostics
```

**Critical fairness rule (enforce in code, not convention):** the same `base_coder_factory` (same class, same order, same alpha) must be used when scoring the no-grammar baseline (parse stream = raw symbol stream) and every grammar arm within one experiment. `GrammarStreamCoder` should take the factory once at construction and refuse (raise) attempts to swap it mid-experiment.

### 1.7 `coding/inline.py` — `InlineGrammarCoder` (one-part / fully prequential regime, v2)

A single-pass code with **no separate model stream**. This is the Sequitur-compressor-style regime that dissolves the model-cost accounting problem.

Encoding semantics (must be exactly decodable; see decoder requirement below):

* The coder maintains a growing vocabulary `V_t`, initialized to the declared base alphabet Σ0.
* The stream being coded is the *rewritten* stream under the final grammar, but each chunk token `N` and category token `M` is **defined inline at its first occurrence**:
  * First occurrence of `N`: emit an ESCAPE symbol (a reserved token in every KT table), then a universal integer code (Elias/`log*`) for `|β|`, then the `|β|` tokens of the body coded by the current adaptive coder (bodies may reference already-defined tokens only — enforce topological order), then continue. Subsequent occurrences cost only the (now cheap, adaptively learned) token code for `N`.
  * First occurrence of `M`: ESCAPE, universal code for `|Ext(M)|`, the member tokens under the current coder, then the chosen member under the fresh per-category KT.
* `V_t` grows at each definition; all live KT tables `grow()`.

Requirements:

* Implement `InlineGrammarDecoder` and a round-trip property test: encode → decode reproduces `S0` exactly for randomized small grammars/streams. This is the only place actual (arithmetic-coded or ideal-simulated) decodability must be demonstrated; ideal-bits simulation with a decoder that consumes the same symbol decisions is acceptable — no real bitstream needed, but the decoder must reconstruct the stream from the decision sequence alone.
* Provide `inline_bits(state) -> CodeBreakdown` with `definition_bits` added to the breakdown fields.

### 1.8 Registry

`coding/registry.py`: a string-keyed registry mapping names to coder factories: `static-unigram`, `static-markov-1`, `static-markov-2`, `adaptive-unigram`, `adaptive-markov-1`, `adaptive-markov-2`, `ctw-d8`, `lz78`, `cssr` (added by §5). Experiments reference coders by name; ledgers record the name and full config hash.

---

## 2. Scoring: two new `Scorer` implementations

### 2.1 `scoring/adaptive_mdl.py` — `AdaptiveTwoPartScorer` (v1, default)

```
L(G, S) = L_model(G)  [existing compact binary serialization, unchanged]
        + GrammarStreamCoder.data_bits(state).total_bits
```

* Reuses the existing compact model transmission exactly — this keeps continuity with the July ledgers and isolates the effect of the data-code change.
* Implements `Scorer.score` and `Scorer.delta`. **`delta` must satisfy the consistency invariant** `abs(delta(X, e) - (score(apply(X,e)).total - score(X).total)) < 1e-6` — add a property test. v1 `delta` may simply apply-and-rescore (full recompute). Do not micro-optimize before the ledgers exist; add a `score_cache` keyed by a canonical state digest, and note in a `# PERF` comment that incremental rescoring (windowed recompute around edit sites) is a later optimization that must preserve the invariant.

### 2.2 `scoring/prequential.py` — `PrequentialScorer` (v2)

```
L(G, S) = InlineGrammarCoder.inline_bits(state).total_bits
```

No `L_model` term. Same `Scorer` protocol, same consistency invariant.

### 2.3 Acceptance policies

`GreedyAcceptancePolicy` is unchanged. Add `BeamSearchPolicy(width: int, seed: int)` at the induction-loop level (keep top-B states per depth, deterministic tie-breaking by canonical state digest). Beam lives in `induction/search.py` per the existing layout.

---

## 3. R0 instrumentation: `induction/ledger.py`

Every proposal at every iteration produces one machine-readable record, whether accepted or not.

```python
@dataclass(frozen=True)
class ProposalRecord:
    step: int
    proposal_kind: str            # "chunk" | "category" | "composite" | "prune" | ...
    payload_digest: str           # stable hash of the edit payload
    payload_summary: str          # human-readable, e.g. "chunk len=3 'a b c' x12"
    support: int                  # occurrences / member count
    delta_data_bits: float
    delta_model_bits: float       # 0.0 under PrequentialScorer; definition_bits delta instead
    delta_definition_bits: float  # inline regime only, else 0.0
    delta_total_bits: float
    accepted: bool
    reason: str                   # "best_negative_delta" | "positive_delta" |
                                  # "dominated_by:<digest>" | "overlap_conflict" |
                                  # "reconstruction_failure" | "beam_pruned"
```

* Written as JSONL, one file per run: `ledger/proposals.jsonl`.
* At run end, emit `ledger/final_breakdown.json`: total bits decomposed into `{symbol_dictionary, production_topology, parameters, parse_stream, member_codes, definition_bits, residual_escapes}` (fields that don't apply are 0.0, never omitted).
* The induction loop must route **all** proposals through the ledger — a proposal generated but never scored (e.g. filtered by a support threshold) still gets a record with `reason="filtered:<rule>"`.

**Acceptance test (mandatory, from the diagnostic report):** with the *legacy* generalized-complete-code scorer plugged in, replay the frozen fixture from ledger `20260717T051500Z-generalized-complete-code-gate-v1` and the ledger must reproduce exactly: data saving 6,232 bits, model increment 6,296 bits, total +64, `accepted=False`, `reason="positive_delta"`. This is the regression proving instrumentation doesn't perturb scoring.

---

## 4. Search repairs

### 4.1 `mining/repair_init.py` — `RePairInitializer`

Implements Re-Pair: repeatedly replace the most frequent digram with a fresh nonterminal until no digram occurs twice, yielding a hierarchical grammar (rules referencing rules) plus the reduced stream.

```python
class RePairInitializer:
    def __init__(self, max_rules: int | None = None, seed: int = 0): ...
    def build(self, corpus: Corpus) -> GrammarState:
        """Deterministic; ties broken by lexicographic digram order."""
```

Followed by an **MDL pruning pass** under the *official* scorer (project rule: no private objectives): for every rule, propose `DeleteUnusedRule`/inline-and-remove; accept while ΔL < 0; iterate to fixpoint. Expose via a fit-time option:

```python
CLA.simple(init="repair")     # default remains init="empty"
```

Also provide `SequiturInitializer` behind the same interface if time permits (lower priority; Re-Pair first — it is simpler and deterministic).

The initializer produces an ordinary `GrammarState` whose edit log records one `Edit(kind="InitializeFromRePair", ...)` plus the pruning edits, so replay determinism holds.

### 4.2 `induction/compound_moves.py` — composite chunk+category proposals

New edit kind:

```python
Edit(kind="Composite", payload={"edits": tuple[Edit, ...]})
```

`EditApplier` applies the sub-edits in order inside a transaction: if any sub-edit fails reconstruction, the whole composite rolls back (state is immutable, so "rollback" = discard). The ledger records the composite as one `ProposalRecord` (kind `"composite"`, payload_summary listing sub-kinds) — sub-deltas may be added to `payload_summary` but the decision is atomic.

Proposal generator `CategoryThenChunkProposer` (implements `GrammarSearcher`):

* For each category candidate `C = {v1..vk}` from the existing JS inducer (or the CSSR seeder, §5.3), find frames: maximal contexts `(l, r)` such that `l vi r` occurs for ≥ 2 distinct members. For each frame with total support ≥ `min_support` (default 3), emit the composite `[AddCategory(C), AddChunkRule(A → l M r), RewriteOccurrences(...)]`.
* This is exactly the `a x b a y b a x b` synergy case: neither edit is accepted alone, the pair is.

### 4.3 Proposal budget

Add `max_proposals_per_step` (default 512) with deterministic ranking (by estimated support × length, ties by digest). Everything cut by the budget still gets a `reason="budget_cut"` ledger record. This keeps full-recompute scoring tractable in v1.

---

## 5. New package: `chaoslang/automata/` — the ε-machine track

### 5.1 `automata/cssr.py` — causal-state reconstruction

Implement CSSR (Shalizi–Klinkner causal-state splitting reconstruction), pure Python:

```python
class CSSR:
    def __init__(self, max_history: int, alpha: float = 0.01,
                 test: Literal["chi2", "ks"] = "chi2", seed: int = 0): ...
    def fit(self, stream: Sequence[TokenId]) -> CausalStateMachine: ...
```

```python
@dataclass(frozen=True)
class CausalStateMachine:
    states: tuple[StateId, ...]
    # unifilar transition: (state, symbol) -> state
    transitions: Mapping[tuple[StateId, TokenId], StateId]
    # per-state next-symbol counts (raw, for adaptive coding downstream)
    emission_counts: Mapping[StateId, Mapping[TokenId, int]]
    history_map: Mapping[tuple[TokenId, ...], StateId]  # suffixes up to max_history
    statistical_complexity_bits: float                  # H[state distribution]
```

Standard three phases (initialize with null-history state; split suffixes whose next-symbol distributions differ at level `alpha`; determinize/make unifilar). Determinism: fixed iteration order over sorted suffixes; `seed` reserved for any randomized tie-breaks.

### 5.2 `automata/unifilar_coder.py` — `CausalStateCoder`

Implements `VocabularyDeclaringCoder`: track the current causal state (via `history_map` fallback until synchronized, then `transitions`); code each next symbol with a per-state adaptive `KTEstimator` (initialized *empty*, not from `emission_counts` — training counts inform the *machine topology* only, so held-out coding is honest). Two-part usage: `machine_model_bits()` serializes states + transitions with the existing compact-binary conventions.

Register in the coder registry as `cssr(max_history=L, alpha=a)`.

**This coder plays two roles:** (i) a *control* every grammar arm must beat on chaotic fixtures; (ii) a *candidate CLA output* in its own right for the attractor track.

### 5.3 `automata/causal_categories.py` — `CSSRCategoryInducer`

Implements `CategoryInducer`. Rule: tokens `v, w` are proposed as co-members when the machine's transition structure treats them equivalently — concretely, when for every state `s` reached with support ≥ `min_support`, `transitions[(s, v)] == transitions[(s, w)]` (they induce the same successor state wherever both occur). Emit ordinary `AddCategory` proposals with `provenance={"source": "cssr", "machine_digest": ...}`. This is the probabilistic-substitutability version of the paradigmatic category and the intended replacement/supplement for blind JS clustering; both inducers can run side by side and the ledger will show whose proposals get accepted.

---

## 6. Configuration and CLI

Extend the experiment config schema:

```yaml
scorer: adaptive_two_part          # legacy_two_part | adaptive_two_part | prequential
base_coder: adaptive-markov-2      # registry name; frozen per experiment
member_alpha: 0.5
init: repair                       # empty | repair | sequitur
search: greedy                     # greedy | beam
beam_width: 16
compound_moves: true
max_proposals_per_step: 512
category_inducers: [js, cssr]
controls: [static-unigram, static-markov-1, static-markov-2,
           adaptive-unigram, adaptive-markov-1, adaptive-markov-2,
           ctw-d8, lz78, cssr]
ledger: true                       # may not be disabled in experiment runs
```

Every run artifact must record: config hash, coder registry names + full params, git commit, seed, and (unchanged from current practice) frozen prefix/suffix boundaries.

---

## 7. Testing invariants (additions to the existing suite)

**Coding invariants**

1. KT closed-form cross-check (§1.2).
2. CTW sanity band vs adaptive Markov-1 on Markov-1 sources (§1.4).
3. LZ78 regression: bit-identical to stored frozen-fixture values.
4. `code_stream` is order-sensitive: shuffling a structured stream must not decrease adaptive-Markov-2 bits on the frozen structured test string (statistical test, 20 shuffles, seed-fixed).
5. Inline coder round-trip: encode→decode reproduces `S0` (property test, randomized grammars).
6. Fairness guard: `GrammarStreamCoder` raises if asked to score two arms with different factories.

**Scorer invariants**

7. `delta`/`score` consistency (≤ 1e-6) for both new scorers, property-tested over random small states and edits.
8. `model_bits + data_bits + definition_bits == total_bits` (tolerance) for every scorer.
9. Legacy replay: the 6,232 / 6,296 / +64 fixture reproduces exactly under the legacy scorer with ledger enabled (§3).

**Search invariants**

10. Re-Pair determinism: same corpus ⇒ identical grammar and edit log.
11. Re-Pair exact reconstruction after build and after every pruning edit.
12. Composite atomicity: a composite whose second sub-edit breaks reconstruction leaves no trace in the state (only a ledger record).
13. Beam determinism under fixed seed.

**Automata invariants**

14. CSSR on a planted 2-state hidden Markov source recovers 2 causal states (alpha default, n ≥ 10k, ≥ 4/5 seeds).
15. `CausalStateCoder` on a planted unifilar source beats adaptive-Markov-1 in held-out bits (the machine has longer memory than order 1 by construction of the fixture).
16. CSSR determinism.

**Ledger invariants**

17. Every generated proposal has exactly one record; accepted count in ledger == length of edit log delta.
18. `final_breakdown.json` totals equal the scorer's reported totals (tolerance).

---

## 8. Milestones (implementation order — do not reorder)

* **M-A (coding core):** `coding/` package: protocols, KT, AdaptiveMarkov, LZ78 wrapper, registry. Tests 1–4, 6.
* **M-B (instrumentation):** `induction/ledger.py`, wire into the existing loop, legacy-scorer replay regression (test 9, 17, 18). *Ship M-A+M-B before anything else — the eval programme's E0/E1 need only these.*
* **M-C (adaptive two-part scorer):** `GrammarStreamCoder`, `AdaptiveTwoPartScorer`, per-category adaptive member codes. Tests 7–8.
* **M-D (search):** `RePairInitializer` + MDL pruning, composite moves, beam, proposal budget. Tests 10–13.
* **M-E (automata):** CSSR, `CausalStateCoder`, `CSSRCategoryInducer`. Tests 14–16. CTW can land here too (it is a control, not a blocker).
* **M-F (one-part regime):** `InlineGrammarCoder` + decoder + `PrequentialScorer`. Test 5.

Each milestone must leave `main` green; `PYTHONPATH=src python3 -m unittest discover -s tests -v` remains the test command.

---

## 9. Antipatterns (extends the existing list)

* **Do not** let any miner, inducer, or initializer consult a coder other than the experiment's frozen `base_coder` when estimating deltas. Estimates may be crude, but the referenced objective must be the official one.
* **Do not** initialize `CausalStateCoder` emission KTs from training counts (leaks training statistics into held-out coding).
* **Do not** implement the inline coder without its decoder. Undécodable "code lengths" are the road back to the proxy-score era.
* **Do not** optimize `delta` with incremental recomputation before the property test (invariant 7) exists and passes on the naive version.
* **Do not** remove or alter the legacy static controls or legacy scorer; they are regression anchors.

---

## Appendix: paste-block for the coding agent

```
Implement the chaoslang upgrade in milestone order M-A..M-F per
chaoslang_upgrade_spec.md. Core rules: (1) all coders implement the
SequenceCoder prequential protocol and return ideal bits from push();
(2) the same base coder (class+order+alpha) must be used for the
no-grammar baseline and every grammar arm in an experiment — enforce
this in GrammarStreamCoder; (3) category member codes are adaptive
per-category KT estimators, never transmitted tables; (4) every
proposal at every step produces exactly one ProposalRecord in a JSONL
ledger, including filtered and budget-cut proposals; (5) Re-Pair
initialization is deterministic and followed by MDL pruning under the
official scorer; (6) composite chunk+category edits are atomic;
(7) CSSR machines inform topology only — held-out coding uses fresh
adaptive emission estimators; (8) the inline one-part coder must have
a decoder and a round-trip property test; (9) the legacy scorer replay
of the 6232/6296/+64 fixture is a mandatory regression; (10) never
change chaoslang.core semantics or the public CLA API. Chunks are
sequences; categories are substitutability sets; exact reconstruction
after every accepted edit.
```
