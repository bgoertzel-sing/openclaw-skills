
# 2026-08-20: TraceAttribution is a distinct persisted artifact class with proof trace

**Decision:** Implement `TraceAttribution` as a frozen, content-addressed
dataclass that binds a compiled result to its originating rule identity and
an opaque proof trace string. Persist it as a create-once checksummed JSON
artifact (`petta-memory-trace-attribution-v1`). Reload verifies schema,
document checksum, trace_digest, and result-binding fields against the
supplied derived capture.

**Rationale:** The existing `PeTTaChainerRuleAttribution` is compiler-bound
and explicitly does not claim a decoded runtime trace (`runtime_trace_decoded
= False`). The trace/rule attribution vertical gate requires a distinct
artifact class that carries proof trace content while preserving stable reload
identity. The proof trace is opaque — the attribution does not interpret or
validate its semantics — but it is content-addressed by the trace_digest and
protected by the create-once write boundary. Reload cannot independently
derive proof_trace from the result, so it verifies result-binding fields
(result_digest, rule_sentence_digest, rule_proof_id) against the supplied
capture rather than rebuilding an expected attribution.

**Consequences:** TraceAttribution is a prototype proving attribution survives
store/reload with identity intact. It does not invoke a runtime, authorize
promotion/write, enable live integration, change dependencies, use paid
compute, or perform a remote action. General trace decoding, reviewed
promotion/write, upstream repair adoption, and live integration remain
separate gates.

# 2026-08-09: Type kernel sentence provenance members before sorting

**Decision:** Validate every immutable kernel sentence stamp as a non-negative
integer and every evidence-basis id as a non-empty string before applying
uniqueness and ordering checks.

**Rationale:** Sorting is a semantic validation step, not an acceptable source
of public exceptions. Reconstructed mixed-type tuples must fail through the
stable typed boundary instead of exposing Python comparison behavior.

**Consequences:** Valid compiler output is unchanged. This closes local
metadata admission only and authorizes no runtime invocation, promotion/write,
live integration, dependency change, paid compute, or remote action.

# 2026-08-09: Normalize malformed capsule merge metadata before traversal

Decision: retain the public iterable API for optional evidence-basis metadata,
but explicitly convert it to an iterator and normalize a non-iterable input to
`ValueError` before reading members.

Rationale: lists and generators are intentional callers, so requiring a tuple
would be an unnecessary compatibility break. A malformed scalar should still
fail through the same typed public boundary as malformed metadata members.

Boundary: valid merge semantics and identities are unchanged. This does not
invoke a runtime, authorize promotion or writes, enable live integration,
change dependencies, use paid compute, or perform a remote action.

# 2026-08-09: Evidence packet schema versions are explicitly typed

Decision: require `EvidencePacket.schema_version` to be an integer (and not a
boolean) before applying the positive-version constraint.

Rationale: reconstructed packets are a public immutable evidence boundary.
Malformed schema metadata must fail through its stable `ValueError` contract,
not leak a Python comparison `TypeError` before downstream snapshot admission.

Boundary: valid packets and serialized identity are unchanged. This is local
contract hardening only and does not invoke a runtime, authorize promotion or
writes, enable live integration, change dependencies, use paid compute, or
perform a remote action.

# 2026-08-08: Evidence capsules contain an immutable typed collection

Decision: require `EvidenceCapsule.contributions` to be an actual tuple whose
members are all `EvidenceContribution` records before reading their basis IDs.

Rationale: a frozen capsule retaining a caller-owned list can change after
validation, invalidating evidence counts and basis identity. Type validation
also keeps malformed direct callers within the stable `ValueError` contract.

Boundary: valid algebra/builders are unchanged. This is local contract
hardening only and does not invoke a runtime, authorize promotion or writes,
enable live integration, change dependencies, use paid compute, or perform a
remote action.

# 2026-08-08: Evidence packet provenance collections are tuple-backed

Decision: require `EvidencePacket.token_ids` and `parent_packet_ids` to be
actual tuples at reconstruction time.

Rationale: these collections define the packet's evidence and derivation
provenance. A frozen dataclass retaining a caller-owned list could change after
validation, invalidating downstream snapshot and basis identities.

Boundary: valid builder output is unchanged. This is local contract hardening
only and does not invoke a runtime, authorize promotion or writes, enable live
integration, change dependencies, use paid compute, or perform a remote action.

# 2026-08-08: Stock episode manifest collections are tuple-backed

Decision: require `EpisodeManifest.parent_episode_ids` and
`projection_policy_ids` to be actual tuples at reconstruction time.

Rationale: a frozen dataclass does not make caller-owned list members
immutable. These collections contribute to the manifest's audit identity and
must not change after validation. Rejecting lists preserves the declared typed
boundary instead of silently retaining mutable aliases.

Boundary: this is local contract hardening only. It does not invoke a runtime,
authorize promotion or writes, enable live integration, change dependencies,
use paid compute, or perform a remote action.

# 2026-08-08: Kernel sentence provenance collections are tuple-backed

**Decision:** Require immutable tuples for every stamp and evidence-basis
collection in reconstructed `KernelSentenceMeta`.

**Rationale:** A frozen dataclass is not immutable when it retains a
caller-owned list. These sidecars close compiled kernel inputs to their
evidence provenance and must remain stable after validation.

**Consequences:** Compiler-produced metadata is unchanged; reconstructed
metadata with mutable collections fails closed. This authorizes no runtime,
promotion/write, live integration, dependency change, paid compute, or remote
action.

# 2026-08-07: Bound checked-add text before canonical parsing

**Decision:** Type-check and independently cap reconstructed PeTTaChainer
statement atom and canonical-term text before parsing the term.

**Rationale:** Although compiler-built statements are already bounded, the
public frozen dataclass is reconstructible. Its duplicated typed term must not
be able to consume parser resources before the atom/content invariant rejects
it.

**Consequences:** Valid compiler output is unchanged. Oversized or non-string
reconstructed statement text fails closed before parsing. This authorizes no
runtime, promotion/write, live integration, dependency change, paid compute,
or remote action.

# 2026-08-07: Preserve the compiler's contiguous stamp space in PeTTaChainer contracts

**Decision:** Require the global stamp keys in each immutable PeTTaChainer
episode contract to be exactly the contiguous range from zero.

**Rationale:** The compiler establishes that invariant before adaptation.
Allowing reconstructed contracts to skip keys would make an incomplete audit
sidecar look like a complete compiler-derived episode.

**Consequences:** Compiler-produced contracts and shared evidence mappings are
unchanged; gap-bearing reconstructed contracts fail closed. This authorizes no
runtime, promotion/write, live integration, dependency change, paid compute,
or remote action.

# 2026-08-07: PeTTaChainer stamps and evidence bases are one-to-one

**Decision:** Require every immutable PeTTaChainer checked-add statement to
carry exactly one evidence-basis id for each retained stamp.

**Rationale:** Stamps and evidence bases are audit-only sidecars because the
public PeTTaChainer statement schema cannot carry them. Permitting unequal
cardinality would make that provenance ambiguous before the episode contract,
even though the downstream derived-result capture already requires closure.

**Consequences:** Compiler-produced valid statements are unchanged; malformed
partially mapped statements fail closed. This authorizes no runtime,
promotion/write, live integration, dependency change, paid compute, or remote
action.

# 2026-08-06: Typed PeTTaChainer builders reject malformed dependencies first

**Decision:** Require immutable typed fact/rule statements, stage captures, and
episode budgets at their public PeTTaChainer construction boundaries before
extracting any nested provenance fields.

**Rationale:** These objects define the compiler/runtime resource boundary.
Rejecting a malformed direct caller through one stable `ValueError` contract
keeps failure precedence deterministic and prevents incidental attribute errors
from becoming part of the API.

**Consequences:** Valid typed construction is unchanged. This closes only local
validation; it authorizes no PeTTaChainer runtime invocation, promotion/write,
live integration, dependency change, paid compute, or remote action.

# 2026-07-31: Treat OS process-launch rejection as a bounded runner failure

**Decision:** Translate `OSError` raised while launching the bounded kernel
subprocess into the runner's public `ValueError` contract while preserving the
original exception as its cause.

**Rationale:** Callers should be able to fail closed on one typed runner
boundary whether rejection occurs during preflight validation or at the OS
launch boundary. Exception chaining retains actionable diagnostics.

**Consequences:** A missing or OS-rejected executable no longer leaks a raw
platform exception. Runtime output/result admission, promotion/write, and live
integration boundaries are unchanged.

# 2026-07-30: Treat frozen Phase-0 output shape as semantic evidence

**Decision:** Admit the declared result and successful marker only when each
appears exactly once as its standalone producer-shaped output line.

**Rationale:** A substring occurrence proves neither that the runtime emitted
the declared result as a result nor that the marker has its recorded output
role. Exact line shape closes this ambiguity without interpreting arbitrary
runtime diagnostics.

**Consequences:** Rehashed captures that embed a valid atom in a larger line
fail closed. This remains read-only replay admission and authorizes no runtime,
promotion/write, or live integration.

# 2026-07-30: Phase-0 replay manifests have closed schemas

**Decision:** Treat every top-level and nested member in the frozen Phase-0
reference manifest as part of its exact v1 schema; reject undeclared fields.

**Rationale:** The clean-room reload gate must distinguish a frozen,
non-promoting archive anchor from a rehashed document carrying an unreviewed
authority claim. Validating only required known fields leaves that distinction
ambiguous to downstream consumers.

**Consequences:** Existing frozen reference manifests remain compatible, while
schema extensions require review and a version change. This is read-only
admission hardening prompted by the Phase-1 reload matrix; it authorizes no
runtime invocation, promotion/write, or live integration.

# 2026-07-25: Treat isolated stage labels as typed provenance

**Decision:** A PeTTaChainer derived-result capture admits only the exact
validator and runtime stage labels defined by the bounded one-rule gate.

**Rationale:** Content-addressing an arbitrary label proves what was recorded,
not that the recorded stage has the role claimed by its field. Exact role
labels prevent correctly rehashed validator/runtime substitution without
decoding opaque diagnostics.

**Consequences:** Capture reload remains non-promoting and compiler-bound.
Renaming either isolated stage requires an explicit schema/code review rather
than silently changing persisted provenance.

# 2026-07-23: Treat archive names as labels, not cross-run identity

**Decision:** A clean-room descriptor that reuses an archived episode/chart/context identifier set is not the same run unless its content-derived chart fingerprint, compiler output, validated result, and frozen program close together.

**Rationale:** Human-readable identifiers can collide across captures. Admission must rely on the existing content/provenance commitments rather than treating matching names as sufficient identity.

**Consequences:** The Phase-1 gate explicitly rejects a same-named altered-evidence descriptor without adding an accessor or changing any provenance schema, runtime, promotion/write, upstream, or live-integration boundary.

# 2026-07-22: Freeze filesystem hardening; proceed to bounded Phase-1 runtime capture/reload gate

**Decision:** Freeze further filesystem/provenance admission hardening. The 599-test descriptor-anchored boundary covering ownership, group-writable, inode drift, symlinks, hard links, special files, duplicate JSON, byte ceilings, nonblocking opens, trusted-parent metadata stability, and Unicode noncharacters is strong enough substrate evidence. Proceed to one bounded, non-live Phase-1 runtime capture/reload gate.

**Scope:**
- Clean-room roundtrip: capture a representative runtime memory state from frozen Phase-0 replay inputs, serialize through the admission boundary, reload in an isolated non-live harness, compare pre/post behavior.
- Three artifact classes: current runtime descriptors, legacy πPLN artifacts, frozen replay manifests.
- Adversarial cases: stale descriptors, provenance mismatch, duplicate anchors, wrong artifact class, cross-run descriptor collision.
- Promotion, writes outside sandbox, upstream adoption, and live integration remain explicitly closed.

**Success:** Deterministic reload, semantic equivalence on frozen probes, 100% rejection of malformed/provenance-invalid artifacts, no unlogged filesystem effects, stable descriptor identity across repeated cycles, and provenance distinction between "loaded from archive," "derived during capture," and "newly asserted after reload."

**Failure:** Semantic drift, nondeterminism, admitted stale/mismatched descriptor, unexplained write, or inability to distinguish artifact provenance after reload. On failure, declare the specific mode and pause; do not open an unbounded hardening branch.

**Rationale:** The hardening sequence has converged—each recent fix covers a narrower edge case with no concrete unresolved flaw. The next concrete risk is not filesystem integrity but whether admitted memory state remains semantically valid when captured and reloaded. More speculative hardening has diminishing returns unless the gate exposes a specific gap.

# 2026-07-21: Preserve artifact-creation failures across parent cleanup errors

**Decision:** When descriptor-anchored exclusive artifact creation fails, retain that failure as primary even if closing the already-open parent-directory descriptor also fails; attach the cleanup error as a diagnostic and leave no artifact.

**Rationale:** The creation failure is the actionable cause. Masking it with a cleanup error would obscure whether the path already existed, permissions failed, or the filesystem rejected creation.

**Consequences:** Regression coverage closes this combined failure path without changing publication semantics or opening runtime, promotion/write, upstream, or live-integration boundaries.

# 2026-07-18: A successful PeTTaChainer artifact write includes directory durability

**Decision:** Treat create-once derived-capture and episode-manifest publication as successful only after syncing both the completed artifact and its parent directory entry.

**Rationale:** File-only `fsync` protects content but does not guarantee that the newly created name survives a crash. These artifacts are replay/provenance anchors, so successful publication must include discoverability.

**Consequences:** Both PeTTaChainer writers share the same exclusive-create durable primitive and clean up on failure. This is persistence hardening only and authorizes no promotion, memory write, upstream adoption, or live integration.

# 2026-07-18: Give repaired PeTTaChainer captures a distinct non-promoting manifest

**Decision:** Adapt an admitted `PeTTaChainerDerivedResultCapture` into a PeTTaChainer-specific manifest that content-addresses the complete checked-add/query contract and records the repaired source/profile, runtime/controller identities, explicit budget, seed, and timestamps. Do not coerce it into the stock patham9 `EpisodeManifest`.

**Rationale:** The patham9 manifest hashes retained raw process streams and closes one result stamp set directly to evidence bases. The bounded PeTTaChainer runner intentionally retains only stream byte counts/digests and preserves fact and rule stamps/evidence bases separately. Reusing the stock type would overstate the captured evidence or require lossy provenance flattening.

**Consequences:** The new typed manifest closes exact compiler/result sidecars and structurally requires `promotion_authorized=False`. Create-once manifest persistence/reload is the next bounded gate. No inferred-belief promotion, journal write, upstream repair adoption, or live OmegaClaw/GoalChainer integration is authorized.

# 2026-07-17: Admit repaired compileadd only with exact stored-fact evidence

**Decision:** Retry one real `compileadd` only after the exact duplicate-import repair, fact-dispatch, and `mm2compile` source gates pass, and require both the expected externalized return and an exact direct match for the internalized atom in `&kb`.

**Rationale:** Completion of `mm2compile` establishes conversion readiness but does not prove the later internalization and KB-add steps completed. A return value alone could likewise be detached from storage. Exact membership closes this narrow add-only boundary without invoking the query compiler.

**Consequences:** The tested promoted-fact shape is admitted for isolated add readiness. Query compilation/execution and typed result admission remain the next separate gate; no upstream source modification, inferred-belief promotion, memory write, or live OmegaClaw/GoalChainer integration is authorized.

# 2026-07-16: Attribute the residual direct-dispatch factor to duplicate registration, without patching imports

