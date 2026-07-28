# P0/P1 execution specification and theorem-assumption audit

- Status: source-grounded execution contract, pre-implementation
- Date: 2026-07-26
- Scope: local CPU implementation and calibration planning only
- Paid/GPU compute: not authorized and not required by this document

## 1. Decision and evidential boundary

P0/P1 validate an HDC measurement instrument. They do not test frozen GPT-2,
causal module structure, linguistic universality, or guided-training benefit.
No P2–P6 result is interpretable until the P0 core gates and P1 instrument-law
gate pass.

P1 must keep three claims separate:

1. independent-random cleanup follows the familiar `D / k` law;
2. a **constructed** coherent dictionary follows a
   `D(1-nu) / k` law and may exhibit the near-duplicate exponents;
3. an implicational hierarchy, without a constituent-sharing code design,
   causes adjacent feature codes to become coherent.

The first two have source theorems or conditional derivations. The third is
the synthesis paper's explicit Conjecture 1. A planted near-duplicate code can
validate the instrument and conditional scaling, but cannot confirm that
linguistic hierarchies naturally induce that code geometry.

## 2. Source authority

| Label | Source | Binding use |
|---|---|---|
| S | `library/hdc-cgcct-source-manuscripts-2026/hdc_cgcct_synthesis.pdf`, SHA-256 `086f...fb20` | Programme intent, frame Eq. 4, P0/P1 procedures and provisional gates |
| HDC-06 | Same bundle, `hdc_guided_factorization_v5.pdf`, SHA-256 `fd5f...21d9` | Independent cleanup, local-query capacity, resonator conditions, factorization defect |
| HDC-07 | `library/resonator-factored-hierarchical-hypervector-embeddings/paper.pdf`, SHA-256 `8643...6f7` | Coherence-limited Lemma 3, near-duplicate Remark 2, toy T2b evidence |
| C | Same bundle, `category_guided_causal_coding_transformers.pdf`, SHA-256 `6601...9f21` | Closure loss and Theorem 7.3's delta-calibration assumption |
| CFL | `projects/causal-fibres-ladder` records and local E1 worktree commit `4ca1b5ee337934c9cf8b349adbd3716dc7baa221` | Deterministic seed/hash patterns, constructed controls, 3/5 calibration/confirmation discipline |

The synthesis's coherence formula matches HDC-07, not HDC-06. HDC-07 is
therefore the only local source that can support the coherence-aware formula.
This version relationship is inferred from equation content; the synthesis
does not pin a source hash.

Exact evidence locations:

- S Eq. 2, frame Eq. 4, and Conjecture 1: pp. 4–6; extracted text
  lines 158–270.
- S P0/P1 procedures and provisional gates: Appendix A.3–A.4, pp. 10–11;
  extracted text lines 482–540.
- HDC-06 Assumptions 1–2 and supported-query restriction: pp. 6–8; extracted
  text lines 295–375.
- HDC-06 independent cleanup/local capacity: pp. 11–13; extracted text
  lines 542–673.
- HDC-07 Assumptions 1–3: pp. 6–7; extracted text lines 349–386.
- HDC-07 coherence-aware Lemma 3, near-duplicate Remark 2, and fixed-family
  Theorem 1: pp. 13–14; extracted text lines 638–764.
- HDC-07 toy T2b study: p. 36; extracted text lines 1891–1926.
- C closure loss and approximate closure theorem: pp. 10 and 17; extracted
  text lines 498–521 and 884–901.

## 3. Frozen algebra and conventions

### 3.1 Code families

The primary family is float32 bipolar MAP:

- atoms: `a in {-1,+1}^D`, sampled independently with a named seeded
  `torch.Generator`;
- binding: `a tensor b = a * b` (Hadamard product);
- inverse: `a^dagger = a`;
- bundling: an unnormalized integer/float32 sum;
- normalization:
  `sign_plus(x)_i = +1 if x_i >= 0 else -1`;
- permutation: `pi(x) = roll(x, +1)` and
  `pi_inverse(x) = roll(x, -1)`;
- similarity: `sim(x,y) = <x,y> / D` for bipolar, norm-`sqrt(D)` vectors;
- canonical dictionary order: ascending UTF-8 identifier;
- cleanup: highest score, with an exact score tie resolved to the lowest
  canonical index;
- cleanup margin:
  `Delta = s_true - max_{j != true} s_j`.

