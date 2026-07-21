# SpecAtom-HS Plain-to-MeTTa Compiler

- Slug: `specatom-hs`
- Status: `active`
- Created: `2026-06-29`
- Last reviewed: `2026-07-20` (backend-safe check status diagnostics)
- Owner: Benjamin Goertzel

## Purpose

Build a conservative compiler pipeline from Plain software specifications into SpecAtom-HS, a typed, source-preserving, context-indexed, evidence-bearing Atomspace-style intermediate representation, then project that IR first to PeTTa/MeTTa reified atoms and later to executable skeletons, MeTTa-IL, Rholang, and PLN reasoning workflows.

The seed design is Benjamin's 2026-06-29/30 PDF *SpecAtom-HS: A Hyperseed-Compatible Intermediate Representation for Plain-to-MeTTa Compilation, PeTTa Execution, Logical Validation, and PLN Reasoning* and its coding-agent appendices, plus earlier local design notes in `projects/hyperseed-formalizations/repos/hyperseed-formalizations/papers/0005-plain-metta-rholang-spec-compiler/` and `papers/0006-plain-metta-rholang-spec-ir/`.

## Success criteria

Initial milestone:

> Given a small Plain-like input, emit inspectable SpecAtom-HS atoms with stable IDs, source spans, roles, concepts, requirements, tests, evidence wrappers, validation obligations, and a PeTTa reified projection; run structural validation checks and report Pass/Fail/Unknown diagnostics without hallucinating executable semantics.

Observable criteria:

- Source indexer preserves file, section, item, raw text, and source spans for every emitted object.
- PlainAST parser recognizes core Plain sections, bullet nesting, concept references, and acceptance-test attachment.
- SpecAtom-HS core emits object roles, semantic levels, contexts, claims/propositions, evidence, interpretations, bridge suggestions, and validation objects.
- MVP facets cover concepts/types, requirements/obligations, actions, tests/validation experiments, witnesses/backend artifacts, process/resource placeholders, questions, and revisions.
- PeTTa target profile emits reified atoms only from supported facets and marks TODO/unknown witnesses rather than inventing code.
- Validator emits validation obligations and check records for schema integrity, source provenance, undefined concepts, uncovered obligations, TODO witnesses, raw-text-only skeleton violations, and selected information-flow/time checks.
- Tests demonstrate malformed/underspecified inputs produce structured diagnostics/questions rather than silent success.

## Scope

### In scope

- Local project notebook and implementation planning.
- Local prototype repository under `projects/specatom-hs/repos/specatom-hs`.
- Parser and IR schema for a practical Plain subset.
- JSON and PeTTa/MeTTa reified backends.
- Validation obligation generation and crisp structural validators.
- SUMO, EXPO, and Hyperseed bridge records as graded contextual correspondences, not identity mappings.
- Test-run representation as EXPO-like validation experiments with measurements and p-bit evidence.
- Python or another host language for the compiler implementation, as long as emitted target atoms and validation outputs are inspectable.

### Out of scope for now

- Full natural-language understanding of arbitrary English.
- Direct generation of production code from raw Plain text.
- Remote repository creation/push until explicitly requested.
- Paid compute.
- Full SUMO/EXPO import, full Hyperseed ontology import, or full PLN execution in the MVP.
- Treating generated PeTTa/Rholang skeletons as verified unless validation evidence supports that claim.

## Current state

As of the 2026-07-21 05:30 PDT worker, crisp PlainFile field validation
matches the PeTTa backend's non-blank path/digest gates and safely requires
preserved source text to be a string before digest recomputation. Malformed
values now Fail deterministically instead of crashing or reaching export.

As of the 2026-07-21 03:30 PDT worker, crisp SourceSpan bound validation
matches the PeTTa backend's integer/order gates. List, boolean, `None`, and
reversed byte/line bounds now deterministically Fail instead of raising during
numeric comparisons, while valid bounds explicitly Pass.

As of the 2026-07-21 01:30 PDT worker, crisp SpecObject source-span identity
validation matches the PeTTa backend provenance gate. `None` remains valid
optional absence, list and blank identities deterministically Fail, non-blank
string identities Pass, and malformed unhashable provenance no longer crashes
the broader source-or-generated provenance check.

As of the 2026-07-20 23:30 PDT worker, crisp ValidationObligation source-span
identity validation matches the PeTTa backend provenance gate. `None` remains a
valid absent optional provenance value, list and blank identities Fail exactly,
and non-blank string identities Pass before declared-span resolution.

As of the 2026-07-20 21:30 PDT worker, crisp CheckRecord status validation
reports exact unsupported runtime values and types, matching the PeTTa backend's
declared-enum refusal gate without ambiguously stringifying malformed statuses.

As of the 2026-07-20 19:30 PDT worker, crisp CheckRecord target validation
matches the PeTTa backend's target-identity gate. `None`, container, and blank
targets now deterministically Fail, while valid non-blank target text
explicitly Passes.

As of the 2026-07-20 17:30 PDT worker, crisp CheckRecord property validation
matches the PeTTa backend's safe-symbol gate. `None`, container, and blank
properties now deterministically Fail, while valid non-blank property text
explicitly Passes.

As of the 2026-07-20 15:30 PDT worker, crisp CheckRecord obligation-link
validation matches the PeTTa backend's obligation-identity gate. `None`,
container, and blank obligation IDs now deterministically Fail instead of
reaching unsafe dictionary membership, while valid non-blank string links Pass.

As of the 2026-07-20 13:30 PDT worker, crisp ValidationObligation target
validation matches the PeTTa backend's target-identity gate. `None`, container,
and blank targets now deterministically Fail, while non-blank string targets
explicitly Pass before declared-target resolution is considered.

As of the 2026-07-20 11:30 PDT worker, crisp ValidationObligation property
validation matches the PeTTa backend's safe-symbol gate. `None`, container,
and blank properties now deterministically Fail, while non-blank property text
explicitly Passes.

As of the 2026-07-20 09:30 PDT worker, crisp ValidationObligation rationale
validation matches the PeTTa backend's reviewable-text gate. `None`, container,
and blank rationales now deterministically Fail, while non-blank rationale text
explicitly Passes.

As of the 2026-07-20 07:30 PDT worker, crisp CheckRecord evidence validation
matches the PeTTa backend's reviewable-text gate. `None` and container values
now deterministically Fail instead of passing through string coercion, while
non-blank string evidence still Passes and blank strings retain their explicit
empty-evidence failure.

As of the 2026-07-20 05:30 PDT worker, crisp fact-subject validation mirrors
the PeTTa backend's exact string-subject gate. Scalar values such as integer
`7` can no longer alias the owning string object identity `"7"`; malformed
subject types deterministically Fail while exact string owners Pass.

As of the 2026-07-20 03:30 PDT worker, crisp fact validation mirrors the
PeTTa backend's argument gates. Container-valued arguments, non-string object
references, blank/None values, and non-finite floats now receive deterministic
Fail evidence, while supported non-empty scalar arguments explicitly Pass.

As of the 2026-07-20 01:30 PDT worker, crisp validation rejects malformed
non-tuple fact records and non-string predicates with deterministic Fail
evidence, matching the PeTTa backend's existing refusal gates. Malformed facts
also can no longer crash generated-provenance inspection.

As of the 2026-07-19 23:30 PDT worker, crisp validation requires Section and
PlainItem identities to be non-blank strings and excludes malformed identities
from section/item and fact-validation indexes. List-valued and blank IDs now
produce deterministic identity Fail evidence instead of crashing, while valid
neighboring IDs explicitly Pass.

As of the 2026-07-19 21:30 PDT worker, crisp validation requires SourceSpan
identities to be non-blank strings and excludes malformed identities from all
span lookup paths. List-valued and blank span IDs now produce deterministic
identity Fail evidence instead of crashing uniqueness, validation-provenance,
or edge-provenance indexing, while valid neighboring span IDs explicitly Pass.

As of the 2026-07-19 19:30 PDT worker, crisp validation requires PlainFile
identities to be non-blank strings and avoids indexing malformed unhashable IDs.
List-valued and blank file IDs now produce deterministic identity Fail evidence
instead of crashing source-span or validation-target indexing, while valid
neighboring file IDs receive explicit Pass records.

As of the 2026-07-19 17:30 PDT worker, crisp validation explicitly requires
ValidationObligation and CheckRecord identities to be non-blank strings. This
matches the PeTTa backend's existing record-ID gates: malformed list-valued or
blank IDs now receive dedicated backend-safe identity Fail evidence, while
valid IDs receive explicit Pass records.