**Decision:** Compare the twice-imported direct `compile_` with one source-equivalent locally registered concrete-fact definition only after confirming both pinned import paths and the exact fact-dispatch shape.

**Rationale:** Internal source-gated probes accounted for 64 identical fact-clause results, while direct `compile_` returned 128. `petta_chainer.metta` imports `chainer/compile` directly and again transitively through `context_from_kb -> context_generation`; the single local registration returned exactly 64 and direct dispatch exactly 128, both with one unique result.

**Consequences:** The observed direct fact-dispatch multiplicity is now source-localized, but this diagnostic does not establish that removing the transitive import is safe for other consumers or that general result deduplication preserves semantics. Upstream import changes, set collapse, `mm2compile`, `compileadd`, query/result admission, promotion/write, and live integration remain separately gated.

# 2026-07-16: Diagnose dispatch multiplicity before considering set collapse

**Decision:** Treat the literal fact branch as multiplicity-free for the exact promoted-fact shape and instrument the public `compile` wrapper versus direct `compile_`, then its nested dispatch conditions, before designing any deduplicating/set-collapse boundary.

**Rationale:** The exact source-gated ladder returned one copy for the base clause, an explicit empty second arm, and the real empty `compile-outputs` arm after substituting the unique literal KB. The separately measured `compile-fact-kb` contributes 8x while public `compile` returns 256x, leaving 32x above the literal branch. Collapsing now would hide the responsible dispatch semantics and could discard intentional nondeterminism for other statement types.

**Consequences:** Keep `mm2compile`, `compileadd`, query/result admission, manifests, belief promotion/write, and live integration closed. The next diagnostic should compare public `compile` with direct `compile_` under the exact contract and remain source-gated, bounded, and non-mutating.

# 2026-07-15: A captured episode commits to its delivered program

**Decision:** Record a canonical content identity for the exact program supplied to every successful bounded kernel subprocess, and require captured manifest construction to match that identity against its `complete_program` argument.

**Rationale:** Binding result admission and process outputs to one immutable capture still allowed a caller to pair that capture with a different complete program when constructing the manifest. Successful pipe delivery alone was not retained as auditable input provenance.

**Consequences:** The captured manifest constructor now closes compiled program input and process outputs through one capture. Older or synthetic captures without a matching program commitment may still support isolated result validation but cannot construct a captured episode manifest. This does not prove semantic consumption, rule/trace identity, promotion eligibility, or live integration safety.

## 2026-07-12: piPLN evidence snapshots are create-once checksummed documents

**Decision:** Persist typed `EvidenceSnapshot` records as canonical, checksummed v1 JSON documents created with exclusive file creation; never replace an existing snapshot path.

**Rationale:** A snapshot identifies a frozen evidence selection and semantic versions. Silent replacement would invalidate replay and provenance. Schema and payload checksums provide a small fail-closed boundary before adding a snapshot repository/index.

**Consequences:** Snapshot callers must choose a new path/id for changed evidence. The current slice does not implement discovery/indexing, runtime derive, memory promotion, or live integration.

## 2026-07-12: Snapshot discovery is content-addressed and validates the whole repository

**Decision:** Store snapshot documents under `<snapshot_fingerprint>.json` and scan/validate the complete bounded repository before listing or ID lookup.

**Rationale:** The semantic fingerprint is the stable content address, while logical snapshot IDs are operator-facing identities. Validating all entries prevents malformed or duplicate records from being hidden by an otherwise successful point lookup.

**Consequences:** Unexpected files, filename/fingerprint drift, duplicate logical IDs, and missing IDs fail closed. This remains a local immutable snapshot index, not a mutable database, episode compiler, or runtime integration.

## 2026-07-13: Chart fingerprints cover complete immutable chart identity

**Decision:** Hash selected packet IDs, adequacy-certificate identity, and kernel-projection policy into `PiChart.chart_fingerprint`, beyond the SDS section 6.2 minimum, and reject empty, blank, or duplicate packet selections.

**Rationale:** These fields can change chart semantics or admissibility. Allowing them to vary under one fingerprint would make compiled-artifact caching and future replay ambiguous; silently deduplicating input would also conceal malformed selection artifacts.

**Consequences:** Unequal chart selections, adequacy reviews, or kernel projection policies now receive unequal fingerprints. Existing chart fingerprints produced before local commit `67e6ee9` are compatibility-era identities and should not be mixed with new cache entries. This does not compile or execute an episode.

## 2026-07-13: Charts bind to validated snapshot content, not caller-supplied snapshot IDs

**Decision:** Require `build_pi_chart()` callers to supply an `EvidenceSnapshot`; verify context equality and selected-packet membership, then record and hash both its logical ID and semantic fingerprint.

**Rationale:** Accepting packet IDs and a snapshot ID independently allowed charts to claim evidence not present in the snapshot, and allowed changed snapshot content under a reused logical ID to collide in future compilation caches. The normative replay boundary requires immutable evidence to be frozen before chart validation and compilation.

**Consequences:** Callers must load or construct a validated snapshot before chart construction. Charts with changed evidence content receive different fingerprints even if the logical snapshot ID is reused. This remains a typed, non-live Phase-1 boundary and does not compile or execute an episode.

## 2026-07-12: Preserve the legacy EC projection serialization while labeling its policy

**Decision:** Identify `ec_projected_stv()` as compatibility policy `adapter-weighted-v1` through a module constant and function introspection metadata, without adding policy metadata to its returned dictionaries.

**Rationale:** Existing wrapper outputs and artifacts are compatibility baselines. They must remain byte/shape stable while the implementation clearly distinguishes the old confidence-weighted adapter from the canonical count/prior chart projection.

**Consequences:** New code can inspect the adapter identity directly, but consumers requiring the canonical projection must call the typed `pipln_models` functions instead. No runtime or serialized handoff behavior changes in this slice.

## 2026-07-13: Begin Phase 2 with a pure, provenance-closing compiler boundary

**Decision:** Compile chart-local patham9 Sentence inputs only after exact chart/snapshot, packet-selection, and packet-derived-basis validation. Keep runtime invocation, program/rule assembly, manifest persistence, and result decoding outside this first compiler function.

**Rationale:** Deterministic compilation can be tested without conflating it with the noisy legacy kernel. Exact input closure and immutable sentence sidecars establish the evidence/stamp/projection provenance needed by later manifests and replay.

**Consequences:** `compile_episode_inputs()` accepts no extra or missing packets/bases, assigns basis stamps deterministically, and records each sentence digest, canonical term, projection ID, chart/context identity, stamps, and evidence bases. It does not claim a completed Phase-2 runtime or replay implementation.

## 2026-07-13: Persist compiler output before assembling or running a kernel program

**Decision:** Store exact `CompiledEpisodeInputs` as a create-once, checksummed v1 JSON artifact and fully reconstruct its typed records on load before adding rule/program assembly or runtime fields.

**Rationale:** The generated Sentence atoms, projections, stamp map, and provenance sidecars are the deterministic replay inputs. Freezing this boundary independently makes compiler drift and tampering testable without conflating them with patham9 output, timestamps, budgets, or process behavior.

**Consequences:** A recomputed outer checksum is insufficient to admit changed sentence atoms or inconsistent stamp-to-basis mappings because typed inner invariants are revalidated. This artifact is a precursor to, not a substitute for, the SDS `EpisodeManifest`; it has no kernel invocation, result, trace, or promotion semantics.

## 2026-07-13: Treat compiled packet statements as bounded data, never kernel control

**Decision:** Before forming patham9 `Sentence` inputs, parse every packet statement as exactly one S-expression list, canonicalize it, reject executable/control heads at any nesting depth, and enforce explicit sentence and emitted-character budgets. On artifact load, require the serialized atom to equal the atom reconstructed from typed canonical-term, projection, and stamp metadata.

**Rationale:** EvidencePacket text crosses a future evaluator boundary. String interpolation alone permits malformed multi-form input, control-form smuggling, and atom/sidecar divergence even when an attacker or faulty producer can recompute checksums.

**Consequences:** The current compiler admits only bounded declarative data terms and fails closed on malformed/control-bearing statements and semantic artifact drift. The denylist is a Phase-2 compatibility guard, not a complete language-fragment capability system; runtime assembly/execution remains separately deferred and gated.
## 2026-07-13: Evidence snapshots expose per-packet content commitments

**Decision:** Version snapshot persistence to `petta-memory-pipln-evidence-snapshot-v2`, store an ordered digest for every packet's complete frozen semantic payload, derive the snapshot fingerprint from those commitments and context identities, and require episode compilation to match supplied packets against them.

**Rationale:** A global snapshot fingerprint proves content only when the original packet collection is available. The compiler receives packets separately; checking IDs alone allowed changed statements, counts, or semantic metadata to be projected while retaining the old chart/snapshot identity.

**Consequences:** v1 snapshot artifacts fail closed rather than being silently upgraded. Callers must rebuild snapshots under v2. Program assembly remains deferred until this packet-content boundary is trustworthy; no runtime or promotion semantics are added.

## 2026-07-13: Validate kernel result structure and episode stamps before decoding proofs

**Decision:** Admit a raw patham9 result only when it is one bounded `((stv S C) (stamps...))` data atom with finite unit-interval values and canonical stamps that all resolve through the exact compiled episode stamp map. Bind the validated value to canonical query, episode/chart identity, evidence-basis IDs, and a semantic digest.

**Rationale:** Shell success and semantic `Passed:` markers do not establish output structure, numeric safety, or provenance closure. Proof/trace decoding and manifests must not consume unknown stamps or injected trailing forms.

**Consequences:** Structurally valid results become typed ephemeral artifacts, but validation does not claim rule identity, replay completeness, or promotion eligibility. Runtime capture, trace decoding, complete manifests, and exact replay remain separate Phase-2 gates.

## 2026-07-14: Persist validated kernel output only against its compiled episode

**Decision:** Store `ValidatedKernelResult` as a create-once checksummed v1 document and require its episode/chart identity, canonical stamps, and evidence-basis IDs to close against caller-supplied immutable `CompiledEpisodeInputs` on every load.

**Rationale:** A result's own digest and an outer checksum detect ordinary drift but do not independently prove that its stamps still name the evidence bases used by the compiler. Replay consumers need both typed reconstruction and an explicit comparison to the frozen input artifact.

**Consequences:** Validated output can now be retained for later manifest and replay comparison work without treating it as an inferred-belief promotion or runtime proof. Generated rule identity, trace capture, complete manifests, kernel re-execution, and reviewed promotion remain separate gates.

## 2026-07-14: Define exact replay at the typed semantic boundary

**Decision:** Compare a fresh replay output only after both the persisted expectation and fresh output close against the same immutable `CompiledEpisodeInputs`; require equality of the canonical typed result digest rather than byte-for-byte output text.

**Rationale:** Patham9 may render equivalent numeric atoms or whitespace differently, while a changed truth value, stamp set, query, or evidence basis is semantically material. Raw string equality is too brittle, but comparing values before episode provenance validation is too permissive.

**Consequences:** Callers can now test exact semantic replay deterministically without confusing formatting drift with inference drift. The gate does not invoke the kernel or establish runtime version, rule bundle, trace identity, or promotion eligibility; those remain required for complete replay and EpisodeManifest work.

## 2026-07-14: Episode manifests content-address the complete supplied run boundary

**Decision:** Implement the SDS section 16.2 manifest as an immutable typed artifact whose constructor closes chart, snapshot, compiled inputs, and validated result; hashes the complete supplied program, exact stamp map, and captured process streams; and records pinned runtime/controller identities, seed, explicit budget, timestamps, and return code. Require every compiler-emitted Sentence to occur exactly once in the bounded program.

**Rationale:** Replay comparison without a manifest cannot establish which program, kernel policy, budget, or process output produced the expected result. Deriving content identities at the constructor boundary prevents callers from freely pairing a result with unrelated compiled inputs or an incomplete program.

**Consequences:** A completed caller-supplied episode can now be retained as a create-once checksummed audit record, and recomputing only the outer checksum cannot conceal field drift because the typed manifest digest is revalidated. The constructor does not run patham9, establish stable rule/trace identity, authorize promotion, or cross a live OmegaClaw/GoalChainer boundary; those remain separate gates.

## 2026-07-14: Legacy kernel programs use one fixed query template

**Decision:** Assemble Phase-2 stock patham9 query input only from immutable compiler-emitted Sentences and one canonical declarative query under fixed `PLN` import/init/query controls and explicit bounded queue/step parameters. Do not accept caller-supplied imports, rules, control forms, or complete program fragments at this boundary.

**Rationale:** The legacy kernel is an evaluator. Allowing arbitrary program text would collapse the validated evidence/data boundary into a code-execution boundary and make compiled-program identity too weak for later replay and manifest checks.

**Consequences:** The assembler is deterministic, fails closed on noncanonical or executable query terms and excessive budgets, and returns inert text only. Subprocess execution, environment/runtime pinning, captured-output parsing, trace/rule attribution, promotion, and live integration remain separately gated.
## 2026-07-14: Patham9 entry points are control forms, not declarative terms

**Decision:** Reject `PLN.Config`, `PLN.Init`, `PLN.Query`, and `PLN.Derive` recursively wherever the Phase-2 compiler/assembler admits caller-derived packet statements or query terms.

**Rationale:** At pinned patham9 revision `55f1751`, these symbols are evaluator/configuration entry points. They may look like ordinary S-expression heads before import, but the fixed assembled program imports `PLN`; admitting them through a data boundary would allow control behavior to be smuggled inside evidence or the query.

**Consequences:** Declarative inputs using these reserved heads now fail closed, including nested occurrences. The fixed assembler remains the sole owner of `PLN.Init` and `PLN.Query`; this does not execute the kernel or establish a complete language capability system.
## 2026-07-14: Bound kernel stdin by encoded bytes before launch

**Decision:** Require `run_kernel_subprocess()` to enforce an explicit positive program-byte ceiling on the UTF-8 encoding before starting the kernel process.

**Rationale:** The assembler's character ceiling does not protect independent runner callers and character counts do not equal transmitted bytes. A subprocess boundary should reject oversized input before allocating child-process resources.

**Consequences:** Runner calls now default to the existing episode-program ceiling and can choose a smaller positive limit. This is a resource gate only; it does not validate program semantics, execute patham9 during tests, or authorize promotion or live integration.
## 2026-07-14: Bound kernel argv by encoded bytes before launch

**Decision:** Enforce a positive aggregate UTF-8 byte ceiling over the complete kernel subprocess argv and reject embedded NULs before invoking the operating system.

**Rationale:** Bounding the assembled program and captured streams leaves a separate launch-input resource boundary open. Character counts also undercount multibyte arguments, while NUL-bearing arguments otherwise fail later at an OS-dependent boundary.

**Consequences:** The shell-free runner now defaults argv to 16 KiB and callers may select a smaller positive limit. This does not validate executable provenance, run patham9 in tests, establish rule/trace identity, or authorize promotion or live integration.
## 2026-07-14: Bound optional kernel working-directory input before launch

**Decision:** Normalize an optional kernel subprocess `cwd` through the filesystem path protocol, reject empty/non-string paths and embedded NULs, and enforce a positive aggregate UTF-8 byte ceiling before starting the child.

**Rationale:** Program and argv bounds did not cover the remaining caller-controlled launch-path input. Multibyte paths can exceed character-based assumptions, while malformed paths otherwise fail later at an OS-dependent boundary.

**Consequences:** The shell-free runner defaults `cwd` to a 4 KiB ceiling and fails closed before launch. This does not pin executable/environment provenance, run patham9 in tests, establish rule/trace identity, or authorize promotion or live integration.
## 2026-07-14: Bound explicit kernel environments before launch

