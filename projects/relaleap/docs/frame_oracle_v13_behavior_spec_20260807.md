# Frame-oracle v13 finite semicolon-coordination behavior contract

- Frozen: `2026-08-07T03:25:23Z`
- Parent implementation: clean frame-oracle v12 at `228ff13`
- Status: hypothesis falsified; conditional rule rejected; v13 unopened

## Source hypothesis

The inherited prompt requires sentences containing more than one proposition
to use the canonical unknown frame. V12 owns only the finite masked-remainder
ASCII comma-`and` delimiter. It therefore appears to preserve non-unknown
proposals when an ASCII semicolon followed by `and` coordinates a second overt
clause.

This is a bounded source capability hypothesis. It is not evidence that the
sealed v13 battery contains coordinated clauses and cannot diagnose any prior
gate result.

## Rejected conditional finite rule

The preregistered independent audit did not reproduce the premise: all four
semicolon-`and` fixtures already became canonical unknown through the inherited
v10 whole-sentence template guard. The following rule is therefore rejected
and must not be implemented:

1. Preserve inherited v12 handling when the proposal predicate is `unknown` or
   `abstain=true`.
2. Apply the inherited whitespace normalization and exact case-insensitive
   surface masking to every occurrence of both canonical proposed slots.
3. In the masked remainder only, recognize the finite ASCII delimiter regex
   `;\s+and\b` case-insensitively.
4. If that delimiter occurs, return the canonical unknown frame while
   preserving validated proposal confidence.
5. Otherwise delegate byte-for-byte to frame-oracle v12.

Do not generalize to bare `and`, comma-`and`, other coordinators, other
punctuation, dependency parsing, or lexical/prosodic cues. Comma-`and` remains
owned by v12. Do not trigger on a delimiter wholly inside a masked proposed
slot. Do not alter the prompt, ontology, question guard, polarity/modality
logic, template guard, provenance, or runner.

## Superseded planned acceptance

The following preregistered implementation coverage is retained only as
provenance for the rejected hypothesis. It is not an admissible implementation
plan:

- all four non-unknown predicates with independent semicolon-`and` sentences;
- matched one-proposition controls;
- a semicolon-`and` delimiter wholly inside each proposed slot position;
- comma-`and`, bare `and`, alternative punctuation/coordinators, and unmatched
  sentences;
- inherited unknown/abstain handling and invalid-envelope rejection;
- confidence preservation and prompt identity;
- focused v13, exposed v1--v13, pinned-complete, and host-complete regressions
  from a clean committed isolated worktree.

No implementation, runner/provenance adaptation, or inference is admitted from
this rejected contract. The sealed v13 files and answers remain out of scope.

## Falsification evidence

`experiments/20260807T032523Z-frame-oracle-v13-source-behavior-audit/`
records the unchanged 0/4 result and passing 50 focused, 311 exposed, 479
pinned plus 5 skipped, and 502 host regressions. This negative result is a
counterexample to the source hypothesis, not evidence about sealed v13 case
contents.
