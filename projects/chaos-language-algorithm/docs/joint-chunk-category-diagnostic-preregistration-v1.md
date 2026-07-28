# CLA minimal joint chunk/category diagnostic — preregistration v1

**Frozen:** 2026-07-16 PDT, before implementation output or diagnostic scores were inspected  
**Status:** separate failure-branch diagnostic; not a rerun or rescue of the failed held-out attractor benchmark

## Question

Under the current sprint-1 MDL proxy, can a deliberately minimal synthetic
stream contain a beneficial generalized chunk/category move that the current
single-edit learner cannot reach? This distinguishes a local proposal/search or
representation failure from a fixture on which the current accounting makes
the intended joint move non-beneficial.

This diagnostic makes no chaos, attractor, predictive-coding, or semantic
grammar claim. It uses no Mackey--Glass or Lorenz--96 data and must not affect
their frozen held-out suffixes.

## Frozen fixture

Construct 19 four-token frames in order:

`a, m00, b, q00, a, m01, b, q01, ..., a, m18, b, q18`

The 19 middle symbols and 19 separators are distinct. The intended abstract
category is `M={m00,...,m18}` and the intended generalized chunk is
`N -> a M b`. The unique separators prevent repeated cross-frame n-grams. The
fixture size is frozen at 19 frames because, under the frozen proxy costs below,
it is the smallest integer frame count for which the prescribed abstract joint
move is strictly beneficial:

- initial score: `4r`;
- joint score: category `(14+r)`, chunk `(0.8+3)`, two edit-log entries `0.2`,
  and top-level data `2r`, hence `18+3r`;
- joint improvement requires `18+3r < 4r`, or `r > 18`.

## Frozen learner and costs

- `CLA.simple(max_iterations=8, seed=0, n_min=2, n_max=5,
  min_uses=2, enable_categories=True, category_method="exact",
  miner="ngram")`.
- `SimpleMDLScorer`: chunk overhead 0.8, category overhead 14.0,
  one data unit per ordinary parse entry, category-member side cost as currently
  implemented, and 0.1 per edit-log entry.
- The abstract joint score uses those same costs, not a new tuned scorer.

## Frozen measurements and classification

Report:

1. fixture token count and SHA-256 of canonical compact JSON symbols;
2. initial proxy score;
3. fitted greedy score, history, production/category counts, exact reconstruction,
   and deterministic repeat equality;
4. whether the current category inducer proposes the intended 19-member category;
5. after manually applying that exact category, whether the current chunk miner
   proposes a member-agnostic `a M b` block;
6. prescribed abstract joint score and delta using the frozen formula.

Classify exactly one primary result:

- `greedy_or_representation_blindness`: abstract joint delta is negative, the
  greedy learner does not improve, and the member-agnostic generalized chunk is
  unavailable;
- `accounting_blocks_joint_gain`: abstract joint delta is nonnegative;
- `greedy_reaches_improvement`: the greedy learner improves the proxy score;
- `integrity_failure`: reconstruction, determinism, fixture hash, or frozen
  formula checks fail.

The first label does not prove the proposed joint grammar is scientifically
meaningful; it only identifies a concrete limitation of the current proposal /
representation path. No parameters may be changed after results are inspected.

## Integrity and command freeze

The implementation must assert the analytical formulas, exact reconstruction,
determinism, intended fixture uniqueness, and fixture hash. The experiment
record freezes the final clean code commit, implementation-file hashes, exact
command, Python/platform provenance, and pre-run tests before `results.json` is
created.