**Decision:** Allow the Phase-2 raw kernel runner to receive an optional explicit string environment mapping, but validate process-safe keys/values and cap its aggregate UTF-8 size before starting a child. Preserve inherited-environment behavior when the option is omitted.

**Rationale:** Program, argv, cwd, and output bounds left one launch input unbounded. An explicit environment is useful for a later pinned runtime, but it must not bypass resource and OS-input validation.

**Consequences:** Reviewed callers can supply a small isolated environment; invalid or oversized mappings fail before execution. This does not pin the runtime by itself, validate semantic output, authorize promotion/write, or enable live OmegaClaw/GoalChainer integration.
## 2026-07-14: Permit reviewed callers to pin the kernel executable by digest

**Decision:** Let the shell-free Phase-2 runner optionally require an exact lowercase SHA-256 digest of the absolute executable file before process creation.

**Rationale:** Bounded argv and environment inputs do not establish which executable bytes a reviewed episode intended to run. An opt-in digest makes accidental or ordinary on-disk drift fail closed without forcing inherited-development callers into a runtime policy prematurely.

**Consequences:** Invalid pins, relative command lookup, unreadable files, and digest mismatch fail before launch. This is not a complete isolation or attestation mechanism: filesystem replacement between hashing and exec remains possible, and semantic result validation, manifest closure, promotion, writes, and live integration remain separate gates.

# 2026-07-15: Phase-0 baseline freeze is tiered; one stock Smokes reference artifact must precede the end-to-end episode gate

**Decision:** Split the Phase-0 baseline freeze into two tiers. Tier 1 (must precede the gate): a pinned reference episode artifact — exact input program, executable/kernel hash, runtime-version manifest, and canonical expected output — as the fixed replay target. Tier 2 (concurrent or after): broader stock-episode corpus coverage, expected semantic-failure classification, and rule/trace identity formalization.

**Rationale:** Exact-replay determinism without a frozen reference anchor only proves the pipeline reproduces *something* consistently, not that it reproduces the *correct* thing. The Phase-2 replay/validation apparatus (497 tests, `validate_exact_kernel_replay()`, `EpisodeManifest`) has never been run against a real patham9 kernel result. An untethered gate would silently ratify whatever the current pipeline happens to produce — the runtime analogue of exporting an unpromoted quote as a premise, which PROJECT.md's core invariant forbids.

**Consequences:** The first end-to-end episode gate must be anchored to a committed pinned reference artifact. The Smokes example (multi-premise inference with derived truth-value computation) was chosen over FlyingRaven (single-step inheritance) because it exercises rule selection, truth-value arithmetic, and result-atom construction simultaneously. Two consecutive runs produced byte-identical output (SHA-256 `fd5a6133deca5c88f6170be634bc0f5101259ba3f685abb9c6fec5babc1f893e`), confirming determinism for v0 exact-replay. Rule/trace identity ambiguity (byte-identical traces from structurally distinct rule applications) remains a genuine unresolved risk for post-integration boundary testing. Reference artifact committed at `artifacts/phase0-reference-smokes-55f1751/`.

# 2026-07-15: Enforce subprocess capture budgets during pipe consumption

**Decision:** Drain kernel stdout and stderr concurrently into byte-bounded buffers, terminate the child immediately when either stream crosses its ceiling, and write stdin concurrently under the same process timeout.

**Rationale:** Checking `subprocess.run()` buffers after process completion did not provide the resource bound claimed by the API and allowed arbitrary child output to accumulate in memory. Sequential large stdin delivery could also block before timeout handling began.

**Consequences:** Capture memory is bounded to at most the configured ceiling plus one reader chunk per stream, and timeout covers blocked stdin as well as process execution. Captures remain raw and confer no semantic result, trace, promotion, write, or live-integration authority.
## 2026-07-15: Require complete kernel program delivery

**Decision:** Treat any broken/failed stdin write or flush as capture failure, even when the kernel process exits successfully and emits otherwise parseable output.

**Rationale:** A capture cannot establish that it corresponds to the content-addressed assembled program if the child consumed only a prefix or none of that program. Silently ignoring `BrokenPipeError` weakened later manifest and replay provenance.

**Consequences:** Early stdin closure now fails closed before raw capture is returned. This proves delivery to the operating-system pipe, not semantic consumption or execution; result validation, manifest closure, promotion, writes, and live integration remain separate gates.

## 2026-07-15: Count serialized process framing inside launch ceilings

**Decision:** Count terminating NULs in argv/cwd budgets and `KEY=VALUE\0` framing in explicit-environment budgets. When executable pinning resolves a symlink, recheck the complete resolved argv against the same ceiling before hashing and launch.

**Rationale:** Payload-only counts understated the bytes represented at the OS process boundary, and a longer resolved executable path could bypass an argv check performed only on the caller's symlink spelling.

**Consequences:** Configured ceilings now apply literally to serialized launch inputs and fail before child creation. This remains a resource/provenance gate, not semantic runtime validation, filesystem attestation, promotion authority, a write path, or live integration.

## 2026-07-15: Admit the frozen replay anchor before launching the end-to-end gate

**Decision:** Require the first end-to-end Phase-2 episode runner to consume a `Phase0ReferenceArtifact` returned by fail-closed local manifest/content validation, rather than accepting an unchecked manifest dictionary or expected-result string.

**Rationale:** Committing a reference artifact establishes reviewable provenance, but does not itself prevent later file tampering, hash drift, relaxed non-live flags, or substitution of an unpinned runtime/kernel identity. The replay gate needs a typed admission boundary before any subprocess is started.

**Consequences:** The current Smokes source/output artifact now closes exactly and can serve as the next runner's anchor. Runtime launch, fresh semantic-result parsing/comparison, EpisodeManifest creation, trace/rule attribution, promotion, writes, and live OmegaClaw/GoalChainer integration remain separate gates.
# 2026-07-15 — Phase-0 fresh replay admission is byte-exact and stderr-clean

**Decision:** A fresh stock-kernel reference replay is admitted only when the bounded process exits zero, emits no stderr, and its UTF-8 stdout exactly matches the admitted reference byte count and SHA-256 while retaining the expected semantic result and pass marker.

**Rationale:** Exit status and marker parsing alone are too weak for the frozen deterministic anchor. Exact output closes the current replay contract without claiming rule/trace identity or promoting the result.

**Consequences:** The successfully reproduced Smokes capture is a Phase-0 replay result only. Phase-2 episode construction must separately close compiled inputs, program/stamp identities, validated result, runtime budget, and manifest persistence.

## 2026-07-15: A Phase-2 result must be demonstrably present in its successful capture

**Decision:** Before a raw kernel result can enter typed Phase-2 validation, require its exact atom to occur in bounded stdout from a zero-exit process with empty stderr.

**Rationale:** Validating a caller-supplied atom separately from process capture permits accidental or malicious pairing of a sound typed result with an unrelated, failed, or noisy execution. Verbatim presence provides a narrow auditable origin link while leaving semantic normalization to the existing typed validator.

**Consequences:** Nonzero exits, any stderr, and detached result atoms fail closed. This does not prove semantic consumption of the complete program, identify the applied rule/trace, build or persist an EpisodeManifest, authorize promotion/write, or enable live integration.
## 2026-07-15: Result admission and manifest construction share one immutable capture

**Decision:** Provide one Phase-2 constructor that validates a result atom against a `KernelProcessCapture` and copies process audit fields into the `EpisodeManifest` from that same capture.

**Rationale:** Separate result validation and manifest construction allowed a caller to accidentally validate one process capture while manually supplying another process's return code or output to the manifest builder.

**Consequences:** Successful end-to-end audit construction no longer has a capture-substitution seam. This constructor remains non-promoting and does not by itself execute a real compiled episode, identify rules/traces, persist a manifest, write memory, or enable live integration.
# 2026-07-15: Require a specialized-kernel readiness proof before the first real Phase-2 manifest

**Decision:** Do not treat a zero-exit generic `PLN.metta` process as a usable Phase-2 kernel. Before constructing the first real compiled-input `EpisodeManifest`, require the compiler-emitted program to produce an admitted typed result with no stderr under the exact generic MeTTaMorph/PeTTaChainer build or `compileadd` contract.

**Rationale:** A bounded empirical probe resolved the `PLN` module and launched the pinned runtime successfully, but the compiler-emitted direct-fact query returned `[()]` and emitted derivation trace output on stderr. The pinned inversion control left `Truth_inversion` unevaluated and failed semantically. By contrast, the Phase-0 Smokes anchor uses an example-specialized `SMOKES.so`; its success cannot establish readiness of the generic compiler-to-kernel path.

**Consequences:** Existing stderr-clean and typed-result admission remains fail closed. The next work item is the bounded PeTTaChainer/MeTTaMorph compilation contract, followed by repetition of the same compiler-to-runtime probe. No manifest, inferred-belief promotion, memory write, or live OmegaClaw/GoalChainer integration may be claimed from zero exit alone.

## 2026-07-15: Keep patham9 Sentence and PeTTaChainer checked-add schemas explicit

**Decision:** Adapt immutable compiled episode inputs to PeTTaChainer with a separate typed contract. Emit `(: pm-<full-sentence-digest> term (STV strength confidence))` for checked add and `(: $prf term $tv)` for query; retain patham9 stamps and evidence-basis identities in audit sidecars rather than embedding them into an unsupported PeTTaChainer field.

**Rationale:** Source and empirical inspection established two distinct compilation systems. Stock patham9 consumes `Sentence` records and builds an episode-specialized MeTTaMorph shared object. PeTTaChainer's validator/compiler consumes three-field `:` proof statements through `compileadd`. Passing one schema to the other produced a zero-exit but semantically empty result and would obscure which compiler contract was actually tested.

**Consequences:** The adapter is deterministic, bounded, non-executable, and content-addresses proof ids with the complete compiler sentence digest. PeTTaChainer validation, `compileadd`, query execution/result decoding, patham9 specialized builds, manifest construction, promotion/write, and live integration remain separate fail-closed gates.

## 2026-07-16: PeTTaChainer runtime probes require exact validator admission and a non-empty bounded query

**Decision:** Run the typed episode contract through PeTTaChainer only after every public statement validator and the query validator return exact numeric `1.0`. Execute add/query in one isolated subprocess, and admit runtime completion only when both recorded stages succeed and the query returns a non-empty list.

**Rationale:** Schema validation and `compileadd` readiness are distinct. The pinned runtime validates the exact contract promptly but still times out in `compileadd`; treating validator success, process success, or an empty answer as inference success would recreate the generic patham9 false-positive boundary.

**Consequences:** Timeouts, errors, validator drift (including boolean `True`), malformed stage records, and empty answers remain auditable non-admissions. The current 15-second timeout is evidence of an add-path bottleneck, not a PLN result, and cannot support a manifest, promotion, write, or live integration.
# 2026-07-16: Bound retained materializer results and expose duplicate fan-out

**Decision:** PeTTaChainer materialization diagnostics retain the total and unique result counts but serialize at most 16 rendered result samples.

**Rationale:** The exact compiler-emitted one-statement contract materialized successfully but returned 512 identical outputs and generated roughly 797 KiB of runtime stdout. Persisting the complete duplicate list makes diagnostic artifacts needlessly large and obscures the useful signal: identity succeeded, multiplicity exploded, and the following `mm2compile` rung still timed out.

**Consequences:** Profile artifacts remain compact while preserving fan-out evidence and structural identity admission. This does not bound the external runtime's own stdout stream, establish `mm2compile` or `compileadd` readiness, admit a query result, construct a manifest, promote a belief, write memory, or enable live integration.
# 2026-07-16: Diagnose PeTTaChainer fact compilation before `mm2compile` collection

**Decision:** Probe the source-selected `compile_` fact-assertion branch directly in an isolated bounded subprocess, cap retained output samples, and stop before `mm2stmt`, temporary-context collection, `compileadd`, or query.

**Rationale:** Materialization and complete `mm2compile` both showed heavy or timeout-bound behavior. Direct fact dispatch distinguishes compiler fan-out from the later clause conversion/context machinery without adding compiled atoms to a knowledge base.

**Consequences:** The exact contract completes direct compilation but fans out to 256 identical base-fact clauses, localizing multiplicity before context collection. This is diagnostic evidence only and cannot admit a PLN result, construct a manifest, promote/write memory, or enable live integration.
# 2026-07-16: Deduplicate compiler output before diagnosing `mm2stmt` and temporary context

**Decision:** Construct one source-equivalent base-fact clause from an already source-gated fact statement, pass that clause directly through `mm2stmt`, and inspect a separately cleared `ctx` space without invoking `compile`, `mm2compile`, or add/query paths.

**Rationale:** Direct `compile` returned 256 identical clauses, so feeding its complete output into the next rung would conflate compiler multiplicity with clause conversion and context collection. A one-clause diagnostic makes converter multiplicity and temporary-context effects independently observable.

**Consequences:** The exact fact clause converts quickly but still doubles, while `ctx` remains empty for this rung. This is diagnostic evidence only; it does not authorize deduplication inside PeTTaChainer semantics, establish `mm2compile` or `compileadd` readiness, admit a query result, construct a manifest, promote/write memory, or enable live integration.

# 2026-07-16: Attribute fact conversion doubling only under exact source overlap

**Decision:** Treat the two identical outputs from a zero-premise `mm2stmt` call as source-explained only while the pinned definition retains both its specialized zero-premise arm and its general premise-list arm.

**Rationale:** `(() |- ($ccl))` unifies with both patterns in the current PeTTaChainer source. Recording the exact definition distinguishes this local case overlap from compiler fan-out and prevents a stale diagnosis if upstream semantics change.

**Consequences:** The diagnostic fails closed on source drift and does not patch or deduplicate upstream behavior. The 256-copy `compile` fan-out, bounded `mm2compile`, `compileadd`, query/result admission, manifest, promotion/write, and live integration remain separate gates.
# 2026-07-16: Source-gate deduplicated mm2compile collection diagnostics

**Decision:** Measure `mm2compile` collection only by first confirming its exact pinned clear/convert/collect definition, then replacing the broad `compile` subexpression with one canonical source-equivalent fact clause inside an otherwise matching bounded expression.

**Rationale:** Direct `compile` returns 256 identical clauses and isolated `mm2stmt` returns two identical facts. Feeding broad compiler output into `mm2compile` conflates compiler, converter, and collection multiplicity; a source-closed one-clause rung distinguishes them without silently changing upstream semantics.

**Consequences:** The copied collector completes and returns four copies of one unique expected fact, locating another 2x multiplicity around collection after compiler fan-out is removed. This is diagnostic evidence, not authorization to deduplicate PeTTaChainer outputs; `compileadd`, query/result admission, manifests, promotion/write, and live integration remain gated.
# 2026-07-16: Decompose fact-branch multiplicity before considering set collapse

**Decision:** Measure `compile-fact-kb` and `compile-outputs` independently under an exact source-shape gate before adding any deduplication or set-collapse behavior to the PeTTaChainer add path.

**Rationale:** The 256-copy `compile` output could reflect distinct semantics as well as evaluator duplication. The component probe shows that `compile-fact-kb` contributes eight identical KB bindings and that `compile-outputs` contributes no adapters for this fact, narrowing the remaining unexplained factor without silently discarding outputs.

**Consequences:** The next diagnostic should isolate branching around direct fact-clause construction. No set-collapse policy is approved yet, and `mm2compile`, `compileadd`, query/result admission, manifests, promotion/write, and live integration remain gated.
# 2026-07-16: Separate public compile wrapper multiplicity from direct dispatch