The exact-zero-to-`+1` rule fills a gap in S Appendix A.2. Randomized
tie-breaking is forbidden.

A secondary linear family is used only for the near-duplicate scaling audit:
sum child terms in float32, rescale each dictionary entry to norm `sqrt(D)`,
and rank by cosine. Do not mix results from bipolar and linear normalization.
Phasor codes are out of P0/P1 scope because no local implementation is
validated.

### 3.2 Frame record and encoding

A frame record is a canonical tuple:

```text
frame_type: string
roles: ordered tuple[(role_id, filler_id)]
relations: ordered tuple[(relation_id, source_role_id, target_role_id)]
features: ordered tuple[feature_id]
```

All tuples are sorted by identifier before encoding. The bipolar frame code is
the deterministic realization of S Eq. 4:

```text
F = sign_plus(
      r_type * h_frame_type
    + sum(r_role * h_filler)
    + sum(r_relation * (r_source * h_source)
                     * pi(r_target * h_target))
    + sum(r_feature * h_feature)
)
```

Sign/phasor rebind, swap, and restrict operations rebuild the bundle from the
canonical frame record; they must not subtract from an already sign-normalized
code.

Feature score:

```text
s_a(F) = <F, r_feature * h_a> / D.
```

For a learned continuous readout `u`, report both:

- raw normalized score using `sqrt(D) * u / max(||u||, tiny)`;
- primary bipolar score after `sign_plus(u)`.

### 3.3 Coherence and capacity quantities

For dictionary `C = {c_1,...,c_M}`:

```text
nu_abs(C) = max_{i != j} |<c_i,c_j>| / D
nu_pos(C) = max_{i != j}  <c_i,c_j>  / D
nu_i(C)   = max_{j != i}  <c_i,c_j>  / D
x_i       = D * (1 - nu_i) / k.
```

`nu_abs` is the conservative theorem quantity; `nu_pos`/`nu_i` diagnose the
positive near-duplicate mechanism. Never replace a measured coherence by a
nominal construction value.

The source bound is

```text
P_fail <= 2 M exp[-c D (1-nu) / k],
D >= alpha * k/(1-nu) * log(2M/epsilon),  alpha = 1/c.
```

The constant is distribution-dependent and unknown. P1 fits `alpha` on
calibration seeds and evaluates it without refitting on confirmation seeds.
Eq. 2 is not a parameter-free numerical prediction.

## 4. P0: library and known-answer fixtures

### 4.1 Required implementation seams

The eventual package must expose independent modules:

```text
atoms.py       seeded atoms, canonical IDs
algebra.py     bind, bundle, normalize, permutation
frames.py      record validation, encode/rebuild, rebind/swap/restrict
cleanup.py     scores, deterministic cleanup, margin, coherence
resonator.py   projected slot updates and recomposition score
fixtures.py    known-answer and capacity fixtures
artifacts.py   canonical JSON, hashes, manifest
```

No transformer dependency belongs in the core HDC module.

### 4.2 Property and known-answer tests

Run every exact test at `D in {64, 256}` and seeds `{101, 211}`:

1. `bind(a, bind(a,x)) == x` exactly for bipolar inputs.
2. Permutation preserves norm and its inverse recovers the exact vector.
3. Canonical record order does not change the encoded frame.
4. Rebind, swap, and restrict equal a fresh encoding of the edited record.
5. Cleanup returns the known target and reports the hand-computed top-two
   margin on a four-entry dictionary.
6. Exact cleanup ties choose the lowest canonical index.
7. A zero bundle coordinate maps to `+1`; repeated encoding is bit-identical.
8. Directed two-role frame:
   - with target permutation ablated, argument exchange has cosine `1.000`
     exactly;
   - with permutation, its cosine lies within `0.05` of the mean unrelated
     pair cosine from 1,024 matched random pairs.
9. Role mask removes only declared terms and produces the specified empty-code
   behavior (empty record is rejected rather than normalized).
10. Batched and scalar cleanup return identical indices, scores, and margins.
11. Resonator:
    - a constructed positive fixture with positive slot margin recovers;
    - a zero/negative-margin fixture is not required to recover;
    - success is never described as arbitrary-initialization convergence;
    - all restart, iteration, and recomposition costs are recorded.

### 4.3 P0 independent-cleanup capacity fixture

For each `(D,k,M)`:

- `D = {128,256,512,1024,2048,4096}`;
- `k = {4,16,64}`;
- `M = {32,256}`;
- 2,048 independent trials per cell and outer seed;
- trial target `a*` and `M-1` distractors are independent bipolar atoms;
- query is `z = a* + sum_{j=1}^{k-1} e_j`, with independent bipolar
  crosstalk terms;
- dictionary and crosstalk are redrawn per trial;
- record target score, maximum distractor score, margin, predicted index,
  success, and measured coherence.

P0 is a qualitative wiring calibration, not the final fitted law. It must show
a positive association between `D/k` and accuracy and a negative association
between `M` and accuracy, with no unexplained reversal larger than 0.05
accuracy. P1 supplies disjoint-seed confirmation.

### 4.4 P0-v2 resolution-grid amendment (authorized 2026-07-27)

The original v1 fixture is retained as a failed-closed result: its
`k=4, M=32` curve was accuracy-saturated at every tested dimension and could
not demonstrate the required qualitative resolution.  Benjamin Goertzel
authorized a fixture/grid revision, while retaining the P0-G1 gate contract
and all deterministic conventions.

P0-v2 uses `D = {32,64,128,256,512,1024}`, `k = {32,64,128}`, and
`M = {32,256}`, with the same 2,048 trials per cell, seed, atom distribution,
query construction, scoring, and two-replay requirement.  The lower-D and
higher-load settings are selected before the v2 scientific replay to expose a
capacity transition, not to optimize a passing threshold.  The old payload,
hash, and failure remain part of the record.  Run v2 through
`scripts/run_p0_gate_v2.sh`; do not overwrite v1 artifacts.

## 5. P1A: capacity and coherence instrument validation

P1A is oracle-code-only. It isolates HDC cleanup from transformer readout error.

### 5.1 Fixtures

Use dimensions

```text
D = {64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384}
```

and 2,048 trials per cell. A preflight may reduce trials to 256 solely for
runtime/memory estimation; preflight outcomes cannot set scientific gates.

**F0 independent null.** Target and dictionary entries are mutually
independent. Crosstalk is independent. This is the HDC-06/HDC-07 Lemma 2
regime.

**F1 coherent positive.** Build each entry from `k` ordered child terms.
The target and its designated near duplicate use identical child terms in
positions `0..k-2` and independent fillers at position `k-1`. Remaining
dictionary entries are independent composites. Crosstalk terms are independent
of the identity of the confusable pair. This is the HDC-07 Lemma 3/Remark 2
regime, not a linguistic claim.

**F2 correlated-noise pathology.** Reuse the differing child in the crosstalk
under the same role product, violating Lemma 3's independence condition.
This fixture must not be expected to follow Eq. 18. It detects an
implementation or interpretation that silently applies the bound outside its
assumptions.

**F3 hierarchy-distance stress.** Starting from a `k`-child composite, replace
one additional child at each hierarchy step. Adjacent entries differ in one
child; distance-`d` entries differ in `d`. Run both bipolar-sign and linear
normalizations. This measures the planted geometry only.

Use `k = {4,8,16,32,64}`. Use `M=32` for F1–F3 to reproduce the source T2b
shape; use `M={32,128,512}` for F0 to estimate the log-`M` term.

### 5.2 Required-dimension and law fit

For each cell and seed:

```text
p_fail = failures / n
U95     = one-sided 95% Wilson upper bound
D*_grid = smallest D such that U95 <= epsilon at D and every larger tested D
epsilon = 0.01.
```

Also fit a binomial logistic curve versus `D` for interpolation. A cell is
`left_censored`, `interior`, or `right_censored`; only interior cells estimate
an exponent. Raw grid values remain authoritative.

On calibration cells, fit

```text
log D* = b0 + b_k log k + b_M log log(2M/epsilon)
```

by weighted least squares with seed-cluster bootstrap confidence intervals.
For the coherence-law prediction, set

```text
alpha_i = D*_i / [k_i/(1-nu_i) * log(2M_i/epsilon)]
alpha_hat = geometric median(alpha_i)
D_pred = alpha_hat * k/(1-nu) * log(2M/epsilon).
```

Freeze `alpha_hat`, eligible cells, and all thresholds before confirmation.

### 5.3 Monotonicity

Finite binomial estimates need not be strictly monotone. Operationalize S
Gate 1 as:

- Spearman correlation between `D` and accuracy is at least `0.90` within
  every eligible `(fixture,k,M,seed)` curve;
- no adjacent dimension has a statistically resolved decrease greater than
  `0.02` (two-sided paired/independent binomial interval as applicable);
- isotonic-regression deviation is reported, not hidden.

This is a finite-sample implementation of a monotone trend, not a theorem that
every observed grid point must increase.

## 6. P1B: planted-PCFG readout and closure-noise fixture

P1B measures the extra error introduced by a trained transformer and linear
frame readout. Its result must never be substituted for P1A's cleanup law.

### 6.1 Exact finite PCFG

For hierarchy length `H in {4,6}`, generate fixed-length sequences:

```text
<bos> SUBJECT VERB OBJECT TENSE POLARITY DISTRACTOR
       HIER_1 ... HIER_H <eos>
```

Independent root choices are uniform:

- `SUBJECT`: 8 tokens;
- `VERB`: 16 tokens;
- `OBJECT`: 8 tokens;
- `TENSE`: 2 tokens;
- `POLARITY`: 2 tokens;
- `DISTRACTOR`: 8 tokens;
- hierarchy rank `J`: integers `0..H`.

At hierarchy position `h` (one-indexed), emit active marker `A_h` iff
`J >= h`, else inactive marker `I_h`. Define feature label
`y_h = 1[J >= h]`. Therefore every sample satisfies
`y_h => y_{h-1}` for `h=2..H`.

This is a known-answer morphosyntactic surface, not evidence about natural
language. The final hierarchy-token residual, immediately before predicting
`<eos>`, is the frame-readout site.

### 6.2 Samples and splits

Enumerate all tuples `(H,J,subject,verb,object,tense,polarity,distractor)`.
Set:

```text
sample_id = SHA256(
  "hdc-cgcct-pcfg-v1|" + pipe-separated canonical tuple
)
```

Within each `(H,J)`, assign by the first unsigned 64 bits of `sample_id`:

- let `bucket = uint64(sample_id[0:8]) mod 100`;
- bucket `0..69`: training;
- bucket `70..84`: calibration;
- bucket `85..99`: confirmation.

Select the lowest hashes in each bucket to obtain, per rank:

- 2,048 training samples;
- 512 calibration samples;
- 512 confirmation samples.

No sentence identity may cross splits. The split manifest and its SHA-256 are
frozen before model training.

### 6.3 Six-layer transformer

Implement a causal decoder with six pre-norm attention/MLP blocks. Freeze in
the first config:

```text
d_model=128, n_heads=4, d_ff=512, layers=6, dropout=0,
AdamW, lr=3e-4, weight_decay=0.01, batch=128,
max_updates=10000, gradient_clip=1.0.
```

Checkpoint selection uses calibration next-token NLL, evaluated every 100
updates. Stop after 10 evaluations without an improvement of `1e-4`; retain
the earliest checkpoint attaining the best NLL. “Train to convergence” means
this rule and nothing else. Model weights and sample order are identical
across HDC dimensions within an outer seed.

The causal-fibres `SyntheticGrammar` and `TokenMixingSixBlockStudent` are not
this fixture: they are fixed-vector classifiers, not a PCFG next-token model.
Only their deterministic seeding, sample hashing, six-block seam, and artifact
patterns are reusable.

### 6.4 Frame targets and readouts

Each sequence's canonical frame record contains subject, verb, object, tense,
polarity, and every active hierarchy feature.

For each `D`, train a fresh linear `K_D: R^128 -> R^D` by mean squared error
to the bipolar frame code, using frozen transformer residuals. Select the
ridge parameter from `{0,1e-6,1e-4,1e-2}` on calibration MSE, breaking ties
toward the larger penalty. Freeze before confirmation.

Evaluate three arms:

1. **oracle code:** ground-truth frame encoded directly;
2. **linear K:** sign-normalized `K_D(z)`;
3. **representation control:** independent logistic probes from the same
   residual to each `y_h`.

Also evaluate shuffled feature labels and an independent-feature-code
dictionary. The same trained transformer and held-out examples are shared
across arms.

### 6.5 Probe and closure metrics

For each feature `h`:

```text
gap_h = mean(s_h | y_h=1) - mean(s_h | y_h=0)
tau_h = threshold minimizing balanced error on calibration data
BER_h = 0.5 * (FPR_h + FNR_h)
delta_max_h = max(FPR_h, FNR_h).
```

