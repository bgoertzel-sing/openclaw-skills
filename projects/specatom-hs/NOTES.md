# Working Notes

## 2026-07-20 backend-safe CheckRecord status diagnostics

- Tightened `check-status-is-known` evidence so `None`, string aliases such as
  `"Pass"`, and container values report their exact unsupported value and type,
  matching the PeTTa backend's declared-enum refusal gate.
- Declared `CheckStatus` values retain explicit normalized Pass evidence.
- Exact malformed/valid neighboring-record ground truth prevents a runtime
  string alias from looking like a declared enum member in crisp diagnostics.

Verification: focused validation-record suite passed 43 tests; full stdlib
unittest discovery passed 373 tests in 241.425 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `a8e9372`; unpushed.

## 2026-07-20 19:30 PDT - Check target validation aligned with export

The validation layer now emits `check-has-safe-target` for every original
CheckRecord. It deterministically rejects non-string and blank targets before
the PeTTa backend gate, while preserving an explicit Pass for non-blank string
targets. Regression and full-suite evidence are recorded in `TASKS.md`; code
commit: `da432ff`.

## 2026-07-20 15:30 PDT - Backend-safe CheckRecord obligation links

Added `check-has-safe-obligation-id` validation before obligation resolution.
`None`, list-valued, and blank obligation identities now produce deterministic
Fail evidence rather than reaching unsafe dictionary membership; a valid
non-blank string link Passes. The focused regression passed, full unittest
discovery passed all 370 tests in 167.117 seconds, and `git diff --check`
passed. Local implementation commit `7a73b32`; no paid compute or remote
mutation was used.

## 2026-07-20 13:30 PDT - Validation-obligation target safety

Added an explicit `validation-obligation-has-safe-target` crisp obligation.
It mirrors the PeTTa export gate: non-string (including container and `None`)
and blank targets Fail deterministically, while non-blank strings Pass. This
keeps malformed target identity separate from the existing declared-target
resolution check. The focused regression, full unittest suite, and
`git diff --check` passed.

## 2026-07-19 23:30 PDT - Backend-safe Section and PlainItem identities

- Added `section-has-safe-identity` and `item-has-safe-identity` obligations.
- Section/item uniqueness indexes and fact-validation item indexes now admit
  only non-blank string IDs, preventing malformed list IDs from reaching
  `Counter`, set, or dictionary operations.
- Exact regression covers list-valued IDs, blank IDs, and valid neighboring
  IDs. `PYTHONPATH=src python3 -m unittest tests.test_specatom_validation_records
  -v` passed 32 tests; full discovery passed 362 tests; `git diff --check`
  passed. Local implementation commit: `4fa1853`.

## 2026-07-19 backend-safe SourceSpan identity validation

- Added `source-span-has-safe-identity` obligations requiring non-blank string
  identities, parallel to PlainFile and backend identity gates.
- Span uniqueness and canonical lookup indexes now admit only safe string IDs;
  validation-obligation provenance and edge-provenance lookup also refuse
  unhashable span IDs without crashing.
- Exact regression coverage exercises list-valued, blank, and valid neighboring
  SourceSpan identities.

Verification: focused validation-record suite passed 31 tests; full stdlib
unittest discovery passed 361 tests in 62.627 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local implementation commit `440399b`;
unpushed.

## 2026-07-19 17:30 PDT - backend-safe validation-record identities

- Added `validation-obligation-has-safe-identity` and
  `check-has-safe-identity` crisp obligations.
- Non-string and whitespace-only identities now produce exact Fail evidence;
  valid non-blank string identities produce Pass evidence.
- This separates malformed identity shape from duplicate identity diagnostics
  and aligns validation with the PeTTa exporter's existing refusal reasons.

Verification: `PYTHONPATH=src python3 -m unittest
tests.test_specatom_validation_records -v` passed 29 tests;
`PYTHONPATH=src python3 -m unittest discover -s tests -q` passed 359 tests;
`git diff --check` passed. Local implementation commit `386ff29`. No paid
compute or remote writes.

## 2026-07-19 13:30 PDT - unhashable object identity validation

- Filtered validation identity indexes to backend-safe, non-blank strings and
  made malformed non-string obligation targets fail without hash membership.
- Exact list-valued object-ID ground truth proves deterministic Fail evidence
  replaces the prior crash.
- Verification: focused validation-record suite passed 27 tests; full unittest
  discovery passed 357 tests; `git diff --check` passed. Local implementation
  commit: `81fda0f`.

## 2026-07-19 11:30 PDT - backend-safe object identity validation

- Added a first-class `object-has-safe-identity` obligation for every
  SpecObject. Crisp validation now fails non-string and whitespace-only IDs
  with deterministic type/value evidence, matching existing PeTTa reified and
  executable-skeleton refusal behavior.
- Exact regression coverage asserts Fail for integer and blank IDs and Pass for
  a neighboring valid string ID.
- Verification: focused validation-record suite passed 26 tests; full stdlib
  unittest discovery passed 356 tests; `git diff --check` passed. No paid
  compute, remote mutation, or secrets/access/security changes. Local
  implementation commit: `a9fe38f`.

## 2026-07-19 unhashable semantic-level validation refusal

- Both crisp semantic-level checks now require a declared `SemanticLevel`
  before testing profile membership.
- A malformed structured value such as `["UnsupportedLevel"]` yields a Fail
  `object-has-known-semantic-level` check plus the existing Unknown profile
  refusal/question instead of raising `TypeError`.
- Exact regression coverage pins the malformed-value evidence.

Verification: focused validation-record suite passed 25 tests; full stdlib
unittest discovery and `git diff --check` passed. No paid compute, remote
writes, push/merge/force-push/delete, or secrets/access/security changes. Local
commit `747efdf`; unpushed.

## 2026-07-19 07:30 PDT - Unsupported object roles fail crisp validation

The PeTTa reified backend already refused non-enum SpecObject roles, but crisp
validation had no matching schema obligation. Added `object-has-known-role` so
an injected role such as `UnsupportedRole` produces one deterministic Fail
record with exact evidence before export. The focused 24-test validation suite
and full 354-test stdlib discovery pass; `git diff --check` passes. No paid
compute, remote mutation, or secrets/access/security changes.
Local implementation commit: `1bafb57`.

## 2026-07-19 05:30 PDT - Unsupported semantic levels produce diagnostics

An injected non-enum semantic-level value exposed two validator crash paths:
the crisp known-level check and the PeTTA reified-profile refusal/question
builder both dereferenced `.value` before returning diagnostics. Both paths now
use enum values only for genuine `SemanticLevel` members and preserve an exact
`repr` for unsupported values. The malformed object receives a deterministic
Fail `object-has-known-semantic-level` check plus the existing conservative
Unknown profile refusal/question. Focused 23-test validation suite and full
353-test stdlib discovery pass; `git diff --check` passes. No paid compute,
remote mutation, or secrets/access/security changes. Local implementation
commit: `e408cf1`.

## 2026-07-19 01:30 PDT - Duplicate SpecObject identities fail crisp validation

The reified and executable PeTTa gates already refuse duplicate SpecObject IDs,
but `validate_document` did not expose the ambiguity as a first-class check.
Added `object-identity-is-unique`, keyed once per identity, with deterministic
Pass evidence for unique objects and exact `ambiguous duplicate object=... count=...`
Fail evidence for duplicates. The focused regression passed; the complete
stdlib suite passed all 351 tests; `git diff --check` passed. No paid compute,
remote writes, or security/access changes. Local implementation commit:
`2fcf5ee`.

## 2026-07-18 21:30 PDT - Parent-item validation aligned with export refusal

The PeTTa backend already suppressed missing, refused, self-referential,
cross-file, and cross-section parent links, but `validate_document` did not
surface equivalent crisp obligations. Added `item-parent-is-indexed`,
`item-parent-is-not-self`, and `item-parent-context-matches` checks for every
nested item. Parent lookup uses only uniquely indexed item identities, so a
duplicate parent ID fails closed with its exact occurrence count rather than
selecting an arbitrary record. Regression ground truth covers duplicate,
missing, self, and cross-context parents. Focused 19-test validation suite,
full 349-test suite, and `git diff --check` pass. Implementation commit:
`4fbbe89`.

## 2026-07-18 19:30 PDT - Duplicate section/item identities fail closed

The source validator now emits explicit uniqueness obligations for indexed
Section and PlainItem IDs. Because ordinary structural obligations are keyed by
property and target ID, duplicate target identities previously collapsed into
one record and could look valid. Regression coverage constructs two sections
and two items with repeated identities and requires one Fail check per identity
class with exact `ambiguous duplicate ... count=2` evidence. Narrow validation
tests and the full 348-test suite pass; `git diff --check` passes. Implementation
commit: `00a41c8` in `projects/specatom-hs/repos/specatom-hs`.

## 2026-07-18 duplicate indexed-span membership refusal

- `section-has-source-span` and `item-has-source-span` now treat an indexed
  source-span identity as known only when it occurs exactly once.
- Duplicate span IDs produce Fail checks with deterministic ID/count evidence,
  aligning membership checks with the existing fail-closed span/file checks.
- Extended the conflicting-duplicate regression to pin all four section/item
  span membership and file-consistency checks.

Verification: corrected focused regression passed; full stdlib unittest
discovery completed with all 347 tests passing; `git diff --check` passed. The
initial focused selector named a nonexistent test class and failed before test
execution; it was corrected to `ValidationRecordTests`. No paid compute, remote
writes, push/merge/force-push/delete, or secrets/access/security changes.
Local implementation commit `7ad549b`; unpushed.

## 2026-07-18 13:30 PDT - Duplicate indexed-section validation refusal

- Replaced last-write-wins section lookup with a unique-ID-only map in crisp item provenance validation.
- Duplicate section IDs now make both `item-has-section` and `item-file-matches-section-file` Fail with exact `ambiguous duplicate section=... count=...` evidence, even when the last duplicate would match the item's file.
- Checks: focused validation-record suite passed 16 tests; full suite passed 346 tests; `git diff --check` passed. Local implementation-repo commit: `8fe7bc1`; unpushed. No paid compute or remote/security mutation.

## 2026-07-18 09:30 PDT - Canonical item-span validation regression

- Added `test_item_file_validation_uses_canonical_indexed_span`, symmetric with the existing section regression.
- The fixture gives the embedded item span and indexed span the same ID but different files and asserts exact Fail evidence from the indexed span.
- Checks: focused validation-record suite passed 14 tests; full suite passed 344 tests; `git diff --check` passed. Local implementation-repo commit: `dbc4c94`.

## 2026-07-18 canonical section-span file-link refusal

The PeTTa section gate previously tested `section.span.file_id` after using only `section.span.id` to link to the separately emitted source manifest. A runtime-corrupted section could therefore carry an embedded span claiming the section's file while the canonical admitted span with the same ID belonged to another file, producing a false cross-file `derived-from` atom. The gate now checks `emitted_spans[section.span.id].file_id`, and exact ground truth proves the section and provenance atom are suppressed with `section-span-file-mismatch`. Focused regression and full 342-test stdlib suite pass; `git diff --check` passes. Local commit `1da9671`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-18 dangling object/obligation provenance-link refusal

The PeTTa reified exporter previously checked the shape of SpecObject and validation-obligation source-span IDs but, in a document carrying a source manifest, could still emit `derived-from` links to a span that was absent or had been refused by an earlier file/span gate. It now checks non-empty provenance IDs against the actually emitted span map before adding those links. Exact ground truth covers absent spans, spans rejected through a malformed parent file, valid neighboring links, and genuinely absent optional provenance. Standalone object-only documents without a source manifest retain the existing projection behavior. The focused regression and full 340-test stdlib suite pass; `git diff --check` passes. Local commit: `dc00958`; no push or other remote mutation.

## 2026-07-17 malformed validation record-type refusal

The PeTTa reified exporter previously trusted every entry in `SpecDocument.validation_obligations` and `.checks` to be the declared dataclass type. Runtime-corrupted entries such as an integer obligation or dictionary check therefore raised during ID counting before the exporter could return a structured refusal. Export now filters these entries through explicit `unsupported-validation-obligation-record-type:*` and `unsupported-check-record-type:*` refusals, continues with valid neighboring records, and keeps malformed checks out of the document-validation summary. The focused 71-test profile suite and full 331-test stdlib suite pass; `git diff --check` passes. Local commit: `269b708`; no push or other remote mutation.

## 2026-07-16 malformed validation-check target refusal

The PeTTa reified exporter previously serialized runtime check target IDs without validating their schema type or content, so integer `7` could alias the legitimate string target `"7"` and blank targets could appear meaningful. Check targets must now be non-blank strings; malformed records produce explicit `unsupported-check-target-id-type:*` / `missing-check-target-id` refusals, emit no partial check atoms, and are excluded from document-validation summary counts. The focused 60-test profile suite and full 320-test stdlib suite pass; `git diff --check` passes. Local commit: `894a7b5`; no push or other remote mutation.

## 2026-07-16 malformed validation-check property refusal

The PeTTa reified exporter previously serialized runtime check properties without validating their schema type or content, so integer `7` could alias the legitimate string property `"7"` and blank properties could appear meaningful. Check properties must now be non-blank strings; malformed records produce explicit `unsupported-check-property-type:*` / `missing-check-property` refusals, emit no partial check atoms, and are excluded from document-validation summary counts. The focused 59-test profile suite and full 319-test stdlib suite pass; `git diff --check` passes. Local commit: `39eda2d`; no push or other remote mutation.

## 2026-07-15 validation-obligation provenance refusal

The PeTTa reified exporter previously applied the non-string source-span refusal gate to `SpecObject` provenance but not to `ValidationObligation` provenance. A malformed runtime obligation with `source_span_id=7` was therefore rendered as `(derived-from ... 7)`, creating an apparently valid but false provenance edge. The exporter now omits that edge and returns `unsupported-source-span-id-type:int-for-validation-obligation`. A focused regression test and the full stdlib suite pass (314 tests); `git diff --check` passes. Local commit: `e5ef724`; no push or other remote mutation.

## 2026-07-15 malformed semantic-level refusal

Concrete repo work in `repos/specatom-hs`:

- Added a diagnostic-safe semantic-level formatter so malformed runtime objects cannot crash refusal construction through an unchecked `.value` access.
- Both `petta_reified_v0` and `petta_executable_skeleton_v0` now reject string, `None`, and numeric pseudo-levels with explicit type-bearing refusals and do not emit the object's facts.
- Kept existing enum-level behavior intact, including the special `RawTextOnly` executable refusal and unsupported-but-valid enum refusals.

Verification: focused regression passed; PeTTa profile-gate suite passed 49 tests; full suite passed 309 tests in 40.549 seconds; `git diff --check` passed. Local commit `45b6b88`; no push or other remote mutation.

## 2026-07-14 validated semantic/profile checkpoint

- Reviewed the accumulated implementation diff in `repos/specatom-hs` against the project records and README, then ran the complete stdlib suite.
- The checkpoint combines conservative exact-spanned semantic markers and their validation questions with fail-closed PeTTa reified/executable gates, including arbitrary-depth reference safety and refusal of empty or `None` scalar/object-reference arguments.
- Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed all 299 tests; `git diff --check` passed.
- Created local commit `0007d99` (`Expand conservative semantic markers and profile refusals`) on `agent/specatom-phase2-semantic-objects`. No push or other remote mutation.

## 2026-07-14 profile-safe diamond reference ground truth

Concrete repo work in `repos/specatom-hs`:

- Added a positive executable-skeleton traversal regression for `coverage -> requirement -> {left artifact, right artifact} -> shared source`.
- The test proves path-local cycle detection accepts a valid profile-safe DAG with a shared descendant rather than conservatively but incorrectly treating the second path as a cycle.
- Existing RawTextOnly, dangling, ambiguous, profile-invalid, and real reference-cycle refusal regressions remain green.

Verification: focused regression passed; PeTTa profile-gate suite passed 31 tests; full suite passed 291 tests in 27.737 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 canonical mixed-depth executable-reference refusal

Concrete repo work in `repos/specatom-hs`:

- Replaced local depth-first unsafe-descendant selection with a lexicographically ordered complete-path frontier, so a deeper canonical `alpha` path is not masked by a shallower but lexically later `zeta` sibling.
- Preserved fail-closed checks for cycles, ambiguous/dangling references, unsafe semantic levels, missing provenance/facts, and invalid profile facts.
- Added mixed-depth ground truth for `coverage -> requirement -> artifact -> {alpha-leaf -> alpha-raw, zeta-raw}`, requiring the `alpha` RawTextOnly path.

