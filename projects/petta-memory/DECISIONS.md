# Decisions

## 2026-06-27: Local-first standalone prototype before OmegaClaw integration

**Decision:** Start `petta-memory` as a standalone local repository under `projects/petta-memory/repos/petta-memory`, then integrate into OmegaClaw/ProtomegaTron only after append/query/view tests pass.

**Rationale:** The memory store affects prompt context and later PLN inference, so schema mistakes could silently shape agent behavior. A standalone prototype permits deterministic tests and review before live agent integration.

**Alternatives considered:** Patch OmegaClaw directly first; rejected for v0 because live integration would mix schema design, runtime policy, and prompt behavior too early.

## 2026-06-27: Append-only clusters are canonical

**Decision:** The canonical write unit is an append-only `MemoryCluster`; current state is derived from status/truth/salience events and supersession links.

**Rationale:** This preserves auditability and is safer for later PLN belief revision than in-place mutation.

## 2026-06-27: Separate audit, prompt, and PLN views

**Decision:** The implementation will maintain distinct view functions for human audit, LLM prompt context, and PLN-safe atoms.

**Rationale:** Raw observed/quoted material is useful evidence but should not be exported as factual PLN premises without explicit promotion.

## 2026-06-30: PLN promotion requires rule, bounded trust, and domain metadata

**Decision:** A `DerivedBelief` is PLN-eligible only when an explicit `PromotionEvent` supplies `PromotesTo`, `PromotionRule`, bounded numeric `PromotionTrust` in `[0, 1]`, and `PromotionDomain`, and the belief has both `TruthValue` and `EvidenceFor`. Normalized exports use `MM-PLNPremise`, `MM-PLNDomain`, `MM-PLNTrust`, and `MM-PLNPromotionRule` mapping atoms.

**Rationale:** Promotion without trust/domain metadata is too ambiguous for later PLN inference and can make quoted or derived material look more authoritative than intended. Keeping normalized mapping atoms explicit makes the intermediate store safer to inspect before choosing a concrete PLN runtime.

## 2026-07-01: First PeTTaChainer export uses STV proof statements, not EC packets yet

**Decision:** Export promoted beliefs to PeTTaChainer initially as `(: proof-id statement (STV strength confidence))`. The mapper preserves the `TruthValue` strength and caps confidence by `PromotionTrust` so promotion can reduce but not inflate confidence. `EvidencePacket`/`EC pos neg` export is deferred until the memory schema represents explicit support and opposition counts.

**Rationale:** PeTTaChainer can validate this shape immediately with `check_stmt`, giving a narrow runtime smoke without inventing unsupported evidence-count semantics.

## 2026-07-01: PeTTa runtime parse checks remain explicit and pre-append

**Decision:** Wire PeTTa runtime validation through an opt-in `make_petta_parse_checker(...)` hook rather than making PeTTa/PeTTaChainer a default dependency of `MediumMemoryStore` or enabling any live OmegaClaw write path.

**Rationale:** Runtime syntax compatibility is useful before PLN/OmegaClaw integration, but the core store should remain dependency-light and deterministic. Keeping the checker explicit preserves local-first operation, lets tests use fake runtimes, and ensures a runtime failure happens before append so the journal remains unchanged.

## 2026-07-01: Preserve PeTTaChainer's pi-PLN semantics, then split work into mechanics optimization and inference control

**Decision:** Use PeTTaChainer because its pi-PLN setup is semantically appropriate for experiential learning across multiple contexts, but treat the current implementation as an initial semantic substrate rather than an optimized or inference-controlled engine. After the basic pipeline works, proceed on two threads: (1) profile and optimize rule-application/truth-value mechanics, and (2) collaborate with Ben on richer OmegaClaw-specific inference control.

**Rationale:** Context-indexed evidence is important for OmegaClaw-style experiential learning; flattening evidence prematurely into a single global truth value would lose exactly the structure the memory layer needs. At the same time, semantic adequacy does not imply efficient implementation or good search/control behavior.

**Alternatives considered:** Replace PeTTaChainer immediately with a simpler/faster PLN substrate; rejected for now because it risks losing the pi-PLN/context semantics before we understand the optimization and control bottlenecks.

