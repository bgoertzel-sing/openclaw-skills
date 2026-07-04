# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] 2026-06-30: Expanded the `specatom_hs` source indexer to preserve multi-line bullet continuations without swallowing nested acceptance-test bullets.
- [x] 2026-06-30: Added conservative concept-table pass distinguishing explicit local definitions, external links, and unresolved references with Unknown checks/questions.
- [x] 2026-06-30: Extended concept-table pass to support conservative aliases (`[def:]`, `[ref:]`, `[concept:]`) and bare glossary definitions beyond explicit `:Concept:` / `[external:...]` syntax.
- [x] 2026-06-30: Extended concept-table pass to preserve first-class concept reference occurrence atoms with exact marker-level spans and occurrence-targeted validation checks.
- [x] 2026-06-30: Added a shallow requirement/test coverage pass with Pass/Unknown `requirement-has-acceptance-test` checks, missing-test questions, and coverage atoms.
- [x] 2026-07-01: Added initial scaffold fact-arity and declared-reference validators for supported object-fact predicates, with Fail diagnostics for malformed arity/dangling targets and Unknown for predicates outside the current schema.
- [x] 2026-07-01: Tightened `petta_reified_v0` backend projection with profile-filtered supported predicates/arity refusals and fuller validation rationale/evidence atoms.
- [x] 2026-07-01: Added first Unknown-to-question validator path beyond concept/coverage cases: unsupported fact predicates now produce profile question objects that block the relevant fact-profile obligation.
- [x] 2026-07-01: Added validation-layer self-checks so check records must cite a known obligation and match its property/target.
- [x] 2026-07-01: Added validation-obligation provenance/target self-checks so malformed obligation source spans and undeclared targets fail crisply.
- [x] 2026-07-01: Extended `petta_reified_v0` export with source provenance manifest atoms (`plain-file`, `source-span`, `section`, `plain-item`, `derived-from`) and ground-truth regression coverage.
- [x] 2026-07-01: Tightened concept occurrence span indexing so marker spans on multi-line bullet continuation lines carry exact start/end line numbers.
- [x] 2026-07-01: Added PeTTa reified-profile semantic-level validation so unsupported levels such as `RawTextOnly` create explicit Unknown checks and blocking questions before export/refusal.
- [x] 2026-07-01: Added explicit requirement/test coverage labels (`[id:...]` / `[covers:...]`) with `RequirementLabel` and `CoverageClaim` atoms, label-resolved coverage, and Unknown/blocking-question handling for unresolved coverage labels.
- [x] 2026-07-01: Added duplicate requirement-label ambiguity handling: explicit `[covers:...]` claims now require exactly one matching label and otherwise produce Unknown checks plus duplicate/ambiguous target questions.
- [x] 2026-07-01: Added orphan acceptance-test coverage obligations/questions plus profile-safe `OrphanAcceptanceTest` export.
- [x] 2026-07-01: Added object-fact subject validation and PeTTa refusal for facts whose declared subject does not match the owning SpecObject.
- [x] 2026-07-02: Made explicit requirement coverage labels document-scoped, so `[covers:...]` acceptance tests can resolve forward to later requirement sections instead of falsely becoming missing-label questions.
- [x] 2026-07-02: Added `check-status-is-known` validation so check records with undeclared/non-enum statuses fail crisply, and made PeTTa check export robust to malformed status text.
- [x] 2026-07-02: Added `check-has-evidence` validation so check records with empty evidence fail crisply as malformed diagnostics.
- [x] 2026-07-02: Added source-span byte/line validation (`source-span-within-file-bounds`, `source-span-lines-match-byte-offsets`) so malformed indexed spans fail crisply as malformed provenance.
- [x] 2026-07-02: Added Plain file digest validation (`plain-file-digest-matches-content`) so corrupted preserved-source manifests fail crisply as malformed provenance.
- [x] 2026-07-02: Added section/item PlainFile link validation (`section-file-is-indexed`, `section-has-source-span`, `item-file-is-indexed`) so malformed source-index records fail crisply before backend provenance export.
- [x] 2026-07-02: Tightened source-index provenance consistency with section/item/span file-ID cross-checks so cross-file-corrupted source records fail crisply.
- [x] 2026-07-02: Froze the v0.1 target profile and completed a validator gap audit against Appendix N/P categories; docs live in `repos/specatom-hs/docs/v01-profile.md` and `repos/specatom-hs/docs/validator-gap-audit.md`.
- [x] 2026-07-02: Added v0.1 CLI/demo outputs (`specatom_hs.cli`, grouped `.metta`, Markdown diagnostics, `scripts/demo.sh`) plus an `auth_service.plain` review fixture and regression checks for duplicate labels, missing coverage targets, unresolved concepts, and backend refusals.
- [x] 2026-07-02: Optimized validation obligation/check de-duplication to use stable record IDs instead of whole-dataclass membership, making the larger auth-service review fixture practical in the unit suite.
- [x] 2026-07-02: Added question-object blocker validation so unresolved concept questions point at their exact Unknown obligations and malformed QuestionObjects fail when review text/blocker links are missing or dangling.
- [ ] Extend validators further toward Appendix N/P: richer coverage semantics, additional Unknown-to-question checks, richer check-record provenance, and wider predicate schemas.
- [x] 2026-07-02: Added first v0.2 conservative ML/time-series methodology validation slice: metric declaration, horizon/frequency declaration, reproducibility evidence, and train-only preprocessing fit-scope obligations/questions.
- [x] 2026-07-02: Extended the v0.2 ML/time-series methodology slice with baseline-comparison and uncertainty/error-bar reporting obligations/questions.
- [x] 2026-07-02: Added explicit preprocess-then-split leakage review (`ml-preprocessing-order-reviewed`) with Unknown checks/questions when specs say normalize/scale/preprocess before splitting without train-only fit scope.
- [x] 2026-07-03: Added explicit future/label-as-feature leakage review (`ml-future-label-leakage-reviewed`) with Unknown checks/questions when future values, labels, or targets appear in feature/input contexts.
- [x] 2026-07-03: Added first conservative metric/task appropriateness review (`ml-metric-task-appropriateness-reviewed`) for classification-style metrics on forecast/regression-like ML specs.
- [x] 2026-07-03: Added conservative temporal split-order review (`ml-temporal-split-order-reviewed`) for random/shuffled time-series split wording without chronological/walk-forward/out-of-time evidence.
- [x] 2026-07-03: Added generic-vs-named baseline/uncertainty methodology review (`ml-baseline-comparator-named`, `ml-uncertainty-method-named`) so vague baseline/uncertainty mentions become Unknown blocking questions.
- [x] 2026-07-03: Added prediction-time feature availability review (`ml-feature-availability-reviewed`) so declared ML inputs/features require point-in-time/as-of, lagged, historical, or equivalent availability evidence.
- [ ] v0.2 follow-up: deepen ML/time-series methodology validation with richer comparator/uncertainty semantics and stronger metric appropriateness once target/task facets are explicit.
- [ ] v0.2 candidate: add information-flow and temporal-availability obligations for declared inputs/outputs, freshness/availability assumptions, and temporally impossible claims.
- [x] 2026-07-03: Added first v0.2 security/privacy obligation scaffolding for secrets, PII/privacy handling, access boundaries, and destructive-action safety, defaulting to Unknown/question where evidence is missing.
- [x] 2026-07-03: Added secret log-exposure review (`security-secret-log-exposure-reviewed`) so secret/token/password specs require redaction, masking, or no-logging evidence.
- [x] 2026-07-03: Added first data/sensitivity classification declaration review (`privacy-data-classification-declared`) for PII/personal-data specs, with Unknown blocking questions when classification evidence is absent.
- [x] 2026-07-03: Added privilege-escalation review (`security-privilege-escalation-reviewed`) so access/auth/admin/role specs require least-privilege, approval, audit, admin-only, or self-grant-prevention evidence.
- [x] 2026-07-03: Added PII retention/deletion review (`privacy-retention-deletion-reviewed`) so personal-data specs require retention, deletion/erasure, expiry, or minimization evidence.
- [x] 2026-07-03: Added data-residency/cross-border transfer review (`privacy-data-residency-reviewed`) so PII specs with region/country/jurisdiction/residency/cross-border wording require policy evidence or produce Unknown blocking questions.
- [x] 2026-07-03: Added third-party/vendor/processor sharing review (`privacy-third-party-sharing-reviewed`) so PII specs that mention vendors, processors, partners, external services, exports, uploads, or sharing require DPA/vendor-review/data-sharing policy evidence.
- [x] 2026-07-04: Added lawful-basis/consent review (`privacy-lawful-basis-reviewed`) so PII/personal-data specs require consent, lawful/legal basis, contract, legal-obligation, legitimate-interest, or similar evidence.
- [x] 2026-07-04: Added purpose-limitation review (`privacy-purpose-limitation-reviewed`) so PII/personal-data specs require specific-purpose, use-limitation, no-secondary-use, or secondary-use-review evidence.
- [x] 2026-07-04: Added data-subject rights review (`privacy-data-subject-rights-reviewed`) so PII/personal-data specs require access/correction/rectification/portability/opt-out/privacy-rights evidence.
- [x] 2026-07-04: Added rights-request identity/authentication review (`privacy-rights-request-authentication-reviewed`) so PII/personal-data specs with rights/access/deletion/erasure request wording require identity-verification or authenticated-request evidence.
- [x] 2026-07-04: Added PII access audit review (`privacy-pii-access-audit-reviewed`) so PII/personal-data specs with access/admin/role wording require access audit, logging, or monitoring evidence.
- [ ] v0.2 follow-up: deepen security/privacy semantics with richer data-classification facets, policy provenance, and stronger access-control checks once Phase 2/3 objects exist.
- [ ] Extend profile-aware backend projection for `petta_reified_v0` beyond the current source manifest, supported object facts, and validation records, still without mutating the IR.
- [ ] Preserve the uploaded SpecAtom-HS PDF as a research-library source sidecar if/when desired; current implementation used `/home/openclaw/tmp/omegaclaw-telegram-attachments/1782780878-file_3.pdf.extracted.txt`.