Threshold candidates are midpoints of distinct calibration scores; exact ties
select the largest threshold (conservative presence call). Thresholds are
frozen before confirmation.

For every planted edge `h => h-1`:

```text
violation = 1[pred_h=1 and pred_{h-1}=0]
V_all     = mean(violation over all held-out samples)
V_active  = mean(violation | y_h=1)
```

Report both. S defines the primary “fraction of held-out states” as `V_all`.
The score gap is not called CGCCT's theorem-level delta; Theorem 7.3 does not
define an estimator that licenses that substitution.

### 6.6 Hierarchy-code arms

Run two target-code constructions:

- **independent feature atoms:** Eq. 4's ordinary independently sampled
  feature atoms; no adjacent/distant coherence difference is expected;
- **planted path composites:** feature code `q_h` is the F3 sequential
  constituent-sharing construction; adjacent coherence is expected.

The second arm tests whether the probe sees the conditional HDC regime. The
first is a direct counter-control to the phrase “by construction” in
Conjecture 1. Neither arm establishes what representation natural linguistic
hierarchies learn.

### 6.7 P1B amendment: target-code realization and dimension grid (2026-07-28)

For each calibration outer seed, run `H in {4,6}`, both code arms, and

```text
D = {64,128,256,512,1024,2048,4096}.
```

This is intentionally distinct from P1A's cleanup grid: P1B reads a fixed
128-dimensional residual into at most six hierarchy features. The dyadic grid
tests compression through a 32-fold expansion without presenting P1A's
17-point cleanup resolution as a P1B requirement. The runner must stream
target batches and record peak GPU memory; it stops rather than changes this
grid if the approved resource limit is exceeded.

For each `(outer_seed,D)`, derive a bipolar float32 atom table using
`component_seed(outer_seed, "p1b-v1|D|atoms")`. Atom IDs are namespaced by
`p1b-v1|D|...`; binding is elementwise multiplication and `sign_plus(0)=+1`.
For PCFG sample `(H,J,S,V,O,T,P,N)`, use the same non-feature terms in both
arms:

```text
B = r_type*h_frame_pcfg_H
  + r_subject*h_subject_S + r_verb*h_verb_V + r_object*h_object_O
  + r_tense*h_tense_T + r_polarity*h_polarity_P + r_distractor*h_distractor_N
F = sign_plus(B + sum(h=1..J, r_feature*q_H,h)).
```

The distractor is explicitly retained as a declared frame role. Feature score
is `<F, r_feature*q_H,h>/D`; inactive features add no term.

- **Independent arm:** `q_H,h` is an independently sampled atom with ID
  `feature|independent|H{H}|h{h}`.
- **Planted path-composite arm:** for each `H`, draw independent role-bound
  terms `b_H,i = path_role_H,i * path_base_H,i` and
  `r_H,i = path_role_H,i * path_replacement_H,i`, then set
  `q_H,h = sign_plus(sum_i (b_H,i if i <= h else r_H,i))`. Thus adjacent
  features share exactly `H-1` constituents and distance `d` changes exactly
  `d` constituents, matching the F3 geometry.

Report coherence of both `q_H,h` and `r_feature*q_H,h`; full-frame-code
coherence is diagnostic only because lexical terms are shared. `H=4` and
`H=6` namespaces remain disjoint. The transformer weights, residuals, split,
and outer seed are shared across arms. The planted arm remains a constructed
positive control, not evidence for natural hierarchy geometry.

## 7. Determinism and seed separation

Use calibration outer seeds:

```text
12011, 13121, 14251
```

and sealed confirmation seeds:

```text
15313, 16417, 17519, 18637, 19739.
```

Derive every component seed independently:

```text
seed(component, outer) =
  little_endian_uint64(
    SHA256("hdc-cgcct-v1|" + outer + "|" + component)[0:8]
  ) mod 2^63.
```

Components include at least `atoms`, `fixture`, `model_init`,
`train_order`, `readout`, `bootstrap`, and `pathology`. No global RNG may be
consumed before a component generator is created.

CPU conventions:

- Python, NumPy, and Torch seeds recorded;
- `torch.use_deterministic_algorithms(True)`;
- dropout disabled;
- float32 scientific arrays, float64 aggregation;
- single-thread replay check with `OMP_NUM_THREADS=1` and
  `MKL_NUM_THREADS=1`;
