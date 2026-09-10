# Frame-oracle v6 bounded behavior specification

- Status: source-derived; implementation not started
- Parent: consumed v5 implementation at `a90298b`
- Evidence:
  `experiments/20260804T031820Z-frame-oracle-v6-source-behavior-audit-r2/`
- Exclusions: no v5 gate row/proposal/normalized output and no v6 public case
  or answer was used

## Bounded hypothesis

The v5 surface layer masks only one non-overlapping occurrence of each
proposed entity slot. If a name or title is repeated in a parenthetical alias
or byline, a later occurrence remains visible to the finite cue recognizers
and can falsely set polarity or modality. Masking every exact surface
occurrence of both proposed slots before cue recognition should close this
specific source contradiction.

This hypothesis is limited to deterministic polarity/modality ownership after
a schema-valid closed proposal. It does not claim to repair predicate or slot
selection, abstention, proposal nondeterminism, cue scope outside exact slot
mentions, or any consumed v5 outcome.

## Required behavior

1. Preserve the v5 prompt, closed schema, slot canonicalization, canonical
   unknown behavior, state-slot cleanup, and finite polarity/modality cue
   vocabularies byte-for-byte.
2. Whitespace-normalize the sentence and compile the existing
   case-insensitive, word-bounded pattern for each non-empty proposed slot.
3. Mark the union of every surface span matched by either slot pattern.
   Overlapping matches are harmless because all matched characters are entity
   material; no first-match or slot-order preference may leave another exact
   occurrence unmasked.
4. Replace the marked characters with spaces before the unchanged v5 cue
   recognizers run. Do not delete characters in a way that concatenates tokens.
5. Do not add fuzzy, substring, semantic, alias, or coreference matching. A
   mention that is not an exact case-insensitive whitespace-normalized slot
   occurrence remains outside this bounded contract.

## Independent fixtures

Implementation tests must include new synthetic examples covering:

- a repeated title containing `could`, with asserted modality;
- a repeated author name containing `May Not`, with affirmed/asserted output;
- a repeated located-entity name containing lower-case `no`, with affirmed
  polarity;
- a single-mention control showing that v5 masking behavior remains intact;
- overlapping or identical slot strings, demonstrating union masking without
  dependence on slot iteration order;
- the complete exposed v2--v5 regression suite.

The audit fixtures are not oracle outcomes or battery rows. They were authored
from source inspection and are recorded in the linked experiment.

## Engineering and scientific gates

A later turn may implement only this all-occurrence union mask on a fresh
isolated descendant of `a90298b`, using independent fixtures. It must run
focused, exposed-regression, and full tests from a clean commit and then adapt
the atomic v6 runner/import-provenance freeze in a separate step before any
inference.

The scientific gate remains the existing one-use 24/24 conjunction. Passing
this engineering contract does not admit labels, readout, substitution
scoring, or a semantic loss.