## Next

- [x] 2026-06-29: Implemented first PeTTa target reality check scaffold: `petta_reified_v0` profile gates, supported semantic levels, unsupported-level refusals, and RawTextOnly executable-skeleton refusal policy.
- [ ] Implement Phase 2 SpecAtom-HS core more completely: `Scope`, `EpistemicStatus`, `Evidence`, `Interpretation`, and `Bridge` objects.
- [ ] Implement Phase 3 facets: witnesses/backend artifacts, process/resource placeholders, and revisions.
- [ ] Implement Phase 4 PeTTa reified backend producing target-profile-filtered `.metta` files and richer source provenance manifests.
- [ ] Add first SUMO/EXPO/Hyperseed bridge table with graded contextual correspondences from Appendix K.
- [ ] Compare emitted atoms against design note 0006 and record divergences.

## Waiting or blocked

- [ ] Remote repository creation/push - needs explicit user direction on name/visibility.
- [ ] Full PDF library preservation - needs a deliberate library-curation step if this source should be kept beyond the temporary attachment path.

## Someday or exploratory

- [ ] Richer information-flow/time validator for future pollution and temporal availability.
- [ ] PLN overlay for conflicting claims and confidence propagation.
- [ ] MeTTa-IL profile.
- [ ] Rholang process profile.
- [ ] TyLA/OSLF deeper type/proof alignment.