## 2026-07-02: EvidencePacket export requires explicit support/opposition counts

**Decision:** PeTTaChainer `EvidencePacket` export is enabled only for promoted beliefs with explicit `EvidenceSupportCount` and `EvidenceOppositionCount` atoms. The exporter emits `(EC pos neg)` from those schema values and does not derive counts from `TruthValue`/STV.

**Rationale:** EC packets carry evidence-count semantics that are stronger than a truth-value confidence. Requiring explicit counts avoids silently inventing support/opposition evidence while still giving OmegaClaw-context workloads a principled path into PeTTaChainer's context-indexed evidence machinery.

## 2026-07-02: Instrument `compileadd` subforms before optimizing or bypassing add

**Decision:** Keep the next PeTTaChainer performance work diagnostic-first: profile `compileadd`'s internal subforms in bounded subprocesses before adding a minimal/precompiled add path or changing exported PeTTaChainer atoms.

**Rationale:** Constructor-only profiling showed initialization is fast while add-only stages time out. The new probes give a narrower failure surface without changing PeTTaChainer semantics or petta-memory export contracts.


## 2026-07-02: Direct-vs-eval probe controls before bypassing PeTTaChainer add

**Decision:** Treat the `materialize-stmt-lambdas`/`mm2compile` timeout as not explained by the previous eval-wrapped probe alone. Keep direct subform probes as the default profiling path, retain narrow eval controls for comparison, and do not change petta-memory export semantics until a minimal/precompiled add option is selected and gated.

**Rationale:** Direct probes mirror PeTTaChainer's `compileadd` `let*` path more closely than `!(eval ...)`. The direct-vs-eval artifact shows both materialize and mm2compile still time out under a 5s bound, while index/maybe-process stages are fast, so bypassing or optimizing add should target materialization/compilation rather than query or context projection.

## 2026-07-02: Use a non-live precompiled statement cache gate before full PeTTaChainer add/query

**Decision:** The next minimal PeTTaChainer path is a non-live precompiled-statement cache/handoff gate for checked promoted STV statements and EvidencePackets. Cached atoms are PLN-ready inputs for downstream inspection or future GoalChainer/OmegaClaw mapping, not inferred beliefs. Full PeTTaChainer `compileadd`/query remains behind an explicit gate until `materialize-stmt-lambdas`/`mm2compile` are instrumented upstream or a precompiled add API exists.

**Rationale:** The direct-vs-eval probe artifact shows that both direct and eval-control materialization/compilation paths time out, while `check_stmt`, constructor initialization, `index-source-implication`, and `maybe-process-on-add` succeed quickly. A direct KB fact add risks bypassing PeTTaChainer indexing/proof semantics; deeper upstream instrumentation is still needed, but a cache gate gives petta-memory and OmegaClaw planning a stable, testable handoff artifact now.

**Alternatives considered:** Minimal direct KB fact add; rejected for the immediate path because query semantics likely depend on PeTTaChainer's compiled/internalized proof structures. Upstream-only instrumentation; kept as a follow-up, but it would not advance the petta-memory handoff contract in this slice.

## 2026-07-02: Handoff cache is non-live input evidence, not inferred memory

**Decision:** `pettachainer_handoff_cache` packages promotion-eligible STV proof statements and explicit-EC EvidencePackets as a JSON handoff artifact for review and future OmegaClaw/GoalChainer mapping. Items are labeled `pln-ready-input-not-inferred-belief`; the cache is not appended to the journal, does not invoke PeTTaChainer `compileadd`/query, and does not claim inference results.

**Rationale:** This advances the integration contract despite the current `materialize-stmt-lambdas`/`mm2compile` bottleneck. Optional `statement_checker` support allows runtime validation of STV statement shape via `PeTTaChainer.check_stmt`, while keeping full add/query semantics behind the existing gate.

## 2026-07-02: GoalChainer smoke remains non-live and cannot use current compileadd path as the gate

**Decision:** Keep the GoalChainer gate at a non-live decision-payload contract and do not treat the current external GoalChainer demo as passed until its PeTTaChainer `compileadd` path is bypassed, adapted to precompiled handoff evidence, or instrumented upstream.