As of the 2026-07-19 15:30 PDT worker, crisp validation handles unhashable
malformed ValidationObligation and CheckRecord identities without attempting
unsafe Counter, set, or dictionary membership. List-valued IDs now produce
deterministic Fail evidence and downstream validation continues instead of
crashing, matching the PeTTa backend's existing refusal gates.

As of the 2026-07-19 13:30 PDT worker, crisp validation handles unhashable
malformed SpecObject identities without attempting unsafe Counter or set
membership. List-valued IDs now produce deterministic Fail evidence for both
identity uniqueness and backend-safe identity obligations, while downstream
validation continues instead of crashing.

As of the 2026-07-19 11:30 PDT worker, crisp validation requires SpecObject
identities to be non-blank strings. Non-string and whitespace-only IDs now
produce deterministic Fail evidence before the PeTTa backend's existing refusal
gate, while valid identities receive an explicit Pass.

As of the 2026-07-19 09:30 PDT worker, crisp validation handles unhashable
malformed semantic-level values without attempting unsafe set membership. Such
values now produce the existing deterministic Fail identity-level check and
Unknown PeTTa-profile refusal/question instead of crashing validation.

As of the 2026-07-19 07:30 PDT worker, crisp validation explicitly requires
every SpecObject role to be a declared `Role` enum member. Malformed or
unsupported role values now produce a deterministic Fail check before the
PeTTa backend's existing refusal gate, rather than leaving the refusal visible
only during export.

As of the 2026-07-19 05:30 PDT worker, crisp validation handles malformed or
unsupported semantic-level values without dereferencing them as enum members.
It now emits a deterministic Fail identity-level check and an Unknown PeTTa
profile refusal/question instead of crashing before diagnostics are available.

As of the 2026-07-19 03:30 PDT worker, crisp validation now requires unique
ValidationObligation and CheckRecord identities. Duplicate validation-layer IDs
produce one deterministic Fail record with the ambiguous identity and occurrence
count, aligning diagnostics with the PeTTa exporter's existing refusal gates.

As of the 2026-07-19 01:30 PDT worker, crisp validation explicitly requires
unique SpecObject identities. Duplicate object IDs now produce one deterministic
Fail record with the ambiguous identity and occurrence count, matching the
PeTTa exporter's existing duplicate-object refusal gate.

As of the 2026-07-18 23:30 PDT worker, crisp validation explicitly requires
unique indexed PlainFile and SourceSpan identities. Duplicate IDs now produce a
single deterministic Fail record on the ambiguous source record itself, in
addition to the existing fail-closed downstream link diagnostics.

As of the 2026-07-18 21:30 PDT worker, crisp validation now mirrors the PeTTa
exporter's nested-item safety gates. Every declared parent link produces
obligations checking that the parent is uniquely indexed, is not the child
itself, and belongs to the same file and section. Missing or duplicate parents,
self-parenting, and cross-context parenting produce deterministic Fail evidence.

As of the 2026-07-18 19:30 PDT worker, crisp validation explicitly requires
unique indexed Section and PlainItem identities. Duplicate IDs now produce a
single deterministic Fail record with the ambiguous identity and occurrence
count instead of collapsing per-target obligations into an apparently valid
record.

As of the 2026-07-18 17:30 PDT worker, `section-has-source-span` and
`item-has-source-span` require a unique indexed source-span identity. Duplicate
span IDs now produce Fail checks with deterministic ambiguity evidence instead
of passing on set membership while adjacent file-match checks fail.

As of the 2026-07-18 15:30 PDT worker, source-span, section, and item
file-link validation fails closed when an indexed PlainFile ID is duplicated.
The validators no longer treat ambiguous file membership as sufficient or use
the final duplicate for bounds/line checks; exact regression evidence includes
the ambiguous identity and occurrence count.

As of the 2026-07-18 13:30 PDT worker, item section-link validation fails
closed when an indexed section ID is duplicated. `item-has-section` and
`item-file-matches-section-file` no longer select the last duplicate and risk
reporting a false Pass; exact regression coverage requires Fail evidence with
the ambiguous ID and occurrence count.

As of the 2026-07-18 11:30 PDT worker, crisp section/item span-file
validation fails closed when an indexed source-span ID is duplicated. It no
longer selects the last duplicate and risks reporting a false Pass; exact
regression coverage requires Fail evidence identifying the ambiguous ID and
occurrence count.

As of the 2026-07-18 09:30 PDT worker, exact regression coverage now pins
`item-span-file-matches-item-file` to the canonical span in `doc.spans`. A
conflicting embedded `SourceSpan` with the same ID cannot mask an item
cross-file mismatch; the validator emits Fail with the canonical file ID.

As of the 2026-07-18 07:30 PDT worker, the crisp
`section-span-file-matches-section-file` validator resolves a section's span ID
through the indexed `doc.spans` manifest. A conflicting embedded `SourceSpan`
with the same ID can no longer mask a canonical cross-file mismatch and produce
a false Pass validation record.

As of the 2026-07-18 05:30 PDT worker, section provenance validation resolves a section's span ID against the source span actually admitted to the PeTTa manifest before checking file consistency. A conflicting embedded `SourceSpan` record can no longer mask that the canonical emitted span belongs to another file and induce a false cross-file `derived-from` atom.

As of the 2026-07-18 03:32 PDT worker, PeTTa source-manifest export also fails closed on Plain-item parent links: missing, previously refused, self-referential, cross-file, and cross-section parents suppress the child item, and refusal propagates to descendants of a refused parent. Forward references to valid parents remain supported.

As of the 2026-07-18 01:30 PDT worker, when a source manifest is present the PeTTa reified exporter emits object and validation-obligation `derived-from` atoms only for source spans that survived the manifest field, duplicate-ID, and file-link gates. Missing or earlier-refused spans produce structured refusals, valid neighboring links still emit, absent optional provenance remains allowed, and standalone object-only projection remains backward-compatible.

As of the 2026-07-17 23:30 PDT worker, PeTTa reified source-manifest export also refuses Plain items whose file, section, or source span was not actually emitted, and refuses items whose emitted section or span belongs to a different file. Together with the earlier file/span/section gates, this closes the emitted provenance chain through `PlainItem` while retaining valid neighboring manifest atoms.

On 2026-06-29, Benjamin uploaded the revised SpecAtom-HS design PDF and requested a bounded subagent lane. Existing related formalization notes live in `hyperseed-formalizations` and should be treated as design context, not the software implementation home. This project notebook tracks the compiler/prototype itself.

As of 2026-07-17, PeTTa reified export fails closed on malformed source-manifest and validation-record container entries, malformed `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` atom-bearing fields, duplicate source-manifest/object IDs, non-string/blank/duplicate obligation/check IDs, malformed obligation properties, target IDs, rationales, and malformed check links, properties, target IDs, statuses, and evidence. Section/item gates now reject unsafe identities and links, boolean/non-integer or negative ordinals, malformed provenance-span records/IDs, blank item text, and malformed optional parent IDs while valid neighboring records still emit. Non-`PlainFile`, non-`SourceSpan`, non-`Section`, non-`PlainItem`, non-`ValidationObligation`, and non-`CheckRecord` entries produce structured type-bearing refusals instead of crashing. Summary atoms use the first actually emitted file identity rather than dereferencing an invalid first source record. All occurrences of a duplicate file, span, section, item, object, or validation identity are suppressed; checks linked to refused obligations are also suppressed. Duplicate question objects are excluded from document-validation summaries rather than being counted despite having no emitted object atoms. Emitted checks must agree with their cited obligation's property and target, so `check-obligation` atoms and summaries cannot claim ambiguous, dangling, or internally inconsistent validation records. Whitespace-only object and validation-obligation source-span IDs are refused rather than exported as malformed `derived-from` atoms, while genuinely absent optional provenance remains allowed. Runtime values such as integer `7` can no longer alias legitimate string fields in emitted atoms; refused checks are excluded from the document-validation summary so it cannot claim records that were not exported.

