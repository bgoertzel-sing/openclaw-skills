# Frame-oracle v14 finite predicate-specific relation-bearing contract

- Frozen: `2026-08-07T19:11:00Z`
- Parent implementation: clean frame-oracle v13 at `8108d98`
- Status: contract frozen; implementation and v14 execution forbidden

## Source basis

Clean v13 accepts relationless grounded fragments whenever exact proposed-slot
masking leaves one unrelated ASCII letter. The independent source audit
reproduced this for every non-unknown predicate. This contract closes only
that finite source gap. It makes no claim about sealed v14 contents and was
written without accessing v14 cases or answers.

## Frozen finite rule

1. Strictly validate the proposal envelope exactly as v13 does.
2. Preserve inherited handling when the raw proposal predicate is `unknown`
   or `abstain=true`.
3. Apply v13 unchanged. If it returns canonical unknown, return that result.
4. Normalize the whole sentence and proposed slots exactly as the inherited
   v10 `_overt_template`, `_template_slot`, and `_work_title_slot` helpers do.
5. Accept a remaining non-unknown proposal only when `_overt_template(sentence)`
   returns exactly `(predicate, canonical entity_a, canonical entity_b)` for
   the proposal. Otherwise return canonical unknown while preserving validated
   confidence.

The inherited finite predicate-specific relation forms are therefore exactly:

- `capital_of`: `The capital of <entity_a> is <entity_b>`;
- `located_in`: `<entity_a> is located in <entity_b>`;
- `authored_by`: `<entity_b> wrote the novel|novella <entity_a>` or
  `<entity_a> was written by <entity_b>`;
- `state`: `<entity_a> is <entity_b>`.

Matching is whole-sentence, case-insensitive, and whitespace-normalized with
only inherited terminal template punctuation and authored-title handling. Do
not add synonyms, inflections, token lists, parsers, Unicode categories, or
sealed-case-dependent exceptions. Do not change prompts, ontology, polarity,
modality, confidence, prior guards, provenance, or runner behavior.

## Fresh implementation fixtures

The implementation turn must author new names and sentences not present in the
2026-08-07 source audit or any sealed battery. Before running them, freeze:

- one positive whole-template case for each of `capital_of`, `located_in`, and
  `state`, plus both active and passive `authored_by` forms;
- matched relationless fragments with an unrelated residual ASCII word;
- wrong-relation and wrong-predicate controls whose slots still match;
- slot-order reversals for every asymmetric predicate;
- relation words occurring wholly inside a proposed slot;
- partial, prefixed, suffixed, and multi-proposition template lookalikes;
- inherited unknown/abstain and invalid-envelope controls;
- confidence preservation, prompt identity, and exact delegation controls.

Positive fixtures must equal v13 output. Every negative fixture must become
canonical unknown. Focused v14, all exposed v1--v13 regressions, the pinned
complete suite, and host-complete tests must pass from a clean committed
isolated worktree. Any discrepancy fails closed without editing fixtures.

## Boundaries and sequencing

Implementation, runner/provenance adaptation, and one-use inference are
separate future turns. The current v14 battery remains sealed, unopened, and
unconsumed. Forbidden are v14 paths or answers, opened v13 rows or identifiers,
oracle/model calls, labels, readout, substitution evaluation, semantic loss,
remote compute, publication, push, and semantic-free exploration input.

## Evidence

- Source counterexample:
  `experiments/20260807T171100Z-frame-oracle-v14-source-behavior-audit/`
- Contract-freeze record:
  `experiments/20260807T191100Z-frame-oracle-v14-relation-bearing-contract/`