**Rationale:** The hand-picked `petta-memory` handoff fixture and wrapper can enforce provenance/no-task/no-write boundaries, but the external GoalChainer demo still reaches PeTTaChainer `compileadd` and fails with SWI `stack_limit=8g` before producing a decision payload. A passing gate must consume promoted evidence without claiming tasks or live skills and without relying on the currently blocked compileadd path.

## 2026-07-02: Precompiled GoalChainer smoke is the first non-live decision gate

**Decision:** Use a precompiled `goalchainer-handoff-cache` bridge as the first passing non-live GoalChainer decision-payload gate. The gate consumes promoted `Acceptable` STV evidence from petta-memory and runs only GoalChainer scenario/scoring/explanation code with a local cache-backed reasoner. It must not invoke GoalChainer CLI, PeTTaChainer `compileadd`/query, directives, execution, OmegaClaw skills, or memory writes. The older external CLI path remains available only as an explicit blocked comparison via `--external-cli`.

**Rationale:** The external GoalChainer demo currently fails before producing a decision payload because its PeTTaChainer `compileadd` path exceeds the SWI stack limit. The precompiled gate preserves provenance and exercises GoalChainer's decision machinery now, while truth-changing PeTTaChainer add/query semantics remain gated pending upstream instrumentation or a proper precompiled-add API.


## 2026-07-03: Keep GoalChainer precompiled and add bounded EC influence before returning to compileadd

**Decision:** The next non-live GoalChainer evidence-depth step is not live integration and not the external CLI path. Keep the precompiled decision gate, but let matching `EvidencePacket` support/opposition counts influence promoted `Acceptable` action appraisal as bounded derived strength/confidence, with explicit proof provenance and `compileadd_not_invoked` checks.

**Rationale:** The external GoalChainer/PeTTaChainer `compileadd` path is still blocked, but ignoring EC packets would discard the context-rich evidence signal Ben wanted preserved for OmegaClaw-style reasoning. A precompiled EC influence path gives a testable bridge from promoted EvidencePackets to GoalChainer decision scoring without claiming inferred beliefs, tasks, skills, or memory writes.

## 2026-07-03: No public PeTTaChainer precompiled-add API in checked-out source

**Decision:** Treat the current PeTTaChainer checkout as not exposing a public precompiled-add/cache API for petta-memory to adopt. Continue using the non-live petta-memory handoff cache as checked input evidence only, and focus further PeTTaChainer work on upstream `materialize-stmt-lambdas`/`mm2compile` instrumentation before full add/query gates.

**Rationale:** Source-level inspection of `pettachainer/pettachainer.py` and `pettachainer/metta/petta_chainer.metta` found public add methods routing through `compileadd`/`compileadd-mine` and no public precompiled/cache/handoff API terms. This matches the prior runtime profiles where `check_stmt` and initialization are healthy but `materialize-stmt-lambdas`/`mm2compile` and add stages time out.

**Alternatives considered:** Adopt a direct KB/precompiled fact add immediately; rejected because source inspection did not reveal a supported public API and direct adds could bypass PeTTaChainer indexing/proof semantics.

## 2026-07-03: Keep compileadd bottleneck work source-grounded before changing semantics

**Decision:** After confirming no public PeTTaChainer precompiled-add/cache API, add a no-runtime source map of the `compileadd` bottleneck path and target future instrumentation at `materialize-stmt-lambdas`, `mm2compile`, and the downstream `compile_` dispatcher before modifying export/add semantics.

**Rationale:** Prior runtime artifacts show tiny promoted-belief add stages timing out while `check_stmt`, constructor init, index-source, and maybe-process hooks are healthy. A source-grounded map narrows the next upstream instrumentation surface without invoking noisy SWI/PeTTaChainer runtime or risking semantic drift. The non-live handoff cache remains the safe integration path until a separate add/query gate passes.

## 2026-07-03: Petta-memory STV proofs should target PeTTaChainer's fact compile branch

**Decision:** Treat the current petta-memory promoted-belief statement shape `(: proof (Requires target PLNReadyViews) (STV s c))` as a PeTTaChainer `compile_` fact-assertion path, not an implication or bidirectional-rule path, unless future export semantics intentionally change the `BeliefContent` type.