- two identical invocations must produce identical scientific payload hashes;
- wall time and peak RSS are explicitly excluded from the scientific hash.

GPU results, if ever authorized later, need tolerance-based replay and a new
environment record; CPU bitwise replay must not be weakened retroactively.

## 8. Frozen gates

### P0-G0: algebra and artifact integrity

Pass only if all P0 property tests pass, scalar/batched results match exactly,
the orientation gate passes, two CPU replays have the same scientific hash,
all arrays are finite, and the artifact manifest verifies.

### P0-G1: qualitative independent-capacity curve

Pass only if every eligible P0 curve has positive `D/k` association, no
unexplained accuracy reversal greater than 0.05, and increasing `M` does not
improve accuracy by more than 0.05 at matched `(D,k)`.

### P1-G1: coherence-law confirmation (programme stop gate)

After constructed positive/null/pathology controls and three calibration
seeds, freeze `alpha_hat`. Pass on five confirmation seeds only if:

- at least 80% of prespecified cells have an interior `D*`;
- at least 90% of eligible confirmation cells satisfy
  `0.5 <= D*_grid / D_pred <= 2`;
- the median ratio is in `[0.75,1.33]`;
- monotonicity conditions in Section 5.3 pass;
- F2 is reported separately and is not used to rescue or reject the
  assumption-matched fit.

Failure stops P2–P6 interpretation.

### P1-G2: closure-noise floor

At the smallest tested `D >= D_pred` for each condition, pass only if both
oracle-code and linear-`K` arms have pooled `V_all` with one-sided Wilson
`U95 < 0.01` on confirmation, every feature has `BER <= 0.05`, and the
linear-`K` violation rate exceeds the oracle arm by no more than 0.005 under a
seed-cluster paired bootstrap upper bound.

If the oracle passes and `K` fails, classify `readout_not_calibrated`, not
`HDC_law_failed`. If both fail, classify `instrument_failed`.

### P1-G3: conditional near-duplicate scaling

For F3:

- well-separated fitted `b_k` must have a 95% seed-bootstrap interval
  containing `1.0`;
- linear near-duplicate `b_k` must contain `2.0` and have lower bound `>1.5`;
- bipolar-sign near-duplicate `b_k` must contain `1.5` and have lower bound
  `>1.15`;
- adjacent `nu_pos` must exceed distance-2 `nu_pos` on all confirmation seeds.

The independent-feature hierarchy arm must not be forced to pass an adjacency
effect. Outcomes are labeled `conditional_scaling_reproduced` or
`conditional_scaling_not_reproduced`. Conjecture 1 remains `unresolved` unless
a non-planted learned or natural hierarchy induces the geometry.

### Stop rules

Stop and report partial evidence if:

- a deterministic/core invariant fails twice after bounded fixes;
- calibration/confirmation sample identities overlap;
- any threshold is changed after confirmation access;
- P1-G1 fails;
- the fitted boundary is mostly outside the dimension grid;
- local preflight estimates exceed 24 CPU-hours or 32 GiB peak RAM without a
  revised sufficient-statistics design;
- paid/GPU work would be required without explicit approval.

## 9. Raw artifact contract

Each run lives at:

```text
experiments/<UTC>-p0-p1-<phase>-v1/
```

Required files:

```text
RUN.md
command.sh
config.json
config.sha256
source-manifest.json
seeds.json
split-manifest.json
environment.json
git.txt
stdout.log
stderr.log
exit-status.txt
status.json
metrics.json
gate.json
raw/manifest.json
raw/cleanup-index.jsonl
raw/probe-index.jsonl
raw/*.npy
artifact-manifest.sha256
```

`raw/cleanup-index.jsonl` has one record per cell/array slice:

```json
{
  "schema": "hdc-cgcct.cleanup-index.v1",
  "phase": "calibration",
  "outer_seed": 12011,
  "fixture": "F1_near_duplicate",
  "code_family": "bipolar_sign",
  "D": 1024,
  "k": 16,
  "M": 32,
  "trials": 2048,
  "arrays": {
    "success": "cleanup-F1-...-success.npy",
    "target_score": "cleanup-F1-...-target-score.npy",
    "max_distractor_score": "cleanup-F1-...-max-distractor.npy",
    "margin": "cleanup-F1-...-margin.npy",
    "nu_target": "cleanup-F1-...-nu-target.npy"
  },
  "dictionary_stream_sha256": "...",
  "scientific_slice_sha256": "..."
}
```