Verification: four focused traversal/refusal tests passed; full suite passed with 290 tests in 24.332 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 deterministic originating executable-refusal ordering

Concrete repo work in `repos/specatom-hs`:

- Canonically sorted each executable candidate's own facts before profile/reference checks, so equivalent candidates emit direct refusal records in the same order regardless of fact insertion order.
- Added reversed-order ground truth for one lowered object referencing `alpha-target` and `zeta-target`, both `RawTextOnly`; both constructions now emit the `alpha` refusal before the `zeta` refusal.
- Updated the existing multi-target ground truth to match the canonical order.

Verification: focused regression and full profile-gate suite passed; full suite passed with 289 tests in 24.858 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 deterministic arbitrary-depth executable-reference refusal

Concrete repo work in `repos/specatom-hs`:

- Canonically sorted each traversed object's object-reference facts by target ID and predicate before depth-first traversal, so competing unsafe descendants produce the same path-bearing refusal regardless of fact insertion order.
- Preserved cycle detection and all existing fail-closed descendant checks while making the canonical smallest unsafe path win.
- Added reversed-order ground truth for `coverage -> requirement -> {alpha-artifact,zeta-artifact} -> RawTextOnly source`, expecting the same `alpha` deep refusal both ways.

Verification: focused regression and full profile-gate suite passed; full suite passed with 288 tests in 24.594 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 executable-reference semantic-level precedence at multiple depths

Concrete repo work in `repos/specatom-hs`:

- Added a parameterized ground-truth regression for direct, one-hop, and deeper executable-reference paths ending at an unprovenanced `TemplateParsed` object.
- The regression proves the gate reports the unsafe semantic level (`TemplateParsed`) rather than masking it as `MissingSourceProvenance`, consistently with the top-level refusal precedence.
- No production change was needed; the existing direct/transitive/deep gates already preserve the intended fail-closed diagnostic ordering.

Verification: focused regression passed; full suite passed with 286 tests in 23.640 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 executable skeleton semantic-level refusal precedence

Concrete repo work in `repos/specatom-hs`:

- Restored the executable gate's primary semantic-level diagnostics after source-provenance validation had begun masking `RawTextOnly` and unsupported-level refusals on objects with empty source span IDs.
- `RawTextOnly` still refuses as `raw-text-only-skeleton-forbidden`, and parsed/non-lowered levels still refuse as `unsupported-semantic-level-for-executable-skeleton`; missing provenance remains the refusal for otherwise executable-safe lowered/verified objects.
- Added a two-object ground-truth regression covering unprovenanced raw and template-parsed objects.

Verification: focused precedence/provenance tests passed; full suite passed with 285 tests in 23.694 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-13 executable skeleton one-hop descendant profile-safety refusal

Concrete repo work in `repos/specatom-hs`:

- Fixed an off-by-one depth condition in `refuse_executable_skeleton`: unsafe descendants exactly one edge below a directly referenced safe object were traversed but silently ignored, while deeper descendants were refused.
- Immediate descendants with missing source provenance, missing profile facts, profile-invalid facts, or duplicate/ambiguous IDs now produce the same path-bearing `unsafe-object-reference-deep-semantic-level` refusal as deeper descendants.
- Added a four-case ground-truth regression for `coverage -> requirement -> source`.

Verification: focused profile-gate tests passed; full suite passed with 284 tests in 22.752 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton deep profile-safety refusal

Concrete repo work in `repos/specatom-hs`:

- Closed an arbitrary-depth traversal gap where a deep descendant at an executable-safe semantic level could be silently skipped when it lacked source provenance, had no profile facts, or contained a profile-invalid fact.
- Added a three-case ground-truth regression for `coverage -> requirement -> artifact -> unsafe-target`, expecting explicit `MissingSourceProvenance`, `MissingProfileFacts`, and `UnsafeProfile:*` refusal details.

Verification: focused deep-reference regressions passed; full suite passed with 282 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton deep reference-cycle refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened deep safe-reference traversal so a descendant cycle is refused explicitly rather than treated as safe by silently skipping a target already in the current path.
- Added a three-object ground-truth regression for `coverage -> requirement -> artifact -> requirement`, expecting a `ReferenceCycle` refusal with the complete path.

Verification: focused regression passed; full suite passed with 281 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton deep dangling-reference refusal

Concrete repo work in `repos/specatom-hs`:

- Extended deep safe-reference traversal so an executable candidate is refused when a descendant reference chain terminates at an undeclared object, rather than only detecting dangling references at the direct or one-transitive-hop levels.
- Added a three-object ground-truth regression for `coverage -> requirement -> artifact -> missing-source`.

Verification: focused regression passed; full suite passed with 280 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton deep reference-chain refusal

Concrete repo work in `repos/specatom-hs`:

- Extended `refuse_executable_skeleton` beyond one transitive hop: a profile-valid reference now walks deeper safe reference chains and refuses lowering when any descendant reaches `RawTextOnly` or another executable-unsafe semantic level.
- Added a four-object ground-truth regression for `coverage -> requirement -> artifact -> raw-source`.

Verification: focused regression passed; full suite passed with 279 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton transitive semantic-level refusal

Concrete repo work in `repos/specatom-hs`:

- Extended `refuse_executable_skeleton` so references cannot lower through an apparently safe intermediate object whose own object-reference fact targets `RawTextOnly` or another executable-unsafe semantic level.
- Added a three-object ground-truth regression (`coverage -> requirement -> raw-source`) expecting explicit direct and transitive refusals.

Verification: focused regression passed; full suite passed with 278 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton transitive target-safety refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so profile-valid references cannot lower merely because their target has a safe semantic-level label.
- References to targets missing source provenance, missing profile facts, or containing profile-invalid facts now get explicit `unsafe-object-reference-*` refusals.
- Added a ground-truth regression covering all three target-safety failures while preserving the safe-reference case.

Verification: focused PeTTa gate tests passed; full suite passed with 276 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton duplicate-ID refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so duplicate object IDs cannot be silently collapsed during declared-reference resolution.
- Every duplicate object is refused with `duplicate-object-id-for-executable-skeleton`, and otherwise-safe facts that reference the duplicated ID are refused with `unsafe-profile-fact:ambiguous-object-reference:*`.
- Added a focused ground-truth regression covering both duplicate declarations and the ambiguous `Covers` target.

Verification: focused PeTTa gate tests passed; full suite passed with 275 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton unsafe-target refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so a profile-valid reference to a declared object is still refused when the target is `RawTextOnly` or otherwise outside executable-safe semantic levels.
- Added focused ground-truth regressions for a lowered `Covers` object targeting a raw-text requirement and for the corresponding safe lowered target.

Verification: focused PeTTa gate tests passed; full suite passed with 274 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton dangling-reference refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so profile-valid object-reference facts cannot lower when their referenced object is absent from the supplied object set.
- Added focused regressions for dangling `Covers` refusal and a declared-reference pass, with the latter also proving one-shot iterable inputs are handled safely.

Verification: focused PeTTa gate tests passed; full suite passed with 273 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 executable skeleton empty-fact refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so a source-provenanced `BackendLowered`/`Verified` object with no profile facts is refused rather than treated as executable-safe.
- Added a focused regression expecting `missing-profile-facts-for-executable-skeleton`, while preserving the profile-safe lowered-object case.

Verification: focused PeTTa gate tests passed; full suite passed with 271 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 executable skeleton source-provenance refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so even profile-safe `BackendLowered`/`Verified` objects are refused when `source_span_id` is empty or whitespace.
- Added a focused regression expecting `missing-source-provenance-for-executable-skeleton`, while preserving the safe lowered-object case.

Verification: focused PeTTa profile tests passed; full suite passed with 270 tests; `git diff --check` passed. Local changes are not pushed.

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-13 deterministic executable-reference refusals

Concrete repo work in `repos/specatom-hs`:

- Replaced first-match selection for unsafe facts and immediate transitive references with canonical minimum selection, so equivalent objects produce the same refusal reason when their fact order differs.
- Kept deep traversal behavior unchanged while making profile-invalid reason selection stable there too.
- Added a ground-truth regression that reverses two `GeneratedFrom` facts and expects the same `alpha-source` transitive semantic-level refusal in both cases.

Verification: focused profile-gate tests passed; full suite passed with 287 tests in 24.005 seconds; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 executable skeleton fact-profile refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `refuse_executable_skeleton` so a `BackendLowered` or `Verified` semantic-level label no longer bypasses fact-profile validation.
- Executable lowering now refuses unknown predicates, malformed fact arity, and object-fact subject mismatches with explicit `unsafe-profile-fact:*` reasons.
- Added ground-truth tests for all three unsafe cases and a profile-safe lowered object.

Verification: focused PeTTa profile tests passed; full suite passed with 269 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 placeholder proof refusal for axiom support

Concrete repo work in `repos/specatom-hs`:

- Fixed a conservative-validation bug where any same-item `Proof:` marker, including `Proof: TODO prove later`, was added as `AxiomEvidence` and caused an axiom justification Pass.
- Only proof markers that pass the concrete proof artifact/procedure gate now enter the same-item support index. Unsupported proof markers still export as reviewable objects with `MissingProofDetail`, while the axiom independently remains Unknown with `MissingAxiomJustification`.
- Added a regression comparing generated links/checks/questions to the expected safe-refusal ground truth.

Verification: targeted proof/axiom tests passed; full suite passed with 267 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 axiom marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Axiom:` marker support as a conservative source-spanned proposition/formalization facet with `Axiom`/`AxiomText`/`AxiomFor`/`SourceItem` facts.
- Axioms link to same-item explicit `Evidence:` or `Proof:` via `AxiomEvidence`; without same-item support they remain Unknown and emit `MissingAxiomJustification` blocking questions rather than being treated as justified assumptions or verified semantics.
- Extended semantic marker boundary handling, fact schemas, README support surface, and PeTTa reified export coverage with regressions for proof-supported and missing-justification cases.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_axiom_marker_links_same_item_proof_and_exports tests.test_specatom_semantic_objects.SemanticObjectTests.test_axiom_without_justification_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted axiom tests passed; semantic-object suite passed; full suite passed with 266 tests; `git diff --check` passed. Local changes are not pushed.


## 2026-07-11 claim marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Claim:` marker support as a conservative source-spanned proposition facet with `Claim`/`ClaimText`/`ClaimFor`/`SourceItem` facts.
- Claims link to same-item explicit `Evidence:` via `ClaimEvidence`; without same-item evidence they stay Unknown and emit `MissingClaimEvidence` blocking questions rather than being treated as supported assertions.
- Extended semantic marker boundary handling, fact schemas, README support surface, and PeTTa reified export coverage with regressions for evidenced and missing-evidence cases.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_claim_marker_links_same_item_evidence_and_exports tests.test_specatom_semantic_objects.SemanticObjectTests.test_claim_without_evidence_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted claim tests passed; semantic-object suite passed with 76 tests; full suite passed with 262 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 counterexample marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Counterexample:` marker support as a conservative source-spanned validation facet with `Counterexample`/`CounterexampleText`/`CounterexampleFor`/`SourceItem` facts.
- Counterexamples now get Pass `counterexample-has-source-provenance` checks so falsification examples are preserved for review without automatically rejecting, proving, or executing any claim.
- Extended semantic marker boundary handling, fact schemas, README support surface, and PeTTa reified export coverage with a regression proving `Counterexample:` stops before following same-item `Evidence:`.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_counterexample_marker_becomes_source_spanned_validation_object -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted counterexample test passed; semantic-object suite passed with 74 tests; full suite passed with 260 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 hypothesis marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Hypothesis:` marker support as a conservative source-spanned proposition facet with `Hypothesis`/`HypothesisText`/`HypothesisFor`/`SourceItem` facts.
- Hypotheses link to same-item explicit `Evidence:` via `HypothesisEvidence`; without same-item evidence they remain Unknown and emit `MissingHypothesisEvidence` blocking questions rather than being treated as supported claims.
- Extended semantic marker boundary handling, fact schemas, README support surface, and PeTTa reified export coverage with regressions for evidenced and missing-evidence cases.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_hypothesis_marker_links_same_item_evidence_and_exports tests.test_specatom_semantic_objects.SemanticObjectTests.test_hypothesis_without_evidence_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted hypothesis tests passed; semantic-object suite passed with 72 tests; full suite passed with 258 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 verification marker alias support

Concrete repo work in `repos/specatom-hs`:

- Added `Verification:` as an explicit alias for validation-procedure markers, sharing the conservative `Validation`/`ValidationText`/`ValidationFor`/`SourceItem` fact shape used by `Validation:` and `Check:`.
- Extended semantic marker lookahead so `Verification:` spans stop cleanly before following same-item markers such as `Evidence:` while preserving exact source-span extraction.
- Added regression coverage proving reviewable verification procedures pass `validation-marker-reviewable`, export through PeTTa reified atoms, and do not create backend refusals.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_verification_marker_alias_preserves_exact_span_before_evidence tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_validation_marker_exports_reviewable_check_procedure tests.test_specatom_semantic_objects.SemanticObjectTests.test_validation_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted validation/verification tests passed; semantic-object suite passed with 70 tests; full suite passed with 256 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 precondition/postcondition marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Precondition:` / `Postcondition:` marker support as conservative formal-condition facets: source-spanned obligation/proposition objects with `Precondition`/`PreconditionText`/`PreconditionFor` and `Postcondition`/`PostconditionText`/`PostconditionFor`/`SourceItem` facts.
- Conditions link to same-item explicit `Evidence:` via `PreconditionEvidence` / `PostconditionEvidence`; without same-item evidence they stay Unknown and create `MissingPreconditionEvidence` / `MissingPostconditionEvidence` blocking questions.
- Extended semantic marker boundary handling so condition spans stop before adjacent markers, and added PeTTa reified profile schema/export coverage plus regressions for evidenced and missing-evidence cases.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_precondition_and_postcondition_markers_link_same_item_evidence tests.test_specatom_semantic_objects.SemanticObjectTests.test_precondition_and_postcondition_without_evidence_become_blocking_questions -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted pre/postcondition marker tests passed; semantic-object suite passed with 69 tests; full suite passed with 255 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 validation/check marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Validation:` / `Check:` marker support as a conservative validation-procedure facet: source-spanned validation objects with `Validation`/`ValidationText`/`ValidationFor`/`SourceItem` facts.
- Validation/check markers now emit `validation-marker-reviewable` checks: concrete tests, golden/ground-truth comparisons, fixtures, audits, diagnostics, schemas, linters/typechecks, benchmarks, or review procedures pass, while TODO/TBD/raw-text-only/validate-later placeholders remain Unknown and create `MissingValidationDetail` blocking questions.
- Added shared marker-boundary handling so validation spans stop before following same-item markers such as `Evidence:`, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder validation procedures.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_validation_marker_exports_reviewable_check_procedure tests.test_specatom_semantic_objects.SemanticObjectTests.test_validation_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted validation/check marker tests passed; semantic-object suite passed with 67 tests; full suite passed with 253 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 metric marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Metric:` marker support as a conservative validation facet: source-spanned metric objects with `Metric`/`MetricText`/`MetricFor`/`SourceItem` facts.
- Metric markers now emit `metric-definition-reviewable` checks: concrete named metrics, thresholds, units, and measurable criteria pass, while TODO/TBD/unknown/raw-text-only/placeholder values remain Unknown and create `MissingMetricDefinition` blocking questions.
- Added shared marker-boundary handling so metric spans stop before following same-item markers, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder metrics.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_metric_marker_exports_reviewable_validation_criterion tests.test_specatom_semantic_objects.SemanticObjectTests.test_metric_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted metric tests passed; semantic-object suite passed with 65 tests; full suite passed with 251 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 citation/reference marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Citation:` / `Reference:` marker support as conservative source-spanned evidence/reference facets with `Citation`/`CitationText`/`CitationFor`/`SourceItem` facts.
- Citation/reference markers now emit `citation-reference-reviewable` checks: concrete DOI/arXiv/URL/ISBN/PMID/bibliography/file-path references pass, while TODO/TBD/unknown/raw-text-only/placeholder/citation-needed values remain Unknown and create `MissingCitationReference` blocking questions.
- Added shared marker-boundary handling so citation spans stop before following same-item markers, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder references.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_citation_marker_exports_reviewable_reference tests.test_specatom_semantic_objects.SemanticObjectTests.test_citation_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted citation/reference tests passed; semantic-object suite passed with 63 tests; full suite passed with 249 tests; `git diff --check` passed. Local changes are not pushed.