**Rationale:** Source-level dispatch inspection of checked-out PeTTaChainer `compile.metta` and `logic_config.metta` shows `(Requires MemoryTarget0 PLNReadyViews)` is a concrete non-`Implication` type and not a configured bidirectional form. After `materialize-stmt-lambdas`/`mm2compile`, `compile_` should therefore use `compile-fact-kb` plus `compile-outputs`. This narrows future instrumentation without invoking runtime `compileadd` or changing the non-live handoff-cache boundary.

## 2026-07-03: Static import is not a direct current PeTTaChainer add bypass

**Decision:** Do not use PeTTa `static-import!` directly for current petta-memory PeTTaChainer exports, and do not treat it as a supported PeTTaChainer precompiled-add/indexing API. Keep it as a possible later non-live scratch benchmark only after symbol quoting/normalization and read-only query semantics are verified.

**Rationale:** Source inspection of checked-out `lib/lib_import.pl` shows a fast `.metta` -> `.pl` -> `.qlf` path, but the converter is line-oriented, intended for S-expression data only/no bangs, and mechanically replaces parentheses/spaces without quoting tokens. Current petta-memory STV/EvidencePacket exports contain uppercase symbols and hyphenated identifiers that are unsafe as unquoted Prolog terms and may not preserve PeTTaChainer compile/index semantics.

**Alternatives considered:** Run `static-import!` immediately as a compileadd bypass; rejected for this slice because it would mix token-conversion uncertainty with PeTTaChainer indexing semantics and could create misleading benchmark results.

## 2026-07-03: Static-import benchmark requires normalized scratch atoms first

**Decision:** Before any runtime `static-import!` microbenchmark, use a scratch-only normalized atom format rather than current PeTTaChainer exports. The designed format uses lowercase/underscore symbols and exactly three top-level fields, e.g. `(pm_stv_statement proof-id (pm_stv_payload statement-key strength confidence))` and `(pm_evidence_packet statement-key (pm_ec_payload support opposition provenance))`.

**Rationale:** PeTTa's converter mechanically turns one line into a Prolog space predicate and declares that predicate as arity 3. Keeping the benchmark records Prolog-safe and arity-compatible isolates loader/query semantics from token quoting bugs and from PeTTaChainer `compileadd` semantics. The benchmark remains non-live, temporary-directory-only, and cannot produce inferred beliefs or OmegaClaw memory writes.

## 2026-07-03: Static-import microbenchmark confirms loader viability for normalized atoms

**Decision:** The non-live runtime `static-import!` microbenchmark passed: 2 normalized atoms were successfully loaded into the `gckb/3` space predicate, all generated `.pl` fact lines matched expected converted Prolog facts, and the predicate count matched (2 facts in ~0.07s). Treat `static-import!` as a confirmed viable bounded loader for Prolog-safe normalized atoms in temporary-directory/non-live benchmarks. It remains a bulk data loader and not a PeTTaChainer `compileadd`/indexing API; do not use it to bypass PeTTaChainer proof/index semantics or claim inferred beliefs.

**Rationale:** The microbenchmark exercised the full `static-import!` path (`.metta` → `.pl` → `.qlf` → consult) with janus_swi in a bounded subprocess. Implementation findings: (1) `static-import!` must be called directly via `janus_swi.query_once` after consulting `lib_import.pl`, not through PeTTa `process_metta_string`; (2) `janus_swi`'s `findall/3` has an instantiation error on the result list variable, so `aggregate_all(count, ...)` and `query_once` are used instead; (3) fact comparison uses generated `.pl` file lines rather than runtime query results to avoid janus iteration limitations.

**Alternatives considered:** Use `static-import!` as a PeTTaChainer compileadd bypass; rejected because it loads atoms into a separate space predicate without PeTTaChainer's compiled proof structures, indexing, or truth-value semantics. The loaded facts are raw data records, not PeTTaChainer-inferred beliefs.
## 2026-07-03: Static-import benchmark spaces must be explicit and safe