A local-only Python stdlib MVP now exists at `projects/specatom-hs/repos/specatom-hs`. It parses a Plain-like subset, preserves source spans and file digests, emits SpecAtom-HS JSON plus MeTTa-ish S-expressions, and runs initial crisp validators. The recommended minimal `specatom_hs` scaffold modules are also present (`schema.py`, `passes.py`, `source_indexer.py`, `validators.py`, `backends/petta.py`) with tests for source indexing, validation records, PeTTa refusal gates, and safe reified emission. A first conservative concept-table/validation pass now distinguishes explicit local definitions, external links, unresolved references, exact-span concept reference occurrence atoms, conservative aliases (`[def:]`, `[ref:]`, `[concept:]`, and bare glossary definitions), and multi-line bullet continuations while keeping nested acceptance-test bullets separate. Concept occurrence spans now also preserve exact marker line numbers for references found on continuation lines, not just exact byte slices. A shallow requirement/test coverage pass now creates requirement and acceptance-test objects, emits `requirement-has-acceptance-test` obligations with Pass/Unknown checks, asks missing-test questions, and exports supported object facts/validation records through the PeTTa reified profile. The validator now also emits scaffold fact-arity and declared-reference checks for supported predicates (`Covers`, `SourceItem`, `Blocks`, `RefersToConcept`, etc.), producing Fail diagnostics for malformed arity or dangling targets and Unknown for predicates outside the current schema. Unknown fact predicates now also create explicit `QuestionObject` records with `UnsupportedFactPredicate` and `Blocks` facts, so profile gaps are reviewable rather than only buried in check text. Unresolved concept questions now also block their exact `concept-reference-resolved` Unknown obligations, and question records are self-validated for non-empty review text plus known blocked obligations. The information-flow slice now also extracts explicit `feeds into`, `pulls ... from`, `pushes ... to`, `ingests ... from`, and `emits ... to` component data-path wording as exact-spanned `DataFlowEdge` atoms, with target-span trimming to avoid swallowing surrounding temporal/preposition words while preserving component labels. The PeTTa backend filters object facts by the supported predicate/arity/subject profile instead of exporting unknown, malformed, or wrong-subject facts, while preserving validation rationales, check-obligation links, and check evidence as reified atoms. Validation-layer self-checks now ensure Plain file digests reproduce from preserved source text, source spans cite indexed files with in-bounds byte ranges and byte-offset-derived line numbers, sections/items link back to indexed PlainFiles/source spans with matching file IDs, validation obligations cite known source spans/targets where available, and each check record cites a known obligation, uses a declared status, preserves non-empty evidence, and matches its declared property/target, catching malformed source/provenance/diagnostic records as first-class failures. The PeTTa reified profile now also emits a source provenance manifest (`plain-file`, `source-span`, `section`, `plain-item`, and `derived-from`) with regression tests comparing generated atoms to indexed ground truth, plus grouped `.metta` output sections for source, object, validation, and refusal review. PeTTa reified-profile semantic-level support is now explicit in validation: unsupported levels such as `RawTextOnly` create `object-supported-by-petta-reified-profile` Unknown checks and blocking `QuestionObject`s instead of being left only to backend refusals. Phase 2 semantic markers now align source spans by raw-text occurrence index, so repeated same-item markers and continuation-line markers cite exact slices instead of the first matching text. `Bridge:` markers now accept arbitrary ontology labels but keep the conservative support whitelist (`sumo`, `expo`, `hyperseed`): unsupported labels still become source-spanned `BridgeObject`s, Unknown `bridge-profile-supported` checks, and blocking review questions rather than being silently skipped. Explicit `Confidence:` markers now create source-spanned epistemic metadata with normalized `Confidence`/`ConfidenceValue` atoms; values in `[0,1]` (including percentages such as `83%`) pass `confidence-value-in-unit-interval`, while out-of-range or non-numeric values produce Unknown checks plus blocking `UnsupportedConfidenceValue` questions rather than being treated as truth values or silently ignored. Bridge relation validation now keeps correspondences conservative: supported labels such as `related`, `analogy`, `refines`, and `approximates` pass `bridge-relation-conservative`, while identity/equivalence-style labels such as `identical` produce Unknown checks plus blocking `UnsupportedBridgeRelation` questions instead of being accepted as ontology identity claims. Explicit `Revision:` markers now create source-spanned `RevisionObject`s with `Revision`/`RevisionText`/`Revises` facts, a `revision-has-source-provenance` Pass check, and PeTTa reified export support without inferring migration semantics. A first Phase 3 witness/backend-artifact marker slice now detects explicit `Witness:`, `Artifact:`, and `Backend artifact:` annotations, emits source-spanned `BackendArtifact` objects with `Witness`/`WitnessText`/`WitnessFor` facts, passes concrete file/test/log/commit/hash-style artifacts, and turns TODO/raw-text-only/non-concrete placeholders into `witness-artifact-reviewable` Unknown checks plus exported `MissingWitnessArtifact` blocking questions rather than inventing executable evidence. Requirement/test coverage now supports document-scoped explicit requirement labels (`[id:...]`) and acceptance-test coverage claims (`[covers:...]`), exports `RequirementLabel`/`CoverageClaim` atoms, avoids proximity-only misattachment when labels resolve (including forward references to later requirement sections), turns unresolved coverage labels into Unknown checks plus blocking questions, refuses ambiguous duplicate-label coverage by emitting `requirement-label-is-unique` / `coverage-claim-target-resolved` Unknown checks plus duplicate/ambiguous target questions, and flags orphan acceptance tests with `acceptance-test-covers-requirement` Unknown checks plus exported `OrphanAcceptanceTest` blocking questions. The v0.2 methodology slice now detects ML/time-series-like specs and emits conservative obligations for evaluation metric declaration, metric/task appropriateness review, horizon/frequency declaration, reproducibility evidence, train-only preprocessing fit scope, explicit preprocess-then-split leakage review, future/label-as-feature leakage review, prediction-time feature availability review, real-time/current feature freshness review, temporal split-order review, baseline comparison, named baseline-comparator review, uncertainty/error-bar reporting, and named uncertainty-method review; missing evidence becomes `MissingMethodologyEvidence` blocking questions and supported PeTTa atoms. Explicit author `Question:` markers now also become source-spanned `QuestionObject`s with `ExplicitQuestion`/`QuestionText`/`QuestionsObject`/`SourceItem`/`Blocks` facts, `explicit-question-needs-answer` Unknown checks, and PeTTa reified export support so review questions are preserved as blocking obligations rather than ordinary prose. Explicit `Open issue:` / `Issue:` markers now likewise become source-spanned blocking question objects with `OpenIssue`/`OpenIssueText`/`IssueFor` facts and `open-issue-needs-resolution` Unknown checks, preserving unresolved issue prose as review obligations while stopping spans before following markers. Explicit `TODO:` / `To-do:` markers now likewise become source-spanned blocking question objects with `TodoItem`/`TodoText`/`TodoFor` facts and `todo-item-needs-resolution` Unknown checks, preserving incomplete spec/implementation notes as blocking review obligations while stopping spans before following markers. Explicit `Priority:` markers now create source-spanned review objects with `Priority`/`PriorityText`/`PriorityValue`/`PriorityFor` facts, Pass/Unknown `priority-value-reviewable` checks, and `UnsupportedPriorityValue` blocking questions for unsupported or placeholder values. Explicit `Owner:` / `Assignee:` markers now create source-spanned accountability review objects with `Owner`/`OwnerText`/`OwnerFor` facts, Pass/Unknown `owner-assignment-reviewable` checks, and `MissingOwnerAssignment` blocking questions for TODO/TBD/unassigned placeholders. Explicit `Deprecated:` / `Deprecation:` and `Replacement:` markers now create source-spanned review objects with `Deprecated`/`DeprecatedText`/`DeprecatedFor` and `Replacement`/`ReplacementText`/`Replaces` facts; same-item replacements link via `DeprecatedReplacedBy`, while missing replacement/migration/sunset/removal dispositions produce Unknown checks plus exported `MissingDeprecationDisposition` blocking questions. Explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` markers now create source-spanned validation objects with `AcceptanceCriterion`/`AcceptanceCriterionText`/`AcceptanceCriterionFor` facts, Pass/Unknown `acceptance-criterion-reviewable` checks, and `MissingAcceptanceCriterionDetail` blocking questions for TODO/TBD/raw-text-only placeholders. Explicit `Assumption:` markers now become source-spanned `AssumptionObject`s with `Assumption`/`AssumptionText`/`AssumptionFor` facts, same-item evidence links via `AssumptionEvidence`, and `assumption-has-explicit-evidence` Pass/Unknown checks plus exported `MissingAssumptionEvidence` blocking questions when evidence is absent. Explicit `Invariant:` markers now become source-spanned proposition objects with `Invariant`/`InvariantText`/`InvariantFor` facts, same-item evidence links via `InvariantEvidence`, and `invariant-has-explicit-evidence` Pass/Unknown checks plus exported `MissingInvariantEvidence` blocking questions when evidence is absent. Explicit `Constraint:` markers now become source-spanned obligation objects with `Constraint`/`ConstraintText`/`ConstraintFor` facts, same-item evidence links via `ConstraintEvidence`, and `constraint-has-explicit-evidence` Pass/Unknown checks plus exported `MissingConstraintEvidence` blocking questions when evidence is absent. Explicit `Risk:` and `Mitigation:` markers now create source-spanned review objects with `Risk`/`RiskText`/`RiskFor` and `RiskMitigation`/`RiskMitigationText`/`MitigatesRiskFor` facts, same-item mitigation links via `RiskMitigatedBy`, and `risk-has-explicit-mitigation` Pass/Unknown checks plus exported `MissingRiskMitigation` blocking questions when mitigation/control evidence is absent. Explicit `Rationale:` markers now become source-spanned explanation objects with `Rationale`/`RationaleText`/`RationaleFor` facts, `rationale-has-source-provenance` Pass checks, and PeTTa reified export support, preserving design reasons without treating them as executable semantics. Process reviewability now also accepts script/config/build artifact-only declarations such as `scripts/deploy.sh` and `Makefile` as concrete process evidence, and resource reviewability accepts direct artifact-path-only declarations such as `docs/capacity.v1.yaml` and `infra/limits.toml`, without relaxing TODO/raw-text-only refusal behavior. A first v0.2 security/privacy slice now detects secrets, PII/personal data, access/auth/role boundaries, and destructive-action wording, emitting Unknown checks plus `MissingSecurityPrivacyEvidence` blocking questions when handling evidence is absent and exporting supported review/question atoms through the PeTTa profile. It now also requires explicit data/sensitivity classification evidence for PII/personal-data specs via `privacy-data-classification-declared`, encryption-scope/transport/key-management evidence via `privacy-encryption-scope-reviewed`, lawful-basis/consent evidence via `privacy-lawful-basis-reviewed`, retention/deletion/minimization evidence via `privacy-retention-deletion-reviewed`, purpose-limitation/use-limitation/secondary-use-review evidence via `privacy-purpose-limitation-reviewed`, data-subject/access/correction/portability/opt-out/privacy-rights evidence via `privacy-data-subject-rights-reviewed`, identity/authentication evidence for rights/access/deletion/erasure requests via `privacy-rights-request-authentication-reviewed`, access audit/logging/monitoring evidence via `privacy-pii-access-audit-reviewed` when PII appears with access/admin/role wording, incident-response/breach-notification evidence via `privacy-incident-response-reviewed`, data-residency/cross-border transfer policy evidence via `privacy-data-residency-reviewed` when PII appears with region/country/jurisdiction/cross-border wording, third-party/vendor/processor sharing evidence via `privacy-third-party-sharing-reviewed` when PII appears with vendor/processor/partner/external-service/export/upload/share wording, and privilege-escalation review evidence for access/auth/admin/role specs via `security-privilege-escalation-reviewed`, authentication/session-management evidence via `security-session-management-reviewed` when login/auth/session wording appears, authentication/API abuse-protection evidence via `security-auth-abuse-protection-reviewed` when auth/login/API/password/token wording appears, API authorization/scope evidence via `security-api-authorization-reviewed` when API/endpoint/request wording appears with auth/access context, authentication/API transport-protection evidence via `security-auth-transport-protection-reviewed` when auth/login/API/password/token wording appears, credential rotation/expiry/revocation evidence via `security-credential-rotation-reviewed` when secrets/tokens/passwords/credentials appear, API/webhook input-validation evidence via `security-api-input-validation-reviewed` when request/payload/body/query/parameter/JSON/form/upload wording appears with API/webhook context, webhook/callback request-authenticity plus replay-protection evidence via `security-webhook-request-authenticity-reviewed` when webhook/callback/external-request wording appears, and safe generic/redacted/sanitized API/webhook error-response evidence via `security-api-error-disclosure-reviewed` when API/webhook error/exception/stack-trace/debug/diagnostic wording appears, defaulting to Unknown blocking questions when absent. The next step is deeper Appendix N/P methodology/security semantics, broader information-flow/temporal availability checks, and richer profile-aware projection beyond the current scaffold predicates/source manifest. A dependency depth / critical path length detection check now computes the longest path in the acyclic DataFlowEdge graph and flags deep dependency chains (>= 4 edges) for review. A bottleneck node detection check now flags components that are both high fan-in and high fan-out (>= 3 in each dimension), emitting `information-flow-bottleneck-node-reviewed` obligations with Unknown blocking questions when unacknowledged. The PeTTa reified profile now also exports an `information-flow-graph-summary` atom with quick-triage graph stats (node count, edge count, temporal edge count, source/sink counts, cycle count, connected component count, max depth, bottleneck count) computed from DataFlowEdge and TemporalOrderEdge facts. A bidirectional edge review check now detects when A→B and B→A both exist in the DataFlowEdge graph, emitting `information-flow-bidirectional-edge-reviewed` obligations (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional wording, Unknown with blocking questions when unacknowledged). A Phase 3 process/resource/dependency marker slice now detects explicit `Process:`, `Resource:`, and `Dependency:`/`Dependencies:` annotations, emits source-spanned `ProcessObject`/`ResourceObject` atoms with `Process`/`ProcessText`/`ProcessFor`, `Resource`/`ResourceText`/`ResourceFor`, and `Dependency`/`DependencyText`/`DependencyFor` facts, passes concrete operational/capacity/service/API/file/package/dataset/artifact evidence via `process-definition-reviewable`/`resource-requirement-reviewable`/`dependency-requirement-reviewable`, and turns TODO/vague placeholders into Unknown checks plus `MissingProcessDefinition`/`MissingResourceRequirement`/`MissingDependencyDetail` blocking questions rather than inventing operational semantics. Witness/backend-artifact marker parsing has also been tightened to stop before following same-item semantic markers such as `Outcome:` while preserving file paths with periods, keeping exact-span witness atoms separate from adjacent proposition atoms; concrete witness recognition now treats `.yaml`, `.yml`, and `.sh` operational artifacts as reviewable evidence rather than missing-witness placeholders. Evidence, rationale, interpretation, scope/context, confidence, epistemic-status, process, and resource marker parsing now use the same boundary discipline, so file-path/test-selector/artifact references such as `tests/test_cli.py::CliTests`, `docs/v01-profile.md`, `out/semantic-map.metta`, `docs/v0.2.review.md`, `scripts/demo.sh`, and `docs/capacity.v1.yaml`, plus percent confidences such as `83%`, are preserved while adjacent semantic markers keep separate exact spans.

A first v0.2 information-flow validation slice now detects data-flow/dependency wording (inputs, outputs, consumes, produces, reads, writes, sends, receives, pipelines, upstream/downstream) and emits conservative obligations for input declaration, output declaration, dependency-direction declaration, temporal-availability review, and circular-dependency termination review; missing evidence becomes `MissingInformationFlowEvidence` blocking questions and supported PeTTa atoms. It also extracts explicit component-level data-path edges ("X reads from Y", "X writes to Y", "X consumes from Y", "X receives ... from Y", "X pulls ... from Y", "X ingests ... from Y", "X pushes ... to Y", "X emits ... to Y", "X feeds into Y", "X depends on Y") as `DataFlowEdge` atoms with exact matched edge-phrase source spans and an `information-flow-data-path-declared` obligation that passes when edges are found and produces Unknown blocking questions when only vague wording exists. Duplicate/parallel declarations of the same normalized edge now emit `information-flow-duplicate-edge-reviewed` (Pass when absent or acknowledged, Unknown with blocking questions when unacknowledged). Direct self-loop edges now get a dedicated `information-flow-self-dependency-reviewed` obligation before broader graph-cycle review, producing Unknown blocking questions for unacknowledged component→same-component dependencies and Pass when recursion/feedback/fixed-point wording acknowledges intent. Transitive dependency chain detection builds an adjacency graph from extracted edges, detects A→B→C chains via bounded BFS, and emits `information-flow-transitive-dependency-reviewed` obligations (Pass when acknowledged, Unknown with blocking questions when not). Graph-based cycle detection via DFS white/gray/black coloring finds actual cycles in the extracted edge graph and emits `information-flow-cycle-detected` obligations (Pass when acyclic, Unknown with blocking questions when cycles exist). Fan-out/fan-in concentration detection computes per-node out-degree and in-degree from extracted edges and triggers `information-flow-fan-out-reviewed` and `information-flow-fan-in-reviewed` obligations when any component has >=3 edges in one direction (Pass when acknowledged or below threshold, Unknown with blocking questions when unacknowledged). Source/sink identification finds source nodes (no incoming edges) and sink nodes (no outgoing edges) and emits `information-flow-source-sink-identified` obligations (Pass when both exist, Unknown with blocking questions when missing). BFS-based source reachability checks whether all nodes are reachable from source nodes and emits `information-flow-reachability-reviewed` obligations (Pass when all reachable, Unknown with blocking questions when unreachable nodes exist); reverse-BFS sink reachability checks whether all nodes can reach at least one sink and emits `information-flow-sink-reachability-reviewed` obligations (Pass when all nodes have a sink path, Unknown with blocking questions for trapped cycles/dead ends/missing outputs). Isolated component detection finds components mentioned with broader data-flow verbs (`flows to`, `provides to`, `gets from`, `pulls from`, `pushes to`) that do not produce explicit DataFlowEdge atoms, and emits `information-flow-isolated-component-reviewed` obligations (Pass when all mentioned components appear in edges, Unknown with blocking questions when isolated components are found). Redundant path detection finds all simple paths between node pairs in the edge graph and, when multiple distinct paths (direct + indirect) connect the same pair, emits `information-flow-redundant-path-reviewed` obligations (Pass when no redundant paths or spec acknowledges redundancy via 'redundant'/'backup'/'fallback'/'failover'/'fault tolerance'/'high availability'/'duplicate'/'resilient'/'replicated' wording, Unknown with blocking questions when unacknowledged). Temporal ordering impossibility detection extracts explicit "A before/after/then/precedes/follows B" statements from spec text, builds a temporal ordering graph, detects impossible cycles via DFS, emits exact-source-spanned `TemporalOrderEdge` atoms and `information-flow-temporal-impossibility-reviewed` obligations (Fail on impossible cycles, Pass when consistent or no temporal statements) with blocking questions.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| design context | `https://github.com/bgoertzel-sing/hyperseed-formalizations` | `projects/hyperseed-formalizations/repos/hyperseed-formalizations` | `agent/protomegatron-formalization-0002` | contains notes 0005/0006; no changes made by this task |
| Plain2Metta public implementation | public `https://github.com/bgoertzel-sing/plain2metta` | `projects/specatom-hs/repos/specatom-hs` | default `main`; launch branch `agent/plain2metta-public-launch` | repository renamed/published 2026-07-15; internal package/IR remains `specatom_hs`; draft PR #2 updates default-branch branding and carries current conservative compiler work through `351bad1` |