**Decision:** Compare public `compile` and direct `compile_` in the same bounded runtime only after confirming the exact pinned one-step wrapper definition, and retain exact total/unique counts with bounded samples.

**Rationale:** The public definition has no explicit transformation, but evaluator matching can still introduce multiplicity at a wrapper boundary. Measuring both calls before copying nested conditions avoids attributing all 256 results to the fact branch or silently approving deduplication.

**Consequences:** Public `compile` returns 256 copies and direct `compile_` returns 128 copies of one unique clause, localizing one 2x factor to the wrapper/evaluator boundary. The remaining 16x above the literal branch should be isolated across nested dispatch conditions. No set-collapse policy, upstream patch, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration is authorized.
# 2026-07-16: Attribute nested fact-dispatch fan-out only under exact predicate shape

**Decision:** Diagnose the concrete-fact `compile_` selection path by rebuilding its variable-type, implication-pattern, and bidirectional-classification predicates over a literal fact clause, and run the ladder only while all three predicates and the fact branch match the pinned source.

**Rationale:** Direct `compile_` returned 128 copies although the literal fact branch returned one. Measuring the nested predicates separately distinguishes branch-classification multiplicity from `compile-fact-kb`, the annotated definition matcher, the public wrapper, and later collection/add stages without changing upstream semantics.

**Consequences:** The current pinned runtime attributes a 4x duplicate factor to `bidirectional-implication-type?`; the outer implication and variable-type predicates add none for this concrete fact. Annotation/definition dispatch and `compile-fact-kb` remain separate diagnostic boundaries. No deduplication policy, query result, promotion/write authority, or live integration follows from this measurement.

# 2026-07-16: Separate annotated matching from fact-dispatch body multiplicity

**Decision:** Attribute an annotated-head multiplicity factor only by comparing two locally registered concrete-fact definitions with identical bodies, one using the pinned `(@ $stmt (: $prf $Type $tv))` head and one using direct structural `(: $prf $Type $tv)` matching, after closing the exact pinned source shape.

**Rationale:** A single registered source-equivalent dispatcher still returned 64 identical clauses after duplicate imports were removed from the comparison. The already measured predicate ladder and `compile-fact-kb` account for 32, leaving the annotated matcher as the last unmeasured boundary rather than evidence that fact semantics require 64 distinct outputs.

**Consequences:** The annotated head returns 64 copies versus 32 for structural matching, completing the measured 256-copy public fact-path decomposition. This diagnostic does not approve changing upstream matching/import semantics or collapsing results; `mm2compile`, `compileadd`, query/result admission, promotion/write, and live integration remain gated.
# 2026-07-17: Repair source-local fact fan-out before testing set collapse

**Decision:** Treat the measured concrete-fact multiplicities as one closed arithmetic attribution and test source-local repairs in this order: duplicate compiler registration, overlapping zero-premise `mm2stmt` patterns, then the remaining matcher/evaluator factors. Consider byte-identical set collapse only as an experimental fallback after separate fact/rule semantic parity tests.

**Rationale:** The existing source-gated probes now explain the complete public compiler count (`1 * 8 * 4 * 2 * 2 * 2 = 256`) and deduplicated collection count (`1 * 2 * 2 = 4`). Collapsing outputs first could conceal duplicate imports or overlapping source patterns and would not remove their runtime cost.

**Consequences:** The repair-plan helper fails closed if any observed count no longer forms the measured factors. The next gate is an isolated pinned-checkout duplicate-registration experiment followed by the existing compile rungs. No upstream patch, set collapse, `compileadd`, query/result admission, manifest, promotion/write, or live integration is authorized by this decision.

# 2026-07-17: Treat duplicate-registration fan-out factors as coupled

**Decision:** Admit the isolated one-line duplicate-import candidate for further non-live testing, but do not infer that the prior per-rung multiplicities survive this repair or proceed immediately to the planned `mm2stmt` change.

**Rationale:** Under exact critical-file hashes, removing only `context_generation.metta`'s `chainer/compile` import reduced direct `compile_` from 128 copies of one clause to one normalized-equivalent output. The provisional repair-plan expectation was 64, so duplicate registration changes evaluator/matcher behavior across the other measured rungs rather than contributing an independent 2x factor.

**Consequences:** Rerun public wrapper, fact-KB, predicate ladder, annotated-head, `mm2stmt`, and collector gates on the single-import candidate before considering a second source repair. Keep upstream modification, set collapse, `mm2compile`, `compileadd`, query/result admission, manifests, promotion/write, and live integration closed.

# 2026-07-17: Retire the pre-repair public-wrapper factor

**Decision:** Treat the earlier public `compile` versus direct `compile_` 2x difference as invalid after the duplicate-import repair, and continue fresh downstream measurement rather than carrying that factor into a repaired-path model.

**Rationale:** On an exact single-import candidate, both entry points returned one identical clause; the baseline counts were 256 and 128. The one-line import repair therefore changes wrapper/evaluator multiplicity as well as direct dispatch multiplicity.

**Consequences:** The next bounded measurements are fact-KB, predicate ladder, annotated head, `mm2stmt`, and collector behavior on the same exact candidate. No second source repair or `compileadd` retry is justified yet, and no upstream, write, query, promotion, or live boundary changes.
# 2026-07-17: Do not repair the overlapping `mm2stmt` arms after registration collapse

**Decision:** Retain the current `mm2stmt` source while advancing the exact single-import candidate to a full bounded `mm2compile` gate.

**Rationale:** With one canonical fact, the single-import candidate returned one conversion and one copied-collector output even though the specialized zero-premise and general premise-list arms remain textually unchanged. The baseline returned two and four. The apparent arm/collector factors were therefore registration-coupled runtime behavior, not independent evidence that a second source edit is required.

**Consequences:** The next ordered gate is full repaired `mm2compile`, followed by `compileadd` only if it completes and preserves the expected fact. No upstream source change, query/result admission, promotion/write, or live integration is authorized.

# 2026-07-17: Advance the single-import candidate to an add-only compileadd retry

**Decision:** After exact source admission and a successful full `mm2compile` result, permit one bounded `compileadd`-only retry on the isolated single-import candidate before any query execution.

**Rationale:** The real repaired `mm2compile` path completed in 0.367 s with one unique expected fact, closing the earlier timeout boundary through compilation, conversion, and collection. Querying in the same step would conflate add readiness with inference/result admission and make a failure harder to localize.

**Consequences:** The next probe may invoke checked add only under the existing process bound and exact source hashes. Query/result admission, inferred-belief promotion, memory writes, upstream source modification, and live OmegaClaw/GoalChainer integration remain separately closed.
# 2026-07-17: Exact stored-fact retrieval is a separate non-promoting gate

**Decision:** After repaired `compileadd` admission, test retrieval in the same isolated process with a query constructed from the added fact, a positive explicit step bound, exact proof/type/STV matching, and an independent exact internal `&kb` membership check.

**Rationale:** Add success alone does not establish that PeTTaChainer's query compiler/runtime can retrieve the stored representation. Constructing the query from the admitted statement removes caller mismatch, while exact structural comparison (with numeric-rendering equivalence) prevents a merely non-empty answer from passing.

**Consequences:** The tested one-step stored-fact path is admitted. This is not inferred-result promotion or a Phase-2 episode result: runtime diagnostics remain noisy, and typed episode-contract admission, diagnostic classification, persistence, memory writes, and live integration stay separately gated.

# 2026-07-17: Exact-fact query admission closes over every returned answer

**Decision:** Admit the repaired PeTTaChainer stored-fact query only when its non-empty result set consists entirely of structural matches for the added proof/type/STV, allowing numeric rendering normalization.

**Rationale:** Requiring only that the expected answer be present could silently admit unrelated or over-broad query results while claiming an exact-answer boundary.

**Consequences:** Expected-plus-unrelated, empty, wrong, timed-out, and source-drifted results fail closed. This establishes only exact retrieval for the tested stored-fact shape; inference-result promotion, memory writes, upstream repair adoption, and live integration remain separate gates.
# 2026-07-17: Require content identity for completed PeTTaChainer query captures

**Decision:** A repaired exact-fact query can be admitted only when both OS-level captured streams have non-negative exact byte counts and lowercase SHA-256 identities.

**Rationale:** Byte counts alone distinguish volume but cannot establish whether two noisy PeTTaChainer executions emitted the same diagnostics or preserve evidence for later classification. Content addressing closes that provenance seam without returning hundreds of kilobytes in the gate artifact.

**Consequences:** Missing or malformed stream provenance now fails the exact-fact gate. The fresh probe's stdout and stderr are identifiable, but their semantic classification, typed episode-result admission, inferred-belief promotion, memory writes, upstream source adoption, and live integration remain separate gates.
# 2026-07-17: Classify the first repaired typed-contract result as stored-fact retrieval only

**Decision:** Admit a compiler-emitted `PeTTaChainerEpisodeContract` through the repaired path only when it contains one statement queried by that exact statement term, public validators return exact numeric admission, and the existing source/storage/complete-answer-set gate closes. Classify success as `stored-fact-retrieval`, not as a derived PLN result.

**Rationale:** The repaired add/query work now proves that PeTTaChainer can retrieve an immutable compiler-emitted input under the isolated import repair. It does not apply a rule, identify a proof trace, or convert opaque runtime diagnostics into typed inference evidence. Treating recall as inference would prematurely cross the Phase-2 semantic boundary.

**Consequences:** The compiler-to-runtime direct-recall rung is closed and content-addressed. Multi-statement/rule inference, diagnostic interpretation, `ValidatedKernelResult`/`EpisodeManifest` construction, promotion, memory writes, upstream repair adoption, and live OmegaClaw/GoalChainer integration remain separate gates.
## 2026-07-17: Require exact proof provenance for the first repaired derived result

**Decision:** Admit the first repaired PeTTaChainer one-rule result only when the query target differs from the stored fact, all answers have the requested target, every proof is exactly `(rule-proof <rule-id> <fact-id>)`, and every truth value is a finite unit-interval STV.

**Rationale:** Non-empty output or target matching alone cannot distinguish genuine rule application from stored-fact recall, unrelated answers, or malformed runtime data.

**Consequences:** The pinned probe is classified as a derived runtime result. It does not establish truth-formula provenance, bind an immutable compiler-emitted rule contract, authorize a manifest, promote/write inferred beliefs, or enable live integration.

## 2026-07-17: Admit a derived STV only against its exact source formula

**Decision:** Require the first repaired unary-implication result to close the exact `TotalMpConclusionFormula`/`TotalMpFormula` source shapes, the `(STV 0.2 0.2)` missing-complement fallback, and a numerical recomputation of every returned STV.

**Rationale:** Unit-interval validation alone cannot establish which truth-value formula produced a plausible answer. Source identity plus recomputation binds this narrow result to the actual pinned runtime semantics and fails closed on formula or fallback drift.

**Consequences:** The tested result now has exact truth-formula provenance. This still does not bind a compiler-emitted rule contract, construct an EpisodeManifest, authorize promotion/write, adopt the repair upstream, or enable live integration.

## 2026-07-18: Bind repaired derivation to compiler inputs before manifest work

**Decision:** Admit a compiler-bound PeTTaChainer one-rule result only from an immutable two-statement episode contract containing exactly one fact and one implication, with a query distinct from both stored inputs. Preserve both statements' sentence digests, content-addressed proof IDs, stamps, and evidence bases in the gate artifact, and reuse the existing exact proof and TotalMP runtime admission.

**Rationale:** The raw derivation gate proved rule execution and truth-formula identity but still accepted caller-supplied strings. Binding it to the compiler adapter closes that substitution seam and makes the expected runtime proof derive from immutable compiler identities.

**Consequences:** The derivation is now tied to compiler-emitted inputs and their audit provenance. A typed PeTTaChainer process/result capture remains necessary before adapting the patham9-specific `EpisodeManifest`; no promotion/write, upstream repair adoption, or live integration follows.

## 2026-07-18: Content-address the PeTTaChainer result before persistence or manifest adaptation

**Decision:** Represent an admitted compiler-bound derivation with separate immutable stage-capture and derived-result records. Require one unique retained answer, exact compiler proof/query identities, exact recomputed TotalMP truth values, retained fact/rule stamp and evidence-basis sidecars, and content digests for both isolated validator/runtime streams.

**Rationale:** The prior gate returned a nested mutable dictionary whose semantic result and process provenance could be copied or altered independently before later persistence. A digest-bound typed record closes that seam while honestly preserving only stream identities, not claiming semantic meaning for noisy diagnostics.

**Consequences:** The fresh pinned repaired run now yields one immutable result identity. Add create-once checksummed persistence and replay closure before designing a PeTTaChainer-specific EpisodeManifest adapter. No inferred belief is promoted or written, the source repair is not adopted upstream, and live OmegaClaw/GoalChainer integration remains closed.
# 2026-07-18: Persist repaired PeTTaChainer results only against their immutable compiler contract

**Decision:** Store a derived PeTTaChainer capture only as a create-once checksummed document containing both complete typed stage captures, and require reload to close the result's episode, query, fact/rule digests, proof IDs, stamps, and evidence-basis IDs against a supplied `PeTTaChainerEpisodeContract`.

**Rationale:** A result digest alone commits to its fields but does not ensure a later caller reloads it beside the compiler contract that produced those proof and audit identities. Persisting only stage digests would also prevent independent reconstruction and validation of the bounded process provenance.

**Consequences:** Document checksum drift, nested capture drift, typed semantic drift, and compiler-contract substitution fail closed. This creates an audit artifact only; PeTTaChainer-specific EpisodeManifest adaptation, promotion/write, upstream repair adoption, and live OmegaClaw/GoalChainer integration remain separate gates.
## 2026-07-18: Persisted PeTTaChainer JSON must have unique object members

**Decision:** Reject duplicate JSON object member names at every nesting depth before checksumming or reconstructing a persisted PeTTaChainer derived capture or episode manifest.

**Rationale:** Standard last-member-wins decoding can turn one text artifact into an ambiguous representation even if the decoded payload checksum and typed identities pass.

**Consequences:** Ambiguous documents fail closed before semantic admission. The change does not authorize inferred-belief promotion, memory writes, upstream repair adoption, or live OmegaClaw/GoalChainer integration.
## 2026-07-18: Persisted PeTTaChainer audit admission requires a direct regular file

**Decision:** Open derived-capture and episode-manifest JSON with no-follow semantics where the platform provides them, then require the opened descriptor to identify a regular file before reading.

**Rationale:** Checksums and compiler-provenance closure authenticate content but do not bind a path to a stable file. Following a symlink admits mutable path indirection, while special files do not have the bounded immutable-artifact behavior this boundary claims.

**Consequences:** Symlinks and non-regular inputs fail before JSON parsing. The existing create-once, byte-limit, duplicate-member, checksum, typed, and provenance gates remain in force. This grants no promotion, memory-write, upstream-change, or live-integration authority.
## 2026-07-18: Artifact type validation must not block on special files

**Decision:** Open PeTTaChainer JSON artifacts with nonblocking and no-follow semantics, then admit only regular files based on the opened descriptor.

**Rationale:** A FIFO opened read-only can wait indefinitely for a writer before `fstat()` runs, turning an otherwise fail-closed type check into a denial-of-service seam.

**Consequences:** FIFO paths now reach the existing regular-file rejection immediately; normal regular-file reads, checksums, provenance closure, and size bounds are unchanged. This authorizes no runtime execution, promotion, write, upstream adoption, or live integration.
# 2026-07-18: Retain a file-synced create-once artifact when directory fsync fails

