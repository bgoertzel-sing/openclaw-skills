# Frame-oracle v8 empty-slot behavior contract

- Frozen: `2026-08-04T19:20:39Z`
- Source baseline: `agent/frame-oracle-v7` commit
  `61776efe74738efffb3434a2b5fce5bff65ca18e`
- Status: source-derived behavior frozen; implementation absent; v8 unopened

## Source counterexample

The generation schema permits arbitrary strings for both entity slots. V7's
proposal validator checks only that they are strings. For a non-unknown
proposal, v6 then whitespace-canonicalizes the slots and constructs a strict
`ClosedFrame` without requiring either canonical slot to be non-empty.

Three independent source-only fixtures therefore produce valid non-unknown
semantic keys with (1) an empty `entity_a`, (2) an empty `entity_b`, or (3)
both slots empty. A non-empty control remains unchanged. These outputs violate
the closed ontology's slot meanings but do not raise or abstain.

## Bounded v8 rule

Validate canonical slot occupancy after the existing v7 proposal-envelope and
predicate/abstention checks, before accepting a non-unknown frame:

1. Canonicalize both slots with the existing whitespace/lowercase rule.
2. If either canonical slot is empty, return canonical unknown with the
   proposal confidence preserved.
3. Otherwise delegate unchanged to v7/v6 behavior.

This is a fail-closed union rule, not an inference rule. It does not infer a
missing entity, repair an entity string, or score whether a non-empty entity is
semantically correct.

## Preserved behavior

- Keep `SYSTEM_PROMPT_V8` byte-identical to v7.
- Keep the closed schema, ontology, confidence handling, strict
  `ClosedFrame` validation, v7 predicate/abstention union, v6 all-occurrence
  slot masking, and finite polarity/modality recognizers unchanged.
- Preserve canonical unknown behavior and non-empty non-unknown behavior.
- Do not change the atomic runner or any sealed-gate artifact in the behavior
  implementation step.

## Acceptance fixtures

- whitespace-only `entity_a` becomes canonical unknown;
- whitespace-only `entity_b` becomes canonical unknown;
- both whitespace-only slots become canonical unknown;
- canonical unknown remains canonical unknown;
- a non-empty non-unknown proposal remains byte-for-byte behavior-compatible
  with v7;
- malformed proposal fields and direct strict-`ClosedFrame` mismatch rejection
  remain fail-closed.

Focused fixtures, all exposed frame/runner regressions, and the full repository
suite must pass from a clean isolated descendant before runner work begins.

## Boundary

This contract was derived only from frozen source and synthetic fixtures. No
v7 case, proposal, response, normalized row, or answer was inspected. No v8
case or answer was read, and no model endpoint, inference, label corpus,
readout, substitution evaluation, semantic loss, remote compute, push, or
publication was used.

Evidence:
`experiments/20260804T192000Z-frame-oracle-v8-source-behavior-audit-r4/`.
