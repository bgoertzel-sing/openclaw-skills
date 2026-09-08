# Frame-oracle v11 terminal-question behavior contract

- Frozen: `2026-08-06T07:14:09Z`
- Parent implementation: clean frame-oracle v10 at `ad7fe09`
- Status: source counterexample reproduced; implementation absent; v11 unopened

## Source observation

The inherited prompt requires questions to use the canonical unknown frame,
but deterministic normalization has no interrogative guard. Four independent
terminal-question fixtures spanning `capital_of`, `located_in`, `authored_by`,
and `state` remained non-unknown when supplied surface-grounded proposals.
Four matched declarative controls were preserved.

This is a source capability counterexample. It is not evidence that questions
occur in v11 and does not diagnose any prior gate result.

## Frozen finite rule

For a schema-valid proposal:

1. Preserve inherited v10 handling when the proposal predicate is `unknown` or
   `abstain=true`.
2. Otherwise trim only trailing whitespace from the source sentence.
3. If the last remaining character is the ASCII question mark `?`, return the
   canonical unknown frame while preserving validated proposal confidence.
4. Otherwise delegate byte-for-byte to frame-oracle v10.

Do not infer interrogative force from auxiliary order, lexical cues, prosody,
Unicode punctuation, or indirect-question syntax. Do not alter the prompt,
ontology, polarity/modality logic, template guard, provenance, or runner.

## Independent acceptance fixtures

A later implementation turn must cover at least:

- all four non-unknown predicates with independent terminal-`?` sentences;
- matched declarative controls;
- trailing-whitespace handling;
- inherited unknown/abstain and invalid-envelope behavior;
- confidence preservation and prompt identity;
- focused, exposed, and full regression suites.

Implementation, runner/provenance adaptation, and inference must remain
separate turns. The sealed v11 files and answers remain out of scope.