## Environments

- Workspace: `/home/openclaw/research-agent`.
- No paid compute approved.
- No compiler implementation environment exists yet.
- PeTTa/SWI-Prolog runtime may later reuse the local PeTTa/SWI stack already validated for `petta-chem`, but the first SpecAtom-HS compiler prototype can be host-language based.

## Key results

- 2026-07-15: Closed a PeTTa fact-predicate type fail-open: non-string predicate values are now refused before schema lookup instead of being stringified into potentially supported predicate names; exact reified/executable ground-truth tests pass; 312 tests pass.
- 2026-07-14: Closed an executable-skeleton identity fail-open by refusing empty object IDs and empty object-reference targets explicitly; added direct and referenced ground-truth tests; 293 tests pass.
- 2026-07-13: Made arbitrary-depth executable-reference refusal selection globally canonical across mixed-depth branches by traversing complete reference paths in lexicographic order; added ground truth where an `alpha` deep RawTextOnly path competes with a shallower `zeta` path; 290 tests pass.
- 2026-07-13: Made direct executable-skeleton refusal record ordering deterministic across originating fact insertion order by canonically sorting candidate facts; added reversed-order two-target RawTextOnly ground truth; 289 tests pass.
- 2026-07-13: Made arbitrary-depth executable-reference refusal selection deterministic across fact insertion order by canonically sorting descendant references before traversal; added reversed-order deep-path ground truth; 288 tests pass.
- 2026-07-13: Locked executable-skeleton refusal precedence across direct and one-to-three-edge references: unsupported semantic levels such as `TemplateParsed` remain the reported cause even when the target also lacks source provenance; added a parameterized ground-truth regression; 286 tests pass.
- 2026-07-11: Added explicit `Axiom:` marker support with exact source spans, same-item Evidence/Proof support links, Unknown missing-justification obligations, `MissingAxiomJustification` blocking questions, PeTTa export coverage, and 266 passing tests.
- 2026-07-11: Added explicit `Hypothesis:` proposition markers with exact source spans, same-item evidence links, Pass/Unknown evidence obligations, `MissingHypothesisEvidence` blocking questions, PeTTa export coverage, and 258 passing tests.
- 2026-07-11: Added explicit `Precondition:` / `Postcondition:` formal condition markers with exact source spans, same-item evidence links, Pass/Unknown evidence obligations, `MissingPreconditionEvidence` / `MissingPostconditionEvidence` blocking questions, PeTTa export coverage, and 255 passing tests.
- 2026-07-10: Added explicit `Metric:` validation markers with source-spanned measurable criteria, Pass/Unknown `metric-definition-reviewable` checks, `MissingMetricDefinition` blocking questions, PeTTa export coverage, and 251 passing tests.
- 2026-07-10: Added explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` validation markers with source-spanned review criteria, Pass/Unknown `acceptance-criterion-reviewable` checks, `MissingAcceptanceCriterionDetail` blocking questions, PeTTa export coverage, and 245 passing tests.
- 2026-07-10: Added explicit `Priority:` review markers with source-spanned priority values, Pass/Unknown `priority-value-reviewable` checks, `UnsupportedPriorityValue` blocking questions, PeTTa export coverage, and 241 passing tests.
- 2026-07-10: Added explicit `Owner:` / `Assignee:` accountability markers with Pass/Unknown owner-assignment review, `MissingOwnerAssignment` blocking questions, PeTTa export coverage, and 239 passing tests.
- 2026-06-29: Created project notebook and source-plan summary at `projects/specatom-hs/docs/source-summary.md`.
- 2026-06-29: Created local-only Python stdlib MVP in `projects/specatom-hs/repos/specatom-hs`; 5 unit tests pass and two examples generate JSON/MeTTa-ish outputs.
- 2026-07-15: With Ben's explicit approval, renamed the existing remote to
  `bgoertzel-sing/plain2metta`, made it public, updated the description and
  README branding, pushed `agent/plain2metta-public-launch`, and opened draft
  PR #2. A tracked-tree secret-like scan found no matches; the MIT license and
  `specatom_hs` internal package name are retained.
- 2026-06-30: Added conservative `specatom_hs` concept-table pass with `ConceptObject`/`ConceptStatus`, external-link recognition, unresolved-question records, and `concept-reference-resolved` validation checks; 14 unit tests pass.
- 2026-06-30: Added exact-span `ConceptReferenceObject` occurrence atoms for definitions/references/external markers and occurrence-targeted validation checks; 15 unit tests pass.
- 2026-06-30: Added `specatom_hs.source_indexer` support for multi-line bullet continuations that extend source spans/raw text without swallowing nested bullets; 16 unit tests pass.
- 2026-06-30: Added conservative concept grammar aliases (`[def:]`, `[ref:]`, `[concept:]`) plus bare definition/glossary bullets and raw-text-to-source span alignment; 17 unit tests pass.
- 2026-06-30: Added shallow requirement/test coverage pass plus PeTTa reified export of supported object facts and validation records; 19 unit tests pass.
- 2026-07-01: Added scaffold fact-arity and declared-reference validation with regression tests for good facts, malformed arity, and dangling references; 21 unit tests pass.
- 2026-07-01: Tightened `petta_reified_v0` profile filtering so unsupported/malformed object facts produce backend refusals instead of exported atoms, and validation rationales/evidence are preserved in the reified projection; 23 unit tests pass.
- 2026-07-01: Added Unknown-to-question handling for unsupported object-fact predicates, emitting `QuestionObject` records that block the relevant profile/arity obligation; 24 unit tests pass.
- 2026-07-01: Added validation-layer self-checks for check records (`check-links-known-obligation`, `check-target-matches-obligation`) with malformed-diagnostic regression coverage; 25 unit tests pass.
- 2026-07-01: Added validation-obligation provenance/target self-checks (`obligation-has-source-provenance`, `obligation-target-is-declared`) with malformed-obligation regression coverage; 28 unit tests pass.
- 2026-07-01: Added PeTTa source provenance manifest export with exact source/index atoms and ground-truth regression coverage; 26 unit tests pass.
- 2026-07-01: Tightened concept occurrence spans to preserve exact marker line numbers for references found on multi-line bullet continuations; 27 unit tests pass.
- 2026-07-01: Added PeTTa reified-profile semantic-level validation with blocking questions for unsupported levels such as `RawTextOnly`; 29 unit tests pass.
- 2026-07-01: Added explicit requirement coverage labels (`[id:...]` / `[covers:...]`) with `RequirementLabel`/`CoverageClaim` export and Unknown questions for unresolved coverage targets; 31 unit tests pass.
- 2026-07-01: Added duplicate requirement-label ambiguity handling so explicit coverage claims require exactly one target label; 32 unit tests pass.
- 2026-07-01: Added orphan acceptance-test coverage obligations/questions and `OrphanAcceptanceTest` profile export; 33 unit tests pass.
- 2026-07-01: Added object-scoped fact subject validation plus PeTTa subject-mismatch refusals; 33 unit tests pass.
- 2026-07-02: Made explicit requirement coverage labels document-scoped so `[covers:...]` can resolve forward to later requirement sections; 34 unit tests pass.
- 2026-07-02: Added validation-layer status self-checks (`check-status-is-known`) so malformed check records with non-declared statuses fail crisply before backend export; PeTTa check export now preserves malformed status text without crashing; 34 unit tests pass.
- 2026-07-02: Added validation-layer evidence self-checks (`check-has-evidence`) so empty diagnostic evidence fails crisply before backend export; 34 unit tests pass.
- 2026-07-02: Added source-span byte/line self-validation (`source-span-within-file-bounds`, `source-span-lines-match-byte-offsets`) so malformed indexed spans fail crisply before backend export; 35 unit tests pass.
- 2026-07-02: Added Plain file digest self-validation (`plain-file-digest-matches-content`) so corrupted source manifests fail crisply before source-span/backend export review; 36 unit tests pass.
- 2026-07-02: Added section/item PlainFile link validation (`section-file-is-indexed`, `section-has-source-span`, `item-file-is-indexed`) so malformed source-index records fail before backend provenance export; 37 unit tests pass.
- 2026-07-02: Tightened source-index provenance consistency with section/item/span file-ID cross-checks (`section-span-file-matches-section-file`, `item-file-matches-section-file`, `item-span-file-matches-item-file`); 37 unit tests pass.
- 2026-07-02: Added CLI/demo tooling for SpecAtom-HS JSON, grouped PeTTa `.metta`, and Markdown diagnostics reports; added an `auth_service.plain` fixture that surfaces duplicate coverage labels, unresolved coverage targets, unresolved concepts, and backend refusals as reviewable questions; optimized validation record de-duplication by stable IDs; 46 unit tests pass.
- 2026-07-02: Added question-object blocker validation: unresolved concept questions now carry `Blocks` links to their exact Unknown obligations, and `QuestionObject` records self-check for non-empty review text plus known blocked obligations; 47 unit tests pass.
- 2026-07-02: Added first v0.2 ML/time-series methodology validator slice (`ml-evaluation-metric-declared`, `ml-horizon-or-frequency-declared`, `ml-reproducibility-evidence-declared`, `ml-preprocessing-fit-scope-declared`) with `MLTimeSeriesExperiment`/`MissingMethodologyEvidence` atoms and blocking questions; 49 unit tests pass.
- 2026-07-02: Extended the ML/time-series methodology slice with `ml-baseline-comparison-declared` and `ml-uncertainty-reporting-declared` obligations, MissingMethodologyEvidence questions, and regression coverage in the existing methodology tests; 49 unit tests pass.
- 2026-07-02: Added explicit preprocess-then-split leakage review via `ml-preprocessing-order-reviewed` obligations/questions; 50 unit tests pass.
- 2026-07-03: Added explicit future/label-as-feature leakage review via `ml-future-label-leakage-reviewed` obligations/questions; 51 unit tests pass.
- 2026-07-03: Added conservative ML metric/task appropriateness review via `ml-metric-task-appropriateness-reviewed`; forecast/regression-like specs with classification-style metrics now produce Unknown blocking questions unless classification-task wording is present; 52 unit tests pass.
- 2026-07-03: Added conservative ML temporal split-order review via `ml-temporal-split-order-reviewed`; random/shuffled time-series split wording without chronological/walk-forward/out-of-time evidence now produces Unknown blocking questions; 54 unit tests pass.
- 2026-07-03: Added conservative named baseline/uncertainty review via `ml-baseline-comparator-named` and `ml-uncertainty-method-named`; generic `baseline`/`uncertainty` mentions now pass declaration checks but produce Unknown blocking questions until a concrete comparator/method is named; 55 unit tests pass.
- 2026-07-03: Added conservative prediction-time feature availability review via `ml-feature-availability-reviewed`; ML/time-series specs with declared features/inputs/predictors/covariates now produce Unknown blocking questions unless availability is described as prediction-time, point-in-time/as-of, lagged, historical, or equivalent; 57 unit tests pass.
- 2026-07-03: Added first conservative security/privacy obligation scaffolding (`security-secrets-handling-reviewed`, `privacy-pii-handling-reviewed`, `security-access-boundary-declared`, `security-destructive-action-safety-reviewed`) with `SecurityPrivacyReview`/`MissingSecurityPrivacyEvidence` export and blocking questions for missing evidence; 59 unit tests pass.
- 2026-07-03: Deepened the security/privacy slice with `security-secret-log-exposure-reviewed`, requiring secret/token/password specs to state redaction/masking/no-logging evidence or produce Unknown blocking questions; 59 unit tests pass.
- 2026-07-03: Added `privacy-data-classification-declared` to require explicit data/sensitivity classification evidence for PII/personal-data specs, with Unknown blocking questions when absent; 59 unit tests pass.
- 2026-07-03: Added `security-privilege-escalation-reviewed` to require access/auth/admin/role specs to state least-privilege, approval, audit, admin-only, or self-grant-prevention evidence; 59 unit tests pass.
- 2026-07-03: Added `privacy-retention-deletion-reviewed` to require PII/personal-data specs to state retention, deletion/erasure, expiry, or minimization evidence; 60 unit tests pass.
- 2026-07-03: Added `privacy-data-residency-reviewed` to require data-residency/cross-border transfer policy evidence when PII/personal-data specs mention regions, countries, jurisdictions, residency, or cross-border context; 61 unit tests pass.
- 2026-07-03: Added `privacy-third-party-sharing-reviewed` to require DPA/vendor-review/data-sharing policy evidence when PII/personal-data specs mention vendors, processors, partners, external services, exports, uploads, or sharing; 62 unit tests pass.
- 2026-07-04: Added `privacy-lawful-basis-reviewed` to require consent, lawful/legal basis, contract, legal-obligation, legitimate-interest, or similar evidence for PII/personal-data specs; 63 unit tests pass.
- 2026-07-04: Added `privacy-purpose-limitation-reviewed` to require purpose limitation, use limitation, specific-purpose, or secondary-use-review evidence for PII/personal-data specs; 64 unit tests pass.
- 2026-07-04: Added `privacy-pii-access-audit-reviewed` to require access audit/logging/monitoring evidence when PII/personal-data specs also mention access/admin/role wording; 67 unit tests pass.
- 2026-07-04: Added `privacy-incident-response-reviewed` to require incident-response, breach-notification, or escalation evidence for PII/personal-data specs; 68 unit tests pass.
- 2026-07-04: Added `privacy-encryption-scope-reviewed` to require encryption-at-rest, transport-encryption, field/database encryption, key-management, KMS, key-rotation, or equivalent scope evidence for PII/personal-data specs; 69 unit tests pass.
- 2026-07-04: Added `security-session-management-reviewed` to require MFA, session timeout/expiry, revocation/logout, refresh-token rotation, or reauthentication evidence when auth/login/session wording appears; 70 unit tests pass.
- 2026-07-04: Added `ml-feature-freshness-reviewed` to require freshness, staleness, latency, update-cadence, data-age, or as-of timestamp evidence when ML/time-series specs mention real-time/live/current/latest/recent/fresh features or inputs; 72 unit tests pass.
- 2026-07-04: Added `security-auth-abuse-protection-reviewed` to require rate limiting, throttling, brute-force protection, lockouts, abuse detection, bot detection, or CAPTCHA evidence when auth/login/API/password/token wording appears; 73 unit tests pass.
- 2026-07-04: Added `security-credential-rotation-reviewed` to require rotation, expiry, or revocation evidence when secrets/tokens/passwords/credentials appear; 74 unit tests pass.
- 2026-07-04: Added `security-auth-transport-protection-reviewed` to require TLS, HTTPS, mTLS, certificate-pinning, transport-encryption, or secure-channel evidence when auth/login/API/password/token wording appears; 75 unit tests pass.
- 2026-07-05: Added `security-api-authorization-reviewed` to require authorization, permission/scope, RBAC/access-control, deny-by-default, or policy-enforcement evidence when API/endpoint/request wording appears with auth/access context; 76 unit tests pass.
- 2026-07-05: Added `security-webhook-request-authenticity-reviewed` to require HMAC/signature verification, webhook secrets, timestamp windows, nonces, idempotency keys, or replay-protection evidence when webhook/callback/external-request wording appears; 77 unit tests pass.
- 2026-07-05: Added `security-api-input-validation-reviewed` to require schema/input/payload/parameter validation, sanitization, allow-listing, type checks, or bounds checks when API/webhook request input wording appears; 78 unit tests pass.
- 2026-07-05: Added `security-api-error-disclosure-reviewed` to require generic/redacted/sanitized/opaque/correlation-ID-style error-response evidence when API/webhook error, exception, stack-trace, traceback, debug, or diagnostic response wording appears; 79 unit tests pass.
- 2026-07-05: Added first v0.2 information-flow validation slice (`information-flow-inputs-declared`, `information-flow-outputs-declared`, `information-flow-dependency-direction-declared`, `information-flow-temporal-availability-reviewed`, `information-flow-circular-dependency-reviewed`) with `InformationFlowReview`/`MissingInformationFlowEvidence` atoms and blocking questions; 88 unit tests pass.
- 2026-07-05: Added component-level data-path edge extraction: `DataFlowEdge` atoms for explicit "X reads from Y" / "X writes to Y" / "X consumes from Y" / "X depends on Y" patterns, `information-flow-data-path-declared` obligation (Pass with edges, Unknown with only vague wording), `DataFlowEdge` fact schema for PeTTa export, and regression tests comparing extracted edges to ground truth; 93 unit tests pass.
- 2026-07-05: Added graph-based cycle detection from extracted DataFlowEdge atoms: builds directed adjacency graph, detects cycles via DFS white/gray/black coloring, emits `information-flow-cycle-detected` obligation (Pass when acyclic, Unknown with blocking question when cycles exist); 100 unit tests pass.
- 2026-07-05: Added fan-out/fan-in concentration detection from extracted DataFlowEdge atoms: computes per-node out-degree and in-degree, triggers review when any component has >=3 edges in one direction, emits `information-flow-fan-out-reviewed` and `information-flow-fan-in-reviewed` obligations (Pass when acknowledged or below threshold, Unknown with blocking question when unacknowledged); 107 unit tests pass.
- 2026-07-05: Added source/sink identification and reachability analysis from extracted DataFlowEdge atoms: identifies source nodes (no incoming edges) and sink nodes (no outgoing edges), emits `information-flow-source-sink-identified` obligation (Pass when both exist, Unknown with blocking question when missing), and BFS-based reachability check emitting `information-flow-reachability-reviewed` obligation (Pass when all nodes reachable from sources, Unknown with blocking question when unreachable nodes exist); 113 unit tests pass.
- 2026-07-05: Added isolated component detection from broader data-flow verbs: components mentioned with non-edge verbs like `receives data from`, `feeds into`, `flows to`, `provides to`, `gets from`, `pulls from`, `pushes to` that don't produce DataFlowEdge atoms trigger `information-flow-isolated-component-reviewed` obligation (Pass when all mentioned components appear in edges, Unknown with blocking question when isolated components are found); 117 unit tests pass.
- 2026-07-06: Added redundant path detection from extracted DataFlowEdge atoms: finds all simple paths between node pairs, detects when multiple distinct paths (direct + indirect) connect the same pair, emits `information-flow-redundant-path-reviewed` obligation (Pass when no redundant paths or spec acknowledges redundancy via 'redundant'/'backup'/'fallback'/'failover'/'fault tolerance'/'high availability'/'duplicate'/'resilient'/'replicated' wording, Unknown with blocking question when unacknowledged); 122 unit tests pass.
- 2026-07-06: Added temporal ordering impossibility detection: extracts explicit "A before/after/then/precedes/follows B" statements from spec text, builds a temporal ordering graph, detects impossible cycles via DFS white/gray/black coloring, emits `TemporalOrderEdge` atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements), blocking `QuestionObject`s, and PeTTa reified profile export; 131 unit tests pass.
- 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B (reads from / writes to / depends on) but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent), blocking questions, and PeTTa reified profile export; 135 unit tests pass.
- 2026-07-06: Added dependency depth / critical path length detection from extracted DataFlowEdge atoms: computes longest path in the acyclic graph via topological sort + DP, emits `information-flow-dependency-depth-reviewed` obligation (Pass when depth < 4 or acknowledged via 'deep'/'multi-layer'/'multi-hop'/'long chain'/'critical path'/'layered'/'pipeline depth' wording, Unknown with blocking question when deep and unacknowledged), 6 regression tests; 141 unit tests pass.
- 2026-07-06: Added bidirectional edge review to information-flow validation: detects A→B and B→A pairs in the DataFlowEdge graph, emits `information-flow-bidirectional-edge-reviewed` obligation (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional/two-way/mutual/round-trip wording, Unknown with blocking question when unacknowledged); 5 regression tests; 178 tests pass.
- 2026-07-07: Added duplicate/parallel edge review to information-flow validation: repeated declarations of the same normalized DataFlowEdge emit `information-flow-duplicate-edge-reviewed` (Pass when absent or acknowledged, Unknown with blocking question when unacknowledged) and export through PeTTa reified validation atoms; 3 regression tests; 186 tests pass.
- 2026-07-07: Tightened Phase 2 semantic-object source-span alignment for repeated same-item markers and continuation-line markers, with regression tests comparing generated `Evidence:` spans to ground truth; 191 tests pass; local commit `c018b74`.
- 2026-07-07: Broadened Phase 2 `Bridge:` parsing so arbitrary unsupported ontology labels (for example `OpenCog.AtomSpace`) still produce reviewable `BridgeObject`s, Unknown checks, and `UnsupportedBridgeOntology` blocking questions instead of being silently ignored; 192 tests pass; local commit `b23cc36`.
- 2026-07-07: Added explicit Phase 2 `Confidence:` marker support: percent/decimal confidence annotations normalize to `ConfidenceValue` atoms and pass only when in `[0,1]`; out-of-range values become Unknown `confidence-value-in-unit-interval` checks with `UnsupportedConfidenceValue` blocking questions; 194 tests pass; local commit `7b7aedb`.
- 2026-07-08: Added explicit Phase 3 `Witness:` / `Artifact:` / `Backend artifact:` marker support with source-spanned `BackendArtifact` witness atoms, concrete-artifact validation, TODO/raw-text-only Unknown blocking questions, PeTTa export coverage, and 199 passing tests; local commit `a838ba7`.
- 2026-07-08: Added explicit `Question:` marker support with source-spanned `QuestionObject` atoms, `explicit-question-needs-answer` Unknown checks, PeTTa export coverage, and 202 passing tests.
- 2026-07-08: Added explicit Phase 3 `Process:` and `Resource:` marker support with source-spanned `ProcessObject`/`ResourceObject` atoms, concrete process/resource validation, TODO/vague placeholder Unknown blocking questions, PeTTa export coverage, and 201 passing tests; local commit `09a5134`.
- 2026-07-09: Tightened `Evidence:` marker boundary parsing so file-path/test evidence with periods stops before following same-item semantic markers while preserving exact evidence/outcome spans and PeTTa export; 217 tests pass.
- 2026-07-09: Tightened `Rationale:` marker boundary parsing so file-path/artifact rationale text with periods stops before following same-item semantic markers while preserving exact rationale/evidence spans and PeTTa export; 218 tests pass.
- 2026-07-09: Tightened `Interpretation:` marker boundary parsing so file-path/artifact interpretation text with periods stops before following same-item semantic markers while preserving exact interpretation/bridge spans and PeTTa export; 219 tests pass.
- 2026-07-09: Tightened `Process:` and `Resource:` marker boundary parsing so period-bearing operational/artifact references stop before following same-item markers without truncating file paths; 222 tests pass.
- 2026-07-09: Broadened `Resource:` concrete artifact recognition so direct artifact-path-only declarations such as `docs/capacity.v1.yaml` and `infra/limits.toml` satisfy `resource-requirement-reviewable` with exact source spans and PeTTa export while placeholders remain Unknown; 228 tests pass.
- 2026-07-10: Added explicit `NonGoal:` / `Non-goal:` marker support: source-spanned exclusion objects with `NonGoal`/`NonGoalText`/`NonGoalFor`/`SourceItem` facts, Pass `non-goal-has-source-provenance` checks, marker-boundary handling before following `Evidence:` clauses, PeTTa reified export coverage, and 231 passing tests.
- 2026-07-07: Added conservative Phase 2 bridge relation validation: `bridge-relation-conservative` passes only for graded correspondence labels and turns identity/equivalence-style labels such as `identical` into Unknown checks plus `UnsupportedBridgeRelation` blocking questions; 195 tests pass; local commit `6c5e2df`.
- 2026-07-07: Tightened `Confidence:` markers so non-numeric scales such as `Confidence: high` become source-spanned confidence objects with `confidence-value-in-unit-interval` Unknown checks and `UnsupportedConfidenceValue` blocking questions instead of being silently ignored; 196 tests pass; local commit `565a348`.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `receives ... from` wording with `receives-from` normalization and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `pulls ... from` / `pushes ... to` wording with `pulls-from` / `pushes-to` normalization, information-flow signal coverage, and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `ingests ... from` / `emits ... to` wording with `ingests-from` / `emits-to` normalization, information-flow signal/declaration coverage, and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Tightened TemporalOrderEdge provenance from whole-item spans to exact matched ordering phrase spans while preserving `edge-has-item-level-source-provenance` validation; source-slice ground-truth regression added; 186 tests pass.
- 2026-07-06: Added sink-reachability review to information-flow validation: reverse BFS from sink nodes detects components/cycles that are source-reachable but cannot reach any output sink, emits `information-flow-sink-reachability-reviewed` obligations with Unknown blocking questions for trapped cycles/dead ends/missing outputs; 2 direct regression tests plus export/no-edge coverage; 180 tests pass.
- 2026-07-06: Added `information-flow-graph-summary` atom to PeTTa reified export with node/edge/temporal-edge/source/sink/cycle/component/max-depth/bottleneck counts computed from DataFlowEdge/TemporalOrderEdge facts; 4 ground-truth tests; 174 tests pass.
- 2026-07-06: Added connected-components detection to the information-flow validation slice: undirected BFS finds disconnected subgraphs, emits `information-flow-connected-components-reviewed` obligation (Pass when acknowledged as independent/separate/standalone, Unknown with blocking question otherwise); 3 regression tests; 170 tests pass.
- 2026-07-06: Fixed O(n^2) validator deduplication bottleneck: replaced linear-scan with O(1) set-based lookups in `add_validation_obligation` and `add_check`; auth_service compile time dropped from >17s to 0.14s.
- 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export with Pass/Fail/Unknown check counts and QuestionObject count; added 18-test end-to-end ground-truth test suite for `auth_service.plain` fixture; 159 tests pass.
- 2026-07-06: Added bottleneck node detection (high fan-in AND high fan-out cross-dimension check): emits `information-flow-bottleneck-node-reviewed` obligation; 5 regression tests; 67 information-flow tests pass.
- 2026-07-06: Added temporal ordering impossibility detection: extracts explicit "A before/after/then/precedes/follows B" statements, builds temporal ordering graph, detects impossible cycles via DFS, emits TemporalOrderEdge atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements); 131 tests pass.
- 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent); 4 regression tests; 135 tests pass.
- 2026-07-06: Added dependency depth / critical path length detection from extracted DataFlowEdge atoms: computes longest path via topological sort + DP, emits `information-flow-dependency-depth-reviewed` obligation (Pass when depth < 4 or acknowledged, Unknown with blocking question when deep and unacknowledged); 6 regression tests; 141 tests pass.
- 2026-07-06: Added per-edge source provenance for DataFlowEdge and TemporalOrderEdge: edges now carry the source span of the specific indexed item where the edge was found; `edge-has-item-level-source-provenance` validation; 167 tests pass.
- 2026-07-06: Added redundant path detection from extracted DataFlowEdge atoms: detects when multiple distinct paths connect the same pair, emits `information-flow-redundant-path-reviewed` obligation (Pass when no redundant paths or spec acknowledges redundancy, Unknown with blocking question when unacknowledged); 122 tests pass.
- 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export: emits Pass/Fail/Unknown check counts and QuestionObject count for quick downstream triage; added comprehensive end-to-end ground-truth test suite for `auth_service.plain` fixture (18 tests) covering source provenance, concepts, requirements/coverage labels, duplicate label detection, orphan acceptance tests, unresolved concepts, validation summary counts, reified export structure, backend refusals, and grouped `.metta` section separators; 159 unit tests pass.

## Open questions

- Which Plain grammar source should be treated as authoritative for the MVP parser?
- Should the first target emit pure PeTTa-readable `.metta`, JSON plus `.metta`, or both from the start?
- How much of SUMO/EXPO should be hand-seeded as bridge tables versus linked as external ontology references?
- Which validation domain should be implemented first after generic structural checks: time-series ML methodology, process/resource discipline, or security/privacy obligations?

## Related projects and concepts

- `hyperseed-formalizations`: design notes 0005 and 0006, plus broader Hyperseed formalization work.
- `petta-memory`: p-bit/PLN-ready atom storage patterns may be reusable for SpecAtom-HS journals or memory views.
- `petta-chem`: computational-experiment records can later be represented through the EXPO/Hyperseed validation facet.
- SUMO typed MeTTa bridge and EXPO experiment ontology PDFs uploaded by Benjamin on 2026-06-29.
- OSLF, TyLA, Curry-Howard, MeTTa-IL, Rholang, PeTTa.

- 2026-07-11: Executable-skeleton gating now requires nonblank source provenance in addition to a safe semantic level and fact profile; 270 tests pass.
- 2026-07-13: Executable-reference refusal diagnostics now select unsafe profile facts and immediate transitive targets canonically rather than depending on fact insertion order; reversed-fact-order ground truth added; 287 tests pass.

## Risks

- **False semantic precision:** shallow English extraction may look more formal than it is. Mitigation: semantic levels, interpretation evidence, questions, and TODO witnesses.
- **Ontology overbuild:** importing too much SUMO/EXPO/Hyperseed can stall the MVP. Mitigation: bridge tables with graded correspondences and small curated slices.
- **Backend capture:** PeTTa details could distort the IR. Mitigation: target profiles and reified facts before executable skeletons.
- **Validation theater:** checks might produce superficial pass/fail labels. Mitigation: every check needs provenance, status, evidence, and counterexample/question when relevant.
- **Security/codegen risk:** never generate positive operational code from negative/security obligations or raw text alone.

## 2026-06-29 implementation update

Created local-only prototype repo `projects/specatom-hs/repos/specatom-hs` (no remote). Implemented a Python stdlib MVP for Appendix H / recommended early phases:

- source indexer with SHA-256 file digests, deterministic IDs, and byte/line `SourceSpan` atoms;
- Plain-like parser for `***section***` headings and nested bullet items;
- SpecAtom-HS subset emitter for source atoms, concepts, requirements, propositions/claims, obligations, shallow action templates, acceptance tests, undefined predicate questions, context/TV assertions, and validation checks;
- JSON and MeTTa-ish S-expression output;
- Appendix G compact task-manager fixture and Appendix O compact ML time-series fixture;
- crisp validator checks for exactly-one primary role, source/generated provenance, obligation propositions, and assertion context/TV.

Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 5 tests. Example generation commands for `examples/task_manager.plain` and `examples/ml_timeseries.plain` succeeded.

## 2026-06-29 scaffold update

Added the PDF-recommended minimal `specatom_hs` package alongside the earlier `plain_to_metta` MVP. It includes source indexing with file/section/item/source spans, first-class validation obligations/check records, a conservative pass registry, and PeTTa backend gates that refuse RawTextOnly/unsupported executable skeleton generation while allowing only safe reified atom stubs. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 12 tests.
