# Frame-oracle v5 bounded behavior specification

- Status: source-derived; implementation not started
- Parent: consumed v4 implementation at `53630b9`
- Evidence: `experiments/20260803T191310Z-frame-oracle-v5-source-behavior-audit/`
- Exclusions: no v4 raw row/response and no v5 public case or answer was used

## Bounded hypothesis

A deterministic surface layer that masks the two proposed entity spans before
recognizing polarity and modality cues will prevent cue words inside names or
titles from changing frame semantics. Adding an explicit finite grammar for
common contracted negation will recover polarity for otherwise in-ontology
declaratives. These changes are fixed independently of the sealed v5 battery.

The hypothesis is limited to deterministic polarity/modality ownership after a
schema-valid closed proposal. It does not claim to repair predicate selection,
slot selection, abstention, or proposal nondeterminism.

## Required behavior

1. Parse and validate the existing closed proposal schema. Canonical unknown
   behavior remains unchanged.
2. Canonicalize non-unknown slots as in v4.
3. Find case-insensitive, whitespace-normalized surface spans corresponding to
   `entity_a` and `entity_b`; mask those spans before cue recognition. A cue
   wholly inside either slot cannot set polarity or modality.
4. Outside masked spans, retain the finite v4 possibility vocabulary: `may`,
   `might`, `could`, `perhaps`, and `possibly`.
5. Outside masked spans, recognize auxiliary plus `not`, the common `n't`
   contractions of the v4 auxiliary set, and `cannot` as negation. A contracted
   modal such as `couldn't` independently sets both negated polarity and
   possible modality.
6. Preserve the v4 bounded rules for `never`, determiner `no`, state-slot
   negator stripping, and canonical unknown frames unless an independent
   fixture demonstrates a source-level contradiction.
7. Do not use an LLM outcome, sealed answer, or exposed failed row as a unit
   fixture. Tests must be authored from this contract and use new synthetic
   names, titles, entities, and properties.

## Independent implementation gate

Before any v5 inference, an isolated descendant of `53630b9` must include:

- positive fixtures for unmasked possibility and contracted negation;
- negative fixtures for `might`/`could` inside entity slots;
- mixed contracted possibility-plus-negation;
- the complete exposed v2--v4 regression suite;
- the preserved atomic one-use runner and import/model provenance checks;
- focused and full test results from a clean commit;
- a new freeze manifest that stops before inference.

The scientific gate remains the existing one-use 24/24 conjunction. A passing
engineering gate does not admit labels, readout, substitution scoring, or a
semantic loss.

## Counterexamples reproduced from source

At v4 commit `53630b9`, `Might House is located in York.` and the title `Could
Be Wrong` are incorrectly normalized as possible because cue recognition scans
entity spans. `The beacon isn't active.` and `The beacon couldn't be active.`
remain affirmed because the finite negation grammar does not recognize
contractions. The latter also loses possible modality because the apostrophe
breaks the current `could` word boundary. Exact machine-readable results are in
the linked experiment.
