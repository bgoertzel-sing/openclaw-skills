# Frame-oracle v12 finite coordination behavior contract

- Frozen: `2026-08-06T17:20:46Z`
- Parent implementation: clean frame-oracle v11 at `46c16f0`
- Status: source counterexample reproduced; implementation absent; v12 unopened

## Source observation

The inherited prompt requires sentences containing more than one proposition
to use the canonical unknown frame, but deterministic normalization has no
general multi-proposition guard. Four independent fixtures spanning
`capital_of`, `located_in`, `authored_by`, and `state` used an ASCII comma
followed by `and` to coordinate a second overt clause. All four remained
non-unknown and had the same semantic key as their matched one-proposition
controls.

This is a bounded source capability counterexample. It is not evidence that
the sealed v12 battery contains coordinated clauses and does not diagnose any
prior gate result.

## Frozen finite rule

For a schema-valid proposal:

1. Preserve inherited v11 handling when the proposal predicate is `unknown` or
   `abstain=true`.
2. Otherwise apply the inherited whitespace normalization and exact
   case-insensitive surface masking to every occurrence of both canonical
   proposed slots.
3. In the masked remainder only, recognize the finite ASCII delimiter regex
   `,\s+and\b` case-insensitively.
4. If that delimiter occurs, return the canonical unknown frame while
   preserving validated proposal confidence.
5. Otherwise delegate byte-for-byte to frame-oracle v11.

Do not infer coordination from bare `and`, other coordinators, semicolons,
punctuation without `and`, dependency parsing, or lexical/prosodic cues. Do
not trigger on the delimiter inside a fully masked proposed slot. Do not alter
the prompt, ontology, question guard, polarity/modality logic, template guard,
provenance, or runner.

## Independent acceptance fixtures

A separate implementation turn must cover at least:

- all four non-unknown predicates with independent comma-`and` coordinated
  sentences;
- matched one-proposition controls;
- a comma-`and` delimiter wholly inside each proposed slot position;
- bare `and`, alternative punctuation/coordinators, and unmatched sentences;
- inherited unknown/abstain handling and invalid-envelope rejection;
- confidence preservation and prompt identity;
- focused v12, exposed v1--v12, pinned-complete, and host-complete regression
  suites from a clean committed isolated worktree.

Implementation, runner/provenance adaptation, and inference remain separate
turns. The sealed v12 files and answers remain out of scope.