**Decision:** After artifact content has been flushed and file-synced, propagate a later parent-directory fsync failure without unlinking the completed path. Continue removing partial output when failure occurs before completed file fsync.

**Rationale:** A failed directory fsync does not prove the directory entry was not persisted. Deleting the path can therefore erase a valid artifact in the running filesystem and allow a retry to replace an artifact whose crash-publication state is uncertain, weakening create-once semantics.

**Consequences:** Callers receive the durability error and must treat the operation as uncertain, while the completed artifact remains inspectable and exclusive creation prevents overwrite. This does not authorize promotion, memory writes, upstream adoption, or live integration.
# 2026-07-18: Anchor create-once publication to one parent directory descriptor

**Decision:** Open the destination parent directory once, create the artifact leaf relative to that descriptor, and fsync that same descriptor after the artifact file is synced.

**Rationale:** Creating through a pathname and later reopening the parent pathname permits a concurrent rename or path substitution to make the directory durability sync refer to a different directory than the one containing the created artifact.

**Consequences:** Artifact creation and directory-entry durability are bound to one opened directory identity. Existing files remain untouched when exclusive creation fails; pre-file-sync partial output is removed relative to that same directory; file-synced artifacts remain retained if directory sync fails. This grants no promotion, memory-write, upstream-change, or live-integration authority.
# 2026-07-19: Durably remove rejected partial PeTTaChainer artifacts

**Decision:** When create-once artifact file flush/fsync fails, unlink the partial entry through the already-open parent directory descriptor and fsync that directory before propagating failure.

**Rationale:** Unlink without a parent-directory sync leaves cleanup crash-uncertain; a rejected partial file could reappear after recovery and then block safe create-once replay.

**Consequences:** Pre-file-sync failure cleanup is now durable when cleanup itself succeeds. Completed file-synced artifacts remain preserved on later directory-sync failure. This does not authorize promotion, memory writes, upstream adoption, or live integration.
# 2026-07-19: Descriptor close failure must not mask artifact publication failure

**Decision:** When closing the anchored parent-directory descriptor fails during propagation of a PeTTaChainer artifact publication error, retain the publication error as primary and attach the close diagnostic. Propagate the close error normally when publication otherwise succeeded.

**Rationale:** Descriptor release is necessary cleanup, but its failure does not identify why artifact publication failed and must not replace a more actionable write/fsync error.

**Consequences:** Callers retain the primary failure and can inspect the secondary diagnostic; successful publication still reports descriptor-close failure. This grants no promotion, memory-write, upstream-change, or live-integration authority.
# 2026-07-19: Descriptor close failure must not mask artifact admission failure

**Decision:** When a PeTTaChainer artifact is rejected before its descriptor ownership transfers to the bounded reader, retain the admission exception as primary if descriptor close also fails and attach the close diagnostic. A close failure after otherwise successful descriptor handling still propagates normally.

**Rationale:** Descriptor cleanup failure does not explain why an artifact failed its no-follow, regular-file, size, JSON, checksum, or provenance boundary and must not replace the actionable rejection.

**Consequences:** Callers retain the primary admission diagnosis and can inspect the secondary close error. This grants no runtime, promotion, memory-write, upstream-change, or live-integration authority.
# 2026-07-19: Reject PeTTaChainer audit artifacts changed during admission

**Decision:** Compare stable descriptor metadata before and after the bounded artifact read and reject the document if device, inode, size, modification time, or change time differs.

**Rationale:** A regular-file check before reading does not prevent a concurrent writer from changing the file while bytes are consumed. Later JSON, checksum, and typed validation should operate on a stable artifact, not a race-dependent stream.

**Consequences:** Concurrently changed derived captures and episode manifests fail closed and may be retried only from a stable create-once artifact. This is a local audit-read boundary and grants no runtime, promotion, memory-write, upstream-change, or live-integration authority.
## 2026-07-19 — Audit artifacts require descriptor-size closure

PeTTaChainer JSON audit artifacts are admitted only when the bounded bytes read equal the stable regular-file descriptor size. A syntactically valid short read is not accepted merely because descriptor metadata remained unchanged around the read. This is a read-only provenance gate and grants no promotion or integration authority.
# 2026-07-19: Stream close failure must not mask artifact read failure

**Decision:** After a PeTTaChainer artifact descriptor transfers to its binary stream, preserve any primary read or metadata-admission exception if stream close also fails and attach the close diagnostic. Propagate stream-close failure normally when the bounded read otherwise succeeded.

**Rationale:** Stream release is necessary cleanup, but its failure does not explain why bytes could not be read or why descriptor metadata failed to close. The actionable admission diagnosis must remain primary across both raw-descriptor and stream-owned lifecycle phases.

**Consequences:** Callers retain the primary artifact rejection and can inspect the secondary close diagnostic. This grants no runtime, promotion, memory-write, upstream-change, or live-integration authority.
## 2026-07-19: Reject metadata-proven oversized PeTTaChainer artifacts before reading

**Decision:** After opening and classifying a PeTTaChainer JSON audit artifact through its descriptor, reject `st_size > max_bytes` before constructing a stream or consuming payload bytes.

**Rationale:** The descriptor metadata is already inside the no-follow, regular-file admission boundary. Reading even a bounded prefix of a file known to exceed the contract ceiling adds unnecessary I/O and weakens the meaning of a pre-admission resource gate.

**Consequences:** Oversized artifacts fail before payload read. Accepted-size artifacts still require stable descriptor identity/size/timestamps/link count, exact delivered byte count, unambiguous JSON, checksum closure, and typed provenance. This does not authorize runtime execution, promotion/write, or live integration.
## 2026-07-19: Audit-artifact admission closes permission metadata across reads

**Decision:** Require a PeTTaChainer checksummed JSON artifact's descriptor mode, owner, and group to remain stable across the bounded read, in addition to the existing device, inode, link-count, size, and timestamp fields.

**Rationale:** Artifact admission should reject a file whose security-relevant descriptor metadata changes while its bytes are being admitted, rather than recording only content-oriented drift.

**Consequences:** Concurrent chmod/chown-like drift fails closed. This does not establish an ownership policy, authorize promotion or writes, execute a runtime, or enable live integration.
## 2026-07-19: Reject broadly writable PeTTaChainer audit artifacts

**Decision:** Reject a checksummed PeTTaChainer JSON audit artifact when its opened regular-file descriptor is group- or world-writable.

**Rationale:** Stable metadata only proves permissions did not change during the read. It does not make an artifact safely immutable when principals beyond the owner retain direct write authority. The create-once publication path already requests owner-only mode `0600`.

**Consequences:** Group/world-writable derived captures and episode manifests fail before payload read. Owner-writable and read-only variants remain admissible subject to all existing gates. This grants no runtime, promotion/write, upstream-change, or live-integration authority.
# 2026-07-19: Artifact publication must not follow a supplied parent symlink

**Decision:** Open the create-once audit artifact's destination parent with `O_NOFOLLOW` where the platform provides it.

**Rationale:** Descriptor-relative exclusive creation and fsync remove replacement races after the parent is opened, but following a parent symlink can redirect publication before that anchor is established. These provenance artifacts should land only in the explicitly named directory.

**Consequences:** Symlinked destination parents fail before file creation on supported platforms; ordinary real directories retain the existing create-once and durability behavior. This authorizes no promotion, journal write, upstream adoption, or live integration.
# 2026-07-20: Audit artifact publication requires a narrowly writable parent

**Decision:** Reject PeTTaChainer create-once artifact publication when the already-open destination parent descriptor is group- or world-writable.

**Rationale:** Exclusive descriptor-relative creation and parent no-follow semantics do not preserve a create-once audit path when another principal can remove or replace directory entries afterward.

**Consequences:** Publication into broadly writable parents fails before artifact creation; owner-writable and read-only-for-group/other parents retain the existing exclusive creation, file sync, directory sync, and cleanup guarantees. This authorizes no runtime, promotion/write, upstream adoption, or live integration.
- 2026-07-20: Treat broad-write permission drift on the anchored audit-artifact parent during create-once publication as a failed publication. Check after file fsync and before directory fsync; retain the completed leaf because its publication state is uncertain and deleting it could permit a later overwrite. Implemented in `93e8fa0`.
## 2026-07-20: Bind create-once publication to stable parent metadata

**Decision:** Require the already-open artifact parent directory to retain its device, inode, mode, link count, owner, and group identity from pre-creation admission through completed file sync and before directory fsync.

**Rationale:** Rejecting only broadly writable final permissions left ownership/group and other directory metadata drift unclosed at the publication boundary.

**Consequences:** Metadata drift now fails closed while the completed file-synced artifact remains retained to preserve create-once semantics under uncertain publication state. This adds no promotion, memory-write, upstream, or live-integration authority.
## 2026-07-20: Bind artifact admission to stable trusted-parent metadata

**Decision:** Require the already-open artifact parent directory to retain its device, inode, mode, link count, owner, and group identity from initial parent admission through the completed bounded child-artifact read.

**Rationale:** Descriptor-relative child opening prevents path substitution after the parent is opened, but an ownership or permission transition during the read weakens the trusted-parent premise and should fail closed.

**Consequences:** Parent metadata drift rejects the artifact before JSON decoding and typed provenance admission. This grants no runtime, promotion/write, upstream, or live-integration authority.
- 2026-07-20: Treat initial parent-metadata inspection as part of descriptor-backed artifact admission cleanup. Once the parent descriptor is open, every later failure path must close it; the primary admission error remains authoritative and a secondary close failure is attached diagnostically. This does not expand artifact write, promotion, runtime, upstream, or live-integration authority.
## 2026-07-21: Preserve publication failures across text-stream cleanup

**Decision:** Explicitly close the descriptor-backed text stream used for create-once PeTTaChainer audit publication. If write, flush, or file sync has already failed, retain that primary exception and attach any stream-close failure as a diagnostic; if close alone fails after file sync, propagate it without deleting the completed artifact.

**Rationale:** Context-manager cleanup can replace the actionable publication error with a secondary close error. Conversely, deleting a file-synced artifact after close failure would weaken the existing uncertain-publication/create-once rule.

**Consequences:** Callers retain the original failure provenance and successfully synced artifacts cannot later be overwritten through a retry. This changes only local audit persistence; runtime inference, promotion/write authority, upstream adoption, and live OmegaClaw/GoalChainer integration remain closed.
# 2026-07-21: Close a newly created artifact descriptor when stream construction fails

**Decision:** When create-once publication successfully opens the artifact but `os.fdopen` cannot construct its text stream, explicitly close the raw descriptor before partial-artifact cleanup. Preserve the stream-construction failure as primary and attach a descriptor-close failure as a cleanup diagnostic.

**Rationale:** Ownership of an open descriptor transfers only after successful stream construction. Treating failed construction like an owned stream leaks the descriptor and can hide a secondary cleanup fault.

**Consequences:** Rejected artifacts are durably removed without leaking their raw descriptor, and callers retain both the actionable construction failure and any close diagnostic. This changes no runtime, promotion/write, upstream, or live-integration boundary. Implementation commit `be5c6d7`.
# 2026-07-21: Integrate ECAN as a derived attention projection

**Decision:** Treat `metta-attention` as an ephemeral, versioned control
projection over immutable petta-memory and OmegaSelf inputs. Keep STV/truth,
AV/salience, authorization, and canonical status as separate typed concerns.
Map upstream forgetting to projection/cache eviction rather than canonical
deletion. Let emotion regimes submit bounded, evidence-bearing stimulus or
parameter requests through the policy governor rather than directly setting AV.

**Rationale:** ECAN's Attentional Focus, diffusion, Hebbian communities, and
Cognitive Integration Period telemetry can improve retrieval, episodic
segmentation, consolidation, self-discrepancy repair, affective control, and
regenerative-goal experiments. Its mutable TypeSpace, global funds,
wall-clock/random paths, and destructive forgetting are incompatible with
petta-memory provenance and OmegaSelf governance if imported directly.

**Evidence:** `docs/metta_attention_integration_assessment.md`; upstream commit
`9196f38db749ddedeb591229dffddfa71664c38d`; GitHub Actions run
`29728552904` succeeded on 2026-07-20.
## 2026-07-21: Use one durable publication boundary for pi-PLN audit artifacts

**Decision:** Publish episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs through the same descriptor-anchored create-once writer used by PeTTaChainer capture artifacts.

**Rationale:** These records have the same immutable audit role, but their legacy pathname-based writers omitted parent-directory fsync and could unlink through a changed pathname after failure. Divergent persistence guarantees created an unnecessary provenance seam.

**Consequences:** All four writers now enforce narrow/stable parent metadata, exclusive descriptor-relative creation, owner-only file mode, file and directory durability, durable partial cleanup, and primary-error preservation. JSON schemas and readers are unchanged. This grants no inference-runtime, promotion/write, upstream, or live-integration authority. Implementation commit `fb7a71d`.
# 2026-07-21: Admit legacy pi-PLN audit JSON through one hardened reader

**Decision:** Route episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs through the same bounded, descriptor-anchored, no-follow JSON admission primitive used by PeTTaChainer audit artifacts.

**Rationale:** Checksums validate content after opening but do not make pathname traversal safe. A symlinked parent could redirect each legacy reader to a different filesystem location, and four direct parsing paths unnecessarily bypassed existing duplicate-key, file-type, permission, link-count, stability, and size checks.

**Consequences:** All four readers now fail closed before semantic reconstruction when their parent is a symlink or the shared artifact-admission invariants fail. This hardens local audit reads only and authorizes no runtime inference, promotion/write, upstream change, or live integration.
- 2026-07-21 — Keep the one-path/one-artifact assumption explicit at every legacy pi-PLN audit reader boundary: checksums alone do not prevent later mutation through a hard-link alias, so any artifact with `st_nlink != 1` remains inadmissible. Regression provenance: local commit `21ff1ce`. This is admission hardening only and grants no runtime, promotion, write, upstream, or live-integration authority.
# 2026-07-22: Require a non-writable parent at every legacy pi-PLN audit read boundary

**Decision:** Keep episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs inadmissible whenever their parent directory is group- or world-writable, even if the artifact itself is owner-only and checksummed.

**Rationale:** Artifact checksums and file permissions cannot prevent another writer with parent-directory authority from replacing the directory entry before admission. The shared reader already enforces this invariant; public regressions now close it for every migrated loader.

**Consequences:** This is local audit-admission hardening only. It grants no runtime inference, promotion/write, upstream change, remote action, paid compute, or live integration authority. Regression provenance: local commit `57b2e66`.
- 2026-07-22 — Phase-1 capture/reload will initially compose the existing compiled-input, validated-result, episode-manifest, and frozen-reference admission contracts rather than introduce a new archive container or provenance schema. Rationale: the first clean-room regression (`19a6528`) demonstrates deterministic identity and frozen-query equivalence while existing schema and compiled-episode closure already reject wrong-class and cross-run collisions. Revisit only if the remaining combined Phase-0/stale-artifact matrix exposes an identity relation that cannot be expressed by the current contracts. Promotion, sandbox-external writes, runtime execution, and live integration remain closed.
# 2026-07-22: Close clean-room manifests against admitted sibling artifacts

**Decision:** When a Phase-1 reload supplies compiled inputs and/or a validated result to the legacy episode-manifest reader, require the manifest's episode, stamp-map, and result identities to match those sibling artifacts before admission.