## 2026-07-10 example marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Example:` marker support as a conservative review facet: source-spanned example/review objects with `Example`/`ExampleText`/`ExampleFor`/`SourceItem` facts.
- Example markers now emit `example-detail-reviewable` checks: concrete illustrative text passes as reviewable source-preserved example material, while TODO/TBD/unknown/none/unclear/raw-text-only/placeholder values remain Unknown and create `MissingExampleDetail` blocking questions.
- Added shared marker-boundary support so example spans stop before following same-item markers, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder examples.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_example_marker_exports_reviewable_source_spanned_example tests.test_specatom_semantic_objects.SemanticObjectTests.test_example_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted example tests passed; semantic-object suite passed with 61 tests; full suite passed with 247 tests; `git diff --check` passed. Local changes are not pushed.


## 2026-07-10 acceptance-criterion marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` marker support as a conservative validation facet: source-spanned validation objects with `AcceptanceCriterion`/`AcceptanceCriterionText`/`AcceptanceCriterionFor`/`SourceItem` facts.
- Acceptance criteria now emit `acceptance-criterion-reviewable` checks: concrete criteria pass as reviewable source-preserved criteria, while TODO/TBD/unknown/none/unclear/raw-text-only/placeholder values remain Unknown and create `MissingAcceptanceCriterionDetail` blocking questions.
- Added shared marker-boundary support so acceptance-criterion spans stop before following same-item markers, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder criteria.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_acceptance_criterion_marker_exports_reviewable_criterion tests.test_specatom_semantic_objects.SemanticObjectTests.test_acceptance_criterion_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted acceptance-criterion tests passed; semantic-object suite passed with 59 tests; full suite passed with 245 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 deadline/due marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Deadline:` / `Due:` marker support as a conservative review facet: source-spanned validation objects with `Deadline`/`DeadlineText`/`DeadlineValue`/`DeadlineFor`/`SourceItem` facts.
- Deadline markers now emit `deadline-value-reviewable` checks: concrete dates (`YYYY-MM-DD`, slash dates, month-name dates), `Qn YYYY` / `Hn YYYY`, and bounded relative intervals pass; TODO/TBD/unknown/none/unclear/someday/eventually/ASAP/raw-text-only placeholders remain Unknown and create `UnsupportedDeadlineValue` blocking questions.
- Added shared marker-boundary support so deadline spans stop before following same-item markers, plus PeTTa reified profile schema/export coverage and regressions for reviewable and placeholder deadlines.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_deadline_marker_exports_reviewable_value tests.test_specatom_semantic_objects.SemanticObjectTests.test_deadline_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted deadline tests passed; semantic-object suite passed with 57 tests; full suite passed with 243 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 priority marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Priority:` marker support as a conservative review facet: source-spanned validation objects with `Priority`/`PriorityText`/`PriorityValue`/`PriorityFor`/`SourceItem` facts.
- Priority markers now emit `priority-value-reviewable` checks: supported values (`blocker`, `critical`, `high`, `medium`, `low`, `P0`-`P3`) pass after normalization, while TODO/TBD/unknown/raw-text-only or unsupported values remain Unknown and create `UnsupportedPriorityValue` blocking questions.
- Added marker-boundary handling before following markers such as `Owner:`, PeTTa reified profile support, and regression coverage for reviewable and placeholder priorities.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_priority_marker_exports_reviewable_value tests.test_specatom_semantic_objects.SemanticObjectTests.test_priority_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted priority tests passed; semantic-object suite passed with 55 tests; full suite passed with 241 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 owner/assignee marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Owner:` / `Assignee:` marker support as a conservative accountability/review facet: source-spanned validation objects with `Owner`/`OwnerText`/`OwnerFor`/`SourceItem` facts.
- Owner markers now emit `owner-assignment-reviewable` checks: concrete person/team/group/review-body assignments pass, while TODO/TBD/unassigned/raw-text-only placeholders remain Unknown and create `MissingOwnerAssignment` blocking questions.
- Added PeTTa reified profile support and regression coverage for both reviewable owner assignments and missing-owner placeholders, including span boundaries before following `Evidence:` markers.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_owner_marker_exports_reviewable_assignment tests.test_specatom_semantic_objects.SemanticObjectTests.test_owner_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted owner tests passed; semantic-object suite passed with 53 tests; full suite passed with 239 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 deprecation/replacement marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Deprecated:` / `Deprecation:` marker support as a conservative Phase 3 review facet: source-spanned `Deprecated`/`DeprecatedText`/`DeprecatedFor`/`SourceItem` facts on validation objects.
- Added explicit `Replacement:` marker support with source-spanned `Replacement`/`ReplacementText`/`Replaces`/`SourceItem` facts; same-item replacements link back via `DeprecatedReplacedBy`.
- Deprecated markers now require a replacement/migration/sunset/removal disposition: linked replacements or disposition wording pass `deprecated-item-has-replacement-or-disposition`; otherwise the compiler emits an Unknown check plus a `MissingDeprecationDisposition` blocking question.
- Added PeTTa reified profile support and regression coverage for both unresolved deprecations and deprecations with same-item replacements.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_deprecated_marker_requires_replacement_or_disposition tests.test_specatom_semantic_objects.SemanticObjectTests.test_deprecated_marker_links_same_item_replacement -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted deprecation/replacement tests passed; semantic-object suite passed with 51 tests; full suite passed with 237 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 TODO marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `TODO:` / `To-do:` marker support as a conservative review/question facet: source-spanned `QuestionObject`s with `TodoItem`/`TodoText`/`TodoFor`/`QuestionText`/`SourceItem`/`Blocks` facts.
- TODO markers now get Unknown `todo-item-needs-resolution` checks, keeping incomplete implementation/spec work blocking and reviewable instead of treating TODO prose as ordinary text.
- The shared semantic-marker lookahead now stops TODO spans before following same-item markers such as `Evidence:` and `Open issue:`, and PeTTa reified export supports the new facts.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_todo_marker_becomes_blocking_question_and_preserves_boundary tests.test_specatom_semantic_objects.SemanticObjectTests.test_todo_marker_stops_before_open_issue_marker -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted TODO tests passed; semantic-object suite passed with 49 tests; full suite passed with 235 tests; `git diff --check` passed. Local changes are not pushed.


## 2026-07-10 open-issue marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Open issue:` / `Issue:` marker support as a conservative review/question facet: source-spanned `QuestionObject`s with `OpenIssue`/`OpenIssueText`/`IssueFor`/`QuestionText`/`SourceItem`/`Blocks` facts.
- Open issues now get Unknown `open-issue-needs-resolution` checks, keeping unresolved design/spec questions blocking and reviewable rather than silently treating issue prose as ordinary text.
- The shared semantic-marker lookahead now stops issue spans before following same-item markers such as `Evidence:` and `Question:`, and PeTTa reified export supports the new facts.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_open_issue_marker_becomes_blocking_question_and_preserves_boundary tests.test_specatom_semantic_objects.SemanticObjectTests.test_issue_marker_stops_before_question_marker -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted open-issue tests passed; semantic-object suite passed with 47 tests; full suite passed with 233 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 non-goal marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `NonGoal:` / `Non-goal:` marker support as a conservative Phase 3 scope/exclusion facet: source-spanned `NonGoal`/`NonGoalText`/`NonGoalFor`/`SourceItem` facts on validation objects.
- Non-goals now get a Pass `non-goal-has-source-provenance` check, preserving exclusions without turning them into executable behavior or creating spurious missing-evidence questions.
- The shared semantic-marker lookahead now stops `Non-goal:` spans before following same-item markers such as `Evidence:`, and PeTTa reified export supports the new facts.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_non_goal_marker_preserves_exclusion_without_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted non-goal test passed; semantic-object suite passed with 45 tests; full suite passed with 231 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-10 limitation marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Limitation:` marker support as a conservative Phase 3 review facet: source-spanned `Limitation`/`LimitationText`/`LimitationFor`/`SourceItem` facts on validation objects.
- Limitations now require a review disposition: same-item `Mitigation:` links produce `LimitationMitigatedBy` and Pass `limitation-has-review-disposition`; otherwise the compiler emits an Unknown check plus a `MissingLimitationDisposition` blocking question.
- Added PeTTa reified profile support for limitation/disposition facts and regression coverage for both mitigated and unresolved limitations.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_limitation_marker_requires_review_disposition tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_limitation_marker_links_same_item_mitigation -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted limitation tests passed; semantic-object suite passed with 44 tests; full suite passed with 230 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-09 resource artifact path recognition

Concrete repo work in `repos/specatom-hs`:

- Broadened explicit `Resource:` concrete requirement recognition to treat direct artifact paths such as `docs/capacity.v1.yaml` and `infra/limits.toml` as reviewable resource evidence even when the text does not also say `file`, `path`, or list numeric capacity.
- Added regression coverage for `Resource: docs/capacity.v1.yaml and infra/limits.toml`, checking exact source slices, Pass `resource-requirement-reviewable`, no `MissingResourceRequirement` question, and PeTTa reified export without profile refusal.
- This keeps artifact-only capacity/limits declarations reviewable while preserving TODO/raw-text-only placeholders as Unknown blocking questions.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_resource_marker_accepts_artifact_paths_without_resource_keyword -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted resource-artifact test passed; semantic-object suite passed with 42 tests; full suite passed with 228 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-09 extensionless build artifact recognition

Concrete repo work in `repos/specatom-hs`:

- Broadened explicit `Witness:` / `Artifact:` / `Backend artifact:` and `Dependency:` concrete artifact recognition to treat extensionless build entrypoints (`Dockerfile`, `Containerfile`, `Makefile`) as reviewable artifacts/dependencies.
- Added regression coverage for `Witness: Dockerfile and Makefile` and `Dependency: Dockerfile and Makefile`, checking exact source slices, Pass `witness-artifact-reviewable` / `dependency-requirement-reviewable`, no `MissingWitnessArtifact` / `MissingDependencyDetail` questions, and PeTTa reified export without profile refusal.
- This preserves safe refusal behavior for TODO/raw-text-only placeholders while avoiding false Unknowns for common repo build artifacts that lack file extensions.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_witness_marker_accepts_extensionless_build_artifacts tests.test_specatom_semantic_objects.SemanticObjectTests.test_dependency_marker_accepts_extensionless_build_artifacts -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted extensionless-artifact tests passed; semantic-object suite passed with 40 tests; full suite passed with 226 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-09 dependency artifact path extension

Concrete repo work in `repos/specatom-hs`:

- Broadened explicit `Dependency:` / `Dependencies:` concrete dependency recognition to treat `.sh`, `.toml`, and `.lock` artifact paths as reviewable concrete dependencies.
- Added regression coverage for `Dependency: scripts/bootstrap.sh and pyproject.toml. Outcome: ...`, checking exact dependency source slices, Pass `dependency-requirement-reviewable`, no `MissingDependencyDetail` question, and PeTTa reified export without dependency profile refusal.
- This complements the witness artifact extension by keeping operational scripts/config manifests reviewable while preserving TODO/raw-text-only dependency placeholders as Unknown blocking questions.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_dependency_marker_accepts_script_and_config_artifact_paths -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted dependency-artifact test passed; semantic-object suite passed with 38 tests; full suite passed with 224 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-09 witness artifact path extension

Concrete repo work in `repos/specatom-hs`:

- Broadened explicit `Witness:` / `Artifact:` / `Backend artifact:` concrete-artifact recognition to treat `.yaml`, `.yml`, and `.sh` paths as reviewable concrete artifacts.
- Added regression coverage for `Witness: scripts/demo.sh and docs/capacity.v1.yaml. Outcome: ...`, checking exact witness source slices, Pass `witness-artifact-reviewable`, no `MissingWitnessArtifact` question, and PeTTa reified export without witness profile refusal.
- This complements the same-day marker-boundary work by preserving operational artifact references while keeping TODO/raw-text-only witness placeholders as Unknown blocking questions.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_witness_marker_accepts_yaml_and_shell_artifact_paths -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted witness-artifact test passed; full suite passed with 223 tests; `git diff --check` passed. Local changes are not pushed.


## 2026-07-09 process/resource marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Process:` and `Resource:` marker parsing to use the shared semantic-marker lookahead instead of stopping at the first period/semicolon.
- This preserves period-bearing operational references such as `scripts/demo.sh`, `out/review.metta`, and `docs/capacity.v1.yaml` while still stopping before following same-item markers such as `Evidence:`.
- Reused the shared marker text trimming helper so source spans exclude sentence punctuation without truncating file/artifact paths.
- Added regression coverage comparing generated process/resource/evidence source slices to ground truth and checking PeTTa reified export has no Process/Resource profile refusal.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_process_and_resource_markers_preserve_file_paths_before_following_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted process/resource-boundary test passed; full suite passed with 222 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-09 epistemic-status marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Epistemic status:` / `Status:` marker parsing to use the shared semantic-marker lookahead instead of the previous broad status label regex.
- This prevents a supported label followed by another marker, such as `Epistemic status: verified. Evidence: docs/status.v1.md`, from being normalized as an unsupported combined status.
- Added regression coverage comparing generated epistemic/evidence source slices to ground truth and checking PeTTa reified export has no profile refusal for the status marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_epistemic_status_marker_stops_before_following_evidence_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted epistemic-boundary test passed; full suite passed with 221 tests; `git diff --check` passed. Local implementation commit: `8cd114e` (not pushed).

## 2026-07-09 scope/confidence marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Scope:` / `Context:` and `Confidence:` marker parsing to use the shared semantic-marker lookahead instead of stopping at the first period.
- This preserves scope/context references to files/MeTTa artifacts such as `docs/v0.2.review.md` and `out/profile-scope.metta`, while stopping before following same-item markers such as `Confidence:` / `Evidence:`.
- Confidence spans now preserve percent values such as `Confidence: 83%` without including the sentence period or swallowing following evidence markers.
- Added regression coverage comparing generated scope/confidence/evidence source slices to ground truth and checking PeTTa reified export has no profile refusal for either marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_scope_and_confidence_markers_preserve_periods_before_following_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted scope/confidence-boundary test passed; full suite passed with 220 tests; `git diff --check` passed.

## 2026-07-09 interpretation marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Interpretation:` marker parsing to use the shared semantic-marker lookahead instead of stopping at the first period.
- This preserves interpretation references to files/MeTTa artifacts such as `docs/interpretation.v1.md` and `out/semantic-map.metta`, while stopping before following same-item markers such as `Bridge:`.
- Added regression coverage comparing generated interpretation/bridge source slices to ground truth and checking PeTTa reified export has no profile refusal for either marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_interpretation_marker_preserves_file_path_before_following_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted interpretation-boundary test passed; full suite passed with 219 tests; `git diff --check` passed.

## 2026-07-09 rationale marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Rationale:` marker parsing to use the shared semantic-marker lookahead instead of stopping at the first period.
- This preserves rationale references to files/MeTTa artifacts such as `docs/v01-profile.md` and `out/design-note.metta`, while stopping before following same-item markers such as `Evidence:`.
- Added regression coverage comparing generated rationale/evidence source slices to ground truth and checking PeTTa reified export has no profile refusal for either marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_rationale_marker_preserves_file_path_before_following_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted rationale-boundary test passed; full suite passed with 218 tests; `git diff --check` passed.


## 2026-07-09 evidence marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Evidence:` marker parsing to use the shared semantic-marker lookahead instead of stopping at the first period.
- This preserves review evidence strings containing file paths/test selectors such as `tests/test_cli.py::CliTests` and `out/demo.metta`, while stopping before following same-item markers such as `Outcome:`.
- Added regression coverage comparing generated evidence/outcome source slices to ground truth and checking PeTTa reified export has no profile refusal for either marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_evidence_marker_preserves_file_path_before_following_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted evidence-boundary test passed; full suite passed with 217 tests; `git diff --check` passed.

