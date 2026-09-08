# Frame-oracle v9 source-derived behavior contract

- Contract: `frame-oracle-v9-surface-grounding-1`
- Frozen: `2026-08-05`
- Parent source: clean v8 commit
  `96460e99fd3ae76e242ca82cabdc499da2570266`
- Status: source behavior frozen; v9 battery unopened; implementation absent

## Question

Can the accepted v8 normalizer emit a non-unknown semantic key when either
proposed canonical entity slot has no exact surface occurrence in the input
sentence?

## Source-derived counterexample

V8 checks that both canonical slots are non-empty, then delegates to v6. The
v6 masker silently skips a slot when its boundary-delimited pattern has no
match and nevertheless constructs a non-unknown frame. Three independent
synthetic `state` proposals reproduce the gap:

1. absent `entity_a`, present `entity_b`;
2. present `entity_a`, absent `entity_b`;
3. both slots absent.

All three remain non-unknown under v8. A control with both slots present is
unchanged. These fixtures are invented source probes; they do not use v8
opened material, v9 cases, or v9 answers.

## Frozen v9 rule

For a structurally valid, non-abstaining, non-unknown proposal:

1. preserve v8's categorical, type, confidence, abstention-union, and
   non-empty-slot checks;
2. canonicalize both slots using the inherited whitespace/lowercase rule;
3. compile each canonical slot with the inherited boundary-delimited
   `_slot_pattern` matcher;
4. require at least one exact case-insensitive surface match for each slot in
   the whitespace-normalized sentence;
5. if either slot has no match, return the canonical unknown frame and
   preserve proposal confidence;
6. otherwise delegate unchanged to v8.

The two matches need not be distinct. Do not guess, complete, lemmatize,
translate, synonym-expand, or repair either slot. Do not use substring-only
matching. Preserve the v8 prompt byte-for-byte.

## Acceptance boundary

An isolated implementation may be accepted only if independent fixtures prove
absent-a, absent-b, and both-absent proposals fail closed; controls for both
present, canonical unknown, predicate/abstention mismatch, empty slots, and
invalid envelopes preserve v8 behavior; and focused, exposed, and full suites
pass from a clean descendant commit.

Atomic runner adaptation, source/import/model provenance, and exact argv must
be frozen separately after behavior implementation. V9 must remain
`opened=false` throughout both steps. No label corpus, readout, substitution
evaluation, or semantic loss is admitted.

## Evidence

`experiments/20260805T090359Z-frame-oracle-v9-source-behavior-audit/`
