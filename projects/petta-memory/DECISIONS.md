
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