## 2026-07-08 witness marker boundary tightening

Concrete repo work in `repos/specatom-hs`:

- Tightened explicit `Witness:` / `Artifact:` / `Backend artifact:` parsing to use the shared semantic-marker lookahead instead of consuming until newline/semicolon.
- This preserves concrete file/path witness strings containing periods, while stopping before following same-item markers such as `Outcome:` so witness and outcome atoms get separate exact source spans.
- Added regression coverage comparing the generated witness/outcome source slices to ground truth and checking PeTTa reified export has no profile refusal for either marker.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_witness_marker_stops_before_following_semantic_marker -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted witness-boundary test passed; full suite passed with 216 tests; `git diff --check` passed.

## 2026-07-08 explicit Dependency marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Dependency:` / `Dependencies:` marker parsing to the Phase 2/3 semantic-object pass.
- Dependency markers now create source-spanned resource/dependency objects with `Dependency`/`DependencyText`/`DependencyFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Outcome:`.
- Added `dependency-requirement-reviewable` validation: concrete services, APIs, files, packages, datasets, credentials, or artifacts pass; TODO/raw-text-only/vague placeholders become Unknown checks plus `MissingDependencyDetail` blocking questions.
- Added profile fact schemas so dependency atoms and missing-dependency questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (29 tests); full suite passed with 215 tests; `git diff --check` passed. Local implementation commit: `f710272` (not pushed).

## 2026-07-08 explicit Decision marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Decision:` marker parsing to the Phase 2/3 semantic-object pass.
- Decision markers now create source-spanned proposition objects with `Decision`/`DecisionText`/`DecidesFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Evidence:`.
- Added `decision-has-source-provenance` validation with Pass checks so design choices remain auditable source-backed propositions rather than inferred executable semantics.
- Added profile fact schemas so decision atoms export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_decision_marker_becomes_source_spanned_proposition -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted decision test passed; full suite passed with 212 tests; `git diff --check` passed. Local implementation commit: `df8cb83` (not pushed).

## 2026-07-08 explicit Rationale marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Rationale:` marker parsing to the Phase 2/3 semantic-object pass.
- Rationale markers now create source-spanned explanation objects with `Rationale`/`RationaleText`/`RationaleFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers.
- Added `rationale-has-source-provenance` validation with Pass checks so design reasons remain auditable source-backed explanations rather than inferred executable semantics.
- Added profile fact schemas so rationale atoms export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_rationale_marker_becomes_source_spanned_explanation -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted rationale test passed; full suite passed with 209 tests; `git diff --check` passed. Local implementation commit: `2514410` (not pushed).

## 2026-07-08 explicit Invariant marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Invariant:` marker parsing to the Phase 2/3 semantic-object pass.
- Invariant markers now create source-spanned proposition objects with `Invariant`/`InvariantText`/`InvariantFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Question:`.
- Added `invariant-has-explicit-evidence` validation: same-item `Evidence:` links produce Pass checks and `InvariantEvidence` facts; invariants without explicit evidence stay Unknown and create `MissingInvariantEvidence` blocking questions.
- Added profile fact schemas so invariants, invariant-evidence links, and missing-invariant questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (20 tests); full suite passed with 206 tests; `git diff --check` passed. Local implementation commit: `75b77a4` (not pushed).

## 2026-07-08 explicit Assumption marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Assumption:` marker parsing to the Phase 2/3 semantic-object pass.
- Assumption markers now create source-spanned `AssumptionObject`s with `Assumption`/`AssumptionText`/`AssumptionFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Question:`.
- Added `assumption-has-explicit-evidence` validation: same-item `Evidence:` links produce Pass checks and `AssumptionEvidence` facts; assumptions without explicit evidence stay Unknown and create `MissingAssumptionEvidence` blocking questions.
- Added profile fact schemas so assumptions, assumption-evidence links, and missing-assumption questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (18 tests); full suite passed with 204 tests; `git diff --check` passed. Local implementation commit: `30365db` (not pushed).

## 2026-07-08 explicit Question marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Question:` marker parsing to the Phase 2/3 semantic-object pass.
- These markers now create source-spanned `QuestionObject`s with `ExplicitQuestion`, `QuestionText`, `QuestionsObject`, `SourceItem`, and `Blocks` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Evidence:`.
- Added `explicit-question-needs-answer` validation obligations with Unknown checks so author-supplied review questions remain blocking, auditable items rather than ordinary prose.
- Added profile fact schemas so explicit questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (16 tests); full suite passed with 202 tests; `git diff --check` passed. Local implementation commit: `a510534` (not pushed).

## 2026-07-08 Phase 3 process/resource markers

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Process:` and `Resource:` marker parsing to the semantic-object pass.
- These markers create source-spanned `ProcessObject` and `ResourceObject` objects with `Process`/`ProcessText`/`ProcessFor` and `Resource`/`ResourceText`/`ResourceFor` facts, preserving exact source slices.
- Added `process-definition-reviewable` validation: concrete operational/procedural process wording (run, execute, validate, review, compile, build, deploy, schedule, cron, batch, pipeline, workflow, operator, approval, rollback, manual, automated) passes; TODO/vague placeholders become Unknown checks plus `MissingProcessDefinition` blocking questions.
- Added `resource-requirement-reviewable` validation: concrete capacity/budget/storage/service/credential/artifact resource wording (CPU, GB, MB, TB, hours, workers, nodes, replicas, budget, quota, memory, storage, disk, GPU, database, queue, cluster, service account, credential, secret, dataset, artifact, file, path) passes; TODO/vague placeholders become Unknown checks plus `MissingResourceRequirement` blocking questions.
- Added profile fact schemas so process/resource atoms and missing-process/missing-resource questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (15 tests); full suite passed with 201 tests; `git diff --check` passed. Local implementation commit: `09a5134` (not pushed).


## 2026-07-08 Phase 3 witness/backend-artifact markers

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Witness:`, `Artifact:`, and `Backend artifact:` marker parsing to the semantic-object pass.
- These markers now create source-spanned `BackendArtifact` objects with `Witness`, `WitnessText`, `WitnessFor`, and `SourceItem` facts, preserving exact source slices even when file paths contain periods.
- Added `witness-artifact-reviewable` validation: concrete file/test/log/commit/hash-style witness annotations pass; TODO/raw-text-only/non-concrete placeholders become Unknown checks plus `MissingWitnessArtifact` blocking questions.
- Added profile fact schemas so witness atoms and missing-witness questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (13 tests); full suite passed with 199 tests; `git diff --check` passed. Local implementation commit: `a838ba7` (not pushed).

## 2026-07-07 non-numeric confidence marker review

Concrete repo work in `repos/specatom-hs`:

- Tightened Phase 2 `Confidence:` marker parsing so explicit non-numeric scales such as `Confidence: high` are not silently ignored.
- Non-numeric confidence markers now create source-spanned confidence objects with `Confidence`, `GeneratedFrom`, and `SourceItem` facts, but no `ConfidenceValue` atom.
- The validator emits a `confidence-value-in-unit-interval` Unknown check plus an `UnsupportedConfidenceValue` blocking question, keeping unsupported epistemic metadata reviewable through the PeTTa reified profile.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (10 tests); full suite passed with 196 tests; `git diff --check` passed. Local implementation commit: `565a348` (not pushed).

## 2026-07-07 conservative bridge relation validation

Concrete repo work in `repos/specatom-hs`:

- Added `bridge-relation-conservative` validation for Phase 2 `Bridge:` markers.
- The current scaffold now accepts only conservative graded correspondence relation labels (`corresponds-to`, `related`, `analogy`, `refines`, `approximates`, `contextual`) without review.
- Identity/equivalence-style relation labels such as `Bridge: SUMO.Process as identical` still create source-spanned `BridgeObject` records, but now produce Unknown checks plus `UnsupportedBridgeRelation` blocking questions instead of being treated as ontology identity claims.
- Added `UnsupportedBridgeRelation` to the profile fact schema so the review question exports through PeTTa reified atoms without backend refusal.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (9 tests); full suite passed with 195 tests; `git diff --check` passed. Local implementation commit: `6c5e2df` (not pushed).

## 2026-07-07 explicit confidence marker support

Concrete repo work in `repos/specatom-hs`:

- Added conservative `Confidence:` marker parsing to the Phase 2 semantic-object pass.
- Percent and decimal confidence annotations now create source-spanned epistemic metadata (`Confidence`, `ConfidenceValue`, `GeneratedFrom`, `SourceItem`) and export through the PeTTa reified profile.
- `confidence-value-in-unit-interval` passes for normalized values in `[0,1]`; out-of-range values such as `120%` produce Unknown checks plus `UnsupportedConfidenceValue` blocking questions instead of being treated as truth values.

Verification so far:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
```

Result: targeted semantic-object tests passed (8 tests); full suite passed with 194 tests; `git diff --check` passed. Local implementation commit: `7b7aedb` (not pushed).

## 2026-07-07 arbitrary unsupported bridge ontology review

Concrete repo work in `repos/specatom-hs`:

- Broadened Phase 2 `Bridge:` marker parsing from a fixed ontology alternation to arbitrary ontology labels with the existing conservative support whitelist (`sumo`, `expo`, `hyperseed`).
- Unsupported bridge ontology labels such as `OpenCog.AtomSpace` now still create a first-class `BridgeObject`, exact source provenance, an `Unknown` `bridge-profile-supported` check, and an `UnsupportedBridgeOntology` blocking question instead of being silently ignored by the regex.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (6 tests); full suite passed with 192 tests; `git diff --check` passed. Local implementation commit: `b23cc36` (not pushed).

## 2026-07-07 Phase 2 semantic marker exact occurrence spans

Concrete repo work in `repos/specatom-hs`:

- Replaced the Phase 2 semantic-object `_raw_match_span` implementation with raw-text-index alignment, matching the source indexer/concept occurrence strategy instead of searching for matched text in the source segment.
- This fixes ambiguous provenance when a Plain item repeats the same marker type (for example two `Evidence:` clauses) and preserves exact source spans for semantic markers on continuation lines.
- Added regression coverage comparing generated evidence source slices to ground truth for repeated same-item evidence markers and continuation-line evidence markers.
- Updated README support surface.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (5 tests); full suite passed with 191 tests; `git diff --check` passed. Local implementation commit: `c018b74` (not pushed).

## 2026-07-07 receive-from data-path edge extraction

Concrete repo work in `repos/specatom-hs`:

- Extended conservative `DataFlowEdge` extraction to recognize explicit `receives ... from` component data-path wording, normalizing it as `receives-from` while preserving exact matched source spans.
- Updated isolated-component regression coverage so broader non-edge wording remains covered by `flows to` examples rather than treating explicit receives-from statements as isolated.
- Added ground-truth coverage for extracted receive edges and exact source-slice provenance (`the worker receives events from the task queue`).
- Updated README support surface.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow.InformationFlowValidationTests.test_explicit_data_path_edges_are_extracted tests.test_specatom_information_flow.InformationFlowValidationTests.test_data_flow_edge_has_exact_source_provenance tests.test_specatom_information_flow.InformationFlowValidationTests.test_isolated_component_detected_and_unacknowledged tests.test_specatom_information_flow.InformationFlowValidationTests.test_isolated_component_atoms_exported_through_petta_profile -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted tests passed; full suite passed with 186 tests; `git diff --check` passed. Local implementation commit: `afe9c8f` (not pushed).

## 2026-07-07 exact TemporalOrderEdge provenance

Concrete repo work in `repos/specatom-hs`:

- Tightened temporal-ordering edge provenance so `TemporalOrderEdge` objects now cite exact matched ordering phrases via the existing raw-text-to-source alignment helper, rather than the whole containing Plain item.
- Updated the temporal provenance regression to use surrounding non-edge text and compare the generated source slice to ground truth (`"the service runs before the database"`).
- Updated README/project records to reflect exact source-span provenance for both `DataFlowEdge` and `TemporalOrderEdge` atoms.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow.InformationFlowValidationTests.test_temporal_order_edge_has_exact_source_provenance -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted temporal provenance test passed; full suite passed with 186 tests; `git diff --check` produced no whitespace errors. Local implementation commit: `dd26bc3` (not pushed).

## 2026-07-07 duplicate data-path edge review

Concrete repo work in `repos/specatom-hs`:

- Added a conservative `information-flow-duplicate-edge-reviewed` obligation to the information-flow validator.
- The pass counts repeated normalized `(source, target, direction)` `DataFlowEdge` declarations while preserving each exact source-spanned edge object as evidence.
- Unacknowledged duplicates now produce an `Unknown` check plus a `MissingInformationFlowEvidence` question blocking the obligation; duplicate/repeated/parallel/same-data-path acknowledgment wording makes the check pass.
- Added regression tests for unacknowledged duplicate edges, acknowledged duplicates, and PeTTa reified export of the new obligation/check.
- Updated README and project records.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 186 tests passed; `git diff --check` produced no whitespace errors.

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

### 2026-07-05 (session 4): Fan-out/fan-in concentration detection

Context: The information-flow pass extracts explicit `DataFlowEdge` atoms and performs graph analysis (transitive chains, cycles), but does not flag concentration risk. Components with many outgoing edges (high fan-out) are potential bottlenecks or single-points-of-failure, and components with many incoming edges (high fan-in) are critical shared dependencies. Both deserve review.

Approach: After cycle detection, compute per-node out-degree and in-degree from the extracted edges list. When any component has >=3 edges in one direction, emit `information-flow-fan-out-reviewed` and/or `information-flow-fan-in-reviewed` obligations: Pass when the spec text acknowledges concentration (fan-out, fan-in, bottleneck, SPOF, critical dependency, coupled, hotspot, etc.) or when no component exceeds the threshold, Unknown with blocking `MissingInformationFlowEvidence` question when concentration is unacknowledged.

Tests added: `test_high_fan_out_detected_and_unacknowledged` (router with 4 outgoing edges → Unknown + blocking question), `test_high_fan_out_acknowledged_passes` (same + 'bottleneck' → Pass), `test_low_fan_out_passes` (2 edges → Pass with 'no components'), `test_high_fan_in_detected_and_unacknowledged` (database with 4 incoming → Unknown + blocking question), `test_high_fan_in_acknowledged_passes` (same + 'critical shared dependency' → Pass), `test_fan_out_and_fan_in_atoms_exported_through_petta_profile` (PeTTa export includes both obligations + MissingInformationFlowEvidence atoms), `test_no_fan_review_when_no_edges` (no DataFlowEdge atoms → no fan obligations).

