# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-06-29 implementation notes

Read `/home/openclaw/tmp/omegaclaw-telegram-attachments/1782780878-file_3.pdf.extracted.txt`, especially appendices A-H, J-N, and O. The existing `specatom-hs` project already tracked this lane, so implementation continued there instead of keeping a duplicate `plain-metta-specatom` notebook.

Concrete repo work in `repos/specatom-hs`:

- `src/plain_to_metta/parser.py`: source indexing and Plain-like section/bullet parser with spans.
- `src/plain_to_metta/compiler.py`: source atoms, concept extraction, shallow requirements/obligations/action templates/tests, Appendix O normalization-scope Unknown, questions, and crisp validator checks.
- `src/plain_to_metta/emit.py`: JSON and MeTTa-ish S-expression emitters.
- `examples/task_manager.plain`: compact Appendix G fixture.
- `examples/ml_timeseries.plain`: compact Appendix O fixture.
- `tests/`: unit tests for source preservation, role uniqueness, questions, validators, and ML Unknown.

Commands run:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m plain_to_metta.cli examples/task_manager.plain --out out/task_manager
PYTHONPATH=src python3 -m plain_to_metta.cli examples/ml_timeseries.plain --out out/ml_timeseries
```

Final result: 5 tests passed. Example generation produced 159 facts for task manager and 190 facts for ML time-series, with zero Fail diagnostics. Generated `out/` files are ignored/local and reproducible.

## 2026-06-30 concept-table scaffold

Concrete repo work in `repos/specatom-hs`:

- Added `specatom_hs.passes.build_concept_table`, a conservative explicit-syntax pass that recognizes local `:Concept:` definitions/references and `[external:Ontology.Term]` links.
- The pass emits first-class `ConceptObject` records at `TemplateParsed` level, `ConceptStatus` facts (`defined`, `external`, `unresolved`), `concept-reference-resolved` validation obligations/checks, and `QuestionObject` records for unresolved concepts instead of inventing meanings.
- Added focused unit tests in `tests/test_specatom_concepts.py` covering defined/external/unresolved concept status, Unknown unresolved-reference checks, and TemplateParsed concept objects.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Result: 14 tests passed.

## 2026-06-30 concept-reference occurrence spans

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_concept_table` so explicit concept markers now create first-class `ConceptReferenceObject` records at `TemplateParsed` level for definition, reference, and external occurrences.
- Each occurrence gets a dedicated exact `SourceSpan` over the marker text (for example `:User:` rather than the whole bullet), `ConceptReference`, `ConceptReferenceKind`, `SourceItem`, and `RefersToConcept` facts when a concept table entry exists.
- `concept-reference-resolved` validation obligations/checks now target occurrence IDs, preserving Unknown checks for unresolved concepts.
- Added focused regression coverage for occurrence kinds, exact source-span slicing, and unresolved-reference check targets.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 15 tests passed. `git diff --check` produced no whitespace errors; note the local implementation repo still has no initial commit, so normal `git diff` only sees staged/tracked changes.

## 2026-06-30 source-indexer continuation support

Concrete repo work in `repos/specatom-hs`:

- Reworked `specatom_hs.source_indexer.index_source` to consume indented non-bullet continuation lines into the preceding Plain item.
- Continuation support extends the item `SourceSpan` through the last continuation line and preserves the combined `raw_text` with newline separators.
- Explicit nested bullets, including acceptance-test style child bullets, remain separate `PlainItem` records with `parent_item_id` links instead of being swallowed as continuation text.
- Added regression coverage in `tests/test_specatom_source_indexer.py` for multi-line rule text plus a nested acceptance-test bullet.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 16 tests passed; `git diff --check` produced no whitespace errors.

