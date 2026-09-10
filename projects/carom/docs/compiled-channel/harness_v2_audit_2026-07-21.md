# CAROM `harness_v2.py` instrument audit

Date: 2026-07-21

## Scope and provenance

Ben supplied `harness_v2.py` through Telegram. The received file is preserved
at `media/inbound/openclaw-staged-aa973b0d-3d47-4093-8965-94a2feb6450e/`
`harness_v2---3b7ad187-d484-463f-81d6-16225e6ed090.py` with SHA-256
`16bea664b1cc4f75726fbc56f147cafe5b1478c96d789babbab5bc4c10a9b3db`.

This audit compares it with
`projects/carom/repos/carom/exp2_compiled_channel.py` and
`projects/carom/docs/teach-loop/exp3_teach.py`. Research Rules 1, 2, 5, and 7
apply: validate estimators with constructed cases, freeze metric semantics,
preserve exact evidence, and keep the span-extraction interface replaceable.

## Observed checks

- `python3 -m py_compile <received-file>`: passed.
- `python3 <received-file> --selftest`: passed. The supplied perfect, subset,
  reversed, smeared, and perfect-edge fixtures behave as asserted.
- A forced trajectory for ranks `[0,1,2,3]` produces phases `[0,1,2,3]`.
  The initially suspected forced/shuffled indentation problem is absent from
  the actual file.

## Failures found by additional counterexamples

### 1. Revisits are erased before order and transition scoring

For phases `[0,1,0,2,3]` against the true order `[0,1,2,3]`, the harness
reports `exact_order=1`, transition precision/recall `1/1`, and `revisits=1`.
This is internally inconsistent. `dict.fromkeys(seq)` removes the repeated
phase before computing exact order and transitions. Exact order must compare
the complete dwell-collapsed phase sequence with the true sequence;
transition metrics must score every observed phase transition. First-visit
Kendall tau may remain a separate, explicitly named diagnostic.

### 2. AUROC is not tie-corrected

With six live directed pairs, one positive edge, and all logits equal, true
AUROC is `0.5`. Moving the positive edge among matrix positions makes the
harness return `1.0`, `0.8`, `0.6`, or `0.2`. `torch.argsort` assigns arbitrary
within-tie ranks. Use average ranks or direct pairwise comparisons with ties
worth one half. Add all-tied and mixed-tie fixtures. AUPRC's tie convention
must also be stated and tested.

### 3. The span path is incompatible with the repository's GPT-2 adapter

`eval_checkpoint`, `intervention_suite`, and `budget_sweep` call
`E2.span_reps` unconditionally. In the current repository,
`GPT2Base.hidden(T)` returns `(hidden_states, attention_mask)`, while
`span_reps` expects a tensor. GPT-2 requires `span_reps_gpt2`. Each public
evaluation function should accept a frozen `span_fn` (or adapter object), and
the chosen base/layer/tokenizer and corpus offsets must be recorded.

## Additional validity risks

- Frozen corpora currently contain tensors on the generator's global
  `DEVICE`. Canonical artifacts should be CPU tensors with hashes, then moved
  explicitly at evaluation time. This avoids device-dependent serialization
  and load/device failures.
- Argmax always declares a winning mode, even for uniform/smeared or nearly
  tied activity. Add dominance margin, normalized entropy, and an unclassified
  state; otherwise a smeared trajectory becomes an arbitrary mode itinerary.
- Forced and shuffled interventions are exposure-matched to each other, but
  not to the natural trajectory. Interpret `forced-shuffled` causally; compare
  either with an exposure-matched natural replay or report mass/dwell/update
  norms before interpreting natural-versus-clamped differences.
- `budget_sweep` mutates `model.S` without `try/finally`; an exception can
  leave the model altered.
- Degenerate edge cases with no positive or no negative edges should return an
  explicit undefined value, not a denominator-clamped number.

## Decision

Do not use this file unchanged to revise the Exp2/Exp3 conclusions. It is a
useful repair draft and its frozen-corpus, intervention, budget-sweep, and
paired-M2 structure should be retained, but the three verified failures above
must be repaired and regression-tested first. After that, run the repaired
harness on fixed paired corpora and preserved checkpoints; never compare its
new metrics directly with old random-batch log values as if they were the same
estimator.