**Decision:** Future non-live PeTTa `static-import!` microbenchmarks should use an explicit, Prolog-safe space predicate when isolation matters, and the benchmark must verify generated facts and runtime counts against that same selected predicate rather than assuming `gckb/3`.

**Rationale:** The first loader gate proved normalized atoms can load into `gckb/3`, but follow-up probes may need separate scratch predicates to avoid stale/runtime cross-talk and to compare alternative normalized representations. Validating the space name and using it consistently in expected facts plus runtime queries keeps these checks bounded and avoids a false pass from the default space. This remains a loader benchmark only, not a PeTTaChainer `compileadd`/indexing API or inferred-belief path.

## 2026-07-03: Static-import runtime gates must prove exact fact membership

**Decision:** Treat a PeTTa `static-import!` microbenchmark as passed only when the generated `.pl` facts match expectation, the selected predicate has the expected count, and each expected generated fact is directly queryable against the consulted runtime predicate.

**Rationale:** Text conversion and aggregate count are useful but can miss a false pass where the wrong named space is consulted or generated facts are not actually reachable as runtime Prolog goals. Exact membership checks keep the normalized-atom loader benchmark honest while preserving the existing boundary: this is still not PeTTaChainer `compileadd`/indexing, not query/inference success, and not a live OmegaClaw memory path.

## 2026-07-03: Lambda-free materialize should be an identity gate before mm2compile

**Decision:** For the current petta-memory promoted-belief proof shape, treat `materialize-stmt-lambdas` as expected to be a source-level identity walk because the statement contains no `|->` lambda forms. The next runtime probe should be a narrow non-live materialize identity gate before proceeding to `mm2compile` or full `compileadd`.

**Rationale:** Checked-out PeTTaChainer source only invokes `eval` inside `materialize-stmt-lambdas` when the current expression head is `|->`. The tiny STV proof `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 0.70 0.55))` has 0 lambda forms, so any timeout on this stage is unlikely to be caused by user lambda execution. This narrows the bottleneck toward PeTTa/MeTTa evaluator recursion/materialization overhead while keeping add/query and live OmegaClaw paths gated.

## 2026-07-03: Do not advance past materialize until the identity runtime gate passes

**Decision:** Keep `mm2compile`, full PeTTaChainer `compileadd`/query, and live OmegaClaw/GoalChainer integration gated until a lambda-free `materialize-stmt-lambdas` identity runtime gate completes with matching output under a bounded subprocess timeout.

**Rationale:** The first runtime identity gate for the tiny promoted-belief STV proof timed out at 6s despite source inspection predicting a pure identity walk. That means the blocker is already at materializer/evaluator recursion overhead, before `mm2compile` or the `compile_` fact branch can be meaningfully profiled. Proceeding deeper would conflate stages and risk misleading benchmarks; the next useful work is upstream materializer instrumentation or a smaller evaluator-level reproduction.

## 2026-07-04: Instrument materialization as a ladder before mm2compile

**Decision:** Treat `materialize-stmt-lambdas` as the current blocked PeTTaChainer add-stage boundary, but instrument it as a non-live ladder of source-checked lambda-free subforms before attempting `mm2compile` or `compileadd` again. Identity checks should compare MeTTa structure and tolerate renderer-only numeric formatting changes such as `0.70` to `0.7`.

**Rationale:** The ladder gate shows simple subforms from the promoted-belief proof materialize quickly, while the complete `(: proof type tv)` atom still times out under the bound. This narrows the bottleneck to full proof-atom traversal/evaluator behavior rather than user lambdas, PeTTaChainer construction, static-import loading, or later query/context stages.

**Alternatives considered:** Proceed directly to `mm2compile` instrumentation; rejected because the full proof has not passed the materialization identity gate. Treat string formatting differences as failure; rejected because PeTTa runtime may normalize floats without changing the structure or truth-value semantics.

## 2026-07-04: Keep PeTTaChainer add/query gated after proof-shape materialize timeout

**Decision:** Do not proceed to `mm2compile`, `compileadd`, query, or any live OmegaClaw/GoalChainer integration from the current PeTTaChainer proof-shape gate. Continue instrumentation at the `materialize-stmt-lambdas` evaluator behavior for the full four-field proof atom.