**Rationale:** Independent checksums prove each artifact is internally intact but do not prevent a valid manifest from one capture being paired with valid descriptors from another capture.

**Consequences:** Cross-run splicing now fails closed without adding an archive schema or changing promotion/runtime boundaries. Compatibility is retained for standalone audit reads that do not supply sibling artifacts. Implementation commit `0bb6d8b`.
# 2026-07-22: Bind clean-room manifest reload to compiled chart provenance

**Decision:** When archived episode manifests are reloaded with compiled inputs, require their chart and context IDs to match the identities carried by all compiled sentence sidecars, in addition to the existing episode and stamp-map checks.

**Rationale:** Equal episode and stamp assignments do not prove that a descriptor belongs to the same chart/context. The Phase-1 gate must reject cross-run descriptor substitution before treating the manifest as a coherent archived state.

**Consequences:** The bounded clean-room reload rejects altered chart provenance. This does not execute a runtime, authorize promotion or memory writes, adopt an upstream repair, or open live OmegaClaw/GoalChainer integration.
# 2026-07-23: Close archived manifests against bounded process captures

**Decision:** When a bounded `KernelProcessCapture` is supplied during episode-manifest reload, require exact equality of return code, stdout/stderr content commitments, and delivered-program commitment before admission.

**Rationale:** A manifest's internally valid digests do not by themselves prove that a separately supplied raw capture is the process event it describes.

**Consequences:** Clean-room replay can now bind archived inputs, typed result, manifest, and raw process capture without executing a kernel. This grants no runtime, promotion/write, upstream, remote, paid-compute, or live-integration authority.
# 2026-07-23: Raw kernel captures are typed provenance records

**Decision:** Reject a `KernelProcessCapture` at construction unless argv is a non-empty tuple of non-empty text arguments, return status is an integer but not a boolean, stdout/stderr are text, and any supplied delivered-program commitment is a valid SHA-256 digest.

**Rationale:** Clean-room manifest closure should consume a well-formed bounded process record. Delaying basic type and identity validation until hashing or result admission produces inconsistent failure behavior and permits malformed provenance to circulate.

**Consequences:** Process failures may still be represented with any integer return status, but malformed capture structure fails before manifest or result admission. This grants no runtime, promotion/write, upstream, remote, paid-compute, or live-integration authority. Implementation commit `09e774d`.
# 2026-07-23: Treat captured kernel results as unique output records

**Decision:** Admit a caller-supplied kernel result only when it occurs exactly once as a complete stdout line, not merely as an arbitrary substring.

**Rationale:** Substring presence cannot distinguish one emitted result from a larger diagnostic token or duplicate outputs and therefore does not establish an unambiguous process-to-result relation.

**Consequences:** Missing, embedded, and duplicated result candidates fail before typed semantic validation. Trace lines may still surround the one result record. This grants no runtime, promotion/write, upstream, remote, paid-compute, or live-integration authority. Implementation commit `f3882ae`.
## 2026-07-24 — Separate compiler-bound attribution from runtime trace claims

For the bounded PeTTaChainer one-rule episode, expose exact TotalMP rule/fact
attribution as a typed content-addressed record, but require
`runtime_trace_decoded=False`. The immutable contract and admitted proof close
which sole rule and fact support the result; opaque diagnostic stream digests
do not establish a general decoded trace. General trace decoding remains a
separate deferred gate.
# 2026-07-24: Rule attribution must close stamps and evidence bases one-to-one

**Decision:** Require equal cardinality between each compiler-bound rule/fact
stamp tuple and its retained evidence-basis tuple, in addition to independent
type, ordering, uniqueness, and digest checks.

**Rationale:** Attribution provenance is a mapping boundary. Independently valid
collections with unequal lengths cannot establish complete stamp-to-basis
closure, even when the enclosing attribution digest is correct.

**Consequences:** Malformed attribution fails before admission. This tightens
typed provenance only; it does not claim decoded runtime traces or authorize
promotion, writes, upstream adoption, or live integration.
# 2026-07-24: Derived-capture provenance collections are immutable tuples

**Decision:** Require the typed PeTTaChainer derived-result capture's fact/rule
stamp and evidence-basis collections to be tuples at construction, in addition
to their existing content, order, uniqueness, and cardinality invariants.

**Rationale:** A frozen dataclass does not make a nested list immutable.
Admitting correctly rehashed lists would weaken the capture's typed,
content-addressed provenance contract and permit post-construction mutation.

**Consequences:** Mutable collection representations fail before result
admission. This tightens local provenance only and authorizes no runtime,
promotion/write, upstream adoption, or live integration. Implemented in
`9f34631`.
# 2026-07-25: Persist compiler-bound attribution separately from runtime traces

**Decision:** Store the bounded one-rule PeTTaChainer attribution as its own
create-once checksummed artifact and admit it only when it exactly equals the
attribution reconstructed from the supplied typed derived-result capture.

**Rationale:** The attribution record identifies the sole compiler-authorized
TotalMP rule and fact but deliberately does not decode opaque runtime
diagnostics. Persisting that claim closes audit/reload provenance without
conflating compiler-bound attribution with a general execution-trace claim.

**Consequences:** A self-consistent attribution from another valid result fails
closed at reload. General trace decoding, reviewed promotion/write, upstream
repair adoption, and live OmegaClaw/GoalChainer integration remain separate
gates.
- 2026-07-25: Treat compiler-bound PeTTaChainer rule attribution as a distinct
  archived artifact class in Phase-1 clean-room verification. Its identity
  must remain stable across isolated reload cycles and its loader must reject
  result/manifest documents; this does not upgrade structural single-rule
  attribution into decoded runtime trace evidence.
- 2026-07-27: Output-path ownership checks at provider-free usability
  boundaries treat symlinks as pre-existing paths even when their targets do
  not exist. A dangling alias is operator-owned namespace state and must be
  rejected before `mkdir`, ingestion, inference, or canary work.
# 2026-07-27: Treat any usability output directory entry as occupied

**Decision:** The provider-free usability gate rejects an output path when
either its target exists or the path itself is a symlink, including a dangling
symlink.

**Rationale:** This is a create-new audit boundary. Following or replacing an
operator-selected alias could mutate an unexpected location, while a
target-existence check alone mistakes a dangling link for an unused name.

**Consequences:** Operators must choose a lexically unused output path.
Rejection occurs before ingestion or inference and does not create the symlink
target. This changes no runtime, promotion/write, upstream, dependency, or
live-integration boundary.
# 2026-07-27: Usability output paths may not traverse symlinked parents

**Decision:** Reject a create-new provider-free usability output path when any
lexical ancestor of its absolute path is a symlink.

**Rationale:** Rejecting only an occupied final path does not stop `mkdir -p`
and later artifact writes from being redirected through an operator-owned
directory alias, contradicting the gate's claimed local-output boundary.

**Consequences:** Operators must select a path whose existing ancestor chain is
symlink-free. This is a pre-runtime safety check and changes no inference,
promotion/write, upstream, dependency, or live-integration authority.
# 2026-07-27: Usability gates do not create output ancestors

**Decision:** Require the immediate parent of a provider-free usability output
directory to exist and create only the final directory entry.

**Rationale:** Recursive directory creation can mutate paths outside the
declared output directory, contradicting the gate's stated local-output
boundary even when every lexical ancestor is symlink-free.

**Consequences:** Operators must explicitly prepare the parent directory.
Missing or non-directory parents fail before fixture ingestion, inference, or
canary work and remain unmodified. This changes no promotion/write, upstream,
dependency, remote, or live-integration authority.
## 2026-07-27 — Persist non-live authority in usability evidence

Machine-readable provider-free usability evidence must explicitly state
read-only canary mode and false autonomous-write/promotion authority. Successful
retrieval and inference are not themselves authorization for either boundary.
- 2026-07-27: Treat every persistent file produced by the provider-free
  usability gate, including the empty journal lock and checksum sidecars, as a
  declared evidence-bundle member. Version the summary contract and regression
  test exact artifact-set equality so review tooling can fail closed on missing
  or unexpected output. This remains non-live and grants no promotion or write
  authority.
# 2026-07-27: Admit only an integrity-bound read-only ProtoMegaBot2 shadow consumer

**Decision:** ProtoMegaBot2 may consume the frozen provider-free usability
bundle only through a bounded adapter that validates the exact schema-v2
artifact inventory and hashes, emits candidate context to stdout, and never
opens ThreadKeeper or PeTTa-memory state for writing.

**Rationale:** This is the smallest operational integration that tests useful
downstream consumption while preserving the existing promotion, canonical
write, provider, Telegram, and live-runtime boundaries. Research Rules 2, 5,
and 7 are load-bearing: explicit fail-closed invariants, reproducible evidence,
and a replaceable public adapter seam.

**Consequences:** The provider-free shadow gate is admitted at ProtoMegaBot2
commit `fc30964`. A private live response remains separately gated on staging
credentials, supervisor isolation, rollback, and an explicit canary record.
- 2026-07-27: Treat provider-free usability summary schema v2 as closed, not
  extensible. Admission requires exactly the declared digest, inventory, and
  non-live claim members; producers must introduce a new schema version for
  additional fields. This keeps unknown authority or outcome claims outside
  the trusted read-only admission boundary.
# 2026-07-27: Integrity commitments do not substitute for semantic admission

**Decision:** Frozen usability admission must independently parse the
integrity-bound inference artifact and reconcile its outcome with the summary;
an artifact digest alone is not evidence that inference passed.

**Rationale:** A producer can recompute the digest of a failed result while
leaving a separate passed claim intact. Cross-artifact semantic equality
closes that internally inconsistent but cryptographically valid bundle.

**Consequences:** Admission remains read-only and non-live. Future claimed
outcomes in the summary should be checked against their authoritative
artifacts, not inferred from digest validity.
## 2026-07-28 — Semantic counters require exact JSON integers

Provider-free usability admission treats inference counters as typed security
claims. Both classification and semantic-marker counts must decode to exact
integers; JSON booleans are rejected even where host-language equality would
equate them with `0` or `1`. This is an admission-only hardening and does not
open runtime, promotion, write, or live-integration authority.
- 2026-07-28: Treat the frozen patham9/PLN inference result's exact member sets
  as part of provider-free usability admission, including nested
  `classification` and `semantic_markers`. Integrity plus semantic success is
  insufficient if undeclared authority-bearing fields remain admissible.
- 2026-07-28: A passed frozen usability inference is admitted only when its
  classification is attributed to the exact reviewed derivation-smoke
  classifier and carries clean success diagnostics. Rehashing an artifact
  cannot transfer pass authority to an unreviewed classifier identity.
- 2026-07-28: Treat the frozen usability derivation program's schema, mode, and
  exact member set as part of admission identity. Integrity-bound inference
  bytes and a named passing classifier do not establish which program contract
  was exercised. This remains read-only evidence admission and grants no
  runtime, promotion, write, or live-integration authority.
- 2026-07-28: Treat the frozen usability derivation's source term, derived
  projection, and numeric-stamp sidecar roles as one provenance contract.
  Integrity-bound executable text does not make independently relabelable
  audit metadata trustworthy. Admission requires source item/evidence
  agreement and the exact non-live synthetic bridge identity; this grants no
  runtime, promotion, write, or live-integration authority.
- 2026-07-28: Frozen usability admission treats the source item's term and STV
  as the authority for reconstructing the two runtime Sentences and expected
  TotalMp result. Merely integrity-binding mutually consistent executable text,
  declared sentences, and result is insufficient if they can detach from the
  provenance-bearing source item.
- 2026-07-28: Frozen provider-free usability admission treats the exact number
  of semantic pass markers as part of the program/result contract. Because the
  admitted bounded program reconstructs exactly one `Test`, it must produce
  exactly one successful marker; internally consistent larger counts do not
  prove that only the reviewed test ran.
- 2026-07-29: Treat a frozen usability source item's exact non-inferred status
  as admission-critical provenance. A patham9/PLN Sentence input may support a
  bounded derivation smoke without thereby becoming an admitted inferred
  belief; integrity-preserving relabeling cannot cross that promotion boundary.
- 2026-07-29: Treat the frozen usability source's `pi_pln_extension` as an
  admission-relevant non-live boundary, not opaque metadata. The consumer
  requires the exact producer declaration that context selection was not run,
  contextual EvidencePackets are empty, and EC projection remains deferred.
  Any later context-selection result needs a distinct reviewed schema/gate; it
  must not be smuggled through a rehashed frozen bundle.
## 2026-07-29: Frozen usability source provenance identities are non-empty

**Decision:** Admit a frozen provider-free usability inference only when its
source item carries non-empty string identities for belief, cluster, evidence,
promotion domain, promotion event, and promotion rule.

**Rationale:** Exact member sets and integrity hashes do not give empty
provenance fields meaning. Allowing a fully rehashed producer to erase the
reviewed promotion rule would sever an important audit boundary while leaving
the derivation structurally valid.

**Consequences:** Frozen bundles with erased provenance now fail closed. This
does not establish the external existence of those identities, authorize
promotion, invoke a runtime, write canonical memory, or enable live
OmegaClaw/GoalChainer integration.
## 2026-07-29 — Provenance identities are canonical MeTTa terms

Frozen provider-free usability admission treats every source provenance
identity as exactly one canonical MeTTa term, including compound evidence
identities. Non-empty strings and cross-field equality are insufficient when
an identity is interpolated into a MeTTa provenance atom: a rehashed identity
must not introduce an additional executable form. This is read-only admission
hardening and grants no runtime, promotion, write, or live authority.
- **2026-07-29 11:00 PDT / 18:00 UTC — Treat inference diagnostic surfaces as
  typed data, not extensible JSON:** Frozen usability admission accepts
  stdout/stderr only as strings and diagnostic lines only as a list of
  strings. Integrity alone does not establish the semantics of a JSON value;
  type-closing these producer-defined fields prevents authority-shaped
  structures from hitchhiking in an admitted result without changing the
  schema or granting diagnostic text authority.
## 2026-07-29 — Frozen runtime tails retain their producer bound

Provider-free usability admission treats the producer's 4,000-character
stdout/stderr tail truncation as part of the frozen result contract. Artifact
size and integrity bounds do not substitute for a field-level diagnostic
resource bound; a rehashed result cannot expand either tail beyond what the
reviewed producer emits. This remains read-only admission hardening and grants
no runtime, promotion, write, or live authority.
- 2026-07-29: Frozen provider-free usability admission treats semantic
  diagnostic lines as derived process evidence, not free-standing commentary.
  Every line must be observable in the producer-bounded stdout or stderr tail;
  otherwise admission fails closed even when all artifact hashes are valid.
  This keeps the existing schema and read-only/non-live authority boundary.
- 2026-07-29: Frozen provider-free usability admission requires the diagnostic
  line list to equal the producer-equivalent reconstruction from bounded
  stdout/stderr, including order, multiplicity, and stripping. Subset
  membership is insufficient because omission would make an audit surface
  independently editable despite integrity and marker-count checks. This
  remains read-only evidence admission with no runtime, write, promotion, or
  live authority.
- 2026-07-30: Treat the frozen Phase-0 reference output's successful semantic
  marker cardinality as admission-critical. Integrity, duplicate-run equality,
  and a `passed: true` claim do not prove that the reviewed single-test
  reference produced only one success when marker presence is checked as a
  substring. Admission requires exactly one declared semantic-result
  occurrence and exactly one `(Passed: #t)` occurrence. This is replay-anchor
  hardening only and grants no runtime, promotion, write, or live authority.