Result: focused information-flow tests passed (28 tests), full suite passed (107 tests), and `git diff --check` passed. Local implementation commit: `390422c` (`Add fan-out/fan-in concentration detection to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

### 2026-07-05 (session 5): Source/sink identification and reachability analysis

Context: The information-flow pass extracts explicit `DataFlowEdge` atoms and performs graph analysis (transitive chains, cycles, fan-out/fan-in), but does not identify source nodes (no incoming edges) or sink nodes (no outgoing edges), and does not check whether all components are reachable from source nodes. Missing source/sink identification and unreachable components may indicate missing dependencies or dead code.

Approach: After fan-out/fan-in detection, compute all nodes and targets from the adjacency graph. Source nodes are nodes with no incoming edges (`adjacency.keys() - all_targets`). Sink nodes are nodes with no outgoing edges (`not adjacency.get(n)`). Emit `information-flow-source-sink-identified` obligation: Pass when both sources and sinks exist, Unknown with blocking `MissingInformationFlowEvidence` question when either is missing. Then perform BFS from all source nodes and check if every node is reachable. Emit `information-flow-reachability-reviewed` obligation: Pass when all nodes reachable, Unknown with blocking question when unreachable nodes exist.

Tests added: `test_source_sink_identified_with_dag` (pipeline→cache + pipeline→sink → Pass with source/sink names in evidence), `test_source_sink_unknown_when_all_nodes_have_incoming_edges` (A↔B cycle → no sources or sinks → Unknown + blocking question), `test_reachability_passes_when_all_nodes_reachable` (DAG → Pass), `test_reachability_unknown_when_unreachable_nodes_exist` (pure cycle → no sources → all nodes unreachable → Unknown + blocking question), `test_no_source_sink_or_reachability_when_no_edges` (no DataFlowEdge atoms → no obligations), `test_source_sink_and_reachability_atoms_exported_through_petta_profile` (PeTTa export includes both obligations + MissingInformationFlowEvidence atoms).

Result: focused information-flow tests passed (34 tests), full suite passed (113 tests), and `git diff --check` passed. Local implementation commit: `6b22902` (`Add source/sink identification and reachability analysis to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

### 2026-07-05 (session 6): Isolated component detection

Context: The information-flow pass extracts explicit `DataFlowEdge` atoms from edge verbs (`reads from`, `writes to`, `consumes from`, `depends on`, `sends to`, `produces to`) and performs graph analysis (transitive chains, cycles, fan-out/fan-in, source/sink, reachability). However, components mentioned with broader data-flow verbs that don't produce explicit edges (e.g., `receives data from`, `feeds into`, `flows to`, `provides to`, `gets from`, `pulls from`, `pushes to`) are not connected to any DataFlowEdge, which may indicate underspecified dependencies or missing declarations.

Approach: After reachability analysis, use a broader verb regex (`ISOLATED_COMPONENT_RE`) to find components mentioned with non-edge data-flow verbs. Compare the set of mentioned components against `all_nodes` (the connected nodes in the edge graph). Components in the mentioned set but not in the connected set are "isolated" — they are mentioned in a data-flow context but have no declared data-path edge. Emit `information-flow-isolated-component-reviewed` obligation: Pass when no isolated components are found, Unknown with blocking `MissingInformationFlowEvidence` question when isolated components exist.

Key design decision: The `ISOLATED_COMPONENT_RE` uses the same article-prefix skipping as `DATA_PATH_EDGE_RE` but with non-overlapping verb patterns. This ensures that components captured by `ISOLATED_COMPONENT_RE` are NOT the same as those in edges (since the edge verbs are different). The broader verbs (`receives from`, `feeds into`, `flows to/from/into`, `provides to`, `gets from`, `pulls from`, `pushes to`) are recognized by `INFO_FLOW_SIGNAL_RE` as data-flow signals, so the items are candidate_items, but `DATA_PATH_EDGE_RE` does not extract edges from them.

Tests added: `test_isolated_component_detected_and_unacknowledged` (pipeline with explicit edge + monitor with `receives data from` → Unknown + blocking question naming `monitor`), `test_isolated_component_passes_when_all_connected` (pipeline reads-from source + writes-to sink → Pass), `test_no_isolated_component_check_when_no_edges` (no DataFlowEdge atoms → no obligation), `test_isolated_component_atoms_exported_through_petta_profile` (PeTTa export includes obligation + MissingInformationFlowEvidence atoms).

Result: focused information-flow tests passed (38 tests), full suite passed (117 tests), and `git diff --check` passed. Local implementation commit: `08354a0` (`Add isolated component detection to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

### 2026-07-06 (session 1): Redundant path detection

Context: The information-flow pass extracts explicit `DataFlowEdge` atoms and performs graph analysis (transitive chains, cycles, fan-out/fan-in, source/sink, reachability, isolated components). However, it does not flag cases where multiple distinct paths connect the same pair of components — this may indicate intentional redundancy (fault tolerance, backup paths) or accidental duplication that should be reviewed.

Approach: After isolated component detection, for each direct edge (src, dst) in the adjacency graph, find all simple paths from src to dst using DFS with a max depth of 6 hops. If any indirect paths (length >= 3, meaning at least one intermediate node) exist alongside the direct edge, the pair is flagged as redundant. Emit `information-flow-redundant-path-reviewed` obligation: Pass when no redundant paths found, Pass when redundant paths exist and the spec text acknowledges them via 'redundant', 'backup', 'fallback', 'failover', 'fault tolerance', 'high availability', 'duplicate', 'resilient', 'replicated' wording, Unknown with blocking `MissingInformationFlowEvidence` question when redundant paths exist without acknowledgment.

Key implementation detail: The `_find_all_paths` helper uses iterative DFS with a visited-set to find all simple paths (no revisits). The `checked_pairs` set prevents duplicate checks for the same (src, dst) pair. The depth bound of 6 prevents exponential blowup on dense graphs.

Tests added: `test_redundant_path_detected_and_unacknowledged` (gateway→cache→database + gateway→queue→database + gateway→database direct edge → Unknown + blocking question mentioning both endpoints), `test_redundant_path_acknowledged_passes` (same edges + 'redundant paths for fault tolerance' → Pass), `test_no_redundant_path_when_no_indirect_paths` (simple DAG with no indirect paths → Pass with 'no redundant paths'), `test_no_redundant_path_check_when_no_edges` (no DataFlowEdge atoms → no obligation), `test_redundant_path_atoms_exported_through_petta_profile` (PeTTa export includes obligation + MissingInformationFlowEvidence atoms).

Result: focused information-flow tests passed (43 tests), full suite passed (122 tests), and `git diff --check` passed. Local implementation commit: `4b4cf8c` (`Add redundant path detection to information-flow validation`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

## 2026-07-06 (session 2): Dependency depth / critical path length detection

Context: The information-flow pass already detects transitive chains, cycles, fan-out/fan-in, source/sink, reachability, isolated components, redundant paths, temporal ordering impossibility, and cross-layer data/temporal consistency. However, it does not flag deep dependency chains — a long critical path (e.g., A→B→C→D→E) may indicate latency, fragility, or excessive coupling concerns that deserve explicit review even when the graph is acyclic.

Approach: After the cross-layer consistency check, when the DataFlowEdge graph is acyclic (`not unique_cycles`), compute the longest path via topological sort (Kahn's algorithm) + DP. The DP tracks `dist[node]` = longest path ending at `node` and `predecessor[node]` for path reconstruction. When `max_depth >= DEPTH_THRESHOLD` (4 edges), emit `information-flow-dependency-depth-reviewed` obligation: Pass when the spec acknowledges depth via 'deep', 'multi-layer', 'multi-hop', 'long chain', 'critical path', 'layered', 'pipeline depth', 'chain of command', or 'nested' wording; Unknown with blocking `MissingInformationFlowEvidence` question when deep and unacknowledged. The check is skipped when the graph is cyclic (only meaningful for DAGs) or when there are no edges.

Key implementation detail: Kahn's algorithm produces a topological order; the DP processes nodes in that order so all predecessors are finalized before updating a node's neighbors. Path reconstruction walks the `predecessor` chain backward from the deepest node.

Tests added: `test_dependency_depth_shallow_passes` (source→pipeline→database, depth 2 → Pass with 'below threshold'), `test_dependency_depth_deep_unacknowledged` (source→gateway→cache→queue→worker→database, depth 5 → Unknown + blocking question), `test_dependency_depth_deep_acknowledged_passes` (same chain + 'deep multi-layer pipeline architecture' → Pass), `test_dependency_depth_no_check_when_no_edges` (pipeline/data-flow wording without explicit edges → no obligation), `test_dependency_depth_no_check_when_cyclic` (A→B→A cycle → cycle check emitted, depth check not emitted), `test_dependency_depth_atoms_exported_through_petta_profile` (PeTTa export includes obligation + MissingInformationFlowEvidence atoms).

Result: focused information-flow tests passed (62 tests), full suite passed (141 tests), and `git diff --check` passed. Local implementation commit: `d63158f` (`Add dependency depth / critical path length detection`); not pushed. No paid compute, executable semantics or RawTextOnly export expansion, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

## 2026-07-06 document-validation-summary and auth_service ground-truth tests

Added a `document-validation-summary` atom to the PeTTa reified export in `src/specatom_hs/backends/petta.py`. The atom is `(document-validation-summary <file_id> <pass_count> <fail_count> <unknown_count> <question_count>)` and appears in the Validation section of grouped `.metta` output. This gives downstream consumers a quick triage signal: if `fail_count > 0` or `unknown_count > 0`, the document has unresolved issues that need review before backend lowering.

The summary is computed after all validation records are emitted by counting check statuses (`Pass`/`Fail`/`Unknown`) and QuestionObject roles. It is not a fact on a SpecObject, so it does not go through the FACT_SCHEMAS profile gate — it is a direct top-level atom in the reified export.

Added `tests/test_auth_service_ground_truth.py` with 18 end-to-end tests that run the full compiler pipeline on `auth_service.plain` and compare generated atoms to expected ground truth:

- Source provenance: file indexed with digest, sections cover Definitions/FunctionalSpecifications/AcceptanceTests.
- Concepts: User/Session/AuthToken defined, argon2id recognized as external concept, AuditSink unresolved with QuestionObject.
- Requirements/coverage: AUTH-1/2/3/4 labels emitted, duplicate AUTH-2 detected via DuplicateRequirementLabel, CoverageClaim atoms for AUTH-1 and AUTH-2, MissingCoverageTarget for AUTH-99, OrphanAcceptanceTest for the bullet without [covers:...].
- Validation summary: atom emitted, counts match `doc.checks` and `doc.objects` exactly, nonzero Unknowns and Questions.
- Reified export: all atom categories (source, object, validation) present in reified output, grouped export has section separators, RawTextOnly objects produce backend refusals.
- Structural integrity: all check statuses are declared enum values, all objects have known SemanticLevel.

Updated the existing `test_reified_atom_refuses_raw_text_only` test to expect the additional summary atom in the empty-document case.

Verification: `PYTHONPATH=src:tests python3 -m unittest discover -s tests -v` → 159 tests pass (141 existing + 18 new). `git diff --check` clean. Local implementation commit: `6351b7e` (`Add document-validation-summary atom and auth_service ground-truth tests`); not pushed. No paid compute, secrets/access/security setting changes, merge, force-push, or remote-ref deletion.

## 2026-07-06 per-edge source provenance for DataFlowEdge and TemporalOrderEdge

Concrete repo work in `repos/specatom-hs`:

- Reworked `build_information_flow_validation` so `DataFlowEdge` and `TemporalOrderEdge` SpecObjects now carry the source span of the specific indexed item where the edge was found, instead of the generic `first_span_id` of the first candidate item. This makes edge provenance precise and traceable to the exact source text.
- Added `_validate_edge_source_provenance` to `specatom_hs.validators`: emits `edge-has-item-level-source-provenance` obligations/checks for every object with a `DataFlowEdge` or `TemporalOrderEdge` fact. Pass when the edge's source span belongs to an indexed PlainItem; Unknown when the span exists but is not item-level; Fail when the span is missing.
- Added regression tests in `tests/test_specatom_information_flow.py`:
  - `test_data_flow_edge_has_item_level_source_provenance`: verifies two DataFlowEdge objects cite per-item spans matching the expected indexed items.
  - `test_temporal_order_edge_has_item_level_source_provenance`: verifies TemporalOrderEdge cites the specific item's span (and DataFlowEdge also has per-item provenance in the same fixture).
  - `test_edge_provenance_validation_fails_for_missing_source_span`: injects a synthetic edge with no source span and asserts the validation produces a Fail check.
- Updated README and validator gap audit.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused information-flow tests passed (70 tests), full suite passed (167 tests, up from 164), and `git diff --check` produced no whitespace errors. No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-06 O(n^2) validator dedup fix and connected-components detection

Concrete repo work in `repos/specatom-hs`:

- **Performance fix**: Replaced O(n^2) linear-scan deduplication in `add_validation_obligation` and `add_check` with O(1) set-based lookups. Added `_obligation_ids` and `_check_ids` sets to `SpecDocument` (in `schema.py`) that are kept in sync with the obligation/check lists. The old code used `all(existing.id != obl.id for existing in doc.validation_obligations)` which is O(n) per call; with 3,579 original checks, `_validate_check_records` created 14,316 new obligations/checks, each requiring a full list scan — taking 17 seconds. After the fix, the same compilation takes 0.14 seconds.

- **Connected-components detection**: Added a new information-flow check that uses undirected BFS to find disconnected subgraphs in the `DataFlowEdge` graph. When multiple components are found (each with internal edges but no edges between groups), emits `information-flow-connected-components-reviewed` obligation: Pass when the spec acknowledges independence (`independent`, `separate`, `standalone`, `decoupled`, etc.), Unknown with blocking question otherwise. This catches a gap that the directed reachability check misses: two independent subgraphs each with their own source pass reachability but are still disconnected.

- 3 regression tests: single-component pass, multi-component pass with acknowledgment, multi-component Unknown without acknowledgment. 170 tests pass total.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused information-flow tests passed (73 tests), full suite passed (170 tests), and `git diff --check` produced no whitespace errors. Local commit: `799cb64` (`Fix O(n^2) validator dedup and add connected-components detection`). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-06 information-flow graph summary and bidirectional edge review

Concrete repo work in `repos/specatom-hs`:

- Added `_compute_information_flow_summary` function to `backends/petta.py` that computes node count, edge count, temporal edge count, source/sink counts, cycle count, connected component count, max dependency depth, and bottleneck node count from DataFlowEdge and TemporalOrderEdge facts.
- The PeTTa reified profile now emits an `information-flow-graph-summary` atom with these stats for quick downstream triage of information-flow graph structure.
- Updated `emit_reified_atoms_grouped` to include the new atom in the validation section of grouped `.metta` output.
- Added a bidirectional edge review check to `build_information_flow_validation` in `passes.py`: detects when A→B and B→A both exist in the DataFlowEdge graph, emits `information-flow-bidirectional-edge-reviewed` obligation (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional/two-way/mutual/round-trip wording, Unknown with blocking question when unacknowledged).
- 9 new tests: 4 for graph summary (focused unit tests with known fixture + empty doc, plus auth_service e2e atom presence and count verification), 5 for bidirectional edge review (unacknowledged Unknown, acknowledged Pass, no-bidirectional Pass, PeTTa reified export, atom presence).

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest tests.test_auth_service_ground_truth -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused information-flow tests passed (79 tests), auth_service e2e tests passed (20 tests), full suite passed (178 tests), and `git diff --check` produced no whitespace errors. Local commits: `9974f83` (graph summary) and `e288da7` (bidirectional edge review). No paid compute, push/merge/force-push/delete, remote writes, or secrets/access changes.

## 2026-07-06 sink-reachability information-flow review

Concrete repo work in `repos/specatom-hs`:

- Added `information-flow-sink-reachability-reviewed` in `specatom_hs.passes.build_information_flow_validation`.
- The check builds a reverse adjacency graph and runs BFS backward from sink nodes to identify graph nodes that cannot reach any sink.
- This complements existing source reachability: a component can be reachable from a source but trapped in a cycle/dead-end with no output path.
- Unknown cases emit `MissingInformationFlowEvidence` + `QuestionText` + `Blocks` question objects, so trapped cycles/dead ends/missing outputs stay reviewable in the PeTTa profile.
- Added focused regression tests for all-nodes-can-reach-sink Pass and a source-reachable cycle with separate sink Unknown, plus updated no-edge/export coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: 81 information-flow tests passed; 180 total tests passed; `git diff --check` clean. Local commit `f6f3f19` (`Add self-dependency information-flow review`). No paid compute, remote writes, access/security changes, push/merge/force-push/delete.

## 2026-07-06 exact DataFlowEdge source spans

Concrete repo work in `repos/specatom-hs`:

- Tightened `DataFlowEdge` provenance from whole-item spans to exact matched edge-phrase spans. For example, a bullet containing additional prose now derives the edge object from just `The pipeline reads from the source`, not the whole bullet.
- Added an exact-match span helper inside `build_information_flow_validation` and changed the extracted edge tuple to carry `(source, target, direction, item_id, span_id)`.
- Updated `_validate_edge_source_provenance` so exact sub-item spans pass when contained within an indexed PlainItem; whole-item spans remain acceptable for edge types that do not yet have exact match spans (notably `TemporalOrderEdge`). Missing edge spans still Fail.
- Fixed the raw-text-to-source-offset alignment helper so raw-text index 0 skips bullet markers before returning, preserving exact spans at the start of bullet text.
- Updated regression coverage: `test_data_flow_edge_has_exact_source_provenance` compares the generated source slice against ground truth for two DataFlowEdge atoms; existing TemporalOrderEdge and missing-span tests still pass.
- Updated README and validator gap audit to describe exact DataFlowEdge source provenance.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: full suite passed (180 tests); `git diff --check` clean. Local commit: `5199f1a` (`Use exact source spans for DataFlowEdge provenance`). No paid compute, remote writes, access/security changes, push/merge/force-push/delete.

## 2026-07-06 self-dependency information-flow review

Concrete repo work in `repos/specatom-hs`:

- Added `information-flow-self-dependency-reviewed` to `build_information_flow_validation`.
- Direct DataFlowEdge self-loops (`source == target`) now get a dedicated obligation before the broader graph-cycle detector, so specs such as "cache depends on cache" produce a crisp Unknown review question unless recursion/feedback/fixed-point wording acknowledges the self-dependency.
- Unknown cases emit `MissingInformationFlowEvidence`, `QuestionText`, and `Blocks` facts for PeTTa-profile-safe review; ordinary non-self edges Pass with "no self-dependency edges detected".
- Added 3 regression tests: unacknowledged self-dependency Unknown + blocking question, acknowledged self-dependency Pass, and ordinary edge Pass.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused information-flow tests passed (84 tests), full suite passed (183 tests), and `git diff --check` produced no whitespace errors. Local commit `f6f3f19` (`Add self-dependency information-flow review`). No paid compute, remote writes, access/security changes, push/merge/force-push/delete.

## 2026-07-07 feed-into data-path edge extraction

Concrete repo work in `repos/specatom-hs`:

- Extended conservative `DataFlowEdge` extraction to recognize explicit `feeds into` component data-path wording, normalizing it as `feeds-into` while preserving exact matched source spans.
- Added target-span trimming for trailing preposition/temporal words captured by the two-word noun-phrase heuristic, while preserving single-letter component labels such as `Component A`.
- Added ground-truth regression coverage for extracted feed edges and exact source-slice provenance (`the parser feeds into the validator`).
- Updated README support surface.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow.InformationFlowValidationTests.test_explicit_data_path_edges_are_extracted tests.test_specatom_information_flow.InformationFlowValidationTests.test_data_flow_edge_has_exact_source_provenance -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted tests passed; full information-flow suite passed; full suite passed with 186 tests; `git diff --check` passed. Local implementation commit: `f710272` (not pushed).

## 2026-07-07 pull/push data-path edge extraction

Concrete repo work in `repos/specatom-hs`:

- Extended conservative `DataFlowEdge` extraction to recognize explicit `pulls ... from` and `pushes ... to` component data-path wording, normalizing them as `pulls-from` and `pushes-to` while preserving exact matched source spans.
- Added `pull`/`push` wording to information-flow signal and dependency-direction detection so those items are included in graph extraction rather than falling through isolated-component review.
- Removed `pulls ... from` / `pushes ... to` from the broader isolated-component-only pattern set and added ground-truth tests for extracted edge facts and exact source-slice provenance.
- Updated README support surface.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow.InformationFlowValidationTests.test_explicit_data_path_edges_are_extracted tests.test_specatom_information_flow.InformationFlowValidationTests.test_data_flow_edge_has_exact_source_provenance tests.test_specatom_information_flow.InformationFlowValidationTests.test_isolated_component_detected_and_unacknowledged -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted tests passed; full suite passed with 186 tests; `git diff --check` passed.

## 2026-07-07 ingest/emit data-path edge extraction

Concrete repo work in `repos/specatom-hs`:

- Extended conservative `DataFlowEdge` extraction to recognize explicit `ingests ... from` and `emits ... to` component data-path wording, normalizing as `ingests-from` / `emits-to` while preserving exact matched source spans.
- Added these forms to the information-flow signal/declaration surface so specs using only ingest/emit wording still create review objects and edges.
- Added ground-truth regression coverage for generated edge facts and exact source slices (`the collector ingests records from the archive`, `the scheduler emits jobs to the queue`).
- Updated README support surface.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_information_flow.InformationFlowValidationTests.test_explicit_data_path_edges_are_extracted tests.test_specatom_information_flow.InformationFlowValidationTests.test_data_flow_edge_has_exact_source_provenance -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted tests passed; full suite passed with 186 tests; `git diff --check` passed after removing one trailing-space line. Local implementation commit: `c2ec215` (not pushed).

## 2026-07-07 Phase 2 semantic-object first slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit-marker-only Phase 2 semantic objects for `Scope`/`Context`, `EpistemicStatus`, `Evidence`, `Interpretation`, and `Bridge` markers.
- Preserved conservative behavior: no inferred executable semantics; every new object uses stable IDs, exact source spans, and `SourceItem` facts.
- Added validation obligations/checks for source provenance, supported epistemic-status vocabulary, interpretation evidence, and bridge-profile support. Unsupported status labels, unsupported bridge ontologies, and interpretations without same-item evidence create `Unknown` checks plus blocking `QuestionObject`s.
- Extended the PeTTa reified predicate schema so supported semantic objects, validation obligations, checks, and question facts export through `petta_reified_v0` while RawTextOnly refusals remain intact.
- Updated README and marked the Phase 2 TASKS item complete.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: focused semantic-object tests passed; full stdlib unittest passed with 189 tests; `git diff --check` passed. Local implementation commit: `0011848` (`Add Scope/Evidence semantic object slice`).

## 2026-07-07 explicit revision marker support

Concrete repo work in `repos/specatom-hs`:

- Added a first Phase 3-adjacent explicit `Revision:` marker slice to `build_semantic_objects`.
- `Revision:` annotations now create source-spanned `RevisionObject`s at `TemplateParsed` level with `Revision`, `RevisionText`, `Revises`, and `SourceItem` facts, targeting the nearest semantic object without inventing migration semantics.
- Added `revision-has-source-provenance` Pass checks and PeTTa reified fact-schema support so revision atoms export without backend refusals.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (11 tests); full suite passed with 197 tests; `git diff --check` passed. Local implementation commit: `497cf1b` (not pushed).

## 2026-07-08 explicit Constraint marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Constraint:` marker parsing to the Phase 2/3 semantic-object pass.
- Constraint markers now create source-spanned `ObligationObject`s with `Constraint`/`ConstraintText`/`ConstraintFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Question:`.
- Added `constraint-has-explicit-evidence` validation: same-item `Evidence:` links produce Pass checks and `ConstraintEvidence` facts; constraints without explicit evidence stay Unknown and create `MissingConstraintEvidence` blocking questions.
- Added profile fact schemas so constraints, constraint-evidence links, and missing-constraint questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted semantic-object tests passed (22 tests); full suite passed with 208 tests; `git diff --check` passed. Local implementation commit: `ea3cb26` (not pushed).

## 2026-07-08 explicit Risk/Mitigation marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Risk:` and `Mitigation:` marker parsing to the Phase 2/3 semantic-object pass.
- Risk markers now create source-spanned validation/review objects with `Risk`/`RiskText`/`RiskFor`/`SourceItem` facts, preserving exact marker spans and stopping before following semantic markers.
- Mitigation markers now create source-spanned `RiskMitigation` objects with `RiskMitigationText`/`MitigatesRiskFor` facts.
- Added `risk-has-explicit-mitigation` validation: same-item mitigation markers or explicit mitigation/control wording produce Pass checks and `RiskMitigatedBy` links; unmitigated risks remain Unknown and create `MissingRiskMitigation` blocking questions.
- Added profile fact schemas so risks, mitigations, mitigation links, and missing-risk questions export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_risk_marker_requires_mitigation tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_risk_marker_links_same_item_mitigation -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted risk/mitigation tests passed; full suite passed with 211 tests; `git diff --check` passed. Local implementation commit: `83e8112` (not pushed).

## 2026-07-08 explicit Outcome marker slice

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Outcome:` marker parsing to the Phase 2/3 semantic-object pass.
- Outcome markers now create source-spanned proposition objects with `Outcome`/`OutcomeText`/`OutcomeFor`/`SourceItem` facts, preserving exact marker spans and stopping before following same-item semantic markers such as `Witness:` or `Evidence:`.
- Added `outcome-has-source-provenance` validation with Pass checks so reported results remain auditable source-backed propositions rather than inferred verification/execution semantics.
- Added profile fact schemas so outcome atoms export through `petta_reified_v0` without backend refusal.
- Updated README support surface and semantic-object regression coverage.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_outcome_marker_becomes_source_spanned_proposition -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted outcome test passed; full suite passed with 213 tests; `git diff --check` passed. Local implementation commit: `59250c6` (not pushed). No paid compute, remote push, secrets/access/security changes, merge, force-push, or remote-ref deletion.

## 2026-07-09 process artifact-only recognition

Concrete repo work in `repos/specatom-hs`:

- Broadened explicit `Process:` marker reviewability so script/config/build artifact declarations such as `scripts/deploy.sh` and `Makefile` can satisfy `process-definition-reviewable` even when the process text is an artifact-only declaration rather than an action-verb sentence.
- Added regression coverage for `Process: scripts/deploy.sh and Makefile. Evidence: ...`, checking exact source slices, Pass reviewability, no `MissingProcessDefinition` question, and PeTTa reified export without Process profile refusal.
- This continues the same boundary/resource artifact tightening while preserving TODO/raw-text-only/vague process placeholders as Unknown blocking questions.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_process_marker_accepts_script_artifact_without_action_verb -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted process-artifact test passed; semantic-object suite passed with 41 tests; full suite passed with 227 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 observation marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Observation:` marker support as a conservative source-spanned proposition facet with `Observation`/`ObservationText`/`ObservationFor`/`SourceItem` facts.
- Observation markers get Pass `observation-has-source-provenance` checks, preserving reported observations without upgrading them to validation success or executable semantics.
- Extended semantic marker lookahead, fact schemas, README support surface, and PeTTa reified export coverage; regression checks exact source spans before following `Evidence:` markers and confirms no validation-marker obligation is created for the observation object.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_observation_marker_preserves_source_without_claiming_validation -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted observation test passed; semantic-object suite passed with 73 tests; full suite passed with 259 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-11 proof marker support

Concrete repo work in `repos/specatom-hs`:

- Added explicit `Proof:` marker support as a conservative source-spanned evidence/review facet with `Proof`/`ProofText`/`ProofFor`/`SourceItem` facts.
- Proof markers now emit `proof-marker-reviewable` checks: concrete proof artifacts/procedures such as Lean/Coq/Isabelle/Agda/Metamath files, theorem/lemma wording, model-check/certificate/review/audit/test references pass, while TODO/TBD/raw-text-only/prove-later placeholders remain Unknown and create `MissingProofDetail` blocking questions.
- Extended semantic marker boundary handling, fact schemas, README support surface, pass description, and PeTTa reified export coverage with regressions for reviewable and placeholder proof markers.

Verification:

```bash
cd projects/specatom-hs/repos/specatom-hs
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects.SemanticObjectTests.test_explicit_proof_marker_exports_reviewable_proof_artifact tests.test_specatom_semantic_objects.SemanticObjectTests.test_proof_placeholder_becomes_blocking_question -v
PYTHONPATH=src python3 -m unittest tests.test_specatom_semantic_objects -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Result: targeted proof tests passed; semantic-object suite passed with 78 tests; full suite passed with 264 tests; `git diff --check` passed. Local changes are not pushed.

## 2026-07-12 transitive executable-reference safety

Concrete repo work in `repos/specatom-hs`:

- Tightened `petta_executable_skeleton_v0` gating so a safe-looking object cannot be lowered through a referenced object whose own profile-valid facts contain a dangling object reference.
- Added an explicit `unsafe-object-reference-transitive-dangling` refusal with the outer predicate/target and nested predicate/missing target in the reason.
- Added ground-truth regression coverage using `Covers -> Requirement -> GeneratedFrom -> missing object`.

Verification: focused PeTTa profile suite passed 17 tests; full suite passed 277 tests; `git diff --check` passed. No paid compute, remote writes, access/security changes, push/merge/force-push/delete.

## 2026-07-12 deep ambiguous-reference refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `petta_executable_skeleton_v0` arbitrary-depth reference traversal so duplicate-ID descendants are refused as `AmbiguousReference` instead of being silently skipped.
- Added ground-truth regression coverage for `Covers -> GeneratedFrom -> GeneratedFrom` ending at two objects with the same source ID.

Verification: focused regression passed; PeTTa profile suite passed 23 tests; full suite passed 283 tests; `git diff --check` passed. Changes remain local/unpushed.

## 2026-07-14 empty executable-object identity refusal

Concrete repo work in `repos/specatom-hs`:

- Tightened `petta_executable_skeleton_v0` so an otherwise profile-safe `BackendLowered`/`Verified` object cannot pass with an empty object ID.
- Added an explicit `missing-object-id-for-executable-skeleton` refusal for the unidentified object and `unsafe-profile-fact:empty-object-reference:<predicate>` for a profile-valid fact that targets an empty ID.
- Added ground-truth regressions for both direct lowering and `Covers` referencing the unidentified object, preventing the declared-object table from turning an empty identity into an apparently valid reference.

Verification: focused PeTTa profile suite passed 33 tests; full suite passed 293 tests; `git diff --check` passed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 transitive empty executable-object identity refusal

Concrete repo work in `repos/specatom-hs`:

- Added a failing ground-truth regression for `coverage -> requirement -> empty-ID object`, demonstrating that the originating executable object previously received no refusal even though the intermediate requirement was directly refused.
- Tightened arbitrary-depth executable-reference traversal to classify an empty-ID descendant as `MissingObjectId` and refuse the originating fact with the complete reference path.
- Preserved the existing direct `missing-object-id-for-executable-skeleton` and `empty-object-reference` diagnostics.

Verification: focused regression passed; PeTTa profile suite passed 34 tests; full suite passed 294 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 whitespace-only executable-object identity refusal ground truth

Concrete repo work in `repos/specatom-hs`:

- Added a regression covering a whitespace-only object ID, a direct profile-valid reference to it, and an outer `Covers -> requirement -> blank-ID object` chain.
- Confirmed executable-skeleton gating treats whitespace-only identities as missing, emits `empty-object-reference` for the direct reference, and propagates `MissingObjectId` to the originating object at arbitrary depth.
- This closes the normalization-shaped ground-truth gap without trimming or silently aliasing identifiers in the IR.

Verification: focused regression passed; full stdlib unittest suite passed 295 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 whitespace-only executable source-provenance refusal ground truth

Concrete repo work in `repos/specatom-hs`:

- Added a regression covering a `BackendLowered` object whose source-span ID contains only spaces/tabs, a requirement that references it, and an outer coverage object.
- Confirmed the gate treats whitespace-only provenance as absent at all three safety boundaries: direct lowering emits `missing-source-provenance-for-executable-skeleton`, the immediate reference emits `unsafe-object-reference-missing-source-provenance`, and arbitrary-depth traversal propagates `MissingSourceProvenance` with the complete path.
- This empirically closes the normalization-shaped provenance gap without trimming or silently rewriting source-span identities.

## 2026-07-14 blank scalar fact-argument refusal

- Tightened the shared PeTTa profile fact gate so a supported, correctly shaped fact with a whitespace-only scalar value is refused as `empty-fact-argument:<predicate>:position-<n>` instead of being emitted as an apparently meaningful atom.
- Object-reference positions remain handled by the established `empty-object-reference` and transitive-reference diagnostics, preserving their more precise safety behavior.
- Added ground-truth coverage with a blank `RequirementLabel` value and verified refusal in both `petta_reified_v0` and `petta_executable_skeleton_v0`.

Verification: PeTTa profile suite passed 37 tests; full stdlib unittest suite passed 297 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

Verification: focused regression passed; full stdlib unittest suite passed 296 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.
## 2026-07-14 `None` scalar fact-argument refusal

- Tightened the shared PeTTa profile fact gate so a supported fact with a `None` scalar value is refused as `empty-fact-argument:<predicate>:position-<n>` rather than being serialized into an apparently meaningful atom.
- Object-reference positions retain the established empty/dangling/transitive diagnostics.
- Added ground-truth coverage using `RequirementLabel(..., None)` and verified refusal in both `petta_reified_v0` and `petta_executable_skeleton_v0`.

Verification: focused regression passed; full stdlib unittest suite passed 298 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 empty object-reference refusal in reified export

- Tightened the shared PeTTa fact gate so `None` and whitespace-only object-reference arguments are refused by `petta_reified_v0` rather than serialized as apparent object IDs such as `None`.
- Preserved the executable profile's established direct `empty-object-reference` diagnostic and arbitrary-depth `MissingObjectId` propagation by handling direct empty references before general profile refusal and excluding them from the intermediate profile-error shortcut.
- Added ground-truth coverage using `GeneratedFrom(requirement-1, None)` and confirmed no corresponding generated atom is emitted.

Verification: focused regression and 39-test PeTTa profile suite passed; full stdlib unittest suite passed 299 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 non-finite scalar fact-argument refusal

- Tightened the shared PeTTa fact gate so floating-point `NaN`, positive infinity, and negative infinity are refused as `non-finite-fact-argument:<predicate>:position-<n>` instead of being serialized as apparently meaningful atoms.
- Added ground-truth coverage using `RequirementLabel` values for all three non-finite cases and verified refusal in both `petta_reified_v0` and `petta_executable_skeleton_v0`.

Verification: focused regression passed; full stdlib unittest suite passed 300 tests; `git diff --check` passed. Changes remain local/unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 structured fact-argument refusal

- Tightened the shared PeTTa profile fact gate so structured Python values such as lists and mappings are refused as `unsupported-fact-argument-type:<predicate>:position-<n>:<type>` instead of being stringified into atoms that falsely look like meaningful scalar values.
- Added ground-truth coverage using list and mapping `RequirementLabel` values and verified fail-closed behavior in both `petta_reified_v0` and `petta_executable_skeleton_v0`.

Verification: focused PeTTa profile suite passed 41 tests; full stdlib unittest suite passed 301 tests; `git diff --check` passed. Local commit `149bd57`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-14 structured object-reference refusal ground truth

- Added a regression for list- and mapping-valued `Covers` targets even when the apparent nested ID names an otherwise valid declared requirement.
- Confirmed both PeTTa reified emission and executable-skeleton gating return `unsupported-fact-argument-type:Covers:position-2:<type>` before object-ID resolution, and emit no misleading `Covers` atom.
- This closes the object-reference side of the structured-value ground-truth gap without stringifying containers into apparent IDs.

Verification: focused regression passed; full stdlib unittest suite passed 302 tests; `git diff --check` passed. Local commit `83507e8`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 semicolon-safe PeTTa serialization

- Tightened the shared atom serializer so scalar values containing `;` are JSON-quoted. In MeTTa source a bare semicolon begins a comment, so previous output could silently truncate source-manifest or supported fact atoms.
- Added an end-to-end regression compiling semicolon-bearing requirement text and comparing the emitted source/fact text to the quoted ground truth.

Verification: focused PeTTa profile suite passed 43 tests; full stdlib unittest suite passed 303 tests; `git diff --check` passed. Local commit `1dfd8ed`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 ASCII-control-safe PeTTa serialization

- Extended the shared atom serializer to JSON-quote strings containing ASCII control characters, including NUL and DEL, rather than writing raw control bytes into `.metta` output.
- Added ground-truth coverage for NUL and BEL in a supported `RequirementText` fact, checking the exact escaped atom and absence of raw control bytes.

Verification: focused regression passed; full stdlib unittest suite passed 304 tests; `git diff --check` passed. Local commit `4f644be`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-string object-reference refusal

- Tightened the shared PeTTa fact gate so object-reference positions require string IDs. Integers, floats, and booleans are refused as `unsupported-object-reference-type` instead of being stringified and potentially resolving to objects named `"1"`, `"1.5"`, or `"True"`.
- Added ground-truth coverage proving the apparent matching objects do not make these references valid in either the reified or executable profile.

Verification: focused regression passed; full stdlib unittest suite passed 305 tests; `git diff --check` passed. Local commit `7bb1514`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-string fact-subject refusal

- Tightened the shared PeTTa profile fact gate so object-scoped fact subjects must be string IDs. Integer, float, and boolean subjects can no longer pass by stringifying to apparently matching object IDs such as `"1"`, `"1.5"`, or `"True"`.
- Added ground-truth coverage proving these aliases emit no supported fact atom and are refused by both `petta_reified_v0` and `petta_executable_skeleton_v0`.

Verification: focused regression passed; full stdlib unittest suite passed 306 tests; `git diff --check` passed. Local commit `0777830`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-string object-ID refusal

- Tightened both PeTTa profiles so integer, float, and boolean SpecObject IDs are refused explicitly rather than emitted as apparent atom identities or reaching executable validation's string-only `.strip()` path.
- Excluded non-string IDs from the executable profile's declared-object lookup, preventing them from aliasing string reference targets.
- Added ground-truth coverage proving neither `spec-object` nor supported fact atoms are emitted and executable validation returns a refusal instead of raising an exception.

Verification: targeted regression and 47-test PeTTa profile suite passed; full stdlib unittest suite passed 307 tests; `git diff --check` passed. Local commit `1367d46`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-enum object-role refusal

- Tightened both PeTTa profiles so malformed runtime object roles (including strings that resemble valid role labels, `None`, and integers) produce explicit refusals instead of reaching `obj.role.value` or being admitted to executable-skeleton lowering.
- Reified emission now suppresses both the `spec-object` atom and otherwise supported object facts when the role is not a declared `Role` enum value.
- Added ground-truth coverage for string, null, and integer role values across reified and executable profiles.

Verification: targeted regression passed; full stdlib unittest suite passed 308 tests; `git diff --check` passed. Local commit `d844856`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 malformed fact-record refusal

- Hardened the shared PeTTa profile gate so facts represented by non-tuple runtime values (lists, strings, mappings, or `None`) produce explicit `unsupported-fact-record-type:<type>` refusals instead of crashing during predicate indexing, canonical ordering, or information-flow summary generation.
- Reified emission suppresses malformed records; executable-skeleton gating wraps the same reason as `unsafe-profile-fact:*`.
- Added ground-truth coverage for all four malformed record shapes across both profiles.

Verification: focused PeTTa profile suite passed 50 tests; full stdlib unittest suite passed 310 tests in 38.825 seconds; `git diff --check` passed. Local commit `71dcd92`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 empty reified object-ID refusal

- Tightened `petta_reified_v0` so empty and whitespace-only `SpecObject` IDs produce `missing-object-id-for-reified-emission` instead of becoming quoted but unusable atom identities.
- Suppressed the invalid object's `spec-object`, `derived-from`, and otherwise profile-valid fact atoms, keeping the refusal boundary aligned with executable-skeleton identity validation.
- Added exact ground-truth coverage for both empty and whitespace-only IDs.

Verification: focused PeTTa profile suite passed 51 tests; full stdlib unittest suite passed 311 tests; `git diff --check` passed. Local commit `0e09f18`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-string fact-predicate refusal

- Tightened the shared PeTTa fact gate so predicates must be strings before schema lookup. Integer, null, and custom values whose string representation matches a supported predicate can no longer alias that predicate.
- Added exact ground-truth coverage proving neither reified emission nor executable-skeleton validation admits the malformed facts.

Verification: focused regression and 52-test PeTTa profile suite passed; full stdlib unittest suite passed 312 tests; `git diff --check` passed. Local commit `14cc125`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-15 non-string source-provenance refusal

- Added a shared source-provenance identity gate for object `source_span_id` values.
- PeTTa reified export now refuses non-string source-span IDs and suppresses the corresponding misleading `derived-from` atom.
- Executable-skeleton validation now returns explicit direct and referenced-object refusals instead of calling `.strip()` on non-string provenance and crashing.
- Added exact ground-truth coverage using an integer provenance ID and a profile-safe object that references the malformed object.

Verification: focused regression and 53-test PeTTa profile suite passed; full stdlib unittest suite passed 313 tests; `git diff --check` passed. Local commit `1ae563b`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-obligation ID refusal

- Tightened PeTTa reified validation export so validation-obligation IDs must be non-blank strings.
- Integer IDs can no longer stringify into and alias legitimate string IDs; malformed obligation and rationale atoms are suppressed and replaced by explicit backend refusals.
- Added exact ground-truth coverage for an integer/string collision and a whitespace-only ID.

Verification: focused regression and 55-test PeTTa profile suite passed; full stdlib unittest suite passed 315 tests in 40.002 seconds; `git diff --check` passed. Local commit `58ab362`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-check ID refusal

- Tightened PeTTa reified validation export so check IDs must be non-blank strings; integer IDs can no longer stringify into and alias legitimate string check IDs.
- Suppressed all atoms for malformed checks and emitted explicit backend refusals.
- Changed `document-validation-summary` to count only emitted checks, preventing refused records from being represented in summary totals.
- Added exact ground-truth coverage for an integer/string ID collision, a whitespace-only ID, atom suppression, refusal reasons, and emitted-summary counts.

Verification: focused regression passed; full stdlib unittest suite passed 316 tests in 38.648 seconds; `git diff --check` passed. Local commit `bc4b348`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed check-to-obligation ID refusal

- Tightened PeTTa reified validation export so each check's `obligation_id` must be a non-blank string; integer IDs can no longer stringify into and alias legitimate string obligation IDs.
- Suppressed the entire malformed check, including check, check-obligation, and check-evidence atoms, and excluded it from document-validation summary counts.
- Added exact ground-truth coverage for an integer/string link collision and a whitespace-only obligation link.

Verification: focused 57-test PeTTa profile suite passed; full stdlib unittest suite passed 317 tests in 39.015 seconds; `git diff --check` passed. Local commit `83c18d3`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 undeclared check-status refusal

- Tightened PeTTa reified validation export so a check status must be a declared `CheckStatus` enum member before any check, check-obligation, or check-evidence atom is emitted.
- Runtime strings such as `"Pass"` can no longer alias a legitimate enum status; missing statuses are also refused.
- Refused records remain excluded from `document-validation-summary` counts.
- Added exact ground-truth coverage for string/enum `Pass` aliasing, a missing status, atom suppression, refusal reasons, and emitted-summary counts.

Verification: focused regression passed; full stdlib unittest suite passed 318 tests; `git diff --check` passed. Local commit `d9bf308`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-obligation property refusal

- Tightened PeTTa reified validation export so validation-obligation properties must be non-blank strings.
- Integer properties can no longer stringify into and alias legitimate string properties; the malformed obligation and rationale atoms are both suppressed and replaced by explicit backend refusals.
- Added exact ground-truth coverage for an integer/string property collision and a whitespace-only property.

Verification: focused regression passed; full stdlib unittest suite passed 321 tests in 38.233 seconds; `git diff --check` passed. Local commit `2115035`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-obligation target refusal

- Tightened PeTTa reified validation export so obligation target IDs must be non-blank strings.
- Integer targets can no longer stringify into and alias legitimate string targets; malformed obligation and rationale atoms are suppressed and replaced by explicit backend refusals.
- Added exact ground-truth coverage for an integer/string target collision and a whitespace-only target.

Verification: focused regression passed; full stdlib unittest suite passed 322 tests in 38.964 seconds; `git diff --check` passed. Local commit `6231ce3`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-obligation rationale refusal

- Tightened PeTTa reified validation export so obligation rationales must be non-blank strings.
- Integer rationales can no longer stringify into and alias legitimate string rationale text; malformed obligations and rationales are suppressed and replaced by explicit backend refusals.
- Added exact ground-truth coverage for an integer/string rationale collision and a whitespace-only rationale.

Verification: focused 63-test PeTTa profile suite passed; full stdlib unittest suite passed 323 tests; `git diff --check` passed. Local commit `62a19c4`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 whitespace-only reified provenance refusal

- Closed a PeTTa reified provenance fail-open where whitespace-only object or validation-obligation source-span IDs were truthy and therefore emitted as malformed `derived-from` atoms.
- Added an optional-provenance gate that continues to allow `None` and the empty-string absence convention, but refuses non-empty whitespace and non-string IDs.
- Added exact atom/refusal ground truth for both an object and a validation obligation.

Verification: focused 64-test PeTTa profile suite passed; full stdlib unittest suite passed 324 tests; `git diff --check` passed. Local commit `5afe6c3`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 malformed validation-check evidence refusal

- Tightened PeTTa reified validation export so check evidence must be a non-blank string before any check, check-obligation, or check-evidence atom is emitted.
- Integer evidence can no longer stringify into and alias legitimate string evidence; blank evidence is also refused.
- Refused records remain excluded from `document-validation-summary` counts.
- Added exact ground-truth coverage for integer/string evidence aliasing, blank evidence, atom suppression, refusal reasons, and emitted-summary counts.

Verification: focused 65-test PeTTa profile suite passed; full stdlib unittest suite passed 325 tests in 36.696 seconds; `git diff --check` passed. Local commit `4d2512a`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-16 dangling check-to-obligation refusal

- Tracked the IDs of validation obligations actually emitted by `petta_reified_v0` and now refuses any check whose `obligation_id` is absent from that set.
- This closes a validation-integrity fail-open where a malformed/refused obligation could still leave behind apparently valid `check`, `check-obligation`, and `check-evidence` atoms.
- Refused dangling checks are excluded from `document-validation-summary`; the regression compares emitted atoms and refusal records to ground truth for a check linked to an obligation rejected for blank rationale.

Verification: focused 66-test PeTTa profile suite passed; full stdlib unittest suite passed 326 tests; `git diff --check` passed. Local commit `d59965e`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 inconsistent check-to-obligation refusal

- PeTTa reified export now looks up each emitted validation obligation and refuses a check when its property or target differs from the cited obligation.
- This closes a validation-integrity fail-open where individually well-formed records could export an internally contradictory `check`/`check-obligation` pair even though the validator layer diagnoses that mismatch.
- Refused inconsistent checks emit no check, link, or evidence atoms and remain excluded from `document-validation-summary`; exact ground truth covers one valid check plus property- and target-mismatch refusals.

Verification: focused 67-test PeTTa profile suite passed; full stdlib unittest suite passed 327 tests in 37.291 seconds; `git diff --check` passed. Local commit `4e06a16`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 duplicate validation-record identity refusal

- PeTTa reified export now preflights non-blank string validation-obligation and check IDs for duplicates.
- Every occurrence of a duplicate obligation ID is refused, rather than exporting two claims and resolving linked checks to whichever record appeared last.
- Every occurrence of a duplicate check ID is refused, preventing contradictory status/evidence atoms under one identity; refused checks remain excluded from `document-validation-summary`.
- Checks linked to duplicate obligations follow the existing `check-obligation-not-emitted` refusal path.

Verification: two focused ground-truth regressions passed; full stdlib unittest suite passed 329 tests in 38.155 seconds; `git diff --check` passed. Local commit `8cc1078`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 duplicate reified object identity refusal

- PeTTa reified export now preflights non-blank string SpecObject IDs for duplicates and refuses every occurrence instead of emitting ambiguous `spec-object`, fact, or `derived-from` atoms under one identity.
- `document-validation-summary` now counts only question objects actually admitted by the reified gate, so duplicate/refused question objects cannot inflate the exported question count.
- Added exact ground truth for two conflicting question objects sharing an ID, including total atom suppression, two explicit refusals, and a zero-question summary.

Verification: focused regression and 70-test PeTTa profile suite passed; full stdlib unittest suite passed 330 tests in 37.475 seconds; `git diff --check` passed. Local commit `be41253`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.
## 2026-07-17 malformed source-manifest record refusal

- PeTTa reified export now type-checks `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` container entries before reading their fields, emitting structured type-bearing refusals for malformed records while preserving valid neighboring source atoms.
- Document-validation and information-flow summaries now use the first emitted file identity, or `document` when no valid file record was emitted, rather than dereferencing an invalid first container entry.
- Added atom/refusal ground truth covering malformed records interleaved with a valid linked file/span/section/item manifest.

Verification: focused 72-test PeTTa profile suite passed; full stdlib unittest suite passed 332 tests; `git diff --check` passed. Local commit `4988bbd`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 malformed source-span field refusal

- Added a fail-closed PeTTa source-span record gate for non-string/blank span and file IDs, non-integer (including boolean) byte/line bounds, negative or reversed byte ranges, and non-positive or reversed line ranges.
- Malformed spans now produce structured refusal records and no `source-span` atom, while a valid neighboring span still emits unchanged.
- Added exact atom/refusal ground truth for all six refusal classes.

Verification: focused source-index/profile suites passed 75 tests; full stdlib unittest discovery passed 333 tests; `git diff --check` passed. Local commit `bf37ab8`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 malformed PlainFile field refusal

- Added a fail-closed PeTTa source-manifest gate for non-string/blank PlainFile IDs, paths, and digests.
- Malformed files now produce structured refusal records and cannot supply the document-validation or information-flow summary identity; a valid neighboring file still emits and supplies that identity.
- Added exact atom/refusal ground truth for all three refusal classes.

Verification: focused source-index/profile suites passed 76 tests; full stdlib unittest discovery passed 334 tests; `git diff --check` passed. Local commit `11e298f`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 malformed Section and PlainItem field refusal

- Added fail-closed PeTTa source-manifest gates for the `Section` and `PlainItem` fields that feed emitted atoms and `derived-from` links.
- Sections now require non-blank string IDs/file IDs/kinds, non-boolean non-negative integer ordinals, and typed source spans with non-blank string IDs.
- Plain items now require non-blank string IDs/section IDs/raw text, absent or non-blank string parent IDs, non-boolean non-negative integer ordinals, and typed source spans with non-blank string IDs.
- Malformed records emit structured refusals and no partial manifest atoms; exact ground truth also proves valid neighboring section/item atoms remain unchanged.

Verification: focused source-index/profile suites passed 77 tests; full stdlib unittest discovery passed 335 tests; `git diff --check` passed. Local commit `346055e`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 duplicate source-manifest identity refusal

- PeTTa reified export now preflights non-blank string IDs across `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` records and refuses every occurrence of any duplicate identity.
- This prevents conflicting source records from exporting ambiguous provenance atoms under one identity while uniquely identified neighboring records still emit unchanged.
- Added exact atom/refusal ground truth covering duplicate identities in all four source-manifest collections plus valid linked neighbors.

Verification: focused source-index/profile suites passed 78 tests; full stdlib unittest discovery passed 336 tests; `git diff --check` passed. Local commit `c97f2c1`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 dangling SourceSpan-to-PlainFile refusal

- PeTTa reified export now records the `PlainFile` identities actually admitted by its field and duplicate gates, then refuses a `SourceSpan` whose `file_id` is not in that emitted set.
- This prevents both absent file links and links to malformed/refused file records from leaving apparently valid but dangling `source-span` atoms.
- Exact atom/refusal ground truth covers a missing file, a span linked to a malformed file, and a valid neighboring file/span pair.

Verification: focused source-index/profile suites passed 79 tests; full stdlib unittest discovery passed 337 tests; `git diff --check` passed. Local commit `48d22c2`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 dangling and cross-file Section provenance refusal

- PeTTa reified export now records the source-span identities admitted by its field, duplicate, and file-link gates, then refuses sections whose file or span was not emitted.
- A section whose emitted span belongs to a different emitted file is also refused, preventing cross-file `section` / `derived-from` claims.
- Exact atom/refusal ground truth covers missing files, earlier-refused files/spans, absent spans, file/span disagreement, and one valid neighboring section.

Verification: focused 78-test PeTTa profile suite passed; full stdlib unittest discovery passed 338 tests; `git diff --check` passed. Local commit `2bfa970`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-17 dangling and cross-file PlainItem provenance refusal

- PeTTa reified export now records the `Section` and `SourceSpan` identities actually admitted by their earlier gates, then refuses Plain items whose file, section, or span was not emitted.
- It also refuses an item when its emitted section or emitted span belongs to a different file, preventing dangling or cross-file `plain-item` / `derived-from` claims.
- The PlainItem field gate now validates `file_id` directly. Exact ground truth covers absent and earlier-refused links, both cross-file inconsistencies, and one valid neighboring item.

Verification: focused source-index/profile suites passed 81 tests; full stdlib unittest discovery passed 339 tests in 39.650 seconds; `git diff --check` passed. Local commit `f53f120`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-18 PlainItem parent-link refusal

- PeTTa source-manifest export now admits Plain items in two passes so parent links are checked against the set of items that survived field, duplicate-ID, file, section, and span gates.
- Missing or previously refused parents, self-parent links, and parents from a different file or section suppress the child item rather than emitting a dangling or inconsistent parent identity.
- Parent refusal propagates to descendants, while forward references to valid later parents remain supported.
- Exact atom/refusal ground truth covers missing, cross-section, self, cascaded-refusal, valid-forward-reference, and valid neighboring cases.

Verification: focused 81-test PeTTa profile suite passed; full stdlib unittest discovery passed 341 tests in 39.408 seconds; `git diff --check` passed. Local commit `012c93d`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-18 canonical indexed-span section validation

- The crisp `section-span-file-matches-section-file` check now resolves the
  section's span ID through `doc.spans`, matching the already-canonical item
  validation and PeTTa manifest gate.
- A section can no longer receive a false Pass by embedding a conflicting
  `SourceSpan` whose ID matches an indexed span belonging to another file.
- Exact ground truth asserts one Fail check and its canonical indexed-file
  evidence for this aliasing case.

Verification: focused validation-record suite passed 13 tests; full stdlib
unittest discovery passed 343 tests in 39.184 seconds; `git diff --check`
passed. Local commit `afd48da`; unpushed. No paid compute, remote writes,
push/merge/force-push/delete, or secrets/access/security changes.

## 2026-07-18 duplicate indexed-span validation refusal

- Crisp section/item span-file checks now build their canonical lookup only
  from unique IDs; duplicate indexed `SourceSpan` identities cannot obtain a
  false Pass through last-write-wins dictionary selection.
- Both checks emit Fail with deterministic evidence containing the ambiguous
  span ID and occurrence count.
- Exact regression coverage uses conflicting duplicates ordered so the old
  implementation would have selected the matching final record and Passed.

Verification: focused validation-record suite passed 15 tests; full stdlib
unittest discovery passed 344 tests; `git diff --check` passed. No paid
compute, remote writes, push/merge/force-push/delete, or secrets/access/security
changes. Local commit `ffad34a`; unpushed.

## 2026-07-18 duplicate indexed-file validation refusal

- `_validate_source_spans` now resolves `SourceSpan.file_id` only through uniquely
  indexed `PlainFile` identities. Duplicate file IDs fail
  `source-span-within-file-bounds` before byte/line validation instead of using
  the last duplicate record.
- `section-file-is-indexed` and `item-file-is-indexed` likewise require a unique
  indexed file identity rather than set membership alone.
- Exact regression coverage orders conflicting duplicate files so the previous
  last-write-wins path would have admitted the matching final record; all three
  checks now Fail with the duplicate ID and occurrence count.

Verification: focused validation-record suite passed 17 tests; full stdlib
unittest discovery passed 347 tests; `git diff --check` passed. No paid compute,
remote writes, push/merge/force-push/delete, or secrets/access/security changes.
Local commit `4c67665`; unpushed.

## 2026-07-18 top-level source identity validation

- Added first-class `plain-file-identity-is-unique` and
  `source-span-identity-is-unique` validation obligations.
- Duplicate PlainFile or SourceSpan IDs now produce one deterministic Fail check
  with the ambiguous identity and occurrence count, rather than being visible
  only through downstream file/span link failures.
- Exact regression coverage asserts the obligation property, target, status,
  evidence, and single-record behavior for both source-record types.

Verification: focused validation-record suite passed 20 tests; full stdlib
unittest discovery passed 350 tests in 41.193 seconds; `git diff --check`
passed. Local commit `810c8f2`; unpushed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes.

## 2026-07-19 validation-layer identity validation

- Added first-class `validation-obligation-identity-is-unique` and
  `check-identity-is-unique` obligations over the validation records present at
  validator entry.
- Duplicate IDs now yield one deterministic Fail check with identity and count,
  matching the PeTTa exporter's fail-closed duplicate-record behavior.
- The entry snapshot prevents the validator's own generated self-checks from
  being mistaken for pre-existing records.

Verification: focused validation-record suite passed 22 tests; full stdlib
unittest discovery passed 352 tests; `git diff --check` passed. No paid compute,
remote writes, push/merge/force-push/delete, or secrets/access/security changes.
Local commit `70891ce`; unpushed.

## 2026-07-19 unhashable validation-layer identity refusal

- Validation now indexes only non-blank string ValidationObligation and
  CheckRecord IDs in uniqueness counts and downstream known-ID maps/sets.
- List-valued malformed IDs yield deterministic
  `validation-obligation-identity-is-unique` and `check-identity-is-unique`
  Fail evidence rather than crashing before diagnostics are available.
- Exact regression coverage exercises both malformed record types together and
  confirms downstream validation completes.

Verification: focused validation-record suite passed 28 tests; full stdlib
unittest discovery passed 358 tests in 55.377 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `75a37b8`; unpushed.

## 2026-07-19 backend-safe PlainFile identity validation

- Added `plain-file-has-safe-identity` obligations requiring non-blank string
  identities, alongside the existing uniqueness obligation.
- PlainFile identity counters, source-span file indexes, and validation-target
  sets now admit only safe string identities. List-valued IDs produce
  deterministic Fail evidence instead of raising `TypeError`; blank IDs also
  fail explicitly, and valid neighboring IDs still Pass.
- Exact regression coverage exercises unhashable, blank, and valid identities
  together.

Verification: focused validation-record suite passed 30 tests; full stdlib
unittest discovery passed 360 tests; `git diff --check` passed. No paid
compute, remote writes, push/merge/force-push/delete, or secrets/access/security
changes. Local commit `752c5b2`; unpushed.

## 2026-07-20 malformed fact validation refusal

- `_validate_object_facts` now requires each fact to be a tuple and each
  predicate to be a string before schema lookup, so malformed fact containers
  cannot be aliased or indexed as supported predicates.
- List, string, dictionary, and `None` fact records plus integer and `None`
  predicates yield exact `fact-has-supported-arity` Fail evidence.
- Object provenance validation now ignores malformed facts while looking for a
  `GeneratedFrom` tuple instead of dereferencing arbitrary values.

Verification: focused validation-record suite passed 33 tests; full stdlib
unittest discovery passed 363 tests; `git diff --check` passed. No paid compute,
remote writes, push/merge/force-push/delete, or secrets/access/security changes.
Local commit `f243bd3`; unpushed.

## 2026-07-20 backend-safe fact argument validation

- Added `fact-arguments-are-backend-safe` obligations after predicate/arity
  admission, matching the PeTTa reified backend's scalar safety gates.
- List/dictionary-style container arguments, non-string declared object
  references, blank or `None` arguments, and non-finite floats now fail crisply
  before export instead of appearing structurally valid until backend refusal.
- Exact regression evidence also pins a supported non-empty string argument to
  Pass, preventing an over-broad refusal rule.

Verification: focused validation-record suite passed 34 tests; full stdlib
unittest discovery passed 364 tests in 67.513 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `255484a`; unpushed.

## 2026-07-20 backend-safe fact subject validation

- `fact-subject-matches-object` now requires object-scoped fact subjects to be
  strings before comparing them with the owning object identity.
- Integer `7` can no longer pass crisp validation by string-coercing to owner
  ID `"7"`; it receives deterministic `subject@1 unsupported type=int` Fail
  evidence, while the exact string subject passes.

Verification: focused validation-record suite passed 35 tests; full stdlib
unittest discovery passed 365 tests in 66.357 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `da469fd`; unpushed.

## 2026-07-20 backend-safe CheckRecord evidence validation

- `check-has-evidence` now requires a non-blank string rather than accepting
  arbitrary values after `str(...)` coercion.
- `None` and list evidence produce deterministic type-bearing Fail evidence,
  matching PeTTa reified export refusal; valid text Passes and blank strings
  retain the existing `empty check evidence` failure.
- Exact regression coverage exercises malformed and valid neighboring records.

Verification: focused validation-record suite passed 36 tests; full stdlib
unittest discovery passed 366 tests in 69.164 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `42432b2`; unpushed.

## 2026-07-20 backend-safe ValidationObligation rationale validation

- Added `validation-obligation-has-reviewable-rationale` to expose the same
  non-blank string requirement already enforced by PeTTa reified export.
- `None`, list, and blank rationales now yield deterministic Fail evidence;
  reviewable non-blank text yields Pass evidence.
- Exact malformed/valid neighboring-record ground truth prevents both unsafe
  coercion and over-broad refusal.

Verification: focused validation-record suite passed 37 tests; full stdlib
unittest discovery passed 367 tests; `git diff --check` passed. No paid
compute, remote writes, push/merge/force-push/delete, or secrets/access/security
changes. Local commit `82625f7`; unpushed.

## 2026-07-20 backend-safe ValidationObligation property validation

- Added `validation-obligation-has-safe-property` to expose the same non-blank
  string property requirement already enforced by PeTTa reified export.
- `None`, list, and blank properties now yield deterministic Fail evidence;
  supported non-blank property text yields Pass evidence.
- Exact malformed/valid neighboring-record ground truth prevents unsafe
  coercion and over-broad refusal.

Verification: focused validation-record suite passed 38 tests; full stdlib
unittest discovery passed 368 tests in 119.217 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `393047e`; unpushed.
## 2026-07-20 backend-safe CheckRecord property validation

- Added `check-has-safe-property` to expose the same non-blank string
  requirement already enforced by PeTTa reified export.
- `None`, list, and blank properties now yield deterministic Fail evidence;
  supported non-blank property text yields Pass evidence.
- Exact malformed/valid neighboring-record ground truth prevents unsafe
  coercion and over-broad refusal.

Verification: focused validation-record suite passed 41 tests; full stdlib
unittest discovery passed 371 tests in 203.201 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `1adf2c0`; unpushed.
## 2026-07-20 backend-safe ValidationObligation source-span identity validation

- Added `validation-obligation-has-safe-source-span-id` so crisp validation
  exposes the PeTTa exporter's absent-or-non-blank-string provenance gate.
- `None` remains valid optional absence; list and blank identities yield exact
  Fail evidence; non-blank string identities Pass before known-span resolution.
- Exact malformed/valid neighboring-record ground truth prevents unsafe
  coercion without turning optional provenance into a requirement.

Verification: focused regression passed; full stdlib unittest discovery passed
374 tests in 260.398 seconds; `git diff --check` passed. No paid compute, remote
writes, push/merge/force-push/delete, or secrets/access/security changes.
Local commit `ac96423`; unpushed.

## 2026-07-21 backend-safe SpecObject source-span identity validation

- Added `object-has-safe-source-span-id` so crisp validation exposes the PeTTa
  exporter's absent-or-non-blank-string provenance gate.
- `None` remains valid optional absence; list and blank identities yield exact
  Fail evidence; non-blank string identities Pass.
- The broader `object-has-source-or-generated-provenance` check now guards set
  membership and emits deterministic evidence for malformed unhashable IDs
  instead of raising `TypeError`.

Verification: focused validation-record suite passed 45 tests; full stdlib
unittest discovery passed 375 tests in 272.379 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local implementation commit `f9a9455`;
unpushed.
Local commit `07110cb`; unpushed.

## 2026-07-21 backend-safe SourceSpan bound validation

- Added `source-span-has-safe-bounds` so crisp validation exposes the PeTTa
  exporter's non-boolean integer and ordering requirements for byte/line bounds.
- List and boolean byte bounds, `None` line bounds, and reversed ranges now
  yield deterministic Fail evidence instead of reaching unsafe comparisons;
  a valid neighboring span explicitly Passes.
- Unsafe bounds stop before file-range and line-offset comparisons, preserving
  fail-closed diagnostics without pretending malformed fields are indexable.

Verification: focused validation-record suite passed 46 tests; full stdlib
unittest discovery passed 376 tests in 268.694 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes. Local commit `0b826ac`; unpushed.

## 2026-07-21 backend-safe PlainFile field validation

- Added `plain-file-has-safe-fields` so crisp validation exposes the PeTTa
  exporter's non-blank string path/digest gates.
- Preserved source text must also be a string before SHA-256 recomputation;
  malformed `None`/container values now Fail deterministically instead of
  raising during `.encode()`.
- Exact malformed/blank/valid neighboring ground truth prevents both crashes
  and over-broad refusal.

Verification: focused validation-record suite passed 47 tests; full stdlib
unittest discovery passed 377 tests; `git diff --check` passed. No paid
compute, remote writes, push/merge/force-push/delete, or secrets/access/security
changes. Local implementation commit `ed7a3d8`; unpushed.

## 2026-07-21 backend-safe Section field validation

- Added `section-has-safe-fields` so crisp validation exposes the PeTTa
  exporter's non-blank string kind and non-negative, non-boolean integer
  ordinal requirements.
- List and blank kinds plus boolean and negative ordinals now yield exact Fail
  evidence, while a valid neighboring section explicitly Passes.

Verification: focused validation-record suite passed 48 tests; full stdlib
unittest discovery passed 378 tests in 276.326 seconds; `git diff --check`
passed. No paid compute, remote writes, push/merge/force-push/delete, or
secrets/access/security changes.