## 2026-06-30 concept grammar aliases

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_concept_table` beyond the original explicit `:Concept:` syntax while staying conservative.
- Added support for bracket aliases `[def:Name]`, `[ref:Name]`, and `[concept:Name]`; `[concept:Name]` is treated as a definition only in definition-like sections (`definitions`, `concepts`, `glossary`) and as a reference elsewhere.
- Added support for bare glossary/definition bullets such as `Task: tracked work.` and `Concept Task: ...` as local concept definitions, limited to definition-like sections.
- Replaced the earlier fixed `- ` source-span offset assumption with raw-text-to-source alignment so concept occurrence spans remain exact for indented items and continuation-normalized raw text.
- Tightened colon marker matching so alias syntax like `[ref:Task]` is not misread as an unresolved `:Task] ... [concept:` colon reference.
- Added regression coverage for alias definitions/references, exact spans over `[ref:Task]`/`[def:Tag]`, and no Unknown check when aliases resolve.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 17 tests passed; `git diff --check` produced no whitespace errors. The implementation repo remains local-only with no initial commit, so `git status --short` continues to show expected untracked scaffold files.

## 2026-06-30 requirement/test coverage and PeTTa fact export

Concrete repo work in `repos/specatom-hs`:

- Added `specatom_hs.passes.build_requirement_test_coverage`, a structural pass for `requirements`, `functional specifications`, and `implementation requirements` sections.
- The pass emits conservative `RequirementObject` records, `ValidationObject` acceptance-test records, `Covers` atoms when a test is nested under or follows a requirement, and `requirement-has-acceptance-test` validation obligations.
- Requirements with explicit acceptance tests receive `Pass` coverage checks; uncovered requirements receive `Unknown` checks plus `QuestionObject` records (`MissingAcceptanceTest`) rather than silent success.
- Extended `specatom_hs.backends.petta.emit_reified_atoms` so the `petta_reified_v0` profile exports supported object facts, validation obligations, and check records while still refusing RawTextOnly object emission.
- Added regression tests in `tests/test_specatom_requirement_coverage.py` that compare emitted coverage atoms to expected ground-truth atoms and verify Unknown-to-question behavior.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 19 tests passed; `git diff --check` produced no whitespace errors. The implementation repo remains local-only with no initial commit, so `git status --short` continues to show expected untracked scaffold files.

## 2026-07-01 fact arity and declared-reference validator slice

Concrete repo work in `repos/specatom-hs`:

- Added a small `FACT_SCHEMAS` table in `specatom_hs.validators` for currently supported object-fact predicates (`SourceItem`, `RefersToConcept`, `Covers`, `MissingAcceptanceTest`, `Blocks`, etc.).
- `validate_document` now emits `fact-has-supported-arity` obligations/checks for object facts. Known predicates with malformed arity fail crisply; predicates outside the scaffold schema remain Unknown rather than being silently accepted or rejected.
- Added `fact-references-known-targets` checks for declared object/item/validation-obligation references, catching dangling targets such as a `Covers` atom pointing to a missing requirement object.
- Added regression tests covering passing supported facts from the normal requirement/test pipeline plus synthetic malformed arity and dangling-reference failures.
- Updated the local README supported-feature list to mention scaffold arity/reference validation.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 21 tests passed; `git diff --check` produced no whitespace errors. The implementation repo remains local-only with no initial commit, so `git status --short` continues to show expected untracked scaffold files.

## 2026-07-01 PeTTa profile-filtered reified export

Concrete repo work in `repos/specatom-hs`:

- Tightened `specatom_hs.backends.petta.emit_reified_atoms` so object facts are exported only when their predicate is in the current scaffold `FACT_SCHEMAS` profile and their arity matches the schema.
- Unsupported object-fact predicates and malformed supported facts now produce `BackendRefusal` records instead of silently entering the `petta_reified_v0` atom stream.
- Extended reified validation export with `validation-rationale`, `check-obligation`, and `check-evidence` atoms, preserving the reason/evidence side of validation records for downstream comparison and review.
- Added regression tests for supported fact export, unknown-predicate refusal, malformed-arity refusal, and validation rationale/evidence preservation.
- Updated the local README supported-feature list.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 23 tests passed; `git diff --check` produced no whitespace errors. The implementation repo remains local-only with no initial commit, so normal tracked diffs are limited until the scaffold is committed.

## 2026-07-01 unsupported fact predicate questions

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators._validate_object_facts` so an object fact with no scaffold schema still gets the existing `fact-has-supported-arity` Unknown check, but now also creates an explicit `QuestionObject`.
- The question object carries `UnsupportedFactPredicate`, `QuestionText`, and `Blocks` facts pointing back to the relevant fact-profile obligation, making unsupported profile gaps inspectable by backends/reviewers instead of only appearing in check evidence text.
- Added `UnsupportedFactPredicate` to the current scaffold fact schema so the question itself can be profile-validated/exported safely in later passes.
- Added regression coverage for a synthetic `InventedExecutable` fact that must produce an Unknown check plus a blocking profile question.
- Updated README and project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 24 tests passed; `git diff --check` produced no whitespace errors.

## 2026-07-01 validation-layer self-checks

Concrete repo work in `repos/specatom-hs`:

- Added `_validate_check_records` to `specatom_hs.validators`, taking a snapshot of existing check records and validating the validation layer without recursively judging newly generated meta-checks.
- The validator now emits `check-links-known-obligation` checks so malformed diagnostics that cite a missing validation obligation fail crisply.
- It also emits `check-target-matches-obligation` checks so a `CheckRecord` must preserve the property and target declared by the cited obligation.
- Added regression coverage with one good synthetic check, one wrong-target check, and one missing-obligation check.
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 25 tests passed; `git diff --check` produced no whitespace errors.

## 2026-07-01 PeTTa source provenance manifest

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.backends.petta.emit_reified_atoms` to include a profile-stable source provenance manifest before object emission: `plain-file`, `source-span`, `section`, `plain-item`, and `derived-from` atoms.
- Kept this as reified/provenance-only export, not executable lowering, and left RawTextOnly object refusal behavior unchanged.
- Added a ground-truth regression test that compares the generated manifest atoms for a small Plain fixture against the indexed file/section/item/span records.
- Updated README supported-feature wording.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 26 tests passed; `git diff --check` produced no whitespace errors. Implementation commit `c8e1e5e` (`Emit PeTTa source provenance manifest`) was pushed to private backup remote `origin/main`.

## 2026-07-01 concept occurrence continuation line spans

Concrete repo work in `repos/specatom-hs`:

- Tightened `specatom_hs.passes.build_concept_table` source-span creation for concept occurrence atoms so exact marker spans compute their own start/end line numbers from byte offsets instead of inheriting the whole parent bullet item's line range.
- This specifically fixes references on multi-line bullet continuation lines: the byte slice was already exact, and now the line span is exact too.
- Added regression coverage for a `[ref:Task]` marker on a continuation line, asserting the exported `SourceSpan` slice and start/end line are both exact.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 27 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `955b636` (`Fix concept occurrence line spans`).

## 2026-07-01 validation-obligation provenance self-checks

Concrete repo work in `repos/specatom-hs`:

- Added `_validate_validation_obligations` in `specatom_hs.validators`, using a snapshot of existing obligations to avoid recursive validation growth.
- The validator now emits `obligation-has-source-provenance` checks: Pass for known source spans, Fail for dangling span IDs, and Unknown when an obligation is generated without a direct source slice.
- It also emits `obligation-target-is-declared` checks for document entities, check IDs, obligation IDs, and supported object-scoped subtargets such as `object:fact:...` and concept-reference targets.
- Added regression coverage for normal compiled obligations plus a synthetic malformed obligation with both a missing source span and undeclared target.
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 28 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `c6e9eb9` (`Validate obligation provenance`).

## 2026-07-01 PeTTa reified semantic-level validation

Concrete repo work in `repos/specatom-hs`:

- Added explicit `object-supported-by-petta-reified-profile` validation obligations for each `SpecObject`, aligning validator output with the `petta_reified_v0` backend semantic-level gate.
- Supported reified levels receive Pass checks; unsupported levels such as `RawTextOnly` receive Unknown checks rather than being silently deferred to backend refusal only.
- Unsupported semantic levels now create blocking `QuestionObject` records with `UnsupportedSemanticLevel`, `QuestionText`, and `Blocks` facts, making profile-lifting/refusal decisions visible to reviewers and downstream PeTTa exports.
- Added `UnsupportedSemanticLevel` to the scaffold fact schema and regression coverage for one RawTextOnly object plus one TemplateParsed object.
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Result: 29 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `36be192` (`Validate PeTTa reified profile levels`).

## 2026-07-01 explicit requirement coverage labels

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_requirement_test_coverage` with conservative requirement labels (`[id:REQ]`, `[req:REQ]`, `[requirement-id:REQ]`) and explicit acceptance-test coverage claims (`[covers:REQ]`, `[covers-requirement:REQ]`).
- Requirements now emit `RequirementLabel` facts and acceptance tests emit `CoverageClaim` facts in addition to `Covers` when the label resolves, preventing a labelled test from being attached only by proximity to the most recent requirement.
- Unresolved explicit coverage labels now create `coverage-claim-target-resolved` Unknown checks plus `QuestionObject` records with `MissingCoverageTarget` and `Blocks`, instead of silently falling back to an unrelated requirement.
- Added `RequirementLabel`, `CoverageClaim`, and `MissingCoverageTarget` to the scaffold fact schema so the validator and PeTTa reified profile can check/export them safely.
- Added regression tests for label-resolved coverage atom ground truth and unresolved-label question behavior.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 31 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `07cf235` (`Add explicit coverage labels`).

## 2026-07-01 duplicate requirement-label ambiguity handling

Concrete repo work in `repos/specatom-hs`:

- Tightened `specatom_hs.passes.build_requirement_test_coverage` so explicit coverage labels now resolve only when exactly one requirement declares the label.
- Duplicate requirement labels now emit `requirement-label-is-unique` Unknown checks and `QuestionObject` records with `DuplicateRequirementLabel` plus `Blocks` facts.
- Acceptance tests with `[covers:...]` pointing at a duplicate label no longer fall back to proximity or choose the first requirement; they emit `coverage-claim-target-resolved` Unknown checks and `AmbiguousCoverageTarget` questions.
- Added `AmbiguousCoverageTarget` and `DuplicateRequirementLabel` to the scaffold fact schema so those questions can be validated/exported safely.
- Added regression coverage for the duplicate-label refusal path and updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 32 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `f40688c` (`Handle duplicate coverage labels`).

## 2026-07-01 orphan acceptance-test coverage questions

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_requirement_test_coverage` with per-test `acceptance-test-covers-requirement` obligations, separate from per-requirement coverage checks.
- Acceptance tests linked by nesting, proximity, or explicit `[covers:...]` labels now get Pass checks; acceptance tests with no requirement target produce Unknown checks plus `QuestionObject` records carrying `OrphanAcceptanceTest`, `QuestionText`, and `Blocks` facts.
- Added `OrphanAcceptanceTest` to the scaffold fact schema so `petta_reified_v0` can export orphan-test questions safely instead of treating them as unsupported predicates.
- Added regression coverage comparing the generated `OrphanAcceptanceTest` atom to the expected test/question IDs.
- Updated README and project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 33 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `f4f5804` (`Flag orphan acceptance tests`).

## 2026-07-01 object-fact subject/profile validation

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators.FactSchema` with an optional `subject_pos`, defaulting to the first fact argument after the predicate for object-scoped facts.
- `validate_document` now emits `fact-subject-matches-object` obligations/checks after arity validation, failing facts such as `(RequirementText other-object ...)` attached to a different owning `SpecObject`. Predicate-scoped facts such as `ConceptStatus` are explicitly exempt.
- Tightened `specatom_hs.backends.petta.emit_reified_atoms` so `petta_reified_v0` refuses wrong-subject object facts instead of exporting atoms whose subject and owner disagree.
- Added regression coverage for validator Fail diagnostics and backend `fact-subject-mismatch` refusals.
- Updated README and project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 33 tests passed; `git diff --check` produced no whitespace errors. Committed and pushed private backup `390554a` (`Validate object fact subjects`).

## 2026-07-02 validation check-status self-check

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators._validate_check_records` with `check-status-is-known` obligations/checks over the original check-record snapshot.
- Valid `CheckStatus` enum values pass; malformed/non-declared statuses now fail crisply as first-class validation diagnostics instead of being silently exported or crashing later.
- Made `specatom_hs.backends.petta.emit_reified_atoms` preserve malformed check status text safely when exporting diagnostic atoms, so bad validation records remain inspectable.
- Added regression coverage in `tests/test_specatom_validation_records.py` for a synthetic malformed status (`Definitely`).
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_validation_records -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused validation tests passed (8 tests), full suite passed (34 tests), and `git diff --check` produced no whitespace errors. Committed locally as `c40eb04` (`Validate check record statuses`); not pushed.

## 2026-07-02 document-scoped coverage labels

Concrete repo work in `repos/specatom-hs`:

- Adjusted `specatom_hs.passes.build_requirement_test_coverage` to pre-scan requirement labels before resolving explicit `[covers:...]` acceptance-test claims.
- This makes coverage labels document-scoped, so acceptance-test sections can appear before requirement sections without producing false `MissingCoverageTarget` Unknown diagnostics.
- Added regression coverage for a forward reference where `[covers:R1]` appears before `[id:R1]`, asserting the generated `Covers` fact and Pass coverage check.
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_requirement_coverage -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused requirement coverage tests passed (7 tests), full suite passed (34 tests), and `git diff --check` produced no whitespace errors. Committed locally as `3fd59a8` (`Resolve forward coverage labels`); not pushed.

## 2026-07-02 validation check-evidence self-check

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators._validate_check_records` with `check-has-evidence` obligations/checks over the original check-record snapshot.
- Non-empty check evidence now passes; blank/whitespace-only evidence now fails crisply as malformed diagnostics before backend export.
- Added regression coverage in `tests/test_specatom_validation_records.py` for one passing evidence record and one whitespace-only failing evidence record.
- Updated README/project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_validation_records -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused validation tests passed (8 tests), full suite passed (34 tests), and `git diff --check` produced no whitespace errors. Committed locally as `0aef25d` (`Validate check evidence`); not pushed.

## 2026-07-02 source-span byte/line validation

Concrete repo work in `repos/specatom-hs`:

- Added source-span self-validation to `specatom_hs.validators`: every `SourceSpan` now gets `source-span-within-file-bounds` and `source-span-lines-match-byte-offsets` obligations/checks.
- The validator fails missing file IDs, out-of-file/non-empty byte-range violations, and line numbers that do not match the span byte offsets, making source-index corruption visible before backend export.
- Added regression coverage for normal compiled spans plus synthetic out-of-bounds, bad-line, and missing-file spans.
- Updated the local README supported-feature list.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_validation_records -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused validation tests passed (9 tests), full suite passed (35 tests), and `git diff --check` produced no whitespace errors.

Implementation commit: local `2d8e93b` (`Validate source span bounds`); not pushed.

## 2026-07-02 Plain file digest validation

Concrete repo work in `repos/specatom-hs`:

- Added Plain file manifest self-validation in `specatom_hs.validators`: each `PlainFile` now gets a `plain-file-digest-matches-content` obligation/check that recomputes SHA-256 from the preserved UTF-8 source text.
- Malformed/corrupted file manifest digests now fail crisply before reviewers trust source spans or PeTTa source-provenance export.
- Added regression coverage for both normal compiled source manifests and a synthetic bad digest, and updated README supported-feature wording.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_validation_records -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused validation tests passed (10 tests), full suite passed (36 tests), and `git diff --check` produced no whitespace errors.

Implementation commit: local `f90f8c9` (`Validate plain file digests`); not pushed.

## 2026-07-02 section/item PlainFile link validation

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators.validate_document` with source-index provenance checks for sections and items.
- New obligations/checks: `section-file-is-indexed`, `section-has-source-span`, and `item-file-is-indexed`.
- Malformed section/item records with missing `file_id` links now fail crisply before PeTTa source-provenance manifest export review, complementing the existing digest and source-span byte/line checks.
- Updated README and regression coverage in `tests/test_specatom_validation_records.py`.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 37 tests passed; `git diff --check` produced no whitespace errors. Local commit `f95fd87` (`Validate section and item file links`); not pushed.

## 2026-07-02 source-index file-consistency validation

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.validators.validate_document` with file-ID consistency checks across indexed source records: `section-span-file-matches-section-file`, `item-file-matches-section-file`, and `item-span-file-matches-item-file`.
- These checks catch malformed/cross-file-corrupted provenance where a section or item names one PlainFile while its span or containing section names another, rather than relying only on existence checks.
- Extended `tests/test_specatom_validation_records.py` to verify Pass checks on compiled source plus Fail diagnostics for mismatched section/span, item/span, and item/section file IDs.
- Updated README supported-feature notes.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 37 tests passed; `git diff --check` produced no whitespace errors.

## 2026-07-02 CLI/demo diagnostics and auth-service fixture

Concrete repo work in `repos/specatom-hs`:

- Added a stdlib CLI module (`specatom_hs.cli`) that can emit SpecAtom-HS JSON, grouped PeTTa/MeTTa reified atoms, and a Markdown diagnostics report to stdout or sidecar files.
- Added `specatom_hs.backends.diagnostics` for compact diagnostics summaries and human-readable reports with Pass/Fail/Unknown counts, per-property breakdowns, questions, and backend refusals.
- Added grouped PeTTa output helpers so `.metta` review artifacts are separated into source, section/item provenance, object facts, validation records, and refusals without changing the underlying backend semantics.
- Added `examples/auth_service.plain` and `scripts/demo.sh`. The auth-service fixture intentionally exercises duplicate requirement labels (`AUTH-2`), an unresolved explicit coverage label (`AUTH-99`), an unresolved concept (`AuditSink`), orphan/coverage questions, and backend skeleton refusals.
- Optimized `add_validation_obligation` and `add_check` de-duplication to compare stable record IDs instead of whole dataclasses; this made the larger review fixture practical in the unit suite and cut full-suite runtime after adding CLI/diagnostics coverage.
- Added regression coverage in `tests/test_cli.py` and `tests/test_diagnostics.py` for grouped `.metta`, Markdown diagnostics, output sidecars, and the auth-service question/refusal path.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_cli tests.test_diagnostics -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused CLI/diagnostics tests passed (9 tests), full suite passed (46 tests), and `git diff --check` produced no whitespace errors. No paid compute, remote push, merge, force-push, secrets/access/security changes, or external messaging.

## 2026-07-02 question-object blocker validation

Concrete repo work in `repos/specatom-hs`:

- Tightened unresolved-concept question records so each now carries a `Blocks` fact pointing at the specific `concept-reference-resolved` validation obligation that remains Unknown.
- Added question-object self-validation in `specatom_hs.validators`: every `QuestionObject` must have non-empty `QuestionText`, and every question must block at least one known validation obligation.
- Added regression coverage for valid unresolved-concept questions and malformed question records with empty text, missing blockers, or dangling blocker IDs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 47 tests passed; `git diff --check` produced no whitespace errors. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access changes during that slice; the changes were later included in private backup commit `718a8c8`.

## 2026-07-02 ML/time-series methodology validator slice

Concrete repo work in `repos/specatom-hs`:

- Added `specatom_hs.passes.build_ml_methodology_validation`, a conservative v0.2 methodology pass that activates only on explicit ML/time-series-ish terms and does not infer model semantics.
- The pass emits a `MLTimeSeriesExperiment` validation object plus obligations/checks for `ml-evaluation-metric-declared`, `ml-horizon-or-frequency-declared`, `ml-reproducibility-evidence-declared`, and `ml-preprocessing-fit-scope-declared`.
- Missing evidence becomes `Unknown` checks plus `QuestionObject` records with `MissingMethodologyEvidence`, `QuestionText`, and `Blocks` facts, so methodology gaps are reviewable and PeTTa-profile exportable.
- Added scaffold fact schemas for `MLTimeSeriesExperiment`, `MethodologySignal`, and `MissingMethodologyEvidence`, and updated the validator gap audit to mark this as the first implemented v0.2 methodology slice.
- Added `tests/test_specatom_ml_methodology.py` covering the underspecified ML fixture and an explicit-pass case with RMSE, 24-hour horizon, seed/dataset snapshot, and train-only preprocessing fit scope.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (2 tests), full suite passed (49 tests), and `git diff --check` produced no whitespace errors. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access changes during that slice; the changes were later included in private backup commit `718a8c8`.

## 2026-07-02 ML/time-series baseline and uncertainty obligations

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with two additional conservative Appendix N/P methodology checks: `ml-baseline-comparison-declared` and `ml-uncertainty-reporting-declared`.
- Baseline evidence is keyword-level only (`baseline`, `benchmark`, `naive`, `persistence`, `last-value`, `ablation`, or `compared against`) and uncertainty evidence is likewise conservative (`confidence interval(s)`, `error bar(s)`, `uncertainty`, `standard deviation`, `bootstrap`, etc.); missing evidence remains `Unknown` with `MissingMethodologyEvidence` question objects rather than invented experiment design.
- Extended the existing methodology regression tests so the underspecified fixture produces Unknown checks/questions for these two new properties and the explicit-pass fixture includes a naive last-value baseline plus confidence intervals.
- Updated README and validator gap audit wording to reflect the expanded v0.2 methodology slice while leaving metric appropriateness and richer leakage semantics deferred.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (2 tests), full suite passed (49 tests), and `git diff --check` produced no whitespace errors. No paid compute, merge, force-push, remote-ref deletion, or secrets/access changes. Pushed private backup commit `718a8c8` (`Extend ML methodology checks`) to `origin/main` after checks passed.

## 2026-07-02 ML preprocessing-order leakage review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with an explicit `ml-preprocessing-order-reviewed` obligation.
- Specs matching normalize/scale/preprocess-before-split wording now get an `Unknown` check plus a `MissingMethodologyEvidence` `QuestionObject` blocking the exact obligation unless train-only preprocessing fit scope is also declared.
- Added regression coverage for a "standardize all rows and then split" fixture, verifying the Unknown check evidence and blocking question link.
- Updated README/project records. This remains conservative review scaffolding; it does not infer actual leakage or approve executable methodology.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 50 tests passed; `git diff --check` passed. Local/pushed backup commit: `2169f2c` (`Review preprocess-then-split leakage`).

## 2026-07-03 ML future/label leakage review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with an explicit `ml-future-label-leakage-reviewed` obligation.
- The new check is conservative and pattern-based: ML/time-series specs pass when no explicit future/label/target-as-feature/input wording is found, and produce `Unknown` plus a `MissingMethodologyEvidence` blocking `QuestionObject` when future values, labels, or targets appear in feature/input/predictor/covariate contexts.
- Added regression coverage for a fixture that says to use the future demand target label as model features, verifying the Unknown check and exact blocker link.
- Updated README/project records. This remains review scaffolding, not a claim to detect all temporal leakage or metric appropriateness issues.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (4 tests), full suite passed (51 tests), and `git diff --check` passed. Committed and pushed private backup `7a94c2a` (`Review future label leakage`) to `origin/main`. No paid compute, merge, force-push, remote-ref deletion, or secrets/access changes.

## 2026-07-03 ML metric/task appropriateness review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with `ml-metric-task-appropriateness-reviewed`, a conservative keyword-level review obligation for declared ML/time-series metrics.
- Forecast/regression-like specs that declare classification-style metrics such as accuracy/AUC/F1 without classification-task wording now produce an `Unknown` check plus a `MissingMethodologyEvidence` `QuestionObject` blocking the exact obligation, rather than treating a metric word as sufficient.
- Regression-style metrics (`MAE`, `MSE`, `RMSE`, `MAPE`) and classification metrics paired with explicit classification-task wording pass at the current scaffold level.
- Updated README and the validator gap audit to mark this as a first metric-appropriateness slice while leaving stronger target/task semantics deferred.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (5 tests), full suite passed (52 tests), and `git diff --check` passed. Local commit `9c93a29` (`Review named ML methodology details`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 ML temporal split-order review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with `ml-temporal-split-order-reviewed`, a conservative temporal-availability/methodology obligation for ML/time-series specs.
- Specs that explicitly say to randomly/shuffle/stratify/k-fold split time-series data now produce an `Unknown` check plus a `MissingMethodologyEvidence` blocking `QuestionObject` unless chronological, temporal, walk-forward, rolling-origin, backtest, or out-of-time split evidence is present.
- Added regression coverage for random split Unknown/question behavior and chronological split Pass behavior.
- Updated README and validator gap audit wording. This remains keyword-level review scaffolding, not a claim to prove temporal validity.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (7 tests), full suite passed (54 tests), and `git diff --check` passed. Local commit `2b8cf79` (`Review temporal split order`). Local commit `9c93a29` (`Review named ML methodology details`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 ML named baseline/uncertainty review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with two more conservative methodology obligations: `ml-baseline-comparator-named` and `ml-uncertainty-method-named`.
- Generic baseline/uncertainty mentions still satisfy the older declaration checks, but now produce `Unknown` checks plus `MissingMethodologyEvidence` blocking `QuestionObject`s unless a concrete comparator family (`naive`, `persistence`, `benchmark`, `ablation`, etc.) or uncertainty method (`confidence interval`, `error bars`, `bootstrap`, standard deviation/variance, etc.) is named.
- Added regression coverage for the generic-baseline/generic-uncertainty refusal path and updated README plus validator gap audit wording.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed (8 tests), full suite passed (55 tests), and `git diff --check` passed. Local commit `9c93a29` (`Review named ML methodology details`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 prediction-time feature availability review

Concrete repo work in `repos/specatom-hs`:

- Extended `specatom_hs.passes.build_ml_methodology_validation` with `ml-feature-availability-reviewed`, a conservative first information-flow/temporal-availability obligation for ML/time-series specs.
- Specs that explicitly mention features, inputs, predictors, or covariates now require availability evidence such as prediction-time availability, point-in-time/as-of wording, lagged/historical inputs, prior-to-prediction evidence, or equivalent no-future-data wording.
- Missing availability evidence becomes an `Unknown` check plus a `MissingMethodologyEvidence` question blocking the obligation; lagged historical features available at prediction time pass.
- Updated README and the validator gap audit to record the new v0.2 slice.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused methodology tests passed 10 tests; full suite passed 57 tests; `git diff --check` produced no whitespace errors. Local commit: `d37da2a` (`Review ML feature availability`).

## 2026-07-03 security/privacy obligation scaffolding

Concrete repo work in `repos/specatom-hs`:

- Added `specatom_hs.passes.build_security_privacy_validation`, a conservative keyword-level v0.2 pass that activates on security/privacy-sensitive wording without inferring a threat model or approving operational behavior.
- The pass emits a `SecurityPrivacyReview` validation object plus obligations/checks for `security-secrets-handling-reviewed`, `privacy-pii-handling-reviewed`, `security-access-boundary-declared`, and `security-destructive-action-safety-reviewed`.
- Missing evidence for secret storage/redaction/no-hardcoding, PII controls, access-control boundaries, or destructive-action safety mechanisms becomes `Unknown` checks plus `MissingSecurityPrivacyEvidence` `QuestionObject`s with exact `Blocks` links.
- Added scaffold fact schemas so the new review and question atoms validate/export through `petta_reified_v0` instead of becoming unsupported-predicate refusals.
- Added regression coverage in `tests/test_specatom_security_privacy.py` for both underspecified specs and explicit controls; updated README and validator gap audit.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (2 tests), full suite passed (59 tests), and `git diff --check` produced no whitespace errors. Local commit `0c18f8a` (`Add security privacy validation slice`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.


## 2026-07-03 secret log-exposure security/privacy review

Concrete repo work in `repos/specatom-hs`:

- Deepened the conservative security/privacy pass with `security-secret-log-exposure-reviewed`, activated by the same secret/token/password/credential signal as the existing secret-handling check.
- Added `SECRET_LOGGING_RE` evidence detection for redacted/masked/not-logged/no-log/scrubbed-from-logs wording.
- Specs mentioning secrets without log-exposure evidence now produce `Unknown` checks plus `MissingSecurityPrivacyEvidence` blocking questions; explicit redaction-from-logs evidence passes.
- Extended the existing security/privacy regression tests and README supported-feature list.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (2 tests), full suite passed (59 tests), and `git diff --check` produced no whitespace errors. Local commit `bba955c` (`Review secret log exposure`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 privacy data-classification review

Concrete repo work in `repos/specatom-hs`:

- Deepened the conservative security/privacy pass with `privacy-data-classification-declared`, activated by PII/personal-data signals.
- Added keyword-level data/sensitivity classification evidence detection (`data classification`, `classified as`, `sensitivity label`, `confidential`, `restricted`, `regulated data`, etc.).
- PII/personal-data specs without classification evidence now produce `Unknown` checks plus `MissingSecurityPrivacyEvidence` blocking questions; explicit classification wording passes.
- Extended security/privacy regression tests and updated README plus validator gap audit wording.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (2 tests), full suite passed (59 tests), and `git diff --check` produced no whitespace errors. Local commit `b88af86` (`Review privacy data classification`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 privilege-escalation review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `security-privilege-escalation-reviewed` for access/auth/admin/role specs.
- The pass now treats least privilege, admin-only, approval, audit, separation of duties, and self-grant-prevention wording as review evidence; otherwise it emits an Unknown check plus a `MissingSecurityPrivacyEvidence` question blocking the new obligation.
- Updated the security/privacy regression tests and README supported-feature list.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 59 tests passed; `git diff --check` produced no whitespace errors. Local commit `20f0130` (`Review privilege escalation controls`). No paid compute or remote writes.

## 2026-07-03 PII retention/deletion security/privacy review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `privacy-retention-deletion-reviewed`, activated by PII/personal-data signals.
- Added keyword-level retention/deletion/minimization evidence detection for retention periods/policies, delete-on-request/deletion requests, right to erasure, expiry/purge rules, and data minimization.
- PII/personal-data specs that mention privacy controls such as consent/encryption but omit retention/deletion/minimization evidence now produce an `Unknown` check plus a `MissingSecurityPrivacyEvidence` question blocking the exact obligation.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists retention/deletion review alongside data classification and privilege-escalation review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (3 tests), full suite passed (60 tests), and `git diff --check` produced no whitespace errors. Local commit `4ce4876` (`Review PII retention deletion controls`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 PII data-residency/cross-border transfer review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `privacy-data-residency-reviewed`, activated only when PII/personal-data wording appears together with region, country, jurisdiction, residency, EU/GDPR/CCPA/HIPAA, international, or cross-border context.
- Added keyword-level residency/transfer policy evidence detection for data residency, regional/same-region storage, allowed/approved regions, jurisdiction policy, GDPR/CCPA/HIPAA, cross-border transfer review, SCCs, and related wording.
- PII specs that mention regional/jurisdictional context without residency/transfer evidence now produce an `Unknown` check plus a `MissingSecurityPrivacyEvidence` question blocking the exact obligation; explicit data-residency wording passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice includes data-residency/cross-border transfer review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (4 tests), full suite passed (61 tests), and `git diff --check` produced no whitespace errors. Local commit `b895eba` (`Review PII data residency policy`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-03 third-party PII sharing review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy validator with `privacy-third-party-sharing-reviewed`.
- The new check triggers only when PII/personal-data wording appears together with third-party/vendor/processor/partner/external-service/export/upload/share wording.
- Passing evidence is deliberately policy-level and reviewable (`DPA`, data-processing/processor agreement, vendor/third-party review, approved vendor, subprocessor list, purpose limitation, onward-transfer/contractual controls).
- Missing evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; the PeTTa profile exports the existing supported question/evidence atoms without adding new executable behavior.
- Added regression coverage for a vendor analytics sharing gap and updated the all-controls pass fixture.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 62 tests passed; `git diff --check` produced no whitespace errors; local commit `000ad5c` (`Review PII third-party sharing`).

## 2026-07-04 PII lawful-basis/consent review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy validator with `privacy-lawful-basis-reviewed`, activated by PII/personal-data signals.
- Added keyword-level lawful-basis evidence detection for consent, lawful/legal basis, contract basis/contractual necessity, legal obligation, legitimate interest, vital interest, and public task wording.
- PII/personal-data specs that include classification/retention/encryption but omit lawful-basis or consent evidence now produce an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; explicit consent/lawful-basis wording passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists lawful-basis/consent review alongside data classification, retention/deletion, residency, and third-party sharing review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (6 tests), full suite passed (63 tests), and `git diff --check` produced no whitespace errors. Local commit `77b1a21` (`Review PII lawful basis`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-04 PII purpose-limitation review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy validator with `privacy-purpose-limitation-reviewed`, activated by PII/personal-data signals.
- Added keyword-level purpose/use-limitation evidence detection for purpose limitation, specific/limited purpose, use limitation, only-used-for wording, no-secondary-use, compatible-use, and secondary-use review.
- PII/personal-data specs that include classification/lawful-basis/retention/encryption but omit purpose-limitation evidence now produce an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; explicit purpose-limitation wording passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists purpose-limitation review alongside lawful-basis, retention/deletion, residency, and third-party sharing review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (7 tests), full suite passed (64 tests), and `git diff --check` produced no whitespace errors. Local commit `05386c5` (`Review PII purpose limitation`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-04 PII data-subject rights review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy validator with `privacy-data-subject-rights-reviewed`, activated by PII/personal-data signals.
- Added keyword-level evidence detection for data-subject/privacy rights, DSAR/access requests, correction/rectification, portability, objection, and opt-out wording.
- PII/personal-data specs that include classification/lawful-basis/retention/purpose/encryption but omit rights-request evidence now produce an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; explicit privacy-rights access-request evidence passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists data-subject rights review alongside lawful-basis, retention/deletion, purpose-limitation, residency, and third-party sharing review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (8 tests), full suite passed (65 tests), and `git diff --check` produced no whitespace errors. No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.


## 2026-07-04 rights-request authentication review

Concrete repo work in `repos/specatom-hs`:

- Extended `build_security_privacy_validation` with `privacy-rights-request-authentication-reviewed`, triggered only when PII/personal-data wording appears with data-subject rights, access, deletion, erasure, portability, correction, opt-out, DSAR, or similar rights-request wording.
- The new conservative check requires identity-verification/authenticated-request/account-owner/authorized-data-subject evidence before rights workflows are trusted. Missing evidence remains `Unknown` and emits a blocking `MissingSecurityPrivacyEvidence` question.
- Added regression coverage for a rights-request spec that lacks identity verification and for an explicit passing security/privacy fixture with identity-verification evidence.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (9 tests), full suite passed (66 tests), and `git diff --check` passed. No executable semantics or RawTextOnly export path was expanded.

## 2026-07-04 PII access audit/logging review

Concrete repo work in `repos/specatom-hs`:

- Extended `build_security_privacy_validation` with `privacy-pii-access-audit-reviewed`, triggered when PII/personal-data wording appears together with access/admin/role/auth wording.
- The new conservative check requires access logs, audit logs, audited access, access monitoring, or equivalent privacy access-log evidence before access-control privacy claims are trusted.
- Missing audit/logging/monitoring evidence remains `Unknown` and emits a blocking `MissingSecurityPrivacyEvidence` question; explicit access-audit-log evidence passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists PII access audit/logging review alongside rights-request authentication, residency, third-party sharing, access-boundary, and privilege-escalation review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (10 tests), full suite passed (67 tests), and `git diff --check` passed. Local commit `c11b7d1` (`Review PII access audit logging`). No executable semantics or RawTextOnly export path was expanded.

## 2026-07-04 PII incident-response/breach-notification review

Concrete repo work in `repos/specatom-hs`:

- Extended `build_security_privacy_validation` with `privacy-incident-response-reviewed`, activated by PII/personal-data signals.
- The new conservative check requires incident response, breach notification, regulator/affected-user notification, incident escalation, or equivalent runbook evidence before downstream privacy claims are trusted.
- Missing incident-response evidence remains `Unknown` and emits a blocking `MissingSecurityPrivacyEvidence` question; explicit breach-notification/incident-response wording passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice includes incident-response/breach-notification review.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (11 tests), full suite passed (68 tests), and `git diff --check` passed. Local commit `b7cd6d9` (`Review PII incident response`). No executable semantics or RawTextOnly export path was expanded.

## 2026-07-04 PII encryption-scope/key-management review

Concrete repo work in `repos/specatom-hs`:

- Extended `build_security_privacy_validation` with `privacy-encryption-scope-reviewed`, activated by PII/personal-data signals.
- The new conservative check no longer treats a generic `encryption` mention as enough for scoped protection evidence; it requires encryption-at-rest, transport encryption/TLS/HTTPS, database or field-level encryption, key-management/KMS, key rotation, or equivalent wording.
- Missing scoped encryption/key-management evidence remains `Unknown` and emits a blocking `MissingSecurityPrivacyEvidence` question; explicit at-rest/TLS/key-rotation evidence passes.
- Updated README and the validator gap audit so the v0.2 security/privacy slice lists encryption-scope/key-management review alongside data classification, lawful basis, retention/deletion, purpose limitation, rights, audit, incident response, residency, and third-party sharing.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (12 tests), full suite passed (69 tests), and `git diff --check` passed. Local commit `61f4145` (`Review PII encryption scope`). No executable semantics, RawTextOnly export path, paid compute, or remote write was expanded.

## 2026-07-04 authentication/session-management review

Concrete repo work in `repos/specatom-hs`:

- Extended `build_security_privacy_validation` with `security-session-management-reviewed`, triggered by auth/login/sign-in/session wording.
- The new conservative check requires MFA, session timeout/expiry, idle timeout, token expiry/expiration, refresh-token rotation, session revocation/logout, or reauthentication evidence before auth/session claims are trusted.
- Missing session-management evidence remains `Unknown` and emits a blocking `MissingSecurityPrivacyEvidence` question; explicit MFA/session-timeout/logout evidence passes.
- Updated README, validator gap audit, and project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (13 tests), full suite passed (70 tests), and `git diff --check` passed. No executable semantics, RawTextOnly export path, paid compute, or remote write was expanded.

## 2026-07-04 — real-time/current feature freshness review

Added `ml-feature-freshness-reviewed` to the conservative ML/time-series methodology slice in `repos/specatom-hs`. The check only becomes blocking when feature/input wording appears together with real-time/live/current/latest/recent/fresh signals; it requires freshness, staleness, latency, max/data age, update cadence, event-time, or as-of timestamp evidence. Missing evidence produces an `Unknown` check plus a blocking `MissingMethodologyEvidence` question; explicit as-of/max-age evidence passes. This advances the Appendix N/P temporal-availability lane without expanding executable semantics or RawTextOnly export.

Verification: `PYTHONPATH=src python3 -m unittest tests.test_specatom_ml_methodology -v` passed 12 tests; `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 72 tests; `git diff --check` passed.

## 2026-07-04 auth/API abuse-protection review

Concrete repo work in `repos/specatom-hs`:

- Added `security-auth-abuse-protection-reviewed` to the conservative security/privacy validator slice.
- The obligation triggers on auth/login/API/password/token wording and requires rate-limit, throttling, brute-force protection, account lockout, login-attempt limits, abuse/bot detection, or CAPTCHA evidence.
- Missing evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; explicit rate-limit/brute-force-lockout evidence passes.
- Updated README and security/privacy regression tests; local implementation commit: `991ef09` (`Review auth abuse protection`).

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (14 tests); full suite passed (73 tests); `git diff --check` produced no whitespace errors.

## 2026-07-04 - credential rotation/expiry/revocation security slice

Added a conservative `security-credential-rotation-reviewed` obligation in `projects/specatom-hs/repos/specatom-hs` for specs that mention secrets, tokens, passwords, or credentials. Missing rotation, expiry, or revocation wording now produces an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question instead of silently treating secret storage/log redaction as enough.

Implementation details:

- `src/specatom_hs/passes.py`: added `SECRET_ROTATION_RE` and a new `check_property(...)` call in `build_security_privacy_validation`.
- `tests/test_specatom_security_privacy.py`: added a regression where secret-manager plus log-redaction evidence still leaves credential lifecycle Unknown, and extended existing all-gaps/pass fixtures.
- `README.md` and `docs/validator-gap-audit.md`: documented the new obligation in the supported security/privacy slice.

Verification:

```bash
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Focused security/privacy tests passed (15 tests); full suite passed (74 tests); `git diff --check` produced no whitespace errors.

## 2026-07-04 authentication/API transport-protection review

Concrete repo work in `repos/specatom-hs`:

- Added `security-auth-transport-protection-reviewed` to the conservative security/privacy pass.
- Auth/login/API/password/token wording now requires TLS, HTTPS, mTLS, certificate-pinning, transport-encryption, or secure-channel evidence before the transport-protection check passes.
- Missing transport-protection evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question, exported through the existing PeTTa reified profile.
- Updated the security/privacy regression suite plus README and validator-gap audit docs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed 16 tests; full suite passed 75 tests; `git diff --check` passed. No executable semantics or RawTextOnly export path was expanded.

## 2026-07-05 API authorization/scope review

Concrete repo work in `repos/specatom-hs`:

- Added a conservative `security-api-authorization-reviewed` obligation to the security/privacy pass.
- The obligation triggers only when API/endpoint/webhook/route/request wording appears together with auth/access context, then requires authorization, permission/scope checks, scoped tokens, RBAC/access-control, deny-by-default, or policy-enforcement evidence.
- Missing evidence produces an Unknown check plus `MissingSecurityPrivacyEvidence` question with a `Blocks` link, matching the existing review/refusal style.
- Added regression coverage for an authenticated API endpoint that has MFA/rate limits/HTTPS but no authorization/scope evidence, and updated the explicit-controls pass case to include the new property.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (17 tests), full suite passed (76 tests), and `git diff --check` produced no whitespace errors. Local implementation commit: `e422ff8` (`Review API authorization scope`); not pushed.

## 2026-07-05 webhook/callback request-authenticity review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `security-webhook-request-authenticity-reviewed`, triggered by webhook, callback, incoming external request, or signed-request wording.
- The check requires request-authenticity/replay-protection evidence such as HMAC, signature verification, webhook secret, request signature, timestamp window/tolerance, nonce, idempotency key, or replay protection.
- Missing evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question, preserving the existing safe refusal/review style without generating executable handling code.
- Added regression coverage for a webhook callback over HTTPS that still lacks request signature/replay evidence, and extended the explicit-controls pass fixture.
- Updated README and validator-gap audit docs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (18 tests), full suite passed (77 tests), and `git diff --check` passed. Local implementation commit: `f6613be` (`Review webhook request authenticity`); not pushed. No paid compute, executable skeleton expansion, RawTextOnly export expansion, secrets/access changes, merge, force-push, or remote-ref deletion.

## 2026-07-05 API/webhook input-validation review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `security-api-input-validation-reviewed`, triggered when API/endpoint/route/request/webhook wording appears near input, payload, body, query, parameter, JSON, form, or upload wording.
- The new check requires reviewable evidence such as input validation, payload/schema/JSON/request-schema validation, parameter validation, sanitization, allow-listing, type checks, or bounds checks before inbound request data is treated as adequately constrained.
- Missing evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question; explicit schema/payload validation evidence passes in the all-controls fixture.
- Updated README and validator-gap audit docs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (19 tests), full suite passed (78 tests), and `git diff --check` passed. Local implementation commit: `e923faf` (`Review API input validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

## 2026-07-05 API/webhook error-disclosure review

Concrete repo work in `repos/specatom-hs`:

- Extended the conservative security/privacy pass with `security-api-error-disclosure-reviewed`, triggered when API/webhook specs mention errors, exceptions, stack traces, tracebacks, debug output, diagnostics, or error/failure responses.
- The check requires safe response evidence such as generic/redacted/sanitized/opaque errors, no stack traces/debug output, error codes, or correlation IDs before diagnostic response wording is treated as reviewed.
- Missing evidence becomes an `Unknown` check plus a blocking `MissingSecurityPrivacyEvidence` question, preserving the existing review/refusal style without adding executable error-handling semantics.
- Added regression coverage for an API endpoint exposing exception diagnostics and extended the explicit-controls fixture with sanitized generic API error responses and no stack traces.
- Updated README and validator-gap audit docs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_security_privacy -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused security/privacy tests passed (20 tests), full suite passed (79 tests), and `git diff --check` passed. Local implementation commit: `0446965` (`Review API error disclosure`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

## 2026-07-05 component-level data-path edge extraction

Concrete repo work in `repos/specatom-hs`:

- Added `DATA_PATH_EDGE_RE` regex to `specatom_hs.passes` that detects explicit component-level data-path patterns: "X reads from Y", "X writes to Y", "X sends to Y", "X consumes Z from Y", "X produces Z to Y", "X depends on Y".
- Added `_EDGE_STOP_WORDS` filter so conjunctions/articles/common prepositions are not treated as source or target component names.
- Added `_normalize_direction` helper that converts matched verb phrases to direction strings (e.g., "reads from" -> "reads-from", "consumes input from" -> "consumes-from").
- Extended `build_information_flow_validation` to extract edges from each candidate item, emit `DataFlowEdge` atoms as `SpecObject` records with `TEMPLATE_PARSED` semantic level, and add an `information-flow-data-path-declared` validation obligation: Pass when at least one explicit edge is found, Unknown when only vague data-flow/dependency wording exists.
- Added `DataFlowEdge` to `FACT_SCHEMAS` in `specatom_hs.validators` with arity 5 and no subject_pos (it is not an object-scoped fact).
- Added regression tests in `tests/test_specatom_information_flow.py` for edge extraction ground truth, pass/unknown data-path check behavior, PeTTa export of `DataFlowEdge` atoms, and no-edge behavior for non-flow specs.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused information-flow tests passed (14 tests), full suite passed (93 tests), and `git diff --check` passed. Local implementation commit: `f0a7fcb` (`Add component-level data-path edge extraction to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

### 2026-07-05 (session 2): Transitive dependency chain detection

Context: The information-flow validation slice now extracts explicit component-level `DataFlowEdge` atoms, but does not reason about chains implied by those edges. The gap audit lists "richer data-path inference" and "component-level dependency graphs" as next steps.

Approach: After extracting `DataFlowEdge` atoms in `build_information_flow_validation`, build an adjacency list from the extracted edges and run a bounded BFS (max 10 hops) to find nodes reachable in 2+ hops from each source. If A→B and B→C exist, A transitively depends on C. Emit `information-flow-transitive-dependency-reviewed` obligation:
- Pass when no transitive chains are detected ("no transitive dependency chains detected").
- Pass when chains exist and the spec text acknowledges them via 'transitive', 'indirect', 'through', 'via', 'chained', or 'intermediary' wording.
- Unknown with blocking `MissingInformationFlowEvidence` question when chains exist but are not acknowledged.

Tests added: `test_transitive_dependency_detected_and_unacknowledged` (A→B→C without ack → Unknown + blocking question mentioning both endpoints), `test_transitive_dependency_acknowledged_passes` (same edges + 'indirectly...through' → Pass), `test_no_transitive_dependency_when_no_chains` (disconnected edges → Pass with 'no transitive' evidence).

Result: focused information-flow tests passed (17 tests), full suite passed (96 tests), and `git diff --check` passed. Local implementation commit: `69b865a` (`Add transitive dependency chain detection to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

### 2026-07-05 (session 3): Graph-based cycle detection

Context: The information-flow pass extracts explicit `DataFlowEdge` atoms and detects transitive chains, but the existing `information-flow-circular-dependency-reviewed` check is keyword-based only. A graph-based cycle check can detect actual cycles (A→B→A or A→B→C→A) that the spec text may not mention.

Approach: After transitive dependency detection, build a directed adjacency graph from extracted edges and run DFS with white/gray/black coloring to detect back edges. When a back edge is found, extract the cycle path from the DFS stack. Deduplicate cycles by sorted node set. Emit `information-flow-cycle-detected` obligation: Pass when no cycles found, Unknown with blocking `MissingInformationFlowEvidence` question when cycles exist.

Tests added: `test_cycle_detected_from_graph_edges` (A→B + B→A → Unknown + blocking question), `test_no_cycle_when_acyclic_graph` (DAG → Pass with 'no cycles' evidence), `test_three_node_cycle_detected` (A→B→C→A → Unknown mentioning endpoints), `test_no_cycle_when_no_edges` (no DataFlowEdge atoms → no cycle obligation).

Result: focused information-flow tests passed (21 tests), full suite passed (100 tests), and `git diff --check` passed. Local implementation commit: `b7b85d9` (`Add graph-based cycle detection to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.