## Done recently

- [x] 2026-07-04: Added PII access audit/logging review to the conservative security/privacy slice; 67 tests pass.
- [x] 2026-07-04: Added rights-request authentication review to the conservative security/privacy slice; 66 tests pass.
- [x] 2026-07-04: Added data-subject rights review to the conservative security/privacy slice; 65 tests pass.
- [x] 2026-07-04: Added purpose-limitation review to the conservative security/privacy slice; 64 tests pass.
- [x] 2026-07-04: Added lawful-basis/consent review to the conservative security/privacy slice; 63 tests pass.
- [x] 2026-07-03: Added third-party/vendor/processor sharing review to the conservative security/privacy slice; 62 tests pass.
- [x] 2026-07-03: Added data-residency/cross-border transfer review to the conservative security/privacy slice; 61 tests pass.
- [x] 2026-07-03: Added first data/sensitivity classification declaration review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added PII retention/deletion review to the conservative security/privacy slice; 60 tests pass.
- [x] 2026-07-03: Added privilege-escalation review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added secret log-exposure review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added security/privacy obligation scaffolding for secrets/PII/access/destructive actions; 59 tests pass.
- [x] 2026-07-03: Added prediction-time feature availability review obligations/questions; 57 tests pass.
- [x] 2026-07-03: Added named baseline-comparator and uncertainty-method review obligations/questions; 55 tests pass.
- [x] 2026-07-03: Added conservative ML temporal split-order review obligations/questions; 54 tests pass.
- [x] 2026-07-03: Added conservative ML metric/task appropriateness review obligations/questions; 52 tests pass.
- [x] 2026-07-03: Added future/label-as-feature leakage review obligations/questions to the conservative ML/time-series methodology pass; 51 tests pass.
- [x] 2026-07-02: Added preprocess-then-split leakage review obligations/questions to the conservative ML/time-series methodology pass; 50 tests pass.
- [x] 2026-07-02: Added baseline-comparison and uncertainty/error-bar obligations/questions to the conservative ML/time-series methodology pass; 49 tests pass; pushed private backup `718a8c8`.
- [x] 2026-07-02: Added conservative ML/time-series methodology obligations/questions; 49 tests pass.
- [x] 2026-07-02: Added question-object blocker validation and unresolved-concept `Blocks` links; 47 tests pass.
- [x] 2026-07-02: Added v0.1 CLI/demo output path, grouped PeTTa atoms, Markdown diagnostics, auth-service review fixture, and stable-ID validation record de-duplication; 46 tests pass.
- [x] 2026-07-02: Tightened section/item/span file-ID provenance consistency plus malformed cross-file regression coverage; 37 tests pass.
- [x] 2026-07-02: Added section/item PlainFile link validation plus malformed-file-link regression coverage; 37 tests pass.
- [x] 2026-07-02: Added Plain file digest validation plus malformed-digest regression coverage; 36 tests pass.
- [x] 2026-07-02: Added source-span byte/line validation plus malformed-span regression coverage; 35 tests pass.
- [x] 2026-07-02: Added validation-layer evidence self-checks (`check-has-evidence`) plus empty-evidence regression coverage; 34 tests pass.
- [x] 2026-07-02: Added validation-layer status self-checks (`check-status-is-known`) plus malformed-status regression coverage; 34 tests pass.
- [x] 2026-07-02: Added document-scoped coverage-label resolution for explicit `[covers:...]` claims; 34 tests pass.
- [x] 2026-07-01: Added `fact-subject-matches-object` validation plus backend subject-mismatch refusals for object-scoped facts; 33 tests pass.
- [x] 2026-07-01: Added orphan acceptance-test coverage obligations/questions with profile-safe `OrphanAcceptanceTest` export and regression coverage; 33 tests pass.
- [x] 2026-07-01: Added duplicate requirement-label ambiguity handling with Unknown checks/questions and regression coverage; 32 tests pass.
- [x] 2026-07-01: Added explicit requirement/test coverage labels (`[id:...]` / `[covers:...]`) with export ground-truth regression and unresolved-target questions; 31 tests pass.
- [x] 2026-07-01: Added PeTTa reified-profile semantic-level obligations (`object-supported-by-petta-reified-profile`) with Unknown/blocking-question handling for RawTextOnly unsupported export; 29 tests pass.
- [x] 2026-07-01: Added validation-obligation provenance/target self-checks (`obligation-has-source-provenance`, `obligation-target-is-declared`) with malformed-obligation regression tests; 28 tests pass.
- [x] 2026-07-01: Tightened concept occurrence line-span indexing for continuation-line references, with regression coverage; 27 tests pass.
- [x] 2026-07-01: Added PeTTa source provenance manifest export with exact source/index atoms and a regression test comparing generated atoms to ground truth; 26 tests pass.
- [x] 2026-07-01: Added validation-layer self-checks (`check-links-known-obligation`, `check-target-matches-obligation`) with malformed diagnostic regression tests; 25 tests pass.
- [x] 2026-07-01: Added Unknown-to-question handling for unsupported fact predicates with `UnsupportedFactPredicate`, `QuestionText`, and `Blocks` facts; 24 tests pass.
- [x] 2026-07-01: Added `petta_reified_v0` profile filtering for supported object-fact predicates/arity plus reified validation rationales, check-obligation links, and check evidence; 23 tests pass.
- [x] 2026-07-01: Added `FACT_SCHEMAS`-based arity/reference validation in `specatom_hs.validators`, including tests for passing supported facts, malformed `Covers` arity, and dangling coverage targets; 21 tests pass.
- [x] 2026-06-30: Added `build_requirement_test_coverage`, conservative requirement/test objects, Pass/Unknown coverage validation, missing acceptance-test questions, and PeTTa reified export of supported object facts/checks; 19 tests pass.
- [x] 2026-06-30: Added conservative concept aliases (`[def:Name]`, `[ref:Name]`, `[concept:Name]`) and bare definition/glossary bullets, with exact occurrence spans and regression coverage.
- [x] 2026-06-30: Preserved multi-line bullet continuations in `specatom_hs.source_indexer` with regression coverage for child/nested acceptance-test bullets.
- [x] 2026-06-30: Added exact-span `ConceptReferenceObject` occurrence atoms for concept definitions/references/external markers plus occurrence-targeted validation checks.
- [x] 2026-06-30: Added `specatom_hs.passes.build_concept_table` plus tests for `ConceptObject`, `ConceptStatus`, `concept-reference-resolved` obligations/checks, and unresolved concept questions.

- [x] 2026-06-29: Added minimal `specatom_hs` scaffold modules (`schema.py`, `passes.py`, `source_indexer.py`, `validators.py`, `backends/petta.py`), `examples/minimal.plain`, and focused tests for source spans, validation records, PeTTa gates, and reified atom stubs.
- [x] 2026-06-29: Created `projects/specatom-hs/` project notebook and source-summary/implementation-plan document from Benjamin's uploaded SpecAtom-HS design PDF and existing project context.
- [x] 2026-06-29: Created local prototype repo `projects/specatom-hs/repos/specatom-hs` with Python stdlib package, parser/indexer, SpecAtom-HS JSON/MeTTa-ish emitter, shallow Appendix G/O templates, crisp validator checks, examples, and 5 passing unit tests.
