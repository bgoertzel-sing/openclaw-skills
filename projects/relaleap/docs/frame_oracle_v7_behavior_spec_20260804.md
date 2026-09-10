# Frame-oracle v7 proposal-ingestion behavior spec

- Date frozen: `2026-08-04`
- Source baseline: clean `agent/frame-oracle-v6-freeze` commit
  `56b9eb989b8561c46827d64eb985cd5f7ec210d4`
- Source audit:
  `experiments/20260804T111528Z-frame-oracle-v7-source-contract-audit-r3/`
- Scientific gate: `sealed/frame-oracle-v7/`, still unopened

## Question

Can the normalizer conservatively handle a proposal whose fields satisfy the
generation JSON schema but whose `predicate` and `abstain` values disagree,
without weakening the strict canonical `ClosedFrame` contract?

## Reproduced source defect

The generation schema constrains field names, types, enums, and confidence but
does not express the cross-field equivalence
`abstain == (predicate == "unknown")`. `normalize_proposal_v6` first calls
strict `ClosedFrame.from_json`, which enforces that equivalence and raises.
Consequently, the later branch intended to canonicalize `predicate ==
"unknown" or abstain` is unreachable for either inconsistent direction.

Four source-only fixtures establish the boundary:

- non-unknown predicate plus `abstain=true`: schema-shaped, raises;
- `predicate=unknown` plus `abstain=false`: schema-shaped, raises;
- canonical unknown: returns canonical empty/unknown fields;
- canonical non-unknown: continues through ordinary normalization.

No opened v6 material or sealed v7 case/answer was used.

## Frozen bounded behavior

V7 must add a proposal-only ingestion step before constructing a strict
`ClosedFrame`:

1. Require exactly the existing seven keys.
2. Preserve the existing categorical vocabularies, string and boolean type
   checks, and finite confidence range check.
3. Do not weaken or modify `ClosedFrame.from_json`; it remains the strict
   canonical-frame and committed-answer validator.
4. At proposal ingestion only, if `predicate == "unknown"` **or**
   `abstain is true`, return the canonical unknown frame with empty slots,
   unknown polarity/modality, `abstain=true`, and the proposed confidence.
5. Otherwise require a non-unknown predicate with `abstain=false` and continue
   through the unchanged v6 slot, polarity, modality, and confidence behavior.

This is a fail-closed union rule: disagreement becomes abstention, never a
positive semantic label.

## Explicit non-changes

- Do not change the oracle prompt, generation schema, ontology, cue
  vocabularies, slot masking, canonicalization, decode settings, or semantic
  key.
- Do not add schema conditionals whose support by the local structured-output
  endpoint has not been independently established.
- Do not repair proposal selection, entity extraction, paired nondeterminism,
  or any opened v4--v6 outcome.
- Do not read v7 answers or invoke the oracle while implementing this behavior.

## Required independent fixtures

- Both inconsistent predicate/abstention directions canonicalize to unknown.
- Canonical unknown and canonical non-unknown controls are unchanged.
- Missing/extra fields, unknown categorical values, wrong field types, and
  invalid confidence still raise.
- Direct strict `ClosedFrame.from_json` calls still reject both inconsistent
  directions.
- All exposed frame and atomic-runner regressions and the full suite pass.

## Successor boundary

Implement only this contract on a fresh isolated descendant branch such as
`agent/frame-oracle-v7`, using independent fixtures. Stop after focused,
exposed, and full tests from a clean commit. Runner adaptation, provenance
freeze, inference, answer access, readout training, substitution evaluation,
and semantic-loss integration remain separate later gates.
