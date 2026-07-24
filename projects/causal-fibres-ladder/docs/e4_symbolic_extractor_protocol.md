# E4 Input-Derived Symbolic Extractor Protocol

## Question

Can a deployment-time analyzer read the raw synthetic-grammar input, derive a
non-label-equivalent symbolic constraint without factor-label access, and
recover material CS task-loss headroom through the frozen direct-logit sink?

The decisive threshold is mean defined-seed
`G=(SC_loss-FF_loss)/(TC_loss-FF_loss) > 0.20` for a realistically noisy
extractor. Teacher-clamped (TC) settlement remains a diagnostic denominator,
not a deployed input.

## Provenance boundary

The extractor API receives only the raw input tensor, the public four-block
input schema, an extraction-accuracy setting, and a random seed. It does not
receive `GrammarBatch.factors`, target labels, teacher logits, or model
predictions.

For each of the four two-coordinate factor blocks, the analyzer takes the
argmax as its clean symbolic reading. At requested accuracy `p`, it flips each
reading independently with probability `1-p`, using a local seeded generator.
The lexical nuisance suffix is ignored. Ground-truth factors may be compared
with extractor output only after extraction, to report realized fidelity; they
must not participate in constraint construction.

## Constraint compiler

For every accuracy `p ∈ {1.0, 0.95, 0.9, 0.8, 0.7}`, compile three
non-label-equivalent statements from the extracted readings:

1. `subset3_123`: the class belongs to the subset matching extracted
   `obj_num`, `tense`, and `negation`; exactly two labels remain possible.
2. `parity_03`: extracted `subj_num XOR negation` equals the class relation;
   eight labels remain possible.
3. `implication_2_1`: if the class matches the extracted tense literal, it
   also matches the extracted object-number literal; twelve labels remain.

These cover subset, parity, and implication structure while preserving at
least two possible labels. The same generic allowed-class direct-logit sink
used by the prior E4 diagnostic receives the compiled masks.

## Validation invariants

- Clean extraction exactly reconstructs all four one-hot factors.
- Lexical nuisance changes do not change extracted factors.
- Seeded noise is deterministic, does not mutate the input, and has the
  requested Bernoulli error mechanism.
- Constraint masks depend only on extractor output and public class-bit
  semantics.
- The clean input-derived masks equal oracle-factor masks as an audit, while
  the runtime path never consumes the oracle.
- All constraint conjunctions leave at least two classes possible.
- Model weights remain unchanged during inference.

## Calibration and freeze

- Calibration seeds: `33013, 34123, 35227`.
- Reserved disjoint confirmation seeds: `36341, 37447, 38557, 39671, 40787`.
- Evaluate 128 examples on each ID and CS split.
- Use the already confirmed sink schedule: 64 steps, step size `0.2`,
  constraint weight multiplier `5`, anchor weight `1`, and reference
  constraint count `2`.
- Rank only the three `p=0.9` conditions by calibration mean defined-seed CS
  task-loss G. Freeze the best as the primary before confirmation. This fixes
  realistic extraction accuracy at 90% while allowing calibration to choose
  which relational form is most useful.

## Confirmation gates

Freeze the following before unblinding confirmation:

- primary mean defined-seed CS `G > 0.20`;
- at least three defined confirmation seeds individually have `G > 0.20`;
- every emitted condition leaves at least two labels possible;
- extractor provenance audit passes on every run.

Report CS task accuracy as an outcome, not a selection criterion. Report the
full accuracy curve and degradation relative to the input-derived `p=1.0`
counterpart. Compare clean-input performance with the prior factor-oracle E4
diagnostic, while distinguishing seed differences.

## Relevant research rules

Rules 1, 2, 5, and 7 are binding: explicitly validate the extractor and
compiler, specify the provenance boundary before coding, retain exact
commands/raw evidence, and keep extraction separate from constraint
compilation and sink execution.