**Rationale:** The proof-shape ladder artifact (`pettachainer_materialize_proof_shape_ladder_gate_2026-07-04T1000Z.json`, sha256 `43669be7cd99dd9fc618ed07297518dd53d1a22527d8fa5d8fb6c9f78553ef24`) showed the type subform, STV subform, `(: proof)`, and `(: proof type)` all materialize as identity quickly, while adding the STV as the fourth field to form the exact proof atom still times out under a 4s bound. This indicates the remaining blocker is not either subform alone and not the shorter proof prefix.

**Alternatives considered:** Treat passing prefix/subform rungs as enough to try `mm2compile`; rejected because the exact full proof statement remains blocked at the first `compileadd` binding.

## 2026-07-04: Target materializer instrumentation at nested statement-type expressions inside proof atoms

**Decision:** Treat the next PeTTaChainer materialization investigation as focused on how `materialize-stmt-lambdas` handles nested statement-type expressions such as `(Requires MemoryTarget0 PLNReadyViews)` when they appear as the type field of a full `(: proof type tv)` atom. Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated.

**Rationale:** The sentinel proof-shape ladder shows that independent type/STV subforms, proof prefixes, and even a synthetic full-arity `(: proof ProofShapeSentinel (STV 1.0 1.0))` atom materialize as identity quickly, while `(: proof (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))` times out under the same bound. That narrows the failure surface from generic proof arity/STV handling to nested type-expression traversal inside the full proof shape.

**Alternatives considered:** Proceed directly to `mm2compile` or a direct KB fact add; rejected because the pre-`mm2compile` materialization rung remains blocked, and bypassing it risks semantic drift from PeTTaChainer's compile/index path.

## 2026-07-04: Narrow materialize blocker to nested Type arity in full proof atoms

**Decision:** Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated. Continue the PeTTaChainer investigation at `materialize-stmt-lambdas`, focused specifically on full proof atoms whose nested Type expression has at least two arguments, e.g. `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))`.

**Rationale:** The nested-Type ladder artifact (`pettachainer_materialize_nested_type_ladder_gate_2026-07-04T1400Z.json`, sha256 `bc5aab720dde2427afb1fbf2ad66dba53c2abcb32022e06b1d0ee4a1f8e8c5f2`) shows that atom Type heads, empty nested Type expressions, and one-argument nested Type expressions materialize as identity quickly under full proof shape plus sentinel STV. The timeout appears only when the nested Type reaches the original two-argument shape. This is a sharper boundary than the previous sentinel proof-shape gate and should guide the next upstream evaluator/materializer reproduction.

**Alternatives considered:** Proceed to `mm2compile` because smaller Type rungs pass; rejected because the exact two-argument nested Type still blocks at the first `compileadd` binding. Treat `static-import!` as a bypass; rejected because it remains a normalized bulk-loader benchmark outside PeTTaChainer compile/index semantics.
## 2026-07-04: Treat two-argument nested Type arity as the current materialize blocker

**Decision:** Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated. The next PeTTaChainer investigation should reproduce or instrument `materialize-stmt-lambdas` on a full proof atom whose Type field is any two-argument nested expression, before spending time on original-token-specific hypotheses.

**Rationale:** The arity/token matrix artifact (`pettachainer_materialize_nested_type_arity_matrix_gate_2026-07-04T1600Z.json`, sha256 `d24401f89cef49eddb83eb6c03ae2990cb626883c7f2f45b01647238e980fa35`) shows that `(: proof (Requires) (STV 1.0 1.0))` and `(: proof (Requires TypeArgSentinel0) (STV 1.0 1.0))` materialize quickly, but `(: proof (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))` times out at 4s. Because the first failing rung uses sentinel arguments rather than `MemoryTarget0` or `PLNReadyViews`, the blocker is now localized to generic nested Type arity inside the full proof shape.

**Alternatives considered:** Continue testing mixed/original argument tokens first; rejected because the all-sentinel two-argument rung already blocks before those controls. Proceed to `mm2compile`; rejected because the first `compileadd` binding still fails on a lambda-free materialization identity check.
