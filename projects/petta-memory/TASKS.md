
- [x] Add TraceAttribution: persisted proof-trace attribution with stable
  reload identity. `TraceAttribution` is a frozen dataclass that binds a
  compiled result to its originating rule and proof trace, following the same
  immutable, content-addressed pattern as `PeTTaChainerRuleAttribution` but
  carrying an opaque proof_trace string. Its identity (`trace_digest` = SHA-256
  over all non-digest fields) is stable across serialize → deserialize.
  Create-once checksummed JSON persistence and reload verify schema, document
  checksum, trace_digest, and result-binding fields against the supplied
  derived capture. Focused 20-test and full 718-test verification passed with
  `py_compile` and repository-local `git diff --check`; local commit
  `df0ea60` (2026-08-20 13:30 PDT / 20:30 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Close malformed kernel sentence provenance member admission. Stamp and
  evidence-basis members are now typed before sorting, preventing reconstructed
  mixed-type tuples from leaking `TypeError`. Focused and full 697-test
  verification passed with repository-local `git diff --check`; local commit
  `7655494` (2026-08-09 19:00 PDT / 2026-08-10 02:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close malformed evidence-capsule merge metadata admission. Optional
  `bases` metadata now explicitly requires an iterable before traversal, so a
  malformed scalar fails through the public `ValueError` contract instead of
  leaking `TypeError`. Focused and full 696-test verification passed with
  repository-local `git diff --check`; local commit `60e1d07` (2026-08-09 17:00 PDT / 2026-08-10
  00:00 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close malformed evidence-packet schema version admission.
  `EvidencePacket` now explicitly requires an integer schema version before
  comparing it, so reconstructed packets with strings or `None` fail through
  the typed `ValueError` contract instead of leaking `TypeError`. Focused and
  full 695-test verification passed with repository-local `git diff --check`;
  local commit `1c6232d` (2026-08-09 13:00 PDT / 20:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close mutable pi-PLN context ancestry. `PiContext` now requires an
  immutable tuple for `parent_context_ids`, so reconstruction cannot retain a
  caller-owned list. Focused and full 687-test verification passed with
  repository-local `git diff --check`; local commit `7df8be5` (2026-08-08
  21:00 PDT / 2026-08-09 04:00 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close mutable and malformed evidence-capsule contributions.
  `EvidenceCapsule` now requires an immutable tuple containing only typed
  `EvidenceContribution` records, so reconstruction cannot retain a
  caller-owned list or leak `AttributeError` on an invalid member. Focused and
  full 686-test verification passed with repository-local `git diff --check`;
  local commit `c07ac52` (2026-08-08 19:02 PDT / 2026-08-09 02:02 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.

- [x] Close mutable evidence-packet provenance collections. `EvidencePacket`
  now requires immutable tuples for `token_ids` and `parent_packet_ids`, so a
  reconstructed frozen packet cannot retain caller-owned lists. Focused and
  full 683-test verification passed with repository-local `git diff --check`;
  local commit `fd6a78d` (2026-08-08 13:00 PDT / 20:00 UTC). Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close mutable stock pi-PLN episode-manifest collections.
  `EpisodeManifest` now requires immutable tuples for `parent_episode_ids` and
  `projection_policy_ids`, so a reconstructed frozen manifest cannot retain
  caller-owned lists. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `bbea4b5` (2026-08-08
  11:01 PDT / 18:01 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.

- [x] Close mutable validated-result provenance collections.
  `ValidatedKernelResult` now requires immutable tuples for `stamp_ints` and
  `evidence_basis_ids`, so a reconstructed admitted result cannot retain
  caller-owned lists. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `2e3bdcd` (2026-08-08
  09:01 PDT / 16:01 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.

- [x] Close mutable kernel sentence provenance sidecars. `KernelSentenceMeta`
  now requires immutable tuples for `stamp_ints` and `evidence_basis_ids`, so
  reconstructed frozen metadata cannot retain caller-owned lists. Focused and
  full 682-test verification passed with repository-local `git diff --check`;
  local commit `f989970` (2026-08-08 07:03 PDT / 14:03 UTC). Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close mutable collections at the compiled-episode boundary.
  `CompiledEpisodeInputs` now requires immutable tuples for both `stamp_map`
  and `sentences`; reconstruction with caller-owned lists fails before member
  validation. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `9e80395` (2026-08-08
  05:00 PDT / 12:00 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.

- [x] Close reconstructed compiled-sentence parser admission. `CompiledSentence`
  now validates immutable projection/metadata dependencies and caps its atom
  and duplicate canonical term before parsing. A parser-sentinel regression,
  the focused compiler test, all 682 tests, and repository-local `git
  diff --check` passed; local commit `546de55` (2026-08-08 03:02 PDT / 10:02
  UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Bound reconstructed PeTTaChainer statement terms before parsing. Direct
  construction can no longer route oversized or non-string duplicate typed
  term text into the canonical parser before the immutable checked-add
  boundary rejects it. Focused and full 677-test verification passed with
  repository-local `git diff --check`; local commit `faad440` (2026-08-07
  17:00 PDT / 2026-08-08 00:00 UTC). Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Bound reconstructed PeTTaChainer query terms before parsing. Direct
  reconstruction can no longer pair a small forged query atom with an
  oversized duplicate typed term to bypass the immutable contract's pre-parse
  resource ceiling. Focused and full 675-test verification passed with
  repository-local `git diff --check`; local commit `99fe409` (2026-08-07
  15:00 PDT / 22:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.

- [x] Close reconstructed PeTTaChainer episode stamp gaps. The immutable
  contract now requires its admitted stamp keys to equal `0..n-1`, preserving
  the source compiler's complete stamp-map invariant. Focused and full
  675-test verification passed with repository-local `git diff --check`;
  local commit `a9d4e65` (2026-08-07 11:00 PDT / 18:00 UTC). Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close mutable PeTTaChainer statement provenance sidecars. Stamp and
  evidence-basis collections now require non-empty immutable tuples rather
  than relying on incidental tuple/list comparison. Focused and full 674-test
  verification passed with repository-local `git diff --check`; local commit
  `d0adc8c` (2026-08-07 09:00 PDT / 16:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.

- [x] Close PeTTaChainer input-statement stamp provenance. Every immutable
  checked-add statement now requires exactly one non-empty evidence-basis id
  per stamp, matching the downstream derived-result boundary and preventing
  partially mapped audit sidecars. Focused and full 672-test verification
  passed with repository-local `git diff --check`; local commit `640e715`
  (2026-08-07 03:00 PDT / 10:00 UTC). Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Close malformed immutable dependencies at the PeTTaChainer
  derived-capture and episode-manifest construction boundaries. Fact/rule and
  validator/runtime stage-capture inputs, plus the episode budget, are now
  type-checked before dereference. Full 669-test verification passed with
  repository-local `git diff --check`; local commits `020f1a4` and `0ec094f`
  (2026-08-06 23:00 PDT / 2026-08-07 06:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close malformed checked-add statement members at the PeTTaChainer
  episode-contract boundary. `PeTTaChainerEpisodeContract` now requires every
  member to be an immutable `PeTTaChainerInputStatement` before extracting
  proof ids. Focused and full 669-test verification passed with
  repository-local `git diff --check`; local commit `817848d` (2026-08-06
  17:00 PDT / 2026-08-07 00:00 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close malformed bounded kernel-capture persistence before filesystem
  mutation. `write_kernel_process_capture()` now builds and serializes its
  typed checksummed document before creating the destination parent; malformed
  input leaves an absent parent absent. Focused and full 667-test verification
  passed with repository-local `git diff --check` (2026-08-05 21:00 PDT /
  2026-08-06 04:00 UTC); local commit `ece240a`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close malformed PeTTaChainer manifest serialization. The public document
  builder now requires a typed `PeTTaChainerEpisodeManifest` before extracting
  its payload, preventing incidental `AttributeError`s at the persistence
  boundary. Focused and full 664-test verification passed with repository-local
  `git diff --check` (2026-08-05 05:24 PDT / 12:24 UTC); local commit
  `fa5c695`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close malformed optional capture handling before episode-manifest
  artifact I/O. `read_episode_manifest()` now validates a supplied
  `KernelProcessCapture` alongside its other optional replay dependencies,
  preserving deterministic caller-error precedence even if the artifact path
  is absent or malformed. Focused and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-04 23:03 PDT / 2026-08-05
  06:03 UTC); local commit `4935583`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close malformed optional replay dependencies at episode-manifest reload.
  `read_episode_manifest()` now requires typed `CompiledEpisodeInputs` and
  `ValidatedKernelResult` values whenever those replay checks are requested,
  preventing incidental `AttributeError`s before provenance comparison.
  Focused and full 664-test verification passed with repository-local `git
  diff --check` (2026-08-04 21:35 PDT / 2026-08-05 04:35 UTC); local commit
  `e6e871d`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close malformed compiled-input handling at the core kernel-result
  admission boundary. `validate_kernel_result()` now requires a typed
  `CompiledEpisodeInputs` before parsing output or looking up stamps, so direct
  admission and every capture/replay wrapper share the same stable typed
  failure contract. Focused 89-test and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-04 17:00 PDT / 2026-08-05
  00:00 UTC); local commit `473962b`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close malformed dependency handling at the exact kernel replay
  boundaries. `validate_exact_kernel_replay()` and
  `validate_exact_kernel_capture_replay()` now require a typed
  `ValidatedKernelResult` and `CompiledEpisodeInputs` before field access; the
  clean-room captured-replay regression proves `None` inputs fail as stable
  `ValueError`s rather than incidental `AttributeError`s. Focused and full
  660-test verification passed with repository-local `git diff --check`
  (2026-08-04 15:00 PDT / 22:00 UTC); local commit `7801117`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Regression-close requested-pipe validation cleanup failures. A mocked
  malformed process construction now proves that an unexpected supplied-stream
  close failure is preserved as the cause of
  `ValueError("kernel subprocess pipe validation cleanup failed")`, without
  skipping the remaining supplied stream close. Focused 1-test and full
  660-test verification passed with repository-local `git diff --check`
  (2026-08-04 01:00 PDT / 08:00 UTC); local commit `d8728dc`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Close the bounded kernel requested-pipe boundary. Immediately after
  process construction, `run_kernel_subprocess()` now requires stdin, stdout,
  and stderr to exist; a missing requested pipe triggers process-group kill,
  direct-process reap, closure of every supplied pipe, and a typed failure.
  Focused 1-test and full 659-test verification passed with repository-local
  `git diff --check` (2026-08-03 23:03 PDT / 2026-08-04 06:03 UTC); local
  commit `f2e809e`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close the bounded kernel captured-stream cleanup exception boundary.
  Unexpected stdout/stderr close failures now become
  `ValueError("kernel subprocess stream cleanup failed")` with the original
  cause, while both streams receive a close attempt. Focused and full
  649-test verification passed with repository-local `git diff --check`
  (2026-08-03 03:00 PDT / 10:00 UTC); local commit `c748b58`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Close the bounded kernel direct-process wait exception boundary. An
  unexpected ordinary `process.wait()` failure now becomes
  `ValueError("kernel subprocess wait failed")` with its original cause, and a
  regression verifies process-group termination plus stdout/stderr closure.
  Focused 1-test and full 647-test verification passed with repository-local
  `git diff --check` (2026-08-02 23:00 PDT / 2026-08-03 06:00 UTC); local
  commit `e1af2e4`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close the explicit subprocess environment against duplicate-key iterator
  output. `run_kernel_subprocess()` now rejects repeated keys before launch,
  preserving an unambiguous one-to-one relationship between admitted entries,
  the environment delivered to the child, and the canonical capture. A
  marker-backed focused test and the full 643-test suite passed with
  repository-local `git diff --check` (2026-08-01 05:00 PDT / 12:00 UTC);
  local commit `aa39ee3`.
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.

- [x] Close the bounded kernel process-launch exception boundary. Missing or
  otherwise OS-rejected executables now fail through the runner's typed
  `ValueError` contract, with the original `OSError` retained as cause for
  diagnosis. Focused 1-test and full 643-test verification passed with
  repository-local `git diff --check` (2026-07-31 15:00 PDT / 22:00 UTC);
  local commit `52e9737`. Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.

- [x] Close the bounded kernel program boundary against embedded NUL bytes.
  `run_kernel_subprocess()` now rejects NUL-bearing program text before
  process launch; a marker-backed regression proves the child is not started.
  Focused 1-test and full 641-test verification passed with repository-local
  `git diff --check` (2026-07-31 09:00 PDT / 16:00 UTC); local commit
  `07827c2`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close the typed raw-capture argv boundary against embedded NUL bytes.
  `KernelProcessCapture` now rejects OS-impossible argv entries just as
  `run_kernel_subprocess()` already did, so a manually reconstructed capture
  cannot bypass the runner's launch-shape validation before Phase-0 replay.
  Focused 2-test and full 640-test verification passed with repository-local
  `git diff --check` (2026-07-31 01:00 PDT / 08:00 UTC); local commit
  `5a7393f`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close fresh Phase-0 replay against an explicit alternate subprocess
  environment. `KernelProcessCapture` now preserves canonical sorted unique
  caller-supplied environment entries, the runner populates them, and the
  frozen reference gate admits only its inherited-environment launch shape.
  Focused and full 639-test verification passed with repository-local `git
  diff --check` (2026-07-30 23:00 PDT / 2026-07-31 06:00 UTC); local commit
  `561d773`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.

- [x] Close fresh Phase-0 replay against an explicit alternate subprocess
  working directory. `KernelProcessCapture` now preserves the normalized
  caller-supplied `cwd`, the runner populates it, and the frozen reference gate
  admits only its inherited-working-directory launch shape. Focused and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-30 21:00 PDT / 2026-07-31 04:00 UTC); local commit `ed17c09`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the unexpected bounded-kernel launch exception boundary. Any
  ordinary exception raised while constructing the isolated process now uses
  `ValueError("kernel subprocess could not be launched")` and retains its
  original cause. Focused 3-test and full 658-test verification passed with
  repository-local `git diff --check` (2026-08-03 21:01 PDT / 2026-08-04
  04:01 UTC); local commit `6c7ce16`. Runtime invocation, result admission,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close fresh Phase-0 replay against unreviewed launch arguments. The
  frozen stdin-fed replay gate now admits only the normalized pinned executable
  as its sole argv entry; an otherwise exact capture carrying an extra mode
  flag fails closed. Focused and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 19:00 PDT / 2026-07-31
  02:00 UTC); local commit `0da04d9`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Close fresh Phase-0 replay against the capture's canonical program CID
  as well as its direct byte digest. The admitted reference derives the same
  complete-program CID from its checksum-verified UTF-8 source, and a capture
  presenting the correct program SHA-256 with a contradictory CID fails
  closed. Focused and full verification passed with repository-local `git
  diff --check` (2026-07-30 15:00 PDT / 22:00 UTC); local commit `bbf5118`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Bind fresh Phase-0 replay to the frozen program bytes. A bounded
  `run_kernel_subprocess()` capture now records the direct UTF-8 program
  SHA-256, and `validate_phase0_reference_replay()` rejects an otherwise
  byte-identical capture whose program digest differs from the admitted
  reference source. Focused and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 13:02 PDT / 20:02 UTC).
  Promotion, writes, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Bind fresh Phase-0 replay to the frozen runtime executable. A
  digest-pinned `run_kernel_subprocess()` capture now records the executable
  SHA-256, and `validate_phase0_reference_replay()` rejects an otherwise
  byte-identical capture from a different or unpinned executable. Focused and
  full verification passed; local commit `dc5326e` (2026-07-30 11:00 PDT / 18:00 UTC). Promotion,
  writes, live integration, dependencies, paid compute, and remote actions
  remain closed.

- [x] Close the frozen Phase-0 producer output inventory. Admission now
  requires exactly the ordered semantic-result and successful-marker lines,
  ignoring only blank lines; a fully rehashed extra authority-shaped line
  fails closed. Focused reload and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 09:00 PDT / 16:00 UTC);
  local commit `23b9c5d`.
  Runtime invocation, promotion/write, live integration, dependency changes,
  paid compute, and remote actions remain closed.

- [x] Require frozen Phase-0 semantic output to preserve exact standalone
  producer line shape. Admission now rejects a fully rehashed output that
  embeds the canonical declared result inside a larger result line. Focused
  reload and full 639-test verification passed with repository-local `git
  diff --check` (2026-07-30 07:01 PDT / 14:01 UTC). Runtime invocation,
  promotion/write, live integration, dependency changes, paid compute, and
  remote actions remain closed.

- [x] Type-close the frozen Phase-0 semantic result itself. Admission now
  requires one bounded canonical patham9 kernel-result atom, finite
  unit-interval STV values, and non-empty canonical sorted unique stamps; a
  rehashed pass-diagnostic relabel fails closed. Focused reload and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-30 05:01 PDT / 12:01 UTC); local commit `22c1f95`. Runtime
  invocation, promotion/write, live integration, dependency changes, paid
  compute, and remote actions remain closed; local commit `ef5136c`.
- [x] Close cyclic-symlink failure behavior at the bounded kernel `cwd`
  boundary. `run_kernel_subprocess()` now maps `Path.resolve()` cycle failures
  to its documented pre-launch `ValueError`; a marker-backed regression proves
  the child is not started. Focused 1-test and full 642-test verification
  passed with repository-local `git diff --check` (2026-07-31 13:00 PDT /
  20:00 UTC); local commit `90d539c`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.

- [x] Close the frozen Phase-0 reference-manifest schema inside the Phase-1
  clean-room reload gate. Admission now requires exact top-level,
  determinism, example, runtime, repository, result, and boundary member sets;
  a rehashed boundary carrying undeclared promotion authority fails closed.
  Focused reload and full 639-test verification passed with repository-local
  `git diff --check` (2026-07-30 01:00 PDT / 08:00 UTC); local commit
  `1462790`. Runtime invocation, promotion/write, live integration, dependency
  changes, paid compute, and remote actions remain closed.

- [x] Bind frozen usability checksum sidecars to the producer's exact
  bundle-local journal path. Admission now rejects two fully rehashed,
  byte-identical sidecars naming `relocated/journal.metta`, while preserving
  the distinct sidecar-equality failure first. Focused 33-test and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-29 23:00 PDT / 2026-07-30 06:00 UTC); local commit `7c00f0a`.
  Runtime invocation, promotion/write, live integration, dependency changes,
  paid compute, and remote actions remain closed.

- [x] Reproduce the frozen usability producer's exact checksum-sidecar
  equality. Admission now requires the after-ingest and after-canary sidecars
  to be byte-identical after independently validating both journal digests,
  rejecting a fully rehashed same-digest/different-path adversary. Focused
  32-test and full 638-test verification passed with repository-local `git
  diff --check` (2026-07-29 21:00 PDT / 2026-07-30 04:00 UTC); local commit
  `dac7e36`. Runtime invocation, promotion/write, live integration, dependency
  changes, paid compute, and remote actions remain closed.

- [x] Reconstruct frozen usability diagnostic lines from captured runtime
  tails. Admission now requires exact producer-equivalent stripped diagnostic
  lines, rejecting a fully rehashed result that omits its observed pass line.
  Focused 31-test and full 637-test verification passed with repository-local
  `git diff --check` (2026-07-29 19:00 PDT / 2026-07-30 02:00 UTC); local
  commit `96e152e`. Runtime
  invocation, promotion/write, live integration, dependency changes, paid
  compute, and remote actions remain closed.

- [x] Preserve the frozen producer's runtime-tail resource bound in admission.
  Stdout and stderr tails must each be at most 4,000 characters; a fully
  rehashed oversized tail fails closed. Focused 28-test and full 634-test
  verification passed with repository-local `git diff --check`; local commit
  `a82d708` (2026-07-29 13:00 PDT / 20:00 UTC). Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.

- [x] Type-close frozen usability diagnostic fields. Admission now requires
  string stdout/stderr tails and a list of string diagnostic lines, rejecting
  a fully rehashed result that substitutes structured authority-shaped JSON.
  Focused 27-test and full 633-test verification passed with repository-local
  `git diff --check`; local commit `79ba928` (2026-07-29 11:00 PDT /
  18:00 UTC). Runtime invocation, promotion/write, live integration,
  dependency changes, and remote actions remain closed.

- [x] Require frozen usability provenance identities to be canonical MeTTa
  terms. Admission now rejects a fully rehashed evidence identity containing
  an injected control form even when the source atom and digest are updated.
  Focused 26-test and full 632-test verification passed with repository-local
  `git diff --check`; local commit `3bdc28d` (2026-07-29 09:00 PDT /
  16:00 UTC). Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.

- [x] Require the frozen usability source term to be one canonical executable
  MeTTa term. Admission now parses the term in a single-expression envelope
  and requires canonical round-trip equality; a fully rehashed
  newline/control-form injection-shaped term fails closed. Focused 25-test and
  full 631-test verification passed with repository-local `git diff --check`;
  local commit `4ec0449` (2026-07-29 07:02 PDT / 14:02 UTC). Runtime
  invocation, promotion/write, live integration, dependency changes, and
  remote actions remain closed.

- [x] Preserve the frozen usability source's non-empty provenance identities.
  Admission now requires non-empty string belief, cluster, evidence,
  promotion-domain, promotion-event, and promotion-rule fields; a fully
  rehashed source with an erased promotion rule fails closed. Focused 24-test
  and full 630-test verification passed with repository-local `git diff
  --check`; local commit `bae697c` (2026-07-29 05:00 PDT / 12:00 UTC).
  Runtime invocation, promotion/write, live integration, dependency changes,
  and remote actions remain closed.

- [x] Bind frozen provider-free usability source classification to the
  non-inferred PLN input boundary. Admission now requires exact
  `pln-ready-input-not-inferred-belief` status; a fully rehashed
  `inferred-belief` relabel fails closed. Focused 22-test and full 628-test
  verification passed with repository-local `git diff --check`; local commit
  `703e071` (2026-07-29 01:00 PDT / 08:00 UTC). Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.

- [x] Bind the frozen provider-free usability provenance atom to the runtime
  source identity. Admission now reconstructs the exact patham9/PLN source
  item atom from its term, STV, and evidence id; a fully rehashed unrelated
  atom fails closed. Focused 21-test and full 627-test verification passed with
  repository-local `git diff --check`; local commit `ea0db1f` (2026-07-28
  23:00 PDT / 2026-07-29 06:00 UTC). Runtime invocation, promotion/write, live
  integration, dependency changes, and remote actions remain closed.

- [x] Bind the frozen provider-free usability inference's semantic pass count
  to its single reconstructed `Test`. Admission now requires exactly one
  successful marker; a fully rehashed two-pass-marker result fails closed.
  Focused 19-test and full 625-test verification passed with repository-local
  `git diff --check`; local commit `ff67c3e` (2026-07-28 19:00 PDT /
  2026-07-29 02:00 UTC). Runtime invocation, promotion/write, live integration,
  dependency changes, and remote actions remain closed.

- [x] Bind frozen provider-free usability inference runtime inputs and expected
  truth value to the provenance-bearing source item. Admission reconstructs the
  exact source Sentence, synthetic bridge Sentence, and TotalMp expected result;
  a fully rehashed source-Sentence substitution fails closed. Focused 18-test
  and full 624-test verification passed with repository-local `git diff
  --check` (2026-07-28 17:15 PDT / 2026-07-29 00:15 UTC); local commit
  `fb13cf7`. Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.

- [x] Bind frozen provider-free usability inference provenance to the exact
  source/derived-term relationship and two-stamp sidecar roles. Require the
  source sidecar's item term and evidence id to agree with the declared source,
  and require the bridge to remain the index-zero synthetic non-live
  implication. A fully rehashed source relabel fails closed. Focused 17-test
  and full 623-test verification passed with repository-local `git diff
  --check`; local commit `de68ca3` (2026-07-28 15:00 PDT / 22:00 UTC).
  Runtime invocation, promotion/write, live integration, dependency changes,
  and remote actions remain closed.

- [x] Bind frozen provider-free usability inference admission to the exact
  bounded PLN program text reconstructed from its two declared runtime
  sentences, derived query term, and expected result. A fully rehashed
  executable-text substitution now fails closed. Focused 16-test and full
  622-test verification passed with repository-local `git diff --check`;
  local commit `f68be17` (2026-07-28 13:02 PDT / 20:02 UTC). Runtime
  invocation, promotion/write, live integration, dependency changes, and
  remote actions remain closed.

- [x] Bind frozen provider-free usability inference admission to the exact
  non-live program boundary and provenance-preserving runtime-stamp policy.
  Fully rehashed replacements claiming live integration or discarded source
  provenance now fail closed. Focused 15-test and full 621-test verification
  passed with repository-local `git diff --check`; local commit `3c4d3e2`
  (2026-07-28 11:00 PDT / 18:00 UTC). Runtime invocation, promotion/write, live integration,
  dependency changes, and remote actions remain closed.

- [x] Bind frozen provider-free usability inference admission to the exact
  patham9/PLN derivation-program schema, read-only two-premise mode, and member
  set. A fully rehashed result using an unreviewed program schema now fails
  closed. Focused 13-test and full 619-test verification passed with
  repository-local `git diff --check`; local commit `b7230cc` (2026-07-28
  09:02 PDT / 16:02 UTC).
  Runtime invocation, promotion/write, live integration, dependency changes,
  and remote actions remain closed.

- [x] Close JSON boolean/integer type confusion in frozen usability inference
  admission. All three `semantic_markers` counts now require exact integers;
  a fully rehashed result using `true` for `passed_true_count` fails closed
  even though Python compares it equal to `1`. Focused 9-test and full
  615-test verification passed with repository-local `git diff --check`;
  local commit `74859ec` (2026-07-28 03:00 PDT / 10:00 UTC). Runtime
  invocation, promotion/write, live integration, dependency changes, and
  remote actions remain closed.

- [x] Semantically close frozen usability inference admission. Require the
  patham9/PLN result schema, zero process/classifier return codes, a positive
  passed-marker count, semantic success, and zero false/error markers; a fully
  rehashed bare `{"status":"passed"}` result now fails closed. Focused 8-test
  and full 614-test verification passed with repository-local `git diff
  --check`; local commit `8e9c567` (2026-07-28 01:00 PDT / 08:00 UTC).
  Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.

- [x] Semantically close the frozen usability journal checksum sidecars:
  require exact `sha256sum` record framing for `journal.metta` and require
  each recorded digest to equal the independently recomputed journal digest.
  A fully rehashed false-sidecar adversary fails closed. Focused 6-test and
  full 612-test verification passed with repository-local `git diff --check`;
  local commit `08abbde` (2026-07-27 21:01 PDT / 2026-07-28 04:01 UTC).
  Promotion/write, runtime invocation, live integration, dependency changes,
  and remote actions remain closed.

- [x] Close the frozen provider-free usability summary to its exact schema-v2
  member set, rejecting undeclared fields even when all declared artifact
  digests and non-live claims are valid. Focused 5-test and full 611-test
  verification passed with repository-local `git diff --check`; local commit
  `7ef5748` (2026-07-27 19:00 PDT / 2026-07-28 02:00 UTC). Promotion/write,
  runtime invocation, live integration, dependency changes, and remote actions
  remain closed.

- [x] Add a producer-owned, read-only admission API for frozen provider-free
  usability bundles. `validate_provider_free_usability_bundle()` requires the
  exact schema-v2 ten-file inventory, bounded regular non-symlink artifacts,
  unambiguous UTF-8 JSON, every declared digest, byte-identical restart
  retrieval, passed inference, and explicit non-live authority. Tampered,
  extra-artifact, and promotion-authorized bundles fail closed. Focused 4 and
  full 610 tests passed with repository-local `git diff --check`; local commit
  `0971225` (2026-07-27 17:03 PDT / 2026-07-28 00:03 UTC). No canonical write,
  promotion, runtime invocation, live integration, dependency change, or
  remote action.

- [x] Integrity-bind the complete non-self-referential provider-free usability
  evidence bundle. Summary schema v2 now records SHA-256 digests for the
  persistent journal lock and both journal checksum sidecars as well as the
  original six evidence files; the regression independently recomputes every
  declared artifact digest except `summary.json` itself. Focused verification
  passed 5 tests; full discovery passed 606 tests; repository-local `git
  diff --check` passed in local commit `41dfdda` (2026-07-27 15:00 PDT /
  22:00 UTC). No promotion/write, live integration, paid compute, dependency
  change, or remote action.

- [x] Version the provider-free usability summary and enumerate its exact
  evidence bundle, including the journal lock, checksum sidecars, and summary
  itself. The regression rejects undeclared output artifacts. Focused
  verification passed 5 tests; full discovery passed 606 tests; repository-local
  `git diff --check` passed in local commit `3773908` (2026-07-27 13:05 PDT /
  20:05 UTC). No promotion/write, live integration, paid compute, dependency
  change, or remote action.

- [x] Make provider-free reproducibility evidence self-describing: include the
  restarted retrieval artifact in `summary.json`, assert its digest equals the
  pre-restart retrieval, and record the semantic inference status. Focused
  verification passed 5 tests; full discovery passed 606 tests; repository-local
  `git diff --check` passed in local commit `8861980` (2026-07-27 09:00 PDT /
  16:00 UTC). No promotion/write, live integration, paid compute, dependency
  change, or remote action.

- [x] Require the provider-free usability output directory's immediate parent
  to exist and replace recursive `mkdir -p` with a single-directory create.
  A nested request with a missing parent now exits 2 without creating any
  filesystem entry. Focused verification passed 5 tests; full discovery passed
  606 tests; repository-local `git diff --check` passed in local commit
  `ac64440` (2026-07-27 07:01 PDT / 14:01 UTC). No runtime promotion/write,
  upstream/remote action, paid compute, dependency change, or live integration.

- [x] Add an automated no-overwrite regression for the provider-free usability
  gate. An existing output directory containing operator-owned data is rejected
  with exit 2 before fixture ingestion or runtime work, and its exact entry
  bytes/mode remain unchanged. Focused verification passed 1 test; full
  discovery passed 602 tests; repository-local `git diff --check` passed
  in local regression commit `a64e7b1` (2026-07-26 13:00 PDT / 20:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  dependency change, or live integration.

- [x] Add a fully rehashed PeTTaChainer manifest resource-budget adversary.
  Setting `budget.max_steps` to zero and recomputing both the typed manifest
  digest and outer document checksum still fails closed during typed
  reconstruction. Focused and full 601-test verification passed with
  repository-local `git diff --check`; local regression commit `3364939`
  (2026-07-26 11:00 PDT / 18:00 UTC). Runtime invocation, promotion/write,
  upstream/remote action, paid compute, and live integration remain closed.

- [x] Add a fully rehashed PeTTaChainer manifest temporal-order adversary.
  Moving `finished_at` before `started_at` and recomputing both the typed
  manifest digest and outer document checksum still fails closed at typed
  reconstruction. Focused and full 601-test verification passed with
  repository-local `git diff --check`; local regression commit `11b853a`
  (2026-07-26 07:00 PDT / 14:00 UTC). Runtime invocation, promotion/write,
  upstream/remote action, paid compute, and live integration remain closed.

- [x] Add a fully rehashed PeTTaChainer manifest adversary for chart-anchor
  drift. Replacing `chart_fingerprint` and recomputing both the typed manifest
  digest and outer document checksum still fails closed against the supplied
  compiler contract. Focused and full 601-test verification passed with
  repository-local `git diff --check`; local regression commit `387c2fa`
  (2026-07-25 23:00 PDT / 2026-07-26 06:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action,
  paid compute, or live integration.

- [x] Add a fully rehashed rule-attribution adversary: replace the attribution
  artifact's bound result identity, recompute its internal attribution digest
  and outer document checksum, and require reload to reject it against the
  supplied admitted result. Local regression commit `a27984a`; focused and
  full 601-test verification passed with `git diff --check` (2026-07-25 13:00
  PDT / 20:00 UTC). No runtime invocation, promotion/write, upstream/remote
  action, paid compute, or live integration.

- [x] Add a fully rehashed manifest-attribution adversary: replace the
  PeTTaChainer manifest's attribution identity, recompute its internal manifest
  digest and outer document checksum, and require reload to reject the artifact
  against the supplied compiler-bound attribution. Local regression commit
  `48c278f`; focused and full 601-test verification passed with `git diff
  --check` (2026-07-25 11:00 PDT / 18:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Extend the PeTTaChainer two-cycle clean-room reload gate across the new
  compiler-bound rule-attribution artifact. Result, manifest, and attribution
  identities remain stable, and wrong artifact classes fail closed. Local
  regression commit `3835baf`; focused and full 601-test verification passed
  with `git diff --check` (2026-07-25
  07:00 PDT / 14:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] Bind typed PeTTaChainer validator/runtime stream captures to their exact
  stage labels. Correctly rehashed captures with swapped or relabeled stage
  roles now fail closed. Local implementation commit `6cef687`; focused and
  full 601-test verification passed, plus
  `git diff --check` (2026-07-25 01:00 PDT / 08:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Close typed PeTTaChainer derived-result provenance cardinality. Both fact
  and rule evidence-basis collections must now contain exactly one entry per
  retained stamp, even when a malformed caller recomputes the result digest.
  Local implementation commit `aabc3fa`; focused and full 601-test verification
  passed, plus `git diff --check` (2026-07-24 17:00 PDT / 2026-07-25 00:00
  UTC). No runtime invocation, promotion/write, upstream/remote action, paid
  compute, or live integration.

- [x] Lock literal-LF captured-result admission against CR and CRLF framing.
  The existing verbatim boundary already rejected both forms; regressions now
  prevent future newline-normalization from admitting them. Local regression
  commit `60aacb2`; focused and full 601-test verification passed, plus `git
  diff --check` (2026-07-24 09:00 PDT / 16:00 UTC). No runtime invocation,
  promotion/write, upstream/remote
  action, paid compute, or live integration.

- [x] Reconciled `docs/implementation-status.md` with the completed
  PeTTaChainer typed capture/result and episode-manifest persistence gates. The
  status no longer incorrectly advertises those gates as open; the remaining
  boundaries are trace/rule attribution, reviewed promotion/write, upstream
  repair adoption, and live integration. Documentation consistency check and
  the full test suite passed (2026-07-24 07:00 PDT / 14:00 UTC). No runtime,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Reconciled the specialized compiled-input kernel gate against the completed
  PeTTaChainer path. The original stock patham9 probe remains a valid negative
  result (`[()]` and a failed generic inversion test), but it is no longer the
  only route: immutable `compile_episode_inputs()` output now adapts to a
  checked PeTTaChainer contract, the exact single-import candidate completes
  bounded `compileadd` plus a one-rule non-stored derivation, TotalMP truth is
  independently recomputed, and typed result/manifest persistence reloads
  against the compiler contract. Fresh full verification passed 601 tests and
  `git diff --check` (2026-07-24 01:00 PDT / 08:00 UTC). Stock patham9 generic
  build support remains unsupported rather than weakened; promotion/write,
  upstream adoption, and live integration remain closed.

- [x] Completed the Phase-1 archived process-capture adversary matrix: clean-room manifest reload now explicitly rejects stderr and return-code drift in addition to stdout and program-commitment drift. Local regression commit `6de6912`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 19:00 PDT / 2026-07-24 02:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Made the Phase-1 no-unlogged-filesystem-effects success criterion executable. The combined clean-room regression now inventories the exact six initial artifacts, proves all reload/query admission steps leave that inventory unchanged, and admits only the explicitly constructed stale-descriptor adversary afterward. Local regression commit `e7602a9`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 13:00 PDT / 20:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Made the Phase-1 clean-room provenance distinction explicit for a newly asserted post-reload memory. A different statement, snapshot, and chart produce identities distinct from the loaded compiled sentence, and neither the frozen replay validator nor archived manifest admits the old derived result against that new assertion. Local regression commit `6ed4a63`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 09:00 PDT / 16:00 UTC). No schema/runtime change, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Added the duplicate-anchor adversary to the Phase-1 clean-room gate. Two valid, distinctly content-addressed evidence snapshots claiming the same logical `snapshot_id` are rejected by archive lookup, preventing filesystem order from choosing a runtime memory state. Local regression commit `2ef2505`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 07:01 PDT / 14:01 UTC). No schema/runtime change, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Added the explicit same-named cross-run collision adversary to the Phase-1 clean-room gate. A second compiled state reuses every human-readable archive identifier while changing evidence content; the resulting chart fingerprint and compiled sentence drift are rejected by archived result and manifest/program admission. Local regression commit `96b736f`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 05:00 PDT / 12:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Extended the Phase-1 clean-room gate across the current PeTTaChainer runtime descriptor/capture class. Two isolated create-once reload cycles preserve the derived result, validator stream, runtime stream, and manifest identities and retain the frozen `(T a)` query plus non-promotion classification. Cross-class reads and a valid but cross-contract manifest pairing fail closed. Local implementation commit `94d749c`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 03:00 PDT / 10:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Closed direct Phase-1 manifest reload over result-to-compiled stamp provenance. When both immutable artifacts are supplied, every result stamp must exist in the compiled stamp map and its ordered evidence-basis IDs must match exactly; a forged, checksummed manifest/result pair now fails closed. Local implementation commit `ef9aeb3`; focused 1 and full 600 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Closed late parent-directory drift at the legacy pi-PLN audit boundary. A public evidence-snapshot load now has a constructed regression in which the parent inode changes between initial admission and final revalidation; the artifact is rejected before typed reconstruction. Local regression commit `48d3e49`; focused 1 and full 598 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Closed the create-once artifact-creation cleanup branch. When descriptor-anchored exclusive creation fails and closing the already-open parent directory also fails, the artifact-creation error remains primary, the parent-close diagnostic is attached, and no artifact exists. Local implementation commit `fb6bfbb`; focused 1 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Closed the remaining combined cleanup branch when create-once PeTTaChainer publication cannot wrap the new artifact descriptor as a text stream and closing both the artifact descriptor and parent descriptor also fails. The primary stream-open failure is preserved, both cleanup notes remain observable, and the partial path is absent. Local implementation commit `d5d8f2a`; focused 1 and full 596 tests passed, plus `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Added the PeTTaChainer-specific EpisodeManifest adapter required by the retained-stream model. `PeTTaChainerEpisodeManifest` content-addresses the complete immutable contract and binds the compiler-closed result, validator/runtime capture identities, repaired source/profile, runtime/controller identities, budget, seed, and timestamps. It rejects contract/result sidecar drift and cannot set `promotion_authorized=True`. Local implementation commit `7656d29`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Next: add create-once checksummed manifest persistence/reload before any promotion/write/upstream/live gate.

- [x] Added create-once, checksummed JSON persistence for `PeTTaChainerDerivedResultCapture`. Reload reconstructs both nested `PeTTaChainerStageCapture` records and typed result digest, rejects document/schema drift, and requires exact episode/query plus fact/rule proof, stamp, and evidence-basis agreement with the supplied immutable compiler contract. Local implementation commit `57e60f0`; focused persistence regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Next: design a PeTTaChainer-specific EpisodeManifest adapter without opening promotion/write/upstream/live boundaries.

- [x] Defined the typed PeTTaChainer process/result capture boundary required before manifest work. `PeTTaChainerStageCapture` content-addresses bounded validator/runtime diagnostics; `PeTTaChainerDerivedResultCapture` binds those captures to the immutable compiler fact/rule digests, proof IDs, stamps, evidence bases, canonical derived atom, and TotalMP STV. Construction fails closed on gate/contract drift, non-unique or missing retained answers, proof/STV mismatch, or malformed stream identity. A fresh isolated pinned `e4db5ca` single-import probe admitted result digest `f77be2210dc63e507140d025645aae1d2d5e6c5f65407f7dbf7326716bb7ca24`. Local implementation commit `011a4a0`; artifact: `repos/petta-memory/artifacts/pettachainer_typed_derived_capture_2026-07-18T0300PDT.json`, SHA-256 `ccb9d1f4d54c2f5fd6dc2066f59d48f47d3d5848bf6a006a0dbdaf85b323d411`. Focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Next: add create-once persistence/reload before any PeTTaChainer-specific EpisodeManifest adapter; no promotion/write/upstream/live change.

- [x] Remeasured the first post-repair downstream rung on the exact single-import PeTTaChainer candidate. Public `compile` and direct `compile_` each returned one identical clause in 0.420 s (previously 256 versus 128), so the old wrapper 2x factor was coupled to duplicate registration too. Local implementation commit `0f59d71`; focused 92 and full 547 tests passed, plus `py_compile` and `git diff --check`. Artifact: `artifacts/pettachainer_repaired_wrapper_2026-07-17T0500PDT.json`, SHA-256 `51b12b5c3a4f6fec7aeed9d5c98f86a2b4b96e867c1e27db0587f5a434d8d3ef`. Next: remeasure fact-KB, predicate, annotation, `mm2stmt`, and collector rungs before another repair or `compileadd` retry; no upstream/live/write change.

- [x] Admitted the first isolated PeTTaChainer source repair under an exact critical-file gate. Removing only `context_generation.metta`'s duplicate `chainer/compile` import in a copied pinned `e4db5ca` checkout reduced direct `compile_` from 128 copies of one clause to one normalized-equivalent output, not the provisional 64. Added reusable before/after source/runtime gates and three regressions in local commit `a345255`; focused 90/full 545 tests, `py_compile`, and `git diff --check` passed. Next: rerun public-wrapper, fact-KB, predicate, annotation, `mm2stmt`, and collector rungs on the single-import candidate before any second repair or `compileadd` retry. Artifact: `artifacts/pettachainer_duplicate_import_repair_2026-07-17T0300PDT.json`; no upstream/live/write change.

- [x] Closed the complete measured PeTTaChainer concrete-fact multiplicity into a source-repair plan. A typed helper requires the empirical counts to close exactly (`1*8*4*2*2*2=256` for public compile; `1*2*2=4` for the deduplicated collector), rejects malformed/stale counts, and ranks isolated duplicate-registration removal first, exclusive zero-premise `mm2stmt` matching second, remaining matcher/evaluator investigation third, and byte-identical set collapse only as a separately parity-tested fallback. Plan: `docs/pettachainer_fact_fanout_repair_plan.md`; local commit `914083d`; focused 87/full 542 tests passed. Next: test the import repair only in an isolated pinned PeTTaChainer checkout and rerun existing compile rungs; keep `compileadd`/query/result/manifest gates closed.

- [x] Closed the final unexplained twofold factor within the single registered PeTTaChainer fact dispatcher. Under the exact pinned annotated-head and fact-ladder source gate, identical local bodies returned 64 copies through `(@ $stmt (: $prf $Type $tv))` versus 32 through direct structural `(: $prf $Type $tv)` matching, with one unique clause in each result. Local commit `05fbb37`; focused 85/full 540 tests passed. Next remains a reviewed upstream/deduplication strategy before retrying `mm2compile`/`compileadd`; no matcher/import patch or add/query/result gate is approved.

- [x] Separated the public `compile` wrapper from direct `compile_` dispatch. An exact source gate confirms the pinned wrapper is only `(compile_ $kb $stmt)`, yet the same bounded runtime returned 256 public-wrapper copies versus 128 direct-dispatch copies of one unique clause in 0.547 s. This assigns one 2x evaluator factor to the wrapper boundary and leaves a 16x factor inside direct `compile_` above the already-unique literal fact branch. Local implementation commit `546696a`; focused 76 and full 531 tests passed, plus `py_compile` and `git diff --check`. Next: isolate the nested `is-var` / implication / bidirectional condition ladder before evaluating any set collapse; keep `mm2compile`/`compileadd`/query/result/manifest gates closed.

- [x] Closed the residual twofold direct-`compile_` fan-out with an exact import-path and single-registration gate. `petta_chainer.metta` imports `chainer/compile` directly and again through `context_from_kb -> context_generation`; one source-equivalent local registration returned 64 copies versus 128 from direct `compile_`, with one unique clause in both cases. Local commit `8150d69`; focused 82/full 537 tests passed. The full fact-dispatch multiplicity is now source-localized, but no upstream deduplication/import change or add/query/result gate is approved.

- [x] Isolated the remaining PeTTaChainer fact-branch fan-out above the literal branch. The exact source-gated copied ladder substituted the unique literal KB for `compile-fact-kb`; its base clause, explicit-empty arm, and real empty `compile-outputs` arm each returned one copy in 0.460 s. Combined with the separately measured eight-copy `compile-fact-kb` and 256-copy public `compile`, this places the unexplained 32x factor in the wrapper/`compile_` dispatch path. Local implementation commit `4a2e9a7`; focused 72 and full 527 tests passed, plus `py_compile` and `git diff --check`. Next: isolate `compile` versus direct `compile_` and then the nested dispatch conditions before evaluating set collapse; keep `mm2compile`/`compileadd`/query/result/manifest gates closed.

- [x] Current progress slice pinned the read-only `live-goal-bridge --run-patham9-runtime` to exact result/program schema identities. Wrong but non-empty patham9 query-smoke schemas now fail closed before GoalChainer appraisal. Verification: local implementation commit `f42d293`; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision-status boundary. The bridge now rejects missing/non-string/unknown decision statuses before emitting a bridge artifact; allowed review statuses are `recommended`, `candidate`, `held`, `weak`, and `blocked`. Verification: focused live-bridge tests pass 20 cases; local implementation commit `0d376e9`; full unittest discovery passes 433 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

# Tasks

- [ ] **ProtoCosmo2 ownership after ASI:Cloud VM2 migration (Ben,
  2026-08-16)** — after the Omega bots are successfully ported and accepted on
  VM2, hand `petta-memory` to ProtoCosmo2 as its first major task. This is
  sequenced after VM2 acceptance and the Protomega2-first Iter staging work;
  do not start early.

- [x] 2026-07-27: Integrate the frozen provider-free PeTTa-memory evidence
  bundle with ProtoMegaBot2 as a read-only shadow consumer. Deliverable: a
  narrow public-interface adapter that retrieves one known episode and its
  recorded pi-PLN result, emits one bounded candidate-context annotation, and
  remains provider-free and write-free. Acceptance test: clean-checkout replay
  passes; source journal/index/evidence hashes are byte-identical before and
  after; restart output is identical; malformed, missing, tampered,
  wrong-version, and ambiguous inputs fail before ThreadKeeper state changes.
  Completed in ProtoMegaBot2 branch `agent/petta-memory-shadow-consumer` at
  commit `fc30964`; eight focused tests and the recorded restart/hash gate
  passed. Evidence:
  `projects/petta-memory/experiments/20260727T233914Z-protomegabot2-shadow-consumer-branch/`.
  Cross-project link: `projects/protomegabot2/TASKS.md`.

- [x] Extend the Phase-1 clean-room reload gate across the frozen Phase-0 replay-anchor class: preserve exact source/output commitments over two isolated cycles and reject stale source content before admission. Local commit `f84d45d`; focused 1 and full 600 tests passed; runtime and live boundaries remain closed.

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] Close the reconstructed PeTTaChainer contract size bypass. The immutable
  contract now applies the compiler adapter's aggregate one-million-character
  ceiling to checked-add plus query atoms, so direct construction cannot evade
  the bounded runtime-input gate. Focused and full 675-test verification passed
  with repository-local `git diff --check`; local commit `dde58b4` (2026-08-07
  13:01 PDT / 20:01 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.

- [x] Reject a fully rehashed PeTTaChainer episode manifest whose seed is
  negative. The typed deterministic-input invariant remains binding even when
  both manifest digests are recomputed (focused and full 601-test verification
  plus `git diff --check`; local regression commit `d3ca892`; 2026-07-26
  09:00 PDT / 16:00 UTC). Runtime
  invocation, promotion/write, upstream/remote action, paid compute, and live
  integration remain closed.

- [x] Reject a fully rehashed PeTTaChainer episode manifest that flips
  `promotion_authorized` to true. The typed non-live invariant remains binding
  even when both the manifest digest and document checksum are recomputed
  (`4ba88fb`; focused and full 601-test verification plus `git diff --check`;
  2026-07-26 03:00 PDT / 10:00 UTC). Runtime invocation, promotion/write,
  upstream/remote action, paid compute, and live integration remain closed.

- [x] **Phase-1 runtime capture/reload gate.** Implemented a bounded, non-live clean-room roundtrip over current PeTTaChainer captures/manifests, legacy πPLN compiled/result/manifest artifacts, and frozen Phase-0 replay manifests. Two isolated cycles retain stable identities and frozen-query behavior; stale source and output, malformed descriptors, provenance mismatch, duplicate anchors, wrong artifact classes, and cross-run collisions fail closed. Final frozen-output regression commit `cf8ed5d`; focused test passed. Promotion, external writes, upstream adoption, and live integration remain closed.

  **Scope:**
  - Cover three artifact classes: current runtime descriptors, legacy πPLN artifacts, and frozen replay manifests.
  - Adversarial cases: stale descriptors, provenance mismatch, duplicate anchors, wrong artifact class, cross-run descriptor collision.
  - Promotion, writes outside the sandbox, upstream adoption, and live integration remain explicitly closed.

  **Success gate:**
  - Deterministic reload.
  - Semantic equivalence on frozen probes.
  - 100% rejection of malformed or provenance-invalid artifacts.
  - No unlogged filesystem effects.
  - Stable descriptor identity across repeated capture/reload cycles.
  - The reloaded system can use admitted memories for frozen queries without confusing "loaded from archive," "derived during capture," and "newly asserted after reload."

  **Failure gate:**
  - Semantic drift, nondeterminism, an admitted stale/mismatched descriptor, an unexplained write, or inability to distinguish artifact provenance after reload.
  - On failure: declare the specific failure mode and pause; do not open an unbounded hardening branch.

  **Boundary:** No new accessors, no provenance schema changes, no chemistry changes. Filesystem hardening is frozen unless the gate exposes a concrete admission flaw.

- [x] Filesystem hardening frozen (2026-07-22). The descriptor-anchored admission boundary covers ownership, group-writable, inode drift, symlinks, hard links, special files, duplicate JSON members, byte ceilings, nonblocking opens, trusted-parent metadata stability, and Unicode noncharacters across all four legacy πPLN audit loaders and the PeTTaChainer artifact boundary. 599 tests pass. No specific unresolved admission flaw remains; further edge-case hardening has diminishing returns unless the Phase-1 gate exposes a concrete gap.

- [x] Route the frozen Phase-0 patham9 replay-anchor manifest through the shared bounded, duplicate-safe, no-follow JSON loader. A regression proves duplicate top-level members are rejected rather than silently resolved by `json.loads`. Local implementation commit `5baedac`; focused 2 and full 599 tests passed; `git diff --check` passed. No runtime replay, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Require current-user ownership at the legacy pi-PLN audit boundary. The shared loader rejects a foreign-owned parent or artifact before JSON admission, and the create-once publisher rejects a foreign-owned parent before artifact creation. Local implementation commit `f726454`; focused 1 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Assess `iCog-Labs-Dev/metta-attention` at a pinned commit for integration
  with petta-memory, OmegaSelf, and the OmegaClaw emotion framework. Acceptance:
  inspect architecture/source/tests/CI; identify non-PLN uses, semantic and
  governance conflicts, a recommended boundary, and a staged validation plan;
  preserve the assessment in `docs/metta_attention_integration_assessment.md`.
  Completed 2026-07-21. Evidence: upstream commit
  `9196f38db749ddedeb591229dffddfa71664c38d`, successful upstream CI run
  `29728552904`, and the assessment document. Local Python synapse tests were
  not run because host Python lacks the declared `igraph` dependency; no
  dependency installation was performed.

- [x] Close the create-once stream-construction descriptor boundary. A failed `os.fdopen` now explicitly closes the already-created artifact descriptor; regressions require cleanup to remove the artifact and preserve the primary stream-open failure with any descriptor-close failure attached. Local implementation commit `be5c6d7`; focused 1 and full 596 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Close the successful create-once publication/parent-close boundary. A regression now requires a post-fsync parent-directory descriptor close error to propagate while preserving the readable create-once artifact. Local implementation commit `1e36bdf`; focused 1 and full 595 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Preserve both PeTTaChainer artifact cleanup diagnostics after a successful bounded read. A regression now requires the artifact-stream close error to remain primary when parent-descriptor close also fails, with the parent cleanup diagnostic attached. Local implementation commit `827a0c0`; focused 1 and full 595 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Preserve early PeTTaChainer artifact admission failures across parent-descriptor close failure. Unsafe-parent rejection and artifact-open failure now remain primary while the secondary close diagnostic is attached, including a Python 3.10-compatible note fallback. Local implementation commit `f07d5b1`; focused 2 and full 588 tests passed; `py_compile` and `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Reject trusted-parent metadata drift during PeTTaChainer artifact admission. The descriptor-anchored loader now compares parent device, inode, mode, link count, owner, and group before and after the bounded artifact read; regressions cover permission and ownership drift. Local implementation commit `39ba877`; focused 131 and full 586 tests passed; `py_compile` and `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Reject hard-link aliases during PeTTaChainer artifact admission. The bounded no-follow loader now requires exactly one filesystem link and includes link count in its before/after stability identity, preventing an admitted checksummed artifact from remaining mutable through another pathname. Local implementation commit `a167fef`; focused 3 and full 573 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Preserve PeTTaChainer artifact admission failures across descriptor-close failure. The bounded no-follow regular-file loader now retains the original rejection and attaches a secondary close diagnostic; successful admission still reports close failure normally. Local implementation commit `0a9f0fd`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Anchor PeTTaChainer create-once artifact publication to one opened parent directory. The shared durable writer now opens the parent once, creates the leaf relative to that descriptor, and fsyncs that same descriptor, closing a parent-path substitution race. The existing artifact is not removed when exclusive creation fails, partial pre-sync output is cleaned up, and file-synced output remains retained on directory-sync failure. Local implementation commit `019154a`; focused regression and full 570 tests passed; `git diff --check` passed. No promotion/write, upstream, remote, paid-compute, or live change.

- [x] Preserve create-once semantics across parent-directory fsync failure. Once a PeTTaChainer artifact has been fully written and file-synced, a later directory-sync error now propagates without deleting the completed artifact; a regression proves it remains valid and cannot be recreated. Local implementation commit `6aad801`; focused and full 570 tests passed, plus `py_compile` and `git diff --check`. No promotion/write, upstream, remote, paid-compute, or live change.

- [x] Made PeTTaChainer derived-capture and episode-manifest create-once persistence crash-durable across the directory-entry boundary. The shared writer now fsyncs the completed file and its parent directory; regressions require both syncs for both artifact types. Local implementation commit `5c1f0d7`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. No promotion/write, upstream, remote, paid-compute, or live change.

- [x] PeTTaChainer derived-capture and episode-manifest reload now opens the artifact itself with no-follow semantics and requires a regular file before bounded reading, preventing an otherwise valid checksummed artifact from being admitted through a mutable symlink target or special file. Local implementation commit `3f37f1c`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.

- [x] Bounded PeTTaChainer derived-capture and episode-manifest reload to 1,000,000 bytes before decode/parse. Oversized artifacts now fail closed alongside duplicate-member, checksum, type, and provenance checks. Local implementation commit `1d96182`; focused 115 and full 570 tests passed; `py_compile` and `git diff --check` passed. No runtime, promotion/write, upstream, or live change.

- [x] Hardened create-once PeTTaChainer derived-capture and episode-manifest reload against duplicate JSON object members at every depth. Ambiguous JSON now fails before checksum, typed reconstruction, or compiler-provenance admission. Local commit `145b902`; focused regression and full 570 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, or live integration change.

- [x] Closed the first typed PeTTaChainer derived-result/process capture. Immutable records content-address the validator/runtime stream identities and bind the canonical one-rule answer to exact compiler input/proof/stamp/evidence identities. Fresh pinned repaired runtime admission produced result digest `f77be221...`; persistence and manifest adaptation remain the next separate gate.

- [x] Bound the repaired TotalMP derivation gate to an immutable compiler-emitted two-statement `PeTTaChainerEpisodeContract`. `run_repaired_pettachainer_rule_episode_contract_gate()` rejects contracts unless they contain exactly one fact and one implication and query a non-stored target, then retains sentence digests, content-addressed proof IDs, stamps, and evidence-basis IDs while delegating to the exact proof/source/truth-formula runtime gate. Local implementation commit `d5abd83`; focused 113 and full 568 tests passed, plus `py_compile` and `git diff --check`. Next: define a typed PeTTaChainer derived-result/capture artifact before considering an EpisodeManifest; no promotion/write/upstream/live change.

- [x] Passed the first repaired PeTTaChainer one-rule derivation gate. Under the exact single-import candidate, `(S a)` plus `S→T` returned exactly `(: (rule-proof rule_s_t fact_a) (T a) (STV 0.7600000000000001 0.52))` in 0.377 s. The gate requires exact validators, fact/rule dispatch identities, a non-stored target, exact proof provenance, target-only answers, finite unit-interval STVs, and content-addressed streams. Local commit `b5cd150`; focused 110 and full 565 tests passed, plus `py_compile` and `git diff --check`. Artifact: `repos/petta-memory/artifacts/pettachainer_repaired_one_rule_derivation_2026-07-17T2100PDT.json`, SHA-256 `598d2dea624d4664ca029eb16150559bd5343205f16375d681e3d6ba5461e925`. Next: bind the rule/result to immutable compiler inputs and validate truth-formula provenance before any manifest; no promotion/write/upstream/live change.

- [x] Bound the exact single-import PeTTaChainer recall path back to one immutable compiler-emitted `PeTTaChainerEpisodeContract`. The gate requires exact public validator admission with content-addressed streams, the existing repair/source/storage checks, and a complete answer set containing only the typed input fact. A fresh run returned one answer and is classified only as `stored-fact-retrieval`. Local commit `9036dd2`; focused 109/full 564 tests, `py_compile`, and `git diff --check` passed. Artifact: `artifacts/pettachainer_repaired_typed_episode_contract_2026-07-17T1900PDT.json`, SHA-256 `0e68d1a9d459439db79004f7376ab83df412bbec30a820788c5d8b5064bb30ee`. Derived PLN inference, diagnostic interpretation, manifests, promotion/write, upstream adoption, and live integration remain closed.

- [x] Closed repaired exact-fact query admission over the entire result set, rejecting expected-plus-unrelated answers; fresh repaired probe returned exactly one expected answer and zero unexpected answers (`4cb2482`, 559 tests).

- [x] Passed the repaired PeTTaChainer exact stored-fact query gate under the exact single-import source repair. One gated `compileadd`, exact internal `&kb` check, and one-step query completed in 0.391 s with one unique answer matching the added proof/type/STV; numeric rendering normalized `0.70` to `0.7`. Local implementation commit `95ade3f`; focused 102 and full 557 tests passed, plus `py_compile` and `git diff --check`. Artifact: `artifacts/pettachainer_repaired_exact_fact_query_2026-07-17T1300PDT.json`, SHA-256 `11897c26895d1cc96798aee75eec85fb623c385353a496c66f16658fda6e91bb`. The captured runtime remained noisy (608,129 stdout, 142 stderr characters), so the next gate is exact typed episode-contract/result admission with diagnostics classified; no inferred-result promotion, write, upstream, or live integration change.

- [x] Passed the repaired PeTTaChainer `compileadd`-only gate under the exact single-import source repair. One promoted-fact statement completed in 0.362 s, returned one expected external fact, and produced one exact internalized `&kb` membership match. The new gate fails closed on source drift or missing storage and stops before query compilation/execution. Local implementation commit `df61d85`; focused 99 and full 554 tests passed, plus `py_compile` and `git diff --check`. Artifact: `artifacts/pettachainer_repaired_compileadd_add_only_2026-07-17T1100PDT.json`, SHA-256 `de979532a71ebdcd5ec3bb903d7ceb83237b7d2034fabfb883d1a7480af327c0`. Next: add a separately bounded exact-fact query rung; do not relax result admission or enable promotion/write/live integration.

- [x] Ran the real repaired PeTTaChainer `mm2compile` entry point after the exact single-import source gate. The one-statement fact path completed in 0.367 s with one unique expected fact; local commit `4cf97bf`, focused 96/full 551 tests, `py_compile`, and `git diff --check` passed. Artifact: `artifacts/pettachainer_repaired_full_mm2compile_2026-07-17T0900PDT.json`, SHA-256 `8547d988e26783039ae403b11c0f13b8d57f9d3d8d499b1b358796a73982a66b`. Next: retry repaired `compileadd` in an isolated add-only gate before any query; do not relax result admission or enable writes/live integration.

- [x] Resolve the first real compiled-input kernel gate at the specialized patham9/PeTTaChainer boundary. The stock patham9 generic probe remains a recorded negative result and its stderr/result admission was not relaxed. The alternate PeTTaChainer branch now consumes actual `compile_episode_inputs()` output through `build_pettachainer_episode_contract()`, completes source-gated bounded `compileadd` and one-rule derivation, independently checks TotalMP truth, and closes typed capture plus a non-promoting `PeTTaChainerEpisodeManifest` against the immutable compiler contract. Reconciled 2026-07-24 after full 601-test verification; stock generic patham9 support remains explicitly unsupported rather than inferred from the specialized `SMOKES.so`.

  - [x] Established the exact inert PeTTaChainer input contract with `build_pettachainer_episode_contract()`: compiler-emitted patham9 Sentences map deterministically to `(: pm-<full-sentence-digest> term (STV strength confidence))`, the query maps to `(: $prf term $tv)`, and the otherwise-unrepresentable patham9 stamps/evidence bases remain closed in typed audit sidecars. Local PeTTaChainer `check_stmt`/`check_query` admitted the exact shapes (`1.0` each). Focused 60 and full 501 tests passed, plus `py_compile` and `git diff --check`. Next gate: the already-required isolated `compileadd`/query runtime probe; do not route these atoms into stock patham9 `PLN.Query` or construct a manifest yet.
  - [x] Added a bounded fail-closed runtime probe for the typed episode contract in local commit `d9ee9f5`. It requires exact numeric `1.0` from every public statement validator and the query validator before entering a single isolated add/query subprocess; timeout, error, malformed stages, or an empty query result leaves `runtime_admitted=false`. Against pinned local PeTTaChainer `e4db5ca`, one exact typed statement and query validated in 0.073 s, but combined `compileadd`/query timed out at the 15 s wall bound, so no result or manifest was admitted. Focused 49 and full 504 tests passed, plus `py_compile` and `git diff --check`. Query/add bottleneck diagnosis remains open; do not relax the gate.
  - [x] Localized the exact contract's first add-path bottleneck beyond validation. A compiler-emitted lambda-free statement completed `materialize-stmt-lambdas` as identity in 0.479 s, but fanned out to 512 duplicate results (one unique atom; 796,938 captured stdout characters); direct `mm2compile`/collapse then timed out at 5 s. Materializer profile artifacts now keep exact multiplicity/uniqueness counts and at most 16 result samples. Local implementation commit `312efc2`; focused 51 and full 506 tests passed, plus `py_compile` and `git diff --check`. Next: inspect/instrument `mm2compile`/fact-assertion dispatch under this exact contract; keep `compileadd`/query/result/manifest gates closed.
  - [x] Isolated the exact contract's `compile_` fact-assertion dispatch from `mm2compile`. A source-gated bounded `compile` probe completed in 0.502 s and produced 256 copies of one unique base-fact clause (796,897 captured stdout characters), retaining only 16 samples. This locates substantial duplicate fan-out before `mm2compile`'s `mm2stmt`/temporary-context collection rather than proving add readiness. Local implementation commit `3ba8d3a`; focused 54 and full 509 tests passed, plus `py_compile` and `git diff --check`. Next: isolate `mm2stmt` conversion and temporary `ctx` collection on one deduplicated compiled clause; keep `compileadd`/query/result/manifest gates closed.
  - [x] Isolated `mm2stmt` and temporary `ctx` inspection from the compiler's duplicate fan-out. One source-equivalent base-fact clause converted in 0.469 s to two copies of one unique expected fact, while a separately cleared/read `ctx` contained zero atoms; runtime initialization still emitted 797,385 stdout and 168 stderr characters, so this is diagnostic completion rather than result admission. Local implementation commit `4cca4cd`; focused 58 and full 513 tests passed, plus `py_compile` and `git diff --check`. Next: isolate why `mm2stmt` doubles a single clause and whether `mm2compile` multiplies compiler and converter fan-out before any `compileadd`/query/result/manifest gate is reopened.
  - [x] Closed the source-level cause of the one-clause `mm2stmt` doubling. Pinned `compile.metta` defines both a specialized `(() |- ($ccl))` case arm and a general `($prms |- ($ccl))` arm, so empty premises unify with both and produce the two identical outputs already observed. `inspect_mm2stmt_fact_case_overlap()` records the exact bounded definition and fails closed on source drift. Local implementation commit `125cb6e`; focused 60 and full 515 tests passed, plus `py_compile` and `git diff --check`. Next: isolate the 256-copy `compile` dispatcher fan-out or measure a bounded deduplicated `mm2compile` equivalent without changing upstream semantics; keep `compileadd`/query/result/manifest gates closed.
  - [x] Measured the bounded deduplicated `mm2compile` equivalent without changing upstream semantics. `inspect_mm2compile_collection_shape()` closes the exact pinned clear/convert/collect source form before a copied expression replaces only `compile` with one canonical fact clause. The runtime completed in 0.461 s and returned four copies of one unique expected fact, separating another 2x collector multiplicity from the compiler's 256-copy input. Local implementation commit `fecb51c`; focused 65 and full 520 tests passed, plus `py_compile` and `git diff --check`. Next: inspect the 256-copy `compile` cause or test a reviewed set-collapse boundary before any `compileadd`/query/result/manifest gate is reopened.
  - [x] Isolated the exact fact branch's two components below `compile`. A source-drift-sensitive gate copied no upstream semantics and measured `compile-fact-kb` at eight copies of one unique KB term; `compile-outputs` produced no adapter outputs for the promoted fact shape. Local implementation commit `cbdb5de`; focused 69 and full 524 tests passed, plus `py_compile` and `git diff --check`. This accounts for one 8x factor inside the 256-copy dispatcher result. Next: isolate the remaining branching multiplicity around the fact clause before evaluating a reviewed set-collapse boundary; keep `mm2compile`/`compileadd`/query/result/manifest gates closed.

- [x] Closed the remaining Phase-2 program/capture substitution seam. `run_kernel_subprocess()` now records a canonical content commitment to the exact program delivered on stdin, and `build_captured_episode_manifest()` rejects a capture whose commitment differs from the manifest's `complete_program`. Local implementation commit `904b707`; focused 60 and full 501 tests passed, plus `py_compile` and `git diff --check`. No real compiled-input inference, rule/trace identity, promotion/write, or live integration claim.

- [x] Closed the Phase-2 capture-to-manifest substitution seam with `build_captured_episode_manifest()`: the exact immutable capture admitted by `validate_kernel_capture_result()` now supplies the manifest's return code, stdout, and stderr directly. Regressions cover successful end-to-end construction plus nonzero, noisy, and detached-result captures. Local implementation commit `9806fbb`; focused 1 and full 501 tests passed; `py_compile` and `git diff --check` passed. A real compiled-input episode, manifest persistence, rule/trace identity, promotion/write, and live integration remain open.

- [x] Executed and admitted the first fresh pinned Phase-0 Smokes replay through the bounded subprocess runner. New `validate_phase0_reference_replay()` fails closed on nonzero exit, stderr, output byte-count/checksum drift, and absent semantic markers. The real pinned MeTTa executable (`53455bfb...`) returned 0, empty stderr, and byte-identical 6,021-byte stdout (`fd5a6133...`). Local commit `bf2ea91`; focused 2 and full 499 tests passed, plus `py_compile` and `git diff --check`. Constructing a Phase-2 `EpisodeManifest` remains the next separate gate.

- [x] Added the missing fail-closed admission boundary for the frozen Phase-0 replay anchor in local implementation commit `cdc3b5d`. The validator closes manifest schema, local source/output hashes, exact output bytes, duplicate-run determinism hashes, canonical query, semantic result/pass marker presence, full patham9 commit, pinned runtime digest, and non-live flags. The real Smokes artifact admits; tampered output and relaxed boundary regressions fail. Focused 1 and full 498 tests passed, plus `py_compile` and `git diff --check`. Fresh pinned-runtime execution and EpisodeManifest construction remain the next separate gate.

- [x] Closed incomplete Phase-2 kernel program delivery in local commit `b3d631f`. The subprocess runner now flushes stdin and fails closed when the child closes its input before the complete bounded program is written, rather than returning a raw capture that could be mistaken for execution of the supplied program. Focused 4 and full 497 tests passed; `py_compile` and `git diff --check` passed. No semantic-result, promotion/write, or live-integration authority changed.

- [x] Closed a Phase-2 kernel capture timeout escape through inherited descendant pipes. Kernel subprocesses now run in a fresh process session, and the runner kills the complete process group on timeout, capture overflow, and direct-process completion before joining readers. A regression proves a direct child cannot exit while a five-second descendant keeps capture blocked. Focused 2 and full 496 tests passed; `py_compile` and `git diff --check` passed. No patham9 inference, promotion/write, or live integration.

- [x] Made the Phase-2 kernel output ceiling effective during capture rather than only after `subprocess.run()` had buffered unbounded output. Dedicated bounded pipe readers now kill the child as soon as either stream exceeds its byte budget; stdin writing is concurrent so timeout still applies when a child does not read a pipe-sized program. Local implementation commit `9899b1d`; focused tests, all 495 tests, `py_compile`, and `git diff --check` passed. No patham9 execution, semantic result claim, promotion/write, or live integration.

- [x] Narrowed the Phase-2 executable-pin symlink boundary. A pinned absolute executable is now strictly resolved before hashing, and that same resolved pathname is passed to `subprocess.run`; the immutable capture exposes the actual resolved argv. Local implementation commit `d73d054`; focused 1 and full 495 tests passed, plus `py_compile` and `git diff --check`. This does not eliminate replacement/TOCTOU on the resolved file or authorize runtime semantics, promotion/write, or live integration.

- [x] Hardened the Phase-2 kernel runner's stdin resource boundary. `run_kernel_subprocess()` now applies a positive byte-level `max_program_bytes` ceiling before process launch (UTF-8 bytes, not Python character count), defaulting to the existing episode-program limit. A regression proves a multibyte program over the limit is rejected without launching the child. Focused 3 and full 491 tests passed; `py_compile` and `git diff --check` passed. No patham9 invocation, promotion/write, trace/rule claim, or live integration.

- [x] Added the first Phase-2 bounded kernel subprocess/capture boundary. `run_kernel_subprocess()` uses explicit argv with `shell=False`, supplies the already-assembled program on stdin, enforces positive timeout and per-stream byte ceilings, rejects non-UTF-8 output, and returns an immutable raw capture that is explicitly not a validated PLN result. Focused tests cover successful stdout/stderr capture, timeout, and overflow. No promotion/write/live integration or trace/rule claim.

- [x] Closed a Phase-2 evaluator-boundary control-injection gap: packet statements and caller-supplied query terms now recursively reject the stock patham9 control heads `PLN.Config`, `PLN.Init`, `PLN.Query`, and `PLN.Derive`, identified from pinned patham9 revision `55f1751`. Focused compiler/assembler tests and the full 488-test suite pass; `py_compile` and `git diff --check` pass. No kernel execution, rule/trace attribution, promotion/write, or live integration.

- [x] Added an explicit opt-in parser-validation hook after bounded stock `PLN.Query` program assembly. Tests prove the exact returned program is checked, parser rejection fails closed, and non-callable hooks are rejected. Focused 47 and full 488 tests passed; `py_compile` and `git diff --check` passed. The default remains inert and does not invoke patham9 or authorize promotion/live integration.

- [x] Added the complete typed Phase-2 `EpisodeManifest` audit boundary from SDS section 16.2 in local commit `a8858d5`. `build_episode_manifest()` requires chart/snapshot/compiler/result closure, content-addresses the bounded complete supplied program and exact stamp map, records pinned kernel/controller identities, deterministic seed, explicit resource budget, timezone-aware start/finish times, return code, and captured stdout/stderr, and requires every compiled Sentence exactly once. Create-once checksummed persistence rejects envelope and typed manifest-digest drift. Focused 46 tests and full 487 tests passed; `py_compile` and `git diff --check` passed. This records a caller-supplied completed run only: no kernel invocation, rule/trace decoding, promotion, write, or live integration.

- [x] Closed the immutable snapshot-to-compiler packet-content provenance gap. Evidence snapshot v2 now stores one canonical digest per complete frozen packet and derives the snapshot fingerprint from the ordered digest set plus context/assumption/ontology identity; `compile_episode_inputs()` recomputes and checks each selected packet digest before projection. Tests prove statement, count, reliability, and origin drift under the same packet/snapshot IDs fail closed, and a recomputed outer document checksum cannot conceal digest/fingerprint inconsistency. Local implementation commit `ab7a50c`; focused 39 tests and full 480 tests passed; `py_compile` and `git diff --check` passed. No runtime, derive/query, memory write/promotion, PeTTaChainer `compileadd`, patham9 source change, or live OmegaClaw/GoalChainer integration.

- [x] Hardened typed Phase-1 `PiChart` identity before episode compilation. Chart construction now rejects empty, blank, or duplicate packet selections and hashes the complete immutable selection plus kernel-projection policy and adequacy-certificate identity, preventing unequal charts from sharing a cache/replay fingerprint. Local implementation commit `67e6ee9`; focused 31 tests and full 472 tests passed; `git diff --check` passed. No runtime derive, memory write/promotion, PeTTaChainer `compileadd`, patham9 source change, or live OmegaClaw/GoalChainer path.

- [x] Added immutable on-disk persistence for Phase-1 piPLN `EvidenceSnapshot` records. `write_evidence_snapshot()` uses create-exclusive mode and fsync, never replaces an existing snapshot, and writes a canonical checksummed v1 JSON envelope; `read_evidence_snapshot()` fails closed on schema, checksum, payload-shape, or typed-record drift. Implementation commit `463310b`. Focused 22 tests and full 462 tests passed; `git diff --check` passed. No runtime derive, memory write/promotion, or live OmegaClaw/GoalChainer path.

- [x] Current progress slice hardened the read-only `live-goal-bridge --run-patham9-runtime` program-count provenance boundary. When a patham9/PLN runtime result includes program `handoff_sentence_count` or `sentence_count`, the bridge now rejects boolean/non-integer/negative counts, rejects handoff sentence counts that do not match the already admitted handoff item count, and rejects total sentence counts smaller than the admitted handoff before any GoalChainer appraisal. Verification: local implementation commit `8e79e1c`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge --run-patham9-runtime` semantic-marker audit boundary. The bridge now rejects patham9 runtime semantic marker counts that are boolean, non-integer, negative, missing for pass/fail counts, or semantically inconsistent (`passed_true_count <= 0`, nonzero false/error markers) before GoalChainer appraisal. Verification: local implementation commit `d75c466`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe/check consistency boundary. The bridge now rejects copied GoalChainer `checks.no_task_or_directive_claim` when present but not `True`, and rejects malformed optional `heuristic_memory_probe.parsed_memory_items` counts (bool/non-int/non-positive) before emitting output. Verification: local implementation commit `9f8d311`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer copied-sidecar boundary against nested directive/task-claim fields. The bridge now recursively rejects directive-shaped keys (`claim`, `task_claim`, `directive_claim`, `directive_report`, `plan`, `task_states`, `next`, `skill`) anywhere inside copied GoalChainer result/decision payload/checks/probe/decision/evidence/contextual-evidence containers before emitting output, so nested metadata cannot smuggle directive/task-claim artifacts through audit sidecars. Verification: local implementation commit `ca220ce`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.


- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer nested decision-evidence directive/task-claim sidecar boundary. The bridge already rejected directive/task-claim-shaped fields at the top-level GoalChainer result, decision payload, checks block, heuristic probe, and individual decisions; it now also rejects those fields inside copied `decision.evidence` objects and each `evidence.contextual_evidence` entry before emitting output. Verification: local implementation commit `84dc0c9`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe sidecar boundary. The bridge already rejected directive/task-claim-shaped fields at the top-level GoalChainer result, decision payload, checks block, and individual decisions; it now also rejects those fields inside the copied `heuristic_memory_probe` sidecar before emitting output. Verification: local implementation commit `9ca7ed0`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer checks sidecar boundary. The bridge already rejected directive/task-claim sidecars at the top-level GoalChainer result, `decision_payload`, and individual decision records; it now also rejects the same directive-shaped fields inside the copied `checks` block before emitting output. Verification: local implementation commit `9f3d241`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer per-decision directive/task-claim sidecar boundary. The bridge already rejected directive-looking fields at the GoalChainer result and decision-payload levels; it now also rejects those fields inside individual decision records before emitting output, so a downstream adapter cannot smuggle directive reports through a recommended/candidate decision sidecar. Verification: local implementation commit `0ee7260`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 25 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 438 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer directive/task-claim sidecar boundary. The bridge now rejects top-level GoalChainer result and decision-payload fields that look like directive/task-claim artifacts (`claim`, `task_claim`, `directive_claim`, `directive_report`, `plan`, `task_states`, `next`, `skill`) before emitting output. Verification: local implementation commit `7b96891`; focused live-bridge tests pass 25 cases; full unittest discovery passes 438 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe check boundary. When `include_heuristic_memory_probe=True`, the bridge now requires downstream GoalChainer `checks.heuristic_with_memory_path_checked is True` in addition to the validated `heuristic_memory_probe` sidecar before emitting output, and records `checks.heuristic_memory_probe_checked` in the bridge artifact. Verification: local implementation commit `07e29bc`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 24 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 437 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe request boundary. When `include_heuristic_memory_probe=True`, the bridge now rejects downstream GoalChainer output that omits the requested probe sidecar before emitting an OmegaClaw-facing bridge artifact, while preserving earlier fail-closed errors for malformed decisions/notes/evidence. Verification: local implementation commit `c2c09af`; focused live-bridge tests pass 23 cases; full unittest discovery passes 436 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket finite-number boundary. The bridge now rejects NaN/Infinity in contextual `support`/`opposition` EC counts and optional `derived_strength`/`derived_confidence` truth values before emitting an OmegaClaw-facing bridge artifact. Verification: local implementation commit `3d8aa4a`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket truth/provenance boundary. The bridge now rejects contextual-evidence entries with malformed optional `derived_strength`/`derived_confidence` truth values and requires non-empty `belief_id`, `cluster_id`, and `promotion_event` provenance before emitting an OmegaClaw-facing bridge artifact. Verification: local implementation commit `4bda953`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket EC-count boundary. The bridge now rejects contextual-evidence entries with missing, boolean, non-numeric, or negative `support`/`opposition` counts before emitting an OmegaClaw-facing bridge artifact. Verification: local implementation commit `183b586`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision-notes boundary. The bridge now rejects non-string or empty entries in `decision_payload.notes`, after already requiring the notes container to be a list, so malformed note sidecars cannot cross into OmegaClaw-facing bridge artifacts. Verification: local implementation commit `59186ef`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer contextual-evidence audit boundary. The bridge now rejects decision `evidence.contextual_evidence` sidecars that are not lists, and rejects contextual-evidence entries that are not objects, before emitting bridge output. Verification: local implementation commit `477ce0a`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision evidence proof-entry boundary. The bridge now rejects decision `evidence.proofs` lists containing non-string or empty-string proof entries, so malformed proof sidecars cannot cross into the OmegaClaw-facing bridge artifact even after the evidence/proofs container shape is valid. Verification: local implementation commit `6eed79a`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision-evidence boundary for actionless decisions. The bridge now validates optional `evidence` sidecars on every decision record before any no-`action_id` candidate/held path can continue, so malformed proof/provenance sidecars cannot bypass validation. Verification: local implementation commit `39c52f5`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision-evidence boundary. The bridge now rejects non-object decision `evidence` sidecars and non-list `evidence.proofs` before emitting read-only bridge output, preventing malformed proof/provenance drift from crossing into the OmegaClaw-facing artifact. Verification: local implementation commit `adf97f6`; focused live-bridge tests pass 22 cases; full unittest discovery passes 435 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe boundary. The bridge now rejects malformed `heuristic_memory_probe` sidecars and requires non-empty probe `schema`/`mode`/`boundary`, `memory_proof_present is True`, and `leak_check_safe is True` before emitting bridge output. Verification: local implementation commit `5d3a9cc`; focused live-bridge tests pass 21 cases; full unittest discovery passes 434 tests; `git diff --check` passes. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer decision action-id boundary. The bridge now rejects malformed non-empty/non-string `action_id` values on any decision record and rejects duplicate decision `action_id` values before emitting a bridge artifact, preventing ambiguous recommended/candidate drift for the same action. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 19 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 432 tests; `git diff --check` passed; local implementation commit `9559372` (not pushed). Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer recommendation boundary. The bridge now fails closed when a downstream GoalChainer runner returns multiple `status: recommended` decisions, rather than silently selecting the first one. Regression coverage proves duplicate recommendations raise `ValidationError`; focused live-bridge tests 19 passed; full unittest suite 432 passed; `git diff --check` passed; local implementation commit `7daf7c3` (not pushed). No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer boundary-check contract. The bridge now fails closed unless the downstream GoalChainer `checks` explicitly assert `no_memory_write is True` and `no_live_directive_or_task_claim is True`, preventing incomplete/malformed adapters from being rewrapped as safe top-level bridge output. Verification: focused live-bridge tests 18 passed; full unittest suite 431 passed; `git diff --check` passed; local implementation commit `11e98c8` (not pushed). No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Replaced synthetic fixture evidence in the archived Protomegabot GoalChainer sidecar replay with a real bounded petta-memory export. Gate `projects/omegaclaw/artifacts/ggb-capacity-gates/20260709-goalchainer-real-petta-memory-replay/` loads an immutable promoted-belief journal with `MediumMemoryStore`, calls the production `goalchainer_handoff_cache()` exporter, allowlists the archived promoted belief and selects its two STV/EC items under a four-item cap with cluster/promotion provenance, then calls local deterministic `solve_incident(memory_items=...)` for one archived Protomegabot decision candidate. Harness 9/9 passed; focused petta-memory 53 tests, focused GoalChainer 52 tests, and full petta-memory 430 tests passed. Journal hash unchanged. No Telegram/provider/supervisor, live bridge, memory write/promotion, secret, paid compute, or push.

- [ ] Future GoalChainer/AtomSpace phase (not implemented): semantically parse selected relevant task text into logical expressions with an explicitly bounded LLM stage, populate only reviewed expressions into AtomSpace, and add ECAN-like attention allocation plus long-term-importance/staleness-based retention/removal. Keep provider use, writes, and live integration separately approval-gated.

- [x] Hardened the read-only `live-goal-bridge` GoalChainer output boundary against malformed notes and recommended-decision drift. The bridge now requires `decision_payload.notes` to be a list when present and rejects any `status: recommended` decision without a non-empty string `action_id` before emitting live-bridge output. Regression coverage proves both malformed shapes raise `ValidationError`. Verification: focused live-bridge tests 17 passed; full unittest suite 430 passed; `git diff --check` passed; local implementation commit `4d6b1f4` (not pushed). No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge --run-patham9-runtime` top-level patham9 audit boundary. A runtime result with `status: passed` must now also provide a non-empty string result `schema` and exact integer `returncode: 0` (bool/string/nonzero returncodes fail closed) before GoalChainer appraisal. Regression coverage proves malformed schema and string/bool/nonzero returncodes abort before GoalChainer is called. Verification: focused live-bridge tests 15 passed; full unittest suite 428 passed; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened the read-only `live-goal-bridge --run-patham9-runtime` audit boundary against malformed patham9 result sidecars. A runtime result with `status: passed` must now still include object-shaped `semantic_markers`, `semantic_passed: true`, object-shaped `program`, and a non-empty string program schema before GoalChainer appraisal. Regression coverage proves malformed semantic markers, semantic-false markers, malformed program artifacts, and empty program schema all fail closed before GoalChainer is called. Verification: focused live-bridge tests 14 passed; full unittest suite 427 passed; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Fixed the ThreadKeeper project-control GoalChainer scenario to avoid forcing canary-only evidence behind a default PR-reconciliation action. `_project_control_scenario()` now includes the `reconcile_threadkeeper_pr` goal/action/obligation only when PR-reconciliation evidence is present; canary-only admitted patham9 evidence recommends `install_threadkeeper_canary_on_protomegabot` directly. Verification: focused GoalChainer smoke tests 8 passed; full unittest suite 426 passed; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Wired patham9-admitted ThreadKeeper evidence back into GoalChainer appraisal. The live bridge passes the admitted pi-PLN handoff into the precompiled GoalChainer gate, and the gate uses the ThreadKeeper project-control evidence to recommend `reconcile_threadkeeper_pr` as the immediate action, retain `install_threadkeeper_canary_on_protomegabot` as the next candidate/admissible action, and block redundant `ask_ben_again` / premature `remove_threadkeeper`. Runtime artifact: `repos/petta-memory/artifacts/live_goal_bridge_threadkeeper_feedback_20260709T135138Z/result.json` sha256 `40987bab24fa59414949bda89aa532280b4bcbacc64baacbb758535a54fb8749`. Verification: focused live-bridge tests 13 passed; full unittest suite 425 passed; `py_compile` and `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, or OmegaClaw skill/task claim.

- [x] Added a ThreadKeeper canary/project-control fixture and live-bridge regression proving the ranked/admitted pi-PLN gate admits only the query-relevant `Acceptable install_threadkeeper_canary_on_protomegabot` branch before GoalChainer appraisal, while preserving all promoted evidence in the GoalChainer handoff cache. Focused live-bridge tests passed 12 cases; full unittest discovery passed 424 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened `live-goal-bridge` against malformed GoalChainer scalar metadata. The bridge now rejects missing/non-string/empty `schema`, `mode`, and `boundary` fields from the GoalChainer gate with explicit `ValidationError` before emitting read-only live-bridge output. Verification: focused live-bridge tests passed 11 cases; full unittest suite passed 423 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened `live-goal-bridge` against malformed GoalChainer decision-list drift. The bridge now rejects non-list `decision_payload.decisions` and non-object decision entries with explicit `ValidationError` before selecting a recommended action or emitting live-bridge output. Verification: focused live-bridge tests passed 10 cases; full unittest suite passed 422 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened `live-goal-bridge` against malformed GoalChainer gate output after appraisal. The bridge now rejects non-object GoalChainer runner results, non-object `decision_payload`, and non-object `checks` with explicit `ValidationError` before emitting live-bridge output. Verification: focused live-bridge tests passed 8 cases; full unittest suite passed 420 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened `live-goal-bridge --run-patham9-runtime` against malformed patham9 runtime runner output before GoalChainer appraisal. The bridge now rejects non-object runtime results with `ValidationError`, and regression coverage verifies an injected GoalChainer runner is not called after malformed patham9 output. Verification: focused live-bridge tests passed 5 cases; full unittest suite passed 417 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, patham9/PLN source change, or OmegaClaw skill/task claim.

- [x] Hardened `live-goal-bridge --run-patham9-runtime` to fail closed before GoalChainer appraisal if the optional patham9/PLN runtime gate does not pass. Added `goalchainer_runner` test injection and a regression proving GoalChainer is not invoked after a failed patham9 gate. Verification: focused live-bridge tests, full unittest suite passed 416 tests, and `git diff --check` passed. No PeTTaChainer `compileadd`, memory write, inferred-belief promotion, or OmegaClaw skill/task claim.

- [x] Wired the read-only live bridge to optionally run the local patham9/PLN runtime over the admitted pi-PLN handoff, bypassing PeTTaChainer `compileadd` for the runtime proof step. `live-goal-bridge --run-patham9-runtime` now composes journal -> ranked/admitted handoff -> bounded patham9 multi-sentence derivation smoke -> GoalChainer appraisal. Runtime artifact: `repos/petta-memory/artifacts/live_goal_bridge_patham9_runtime_2026-07-08T1813Z.json` (sha256 `7777b0269807d12c218bd135dcaa401cafae718df6df7649f63f76cc6dfc3eb5`), journal artifact sha256 `c3b0c603d0a8c90a59200daff8cc608d53ce588f6fc8d45466eefbf1685d3f5d`. Result: patham9 semantic `Passed: true`, returncode 0, GoalChainer recommended `publish_redacted_summary`; no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no OmegaClaw skill/task claim. Verification: `py_compile`, full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 415 tests, and `git diff --check` passed.

- [x] Added the first read-only live bridge from a `MediumMemoryStore` journal into local GoalChainer. New `live-goal-bridge` CLI composes journal -> promoted PeTTa/GoalChainer handoff -> pi-PLN ranked/admitted gate -> GoalChainer precompiled appraisal + heuristic memory probe, while preserving no OmegaClaw skill/no directive task claim/no memory write/no inferred-belief promotion boundaries. Runtime artifact: `repos/petta-memory/artifacts/live_goal_bridge_2026-07-08T1830Z.json`; result recommended `publish_redacted_summary` with 2 GoalChainer evidence inputs, 1 patham9 item, 1 ranked/admitted branch. Verification: `python3 -m py_compile src/petta_memory/live_bridge.py src/petta_memory/cli.py`; `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 414 tests; `git diff --check` passed.

- [x] Hardened the non-live ranked/admitted inference-control gates against boolean/non-integer audit metadata drift. `ranked_inference_control_plan()` now rejects bool/non-integer source `item_count` before estimator/controller dispatch. `ranked_plan_admitted_handoff()` now rejects bool/non-integer top-level counts (`input_count`, `recommended_count`, `held_count`, `candidate_count`) and bool rank/item-index keys before branch-plan mirror checks or admitted premise copying. Focused ranked-plan tests pass 40 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 412 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the ranked inference-control plan gate against non-object source handoff items. `ranked_inference_control_plan()` now validates every source `items` entry is an object before invoking estimator/controller wrappers, preserving audit-friendly `ValueError` failures instead of lower-level wrapper/container errors for malformed reviewed handoff artifacts. Focused ranked-plan tests pass 37 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 409 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against source handoff `item_count` drift. `ranked_plan_admitted_handoff()` now requires any present source handoff `item_count` to match the actual `items` list length before comparing ranked-plan mirrors or copying admitted premises, preventing a reviewed plan from being replayed against a handoff whose metadata no longer matches its payload. Focused ranked-plan tests pass 36 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 408 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the ranked inference-control plan gate against malformed source handoff containers/counts. `ranked_inference_control_plan()` now requires source handoff `items` to be a list and rejects `item_count` drift before invoking estimator/controller wrappers or building the reviewed branch plan. This keeps the pre-derive branch-plan artifact internally tied to the exact source handoff that will later feed admitted-handoff review. Focused ranked-plan tests pass 35 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 407 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against non-object source handoff items. `ranked_plan_admitted_handoff()` now validates that every source handoff item referenced by the audited `branch_plan` is an object before comparing `belief_id`/`term` or copying admitted premises, preserving audit-friendly `ValueError` failures instead of Python attribute errors when a reviewed handoff artifact contains list/scalar item records. Focused ranked-plan tests pass 33 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 405 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against non-object branch-record drift. `ranked_plan_admitted_handoff()` now rejects malformed entries inside `recommended_branches`, `held_branches`, and `branch_plan` before field access, preserving audit-friendly `ValueError` failures instead of container attribute errors when a reviewed plan artifact has list/scalar records. Focused ranked-plan tests pass 32 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 404 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against malformed container-type drift. `ranked_plan_admitted_handoff()` now explicitly rejects non-list source handoff `items` and non-list ranked-plan partitions (`recommended_branches`, `held_branches`, `branch_plan`) before iterating or validating count/mirror fields. This preserves audit-friendly `ValueError` failures instead of Python container/attribute errors when a reviewed plan artifact is malformed. Focused ranked-plan tests pass 31 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 403 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against ranked-plan rank-gap/order drift. `ranked_plan_admitted_handoff()` now requires audited `branch_plan` ranks to be contiguous `1..candidate_count` before any recommended premise is copied, preventing a malformed reviewed plan from preserving unique ranks while shifting admission order/gaps. Focused ranked-plan tests pass 29 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 401 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against full branch-plan item-index duplication. `ranked_plan_admitted_handoff()` now rejects duplicate source handoff item indexes while scanning the audited `branch_plan`, including malformed recommended/held partition drift where the same item appears under different ranks/statuses before any premise is copied. Focused ranked-plan tests pass 28 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 400 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against duplicate rank/key drift across the audited plan and held partition. `ranked_plan_admitted_handoff()` now rejects duplicate `branch_plan` ranks even when item indexes differ, and rejects duplicate held-branch ranks/items before copying any admitted premises. Focused ranked-plan tests pass 27 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 399 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against ranked-plan audit-field drift. `ranked_plan_admitted_handoff()` now requires recommended and held branch records to mirror the audited `branch_plan` not only by rank/item/source identity/status but also by estimator probability, mean viability, query relevance, controller decision/checks, hold reasons, and deferred-branch metadata before any recommended premise is copied. Focused ranked-plan tests: 25 passed; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 397 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against stale source-handoff drift across the full audited branch plan. `ranked_plan_admitted_handoff()` now rejects `input_count` mismatches, rejects `branch_plan` records whose `item_index` points outside the source handoff, and verifies every branch-plan `belief_id`/`term` against the current handoff item before any recommended premise is copied into the admitted handoff subset. Focused ranked-plan tests: 23 passed; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 395 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against held-branch partition/mirror drift. `ranked_plan_admitted_handoff()` now rejects `held_branches` entries that no longer have `status: "held"` and requires held branches to mirror the audited `branch_plan` by rank, item index, belief id, term, and status before producing the admitted handoff subset. Focused ranked-plan tests: 20 passed; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 392 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against malformed `branch_plan` records outside the reviewed recommended/held partition. `ranked_plan_admitted_handoff()` now rejects `branch_plan` entries with non-`recommended`/`held` statuses plus malformed rank/item-index key fields, closing an audit gap where an extra `deferred` branch could be hidden in `branch_plan` while counts still matched. Focused ranked-plan tests: 18 passed; full unittest suite: 390 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against malformed branch-plan totals and partition drift. `ranked_plan_admitted_handoff()` now rejects `candidate_count`/`branch_plan` length mismatches, duplicate branch-plan `(rank, item_index)` keys, and branch-plan recommended/held status counts that do not mirror the reviewed recommended/held lists before a future derive gate can copy premises. Focused ranked-plan tests: 16 passed; full unittest suite: 388 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against malformed ranked-plan count and branch-plan mirror drift. `ranked_plan_admitted_handoff()` rejects plans whose `recommended_count`/`held_count` disagree with their branch lists and rejects recommendations that are not mirrored consistently in `branch_plan`, preventing spliced/ad hoc recommendations from bypassing the auditable full branch plan. Focused ranked-plan tests: 13 passed; full unittest suite: 385 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against malformed recommended-list status. `ranked_plan_admitted_handoff()` now rejects any branch found under `recommended_branches` whose `status` is not still `recommended`, preventing copied/edited held branches from being admitted into a future reviewed derive handoff even if id/term/index still match. Focused ranked-plan tests: 11 passed; full unittest suite: 383 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against duplicated ranked-plan recommendations. `ranked_plan_admitted_handoff()` now rejects duplicate ranks and duplicate handoff item indexes before copying admitted items, preventing a malformed/replayed plan from feeding repeated premises into a later reviewed derive gate. Focused ranked-plan tests: 10 passed; full unittest suite: 382 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Hardened the admitted-handoff pre-derive gate against stale term reuse. `ranked_plan_admitted_handoff()` already rejected recommended branches whose item-index/belief-id no longer matched the handoff; it now also rejects same-belief-id/different-term mismatches and records the admitted term in `admission_records` for audit. Focused ranked-plan tests: 9 passed; full unittest suite: 381 passed; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Exposed the admitted-handoff subset as a non-live CLI gate. New command `pi-pln-admitted-handoff` composes the existing store handoff, `ranked_inference_control_plan()`, and `ranked_plan_admitted_handoff()` to emit only recommended branches in the existing `petta-memory-patham9-pln-handoff-v1` shape for a later separately reviewed derive gate. README documents the operator path; CLI regression verifies append-only store -> ranked plan -> admitted subset recommends/adopts `b1` while preserving the no-runtime/no-derive boundary. Checks: focused CLI/ranked-plan tests 16 passed; full unittest suite 380 passed; `git diff --check` passed. No SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append beyond temp test stores, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Added a non-live admitted-handoff subset gate after ranked inference control. `ranked_plan_admitted_handoff()` validates the original handoff and ranked plan, copies only recommended branches in rank order into an embedded `petta-memory-patham9-pln-handoff-v1` handoff, rejects stale item-index/belief-id mismatches, and is compatible with the existing multi-Sentence derivation program builder while preserving the no-runtime/no-derive boundary. Checks: focused ranked-plan tests 8 passed; full unittest suite 380 passed; `git diff --check` passed. No SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Exposed the non-live ranked inference-control plan as a reviewed CLI gate. New command `pi-pln-ranked-plan` builds `ranked_inference_control_plan()` from the store handoff with estimator/controller thresholds, query relevance gating, reproducible seed, and branch caps; README documents it as a pre-`PLN.Derive` plan artifact. Added CLI round-trip coverage from append-only store -> patham9 handoff -> ranked plan, recommending `b1` while preserving the no-runtime/no-derive boundary. Checks: focused CLI/ranked-plan tests 13 passed; full unittest suite 377 passed; `git diff --check` passed. No SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append beyond temp test stores, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.

- [x] Extended the non-live GoalChainer handoff smoke to test the actual heuristic-with-memory path. `run_goalchainer_precompiled_handoff_smoke(..., include_heuristic_memory_probe=True)` now parses handoff cache items with GoalChainer `parse_memory_evidence()` and calls `solve_incident(memory_items=...)` under the existing local PeTTa/SWI environment while preserving the non-live boundary (no OmegaClaw skill, accepted directive/task claim, memory write, or live Telegram/runtime bridge). CLI flag: `goalchainer-smoke --heuristic-memory-probe`. Runtime artifact: `repos/petta-memory/artifacts/goalchainer_heuristic_memory_probe_2026-07-07T0334Z.json` sha256 `3e55ca9531ef93ecd4e2f5b8375d318aa53b1cf21d4e02f6ae92724b3bdeaa2f`; result `decided=publish_redacted_summary`, `memory_proof_present=True`, `leak_check_safe=True`. Checks: focused GoalChainer smoke tests 7 passed, full unittest suite 377 passed, `git diff --check` passed. Gate archived under `projects/omegaclaw/artifacts/ggb-capacity-gates/20260706-petta-memory-goalchainer-heuristic-probe/`.

- [x] Added a non-live ranked inference-control plan gate. `ranked_inference_control_plan()` composes `pln_estimator_wrapper()` EDCall ranking with `continuation_predicate_wrapper()` controller checks before any future live `PLN.Derive` call. The returned artifact separates recommended and held branches and records estimator probability, mean viability, query relevance, controller decision/checks, and hold reasons. Tests: 5 new `RankedInferenceControlPlanTests` plus 1 unified store -> handoff integration gate. Verification: 376 tests pass; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no OmegaClaw/GoalChainer live path.
- [x] Added local commit `a448fe6` with unified inference-control integration test. `StoreRoundTripUnifiedInferenceControlTests` in `repos/petta-memory` exercises all eight inference-control patterns from the trueagi-io/chaining survey against a single realistic 4-belief store fixture with diverse domains (memory-architecture, reasoning, planning), STVs (0.92/0.80 through 0.45/0.30), and EC counts (including conflicting 2/8 evidence). The fixture flows through the full pipeline: store -> pettachainer_handoff_cache -> patham9_pln_handoff_sentences -> each inference-control wrapper. 10 new tests validate handoff diversity, per-pattern correctness on the richer input, and provenance preservation across all patterns. Verification: 370 tests pass; `git diff --check` passes.
- [x] Created author-facing ASCII LaTeX + PDF PeTTaChainer codebase assessment documenting strengths, weaknesses, materializer/compileadd blocker, and repair recommendations. Files: `docs/pettachainer_codebase_assessment.tex` (ASCII) and `docs/pettachainer_codebase_assessment.pdf`; PDF compiled with `tectonic`; sha256 tex `7a79413ab2014786e34b7b9d7760cb513525994283ce918858899f79a654f663`, pdf `6501afae396ec3e0783156d6b19891b02a683bbc2233267ed93ec39767b6ca01`.
- [x] Reproduced the Smokes stock patham9 example at pinned commit `55f1751` with a fully local MeTTaMorph→Chicken→PLN toolchain. Built Chicken Scheme 5.4.0 from source (no root), installed eggs (matchable, srfi-69, amb), compiled `SMOKES.so`, and ran `metta Smokes.metta` with `LD_LIBRARY_PATH` set. Result: `Passed: #t` with derived truth value `(stv 0.519920454545454 0.829078220412911)` for `(cancerous Edward)`. Two consecutive runs produced byte-identical output (SHA-256 `fd5a6133deca5c88f6170be634bc0f5101259ba3f685abb9c6fec5babc1f893e`, 6021 bytes). Reference artifact: `artifacts/phase0-reference-smokes-55f1751/reference_manifest.json`. Remaining examples (FlyingRaven, Robot, Toothbrush) not yet reproduced under this toolchain.
- [x] Map `patham9/PLN` API surface: `PLN.Derive`, `PLN.Query`, `Sentence`, `stv`, evidence stamps, `StampDisjoint`, priority/belief queues. Identify extension points for π-PLN semantics (EvidencePacket, EC counts, context selection, provenance lineage, STV projection). Source-level `patham9_pln_api_surface(...)` helper + CLI `patham9-pln-api-surface` maps all core API entries (4 PLN.Derive signatures, 4 PLN.Query signatures, Sentence structure, StampDisjoint, PriorityRank, ConfidenceRank, LimitSize, BestCandidate), 16 truth-value formulas, 17 inference rules, 5 guard predicates, 3 config defaults, 14 utility helpers, 4 translator definitions, and the Python PLN.Init entrypoint. pi-PLN extension points identified at wrapper boundary (sentence construction, stamp assignment, STV pre-projection, context selection, queue priority, provenance lineage) and internal extension boundary (context-indexed evidence, EC-aware formulas, inference control, custom link types) with revisit trigger. Artifact: `artifacts/patham9_pln_api_surface_2026-07-05T2000Z.json` sha256 `58896b1045cc7893ebd090736c1d6355bd7b8446526fb2ed3ae326b6f2c2dced`. No SWI/PeTTa/MeTTa runtime invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 144 tests; `git diff --check` passes.
- [x] Design the π-PLN extension layer: wrap or extend `patham9/PLN` with contextual evidence packets, EC-aware truth-value formulas, and provenance-bearing proof traces. Decide wrapper-vs-internal boundary. Implemented `patham9_pi_pln_extension_spec()` as a concrete design spec covering sentence construction protocol, EC projection formula (confidence-weighted blend, already tested), provenance sidecar policy, context selection policy (not-live), inference control hooks (deferred, referencing trueagi-io/chaining patterns), read/write boundaries, and revisit triggers. Also added `patham9_pln_multi_sentence_derivation_smoke_program()` and `run_patham9_pln_multi_sentence_derivation_smoke()` to validate the wrapper boundary with multiple handoff Sentences plus a synthetic bridge implication. CLI: `patham9-pi-pln-spec` and `patham9-pln-multi-derivation-smoke`. Local commit `0ee27d1`. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 163 tests; `git diff --check` passes.
- [x] Connect `petta-memory` handoff cache exports (promoted STV statements + EvidencePackets) as input to the `patham9/PLN` + π-PLN chainer. Validate end-to-end on a tiny example. Local commit `534a3b9` fixed a sentence-separator bug (comma vs whitespace) in the multi-Sentence derivation smoke program builder and passed the first end-to-end gate: 3 promoted handoff Sentences (stamps 0-2) plus 1 synthetic bridge implication (stamp 3) successfully derive `(PMDerivedFromMultiHandoff (Requires MemoryTarget0 PLNReadyViews))` with result `((stv 0.706 0.495) (0 3))`. Runtime artifact: `artifacts/patham9_pln_multi_sentence_derivation_smoke_2026-07-05T2000Z.json` sha256 `ebbfd2cf9c0eb27e5cf89ae919ba4091ed27c5e934f087fcd77af0a8c8f454f3`. No memory append, inferred-belief promotion, patham9 source patch, OmegaClaw/GoalChainer live path invoked. Verification: 163 tests pass; `git diff --check` passes.
- [x] Add empirical round-trip tests from MediumMemoryStore through the full patham9/PLN pipeline. Local commit `42ad841` adds `StoreRoundTripPatham9PlnTests` with 5 tests that exercise the full artifact pipeline from stored promoted beliefs (not synthetic handoff items) to a patham9/PLN multi-Sentence derivation program: store -> `pettachainer_handoff_cache()` -> `patham9_pln_handoff_sentences()` -> `patham9_pln_multi_sentence_derivation_smoke_program()`. Validates STV, PMEvidence provenance, contextual EvidencePackets, stamp sidecar, boundary text, and EC projection formula compatibility without invoking SWI/PeTTa runtime. Verification: 168 tests pass; `git diff --check` passes.
- [x] Survey trueagi-io/chaining inference-control patterns for pi-PLN wrapper. Local commit `cd18b51` adds `survey_trueagi_chaining_inference_control()` and CLI `trueagi-inf-ctl-survey` that maps six concrete inference-control patterns from the checked-out trueagi-io/chaining repo (commit `bc9beb2`) to pi-PLN wrapper extension points: (1) PLN-based inference controller with Thompson sampling, (2) controlled backward chainer with context updaters and termination predicate, (3) meta-learning inference control benchmark, (4) controller-as-chainer (termination via another backward chainer), (5) continuation predicate (opt-in branch justification), (6) probabilistic backward chaining (ProbLog-inspired). All six patterns can be adopted at the wrapper boundary without modifying patham9/PLN source. Patterns categorized by adoption complexity: near-term (probabilistic filtering, meta-learning benchmark), medium-term (controlled chainer, continuation predicate), long-term (PLN estimator, controller-as-chainer). Tests: 8 new tests in `TrueagiChainingInferenceControlSurveyTests`. Verification: 176 tests pass; `git diff --check` passes.
- [x] Implement first inference-control mechanism: probabilistic filtering wrapper. `probabilistic_inference_filter()` in `patham9_pln.py` implements the near-term "probabilistic filtering" pattern from the survey. Takes a `petta-memory-patham9-pln-handoff-v1` handoff, applies EC projection to each Sentence, computes `composite_score = projected_strength * projected_confidence`, filters by `min_confidence` and/or `top_k`. CLI: `pi-pln-inference-filter`. Tests: 16 new tests (15 in `ProbabilisticInferenceFilterTests` + 1 in `StoreRoundTripInferenceFilterTests`). Verification: 192 tests pass; `git diff --check` passes.
- [x] Implement second inference-control mechanism: context-selection wrapper. `context_selection_wrapper()` in `patham9_pln.py` implements the near-term "context selection" pattern from the survey. Filters EvidencePackets by domain, cluster_id, or promotion_rule, and scores each remaining packet by evidence-weighted relevance: `evidence_weight = (support + opposition) / (support + opposition + 2)`. Packets below `min_packet_relevance` threshold are filtered out. Items with no packets pass through unchanged. CLI: `pi-pln-context-select`. Tests: 16 new tests (15 in `ContextSelectionWrapperTests` + 1 in `StoreRoundTripContextSelectionTests`). Verification: 208 tests pass; `git diff --check` passes.
- [x] PeTTaChainer materialize instrumentation track (paused — see `## Waiting or blocked` below). Last gate `cda5cbe` narrowed the blocker to adjacent arity-two nested sibling payloads in a four-field wrapper. 116 tests pass.
- [x] Added local commit `349f60d` with the first non-live wrapper-level EC projection formula gate for patham9/pi-PLN. New helpers `ec_projected_stv(...)`, `patham9_pln_ec_projection_smoke_program(...)`, `run_patham9_pln_ec_projection_smoke(...)`, and CLI `patham9-pln-ec-projection-smoke` compare direct STV versus projected STV query smokes. The formula blends base STV with EC-derived evidence using confidence-weighted averaging: `projected_strength = sum(s_i * w_i) / sum(w_i)` where weights are confidences, and `projected_confidence = max(all confidences)`. Runtime artifact `artifacts/patham9_pln_ec_projection_smoke_2026-07-05T1600Z.json` sha256 `f6802b2b661273ec1fd09c4970142b54d660e63d56d99e92abcf218a6f67f23e` passed both direct (`(stv 0.91 0.74)`) and projected (`(stv 0.904703 0.833333)`) query smokes for `(Acceptable publish_redacted_summary)` with EC `(9 1)` support. No memory append, inferred-belief promotion, patham9 source patch, OmegaClaw/GoalChainer live path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 135 tests; `git diff --check` passes.

- [x] Added local commit `cda5cbe` with a bounded non-live PeTTaChainer four-field adjacent-nested arity gate after the right-payload arity/head gate. New helpers `materialize_four_field_adjacent_nested_arity_rungs(...)` and `run_materialize_four_field_adjacent_nested_arity_gate(...)` keep a generic `PayloadA`, fix the right sibling at generic two-argument `(RightPayload 1.0 1.0)` before STV controls, and grow the nested Type from zero to one to two arguments. Artifact: `artifacts/pettachainer_materialize_four_field_adjacent_nested_arity_gate_2026-07-05T0400Z.json` (sha256 `26041a112cd12fef42f79cfed34700502bbaf16525b49cbd71743f35f47d3b8a`) shows zero- and one-argument nested Types pass in ~0.43s, while the two-argument nested Type beside generic two-argument right payload times out at 4s. This narrows the materializer blocker to adjacent arity-two nested sibling payloads in a four-field wrapper, not STV head or one-sided right payload arity alone. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 116 tests; `git diff --check` passes.
- [x] Added local commit `ad7fffa` with a bounded non-live PeTTaChainer four-field right-payload arity/head materialize gate after the neighbor-shape gate. New helpers `materialize_four_field_right_payload_arity_rungs(...)` and `run_materialize_four_field_right_payload_arity_gate(...)` keep generic left `PayloadA` plus all-sentinel nested Type fixed while increasing the right nested payload arity before STV-head controls. Artifact: `artifacts/pettachainer_materialize_four_field_right_payload_arity_gate_2026-07-05T0200Z.json` (sha256 `5c0c35948008aba32eaf95754ca8a92b4b10761de6518a3ca4515317dbc19728`) shows atom/zero-arg/one-arg right payloads pass, while `(RightPayload 1.0 1.0)` times out at 4s. This narrows the materializer blocker to generic arity-two right nested payload beside a two-argument nested Type, not specifically the STV head. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 114 tests; `git diff --check` passes.
- [x] Added local commit `82c2cd9` adds a bounded non-live PeTTaChainer four-field neighbor-shape materialize gate in `repos/petta-memory`: `materialize_four_field_neighbor_shape_rungs(...)` and `run_materialize_four_field_neighbor_shape_gate(...)` keep the all-sentinel two-argument nested Type in the second payload slot while adding the left proof id and right truth-value/STV-like payload stepwise. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_four_field_neighbor_shape_gate_2026-07-05T0000Z.json` sha256 `b4aa2b5f3ebe512d258a49352b2cc0a493868c6dd606ba5cc10477c2b88fa9e0` shows generic payload siblings and proof-id + payload pass in ~0.47-0.49s, but `PayloadA + nested Type + (STV 1.0 1.0)` times out at 4s. This narrows the blocker from proof-id-specific neighbor shape to the combination of a two-argument nested Type with an adjacent STV-shaped right sibling in a four-field wrapper. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 112 stdlib unit tests plus `git diff --check`.
- [x] Added local commit `2900386` with a bounded non-live PeTTaChainer four-field nested-position materialize gate after the generic four-field arity gate. New helpers `materialize_four_field_nested_position_rungs(...)` and `run_materialize_four_field_nested_position_gate(...)` move the all-sentinel two-argument nested Type through synthetic four-field `ProofEnvelope` argument positions before returning to the proof-like proof-id/type/STV slot layout. Artifact: `artifacts/pettachainer_materialize_four_field_nested_position_gate_2026-07-04T2200Z.json` (sha256 `00dda1cfd8319db4edb5fc665a4d9b40af97493a032c1869cabc24d6a9bb8ac7`) shows the nested Type passes in each generic Payload slot but times out at 4s in `(ProofEnvelope b-profile-000 (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))`. This narrows the materializer blocker to proof-like neighboring payload shape, not any four-field list containing a two-argument nested expression. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 110 tests; `git diff --check` passes.
- [x] Added local commit `53eb8e8` with a bounded non-live PeTTaChainer generic four-field context arity gate after the context matrix. New helpers `materialize_generic_four_field_context_arity_rungs(...)` and `run_materialize_generic_four_field_context_arity_gate(...)` keep synthetic `(ProofEnvelope proof type tv)` fixed while testing empty, one-argument, then two-argument nested Type rungs before mixed/original token controls. Artifact: `artifacts/pettachainer_materialize_generic_four_field_context_arity_gate_2026-07-04T2000Z.json` (sha256 `5877d1966b10c99d6eccd66a27e41e49f56b41aab365200b77486919ea6d9e9`) shows `(ProofEnvelope b-profile-000 (Requires) (STV 1.0 1.0))` and `(ProofEnvelope b-profile-000 (Requires TypeArgSentinel0) (STV 1.0 1.0))` pass in ~0.45-0.48s, while the all-sentinel two-argument nested Type times out at 4s. This confirms the blocker is generic four-field wrapper context plus nested Type arity two, not original tokens or `:` proof-head syntax. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 108 tests; `git diff --check` passes.
- [x] Added local commit `e67d99c` with a bounded non-live PeTTaChainer nested-Type context matrix gate after the arity/token matrix. New helpers `materialize_nested_type_context_matrix_rungs(...)` and `run_materialize_nested_type_context_matrix_gate(...)` keep `(Requires TypeArgSentinel0 TypeArgSentinel1)` fixed and test it alone, under `(: proof type)`, under synthetic `ProofEnvelope` prefixes, and finally under the original `(: proof type tv)` context. Artifact: `artifacts/pettachainer_materialize_nested_type_context_matrix_gate_2026-07-04T1800Z.json` (sha256 `1926d9f5af5ca5f1343844005ea5fd978edc3b081c19a2dfdefbcfa96af21acd`) shows the nested Type alone, `(: b-profile-000 type)`, and `(ProofEnvelope b-profile-000 type)` pass in ~0.47-0.49s, while `(ProofEnvelope b-profile-000 type (STV 1.0 1.0))` times out at 4s. This moves the blocker from PeTTaChainer `:` proof syntax specifically to generic four-field list context with a two-argument nested subexpression. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 106 tests; `git diff --check` passes.
- [x] Added local commit `d28ab4e` with a bounded non-live PeTTaChainer nested-Type arity/token matrix gate after the nested-Type ladder. New helpers `materialize_nested_type_arity_matrix_rungs(...)` and `run_materialize_nested_type_arity_matrix_gate(...)` keep full proof shape plus sentinel STV fixed while testing all-sentinel arity before mixed/original argument tokens. Artifact: `artifacts/pettachainer_materialize_nested_type_arity_matrix_gate_2026-07-04T1600Z.json` (sha256 `d24401f89cef49eddb83eb6c03ae2990cb626883c7f2f45b01647238e980fa35`) shows the empty nested Type and one-sentinel-argument nested Type pass in ~0.47-0.49s, while the all-sentinel two-argument Type times out at 4s. This narrows the blocker to generic two-argument nested Type arity inside a full proof atom, not the original argument tokens. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 104 tests; `git diff --check` passes.
- [x] Added local commit `bc32501` with a bounded non-live PeTTaChainer nested-Type `materialize-stmt-lambdas` ladder after the sentinel proof-shape gate. New helpers `materialize_nested_type_proof_rungs(...)` and `run_materialize_nested_type_ladder_gate(...)` keep a full proof atom and sentinel STV while rebuilding the nested Type expression. Artifact: `artifacts/pettachainer_materialize_nested_type_ladder_gate_2026-07-04T1400Z.json` (sha256 `bc5aab720dde2427afb1fbf2ad66dba53c2abcb32022e06b1d0ee4a1f8e8c5f2`) shows the atom Type head and one-argument nested Type pass in ~0.49s, while the two-argument nested Type `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))` times out at 4s. This narrows the blocker to a full proof atom with a nested Type expression of arity at least 3 (`Requires` plus two args). No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 101 tests; `git diff --check` passes.
- [x] Added local commit `e655c79` refining the non-live PeTTaChainer `materialize-stmt-lambdas` proof-shape ladder with sentinel full-arity rungs. The gate now tests the already-passing subforms/prefixes plus `(: proof ProofShapeSentinel (STV 1.0 1.0))`, original type with sentinel STV, sentinel type with original STV, and then the exact full proof. Artifact: `artifacts/pettachainer_materialize_proof_shape_sentinel_ladder_gate_2026-07-04T1200Z.json` (sha256 `989cfce15fe4d7703f03e5f67cb0ecde858b191869d1ce062fe66798eefdd78c`) shows the synthetic full-arity proof atom materializes as identity in ~0.44s, but `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))` times out at 4s. This narrows the blocker to full proof shape plus nested statement-type expression, not top-level arity or STV alone. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 98 tests; `git diff --check` passes.
- [x] Added local commit `8fe569e` with a bounded non-live PeTTaChainer `materialize-stmt-lambdas` proof-shape ladder gate. The new gate builds deterministic rungs for `(: proof type tv)`: type subform, STV subform, `(: proof)`, `(: proof type)`, then the full statement. Artifact: `artifacts/pettachainer_materialize_proof_shape_ladder_gate_2026-07-04T1000Z.json` (sha256 `43669be7cd99dd9fc618ed07297518dd53d1a22527d8fa5d8fb6c9f78553ef24`) shows the first four rungs materialize as identity in ~0.47s, while the complete `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 0.70 0.55))` rung still times out at 4s. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 98 tests; `git diff --check` passes.
- [x] Added a bounded non-live `materialize-stmt-lambdas` identity ladder gate in `repos/petta-memory`. `run_materialize_identity_ladder_gate(...)` tests source-checked lambda-free subforms before the full proof, compares materialized output structurally with float-rendering tolerance, and stops at the first blocked rung. Artifact: `artifacts/pettachainer_materialize_identity_ladder_gate_2026-07-04T0800Z.json` (sha256 `2d3d76eed14378a1597bffd557df2429fe30d688542208b0c4ce6d332a7a3f01`) shows `(Requires MemoryTarget0 PLNReadyViews)` and `(STV 0.70 0.55)` materialize successfully, while the complete `(: b-profile-000 ... (STV 0.70 0.55))` proof still times out at 6s. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 95 tests; `git diff --check` passes.
- [x] Added local commit `18e364a` with a bounded non-live `materialize-stmt-lambdas` identity runtime gate in `repos/petta-memory`. `run_materialize_identity_gate(...)` source-checks lambda-free statements, runs only the materializer in an isolated subprocess, and keeps `mm2compile`/`compileadd`/query/live paths gated. Runtime artifact `artifacts/pettachainer_materialize_identity_runtime_gate_2026-07-04T0600Z.json` (sha256 `df9a7339afad400e3262bf7e9eb289cc9b09fb41299024dc79a36f0de6cd5687`) timed out at 6s for the tiny promoted-belief proof, so the next bottleneck remains upstream materializer/evaluator recursion instrumentation. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 91 tests; `git diff --check` passes.
- [x] Added local commit `662845c` with source-level PeTTaChainer `materialize-stmt-lambdas` identity inspection after the exact static-import runtime check. New helper `inspect_materialize_stmt_lambdas_for_statement(...)` records the checked-out definition and statically verifies the tiny promoted-belief STV proof has no `|->` lambda forms, so materialization should be a structural identity walk before `mm2compile`. Artifact: `artifacts/pettachainer_materialize_identity_source_inspection_2026-07-04T0400Z.json` (sha256 `6a5c58ebe7a403dbf2838c0faa430cf80d5554650873aab50915c9e9f02ee682`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 89 tests; `git diff --check` passes.
- [x] Hardened the non-live PeTTa `static-import!` microbenchmark with exact runtime fact membership checks after named-space validation. The loader stage now turns each expected generated clause into a Prolog query goal and verifies it against the consulted selected predicate, preventing a false pass where `scratch.pl` conversion/counts succeed but the runtime predicate is not actually queryable. Artifact: `artifacts/petta_static_import_runtime_fact_check_microbenchmark_2026-07-04T0200Z.json` (sha256 `e893ea1c2edacebf57c4aa4aaa677645890bed6eaddc3eacbd6bfc65543049e8`) loaded 2 normalized atoms into `pmbench_rtcheck/3`; `facts_match` and `runtime_expected_facts_present` are both true. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 88 tests; `git diff --check` passes.
- [x] Added local commit `1e81e10` tightening the non-live `static-import!` microbenchmark after the first loader success. The benchmark now accepts a validated Prolog-safe `space` parameter, computes expected facts for that selected predicate, and queries/counts the selected predicate rather than hard-coding `gckb/3`, preventing false positives if future scratch loader tests use isolated named spaces. Named-space artifact: `artifacts/petta_static_import_named_space_microbenchmark_2026-07-04T0000Z.json` (sha256 `83e77667009e1a0250c814907c84699c073c2d1cb6fe614d73e80e75b1686e58`) loaded 2 normalized atoms into `pmbench/3` with matching facts. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 87 tests; `git diff --check` passes.
- [x] Added local commits `294c8e4` + `5ce4ec0` with a non-live runtime static-import microbenchmark gate after the atom design. `run_static_import_microbenchmark(...)` writes normalized atoms to a temp `scratch.metta`, calls PeTTa `static-import!` via janus_swi in a bounded subprocess, verifies generated `.pl` fact lines match expected Prolog facts and loaded `gckb/3` predicate count matches. Result: 2 atoms loaded, 2 facts matched, ~0.07s. Confirms `static-import!` is a viable bounded loader for Prolog-safe normalized atoms (not a PeTTaChainer `compileadd`/indexing API). Artifact: `artifacts/petta_static_import_microbenchmark_2026-07-03T2200Z.json` (sha256 `f3c9aee668d31cd01595eb07071509ad51d54371b4cc2f0cd2c9b61e99d3a21a`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 86 tests; `git diff --check` passes.
- [x] Added local commit `6513e27` with source-only static-import microbenchmark atom design after the direct static-import inspection. New helper `design_static_import_microbenchmark_atoms(...)` sketches Prolog-safe lowercase/underscore, three-argument top-level scratch atoms for the current STV proof and EvidencePacket examples so a later temporary-directory `static-import!` semantics benchmark can compare generated facts without feeding unsafe current exports directly. Artifact: `artifacts/petta_static_import_microbenchmark_atom_design_2026-07-03T2000Z.json` (sha256 `354c8b77447902098fd14848ec53fe7a15012d3252ea7e5de60d1703ea4762d8`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 84 tests; `git diff --check` passes.
- [x] Added local commit `172b4c9` with source-level PeTTa `static-import!` bulk-load inspection. New helper `inspect_petta_static_import_source(...)` reads checked-out `repos/PeTTa/lib/lib_import.pl` without invoking SWI/qcompile/consult and models its conversion for current petta-memory STV/EvidencePacket exports. Result: do not use `static-import!` directly for current exports; the converter is line-oriented, data-only/no-bangs, and does not quote tokens, while current proof atoms contain uppercase symbols and hyphenated ids unsafe as raw Prolog terms. Artifact: `artifacts/petta_static_import_source_inspection_2026-07-03T1800Z.json` (sha256 `3c3e3829e284a7c837a0ad4be0850c685695c0e49199259d65713ad0d6b2866a`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 83 tests; `git diff --check` passes.
- [x] Added local commit `1091b31` with source-level PeTTaChainer `compile_` branch mapping for the tiny promoted-belief STV statement. New helper `inspect_compile_dispatch_for_statement(...)` parses the exported `(: proof type tv)` atom and checked-out `compile.metta`/`logic_config.metta` without invoking SWI/PeTTaChainer runtime, confirming `(Requires MemoryTarget0 PLNReadyViews)` should reach the `compile_` fact-assertion branch (`compile-fact-kb` + `compile-outputs`) rather than implication/bidirectional rule branches after `materialize-stmt-lambdas`/`mm2compile`. Artifact: `artifacts/pettachainer_compile_dispatch_fact_branch_2026-07-03T1600Z.json` (sha256 `a0e512ae36bf875cb3938de1a5e9370716241ad4839c8548012ded4dc159a0e5`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 82 tests; `git diff --check` passes.
- [x] Added local commit `2cd1b4c` with source-level PeTTaChainer `compileadd` bottleneck mapping before further runtime probes. New helper `inspect_compileadd_bottleneck_sources(...)` records exact upstream source definitions/imports for `materialize-stmt-lambdas`, `mm2compile`, `compile_`, and neighboring `compileadd` subforms without invoking SWI/PeTTaChainer runtime. Artifact: `artifacts/pettachainer_compileadd_source_bottleneck_2026-07-03T1400Z.json` (sha256 `98a1812c5b678d3309d58f7c8b106500f2654e927e3f50b6a61c24323ceee561`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 80 tests; `git diff --check` passes.
- [x] Added local commit `f6d7dbf` with source-level PeTTaChainer add API inspection before further `compileadd` work. New helper `inspect_pettachainer_add_api(...)` reads the checked-out `repos/PeTTaChainer` sources without invoking SWI/PeTTaChainer runtime and records that public add methods route through `compileadd`/`compileadd-mine`; no public precompiled-add/cache API terms were found. Artifact: `artifacts/pettachainer_add_api_inspection_2026-07-03T1200Z.json` (sha256 `b94c89a3af8ce2817e2b5b763d00b676c7e060ffa34c62417ea0e9d1a130d097`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 79 tests; `git diff --check` passes.
- [x] Added local commit `0270fda` reviewing the non-live GoalChainer EC handoff against a second policy fixture before returning to PeTTaChainer `compileadd` work. New fixture `fixtures/goalchainer_conflicting_ec_smoke.metta` supplies strong promoted STV acceptability for `publish_redacted_summary` plus opposing contextual EC counts `(EC 1 9)`; the precompiled gate lowers evidence strength to `0.511429`, keeps confidence `0.833333`, still ranks the action recommended, and preserves `compileadd_not_invoked`/no-task/no-write checks. Artifact: `artifacts/goalchainer_precompiled_conflicting_ec_smoke_2026-07-03T1000Z.json` (sha256 `5dfa832b854c7c4a427686f0419530ec76891c953ed9ac22f1f1e7212c9548bc`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 78 tests; `git diff --check` passes.
- [x] Added local commit `ec84403` deciding and implementing the next non-live GoalChainer evidence depth: keep the precompiled decision-payload gate and add a bounded EvidencePacket/EC influence path before returning to upstream PeTTaChainer `compileadd` instrumentation. Matching `contextual-appraisal-evidence` `EvidencePacket` counts now adjust promoted `Acceptable` action appraisal with provenance while keeping compileadd/query/live OmegaClaw paths disabled. Artifact: `artifacts/goalchainer_precompiled_ec_smoke_2026-07-03T0800Z.json` (sha256 `ec34815dc6f2bbace492a9f6d92484df61775831e957cd0cacf0ce45a4ae654f`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 77 tests; `git diff --check` passes.
- [x] Added a precompiled handoff-cache bypass for the first non-live GoalChainer decision payload gate. `run_goalchainer_precompiled_handoff_smoke(...)` imports only GoalChainer scenario/scoring/explanation modules, consumes promoted `Acceptable` STV items from `goalchainer-handoff-cache`, and explicitly avoids GoalChainer CLI, PeTTaChainer `compileadd`/query, directives, execution, OmegaClaw skills, and memory writes. CLI `goalchainer-smoke` now uses this bypass by default, with `--external-cli` retained for the old blocked subprocess path. Artifact: `artifacts/goalchainer_precompiled_smoke_2026-07-03T0600Z.json` (sha256 `9bad7a5bb956b6c1128f8e6dbb64c304bd430f3cc25830114f9ffe7b6fd39d0c`). Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 77 tests; `git diff --check` passes.
- [x] Added local commit `a2dc693` and attempted the first non-live GoalChainer smoke wrapper using a hand-picked `goalchainer-handoff-cache` fixture under timeout. The wrapper/CLI/test contract requires ranked decision payload provenance and rejects directive/task-claim output; the external GoalChainer run currently fails before payload with SWI `stack_limit=8g` exceeded in PeTTaChainer `compileadd`. Failure artifact: `artifacts/goalchainer_smoke_failure_2026-07-03T0400Z.json` (sha256 `a35c65c0e771a86551fd481dae1e837d2a1796eb43e424d76a8948087f4945cd`).

## Next
- [x] Require distinct fact and rule compiler identities in typed
  PeTTaChainer derived captures and compiler-bound rule attribution, preventing
  a correctly rehashed TotalMP artifact from reusing one sentence/proof on
  both sides. Local commit `19fb7a9`; fresh full 601 tests and `git diff
  --check` passed (2026-07-25 03:00 PDT / 10:00 UTC). No runtime,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Close TotalMP premise independence in typed PeTTaChainer result captures
  and compiler-bound rule attribution: fact and rule stamp sets and
  evidence-basis sets must be mutually disjoint, so a correctly rehashed
  artifact cannot double-count one provenance source on both sides. Focused 1
  and full 601 tests passed; `git diff --check` passed; local commit `1198954`
  (2026-07-24 21:02 PDT / 2026-07-25 04:02 UTC). No runtime, promotion/write,
  upstream/remote action, paid compute, or live integration.
- [x] Close the Phase-1 clean-room reload gate over the exact archived kernel program. `read_episode_manifest(..., complete_program=...)` now verifies the manifest program CID, exact-once compiled sentence inclusion, and validated-query inclusion; byte-different cross-run program input fails closed. Local commit `58fa218`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-22 23:00 PDT / 2026-07-23 06:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Route all four legacy pi-PLN audit readers through bounded descriptor-anchored admission and prove their public APIs reject symlinked parents. Local commit `bfcc28b`; focused 4 and full 597 tests passed; `git diff --check` passed (2026-07-21 21:00 PDT / 2026-07-22 04:00 UTC). No runtime inference, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Added public-boundary regression coverage for all four pi-PLN writers unified in `fb7a71d`. Each now proves a group-writable parent is rejected without creating the requested artifact. Local regression commit `b3cbf00`; focused 4 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Closed the missing regression for simultaneous initial parent `fstat` failure and parent-descriptor close failure in checksummed PeTTaChainer artifact admission. The test proves `c50eb47` preserves the metadata error and attaches the secondary cleanup diagnostic. Focused 2 and full 590 tests passed; `py_compile` and `git diff --check` passed. No runtime, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Hardened ranked-plan admitted handoff metadata consistency: embedded `admitted_handoff["item_count"]` is rewritten to the admitted subset length after recommendation filtering, with regression coverage for a 2-source/1-admitted handoff. Verification: focused ranked-plan tests pass 33 cases; full suite passes 405 tests; `git diff --check` passes. Non-live wrapper gate only; no `PLN.Query`/`PLN.Derive` or live integration.
- [x] Reviewed the non-live GoalChainer EC handoff behavior against a second policy fixture (`goalchainer_conflicting_ec_smoke.metta`) with high STV but opposing EC counts; the precompiled gate remains bounded and non-live while evidence strength is reduced as expected.
- [x] Added a source-level PeTTaChainer `compileadd` bottleneck map for `materialize-stmt-lambdas`, `mm2compile`, and downstream `compile_` dispatcher definitions without rerunning noisy runtime stages.
- [ ] Continue PeTTaChainer `compileadd` upstream instrumentation at the now-isolated `materialize-stmt-lambdas` recursion/evaluator rung before `mm2compile`, then the identified `compile_` fact-assertion branch. The four-field right-payload arity/head gate now shows generic left `PayloadA` + nested Type + atom/zero-arg/one-arg right payloads pass, but a generic two-argument right payload `(RightPayload 1.0 1.0)` times out before STV-specific rungs; the blocker is no longer proof-id-specific or STV-head-specific and appears tied to adjacent two-argument nested siblings in a four-field wrapper. Source inspection found no `|->` forms and no public precompiled-add/cache API. The `static-import!` side path is verified only as a normalized-atom loader, including exact runtime predicate membership checks, and remains outside PeTTaChainer compile/index semantics. This track is now deprioritized in favor of the patham9/PLN pivot below.
- [x] Clone `patham9/PLN` (aka `trueagi-io/PLN`) locally and reproduce initial smoke tests under the existing local SWI/PeTTa environment. Actual checkout path: `projects/petta-memory/repos/patham9-pln`, remote `https://github.com/patham9/PLN.git`, commit `55f1751d993f71b8a24da03e3aec94ab40789a59`; compatibility symlink: `projects/petta-memory/repos/PeTTa/repos/PLN -> ../../patham9-pln`. Built `PLN.metta` with `sh build.sh`; `FlyingRaven` and `Smokes` pass under `../PeTTa/run.sh` when run from the PLN checkout. Several examples/rule tests emit `Passed: false` despite shell status 0, so the next gate must parse semantic test output. Run record: `artifacts/patham9-pln-smoke-20260704/RUN.md`.
- [x] Built a robust patham9/PLN smoke-gate parser that treats shell-successful semantic failures (`Passed: #f`, missing `Passed: #t`, or `(Error ...)`) as failures and can reclassify explicit `.retry.log` evidence. Artifact-only triage over `artifacts/patham9-pln-hyperon-smoke-20260704/results.json`: primary summary 4/11 passed and 7/11 failed from initial ruletest import/module-resolution errors; retry-aware summary 11/11 passed, classifying those ruletest failures as harness/environment drift rather than semantic PLN regressions. Artifacts: `artifacts/patham9_pln_smoke_gate_summary_2026-07-05T0600Z.json` sha256 `942e6fa303bd0b5d6b0701f54050955e3e0a53c707947ec9efe3808e40ffe717`; `artifacts/patham9_pln_smoke_retry_gate_summary_2026-07-05T0600Z.json` sha256 `ceaddccdd997c46c209d757c43280aa4df462561085ebf7236207090873dd444`.
- [x] Added local commit `94f5b2d` with the first non-live `patham9/PLN` Sentence handoff bridge in `repos/petta-memory`: `patham9_pln_handoff_sentences(...)` and CLI `patham9-pln-handoff` map promoted handoff STV items into `(Sentence $Term (stv S C) ($EvidenceID))` while preserving contextual EvidencePacket/EC/provenance metadata under a π-PLN extension block. Artifact: `artifacts/patham9_pln_handoff_sentence_bridge_2026-07-05T0800Z.json` sha256 `27745f0c0a1c417ed295f4bcc8c31ae4d3c1113c9b31ed37c7d4e33850c0f41f`. No `PLN.Query`/`PLN.Derive`, PeTTaChainer `compileadd`, OmegaClaw/GoalChainer live path, or memory write path was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 125 tests; `git diff --check` passes.
- [x] Added local commit `a653dea` with a patham9/PLN read-only query smoke gate in `repos/petta-memory`: `patham9_pln_query_smoke_program(...)`, `run_patham9_pln_query_smoke(...)`, and CLI `patham9-pln-smoke` load one generated Sentence into the local chainer, parse semantic `Passed:` markers, and preserve original PMEvidence/EvidencePacket provenance in a sidecar while using a numeric runtime stamp for patham9 stamp compatibility. Artifact: `artifacts/patham9_pln_handoff_query_smoke_2026-07-05T1000Z.json` sha256 `b37fe179482b5d758b2a7c2b8d6b6da1a2271e226cb04b528c051ab2a44352bd`; status passed over `(Acceptable publish_redacted_summary)` with `((stv 0.91 0.74) (0))`. No PeTTaChainer `compileadd`, GoalChainer live path, OmegaClaw integration, memory append, or inferred-belief promotion was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 126 tests; `git diff --check` passes.
- [x] Added local bounded non-live two-premise patham9/PLN derivation smoke after the direct query smoke. New helpers `patham9_pln_derivation_smoke_program(...)` and `run_patham9_pln_derivation_smoke(...)`, plus CLI `patham9-pln-derivation-smoke`, load one generated promoted handoff Sentence plus one synthetic bridge implication to `(PMDerivedFromHandoff <term>)`. Runtime artifact: `artifacts/patham9_pln_handoff_derivation_smoke_2026-07-05T1200Z.json` (sha256 `7352b59ffec908f9752f174fc7c7102c5d5ce737589fe16bfe19314bfdd9e545`) passed for `(PMDerivedFromHandoff (Acceptable publish_redacted_summary))` with `((stv 0.9118 0.666) (0 1))`. Numeric runtime stamps are mapped to PMEvidence/synthetic-bridge provenance in the sidecar. No PeTTaChainer `compileadd`, GoalChainer live path, OmegaClaw integration, memory append, or inferred-belief promotion was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 127 tests; `git diff --check` passes.
- [x] Decided and implemented the patham9/pi-PLN wrapper-vs-internal boundary after the direct recall and two-premise derivation gates. New helper `patham9_pi_pln_boundary_plan(...)` records a wrapper-first policy: keep checked-out patham9/PLN unmodified for `PLN.Query`/`PLN.Derive` over `Sentence` atoms; petta-memory owns numeric runtime stamps, PMEvidence/provenance sidecars, and later reviewed EC/context pre-projection. Artifact: `artifacts/patham9_pi_pln_wrapper_boundary_plan_2026-07-05T1400Z.json` (sha256 `4e85e10f97ebed4317f6b299fc42ccecc63b89a7b65ce66a76550eaba1558588`). No truth-changing EC projection, patham9 source patch, memory append, inferred-belief promotion, PeTTaChainer `compileadd`, or live OmegaClaw/GoalChainer integration was invoked. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 129 tests; `git diff --check` passes.
- [x] Added local commit `349f60d` with the first non-live wrapper-level EC projection formula gate for patham9/pi-PLN. New helpers `ec_projected_stv(...)`, `patham9_pln_ec_projection_smoke_program(...)`, `run_patham9_pln_ec_projection_smoke(...)`, and CLI `patham9-pln-ec-projection-smoke` compare direct STV versus projected STV query smokes. The formula blends base STV with EC-derived evidence using confidence-weighted averaging. Runtime artifact `artifacts/patham9_pln_ec_projection_smoke_2026-07-05T1600Z.json` sha256 `f6802b2b661273ec1fd09c4970142b54d660e63d56d99e92abcf218a6f67f23e` passed both direct and projected query smokes. Verification: 135 tests pass; `git diff --check` passes.
- [x] Added local commit `4650d42` with conflicting-EC and derivation EC projection smokes. The conflicting-EC smoke (`patham9_pln_ec_projection_conflicting_smoke_program`, `run_patham9_pln_ec_projection_conflicting_smoke`, CLI `patham9-pln-ec-conflicting-smoke`) verifies the formula lowers strength: strong base STV (0.94, 0.80) with opposing EC (1, 9) drops projected strength to 0.511429 while confidence rises to 0.833333. The derivation EC projection smoke (`patham9_pln_derivation_ec_projection_smoke_program`, `run_patham9_pln_derivation_ec_projection_smoke`, CLI `patham9-pln-derivation-ec-smoke`) extends EC projection to two-premise derivation: direct produces `((stv 0.9118 0.666) (0 1))` while projected produces `((stv 0.90660894 0.7499997) (0 1))`, confirming the formula influences derived results. Runtime artifacts: `artifacts/patham9_pln_ec_conflicting_projection_smoke_2026-07-05T1800Z.json` sha256 `e64d3abff53e8d8dff5e7ec62747c5b6192e9bf906cb68f5018f0a52440c3c2f` and `artifacts/patham9_pln_derivation_ec_projection_smoke_2026-07-05T1800Z.json` sha256 `c6a3134108bf8f613e22202646992f5a2c54784dec40ec46ee233a87341f9210` both pass. No memory append, inferred-belief promotion, patham9 source patch, OmegaClaw/GoalChainer live path was invoked. Verification: 142 tests pass; `git diff --check` passes.
- [x] Extend the EC projection smoke to a two-premise derivation smoke (direct vs projected) to verify the formula influences derived results, not just direct recall.
- [x] Added local commit `4650d42` with conflicting-EC and derivation EC projection smokes.
- [x] Inspected `trueagi-io/PeTTa` `lib/lib_import.pl` `static-import!` as a possible fast static atom/bulk-load path. Source-only result: it may still be useful for a later scratch microbenchmark, but not directly with current petta-memory PeTTaChainer exports because token quoting/line-oriented conversion is unsafe and it is not a supported PeTTaChainer precompiled-add/indexing API.
- [x] Designed the static-import scratch atom format in source-only mode: lowercase/underscore normalized STV/EvidencePacket records with exactly three top-level fields for PeTTa `static-import!` converter compatibility, plus mapping metadata and non-live gates.
- [x] Ran the non-live temporary-directory runtime microbenchmark over the designed normalized atoms. `static-import!` successfully loaded 2 Prolog-safe atoms into the `gckb/3` space predicate, generated `.pl` and `.qlf` files, and all 2 loaded fact lines matched expected converted Prolog facts in ~0.07s. The loader is viable for normalized atoms but remains a bulk data loader, not a PeTTaChainer `compileadd`/indexing API.
- [x] Hardened the same microbenchmark for isolated named spaces: selected predicates are validated and used consistently for expected facts, runtime count, and first-solution query; `pmbench/3` passed the same 2-atom loader gate.
- [x] Implemented a minimal non-live precompiled-statement cache/handoff artifact for checked promoted STV statements and EvidencePackets, explicitly labeled as non-inferred PLN-ready inputs, so OmegaClaw/GoalChainer mapping can consume stable evidence without invoking PeTTaChainer `compileadd`.
- [x] Reviewed Nil Geisweiller / trueagi-io experimental chaining repo. Cloned at `repos/trueagi-chaining` commit `bc9beb2`. Key findings recorded in NOTES.md (2026-07-02 entry): pure-MeTTa PLN prototypes under four representation strategies, PLN-based inference controller (`pln-inf-ctl.metta`), four iterations of backward-chaining continuation control, probabilistic backward chaining. Most relevant for the inference-control phase (roadmap item 4); no runtime integration needed now.
- [x] Design OmegaClaw-specific inference-control mechanisms for context-rich experiential learning after the basic PeTTaChainer path is working and profiled. First pattern (probabilistic filtering) implemented as `probabilistic_inference_filter()`; second pattern (context selection) implemented as `context_selection_wrapper()`; third pattern (chained filter+select pipeline) implemented as `chained_inference_pipeline()` combining stages 1+2 with index remapping; fourth pattern (meta-learning benchmark) implemented as `build_meta_learning_benchmark_handoff()` and `run_meta_learning_benchmark()` creating a synthetic shortcut-vs-chain scenario and verifying the existing wrappers correctly prefer the high-confidence shortcut; fifth pattern (continuation predicate) implemented as `continuation_predicate_wrapper()` evaluating whether each handoff item should continue, terminate, or be rejected based on STV strength/confidence, derivation depth, domain, EC support ratio, and promotion rule; sixth pattern (controlled backward chainer) implemented as `controlled_backward_chainer()` simulating a bounded backward-chaining loop using the continuation predicate as a per-branch decision function with context updaters (accumulate_depth, accumulate_ec, fixed) tracking depth and EC accumulation between steps, max_steps/max_branches safety caps, and a derivation trace showing per-step decisions; seventh pattern (PLN estimator) implemented as `pln_estimator_wrapper()` converting handoff items into PLN viability prior parameters (alpha/beta) from EC counts or STV values, Thompson-sampling from the Beta posterior to rank exploration branches, producing EDCall (Estimated Delayed Call) records with exploration weight controlling the exploration/exploitation tradeoff. Eighth and final pattern (controller-as-chainer) implemented as `controller_as_chainer()` running a primary controlled backward chainer and then a controller chainer with stricter parameters that can confirm, override-terminate, or override-reject branches the primary would have continued. Override-terminate takes priority over override-reject because termination preserves the result as a final answer. All eight inference-control patterns from the trueagi-io/chaining survey are now implemented: four near-term (probabilistic filtering, context selection, chained pipeline, meta-learning benchmark), two medium-term (continuation predicate, controlled backward chainer), and two long-term (PLN estimator, controller-as-chainer). Local commits `23dc651` + `fd01014`; 360 tests pass; `git diff --check` passes.
- [ ] Profile PeTTaChainer rule-application and truth-value-formula mechanics on larger narrow petta-memory/OmegaClaw-context workloads after add-stage bottlenecks are understood.
- [x] Source-gate the first repaired one-rule result's exact truth formula and recompute its STV. `TotalMpConclusionFormula` uses the absent-complement fallback `(STV 0.2 0.2)` and `TotalMpFormula` yields `[0.7600000000000001, 0.52]` from fact `(0.8, 0.6)` and rule `(0.9, 0.8)`; the fresh runtime answer matched exactly. Focused 111 and full 566 tests passed, plus `py_compile` and `git diff --check`. Immutable compiler rule binding, manifests, promotion/write, and live integration remain closed. (2026-07-17 23:00 PDT)

## Done recently

- [x] Source-gate and replay the three nested concrete-fact predicates inside direct PeTTaChainer `compile_` over a literal KB clause. The literal branch returned one clause; `bidirectional-implication-type?` introduced four identical copies, while implication and variable-type gates added none. Local commit `1f219a6`; focused 79/full 534 tests passed. Annotation/definition dispatch and the separately measured `compile-fact-kb` factor remain diagnostic; no add/query/write/live gate changed.

- [x] Added local commit `32746a2` with non-live GoalChainer handoff mapping in `repos/petta-memory`: `MediumMemoryStore.goalchainer_handoff_cache(...)` and CLI `goalchainer-handoff-cache` repackage promoted PeTTaChainer handoff items as GoalChainer appraisal/acceptability evidence inputs, preserving belief/cluster/promotion provenance and explicitly disabling task claims, live OmegaClaw skills, memory writes, and inferred-belief status. Added `docs/goalchainer_handoff.md` with the non-live gate contract. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 72 tests; `git diff --check` passes.
- [x] Added local commit `10f2579` with a non-live PeTTaChainer handoff cache in `repos/petta-memory`: `MediumMemoryStore.pettachainer_handoff_cache(...)` and CLI `pettachainer-handoff-cache` emit JSON containing promotion-eligible STV statements and EvidencePackets, labeled as `pln-ready-input-not-inferred-belief`, with optional runtime statement checking and `compileadd`/query still gated. Generated artifact `projects/petta-memory/artifacts/pettachainer_handoff_cache_2026-07-03T0000Z.json` (sha256 `fa6bccab591590c799685ff85c336b49329771183bc72433765ed37e1b0b97a2`) from a size-2 profile workload using `PeTTaChainer.check_stmt == 1.0` for STV statements; EvidencePackets carry explicit non-negative EC counts. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 71 tests; `git diff --check` passes.
- [x] Added local commit `1fc6f04` deciding the next minimal PeTTaChainer add path in `repos/petta-memory`: added `summarize_compileadd_strategy(...)` to turn bounded profile artifacts into a reproducible strategy summary, plus a regression test. Artifact `projects/petta-memory/artifacts/pettachainer_compileadd_strategy_2026-07-02T2200Z.json` (sha256 `6261705d465c8ee94faea5f2d5d74f080e6440257482ddcb5f4d4f5e5013311d`) recommends a non-live `precompiled_statement_cache_gate`: cache checked promoted STV statements/EvidencePackets as handoff inputs, not inferred beliefs, while full PeTTaChainer `compileadd`/query remains gated pending upstream materialize/mm2compile instrumentation or a precompiled add API. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 69 tests; `git diff --check` passes.
- [x] Refined PeTTaChainer `compileadd` probes in `repos/petta-memory` to compare direct subform invocation against eval-wrapped controls. Artifact `projects/petta-memory/artifacts/pettachainer_profile_compileadd_direct_probe_2026-07-02T2000Z.json` (sha256 `e7a92e21d635e72df346e0684371e847b7f613602f1fe09bd15cf176ff520307`) shows constructor/check_stmt still succeed; direct and eval-control materialize/mm2compile both time out at 5s, while `index-source-implication` and `maybe-process-on-add` remain fast. Decision point sharpened: the early timeout is not merely the previous `eval` wrapper; next choose a minimal/precompiled add strategy or deeper upstream instrumentation. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 68 tests; `git diff --check` passes.
- [x] Added local commit `953c504` with internal PeTTaChainer `compileadd` probes in `repos/petta-memory`: opt-in runtime profiling now schedules seven isolated subprocess stages for `materialize-stmt-lambdas`, `mm2compile`, proof-structure internalize/externalize, `index-source-implication`, add-internalized atoms, and `maybe-process-on-add` before the existing add-only/add+query stages. Artifact `projects/petta-memory/artifacts/pettachainer_profile_compileadd_probe_2026-07-02T1800Z.json` (sha256 `1891e2ebda4895cf73ddcd2595168fae93d038699d59d020cfd05c73da362b12`) shows constructor/check_stmt succeeded, `index-source-implication` and `maybe-process-on-add` completed quickly after initialization, while materialize/mm2compile/internalize/externalize/add-internalized and full add stages timed out at 3s. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 67 tests; `git diff --check` passes.
- [x] Added PeTTaChainer constructor-only profiling in `repos/petta-memory`: opt-in runtime profiles now record `pettachainer_init_only` before add-only/add+query stages, separating SWI/MeTTa library construction from `compileadd`. Smoke artifact `projects/petta-memory/artifacts/pettachainer_profile_init_2026-07-02T1601Z.json` (sha256 `fb9cc8c6ce7ee67015fa52e4074c6749095b3cca1a7f89e93b84c7d9838969bf`) shows constructor initialization succeeds in ~0.48s while proof add-only, proof add+query, contextual packet add-only, and contextual add+query still time out at 6s. Decision: the immediate bottleneck is inside `compileadd`/add instrumentation, not PeTTaChainer construction or query/context projection. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 67 tests; `git diff --check` passes.
- [x] Added local commit `f43be64` with add-only bottleneck stages to the isolated PeTTaChainer profiler in `repos/petta-memory`: opt-in runtime profiling now records `proof_runtime_add_only` and `contextual_packet_add_only` before combined add+query stages, so timeouts can be attributed before query/contextual projection work starts. Ran `--sizes 1 --steps 1 --timeout-sec 1 --stage-timeout-sec 6 --include-contextual`; artifact `projects/petta-memory/artifacts/pettachainer_profile_contextual_2026-07-02T1400Z.json` (sha256 `6054d50ec9fff76c6107a6adfa9a495a9ef735189d09e154c07dc8a08b893b79`) shows `check_stmt` succeeds while proof add-only, proof add+query, contextual packet add-only, and contextual add+query all time out at 6s. Decision: the immediate bottleneck is compile/add/instrumentation, not query search yet. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 67 tests; `git diff --check` passes.
 - [x] Added local commit `7a764d0` with isolated PeTTaChainer runtime profiling stages in `repos/petta-memory`: optional `compileadd`/query/contextual profile work now runs in bounded subprocesses via `--stage-timeout-sec`, captures OS-level stdout/stderr byte counts, and records timeout events instead of hanging the worker. Smoke artifact `projects/petta-memory/artifacts/pettachainer_profile_isolated_2026-07-02T1200Z.json` (sha256 `b51bbe7cc7c38908be36036b5e86b01de8202673d741e5344c07b3b63c9a9f73`) shows size 1 `check_stmt` succeeds while proof `compileadd`+query times out cleanly at 3s. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 66 tests; `git diff --check` passes.

## Waiting or blocked

- [x] PeTTaChainer runtime dependency setup - local SWI-Prolog 9.3.36 with Janus is installed at `toolchains/local/swi-prolog-9.3.36`; the helper `local/pettachainer-env.sh` currently points at the separately validated shared copy `projects/omegaclaw/local/swipl-9.3.36`. Created/verified PeTTaChainer venvs with `janus-swi`, sibling `PeTTa`, and editable `PeTTaChainer`. Verification: `swipl --version`, Janus import/library check, `PeTTa.process_metta_string('!(+ 1 2)') -> ['3']`, `PeTTa.process_metta_string('!(+ 2 3)') -> ['5']`, and `pettachainer.check_stmt(...) -> 1.0` passed. Full upstream demo/tests emit huge PeTTa compilation traces and run long/benchmark-like, so the next step is a deliberately narrow PLN smoke rather than broad upstream tests.

## Done recently

- [x] Added local commit `7a764d0` with isolated PeTTaChainer runtime profiling stages in `repos/petta-memory`: optional `compileadd`/query/contextual profile work now runs in bounded subprocesses via `--stage-timeout-sec`, captures OS-level stdout/stderr byte counts, and records timeout events instead of hanging the worker. Smoke artifact `projects/petta-memory/artifacts/pettachainer_profile_isolated_2026-07-02T1200Z.json` (sha256 `b51bbe7cc7c38908be36036b5e86b01de8202673d741e5344c07b3b63c9a9f73`) shows size 1 `check_stmt` succeeds while proof `compileadd`+query times out cleanly at 3s. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 66 tests; `git diff --check` passes.
- [x] Added local commit `9cb3002` with a narrow PeTTaChainer profiling harness in `repos/petta-memory`: `python -m petta_memory.pettachainer_profile` generates promoted-belief clusters with explicit STV and EC counts, exports both proof statements and EvidencePackets, and times store/export plus `check_stmt` validation. Wrote artifact `projects/petta-memory/artifacts/pettachainer_profile_2026-07-02T1000Z.json` (sha256 `0dcb4a131439b1ef550275ef22bdfed289c6f574d13e9569b0e9892fcb10dacb`) for sizes 1/3/5. Runtime `compileadd`/contextual-query stages are opt-in after an attempted run exceeded the worker timeout/noise budget. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 64 tests; `git diff --check` passes.
- [x] Added local commit `0fda6d3` with explicit `EvidenceSupportCount`/`EvidenceOppositionCount` schema support and PeTTaChainer `EvidencePacket` export in `repos/petta-memory`. Counts are validated as non-negative numeric binary relations and `MediumMemoryStore.pettachainer_evidence_packet_view()` plus CLI `pettachainer-packets-view` emit `(EvidencePacket statement (EC pos neg) ((domain ...) (promotion-rule ...)) promotion-event)` only when promoted beliefs carry explicit counts. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 61 tests; `git diff --check` passes.
- [x] Added local commit `66aebbb` wiring the optional parse-check seam to local PeTTa runtime validation and drafting the live OmegaClaw integration review gate. `petta_memory.make_petta_parse_checker(...)` can now be explicitly passed to `MediumMemoryStore(parse_checker=...)` so canonicalized clusters are checked with `PeTTa.process_metta_string` before append; runtime rejection becomes `ValidationError` and leaves the journal unchanged. `docs/omegaclaw_migration.md` now lists the live-read/write boundary review gate before any OmegaClaw wiring. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 59 tests; `git diff --check` passes.
- [x] Added local commit `0460d3d` with PeTTaChainer-specific normalized evidence export and first runtime smoke: `MediumMemoryStore.pettachainer_evidence_view()` plus CLI `pettachainer-view` emit promoted beliefs as `(: proof-id statement (STV strength confidence))`, preserving strength and capping confidence by `PromotionTrust`. Added unit/CLI coverage plus a local PeTTaChainer `check_stmt(...)` smoke over the checked-out SWI-Prolog 9.3.36 + Janus runtime. EC/EvidencePacket export is explicitly deferred until support/opposition counts are represented. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 56 tests; `git diff --check` passes.
- [x] Added local commit `78478b3` tightening `Contains` read/write-boundary validation: a cluster may no longer contain its own `MemoryCluster` id, preventing self-containment cycles from being accepted into audit/query/prompt/index views. Added regression coverage. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 53 tests; `git diff --check` passes.
- [x] Added pushed local commit `f9647bd` tightening delimited journal read validation: records whose `BEGIN`/`END` MemoryCluster envelope id disagrees with the internal `(MemoryCluster ...)` atom now raise `ValidationError` instead of being silently normalized by audit/query views. Added regression coverage. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 53 tests; `git diff --check` passes.
- [x] Added local commit `51045c3` tightening binary metadata/retrieval relation validation: known subject/object predicates such as `SchemaVersion`, `About`, `StatusValue`, `PromotionTrust`, and `EvidenceFor` now reject extra arguments instead of allowing hidden fields that read views would ignore. Added regression tests. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 52 tests; `git diff --check` passes.
- [x] Added local commit `ba08f54` tightening audit/read-boundary validation: bounded audit-view plus ID-declaration arity validation; unary ID-declaring predicates such as `MemoryCluster`, `ObservedEvent`, and `Decision` now reject extra arguments instead of silently indexing only the first id. Added regression tests. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 51 tests; `git diff --check` passes.
- [x] Added a bounded audit view for complete canonical cluster records: `MediumMemoryStore.audit_view()` and CLI `audit-view` keep newest records that fit, preserve begin/end delimiters, omit over-budget records rather than truncating, and reject negative bounds. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 50 tests; `git diff --check` passes.
- [x] Added local commit `423a372` with a separately feature-flagged OmegaClaw generated-index wrapper: `OmegaClawMemoryPolicy.index_view_reads_enabled` defaults off, `OmegaClawMemoryBridge.index_view_metta()` emits a bounded read-only-derived `MM-index` envelope with validated wrapper id and escaped generated-at string, and policy rejects negative index bounds. Updated migration/API boundary docs. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 47 tests; `git diff --check` passes.
- [x] Added an OmegaClaw-style non-live prompt/index fixture and regression test: `fixtures/omegaclaw_prompt_context.metta` is loaded into a temporary store, `OmegaClawMemoryBridge.prompt_view_metta()` is exercised under a bounded read-only policy, and `MediumMemoryStore.index_view()` is checked for matching retrieval edges. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 45 tests; `git diff --check` passes.
- [x] Hardened the safe OmegaClaw prompt-view wrapper boundary: `OmegaClawMemoryPolicy.view_id` now rejects malformed symbol ids, and `PromptViewGeneratedAt` uses the shared S-expression string escaper so caller-supplied timestamps with quotes/backslashes/newlines remain parseable inside the read-only wrapper. Added regression tests. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 44 tests; `git diff --check` passes.
- [x] Tightened cluster validation/read-write boundaries: declared IDs under ID-declaring predicates must be valid symbol IDs, and `Contains` edges must have exactly cluster/target IDs, use the local cluster id, and point to records declared in the same cluster. Added regression tests. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 42 tests; `git diff --check` passes.
- [x] Extended complete-atom bounded rendering to PLN-safe views: `MediumMemoryStore.pln_view(limit_chars=...)` and CLI `pln-view --limit-chars` reject negative limits and omit over-budget atoms instead of returning partial MeTTa. Added store and CLI regression tests. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 40 tests; `git diff --check` passes.
- [x] Tightened bounded prompt/index views to preserve complete atom lines instead of slicing mid-atom, keeping returned MeTTa snippets parseable under character budgets. Added regression tests for prompt-view and `MM-index` boundaries. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 36 tests; `git diff --check` passes.
- [x] Documented non-live OmegaClaw migration/API names in `docs/omegaclaw_migration.md`, linked it from README, and tightened prompt-view bounded-read validation by rejecting negative `limit_chars` through API and CLI. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 34 tests; `git diff --check` passes.
- [x] Added second empirical bounded retrieval fixture `fixtures/bounded_prompt_recall.metta` for prompt-view topic/status preferences under a tight character budget; regression test verifies the relevant MediumPeTTaMemory/active atoms stay visible while a newer distractor is excluded. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 32 tests; `git diff --check` passes.
- [x] Added first empirical recall/query fixture `fixtures/index_query_parity.metta` for `MM-index` versus direct query parity across id/type/about/status/role retrieval; `MM-index-id` now includes identifier argument mentions so index id retrieval matches `query_id` on the fixture. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 31 tests; `git diff --check` passes.
- [x] Added generated bounded `MM-index` view and CLI `index-view` for id/type/about/status/role retrieval edges; status index ignores superseded `StatusEvent`s and maps `StatusValue` to `StatusSubject` when present. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 30 tests.
- [x] Added stricter PLN promotion metadata and normalized mapping on branch `agent/parser-validation`: promoted derived beliefs now require explicit `PromotionRule`, bounded `PromotionTrust`, and `PromotionDomain`; `pln-view --normalized` emits `MM-PLNPremise`, `MM-PLNDomain`, `MM-PLNTrust`, and `MM-PLNPromotionRule` atoms for eligible beliefs. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 27 tests; `git diff --check` passes.
- [x] Added optional caller-supplied `parse_checker` seam on branch `agent/parser-validation` after commit `fa10642`; checker sees canonicalized clusters before append and rejection leaves the journal unchanged. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 25 tests.
- [x] Replaced shallow line validation with a small recursive S-expression parser on branch `agent/parser-validation`; parser now accepts multiline nested atoms and comments outside strings while rejecting top-level non-atoms/stray tokens. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 23 tests.
- [x] Improved prompt-view relevance ordering by optional topic/status preferences plus salience/recency ordering in branch `agent/omegaclaw-wrapper-sketch`, commit `22d5aa4`.
- [x] Added local-only OmegaClaw MeTTa prompt-view wrapper sketch and feature-flag/read-write-boundary notes in branch `agent/omegaclaw-wrapper-sketch`, commit `1e2a109`; live/autonomous writes remain disabled.
- [x] Created public GitHub repo `https://github.com/bgoertzel-sing/petta-memory` and pushed local `main` through commit `51eb629`.
- [x] Created local repository scaffold at `projects/petta-memory/repos/petta-memory`.
- [x] Implemented `petta_memory.store.MediumMemoryStore` append-only cluster journal prototype.
- [x] Added CLI: `python -m petta_memory.cli append|query|prompt-view|pln-view|tail`.
- [x] Added validation for parseable atoms, required `MemoryCluster` metadata, schema version, max atom/cluster sizes, and provenance/source.
- [x] Added explicit begin/end cluster delimiters and temporary-file replacement for local atomic writes.
- [x] Added bounded queries by cluster/id, type, `About`, status, and epistemic role.
- [x] Added current-status derivation from append-only `StatusEvent` and `Supersedes` atoms.
- [x] Added prompt-view and PLN-view exports; PLN view filters raw utterances, unpromoted quoted claims, and unpromoted derived beliefs.
- [x] Added explicit `PromotionEvent` path for PLN-safe derived beliefs.
- [x] Added example clusters for a fresh Telegram-message episode, idle/no-input episode, and design-project episode.
- [x] Added e2e fixture `fixtures/e2e_journal.metta` covering request -> commitment -> artifact -> resolved status -> PLN promotion.
- [x] Incorporated GPT5.5-Pro design-review hardening in local commits `3d60071` and `51eb629`.
- [x] Added file locking, duplicate ID rejection, safer PLN-view exclusions/dangling quote filtering, and CLI query cleanup in commit `51eb629`.
- [x] Added stdlib `unittest` tests; `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes 14 tests.

- [x] Hardened `live-goal-bridge` against malformed GoalChainer decision-payload metadata (`scenario`, `runtime`, `explanation`) before emitting read-only bridge artifacts. Added regression coverage for non-string/empty scenario, non-object runtime, non-list explanation, and malformed explanation entries. Verification: focused live-bridge tests passed 26 cases; full unittest discovery passed 439 tests; `git diff --check` passed.
  - Local implementation commit in `repos/petta-memory`: `ab16409`.

- [x] Hardened the read-only `live-goal-bridge --run-patham9-runtime` program sentence-count contract. Successful runtime artifacts must now include integer, non-negative `handoff_sentence_count` and `sentence_count`; the handoff count must equal the admitted item count and the total must equal handoff sentences plus the one synthetic bridge sentence. Missing counts and count drift fail closed before GoalChainer appraisal. Verification: local implementation commit `561f0be`; focused live-bridge tests passed 27 tests; full unittest discovery passed 440 tests; `git diff --check` passed. Boundaries preserved: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9 source change, or OmegaClaw skill/task claim.

- [x] Pinned the read-only `live-goal-bridge --run-patham9-runtime` gate to the exact multi-sentence derivation result/program schemas before GoalChainer appraisal. Wrong-but-nonempty query-smoke schemas now fail closed, closing a provenance/type-confusion gap left by non-empty-string validation. Local commit `f42d293`; focused live-bridge tests passed 27 cases; full unittest discovery passed 440 tests; `git diff --check` passed. No PeTTaChainer `compileadd`, memory append/promotion, patham9 source change, or OmegaClaw skill/task claim.

## Atlas-indexed reversible πPLN roadmap (adopted 2026-07-11)

- [x] Make Phase-2 launch byte budgets literal at the OS serialization boundary. Argv and cwd now include terminating NULs, explicit environments include `KEY=VALUE\0` framing, and pinned executable symlink resolution triggers a second argv-size check before hashing/launch. Local commit `5d637c7`; focused 4 and full 497 tests passed; `py_compile` and `git diff --check` passed. No kernel semantic, promotion/write, or live-integration claim.

- [x] Bounded the optional Phase-2 kernel working-directory launch input before subprocess creation in local commit `b49e4ae`. `run_kernel_subprocess()` now accepts only a non-empty string/path-like `cwd`, rejects embedded NULs, and enforces a positive 4 KiB default UTF-8 byte ceiling. A multibyte overflow regression proves the marker child does not launch. Focused 1 and full 493 tests passed; `py_compile` and `git diff --check` passed. No patham9 execution, memory write/promotion, rule/trace claim, or live integration.

- [x] Preserve and index the normative SDS with PDF/text hashes and a source sidecar.
- [x] Start Phase 1 with immutable typed evidence/basis records, deterministic basis stamps, canonical local-chart projection, conflict/mass diagnostics, and direct tests.
- [x] Phase-0 baseline freeze (Tier 1): pinned Smokes reference artifact committed at `artifacts/phase0-reference-smokes-55f1751/`. Contains input program hash, executable/kernel hashes, runtime-version manifest, canonical expected output, determinism proof (two byte-identical runs), and reproducibility command. Tier 2 (semantic-failure classification, full corpus coverage, rule/trace identity) remains open and runs concurrently or after the gate.
- [x] Add exact union-by-basis packet algebra with idempotence/commutativity/associativity properties and fail-closed partial/unknown overlap handling. Completed in two slices: exact duplicate deduplication/conflict rejection, then optional reviewed `EvidenceBasis` metadata enforcement requiring complete unique metadata, rejecting token overlap across distinct bases, and refusing multi-basis merges containing `UNKNOWN` units. Verification: focused 14 tests; full 454 tests; `git diff --check` passed.
- [x] Add typed `PiContext`, `ChartPolicy`/`PiChart`, immutable snapshots, fingerprints, JSON schemas, beta round-trip, and prior-cycling tests. Completed through local commits `9aed63a`, `66a4739`, `463310b`, `213d1f8`, `9f4ce4d`, and `e7073cc`; full suite passed 470 tests after completion.
- [x] Close chart-to-snapshot provenance before Phase-2 compilation in local commit `820eed4`. `build_pi_chart()` now requires a validated `EvidenceSnapshot`, rejects context mismatch and selected packet IDs absent from that snapshot, records the snapshot fingerprint on `PiChart`, and includes it in chart identity so changed evidence content cannot reuse a compiled chart artifact under the same logical snapshot ID. Verification: focused 32 tests; full 473 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-13 07:00 PDT / 14:00 UTC.
- [x] Add compatibility adapters that explicitly label `ec_projected_stv()` as `adapter-weighted-v1` without changing serialized outputs. `EC_PROJECTED_STV_POLICY_ID` plus function introspection metadata make the legacy boundary explicit while regression coverage proves result dictionaries do not gain a new field. Local commit `8b4ac1d`; full suite passed 470 tests; `git diff --check` passed.
- [x] Phase 2: isolated episode compiler, legacy kernel backend, result validator,
  manifest, and exact replay. The final boundary now validates semantic replay
  directly from a bounded `KernelProcessCapture`, requiring successful exit,
  empty stderr, and exactly one complete stdout result record before comparing
  the compiler-bound result digest. Focused and full 664-test verification
  passed with repository-local `git diff --check` (2026-08-04 13:03 PDT /
  20:03 UTC); local commit `453a83b`. General rule/trace identity remains a separately bounded later
  phase; runtime invocation, promotion/write, live integration, dependencies,
  paid compute, and remote actions remain closed.
- [x] Bind a selected result atom to its bounded Phase-2 process capture before manifest construction. `validate_kernel_capture_result()` now rejects nonzero exit, any stderr, and result atoms absent from stdout, then closes accepted values through the typed stamp/evidence validator. Local commit `b2be8c7`; focused 1 and full 500 tests passed, plus `py_compile` and `git diff --check`. This does not yet construct/persist the end-to-end manifest or identify rules/traces.
- [x] Bound the Phase-2 kernel executable argument vector before launch. `run_kernel_subprocess()` now enforces a positive 16 KiB default over the complete UTF-8 argv and rejects NUL-bearing arguments before invoking the OS. Local commit `c04bfaa`; focused 2 and full 492 tests passed; `py_compile` and `git diff --check` passed. The runner remains shell-free and non-live; this does not establish runtime/rule/trace identity or authorize promotion.
- [x] Added deterministic bounded legacy-kernel query-program assembly in local commits `e0e2c16` and `9dc338b`. `assemble_legacy_kernel_query_program()` inserts immutable compiler-emitted Sentences and one canonical declarative query into fixed stock patham9 `PLN` import/init/query controls; callers cannot inject rules or executable program fragments. Positive limits, a 10,000-step ceiling, a 100,000-entry ceiling for each queue, and total program-size cap fail closed. Focused 47 tests and full 488 tests passed; `py_compile` and `git diff --check` passed. Kernel subprocess/capture, trace/rule attribution, promotion/write, and live integration remain open.
- [x] Started Phase 2 with a pure deterministic episode-input compiler. `compile_episode_inputs()` validates chart/snapshot identity, exact packet and packet-derived-basis closure, ACTIVE/context boundaries, and rejects extra/missing inputs; it assigns deterministic basis stamps and emits canonical-projection patham9 `Sentence` atoms plus immutable `KernelSentenceMeta` sidecars. Focused 34 tests and full 475 tests passed; `py_compile` and `git diff --check` passed. Runtime execution, generated rule/program assembly, manifest persistence, result validation, and replay remain deferred.
- [x] Added immutable checksummed persistence for exact `CompiledEpisodeInputs` replay inputs. The create-once v1 artifact stores chart/snapshot fingerprints, the complete stamp map, generated Sentence atoms, canonical projection records, and provenance sidecars. Loading revalidates the outer checksum and inner sentence/stamp/basis invariants, so a recomputed envelope cannot hide atom or mapping drift. Focused 36 tests and full 477 tests passed; `py_compile` and `git diff --check` passed. This is not yet a complete runtime episode manifest and invokes no kernel.
- [x] Added the first Phase-2 kernel-result validation boundary. `validate_kernel_result()` parses one bounded patham9 `((stv S C) (stamps...))` atom, rejects malformed/injected output, nonfinite or out-of-range truth values, noncanonical/duplicate stamps, and stamps absent from the compiled episode map. `ValidatedKernelResult` binds canonical query, episode/chart identity, exact evidence-basis provenance, and a semantic digest without granting promotion or rule identity. Focused 41 tests and full 482 tests passed; `py_compile` and `git diff --check` passed. Committed locally as `cc6f4d4`. Manifest/runtime/trace/replay remain open.
- [x] Persist validated Phase-2 kernel results as immutable checksummed v1 JSON artifacts. `write_validated_kernel_result()` is create-once; `read_validated_kernel_result()` rejects schema/checksum/typed-content drift and requires episode/chart identity plus exact stamp-to-basis closure against the supplied immutable `CompiledEpisodeInputs`. Focused 43 tests and full 484 tests passed; `py_compile` and `git diff --check` passed; local commit `0e8942d`. This is persisted validated output only: runtime assembly, trace/rule identity, complete manifest, re-execution comparison, promotion, and live integration remain open.
- [x] Added the first exact replay-comparison gate. `validate_exact_kernel_replay()` closes the expected result against immutable compiled inputs, validates a fresh raw result with the bounded result parser, and rejects any semantic digest drift in query, STV, stamps, or evidence bases while accepting harmless numeric/whitespace rendering differences. Local implementation commit `e979d52`; focused 44 tests and full 485 tests passed; `py_compile` and `git diff --check` passed. Kernel execution, runtime/rule/trace identity, promotion, and live integration remain open.
- [x] Added a complete typed SDS section 16.2 `EpisodeManifest` constructor and create-once artifact in local commit `a8858d5`. The manifest binds exact chart/snapshot/compiler/result provenance to the bounded supplied complete program, stamp map, kernel/capability/rule/projection/controller identities, seed, resource budget, timezone-aware run interval, return code, and captured output digests. Program admission requires every compiler-emitted Sentence exactly once; persistence rejects recomputed-checksum typed drift. Focused 46 tests and full 487 tests passed; `py_compile` and `git diff --check` passed. Runtime execution, trace/rule attribution, promotion, and live integration remain open.
- [x] Persist compiler-bound PeTTaChainer TotalMP attribution as a create-once
  checksummed artifact and close reload against the exact supplied typed
  derived-result capture. General decoded runtime traces remain deferred.
- [x] Add a fully rehashed PeTTaChainer manifest adversary for `result_cid`
  drift. The loader rejects a self-consistent manifest whose result link no
  longer matches the supplied admitted result, even while the attribution link
  remains unchanged. Focused and full 601-test verification passed with `git
  diff --check`; local regression commit `a744390` (2026-07-25 15:00 PDT /
  22:00 UTC).
- [x] Add a fully rehashed PeTTaChainer manifest adversary for `contract_cid`
  drift. The loader rejects a self-consistent manifest whose compiler-contract
  link no longer matches the supplied immutable contract. Focused and full
  601-test verification passed with repository-local `git diff --check`
  (2026-07-25 17:00 PDT / 2026-07-26 00:00 UTC); local commit `effcba5`.
- [ ] Later phases: external geodesic controller; proof classes/reversibility; atlas transitions/revision; native backend; curvature/descent; reviewed promotion.

- [x] Added the next typed πPLN Phase-1 evidence-algebra slice in `repos/petta-memory`: immutable `EvidenceContribution`/`EvidenceCapsule` records and exact union-by-basis merge. Identical shared basis contributions are counted once; conflicting weights under the same basis ID fail closed. This implements specification equations 8.1-8.4 without claiming independence, residualizing partial overlap, changing runtime stamps, or touching live OmegaClaw/GoalChainer paths. Verification: focused 11 tests; full 451 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 01:00 PDT / 08:00 UTC.
- [x] Completed the reviewed overlap gate for exact capsule merges. Supplying `EvidenceBasis` metadata now fails closed on missing/duplicate basis records, partial token overlap between distinct basis IDs, and any multi-basis combination containing an `UNKNOWN` independence unit. Property tests cover commutativity and associativity for reviewed disjoint bases; exact shared-basis deduplication provides idempotence. Verification: focused 14 tests; full 454 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 03:00 PDT / 10:00 UTC.

- [x] Added the first explicit packet-to-basis constructor for the typed πPLN nucleus. `evidence_basis_from_packet()` requires an explicit reviewed independence status and justification CID, verifies exact token-metadata closure (rejecting missing, extra, or duplicate token records), collects sorted causal groups, and derives a deterministic basis ID from packet/token provenance without inferring independence from distinct IDs. Focused 16 tests and full 456 tests passed; `git diff --check` passed. Normative provenance: atlas-indexed reversible πPLN SDS sections 8.2-8.4. No runtime/live/write/promotion path invoked.

- [x] Added the first typed semantic-context/chart slice for the normative πPLN Phase-1 nucleus. Immutable `PiContext`, `ChartPolicy`, and `PiChart` records validate semantic guards, versioned policies, canonical parent/packet sets, local priors, and chart identity. `build_pi_chart()` deterministically hashes every SDS section 6.2 mandatory fingerprint field and canonicalizes packet order; tests prove order invariance, prior sensitivity, and fail-closed context ancestry. Focused 18 tests and full 458 tests passed; `git diff --check` passed. Provenance: progress worker, 2026-07-12 07:00 PDT / 14:00 UTC.
- [x] Added immutable evidence snapshots for the Atlas-indexed reversible πPLN Phase-1 model. `EvidenceSnapshot` freezes sorted packet IDs plus context/assumption/ontology versions; `build_evidence_snapshot()` accepts only unique ACTIVE packets matching those versions and computes a packet-order-invariant fingerprint including packet provenance digests. This is a typed, non-live snapshot boundary only: no runtime derive, memory append, inferred-belief promotion, or OmegaClaw/GoalChainer action. Verification: focused 20 tests; full 460 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 09:00 PDT / 16:00 UTC.

- [x] Hardened immutable piPLN snapshot invariants at the persistence boundary. Snapshots now require a non-empty canonical packet set, validate each packet ID, and require a lowercase SHA-256 snapshot fingerprint; a separately checksummed document with an invalid semantic fingerprint fails closed on load. Local implementation commit `213d1f8`; focused model tests passed 24 tests; full unittest discovery passed 464 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 15:00 PDT / 22:00 UTC.

- [x] Added the first content-addressed piPLN snapshot repository/index. `EvidenceSnapshotRepository` stores create-once documents by semantic snapshot fingerprint, validates every discovered document, rejects unexpected entries, filename/fingerprint drift, and duplicate logical snapshot IDs, and provides deterministic listing plus fail-closed ID lookup. Verification: focused model tests passed 26 tests; full unittest discovery passed 466 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 17:00 PDT / 2026-07-13 00:00 UTC.

- [x] Hardened the pure Phase-2 piPLN compiler/runtime-input boundary. `compile_episode_inputs()` now parses and canonicalizes each packet statement as exactly one S-expression data term, recursively rejects MeTTa executable/control heads, and enforces positive sentence-count and aggregate emitted-atom character budgets. `CompiledSentence` reconstruction now derives the only admissible atom from typed canonical term/projection/stamp metadata, so a recomputed outer checksum and sentence digest cannot conceal atom/sidecar drift or executable-term smuggling. Verification: focused 38 tests; full 479 tests; `py_compile`; `git diff --check`. No patham9/PeTTa runtime, derive/query, memory write/promotion, or live OmegaClaw/GoalChainer path. Provenance: progress worker, 2026-07-13 13:00 PDT / 20:00 UTC.
- [x] Bound the optional explicit Phase-2 kernel subprocess environment before launch: validate string mappings, reject process-invalid keys/values, enforce a positive aggregate UTF-8 byte ceiling, and prove rejection occurs before child execution. Full unittest discovery passed 494 tests; no inference, promotion/write, or live integration boundary changed. (2026-07-14)
- [x] Add an opt-in pre-launch SHA-256 identity gate for the Phase-2 kernel executable, with a no-launch mismatch test. Completed 2026-07-14; full suite 495 tests passed. Follow-up: a later isolated runner must close the remaining path replacement/TOCTOU boundary if stronger runtime identity is required.
- [x] Remeasured the post-repair `mm2stmt` and copied `mm2compile` collector rungs under the exact single-import source gate. One canonical fact now converts once and collects once (baseline: two and four), despite the unchanged overlapping `mm2stmt` definition. Local commit `28be231`; focused 94 and full 549 tests, `py_compile`, and `git diff --check` passed. Artifact: `artifacts/pettachainer_repaired_conversion_collection_2026-07-17T0700PDT.json`, SHA-256 `45edecff2d811c8b433e5089aeaf8a1d06b30eeefaa182d3864e77aa66b132d3`. Next: run full repaired `mm2compile`, then retry bounded `compileadd` only if that succeeds; do not apply a second source repair yet.
- [x] Content-addressed captured stdout/stderr for completed isolated PeTTaChainer stages and made complete stream provenance a fail-closed requirement of repaired exact-fact query admission. Fresh real probe: one exact answer, zero unexpected answers; stdout 608,129 bytes SHA-256 `3eafb227...`; stderr 138 bytes SHA-256 `3207c3f2...`. Local commit `468d55a`; focused 106/full 561 tests, `py_compile`, and `git diff --check` passed. Next: classify the content-addressed diagnostics before typed episode-contract/result admission; no promotion/write/upstream/live change.
- [x] Added create-once, checksummed persistence for the non-promoting `PeTTaChainerEpisodeManifest`. The loader reconstructs `EpisodeBudget` and all typed digest/timestamp/classification invariants and rejects contract, derived-result, validator-capture, or runtime-capture provenance drift. Local implementation commit `6bfc31e`; focused regression and full 570 tests passed; `py_compile` and `git diff --check` passed. No promotion/write authorization, upstream repair adoption, or live integration.
- [x] Prevented special-file denial of service at the PeTTaChainer artifact boundary: derived-capture and episode-manifest JSON opens are nonblocking, then require a regular descriptor before bounded reading. A FIFO regression proves immediate rejection. Local implementation commit `e770f5e`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, or live change.
- [x] Preserve the primary PeTTaChainer artifact publication failure across a secondary parent-directory descriptor close failure; retain the secondary diagnostic on the original exception. Local implementation commit `882f3fe`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. No promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Require PeTTaChainer audit-artifact bytes read to equal stable descriptor size; regression simulates internally consistent metadata that disagrees with delivered bytes. Full 572 tests, `py_compile`, and `git diff --check` passed. (2026-07-19 11:00 PDT)
- [x] Preserve a primary PeTTaChainer artifact stream read/metadata failure across secondary stream-close failure after descriptor ownership transfer; propagate stream-close failure normally when the read otherwise succeeded. Focused 3 and full 575 tests, `py_compile`, and `git diff --check` passed. (2026-07-19 15:00 PDT)
- [x] PeTTaChainer checksummed artifact admission now rejects a descriptor whose declared regular-file size already exceeds the byte ceiling before constructing a stream or reading payload bytes. Local implementation commit `8c39ad3`; focused regression and full 576 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] Reject PeTTaChainer audit artifacts whose mode, owner, or group changes during the bounded descriptor read. Local implementation commit `6bcc26c`; focused regression and full 577 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change. (2026-07-19 19:00 PDT)
- [x] Reject group- or world-writable PeTTaChainer checksummed JSON audit artifacts before payload read. The writer already publishes owner-only files; the loader now fails closed on broader write authority. Focused regression and full 578 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream/remote, paid-compute, or live integration action. (2026-07-19 21:00 PDT)
- [x] Reject symlinked parent directories during create-once PeTTaChainer artifact publication. The durable writer now opens the supplied destination parent with `O_NOFOLLOW` where available, so a symlink cannot redirect the derived-capture or episode-manifest artifact into another directory. Local implementation commit `57ba221`; focused 1 and full 579 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Reject broadly writable PeTTaChainer audit-artifact publication parents before creating the destination leaf. Regression verifies a `0770` parent fails closed and remains empty. Local implementation commit `893e837`; focused 1 and full 580 tests passed, plus `py_compile` and `git diff --check`. No runtime invocation, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Detect parent-directory permission drift during PeTTaChainer create-once audit publication via a final check on the anchored descriptor; retain a file-synced artifact on rejection to preserve create-once semantics (`93e8fa0`; 581 tests).
- [x] Reject PeTTaChainer artifact publication parent metadata drift. The durable create-once writer now requires stable device, inode, mode, link count, owner, and group identity across publication, closing ownership/group drift before directory fsync. Local implementation commit `b53e7bb`; focused 2 and full 582 tests passed, plus `py_compile` and `git diff --check`. No promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Anchor checksummed PeTTaChainer artifact reads to a non-symlinked parent directory descriptor and open the basename relative to it; reject broadly writable parents before admission. Commit `7eed3f6`; full 584 tests and `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Close the PeTTaChainer artifact parent descriptor when initial `fstat` fails, while retaining the primary admission error and secondary close provenance. Local implementation commit `c50eb47`; focused 1 and full 589 tests passed, plus `py_compile` and `git diff --check`. Provenance: progress worker, 2026-07-20 13:00 PDT / 20:00 UTC; no runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Close regression coverage for a final parent-metadata revalidation failure combined with parent-descriptor close failure during PeTTaChainer audit-artifact admission. The final metadata error remains primary and the cleanup failure is retained as a diagnostic note. Local commit `06e57c3`; focused 1 and full 591 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Cover the combined PeTTaChainer artifact-admission path where final trusted-parent metadata drift is detected and closing the parent descriptor also fails. The regression preserves the actionable drift rejection and retains the cleanup failure in `__notes__`; focused 1 and full 592 tests passed, plus `py_compile` and `git diff --check`.
- [x] Cover the successful PeTTaChainer artifact-read path when closing the trusted parent descriptor fails. The loader propagates the close error rather than returning decoded JSON; local commit `5f4d675`; focused 1 and full 593 tests passed, plus `py_compile` and `git diff --check`. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Close the combined pre-stream artifact rejection + leaf descriptor close failure + parent descriptor close failure regression; preserve the primary rejection with both cleanup diagnostics (`664d592`, 594 tests).
- [x] Preserve primary PeTTaChainer create-once publication failures across descriptor-backed text-stream close failures, while retaining a successfully file-synced artifact when close alone fails (`ff313b6`; focused 1 and full 596 tests passed; `py_compile`; `git diff --check`).
- [x] Delivered a systematic 19-page, outside-reader-facing PDF evaluating `metta-attention` and its integration with petta-memory, OmegaClaw, OmegaSelf, and the emotion framework. The ASCII-safe LaTeX incorporates the pinned source assessment, two-strata C1--C5 synthesis, Recoverability Invariant, governed emotion modulation, OmegaSelf background sentinels, regenerative goals, adapter contracts, risks, decision matrix, and staged falsifiable experiments. `tectonic` compiled successfully with no overfull boxes; all 19 rendered pages were visually checked; `git diff --check` passed. Evidence: `docs/metta_attention_omegaclaw_integration.tex` SHA-256 `ac06d052e2ec797e1d48566151de451479714201b2c49f0bc121e3568d876782`; PDF SHA-256 `1859d101704dfc5f03732363d8ace0d6588be279db3aa8289d2dd4f7a20c305c`.
- [x] Route the legacy pi-PLN episode-manifest, validated-result, evidence-snapshot, and compiled-input writers through the hardened descriptor-anchored create-once publication primitive. Commit `fb7a71d`; full 597 tests and `git diff --check` passed (2026-07-21).
- [x] Add public-boundary regressions proving all four legacy pi-PLN writers reject a symlinked destination parent without creating an artifact in the symlink target. Local commit `fdf199d`; focused 4 and full 597 tests passed, plus `git diff --check` (2026-07-21 19:00 PDT / 2026-07-22 02:00 UTC). Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Close hard-link alias admission for the four legacy pi-PLN audit artifacts. Public regressions now require episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs to fail closed when an otherwise valid checksummed artifact has more than one filesystem link. Local implementation commit `21ff1ce`; focused 4 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Closed unsafe-parent admission coverage across the four legacy pi-PLN audit loaders. Existing episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs are rejected when their parent is group-writable. Local regression commit `57b2e66`; focused 4 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Close current-user ownership enforcement at every public legacy pi-PLN persistence route. Added reusable regressions proving evidence snapshots, compiled episode inputs, and episode manifests reject foreign-owned parents/artifacts and refuse publication into a foreign-owned parent, complementing validated-result coverage. Local commit `b45839b`; focused 3 and full 597 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Closed late parent-directory drift at the legacy pi-PLN audit boundary. A public evidence-snapshot load now has a constructed regression in which the parent inode changes between initial admission and final revalidation; the artifact is rejected before typed reconstruction. Local regression commit `48d3e49`; focused 1 and full 598 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Add the first Phase-1 clean-room capture/reload regression without adding an archive schema or accessor. Existing compiled-input, validated-result, and episode-manifest artifacts are create-once persisted and admitted in two isolated directories; exact replay answers the frozen query and all three semantic identities remain stable. A manifest presented as compiled inputs and a result presented against a new-run compiled descriptor both fail closed. Local commit `19a6528`; focused 1 and full 600 tests passed; `git diff --check` passed. This advances but does not complete the Phase-1 gate: next combine the admitted Phase-0 reference-manifest class and expand the bounded stale/malformed provenance matrix. No runtime, promotion/write, upstream, remote, paid-compute, or live-integration change.
- [x] Extend the Phase-1 clean-room gate across the frozen Phase-0 replay-anchor class. Two isolated reload cycles now admit identical source/output commitments, and a stale source is rejected by the existing bounded manifest admission contract. Focused 1 and full 600 tests passed; `git diff --check` passed. Next: cover the current PeTTaChainer runtime descriptor/capture class and duplicate-anchor/cross-run matrix without adding a schema.
- [x] Extend the Phase-1 clean-room gate with a recomputed-checksum stale-descriptor attack and explicit provenance-class separation. A top-level episode substitution retaining the frozen stamp/sentence sidecars is rejected during typed reconstruction, while archived Phase-0, captured-derived, and post-reload assertion identities remain distinct. Local commit `535b1db`; focused 1 and full 600 tests passed; `git diff --check` passed. No runtime or live boundary opened.
- [x] Close cross-artifact provenance during Phase-1 clean-room reload. `read_episode_manifest(..., compiled=..., result=...)` now verifies episode/stamp-map/result identity across independently checksummed artifacts and rejects cross-run descriptor/result collisions. Local commit `0bb6d8b`; focused 1 and full 600 tests passed; `git diff --check` passed. No runtime invocation, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Closed Phase-1 clean-room episode-manifest reload against supplied compiled chart and context identities, not only episode/stamp-map identity. Local commit `546318b`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-22 21:00 PDT / 2026-07-23 04:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Closed the Phase-2 archived manifest against its bounded process capture on reload. `read_episode_manifest(..., capture=...)` now requires exact return-code, stdout/stderr content commitments, and the capture's delivered-program commitment; output and program drift regressions fail closed. Local commit `10afdf1`; focused 1 and full 600 tests passed; `git diff --check` passed (2026-07-23 15:00 PDT / 22:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Close the typed boundary for bounded `KernelProcessCapture` provenance before clean-room manifest admission. Commit `09e774d` rejects empty/non-text argv, boolean/non-integer status, byte/non-text streams, and malformed optional program commitments at construction. Focused 1 and full 601 tests passed; `git diff --check` passed. No runtime, promotion/write, upstream/remote, paid-compute, or live-integration action.
- [x] Closed ambiguous raw kernel-result capture admission. `validate_kernel_capture_result()` now accepts one result only when it occurs exactly once as a complete stdout line; substring-only and duplicate occurrences fail closed. Local implementation commit `f3882ae`; focused 2 and full 601 tests passed; `git diff --check` passed (2026-07-23 23:00 PDT / 2026-07-24 06:00 UTC). No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Make the unique captured kernel-result line byte-exact rather than
  whitespace-normalized. `validate_kernel_capture_result()` now rejects leading
  or trailing whitespace around an otherwise valid result atom; focused 1 and
  full 601 tests passed, plus `git diff --check`; local commit `bf27ee5`.
  Provenance: progress worker,
  2026-07-24 03:00 PDT / 10:00 UTC. No runtime, promotion/write, upstream,
  remote, paid-compute, or live-integration boundary changed.
- [x] Require literal LF framing for captured kernel-result records.
  `validate_kernel_capture_result()` no longer uses Unicode-aware
  `str.splitlines()`, so vertical-tab and U+2028 separators cannot manufacture
  an apparent complete record. Focused 1 and full 601 tests passed with
  `git diff --check`; local implementation commit `f3c569f`. Provenance:
  progress worker, 2026-07-24 05:00 PDT / 12:00 UTC. No runtime,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Add explicit bounded rule attribution for the admitted one-rule
  PeTTaChainer path. `build_pettachainer_rule_attribution()` content-addresses
  TotalMP, exact rule/fact sentence and proof identities, stamps, evidence
  bases, and the typed result identity, while requiring
  `runtime_trace_decoded=False`. Local commit `e3a0d37`; focused 1 and full 601
  tests passed, plus `git diff --check` (2026-07-24 11:00 PDT / 18:00 UTC).
  General runtime trace decoding and promotion/write/live gates remain closed.
- [x] Harden the compiler-bound rule-attribution constructor against
  correctly rehashed malformed provenance collections. Rule and fact stamps
  and evidence bases must each be non-empty, sorted, unique tuples with
  non-negative integer stamps and non-blank string basis IDs. Focused 1 and
  full 601 tests passed, plus `git diff --check`; local commit `39d5975`
  (2026-07-24 13:00 PDT / 20:00 UTC). No runtime, promotion/write,
  upstream/remote action, paid
  compute, or live integration.
- [x] Close compiler-bound PeTTaChainer rule attribution cardinality: each
  rule/fact stamp must have exactly one retained evidence-basis ID. A
  correctly rehashed mismatched tuple now fails closed. Local implementation
  commit `e826c4e`; focused and full 601-test verification passed, plus `git
  diff --check` (2026-07-24 15:00 PDT / 22:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Reject mutable list-backed stamp/evidence collections in typed
  PeTTaChainer derived-result captures even when their digest is correctly
  recomputed (`9f34631`; focused plus full 601 tests and `git diff --check`,
  2026-07-24 19:00 PDT / 2026-07-25 02:00 UTC).
- [x] Require distinct compiler identities for the fact and rule in typed
  PeTTaChainer one-rule results and attributions. Correctly rehashed adversary
  records that reuse the fact sentence digest/proof ID as the rule now fail
  closed. Local implementation commit `19fb7a9`; focused and full 601-test
  verification passed with `git diff
  --check` (2026-07-24 23:00 PDT / 2026-07-25 06:00 UTC). No runtime,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Bind compiler-bound PeTTaChainer TotalMP attribution into episode-manifest
  v2. The manifest commits `attribution_cid`; build/reload require exact
  derivability from the supplied typed result, and cross-result pairing fails
  closed. Local implementation commit `9ef4fef`; focused and full 601-test
  verification passed with `git diff
  --check` (2026-07-25 09:02 PDT / 16:02 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Add a fully rehashed PeTTaChainer manifest adversary for
  `validator_capture_cid` drift. The loader rejects a self-consistent manifest
  whose validator-stage stream identity no longer matches the validator
  capture nested in the supplied admitted result. Focused and full 601-test
  verification passed with repository-local `git diff --check`; local
  regression commit `947367a` (2026-07-25 19:00 PDT / 2026-07-26 02:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.
- [x] Add the symmetric fully rehashed PeTTaChainer manifest adversary for
  `runtime_capture_cid` drift. Reload rejects a self-consistent manifest whose
  runtime-stage stream identity differs from the runtime capture nested in the
  supplied admitted result. Focused and full 601-test verification passed with
  repository-local `git diff --check`; local regression commit `bc2338c`
  (2026-07-25 21:00 PDT / 2026-07-26 04:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Add a fully rehashed PeTTaChainer manifest adversary for `episode_id`
  drift. Reload rejects a self-consistent artifact whose episode anchor no
  longer matches the supplied compiler contract. Local regression commit
  `47022b3`; focused and full verification passed with repository-local `git
  diff --check` (2026-07-26 01:00 PDT / 08:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Add a fully rehashed PeTTaChainer manifest adversary for
  `result_classification`. Reload rejects a self-consistent artifact that
  relabels the compiler-bound one-rule result as runtime-trace-derived at the
  typed classification invariant. Focused and full 601-test verification
  passed with repository-local `git diff --check`; local regression commit
  `b21d1be` (2026-07-26 05:00 PDT / 12:00 UTC). No runtime invocation, promotion/write, upstream/remote action,
  paid compute, or live integration.
- [x] 2026-07-26: Run one provider-free production-path usability gate:
  ingest → index → retrieve → local inference → restart → reproduce, then an
  isolated read-only private canary. Acceptance: semantic patham9/PLN result
  passes, restart retrieval is byte-identical, and the journal hash is unchanged
  by canary reads. Evidence:
  `repos/petta-memory/scripts/provider_free_usability_gate.sh` and
  `experiments/20260726T185632Z-provider-free-usability-roundtrip-retry/`.
  No live agent integration, promotion, or autonomous write was enabled.
- [x] Reject dangling output-directory symlinks in the provider-free usability
  gate before `mkdir`, preserving the link and leaving its absent target
  untouched. Focused 2-test and full 603-test verification passed with
  repository-local `git diff --check` (2026-07-27 01:00 PDT / 08:00 UTC).
- [x] Close the provider-free usability gate's dangling-output-symlink case.
  The create-new output boundary now rejects lexical path occupancy (`-e ||
  -L`) before fixture ingestion or inference; regression coverage proves exit
  2, exact symlink preservation, and no target creation. Focused 2 and full
  603-test verification passed with repository-local `git diff --check`;
  local regression commit `63f9a2e` (2026-07-27 01:00 PDT / 08:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  dependency change, or live integration.
- [x] Reject symlinked parent components at the provider-free usability
  gate's create-new output boundary, with a regression proving the alias target
  remains empty. Focused 3 and full 604 tests passed, plus repository-local
  `git diff --check`; local commit `c7811d2`
  (2026-07-27 03:00 PDT / 10:00 UTC).
- [x] Make provider-free usability outputs private independently of the
  caller's ambient umask. The gate now sets `umask 077`; a regression launches
  it under `umask 000` and verifies the new directory is `0700` and every
  generated file is `0600`. Focused 4-test and full 605-test verification plus
  repository-local `git diff --check` passed; local commit `651a41a`
  (2026-07-27 05:04 PDT / 12:04 UTC). No canonical memory write/promotion,
  live integration, paid compute, dependency change, or remote action.
- [x] Make the provider-free usability artifact state its non-live authority:
  `summary.json` now records `canary_mode: read-only`,
  `autonomous_writes_enabled: false`, and `promotion_authorized: false`.
  Focused 5-test and full 606-test verification passed with repository-local
  `git diff --check`; local commit `81e13d7` (2026-07-27 11:00 PDT / 18:00
  UTC). No promotion/write, live integration, paid compute, dependency change,
  or remote action.
- [x] Semantically close the frozen usability inference artifact: parse
  `inference.json` as an unambiguous UTF-8 JSON object and require its status
  to equal the admitted passed summary claim. A fully rehashed failed result
  fails closed. Focused 7-test and full 613-test verification passed with
  repository-local `git diff --check`; local commit `ff3b552` (2026-07-27
  23:00 PDT / 2026-07-28 06:00 UTC). Promotion/write, runtime invocation,
  live integration, dependency changes, and remote actions remain closed.
- [x] Close the frozen usability inference result to its exact producer member
  sets at the top level and within `classification` and `semantic_markers`.
  Fully rehashed undeclared promotion/live-integration authority fields now
  fail closed. Focused 11-test and full 617-test verification passed with
  repository-local `git diff --check`; local commit `15b11ce` (2026-07-28
  05:05 PDT / 12:05 UTC).
  Runtime invocation, promotion/write, live integration, dependency changes,
  and remote actions remain closed.
- [x] Bind frozen usability inference admission to the exact
  `patham9-pln-handoff-derivation-smoke` classifier and its clean success
  diagnostics. A fully rehashed inference artifact using an unreviewed
  classifier identity now fails closed. Focused 12-test and full 618-test
  verification passed with repository-local `git diff --check`; local commit
  `eb90064` (2026-07-28 07:00 PDT / 14:00 UTC). Runtime invocation, promotion/write, live
  integration, dependency changes, and remote actions remain closed.
- [x] Close undeclared authority inside the frozen usability inference's
  provenance-bearing source item. Admission now requires the exact producer
  member set; a fully rehashed nested `promotion_authorized` field fails
  closed. Focused 20-test and full 626-test verification passed with
  repository-local `git diff --check`; local commit `c4dcb95` (2026-07-28
  21:00 PDT / 2026-07-29 04:00 UTC). Runtime invocation, promotion/write, live integration,
  dependency changes, and remote actions remain closed.
- [x] Bind the frozen provider-free usability source's nested pi-PLN
  extension to its actual non-live producer behavior. Admission requires
  context selection to remain not-run with no generated contexts, an empty
  contextual EvidencePacket set, and deferred EC projection; a fully rehashed
  claim that contexts were admitted fails closed. Focused 23-test and full
  629-test verification passed with repository-local `git diff --check`;
  local commit `a6edd1b` (2026-07-29 03:00 PDT / 10:00 UTC). Runtime invocation,
  promotion/write,
  live integration, dependency changes, and remote actions remain closed.
- [x] Bind frozen usability diagnostics to captured runtime evidence.
  Admission requires every semantic diagnostic line to occur in one of the
  bounded stdout/stderr tails; a fully rehashed invented diagnostic fails
  closed. Focused 29-test and full 635-test verification passed with
  repository-local `git diff --check`; local commit `e9c6fc3` (2026-07-29
  15:00 PDT / 22:00 UTC).
  Runtime invocation, promotion/write, live integration, dependency changes,
  paid compute, and remote actions remain closed.
- [x] Reproduce frozen usability semantic marker counts from captured runtime
  evidence. Admission now independently counts successful, failed, and error
  markers in the bounded stdout/stderr tails instead of trusting the
  integrity-bound semantic count fields alone. A fully rehashed claimed pass
  with no observed pass marker fails closed. Focused 30-test and full 636-test
  verification passed with repository-local `git diff --check`; local commit
  `338c2aa` (2026-07-29 17:00 PDT / 2026-07-30 00:00 UTC). Runtime invocation,
  promotion/write, live integration, dependency changes, and remote actions
  remain closed.
- [x] Close successful-marker cardinality in the frozen Phase-0 replay anchor.
  Admission now requires exactly one semantic-result occurrence and exactly
  one `(Passed: #t)` occurrence; a fully rehashed duplicate-pass capture fails
  closed. Focused reload and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 03:01 PDT / 10:01 UTC);
  local commit `08c67a6`.
  Runtime invocation, promotion/write, live integration, dependency changes,
  paid compute, and remote actions remain closed.
- [x] Close fresh Phase-0 replay to the digest-pinned runner's executable-path
  shape. Replay admission now requires `argv[0]` to be absolute and normalized;
  an otherwise valid manually reconstructed relative-path capture fails
  closed. Focused and full 639-test verification passed with repository-local
  `git diff --check` (2026-07-30 17:00 PDT / 2026-07-31 00:00 UTC); local
  commit `8082999`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.
- [x] Close typed raw captures against non-UTF-8 surrogate-bearing text.
  `KernelProcessCapture` now rejects unencodable argv, stdout/stderr, cwd, and
  environment strings before hashing or Phase-0 replay can encounter an
  incidental `UnicodeEncodeError`. Focused 2-test and full 641-test
  verification passed with repository-local `git diff --check`; local commit
  `af1ec4d` (2026-07-31 03:00 PDT / 10:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close the actual bounded subprocess launch boundary against non-UTF-8
  program, argv, cwd, and explicit-environment text. Invalid inputs now fail
  with field-specific `ValueError`s before launch, consistent with typed raw
  capture validation. Five focused tests, the full 641-test suite, and
  repository-local `git diff --check` passed (2026-07-31 05:00 PDT / 12:00
  UTC); local commit `ed4d68d`. Runtime promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.
- [x] Complete symmetric UTF-8 regression coverage for process-environment
  keys and values at both `KernelProcessCapture` reconstruction and
  `run_kernel_subprocess()` pre-launch validation. Marker-backed runner
  coverage proves a surrogate-bearing key fails before spawn. Focused 2-test
  and full 641-test verification passed with repository-local `git diff
  --check` (2026-07-31 07:01 PDT / 14:01 UTC); local commit `12acaea`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the bounded kernel working-directory provenance boundary. The
  runner now resolves an optional `cwd` to the exact absolute directory used
  for launch, rechecks its framed byte budget after resolution, and records
  that canonical path; typed captures reject relative or non-normalized cwd
  claims. Focused 2-test and full 642-test verification passed with
  repository-local `git diff --check` (2026-07-31 11:00 PDT / 18:00 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed; local commit `ef5136c`.
- [x] Close the bounded kernel argv container boundary. Bare text/bytes are no
  longer silently expanded into character/integer arguments, and a
  non-iterable now fails through the public typed `ValueError` contract.
  Focused and full 643-test verification plus repository-local `git diff
  --check` passed (2026-07-31 17:00 PDT / 2026-08-01 00:00 UTC); local commit
  `a535e9a`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Bound argv iterable consumption before kernel launch. Argument entries
  are now validated and UTF-8/terminator bytes counted incrementally, so even
  an unbounded iterable reaches the configured byte ceiling without unlimited
  tuple materialization. Focused and full 643-test verification plus
  repository-local `git diff --check` passed (2026-07-31 19:00 PDT /
  2026-08-01 02:00 UTC); local commit `3818a3b`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the bounded kernel argv enumeration exception boundary. A
  caller-controlled iterator that fails after yielding an entry now raises a
  typed `ValueError` with the iterator exception retained as cause, before
  process launch. Focused and full 643-test verification passed with
  repository-local `git diff --check` (2026-07-31 21:00 PDT / 2026-08-01
  04:00 UTC); local commit `9e1ee9c`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close bounded kernel environment traversal failures. Exceptions from a
  caller-supplied mapping's `items()` iterator now fail through the runner's
  typed `ValueError` contract before child launch, retaining the original
  exception as cause. A marker-backed focused regression, the full 643-test
  suite, and repository-local `git diff --check` passed (2026-07-31 23:00 PDT
  / 2026-08-01 06:00 UTC); local commit `10ab2fd`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed environment-item shape at the bounded kernel launch
  boundary. An untrusted `Mapping.items()` iterator yielding a non-pair now
  fails with a chained typed `ValueError` before launch instead of leaking its
  unpacking exception. Focused 1-test and full 643-test verification passed
  with repository-local `git diff --check` (2026-08-01 01:02 PDT / 08:02
  UTC); local commit `bfad0a9`. Runtime invocation, promotion/write, live integration, dependencies,
  paid compute, and remote actions remain closed.
- [x] Close scalar environment-item admission at the bounded kernel launch
  boundary. Environment items must now be exact two-element tuples, so a
  hostile mapping cannot have a two-character scalar silently interpreted as
  `KEY=VALUE`. Focused and full 643-test verification passed with
  repository-local `git diff --check` (2026-08-01 03:00 PDT / 10:00 UTC);
  local commit `776efe9`. Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close the remaining documented subprocess-construction exception class
  at the bounded kernel launch boundary. `subprocess.SubprocessError` now
  follows the same chained typed `ValueError` contract as `OSError`; focused
  2-test and full 644-test verification plus repository-local `git diff
  --check` passed (2026-08-01 07:01 PDT / 14:01 UTC); local commit `b7322fe`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the bounded kernel output-capture exception boundary. OS-level
  stdout/stderr read failures now terminate the isolated process group and
  fail through the runner's typed `ValueError` contract with the original
  exception retained as cause. Focused 1-test and full 645-test verification
  passed with repository-local `git diff --check` (2026-08-01 09:00 PDT /
  16:00 UTC); local commit `43152c2`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close the bounded kernel output-reader exception boundary. Any ordinary
  exception raised while reading or assembling stdout/stderr is now captured,
  terminates the process group, and fails through the runner's typed
  `ValueError` contract with its original cause. A `RuntimeError` regression,
  the full 645-test suite, and repository-local `git diff --check` passed
  (2026-08-02 20:11 PDT / 2026-08-03 03:11 UTC); local commit `9546ad1`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the bounded kernel stdin-writer exception boundary. Any ordinary
  exception raised while writing, flushing, or closing program stdin is now
  retained and returned as the existing typed incomplete-delivery failure,
  preventing a worker-thread exception from producing a capture. Focused
  2-test and full 646-test verification passed with repository-local `git
  diff --check` (2026-08-02 21:21 PDT / 2026-08-03 04:21 UTC); local commit
  `cf31b9d`. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.
- [x] Close the bounded kernel timeout-reap exception boundary. If the direct
  process times out and the mandatory post-SIGKILL `wait()` then fails, the
  runner now raises `ValueError("kernel subprocess timeout cleanup failed")`
  with the cleanup failure retained as its cause. Focused and full 648-test
  verification passed with repository-local `git diff --check` (2026-08-03
  01:00 PDT / 08:00 UTC); local commit `80dc2fa`. Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close the bounded kernel process-group cleanup exception boundary.
  Ordinary `killpg()` failures are now retained and reported through
  `ValueError("kernel subprocess process-group cleanup failed")` after stream
  finalization, rather than escaping a worker thread or allowing a capture.
  Focused and full 650-test verification passed with repository-local `git
  diff --check` (2026-08-03 05:00 PDT / 12:00 UTC); local implementation
  commit `aa4304b`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close the bounded kernel worker cleanup exception boundary. Unexpected
  writer/reader `join()` failures now become
  `ValueError("kernel subprocess worker cleanup failed")` with the original
  cause, while every worker receives a join attempt and stdout/stderr still
  receive close attempts. Focused 1-test and full 651-test verification passed
  with repository-local `git diff --check` (2026-08-03 07:01 PDT / 14:01 UTC);
  local commit `6ac5199`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close the bounded kernel capture-worker startup exception boundary.
  A worker `start()` failure after child launch now becomes a typed
  `ValueError`, after process-group termination/reaping, joining only workers
  that actually started, and closing both captured streams. Focused 3-test and
  full 652-test verification passed with repository-local `git diff --check`
  (2026-08-03 09:00 PDT / 16:00 UTC); local commit `3626e60`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Close the bounded kernel capture-worker construction boundary. A thread
  constructor failure after child launch now kills and reaps the child,
  attempts stdin/stdout/stderr closure, and returns a typed construction or
  construction-cleanup `ValueError` with the original cause. Focused 2-test
  and full 654-test verification passed with repository-local `git diff
  --check` (2026-08-03 11:01 PDT / 18:01 UTC); local commit `55435a7`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close the bounded kernel stdin pipe after capture-worker startup failure.
  Post-launch finalization now closes all three subprocess pipes, including the
  stdin pipe whose writer may never have started. A focused regression and the
  full 654-test suite passed with repository-local `git diff --check`
  (2026-08-03 13:00 PDT / 20:00 UTC); local commit `0ae13bc`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Preserve process-group termination failure during bounded kernel worker
  construction cleanup. The runner now prioritizes the cleanup failure that
  could leave a child alive, while still attempting direct-process reap and
  closure of all three pipes. Focused 1-test and full 655-test verification
  passed with repository-local `git diff --check` (2026-08-03 15:00 PDT /
  22:00 UTC); local commit `15f5335`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Preserve process-group termination failure on the ordinary kernel wait
  failure path. The runner now defers normalization of the wait error until
  after finalization, allowing a recorded kill failure to retain cleanup
  priority. Focused 2-test and full 656-test verification passed with
  repository-local `git diff --check` (2026-08-03 17:01 PDT / 2026-08-04
  00:01 UTC); local commit `98e1f23`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Preserve timeout-path process-group termination failures. Timeout and
  timeout-cleanup exceptions are now retained until shared subprocess
  finalization completes, allowing the existing process-group cleanup error to
  report a potentially surviving child/descendant first. Focused 3-test and
  full 657-test verification passed with repository-local `git diff --check`
  (2026-08-03 19:00 PDT / 2026-08-04 02:00 UTC); local commit `afa955e`. Runtime result admission,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Regression-close requested-pipe process-group termination failures. A
  mocked malformed construction now proves a failed `killpg` is retained as
  the cause of `ValueError("kernel subprocess pipe validation cleanup failed")`
  without skipping direct-process reap or supplied-stream closure. Focused 86
  and full 661 tests passed with repository-local `git diff --check`
  (2026-08-04 03:00 PDT / 10:00 UTC); local commit `fc989fd`. Runtime,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Regression-close requested-pipe validation reap failures. A mocked
  malformed process construction now proves that an unexpected `wait()`
  failure is preserved as the cause of
  `ValueError("kernel subprocess pipe validation cleanup failed")`, without
  skipping closure of the remaining supplied streams. Focused 1-test and full
  662-test verification passed with repository-local `git diff --check`
  (2026-08-04 05:01 PDT / 12:01 UTC); local commit `d3f0851`. Runtime
  invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Complete and jointly validate malformed requested-pipe cleanup coverage
  for process-group kill and direct-process reap failures. The regressions
  prove first-failure preservation plus continued reap/stream-close attempts;
  focused 2-test and full 662-test suites passed with repository-local `git
  diff --check` (2026-08-04 07:01 PDT / 14:01 UTC), covering local commits
  `fc989fd` and `d3f0851`. Return to the bounded Phase-1 semantic
  capture/reload gate rather than extending this hardening branch. Runtime
  invocation, promotion/write, live integration, dependencies, paid compute,
  and remote actions remain closed.
- [x] Regression-close the already-exited requested-pipe cleanup path. A
  mocked malformed process construction now proves that `ProcessLookupError`
  during process-group kill remains benign while the runner still reaps the
  child, closes every supplied stream, and raises the primary typed
  missing-pipe error. Focused 1-test and full 663-test verification passed with
  repository-local `git diff --check` (2026-08-04 09:00 PDT / 16:00 UTC);
  local commit `2d3af71`. Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Persist and reload the bounded Phase-2 raw kernel capture. Added the
  create-once `petta-memory-kernel-process-capture-v1` document, complete typed
  reconstruction, checksum/canonical-environment adversaries, and integration
  into both clean-room reload cycles. Focused 2-test and full 664-test suites
  passed with repository-local `git diff --check` (2026-08-04 11:00 PDT / 18:00
  UTC); local commit `b54a935`. Runtime invocation, result promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed dependency handling at the episode-manifest construction
  boundary. `build_episode_manifest()` now requires typed compiled inputs,
  validated result, pi chart, evidence snapshot, and episode budget before any
  field access; five adversarial cases prove stable `ValueError` failures.
  Focused 1-test and full 664-test verification passed with repository-local
  `git diff --check` (2026-08-04 19:10 PDT / 2026-08-05 02:10 UTC); local
  commit `a125a1b`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed optional complete-program handling before
  episode-manifest artifact I/O. `read_episode_manifest()` now rejects
  non-string and empty replay programs before opening the artifact; a
  missing-path adversary proves deterministic caller-error precedence.
  Focused and full 664-test verification passed with repository-local `git
  diff --check` (2026-08-05 01:14 PDT / 08:14 UTC); local commit `ba763bd`.
  Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close PeTTaChainer manifest replay dependencies before artifact I/O.
  `read_pettachainer_episode_manifest()` now establishes the immutable episode
  contract, typed derived capture, and matching rule attribution before
  loading JSON. A missing-path adversarial matrix proves malformed inputs have
  deterministic typed precedence. Focused and full 664-test verification
  passed with repository-local `git diff --check` (2026-08-05 03:13 PDT /
  10:13 UTC); local commit `bd086fb`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Validate PeTTaChainer episode manifests before persistence-side effects.
  `write_pettachainer_episode_manifest()` now constructs the typed checksummed
  document before creating a missing parent, and a regression proves malformed
  input leaves that parent absent. Focused 142-test and full 664-test
  verification passed with repository-local `git diff --check` (2026-08-05
  07:01 PDT / 14:01 UTC); local commit `87e45c0`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed PeTTaChainer derived-result persistence before filesystem
  mutation. The checksummed document builder now requires a typed capture, and
  the writer serializes it before creating a missing parent; an adversarial
  regression proves malformed input leaves that parent absent. Focused and full
  664-test verification passed with repository-local `git diff --check`
  (2026-08-05 09:03 PDT / 16:03 UTC); local commit `8771716`. Runtime invocation,
  promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed PeTTaChainer rule-attribution persistence before
  filesystem mutation. The writer now builds the typed checksummed document
  before creating the destination parent, and a regression proves malformed
  input leaves the parent absent. Focused and full 664-test verification passed
  with repository-local `git diff --check` (2026-08-05 11:00 PDT / 18:00 UTC);
  local commit `c3de0a0`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed stock pi-PLN episode-manifest persistence before
  filesystem mutation. The public document builder now requires a typed
  `EpisodeManifest`, and the writer serializes it before creating a missing
  parent. Focused and full 664-test verification passed with repository-local
  `git diff --check` (2026-08-05 13:04 PDT / 20:04 UTC); local commit `f7fba44`.
  Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed validated-kernel-result persistence before filesystem
  mutation. `validated_kernel_result_document()` now requires a typed
  `ValidatedKernelResult`, and `write_validated_kernel_result()` completes
  validation/serialization before creating a destination parent. A regression
  proves a malformed result leaves the requested parent absent. Focused and
  full 664-test verification passed with repository-local `git diff --check`
  (2026-08-05 15:01 PDT / 22:01 UTC); local commit `1974cc8`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Close malformed evidence-snapshot serialization before filesystem
  mutation. The canonical document builder now requires an immutable
  `EvidenceSnapshot`, and the writer serializes it before creating parent
  directories. A regression proves malformed input leaves no directory behind.
  Focused and full 665-test verification passed with repository-local `git
  diff --check` (2026-08-05 17:10 PDT / 2026-08-06 00:10 UTC); local commit
  `ecd38a8`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed compiled episode-input persistence before filesystem
  mutation. The canonical document builder now requires immutable
  `CompiledEpisodeInputs`, and the writer serializes before parent creation.
  Focused and full 666-test verification passed with repository-local `git
  diff --check` (2026-08-05 19:00 PDT / 2026-08-06 02:00 UTC); local commit
  `e012c48`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed compiled-input handling before validated-result artifact
  I/O. `read_validated_kernel_result()` now requires immutable
  `CompiledEpisodeInputs` before opening the supplied path; an absent-artifact
  regression proves deterministic caller-error precedence. Focused and full
  667-test verification passed with repository-local `git diff --check`
  (2026-08-05 23:00 PDT / 2026-08-06 06:00 UTC); local commit `4eec465`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed compiler-contract handling before PeTTaChainer
  derived-result artifact I/O. `read_pettachainer_derived_result_capture()` now
  requires a typed immutable episode contract before opening its path; an
  absent-artifact regression fixes deterministic caller-error precedence.
  Focused and full 667-test verification passed with repository-local `git
  diff --check` (2026-08-06 03:00 PDT / 10:00 UTC); local commit `6cd83e5`.
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.

- [x] Close the evidence-snapshot top-level persistence schema. Reload now
  admits exactly `schema`, `payload`, and `document_digest`; an undeclared
  `promotion_authorized` member fails closed without relying on the payload
  checksum. Focused and full 667-test verification passed with repository-local
  `git diff --check` (2026-08-06 07:01 PDT / 14:01 UTC); local commit
  `d956bc6`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed immutable dependency handling in `build_pi_chart()`.
  Context, chart policy, and evidence snapshot are now type-checked before
  provenance closure and fingerprint construction, preserving a stable typed
  failure boundary. Focused and full 668-test verification passed with
  repository-local `git diff --check` (2026-08-06 09:02 PDT / 16:02 UTC);
  local commit `fbf6ed5`. Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed immutable dependency handling at deterministic episode
  compilation. `compile_episode_inputs()` now requires typed `PiChart` and
  `EvidenceSnapshot` inputs before dereferencing provenance, preserving a
  stable public validation contract. Focused and full 669-test verification
  passed with repository-local `git diff --check` (2026-08-06 11:00 PDT /
  18:00 UTC); local commit `225aade`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Close malformed episode compiler collection members. Every supplied
  packet and evidence basis is now admitted as its immutable typed model
  before identifier/provenance access; adversarial `None` members prove the
  stable public `ValueError` boundary. Focused and full 669-test verification
  passed with repository-local `git diff --check` (2026-08-06 13:01 PDT /
  20:01 UTC); local commit `2f50b6b`. Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed immutable compiled-input collection members.
  `CompiledEpisodeInputs` now requires typed `StampMapEntry` and
  `CompiledSentence` members before field access, preserving the typed model
  boundary consumed by patham9/PLN and PeTTaChainer adapters. Focused and full
  669-test verification passed with repository-local `git diff --check`
  (2026-08-06 15:00 PDT / 22:00 UTC); local commit `940f8d9`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Close malformed immutable dependencies at PeTTaChainer derived-result
  construction. `build_pettachainer_derived_result_capture()` now requires
  typed input statements and stage captures before dereferencing them. Focused
  and full 669-test verification passed with repository-local `git diff
  --check` (2026-08-06 19:00 PDT / 2026-08-07 02:00 UTC); local commit
  `020f1a4`. Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed immutable budget handling at PeTTaChainer episode-manifest
  construction. `build_pettachainer_episode_manifest()` now requires an
  `EpisodeBudget` before constructing its digest payload, preserving a stable
  public `ValueError` boundary. Focused and full 669-test verification passed
  with repository-local `git diff --check`; local commit `0ec094f` (2026-08-06
  21:03 PDT / 2026-08-07 04:03 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed PeTTaChainer input-statement provenance sidecars.
  Boolean/non-integer/negative stamps and non-string/blank evidence-basis IDs
  now fail through explicit typed validation. Focused and full 671-test
  verification passed with repository-local `git diff --check`; local commit
  `2450609` (2026-08-07 01:00 PDT / 08:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close cross-statement PeTTaChainer stamp provenance. The immutable
  episode contract now requires a consistent one-to-one stamp/evidence-basis
  mapping across every checked-add statement, rejecting both same-stamp /
  different-basis and same-basis / different-stamp reconstructions. Focused
  and full 672-test verification passed with repository-local `git diff
  --check`; local commit `03d58c1` (2026-08-07 05:01 PDT / 12:01 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close mutable statement-container admission at the PeTTaChainer episode
  contract boundary. `statements` must now be a non-empty tuple, preserving
  the contract's immutable audit identity. Focused and full 673-test
  verification passed with repository-local `git diff --check`; local commit
  `5a30718` (2026-08-07 07:01 PDT / 14:01 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Enforce reconstructed PeTTaChainer aggregate statement size before
  uniqueness and provenance scans. The immutable contract now accumulates its
  checked-add character budget incrementally and fails oversized repeated
  statement tuples at the resource boundary. Focused and full 678-test
  verification passed with repository-local `git diff --check`; local commit
  `a8dc813` (2026-08-07 19:00 PDT / 2026-08-08 02:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Bound PeTTaChainer query text before episode provenance scans. Query
  type and aggregate atom/term ceilings now precede proof-id and stamp/basis
  scans; an adversarial duplicate-statement regression proves deterministic
  resource-error precedence. Focused and full 679-test verification passed
  with repository-local `git diff --check`; local commit `716292a`
  (2026-08-07 21:00 PDT / 2026-08-08 04:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Bound reconstructed PeTTaChainer derived-result text before parsing.
  Query term, derived atom, and derived proof must be strings within the
  immutable compiled-atom ceiling before the canonical parser is reached.
  Two focused regressions and the full 681-test suite passed with
  repository-local `git diff --check` (2026-08-07 23:00 PDT / 2026-08-08
  06:00 UTC); local commit `920fe33`. Runtime invocation, promotion/write,
  live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Bound reconstructed `ValidatedKernelResult.query_term` before parsing.
  Non-string and oversized duplicate typed query text now fails at the
  immutable stock pi-PLN result boundary without entering the canonical
  parser. Focused and full 682-test verification passed with repository-local
  `git diff --check`; local commit `4020052` (2026-08-08 01:00 PDT / 08:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close mutable evidence-basis provenance collections. `EvidenceBasis`
  now requires immutable tuples for `member_token_ids` and
  `causal_group_ids`, so a reconstructed frozen basis cannot retain
  caller-owned lists. Focused and full 684-test verification passed with
  repository-local `git diff --check`; local commit `620ea50` (2026-08-08
  15:00 PDT / 22:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close mutable evidence-snapshot content collections. `EvidenceSnapshot`
  now requires immutable tuples for `packet_ids`, `packet_content_digests`, and
  each nested digest pair, preventing post-validation mutation through a
  reconstructed frozen snapshot. Focused and full 685-test verification passed
  with repository-local `git diff --check`; local commit `7ba8f1e` (2026-08-08
  17:00 PDT / 2026-08-09 00:00 UTC). Runtime invocation, promotion/write, live
  integration, dependencies, paid compute, and remote actions remain closed.
- [x] Close mutable and malformed pi-chart inputs. `PiChart` now requires an
  immutable tuple for `selected_packet_ids` and a typed `ChartPolicy`, so a
  reconstructed frozen chart cannot retain a caller-owned list or leak an
  attribute error through downstream policy access. Focused and full 688-test
  verification passed with repository-local `git diff --check`; local commit
  `a6c7fd1` (2026-08-08 23:00 PDT / 2026-08-09 06:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed evidence-snapshot builder inputs.
  `build_evidence_snapshot(...)` now requires every supplied item to be an
  immutable `EvidencePacket` before reading its identity, so malformed callers
  receive a stable `ValueError` instead of leaking `AttributeError`. Focused
  and full 689-test verification passed with repository-local `git diff
  --check`; local commit `da3cf8b` (2026-08-09 01:00 PDT / 08:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.

- [x] Close mutable and malformed pi-chart inputs. `PiChart` now requires a
  typed immutable `ChartPolicy` and tuple-backed `selected_packet_ids` before
  their existing semantic checks. Focused and full 688-test verification
  passed with repository-local `git diff --check`; local commit `a6c7fd1`
  (2026-08-08 23:02 PDT / 2026-08-09 06:02 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed evidence-packet provenance identifiers. Token and parent
  packet identifiers now pass the shared non-empty string validator before
  sorted/unique checks, yielding stable `ValueError` boundaries for malformed
  reconstructed packets. Focused and full 690-test verification passed with
  repository-local `git diff --check`; local commit `8b83035` (2026-08-09
  03:02 PDT / 10:02 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.
- [x] Close malformed evidence-token provenance fields. Optional source-event,
  causal-group, and payload identifiers now pass the shared non-empty string
  boundary when present, and schema versions must be positive integers.
  Focused and full 691-test verification passed with repository-local `git
  diff --check`; local commit `d3cc023` (2026-08-09 05:00 PDT / 12:00 UTC).
  Runtime invocation, promotion/write, live integration, dependencies, paid
  compute, and remote actions remain closed.
- [x] Validate evidence-basis provenance members. `EvidenceBasis` now rejects
  empty and non-string member-token and causal-group ids through stable
  `ValueError` contracts before canonical ordering checks. Focused and full
  692-test verification passed with repository-local `git diff --check`
  (2026-08-09 07:03 PDT / 14:03 UTC); local commit `79e8264`. Runtime invocation, promotion/write,
  live integration, dependencies, paid compute, and remote actions remain
  closed.
- [x] Close untyped deterministic stamp-map inputs. The stamp allocator now
  freezes and validates its supplied basis collection before sorting by
  `basis_id`; a forged member cannot trigger field access before admission.
  Focused and full 693-test verification passed with repository-local `git
  diff --check`; local commit `9be0d85` (2026-08-09 09:00 PDT / 16:00 UTC).
  Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed evidence-basis builder dependencies.
  `evidence_basis_from_packet()` now validates the immutable `EvidencePacket`
  and every `EvidenceToken` before reading provenance fields. Sentinel-backed
  focused verification and the full 694-test suite passed with repository-local
  `git diff --check`; local commit `8e926d3` (2026-08-09 11:03 PDT / 18:03
  UTC). Runtime invocation, promotion/write, live integration, dependencies,
  paid compute, and remote actions remain closed.
- [x] Close malformed exact evidence-capsule merge dependencies. The merge
  boundary now requires typed immutable `EvidenceCapsule` operands and typed
  `EvidenceBasis` metadata before dereferencing either. Focused and full
  696-test verification passed with repository-local `git diff --check`; local
  commit `9f61044` (2026-08-09 15:00 PDT / 22:00 UTC). Runtime invocation,
  promotion/write, live integration, dependencies, paid compute, and remote
  actions remain closed.
- [x] Close malformed evidence-snapshot packet-id admission. Packet-id members
  are now typed before sorting, preventing reconstructed mixed-type tuples from
  leaking `TypeError`. Focused and full 698-test verification passed with
  repository-local `git diff --check`; local commit `e93f4bb` (2026-08-09 21:01 PDT / 2026-08-10
  04:01 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [x] Close malformed evidence-snapshot digest-entry arity admission.
  `packet_content_digests` now requires immutable two-field tuples before
  destructuring, preventing wrong-length reconstructed entries from leaking
  incidental unpacking errors. Focused and full 698-test verification passed
  with repository-local `git diff --check`; local commit `5b842f4` (2026-08-09
  23:00 PDT / 2026-08-10 06:00 UTC). Runtime invocation, promotion/write, live integration,
  dependencies, paid compute, and remote actions remain closed.
- [ ] ProtoCosmo2 handoff canary on isolated branch `agent/protocosmo2-handoff`.
  Starting point is frozen at clean commit
  `5b842f4d8e203d86c0d14f42eb91a03535376c0a` in
  `worktrees/protocosmo2-handoff`; the competing recurring progress worker is
  disabled. Deliverable: inspect the authoritative project records and select
  one bounded, nontrivial frontier task beyond repeated reconstructed-input
  micro-hardening, then implement, test, document, and commit it locally.
  Acceptance: focused tests, full provider-free suite (baseline 698 tests),
  `git diff --check`, clean committed worktree, and PROJECT/TASKS/NOTES evidence.
  Next command: have ProtoCosmo2 inspect PROJECT.md, TASKS.md, DECISIONS.md,
  NOTES.md and the isolated worktree, then propose the smallest frontier slice.
  Evidence path: `projects/petta-memory/worktrees/protocosmo2-handoff` and a new
  run under `projects/petta-memory/experiments/`.
- [x] Produce the 2026-08-10 petta-memory status and coding-agent handoff pack.
  Deliverables: an ASCII-only LaTeX source plus compiled PDF separating proposed
  ideas from implemented/evidenced work, and a practical Markdown takeover guide
  covering local paths, code/directory roles, GitHub remote, tests, and a
  secret-safe authentication procedure. Acceptance: PDF builds successfully,
  source is ASCII-only, repository facts are checked against the frozen handoff
  worktree, and both requested deliverables are attached to Ben's conversation.
  Next command: inspect repository README, source tree, test inventory, project
  history, and experiment records. Evidence path:
  `projects/petta-memory/docs/handoff-2026-08-10/`. Completed with ASCII-only
  LaTeX, compiled PDF, practical Markdown handoff, repository/remote audit, and
  secret-safe GitHub authentication guidance. Tectonic build passed. A fresh
  isolated-worktree verification run collected 698 tests but exposed one
  failure, one error, and eight skips caused or plausibly caused by unresolved
  dependency-relative paths; exact evidence is in
  `experiments/20260810T145211Z-protocosmo2-handoff-full-suite/`.
- [ ] Standing main-task assignment (Ben, 2026-08-10): advance petta-memory
  step by step whenever no more urgent work intervenes. Current deliverable:
  make the frozen `5b842f4` ProtoCosmo2 handoff reproduce its recorded
  provider-free baseline from the isolated worktree. Acceptance: all 698 tests
  pass (with only the expected documented skips), dependency commits and paths
  are recorded, and a successful experiment `RUN.md` exists. Next command:
  inspect the two failing tests and their dependency-path resolution without
  modifying or repinning sibling repositories. Evidence:
  `experiments/20260810T145211Z-protocosmo2-handoff-full-suite/RUN.md` and its
  eventual successful successor.