- 2026-07-30: Treat the frozen Phase-0 reference's declared semantic result as
  a typed kernel-result atom, not an arbitrary integrity-bound output
  substring. Admission requires the canonical patham9 result shape, bounded
  text, finite unit-interval truth values, and canonical non-empty stamps.
  This closes replay-anchor classification only and grants no runtime,
  promotion, write, or live-integration authority.
- 2026-07-30: Treat the complete non-empty output-line inventory and ordering
  of the frozen Phase-0 producer as admission-critical. Required-line
  cardinality alone permits an integrity-consistent anchor to carry additional
  contradictory or authority-shaped output. Admission therefore requires
  exactly the declared kernel-result line followed by the pass-marker line,
  while granting no runtime, promotion, write, or live authority.
- 2026-07-30: Treat the exact program bytes delivered during a frozen Phase-0
  replay as admission-critical. Matching runtime identity and deterministic
  output does not prove that the reviewed source was executed. Bounded
  captures therefore retain both the existing canonical program CID and a
  direct byte digest; Phase-0 admission compares the latter with the frozen
  source SHA-256. This grants no runtime, promotion, write, or live authority.
- 2026-07-30: Treat the normalized absolute executable launch path as part of
  fresh Phase-0 replay capture provenance. The digest-pinned subprocess helper
  resolves the executable before hashing and launch, so replay should not
  admit a weaker manually reconstructed relative-path capture merely because
  its asserted digest matches. This hardens the non-live replay gate and
  grants no runtime, promotion, write, or integration authority.
- 2026-07-30: Treat the frozen Phase-0 replay argv shape as admission-critical.
  Because the bounded replay delivers the checksum-verified complete program on
  stdin, the admitted launch consists only of the pinned normalized executable.
  Additional flags or filenames are unreviewed execution inputs even when all
  recorded content digests and output bytes match. This grants no runtime,
  promotion, write, or live-integration authority.
## 2026-07-30: Preserve subprocess cwd in raw captures and close the frozen replay shape

**Decision:** Record the normalized caller-supplied working-directory input in
`KernelProcessCapture`. The frozen Phase-0 stdin-only reference admits only a
capture with no explicit `cwd`.

**Rationale:** Executable, program, and argv identities do not reveal whether
the process was launched under an alternate caller-selected filesystem
context. Discarding that input made the raw capture weaker than the bounded
runner invocation it represented.

**Consequences:** Fresh reference replay fails closed on an explicit alternate
working directory. This records caller input, not the ambient inherited
directory's absolute identity, and it does not bind environment variables,
invoke the runtime, or authorize promotion, writes, or live integration.
# 2026-07-31: Typed kernel captures contain only valid UTF-8 text

**Decision:** Require all textual process-boundary fields in
`KernelProcessCapture` to encode as strict UTF-8 at construction.

**Rationale:** The bounded runner and replay gates define byte limits, hashes,
and output decoding in UTF-8. Allowing manually reconstructed captures to
contain lone surrogates violates that shared representation and shifts a typed
validation failure into incidental encoding exceptions downstream.

**Consequences:** Unencodable argv, streams, cwd, and environment entries fail
closed before replay. This grants no runtime, promotion/write, or live
integration authority.
# 2026-07-31: Require UTF-8 at both kernel launch and capture boundaries

**Decision:** Treat program and process-context text as UTF-8 data before
launch, and reject unencodable values with the same typed fail-closed contract
used for reconstructed captures.

**Rationale:** A reconstructed capture must not admit text the actual runner
cannot deliver, while callers of the runner should receive bounded validation
errors before any subprocess side effect rather than platform encoding errors.

**Consequences:** Surrogate-bearing program, argv, cwd, and explicit environment
inputs cannot launch. This changes no valid UTF-8 execution and grants no
promotion, write, or live-integration authority.

# 2026-07-31: Normalize cwd resolution failures at the launch boundary

**Decision:** Convert both OS resolution errors and symlink-cycle errors into a
typed `ValueError` before launching the bounded kernel subprocess.

**Rationale:** A caller-controlled invalid cwd is input-validation failure.
Python exposes a symlink cycle as `RuntimeError`, but that implementation detail
must not escape the runner's fail-closed validation contract.

**Consequences:** Cyclic cwd inputs cannot launch and report the same bounded
resolution failure class as missing or otherwise unresolvable paths. Valid cwd
behavior and all promotion, write, and live-integration boundaries are unchanged.
# 2026-07-31: Treat argv as a collection, not scalar text

**Decision:** Reject text/bytes and non-iterable `argv` values before bounded
kernel launch, using the runner's typed `ValueError` contract.

**Rationale:** Python strings are iterable, so unconditional tuple conversion
silently changes a bare executable pathname into one-character arguments.
That is an ambiguous launch shape rather than a valid argument vector.

**Consequences:** Callers must supply an actual iterable of argument strings.
Result admission, promotion/write, dependencies, and live integration remain
unchanged.
# 2026-07-31: Apply the argv byte ceiling during iterable consumption

**Decision:** Validate and byte-account kernel argv entries incrementally
instead of materializing the caller's complete iterable before enforcing its
budget.

**Rationale:** An iterable is not necessarily finite or cheaply materialized.
The launch boundary's byte ceiling must also bound Python-side admission work,
not only the final OS argument vector.

**Consequences:** Oversized and unbounded argv sources fail closed once their
UTF-8 payload plus terminating-NUL framing crosses `max_argv_bytes`. Valid
bounded vectors behave unchanged; no runtime result, promotion/write, or live
integration authority is added.

# 2026-07-31: Normalize argv enumeration failures before launch

**Decision:** Convert exceptions raised by a caller-supplied argv iterator
during enumeration into the bounded runner's typed `ValueError`, retaining the
original exception as its cause.

**Rationale:** Iterator execution is caller-controlled input admission. Its
implementation exceptions must not escape the same typed boundary already
used for non-iterability, malformed entries, and byte-budget violations.

**Consequences:** Failing argv iterators cannot launch a process and remain
diagnosable through exception chaining. Valid bounded vectors and all result,
promotion/write, and live-integration boundaries are unchanged.
# 2026-08-01: Treat environment item shape as part of runner admission

**Decision:** Convert malformed entries yielded by a caller-supplied process
environment iterator into the bounded runner's chained `ValueError` contract
before subprocess launch.

**Rationale:** Merely requiring `Mapping` does not guarantee a custom
`items()` implementation yields key-value pairs. The complete caller-controlled
iteration surface needs one fail-closed typed boundary.

**Consequences:** Non-pair environment entries cannot leak raw unpacking
exceptions or reach `Popen`. Runtime output/result admission, promotion/write,
and live integration boundaries are unchanged.
# 2026-08-01: Environment items have an exact structural boundary

**Decision:** Require every item from an explicit environment mapping to be an
exact two-element tuple before interpreting its key and value.

**Rationale:** Generic sequence unpacking admits scalar strings of length two,
allowing a hostile mapping implementation to alter the subprocess environment
despite not yielding a key/value item.

**Consequences:** Scalar and other non-tuple items fail through the typed
pre-launch boundary. Ordinary mapping `items()` output is unchanged; runtime
result admission, promotion/write, and live integration remain closed.
# 2026-08-01: Normalize subprocess process-construction failures

**Decision:** Treat both `OSError` and `subprocess.SubprocessError` raised by
`Popen` as typed bounded-runner launch failures, retaining the original
exception as cause.

**Rationale:** Callers should receive one stable pre-execution failure contract
for the exception classes exposed by process construction rather than having a
subprocess-specific exception escape the boundary.

**Consequences:** Process-construction failure cannot be mistaken for a
capture or validated result. Successful execution, result admission,
promotion/write, and live integration semantics are unchanged.
# 2026-08-01: Treat child-stream read errors as bounded runner failures

**Decision:** Translate OS-level stdout/stderr capture failures into the
bounded runner's public `ValueError` contract, preserving the original
exception as cause and terminating the isolated process group.

**Rationale:** A failure in a reader thread must not become an untyped missing
capture or leave the subprocess running. Preflight, launch, program delivery,
and output capture should share one fail-closed caller contract.

**Consequences:** Failed stream capture cannot produce a
`KernelProcessCapture`. Result admission, promotion/write, and live integration
boundaries remain unchanged.
- 2026-08-02: Treat every ordinary exception raised inside a bounded kernel
  stdout/stderr reader as a capture failure at the thread boundary. Preserve
  the exception as the cause of the public typed `ValueError`; do not permit a
  worker-thread traceback or missing capture entry to become the caller-visible
  failure. `BaseException` remains outside this normalization boundary.
- 2026-08-02: Treat every ordinary exception raised while delivering the
  bounded kernel program over stdin as incomplete delivery. Preserve the first
  failure as the cause of the public typed `ValueError`; never admit a capture
  after its daemon writer failed. `BaseException` remains outside this
  normalization boundary. Result admission, promotion/write, and live
  integration semantics are unchanged.
- 2026-08-02: Treat every ordinary direct-process wait exception as a bounded
  runner failure. Preserve the original exception as the cause of a typed
  `ValueError`, and retain cleanup of the isolated process group and captured
  streams. `BaseException` remains outside normalization; result admission,
  promotion/write, and live integration semantics are unchanged.
# 2026-08-03: Treat timeout reaping as part of the typed runner boundary

**Decision:** Translate an unexpected failure from the post-timeout reap into
`ValueError("kernel subprocess timeout cleanup failed")`, preserving the
cleanup exception as its cause.

**Rationale:** Killing a timed-out process group is not the end of cleanup; the
direct child must also be reaped. That mandatory operation belongs inside the
same fail-closed typed contract as launch, capture, stdin delivery, and the
ordinary wait.

**Consequences:** Callers no longer receive an arbitrary exception from the
timeout cleanup path. Stream finalization remains active, and result admission,
promotion/write, external runtimes, and live integration are unchanged.

# 2026-08-03: Treat process-group termination as typed runner cleanup

**Decision:** Record ordinary `killpg()` failures and reject capture through a
typed process-group cleanup `ValueError`, preserving the first failure as its
cause. `ProcessLookupError` continues to mean the group is already absent.

**Rationale:** Process-group termination is used from worker and caller paths.
Its failures must not escape only inside a daemon thread or permit a successful
capture after descendant cleanup was not established.

**Consequences:** Stream finalization still runs before the cleanup failure is
reported. Result admission, promotion/write, external runtimes, and live
integration remain unchanged.
# 2026-08-03: Treat worker joins as typed runner cleanup

**Decision:** Record ordinary writer/reader `join()` failures and reject capture
through `ValueError("kernel subprocess worker cleanup failed")`, preserving the
first failure as its cause while attempting all joins and stream closes.

**Rationale:** Worker synchronization is part of bounded capture finalization.
One failed join must not leak an arbitrary exception or suppress remaining
cleanup attempts.

**Consequences:** Failed worker cleanup cannot produce a capture. Result
admission, promotion/write, external runtimes, and live integration remain
unchanged.
# 2026-08-03: Treat capture-worker startup as part of the bounded launch boundary

**Decision:** Normalize an unexpected capture-worker `start()` failure through
the runner's typed failure contract and complete bounded child/worker/stream
cleanup before returning it.

**Rationale:** Successful `Popen` is not a completed runner launch: without all
three I/O workers, the child cannot produce a trustworthy bounded capture and
must not survive an internal thread-start failure.

**Consequences:** Only successfully started workers are joined; the process is
killed and reaped and both captured streams are closed. Result admission,
promotion/write, and live integration boundaries are unchanged.
# 2026-08-03: Treat post-launch worker construction as a typed cleanup boundary

**Decision:** If a capture thread cannot be constructed after subprocess
launch, kill/reap the child, attempt closure of every subprocess pipe, and
surface construction or cleanup failure through a chained `ValueError`.

**Rationale:** Worker construction is untrusted runtime setup just like worker
startup. It must not leak an orphan process, descriptors, or a raw exception.

**Consequences:** Kernel execution, inference admission, promotion/write, and
live integration authority are unchanged.
# 2026-08-03: Finalize every post-launch subprocess pipe

**Decision:** Close stdin together with stdout and stderr in the bounded
runner's post-launch finalizer, including when capture-worker startup fails
before the stdin writer starts.

**Rationale:** Killing and reaping the child does not release the parent's pipe
descriptor. Every pipe acquired at successful process construction belongs to
the same fail-closed cleanup boundary.

**Consequences:** Startup failure cannot leak the unstarted writer's stdin
pipe. Result admission, promotion/write, external runtimes, and live
integration remain unchanged.
# 2026-08-03: Preserve worker-construction termination failures

**Decision:** When capture-worker construction fails after launch, treat a
process-group termination failure as the primary typed construction-cleanup
cause, while still attempting direct-child reap and closure of every pipe.

**Rationale:** The triggering thread-constructor exception explains why setup
stopped, but a failed kill identifies the higher-risk cleanup condition: the
isolated child or descendants may remain alive. Discarding it makes the
fail-closed boundary misleading.

**Consequences:** Construction cleanup remains typed and diagnostic, and all
remaining cleanup attempts still run. Runtime result admission,
promotion/write, external runtimes, and live integration remain unchanged.
# 2026-08-03: Process-group cleanup outranks an ordinary wait failure

**Decision:** Defer the typed ordinary-wait failure until after subprocess
finalization, and report a recorded process-group termination failure first.

**Rationale:** A wait exception describes observation/reaping failure, while a
failed kill means the isolated process group may remain alive. The latter is
the higher-risk cleanup condition and must not be masked by control flow.

**Consequences:** Successful-kill wait failures retain the existing typed
`kernel subprocess wait failed` contract. Simultaneous kill failure instead
uses the existing process-group cleanup contract. Result admission,
promotion/write, external runtimes, and live integration remain unchanged.
# 2026-08-03: Process-group cleanup outranks a subprocess timeout

**Decision:** Defer timeout and timeout-cleanup classification until common
post-launch finalization, and report any recorded process-group termination
failure first.

**Rationale:** The timeout explains why termination was requested, but a failed
kill means the isolated child or descendants may still be alive. That
higher-risk cleanup condition must remain visible rather than being masked by
an immediate timeout raise.

**Consequences:** Ordinary timeouts and timeout-reap failures keep their
existing typed messages and original causes when termination succeeds. Worker
joins and every pipe closure still run. Result admission, promotion/write,
external runtimes, and live integration remain unchanged.
# 2026-08-03: Normalize every ordinary process-construction failure

**Decision:** Treat any ordinary `Exception` raised by `subprocess.Popen` as a
typed kernel launch failure while preserving the original exception as cause.

**Rationale:** The bounded runner is a fail-closed API boundary. Constructor
failures from wrappers, instrumentation, or future runtime internals should
not leak an unrelated exception type to episode callers.

**Consequences:** `KeyboardInterrupt`, `SystemExit`, and other
`BaseException` controls still propagate. No child exists yet on this path, so
cleanup behavior, result admission, promotion/write, and live integration are
unchanged.
# 2026-08-04: Preserve requested-pipe termination failures without truncating cleanup

**Decision:** Treat process-group termination failure during requested-pipe
validation as the first typed cleanup cause, while still attempting direct
process reap and closure of every supplied pipe.

**Rationale:** A malformed `Popen` result is already outside the runner's
admitted launch contract. Failure to terminate it is the most urgent cleanup
diagnostic, but must not prevent the remaining bounded cleanup attempts.

**Consequences:** Regression coverage now fixes the ordering and completeness
of this cleanup path. Runtime result admission, promotion/write, dependencies,
and live integration remain unchanged and closed.
# 2026-08-04: Preserve requested-pipe reap failures without truncating cleanup