`raw/probe-index.jsonl` records:

```json
{
  "schema": "hdc-cgcct.probe-index.v1",
  "sample_id": "...",
  "split": "confirmation",
  "outer_seed": 15313,
  "H": 6,
  "D": 4096,
  "arm": "linear_K",
  "model_sha256": "...",
  "readout_sha256": "...",
  "feature_labels": [1, 1, 0, 0, 0, 0],
  "feature_scores": [0.31, 0.27, -0.02, -0.08, -0.11, -0.14],
  "feature_predictions": [1, 1, 0, 0, 0, 0],
  "edge_violations": [0, 0, 0, 0, 0]
}
```

Feature score/prediction arrays have length `H`; edge arrays have length
`H-1`. Large numeric data use uncompressed `.npy` files with dtype, shape,
endianness, semantic name, and SHA-256 in `raw/manifest.json`. Do not rely on
pickled tensors or nondeterministic archive timestamps. `metrics.json` is
derived and replaceable; raw arrays and manifests are authoritative.

`status.json` must distinguish `preflight`, `calibration`, `criteria_frozen`,
`confirmation`, `failed_closed`, and `complete`. A confirmation command must
reject any config not marked `criteria_frozen` and must verify disjoint seeds
and split hashes.

## 10. Reusable local infrastructure audit

| Component | Local evidence | Disposition |
|---|---|---|
| Seed/component hashing, canonical JSON, model hashes | causal-fibres E1 `e1_homotopy.py` at commit `4ca1b5e...` | Reuse pattern after copying into a new owned package with attribution/provenance |
| Six-block deterministic seam and exact replay tests | same module/tests; `11 passed in 2.26s` on 2026-07-26 | Reuse test conventions, not scientific model |
| SyntheticGrammar | four independent binary factors plus lexical Gaussian nuisance | Do not call it a PCFG or hierarchy fixture; replace for P1B |
| TokenMixingSixBlockStudent | six attention/MLP virtual-token blocks | Useful CPU plumbing reference; not an autoregressive token transformer |
| Calibration/confirmation discipline | causal-fibres decisions/configs require constructed controls and disjoint 3/5 seeds | Adopt |
| HDC MusicGen companion script | role-bound bipolar atoms, cleanup, resonator sketches | Reference only; it is monolithic, import-unsafe at module load, and not a tested P0 library |
| `causal-fibres` 0.4.0 release | probe/measurement toolkit | No frame-code/cleanup implementation found; not a substitute for P0 |

No unrelated worktree was modified.

## 11. Exact next commands

The next implementation turn should create a dedicated local repository, not
edit the dirty causal-fibres or RelaLeap worktrees:

```bash
cd /home/openclaw/research-agent
mkdir -p projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes
git -C projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes init -b main
python3 -m venv projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes/.venv
```

After adding a hash-locked CPU requirements file and the P0 module/tests:

```bash
cd /home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes
.venv/bin/python -m pip install --require-hashes -r requirements-cpu.lock
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 .venv/bin/python -m pytest -q tests/test_algebra.py tests/test_frames.py tests/test_cleanup.py tests/test_resonator.py tests/test_artifacts.py
.venv/bin/python -m hdc_cgcct.run --config configs/p0_selftest_v1.json --output ../../experiments/p0-preflight-v1
.venv/bin/python -m hdc_cgcct.verify ../../experiments/p0-preflight-v1
```

Only after P0-G0/G1 pass:

```bash
.venv/bin/python -m hdc_cgcct.run --config configs/p1a_calibration_v1.json --output ../../experiments/p1a-calibration-v1
.venv/bin/python -m hdc_cgcct.freeze --run ../../experiments/p1a-calibration-v1 --output configs/p1_criteria_frozen_v1.json
.venv/bin/python -m hdc_cgcct.run --config configs/p1_confirmation_frozen_v1.json --criteria configs/p1_criteria_frozen_v1.json --output ../../experiments/p1-confirmation-v1
.venv/bin/python -m hdc_cgcct.verify ../../experiments/p1-confirmation-v1
```

These commands are the planned acceptance interface. They are not executable
until the listed implementation/config files exist; this specification does
not claim that code has been written.

## 12. Theorem-assumption audit

