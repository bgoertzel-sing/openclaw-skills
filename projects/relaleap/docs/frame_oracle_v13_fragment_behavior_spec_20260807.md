# Frame-oracle v13 finite slot-only-fragment behavior contract

- Frozen: `2026-08-07T05:31:56Z`
- Parent implementation: clean frame-oracle v12 at `228ff13`
- Status: source counterexample reproduced; rule frozen; v13 unopened

## Source counterexample

The inherited prompt requires fragments to use the canonical unknown frame.
Clean v12 nevertheless preserves grounded non-unknown proposals for four
independent punctuation-separated slot-only fragments spanning `capital_of`,
`located_in`, `authored_by`, and `state`. Each fragment has the same semantic
key as its matched full-sentence control and preserves proposal confidence.

After all exact case-insensitive whitespace-normalized occurrences of both
canonical proposed slots are masked, every reproduced fragment remainder has
no ASCII letter. Each matched one-proposition control retains at least one
ASCII letter in its masked remainder.

This is a bounded source capability counterexample. It is not evidence that
the sealed v13 battery contains slot-only fragments and cannot diagnose a
prior gate result.

## Frozen finite rule

1. Strictly validate the proposal envelope exactly as v12 does.
2. Preserve inherited handling when the raw proposal predicate is `unknown`
   or `abstain=true`.
3. Canonicalize both proposed slots and mask the union of every exact surface
   occurrence using the inherited whitespace normalization, boundary rules,
   and case-insensitive matching.
4. If the masked remainder contains no ASCII letter matching `[A-Za-z]`,
   return the canonical unknown frame while preserving validated confidence.
5. Otherwise delegate byte-for-byte to frame-oracle v12.

Do not generalize this guard to a parser, lexical verb list, Unicode letter
classifier, clause detector, punctuation taxonomy, or sealed-case-dependent
rule. Do not alter the prompt, ontology, polarity/modality logic, question,
template, or comma-`and` guards, provenance, or runner.

## Required implementation coverage

- all four non-unknown predicates with fresh independent slot-only fragments;
- matched declarative controls with at least one ASCII letter after masking;
- proposed slots containing punctuation and ASCII letters internally;
- repeated and overlapping exact slot occurrences under inherited union
  masking;
- remainders containing digits or non-ASCII symbols but no ASCII letters;
- remainders with one ASCII letter, which must delegate unchanged;
- inherited unknown/abstain handling and invalid-envelope rejection;
- confidence preservation and prompt identity;
- focused v13, exposed v1--v13, pinned-complete, and host-complete regressions
  from a clean committed isolated worktree.

Implementation, runner/provenance adaptation, and inference are separate
turns. No sealed v13 path or answer, v12 opened material or identifier, model
endpoint, label corpus, readout, substitution evaluation, semantic loss,
remote compute, push, publication, or semantic-free lane input may be used.

## Evidence

`experiments/20260807T052500Z-frame-oracle-v13-fragment-source-audit/`
records the 4/4 counterexample and passing 50 focused, 311 exposed, 479 pinned
plus 5 skipped, and 502 host regressions at unchanged clean commit `228ff13`.
