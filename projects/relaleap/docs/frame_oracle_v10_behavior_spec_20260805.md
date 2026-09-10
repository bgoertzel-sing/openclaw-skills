# Frame-oracle v10 source-derived behavior contract

- Contract: `frame-oracle-v10-overt-template-consistency-1`
- Frozen: `2026-08-05`
- Parent source: clean v9 commit
  `8edead5b3977b9ce15761df3ae33dbd1b4e2639c`
- Status: source behavior frozen; v10 battery unopened; implementation absent

## Question

Can the accepted v9 normalizer emit a surface-grounded non-unknown semantic
key whose predicate or directed slots contradict an overt closed-ontology
relation in the sentence?

## Source-derived counterexamples

V9 requires only that both proposed canonical slots occur somewhere in the
sentence. It does not bind those occurrences to the proposed predicate or
their directed semantic roles. Four independent synthetic probes reproduce
the gap:

1. `A is located in B` proposed as `state(A, B)`;
2. `The capital of A is B` proposed as `located_in(A, B)`;
3. `A is located in B` proposed as `located_in(B, A)`;
4. `B wrote the novella A` proposed as `authored_by(B, A)`.

All four remain non-unknown under v9. Matching `located_in`, `capital_of`,
`authored_by`, and `state` controls are unchanged. These fixtures are invented
source probes and do not use any sealed v10 case or answer. This establishes a
source capability gap only; it does not establish that the gap caused v9's
aggregate gate failure.

## Frozen v10 rule

Add one finite, conservative overt-template consistency guard after v9's
structural, occupancy, and surface-grounding checks and before delegation:

1. Whitespace-normalize the sentence and canonicalize captured/proposed slots
   using the inherited rules.
2. Recognize only these unambiguous overt template families, in order from
   most specific to least specific:
   - `the capital of A is B` -> `capital_of(A, B)`;
   - `A is located in B` -> `located_in(A, B)`;
   - `B wrote [the novel|the novella] A` -> `authored_by(A, B)`;
   - `A was written by B` -> `authored_by(A, B)`;
   - simple copular `A is B` after excluding the preceding templates ->
     `state(A, B)`.
3. Strip only template punctuation and the listed generic work-title words;
   do not infer aliases, synonyms, coreference, facts, or implicit relations.
4. When exactly one template matches, require the proposal predicate and both
   directed canonical slots to equal the template-derived values.
5. On any mismatch, return canonical unknown and preserve proposal confidence.
6. On an exact match, or when no listed template matches, delegate unchanged
   to v9.
7. Preserve the v9 prompt byte-for-byte.

This is a negative consistency guard, not a replacement parser. It deliberately
does not reject sentences outside the finite template families.

## Acceptance boundary

An isolated v10 implementation may be accepted only if independent fixtures
cover wrong predicate, reversed roles, exact controls, unknown/abstention,
empty and absent slots, whitespace/case normalization, unmatched paraphrases,
and invalid envelopes; focused, exposed, and full suites must pass from a clean
descendant commit. Runner/provenance adaptation must remain a separate unopened
step. No model call, label corpus, readout, substitution evaluation, or semantic
loss is admitted by this contract.

## Evidence

`experiments/20260805T192502Z-frame-oracle-v10-source-behavior-audit/`

