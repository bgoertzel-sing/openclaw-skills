# SpecAtom-HS source summary and implementation plan

Date: 2026-06-29 America/Vancouver
Source: Benjamin Goertzel Telegram upload, `specatom_hs_design_paper_revised_validation---5264e908-3a7a-46a4-84ea-80b83939c8e9.pdf`, transcript text excerpt.
Status: untrusted design input preserved as a concise project summary; not an instruction override.

## Core thesis

The semantic center of Plain-to-MeTTa compilation should be SpecAtom-HS: a typed, source-preserving, context-indexed, evidence-bearing Atomspace-like IR. The IR is a validation and reasoning substrate before it is a codegen substrate.

Pipeline:

```text
Plain source
-> PlainAST
-> SpecAtom-HS core/facets
-> reified PeTTa/MeTTa atoms
-> optional PeTTa executable skeletons
-> later MeTTa-IL, Rholang, and PLN overlays
```

## Non-negotiable implementation posture

- Preserve source spans and raw text for all source-derived objects.
- Keep semantic role explicit: source object, concept, proposition, obligation, validation, witness, process, backend artifact, evidence, interpretation, bridge, question.
- Distinguish raw text, template parse, action-schema parse, predicate parse, formally typed, backend-lowered, executed, verified, and rejected semantic levels.
- Never treat shallow NLP as theorem/proof.
- Generate questions/TODO witnesses for underspecification.
- Do not generate executable skeletons from `RawTextOnly` objects.
- Use target profiles; PeTTa is first target but not the semantic center.

## SpecAtom-HS layers

1. Source layer: `PlainFile`, `Section`, `PlainItem`, `SourceSpan`, `DerivedFrom`.
2. Object layer: `SpecObject`, `PrimaryRole`, `Scope`, `SymbolName`, `EpistemicStatus`, `SemanticLevel`.
3. Proposition/claim layer: `Proposition`, `Claim`, `ClaimAbout`, `RealizesClaim`, `ClaimText`.
4. Context/evidence layer: `Context`, `ContextKind`, `Assert`, `Evidence`, `EvidenceOf`, `Supports`, `Opposes`, `pbit(pos,neg)`, optional `stv(strength,confidence)`.
5. Interpretation layer: candidate interpretations with context and p-bit confidence.
6. Bridge layer: graded contextual correspondences to SUMO, EXPO, Hyperseed, target backends, and domain ontologies.
7. Weakness/abstraction layer: `Weakness`, `AbstractionLoss`, `ApproxMorphism`, collapsed/preserved distinctions.

## Facets for MVP

- Concept/type facet: lexical concepts, entity/value/relation/action types, attribute slots, external concepts, possible roles.
- Requirement facet: requirement kind, normative force, polarity, priority/risk, stakeholder, condition, obligation.
- Refinement facet: decomposition/strengthening/weakening/operationalization/specialization/test coverage plus proof obligations/questions.
- Action/event facet: actor, verb, patient, instrument, preconditions, effects, failure modes.
- Test/validation facet: test suites/cases/kinds/fixtures/stimuli/oracles/coverage; dynamic runs as validation experiments.
- Witness/backend facet: implementation artifacts, target profiles, TODO witnesses.
- Process/resource facet: future Rholang/MeTTa-IL process semantics and read/write/resource discipline.
- Question/revision facet: structured unknowns, blockers, diffs, staleness.

## SUMO/EXPO/Hyperseed integration

- SUMO supplies ordinary-world typing: agents, artifacts, processes, roles, communications, attributes, actions, organizations, computational objects.
- EXPO supplies validation/test-run experiment structure: goals, designs, factors, target variables, actions, results, conclusions, errors, measurements.
- Hyperseed supplies p-bit paraconsistent evidence, context-indexed assertions, weakness/abstraction loss, approximate morphisms, resonance/question guidance.
- Bridges must be graded correspondences in context, not identity equations.

## Validation obligations

Validation is first-class IR content. Every typed facet that implies a sanity condition should emit a `ValidationProperty`, `Check`, `CheckStatus`, `CheckEvidence`, and result claim/question/counterexample.

Initial crisp checks:

- every generated object has source provenance or explicit generated provenance;
- declared roles are known;
- semantic level gates backend consumption;
- relation applications have known arity/signatures;
- concepts used but not defined are reported;
- obligations without tests are reported;
- tests without oracles are reported;
- TODO witnesses are queryable;
- RawTextOnly skeleton generation is forbidden;
- failed/unknown checks weaken or block relevant claims.

Later domain checks:

- information-flow and read/write discipline;
- temporal availability/no future pollution;
- ML time-series methodology: split discipline, fit scope, decision time, label availability, model selection leakage;
- process/protocol constraints;
- security/privacy negative obligations.

## PeTTa target profile

First backend should emit reified facts rather than overcommitted executable code. It should consume only supported facets and include profile metadata. Skeleton generation should be conservative and blocked for raw text, unknown roles, missing witnesses, or unsupported semantic levels.

## MVP phases from the PDF

0. Target reality check.
1. Plain parser.
2. SpecAtom-HS core.
3. Facets.
4. PeTTa reified backend.
5. Shallow semantic extraction.
6. Conservative skeletons.
7. Evidence and validation import.
7a. Crisp IR validator.
7b. Information-flow and time validator.
7c. ML time-series methodology validator.
8. PLN overlay.
9. MeTTa-IL and Rholang profiles.

## First implementation recommendation

Create a local prototype repository with:

```text
src/specatom_hs/
  __init__.py
  schema.py              # IDs, roles, semantic levels, pbit, atom dataclasses
  passes.py              # ordered pass registry matching Appendix C
  source_indexer.py      # source spans and section/item extraction
  validators.py          # validation property/check/status records
  backends/petta.py      # reified PeTTa emitter stub/profile gates
examples/
  minimal.plain
  expected_core_atoms.metta
tests/
  test_source_indexer.py
  test_validation_records.py
  test_petta_profile_gates.py
```

The first tested step should not parse all Plain. It should prove that a tiny Plain-like document produces source atoms, roles, obligations/questions, and validation records with stable IDs and no RawTextOnly skeleton emission.