**Decision:** Treat direct-child `wait()` failure during requested-pipe
validation as a typed pipe-validation cleanup failure, while still attempting
closure of every supplied subprocess stream.

**Rationale:** A malformed construction result must not leak an arbitrary reap
exception or cause later descriptor cleanup to be skipped.

**Consequences:** Regression coverage now fixes the typed cause and cleanup
completeness. Runtime result admission, promotion/write, dependencies, and live
integration remain unchanged and closed.
# 2026-08-04: Close requested-pipe cleanup follow-ups and return to Phase-1

**Decision:** Treat the kill-, reap-, and supplied-stream-failure regressions
for malformed requested-pipe cleanup as the completed bounded follow-up to the
pipe-validation change. Do not add more speculative subprocess hardening unless
a concrete Phase-1 gate failure exposes it; return to semantic capture/reload.

**Rationale:** The focused matrix now preserves each cleanup failure class as a
typed cause and proves later cleanup attempts still occur. Joint focused and
full verification passed (2 and 662 tests), so further edge-case expansion
would repeat the diminishing-return branch frozen on 2026-07-22.

**Consequences:** The next meaningful implementation slice is again the bounded,
non-live Phase-1 semantic capture/reload gate. Runtime invocation,
promotion/write, upstream adoption, paid compute, remote actions, and live
OmegaClaw/GoalChainer integration remain closed.
# 2026-08-04: Persist raw kernel captures as a distinct typed artifact

**Decision:** Store the complete bounded `KernelProcessCapture` in a create-once,
checksummed v1 document and reconstruct its typed invariants before using it for
clean-room manifest admission.

**Rationale:** Compiled inputs, semantic results, and manifests were persistent,
but the OS-level process evidence connecting them was manually reconstructed on
reload. A distinct raw-capture artifact preserves argv, streams, runtime/program
identities, cwd, and environment without conflating raw diagnostics with a
validated PLN result or promotion authority.

**Consequences:** Clean-room replay can now admit persisted process provenance
end to end. The artifact does not execute a runtime, validate semantic output by
itself, authorize promotion/write, or open live OmegaClaw/GoalChainer integration.
- 2026-08-04 19:10 PDT / 2026-08-05 02:10 UTC: Treat every immutable dependency
  supplied to episode-manifest construction as part of the public typed audit
  boundary. Reject malformed dependencies before field access so orchestration
  errors remain stable and fail closed; this grants no runtime or promotion
  authority. Implemented in local commit `a125a1b`.
- 2026-08-05 09:03 PDT / 16:03 UTC: PeTTaChainer derived-result artifacts must
  establish their typed serialization contract before any destination-parent
  creation. Malformed caller input is not allowed to mutate the filesystem.
- 2026-08-05 11:00 PDT / 18:00 UTC: PeTTaChainer rule-attribution artifacts,
  like derived-result and episode-manifest artifacts, must establish their
  typed checksummed serialization boundary before destination-parent creation.
  Malformed caller input must not mutate the filesystem. Implemented in local
  commit `c3de0a0`; no runtime, promotion, write, or live authority is added.
- 2026-08-05 13:04 PDT / 20:04 UTC: Stock pi-PLN episode-manifest artifacts,
  like the PeTTaChainer audit artifacts, must establish their typed checksummed
  serialization boundary before destination-parent creation. Malformed caller
  input must not mutate the filesystem; this grants no runtime, promotion,
  write, or live authority. Implemented in local commit `f7fba44`.
- 2026-08-05 19:00 PDT / 2026-08-06 02:00 UTC: Immutable compiled episode
  inputs must establish their typed checksummed serialization boundary before
  destination-parent creation. Malformed caller input must not mutate the
  filesystem. Implemented in local commit `e012c48`; this grants no runtime,
  promotion, write, or live authority.
- 2026-08-06 03:00 PDT / 10:00 UTC: Required immutable compiler provenance for
  PeTTaChainer derived-result reload is a caller admission boundary and must be
  validated before artifact I/O. This preserves deterministic typed failure
  precedence without granting runtime, result-promotion, write, or live
  integration authority. Implemented in local commit `6cd83e5`.

# 2026-08-06: Require an exact evidence-snapshot persistence envelope

**Decision:** Admit evidence-snapshot documents only when their top level is
exactly `schema`, `payload`, and `document_digest`.

**Rationale:** The payload digest cannot authenticate or reject undeclared
top-level siblings. Exact schema closure prevents authority-shaped metadata
from riding beside an otherwise valid immutable snapshot.

**Consequences:** Older or adversarial snapshot documents with extra envelope
members fail closed; the canonical writer output and payload schema are
unchanged.
# 2026-08-06: Type-check immutable episode compiler dependencies first

**Decision:** Require `PiChart` and `EvidenceSnapshot` instances at the start
of `compile_episode_inputs()` before reading provenance fields.

**Rationale:** Malformed orchestration input should fail through the compiler's
stable validation boundary, independently of later snapshot or packet checks.

**Consequences:** Direct callers no longer receive incidental attribute errors;
compilation semantics and all runtime, promotion, write, and live-integration
gates are unchanged. Implementation commit: `225aade`.
- 2026-08-06 13:01 PDT: Treat every packet and evidence-basis member accepted
  by deterministic episode compilation as an explicit immutable dependency.
  Reject malformed members at the public compiler boundary before provenance
  or identifier access, preserving a stable typed failure contract.
## 2026-08-07 — PeTTaChainer contract stamp sidecars are globally bijective

Decision: within one immutable `PeTTaChainerEpisodeContract`, every repeated
stamp must identify the same evidence basis and every repeated evidence basis
must identify the same stamp. Statement-local cardinality is insufficient for
an episode-level provenance claim.

Reason: PeTTaChainer's public checked-add atom has no stamp field, so the typed
sidecar is the audit boundary. Allowing contradictory reconstructed sidecars
would make downstream capture and attribution provenance ambiguous even when
each statement passed independently.
# 2026-08-07: PeTTaChainer contract statement containers are immutable

**Decision:** Require the checked-add statement collection in every immutable
PeTTaChainer episode contract to be a non-empty tuple.

**Rationale:** A frozen dataclass that retains a caller-owned list is still
mutable after validation, which can invalidate its proof-id and stamp/basis
audit checks without reconstructing the contract.

**Consequences:** Valid compiler-produced contracts are unchanged; manually
constructed list-backed contracts fail closed. This authorizes no runtime,
promotion/write, live integration, dependency change, paid compute, or remote
action.
# 2026-08-07: Bound immutable PeTTaChainer contracts at reconstruction

**Decision:** Apply the compiler adapter's aggregate one-million-character
checked-add/query atom ceiling inside `PeTTaChainerEpisodeContract` itself.

**Rationale:** Builder-only enforcement is not an immutable contract invariant;
a direct or deserialized caller could otherwise construct oversized runtime
input while retaining all other typed provenance checks.

**Consequences:** Compiler-produced contracts are unchanged, while oversized
reconstructed contracts fail before query canonicalization. This grants no
runtime, promotion/write, live-integration, dependency, paid-compute, or remote
authority. Implemented in local commit `dde58b4`.
# 2026-08-07: Bound duplicated PeTTaChainer query terms before parsing

**Decision:** Type-check and cap a reconstructed contract's typed `query_term`
before canonical S-expression parsing, independently of its emitted
`query_atom` ceiling.

**Rationale:** Direct reconstruction can make those duplicate fields disagree.
A small forged atom must not allow an oversized term to consume parser work
before the later equality check rejects it.

**Consequences:** Compiler-produced contracts are unchanged; malformed direct
reconstructions fail at the immutable resource boundary. This grants no
runtime, promotion/write, live-integration, dependency, paid-compute, or remote
authority. Implemented in local commit `99fe409`.
# 2026-08-07: Enforce aggregate PeTTaChainer size before semantic scans

**Decision:** Accumulate and enforce a reconstructed episode contract's
checked-add statement character ceiling before proof-id uniqueness allocation
and provenance scanning.

**Rationale:** The ceiling is a resource-admission boundary. An oversized tuple
of repeated valid statements must fail there before later semantic checks do
work proportional to the entire adversarial collection.

**Consequences:** Valid compiler-produced contracts are unchanged; oversized
reconstructions now fail earlier and deterministically. This grants no runtime,
promotion/write, live-integration, dependency, paid-compute, or remote
authority. Implemented in local commit `a8dc813`.
# 2026-08-07: Bound reconstructed derived-result text before parsing

**Decision:** Type-check and independently cap PeTTaChainer derived-result
query, atom, and proof text before canonical query parsing.

**Rationale:** The public frozen capture is reconstructible, so persistence
and replay callers must not be able to spend unbounded parser work before the
typed atom/result consistency checks run.

**Consequences:** Valid captures are unchanged. Malformed reconstructed text
fails closed before parsing. This authorizes no runtime, promotion/write, live
integration, dependency change, paid compute, or remote action.
# 2026-08-08: Bound reconstructed stock pi-PLN result queries before parsing

**Decision:** Type-check and cap the duplicate query term retained by a
directly reconstructed `ValidatedKernelResult` before canonical parsing.

**Rationale:** Validator-created results already carry canonical bounded query
text, but the public frozen dataclass is reconstructible. Its immutable
boundary must enforce the same parser resource ceiling independently.

**Consequences:** Valid admitted results are unchanged. Malformed duplicate
query text fails closed before parsing. This authorizes no runtime,
promotion/write, live integration, dependency change, paid compute, or remote
action.
# 2026-08-08: Bound reconstructed compiled sentences before parsing

**Decision:** Require immutable projection and kernel-sentence metadata on
every `CompiledSentence`, and cap its emitted atom and canonical term before
canonical S-expression parsing.

**Rationale:** Compiler-produced sentences are safe, but the public frozen
dataclass is reconstructible. Malformed dependencies must not leak attribute
errors, and oversized duplicate term text must not consume unbounded parser
work.

**Consequences:** Valid compiler output is unchanged. Malformed reconstructed
sentences fail closed without granting runtime, promotion/write, live
integration, dependency, paid-compute, or remote authority.
# 2026-08-08: Require immutable evidence-basis provenance collections

**Decision:** Require tuple-backed `member_token_ids` and `causal_group_ids`
when directly constructing a frozen `EvidenceBasis`.

**Rationale:** Evidence bases feed deterministic stamp allocation and exact
evidence algebra. Accepting caller-owned lists allowed provenance to change
after validation despite the frozen record boundary.

**Consequences:** Valid builder output is unchanged. Malformed reconstructed
bases fail closed without granting runtime, promotion/write, live integration,
dependency, paid-compute, or remote authority.
## 2026-08-08 17:00 PDT / 2026-08-09 00:00 UTC — require immutable snapshot collections

- Decision: require tuple-backed `EvidenceSnapshot.packet_ids` and
  `packet_content_digests`, and require every digest pair to be a tuple.
- Rationale: `frozen=True` blocks field reassignment but does not freeze
  caller-owned lists; the snapshot is a content-addressed provenance boundary,
  so nested mutable aliases must be rejected at reconstruction.
- Scope: validation and regressions only. Runtime, promotion/write, live
  integration, dependency, paid-compute, and remote gates remain unchanged.
# 2026-08-08: Require immutable typed pi-chart inputs

**Decision:** Require direct `PiChart` construction to supply a typed
`ChartPolicy` and tuple-backed `selected_packet_ids`.

**Rationale:** Charts are fingerprinted compiler inputs. A frozen record must
not retain caller-owned mutable selection state, and malformed reconstructed
policies should fail at the chart boundary rather than during downstream field
access.

**Consequences:** Builder-produced charts are unchanged. Malformed direct
reconstructions fail closed without authorizing runtime, promotion/write, live
integration, dependency changes, paid compute, or remote actions. Implemented
in local commit `a6c7fd1`.
# 2026-08-09: Snapshot builders admit only typed evidence packets

Decision: require every item supplied to `build_evidence_snapshot(...)` to be
an immutable `EvidencePacket` before reading packet identity or state.

Rationale: the snapshot is a content-addressed evidence boundary. Malformed
direct callers should fail through its stable `ValueError` contract rather
than leaking implementation-level attribute errors before validation.

Boundary: valid snapshot construction is unchanged. This does not invoke a
runtime, authorize promotion or writes, enable live integration, change
dependencies, use paid compute, or perform a remote action.
- 2026-08-09: Treat every present optional `EvidenceToken` provenance id as a
  typed non-empty string and reject non-integer schema versions at immutable
  construction. This keeps malformed reconstructed evidence outside later
  snapshot/pi-PLN paths and preserves the public `ValueError` boundary.
  Implemented and verified in local repo commit `d3cc023`; non-live gates are
  unchanged.
# 2026-08-09: Evidence basis provenance ids are non-empty strings

Decision: validate every `EvidenceBasis.member_token_ids` and
`causal_group_ids` member as a non-empty string before uniqueness and ordering
checks.

Rationale: these values identify the atomic provenance and causal grouping of
an evidence unit. Directly reconstructed typed records must not admit empty ids
or leak `TypeError` from mixed-type sorting; malformed callers should receive
the public `ValueError` contract.

Boundary: valid basis construction and evidence algebra are unchanged. This
does not invoke a runtime, authorize promotion or writes, enable live
integration, change dependencies, use paid compute, or perform a remote
action.
# 2026-08-09: Evidence-basis builders require immutable typed dependencies

Decision: validate the packet and complete materialized token collection as
`EvidencePacket`/`EvidenceToken` records before reading their provenance.

Rationale: direct reconstruction with property-bearing foreign objects could
otherwise leak arbitrary field-access failures across a PLN-ready public
boundary. Early type admission preserves the stable `ValueError` contract.

Boundary: valid builder output and evidence algebra are unchanged. This is
local contract hardening only; no runtime, promotion/write, live integration,
dependency, paid-compute, or remote action is authorized.
# 2026-08-09: Exact evidence-capsule merges require typed dependencies

Decision: validate both merge operands as immutable `EvidenceCapsule` records
and every supplied basis item as an immutable `EvidenceBasis` before reading
their fields.

Rationale: exact evidence algebra is a PLN-ready provenance boundary.
Malformed reconstructed callers must fail through its stable `ValueError`
contract rather than leaking incidental attribute-access failures.

Boundary: valid deduplication and reviewed-overlap behavior is unchanged. This
does not invoke a runtime, authorize promotion or writes, enable live
integration, change dependencies, use paid compute, or perform a remote
action. Implemented in local commit `9f61044`.
# 2026-08-09: Validate evidence-snapshot packet ids before ordering

**Decision:** Validate every `EvidenceSnapshot.packet_ids` member as a
non-empty string before uniqueness sorting.

**Rationale:** Snapshots are content-addressed PLN-ready provenance boundaries.
Malformed reconstructed mixed-type identifiers must fail through their stable
`ValueError` contract instead of leaking an incidental sorting `TypeError`.

**Consequences:** Valid builder output is unchanged. This authorizes no runtime,
promotion/write, live integration, dependency change, paid compute, or remote
action.
# 2026-08-09: Evidence snapshot digest sidecars require exact immutable pairs

Decision: validate each `packet_content_digests` entry as a tuple of exactly
two fields before extracting its packet id and content digest.

Rationale: tuple immutability alone does not establish record shape. Wrong
arity at this immutable snapshot boundary must produce the model's stable
`ValueError` contract rather than an incidental destructuring exception.

Boundary: valid snapshot identities and serialization are unchanged. This
authorizes no runtime invocation, promotion/write, live integration,
dependency change, paid compute, or remote action.