| Claim | Source status | Required assumptions / gap | P0/P1 treatment |
|---|---|---|---|
| `P_fail <= 2M exp(-cD/k)` | Established as HDC-06 Lemma 2 and HDC-07 Lemma 2, conditional | Independent normalized random atoms, sub-Gaussian overlap, isometric binding, target plus independent crosstalk, finite fixed dictionary | F0 and P0 capacity fixture |
| `P_fail <= 2M exp[-cD(1-nu)/k]` | Established as HDC-07 Lemma 3, conditional; absent from HDC-06 | Crosstalk randomness independent of confusable-distractor identity; measured `nu<1`; same concentration/isometry assumptions | F1 positive and F2 assumption-violation pathology |
| `D ~ k^2 log M` for linear/phasor near duplicates | Conditional asymptotic derivation in HDC-07 Remark 2 | Adjacent entries differ in one of `k` equally scaled constituents, raw overlap `1-Theta(1/k)`, normalization preserves it; constants unknown | F3 linear reproduction; no phasor claim |
| `D ~ k^(3/2) log M` for sign MAP | Conditional arcsine-law asymptotic plus toy evidence in HDC-07 | Child sums approximately jointly Gaussian; sign correlation follows arcsine law; asymptotic regime and constants; source toy shaped the refinement and was not independently preregistered here | F3 bipolar reproduction with disjoint seeds |
| Fixed-family local query capacity | Established conditional theorem | Fixed non-adversarial query family, bounded depth/load, reusable finite dictionaries, coherence controlled, union-bound accounting | P0 only tests single-step/local queries; no global memory claim |
| Resonator recovery | Established only under positive slot margins | Basin entry, positive margin every update, projection, finite iterations/restarts, recomposition rejection | P0 tests positive/pathology fixtures and records cost; no arbitrary-start guarantee |
| CGCCT approximate closure preservation | Algebraic telescoping theorem C 7.3 | Probes are already delta-calibrated; one-step closure score error bounded; chain length known | Report empirical scores/errors; do not equate them to theorem delta without a definition |
| “HDC discharges CGCCT probe calibration” | Not established as stated | Learned `K_D` adds factorization, approximation, finite-sample, and optimization error outside cleanup theorem; algebraic scores are not automatically calibrated probabilities | Separate oracle-code and linear-`K` gates; classify failures by layer |
| “Implication hierarchies are near duplicates by construction” | Explicit S Conjecture 1, not theorem | Needs a representation map that makes adjacent features share constituents. Eq. 4 with independent feature atoms does not do this | Independent-code counter-control plus planted-composite positive; conjecture remains unresolved |
| Hierarchy-adjacent required `D` exceeds distant by the predicted factor | Conjectural for linguistic features; conditional for F3 | Distance must actually control measured coherence, and load `k` must not be conflated with hierarchy length `H` | Measure `H`, `k`, distance, and `nu` separately |
| Probe “calibration” is positive-vs-negative score gap | Programme operational definition, not C Theorem 7.3 definition | A mean gap does not control uniform probability error or thresholded false violations | Report gap, BER, `delta_max`, and closure violation separately |
| Calibration improves monotonically in `D` | Population trend suggested by bound, not strict finite-sample theorem | Fixed distribution, no readout-capacity/optimization confound, adequate trials | P1A primary; robust monotonic trend rule; P1B error decomposed |
| Similarity can only decrease under composition | Asserted in S Section 3.1, not generally proved | Requires non-expansive maps/normalizations; arbitrary rebind, projection, or learned maps may increase pairwise similarity | No guarantee transfer; property-test each operation and report changes |
| Orientation permutation is necessary | Algebraically established for commutative symmetric encoding; empirical source support | Ordered roles/permutation independent enough that exchanged code reaches unrelated baseline | P0 exact ablation plus random-baseline gate |
| P1 confirms linguistic hierarchy scaling | Not licensed | Synthetic markers and planted code geometry are known-answer fixtures, not typological or cognitive evidence | Report only instrument validation and conditional scaling |

## 13. Rules applied

Research Rules 1, 2, 3, 5, 6, and 7 are binding here: validate the
estimator, freeze the plain-language spec first, reuse tested infrastructure
only at valid abstraction seams, preserve reproducible raw evidence, separate
theorem from conjecture, and keep algebra/fixture/model/artifact components
replaceable.
