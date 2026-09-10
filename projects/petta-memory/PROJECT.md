
- [x] **2026-08-30**: Fixed `_isolated_stage_worker` stdout capture bug. The worker
  redirected OS fds 1/2 via `dup2` but did not replace `sys.stdout`/`sys.stderr`.
  Under pytest's stdout capturing, `sys.stdout` is a pytest capture object, not
  fd 1, so `print()` output never reached the temp capture files. Fix: after
  `dup2`, open new Python file objects on fds 1/2 with `closefd=False` and
  assign to `sys.stdout`/`sys.stderr`. Save and restore originals in `finally`.
  Full 718-test suite passes. Local commit `8b94ccc`.

- [x] **2026-08-30**: Added 12 pipeline evaluation tests on a rich 6-belief store
  with 3 domains and diverse EC profiles (overwhelming, balanced, strongly
  conflicting, no-evidence, high-STV-low-EC, mid-range). Tests verify pipeline
  ranking, domain filtering, top_k selection, min_confidence filtering,
  combined filters, and EC projection formula edge cases. Full 730-test
  suite passes. Local commit `b48975d`.

- [x] Immutable kernel sentence provenance now validates stamp and evidence-basis
  members before uniqueness sorting, so mixed-type reconstructed metadata fails
  through stable `ValueError` boundaries instead of leaking `TypeError`. Focused
  and full 697-test verification passed with repository-local `git diff
  --check`; local commit `7655494` (2026-08-09 19:00 PDT / 2026-08-10 02:00
  UTC). No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.

- [x] Optional evidence-capsule merge metadata now rejects non-iterable input
  through the stable `ValueError` boundary instead of leaking `TypeError`.
  Focused and full 696-test verification passed with repository-local `git
  diff --check`; local commit `60e1d07` (2026-08-09 17:00 PDT / 2026-08-10 00:00 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] Immutable evidence packets now reject non-integer schema versions through
  the stable `ValueError` boundary instead of leaking a comparison `TypeError`.
  Focused and full 695-test verification passed with repository-local `git
  diff --check`; local commit `1c6232d` (2026-08-09 13:00 PDT / 20:00 UTC).
  No runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.

- [x] Immutable pi-PLN contexts now require tuple-backed parent-context
  provenance, preventing reconstructed frozen contexts from retaining a
  caller-owned mutable list. Focused and full 687-test verification passed
  with repository-local `git diff --check`; local commit `7df8be5`
  (2026-08-08 21:00 PDT / 2026-08-09 04:00 UTC). No runtime invocation,
  promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Immutable evidence capsules now require a tuple of typed
  `EvidenceContribution` records, preventing reconstructed frozen capsules
  from retaining caller-owned lists and normalizing malformed members through
  the public `ValueError` boundary. Focused and full 686-test verification
  passed with repository-local `git diff --check`; local commit `c07ac52`
  (2026-08-08 19:02 PDT / 2026-08-09 02:02 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Immutable evidence packets now require tuple-backed token and parent
  provenance collections, preventing reconstructed frozen packets from
  retaining caller-owned mutable lists. Focused and full 683-test verification
  passed with repository-local `git diff --check`; local commit `fd6a78d`
  (2026-08-08 13:00 PDT / 20:00 UTC). No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.

- [x] Immutable stock pi-PLN episode manifests now require tuple-backed parent
  episode and projection-policy collections, preventing reconstructed frozen
  manifests from retaining caller-owned mutable lists. Focused and full
  682-test verification passed with repository-local `git diff --check`;
  local commit `bbea4b5` (2026-08-08 11:01 PDT / 18:01 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Immutable validated kernel results now require tuple-backed stamp and
  evidence-basis provenance collections, preventing caller mutation after
  result admission. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `2e3bdcd` (2026-08-08
  09:01 PDT / 16:01 UTC). No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] Immutable kernel sentence provenance metadata now requires tuple-backed
  stamp and evidence-basis sidecars, preventing caller mutation after
  validation. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `f989970` (2026-08-08
  07:03 PDT / 14:03 UTC). No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] Immutable compiled episode inputs now require tuple-backed stamp maps and
  sentence collections, preventing caller mutation after validation. Focused
  and full 682-test verification passed with repository-local `git diff
  --check`; local commit `9e80395` (2026-08-08 05:00 PDT / 12:00 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Immutable compiled patham9 sentences now type-check their projection and
  provenance metadata dependencies and bound atom/term text before canonical
  S-expression parsing. Focused and full 682-test verification passed with
  repository-local `git diff --check`; local commit `546de55` (2026-08-08
  03:02 PDT / 10:02 UTC).
  No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.

- [x] Reconstructed PeTTaChainer checked-add statements now type-check and
  bound their duplicated atom/term text before canonical S-expression parsing.
  Focused and full 677-test verification passed with repository-local `git
  diff --check`; local commit `faad440` (2026-08-07 17:00 PDT / 2026-08-08
  00:00 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Reconstructed PeTTaChainer contracts now bound the duplicated typed
  query term before canonical S-expression parsing, so a small forged query
  atom cannot route an oversized term into the parser. Focused and full
  675-test verification passed with repository-local `git diff --check`;
  local commit `99fe409` (2026-08-07 15:00 PDT / 22:00 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] PeTTaChainer episode contracts now preserve the compiler's global
  zero-based contiguous stamp space, rejecting reconstructed contracts that
  skip a provenance stamp. Focused and full 675-test verification passed with
  repository-local `git diff --check`; local commit `a9d4e65` (2026-08-07
  11:00 PDT / 18:00 UTC). No
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.

- [x] PeTTaChainer checked-add statement provenance sidecars now require
  immutable tuples, preventing caller mutation after validation. Focused and
  full 674-test verification passed with repository-local `git diff --check`
  (2026-08-07 09:00 PDT / 16:00 UTC); local commit `d0adc8c`. No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] PeTTaChainer checked-add statements now require a one-to-one audit
  mapping from every stamp to an evidence-basis id, closing provenance at the
  earliest immutable PLN-ready contract boundary. Focused and full 672-test
  verification passed with repository-local `git diff --check`; local commit
  `640e715` (2026-08-07 03:00 PDT / 10:00 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] PeTTaChainer derived-capture and episode-manifest builders now validate
  their immutable fact/rule, stage-capture, and episode-budget dependencies
  before field access. Malformed callers fail through stable `ValueError`
  contracts instead of leaking `AttributeError`. Full 669-test verification
  passed with repository-local `git diff --check`; local commits `020f1a4` and
  `0ec094f` (2026-08-06 23:00 PDT / 2026-08-07 06:00 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] PeTTaChainer episode contracts now type-check every checked-add statement
  before proof-id access. Malformed reconstructed contracts fail through a
  stable `ValueError` instead of leaking `AttributeError`. Focused and full
  669-test verification passed with repository-local `git diff --check`;
  local commit `817848d` (2026-08-06 17:00 PDT / 2026-08-07 00:00 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Bounded kernel-process capture persistence now completes typed document
  validation and serialization before creating destination directories. A
  malformed-input regression proves the immutable artifact boundary has no
  filesystem side effect. Focused and full 667-test verification passed with
  repository-local `git diff --check` (2026-08-05 21:00 PDT / 2026-08-06
  04:00 UTC); local commit `ece240a`. No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.

- [x] PeTTaChainer episode-manifest serialization now rejects malformed
  manifest objects through a stable `ValueError` contract before payload
  field access. Focused and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-05 05:24 PDT / 12:24 UTC);
  local commit `fa5c695`.
  No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.

- [x] Episode-manifest reload now type-checks an optional immutable kernel
  capture before artifact I/O, so malformed callers receive the stable capture
  `ValueError` boundary rather than an unrelated missing-file or schema error.
  Focused and full 664-test verification passed with repository-local `git
  diff --check` (2026-08-04 23:03 PDT / 2026-08-05 06:03 UTC); local commit
  `4935583`. No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] Episode-manifest reload now type-checks optional immutable compiler and
  validated-result replay dependencies before dereferencing them. Malformed
  callers fail through stable `ValueError` boundaries instead of leaking
  `AttributeError`. Focused and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-04 21:35 PDT / 2026-08-05
  04:35 UTC); local commit `e6e871d`. No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Core patham9 kernel-result admission now type-checks its immutable
  compiled-input dependency before parsing or provenance lookup. Malformed
  direct callers fail through the public `ValueError` boundary instead of
  leaking `AttributeError`, and capture/replay callers inherit the same
  closure. Focused 89-test and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-04 17:00 PDT / 2026-08-05
  00:00 UTC); local commit `473962b`. No external runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] Exact semantic replay and captured replay now type-check their expected
  result and immutable compiled inputs before dereferencing either dependency.
  Malformed orchestration input fails through the public typed `ValueError`
  boundary instead of leaking `AttributeError`. Focused clean-room replay and
  full 660-test verification passed with repository-local `git diff --check`
  (2026-08-04 15:00 PDT / 22:00 UTC); local commit `7801117`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] The requested-pipe validation boundary now has an adversarial cleanup
  regression: if a malformed process construction omits a requested pipe and
  cleanup itself fails, the runner raises its typed pipe-validation cleanup
  failure with the original cause while still attempting every supplied stream
  close. Focused and full 660-test verification passed with repository-local
  `git diff --check` (2026-08-04 01:00 PDT / 08:00 UTC); local commit
  `d8728dc`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] The bounded kernel subprocess runner now validates that process
  construction actually supplied all three requested pipes before starting
  capture workers. A malformed construction result is killed, reaped, and
  closed through a typed failure instead of permitting a worker assertion to
  escape asynchronously. Focused and full 659-test verification passed with
  repository-local `git diff --check` (2026-08-03 23:03 PDT / 2026-08-04
  06:03 UTC); local commit `f2e809e`. No external runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] The bounded kernel subprocess runner now normalizes unexpected captured
  stream close failures through a typed `ValueError`, retains the original
  cause, and attempts both stdout and stderr closure even when the first
  fails. Focused and full 649-test verification passed with repository-local
  `git diff --check` (2026-08-03 03:00 PDT / 10:00 UTC); local commit
  `c748b58`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] The bounded kernel subprocess runner now normalizes unexpected ordinary
  process-construction failures through its typed launch `ValueError`
  contract, retaining the original exception as the cause. Focused 3-test and
  full 658-test verification passed with repository-local `git diff --check`
  (2026-08-03 21:01 PDT / 2026-08-04 04:01 UTC); local commit `6c7ce16`. No
  external runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.

- [x] The bounded kernel subprocess runner now normalizes every ordinary
  direct-process wait failure through a typed `ValueError`, retaining the
  original failure as its cause while still terminating the process group and
  closing captured streams. Focused and full 647-test verification passed with
  repository-local `git diff --check` (2026-08-02 23:00 PDT / 2026-08-03
  06:00 UTC); local commit `e1af2e4`. No external runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] The bounded kernel subprocess runner now rejects duplicate keys emitted
  by adversarial `Mapping.items()` implementations instead of silently letting
  the last value replace the first before capture. Marker-backed focused
  verification and the full 643-test suite passed with repository-local `git
  diff --check` (2026-08-01 05:00 PDT / 12:00 UTC); local commit `aa39ee3`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] The bounded kernel subprocess runner now converts OS-level process launch
  failures into its typed `ValueError` contract while retaining the original
  exception as the cause. A focused regression, the full 643-test suite, and
  repository-local `git diff --check` passed (2026-07-31 15:00 PDT / 22:00
  UTC); local commit `52e9737`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] The bounded kernel subprocess runner now rejects NUL-bearing program
  text before launch, closing a control-byte path into the evaluator while
  preserving the existing UTF-8 and byte-budget checks. A marker-backed
  focused test and the full 641-test suite passed with repository-local `git
  diff --check` (2026-07-31 09:00 PDT / 16:00 UTC); local commit `07827c2`.
  No external runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Typed kernel captures now reject NUL-bearing argv entries, matching the
  bounded subprocess runner's OS launch boundary and preventing an impossible
  manually reconstructed capture from reaching Phase-0 replay admission.
  Focused 2-test and full 640-test verification passed with repository-local
  `git diff --check` (2026-07-31 01:00 PDT / 08:00 UTC); local commit
  `5a7393f`. No external runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Fresh Phase-0 replay now preserves and closes the subprocess environment
  input: captures retain canonical caller-supplied environment entries, and the
  frozen anchor rejects an explicit alternate environment. Focused and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-30 23:00 PDT / 2026-07-31 06:00 UTC); local commit `561d773`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] Fresh Phase-0 replay now preserves and closes the subprocess
  working-directory input: captures retain the normalized caller-supplied
  `cwd`, and the frozen stdin-only anchor rejects an explicit alternate
  runtime context. Focused and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 21:00 PDT / 2026-07-31
  04:00 UTC); local commit `ed17c09`. No external runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] Fresh Phase-0 replay now requires the exact stdin-only launch shape
  exercised by the bounded capture primitive: the normalized pinned executable
  must be the sole argv entry. A capture with correct executable/program/output
  identities plus an unreviewed mode flag fails closed. Focused and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-30 19:00 PDT / 2026-07-31 02:00 UTC); local commit `0da04d9`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] Fresh Phase-0 replay now closes both program identities emitted by the
  bounded subprocess capture: the direct program SHA-256 and the canonical
  complete-program CID must both match the admitted frozen source. A capture
  with a correct direct digest but contradictory CID fails closed. Focused and
  full verification passed with repository-local `git diff --check`
  (2026-07-30 15:00 PDT / 22:00 UTC); local commit `bbf5118`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action; local commit `ef5136c`.
- [x] Cyclic working-directory symlinks now fail through the bounded runner's
  typed `ValueError` contract before process launch instead of leaking a
  `RuntimeError`. A marker-backed focused test and the full 642-test suite
  passed with repository-local `git diff --check` (2026-07-31 13:00 PDT /
  20:00 UTC); local commit `90d539c`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.

- [x] Fresh Phase-0 replay now binds the exact program bytes delivered to the
  frozen runtime, not only its executable and byte-exact output. Bounded
  subprocess captures retain a direct program SHA-256 and replay admission
  requires it to equal the reference source digest. Focused and full 639-test
  verification passed with repository-local `git diff --check` (2026-07-30
  13:02 PDT / 20:02 UTC). No external runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.

- [x] Fresh Phase-0 replay now binds the frozen runtime executable identity,
  not only its byte-exact stdout: pinned subprocess captures retain the
  verified executable SHA-256 and replay admission requires it to equal the
  reference manifest digest. Focused and full verification passed; local
  commit `dc5326e` (2026-07-30 11:00 PDT / 18:00 UTC). No runtime invocation beyond the existing local
  subprocess unit fixture, promotion/write, live integration, dependency
  change, paid compute, or remote action.

- [x] The frozen Phase-0 replay anchor now admits only its exact two
  non-empty producer lines, in order: the declared semantic result followed
  by the successful marker. A fully rehashed output with an additional
  authority-shaped line fails closed. Focused reload and full 639-test
  verification passed with repository-local `git diff --check` (2026-07-30
  09:00 PDT / 16:00 UTC); local commit `23b9c5d`. No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] The frozen Phase-0 replay anchor now requires the declared semantic
  result and successful marker to occur as exact standalone producer-shaped
  output lines. A fully rehashed output that embeds the valid result as a
  substring of a larger line fails closed. Focused reload and full 639-test
  verification passed with repository-local `git diff --check` (2026-07-30
  07:01 PDT / 14:01 UTC). No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] The frozen Phase-0 replay anchor now admits its declared semantic result
  only as one bounded canonical patham9 kernel-result atom with finite
  unit-interval STV values and non-empty canonical sorted unique stamps. A
  rehashed manifest that relabels the pass diagnostic as the semantic result
  fails closed. Focused reload and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 05:01 PDT / 12:01 UTC);
  local commit `22c1f95`. No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.

- [x] The Phase-1 clean-room reload gate now admits frozen Phase-0 reference
  manifests only with their exact top-level and nested schema members. A
  rehashed reference boundary carrying an undeclared
  `promotion_authorized=true` claim fails closed. Focused reload and full
  639-test verification passed with repository-local `git diff --check`
  (2026-07-30 01:00 PDT / 08:00 UTC); local commit `1462790`. No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.

- [x] Frozen provider-free usability admission now binds both checksum
  sidecars to the producer's exact bundle-local `journal.metta` path, after
  first preserving the byte-identical sidecar invariant. Two fully rehashed,
  identical sidecars naming a relocated journal fail closed. Focused 33-test
  and full 639-test verification passed with repository-local `git diff
  --check` (2026-07-29 23:00 PDT / 2026-07-30 06:00 UTC); local commit
  `7c00f0a`. No runtime invocation, canonical write, promotion, live
  integration, dependency change, paid compute, or remote action.

- [x] Frozen provider-free usability admission now reproduces the producer's
  byte-identical checksum-sidecar invariant, not merely each sidecar's journal
  digest. A fully rehashed after-canary sidecar with the correct digest but a
  different recorded path fails closed. Focused 32-test and full 638-test
  verification passed with repository-local `git diff --check` (2026-07-29
  21:00 PDT / 2026-07-30 04:00 UTC); local commit `dac7e36`. No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, paid compute, or remote action.

- [x] Frozen provider-free usability inference admission now reconstructs the
  producer's exact stripped diagnostic-line list from the bounded stdout/stderr
  tails. A fully rehashed result that omits an observed pass diagnostic fails
  closed. Focused 31-test and full 637-test verification passed with
  repository-local `git diff --check` (2026-07-29 19:00 PDT / 2026-07-30
  02:00 UTC); local commit `96e152e`. No runtime invocation, canonical write, promotion, live
  integration, dependency change, paid compute, or remote action.

- [x] Frozen provider-free usability inference admission now enforces the
  producer's 4,000-character bound on each captured runtime stream tail. A
  fully rehashed 4,001-character stdout tail fails closed. Focused 28-test and
  full 634-test verification passed with repository-local `git diff --check`;
  local commit `a82d708` (2026-07-29 13:00 PDT / 20:00 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, or remote action.

- [x] Frozen provider-free usability inference admission now type-closes its
  diagnostic surfaces: stdout/stderr tails must be strings and every
  `diagnostic_lines` entry must be a string. A fully rehashed result carrying
  structured authority-shaped JSON in those fields fails closed. Focused
  27-test and full 633-test verification passed with repository-local `git
  diff --check`; local commit `79ba928` (2026-07-29 11:00 PDT / 18:00 UTC).
  No runtime invocation, canonical write, promotion, live integration,
  dependency change, or remote action.

- [x] Frozen provider-free usability admission now requires each provenance
  identity interpolated into MeTTa-side records to be exactly one canonical
  term. A fully rehashed evidence-id control-form injection fails closed.
  Focused 26-test and full 632-test verification passed with repository-local
  `git diff --check`; local commit `3bdc28d` (2026-07-29 09:00 PDT /
  16:00 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, or remote action.

- [x] Frozen provider-free usability inference admission now requires the
  interpolated source term to be exactly one canonical MeTTa S-expression.
  A fully rehashed newline/control-form injection-shaped term fails closed
  before its reconstructed runtime program can be admitted. Focused 25-test
  and full 631-test verification passed with repository-local `git diff
  --check`; local commit `4ec0449` (2026-07-29 07:02 PDT / 14:02 UTC). No
  runtime invocation, canonical write, promotion, live integration,
  dependency change, or remote action.

- [x] Frozen provider-free usability admission now preserves non-empty source
  provenance identities across belief, cluster, evidence, promotion domain,
  promotion event, and promotion rule fields. A fully rehashed source with an
  erased promotion rule fails closed. Focused 24-test and full 630-test
  verification passed with repository-local `git diff --check`; local commit
  `bae697c` (2026-07-29 05:00 PDT / 12:00 UTC). No runtime invocation,
  canonical write, promotion, live integration, dependency change, or remote
  action.

- [x] Frozen provider-free usability admission now preserves the source
  item's non-inferred boundary: `source_status` must be exactly
  `pln-ready-input-not-inferred-belief`. A fully rehashed relabel to
  `inferred-belief` fails closed. Focused 22-test and full 628-test
  verification passed with repository-local `git diff --check`; local commit
  `703e071` (2026-07-29 01:00 PDT / 08:00 UTC). No runtime invocation,
  canonical write, promotion, live integration, dependency change, or remote
  action.

- [x] Frozen provider-free usability inference admission now requires the
  provenance source item to be a patham9/PLN Sentence input whose exact atom is
  reconstructed from its admitted term, STV, and evidence identity. A fully
  rehashed unrelated source atom fails closed. Focused 21-test and full
  627-test verification passed with repository-local `git diff --check`; local
  commit `ea0db1f` (2026-07-28 23:00 PDT / 2026-07-29 06:00 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, or remote action.

- [x] Frozen provider-free usability inference admission now requires exactly
  one successful semantic marker for its exactly one reconstructed `Test`.
  A fully rehashed result claiming two successful markers fails closed.
  Focused 19-test and full 625-test verification passed with repository-local
  `git diff --check`; local commit `ff67c3e` (2026-07-28 19:00 PDT /
  2026-07-29 02:00 UTC). No runtime invocation, canonical write, promotion,
  live integration, dependency change, or remote action.

- [x] Frozen provider-free usability inference admission now reconstructs the
  exact source and bridge runtime Sentences plus expected truth value from the
  provenance-bearing source item. A fully rehashed runtime-source substitution
  fails closed. Focused 18-test and full 624-test verification passed with
  repository-local `git diff --check` (2026-07-28 17:15 PDT / 2026-07-29
  00:15 UTC); local commit `fb13cf7`. No runtime invocation, canonical write, promotion, live
  integration, dependency change, or remote action.

- [x] Frozen provider-free usability inference admission now binds the
  declared source term to its derived term and exact two-stamp provenance
  sidecar roles, including the source item's evidence identity. A fully
  rehashed source relabel fails closed. Focused 17-test and full 623-test
  verification passed with repository-local `git diff --check`; local commit
  `de68ca3` (2026-07-28 15:00 PDT / 22:00 UTC). No runtime invocation,
  canonical write, promotion, live integration, dependency change, or remote
  action.

- [x] Frozen provider-free usability inference admission now reconstructs and
  requires the exact bounded two-premise PLN program from its declared runtime
  sentences, derived query term, and expected result. A fully rehashed program
  text substitution fails closed. Focused 16-test and full 622-test
  verification passed with repository-local `git diff --check`; local commit
  `f68be17` (2026-07-28 13:02 PDT / 20:02 UTC). No runtime invocation,
  canonical write, promotion, live integration, dependency change, or remote
  action.

- [x] Frozen provider-free usability inference admission now binds the
  producer's exact non-live program boundary and provenance-preserving runtime
  stamp policy. Fully rehashed live-boundary and provenance-discarding
  adversaries fail closed. Focused 15-test and full 621-test verification
  passed with repository-local `git diff --check`; local commit `3c4d3e2`
  (2026-07-28 11:00 PDT / 18:00 UTC). No runtime invocation, canonical write, promotion, live
  integration, dependency change, or remote action.

- [x] Frozen provider-free usability inference admission now binds the exact
  derivation-program schema, mode, and member set. A fully rehashed result
  claiming an unreviewed program schema fails closed. Focused 13-test and full
  619-test verification passed with repository-local `git diff --check`;
  local commit `b7230cc` (2026-07-28 09:02 PDT / 16:02 UTC). No runtime invocation, canonical write,
  promotion, live integration, dependency change, or remote action.

- [x] Frozen provider-free usability inference admission now requires integer
  semantic marker counts, closing Python/JSON boolean-number type confusion
  (`true == 1`). A fully rehashed boolean-count result fails closed. Focused
  9-test and full 615-test verification passed with repository-local `git
  diff --check`; local commit `74859ec` (2026-07-28 03:00 PDT / 10:00 UTC).
  No runtime invocation, canonical write, promotion, live integration,
  dependency change, or remote action.

- [x] Frozen provider-free usability admission now requires the actual
  patham9/PLN derivation result contract, not only a top-level `"passed"`
  label: schema, process/classifier success, positive semantic-pass markers,
  and zero failure/error markers must agree. A fully rehashed bare-pass result
  fails closed. Focused 8-test and full 614-test verification passed with
  repository-local `git diff --check`; local commit `8e9c567` (2026-07-28
  01:00 PDT / 08:00 UTC). No
  runtime invocation, canonical write, promotion, live integration, dependency
  change, or remote action.

- [x] Frozen provider-free usability admission now semantically validates both
  producer checksum sidecars against the exact `journal.metta` digest, rather
  than trusting their integrity-bound bytes alone. A fully rehashed pair of
  false sidecars fails closed. Focused 6-test and full 612-test verification
  passed with repository-local `git diff --check`; local commit `08abbde`
  (2026-07-27 21:01 PDT / 2026-07-28 04:01 UTC). No canonical write,
  promotion, runtime invocation, live integration, dependency change, or
  remote action.

- [x] Frozen provider-free usability admission now requires the exact schema-v2
  summary member set. An otherwise valid bundle cannot carry an undeclared
  authority or outcome field alongside its integrity-bound artifacts. Focused
  5-test and full 611-test verification passed with repository-local `git
  diff --check`; local commit `7ef5748` (2026-07-27 19:00 PDT / 2026-07-28
  02:00 UTC). No canonical write, promotion, runtime invocation, live
  integration, dependency change, or remote action.

- [x] Frozen provider-free usability bundles now have a producer-owned,
  reusable read-only admission API. It verifies exact schema-v2 inventory,
  bounded regular artifacts and their digests, restart equality, passed
  inference, and explicit non-live authority before returning the summary.
  Focused 4 and full 610 tests passed with repository-local `git diff --check`
  in local commit `0971225` (2026-07-27 17:03 PDT / 2026-07-28 00:03 UTC).
  No canonical write, promotion, runtime invocation, live integration,
  dependency change, or remote action.

- [x] The provider-free usability summary v2 now integrity-commits every
  non-self-referential artifact in its declared ten-file bundle. In particular,
  the persistent journal lock and both journal checksum sidecars are no longer
  merely enumerated; their exact bytes are SHA-256-bound and independently
  recomputed by regression. Focused 5-test and full 606-test verification
  passed with repository-local `git diff --check`; local commit `41dfdda`
  (2026-07-27 15:00 PDT / 22:00 UTC). No promotion/write to canonical memory,
  live integration, paid compute, dependency change, or remote action.

- [x] The provider-free usability evidence bundle now declares a versioned
  summary schema and the exact ten-file artifact set, including the persistent
  journal lock and checksum sidecars. The regression also requires the output
  directory to contain no undeclared artifacts. Focused 5-test and full
  606-test verification passed with repository-local `git diff --check`; local
  commit `3773908` (2026-07-27 13:05 PDT / 20:05 UTC). No promotion/write to
  canonical memory, live integration, paid compute, dependency change, or
  remote action.

- [x] The provider-free usability summary now commits the independent-process
  restart retrieval artifact and records explicit passed-inference and
  byte-identical-restart outcomes. Focused 5-test and full 606-test
  verification passed with repository-local `git diff --check`; local commit
  `8861980` (2026-07-27 09:00 PDT / 16:00 UTC). No promotion/write to
  canonical memory, live integration, paid compute, dependency change, or
  remote action.

- [x] The provider-free usability gate now requires the output directory's
  immediate parent to exist and uses single-directory `mkdir`, so a nested
  output request cannot create undeclared parent directories outside the
  claimed output boundary. Focused 5-test and full 606-test verification
  passed with repository-local `git diff --check`; local commit `ac64440`
  (2026-07-27 07:01 PDT / 14:01 UTC). No promotion/write to canonical memory,
  live integration, paid compute, dependency change, or remote action.

- [x] The provider-free usability gate now fixes its process umask at `077`
  before creating any output. A permissive caller umask can no longer expose
  the private journal, prompt/index views, inference result, or summary to
  group/other users. Focused 4-test and full 605-test verification passed with
  repository-local `git diff --check`; local commit `651a41a` (2026-07-27
  05:04 PDT / 12:04 UTC). No promotion/write to canonical memory, live
  integration, paid compute, dependency change, or remote action.

- [x] The provider-free usability gate now rejects a lexically symlinked
  output parent before `mkdir`, ingestion, inference, or canary work, preventing
  its local-output boundary from being redirected through an operator-owned
  directory alias. Focused 3-test and full 604-test verification passed with
  repository-local `git diff --check`; local commit `c7811d2`
  (2026-07-27 03:00 PDT / 10:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  dependency change, or live integration.

- [x] The provider-free usability roundtrip now has an automated no-overwrite
  regression. A pre-existing output directory with operator-owned content is
  rejected before ingestion/inference, with its exact file bytes and mode
  preserved. Focused and full 602-test verification passed with
  repository-local `git diff --check`; local regression commit `a64e7b1`
  (2026-07-26 13:00 PDT / 20:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, dependency change, or live integration.

- [x] **Reproduced 2026-07-26:** provider-free usability roundtrip completed:
  fixture ingestion into a newly created journal, generated index, retrieval,
  local bounded patham9/PLN two-premise derivation, independent-process restart
  retrieval, and an explicitly enabled private read-only canary. The journal
  SHA-256 was identical before and after the canary; promotion and autonomous
  writes remained disabled. Evidence:
  `experiments/20260726T185632Z-provider-free-usability-roundtrip-retry/`.

- [x] PeTTaChainer episode-manifest resource bounds now have a fully rehashed
  semantic adversary. Setting `budget.max_steps` to zero and recomputing both
  the typed manifest digest and outer document checksum still fails closed at
  the positive-budget invariant. Focused and full 601-test verification passed
  with repository-local `git diff --check`; local regression commit `3364939`
  (2026-07-26 11:00 PDT / 18:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode-manifest seed validation now has a fully rehashed
  semantic adversary. Replacing the deterministic non-negative seed with `-1`
  and recomputing both the typed manifest digest and outer document checksum
  still fails closed at the typed seed invariant. Focused and full 601-test
  verification passed with repository-local `git diff --check`; local
  regression commit `d3ca892` (2026-07-26 09:00 PDT / 16:00 UTC). No runtime
  invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode-manifest temporal ordering now has a fully rehashed
  persistence adversary. Moving `finished_at` before `started_at` and
  recomputing both the typed manifest digest and outer document checksum still
  fails closed at the typed timestamp invariant. Focused and full 601-test
  verification passed with repository-local `git diff --check`; local
  regression commit `11b853a` (2026-07-26 07:00 PDT / 14:00 UTC). No runtime
  invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode-manifest result classification now has a fully
  rehashed semantic adversary. Relabeling the compiler-bound one-rule result as
  runtime-trace-derived and recomputing both manifest digests still fails
  closed at the typed classification invariant. Focused and full 601-test
  verification passed with repository-local `git diff --check`; local
  regression commit `b21d1be` (2026-07-26 05:00 PDT / 12:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode manifests now have a fully rehashed promotion
  adversary. Flipping `promotion_authorized` to true and recomputing both the
  typed manifest digest and outer document checksum still fails closed at the
  non-live typed invariant. Focused and full 601-test verification passed with
  repository-local `git diff --check`; local regression commit `4ba88fb`
  (2026-07-26 03:00 PDT / 10:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode-manifest chart anchoring now has a fully rehashed
  artifact adversary. Altering `chart_fingerprint` and recomputing both the
  typed manifest digest and outer document checksum still fails closed against
  the supplied compiler contract. Focused and full 601-test verification
  passed with repository-local `git diff --check`; local regression commit
  `387c2fa` (2026-07-25 23:00 PDT / 2026-07-26 06:00 UTC). No runtime
  invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer episode-manifest result binding now has a fully rehashed
  artifact adversary. Altering `result_cid` and recomputing both the typed
  manifest digest and outer document checksum still fails closed against the
  supplied admitted result and attribution. Focused and full 601-test
  verification passed with repository-local `git diff --check`; local
  regression commit `a744390` (2026-07-25 15:00 PDT / 22:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] PeTTaChainer rule-attribution reload now has a fully rehashed artifact
  adversary. Altering the attribution's bound `result_digest` and recomputing
  both its typed attribution digest and outer document checksum still fails
  closed against the supplied admitted result. Local regression commit
  `a27984a`; focused and full 601-test verification passed with
  repository-local `git diff --check` (2026-07-25 13:00 PDT / 20:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.

- [x] PeTTaChainer episode-manifest attribution binding now has a fully
  rehashed artifact adversary. Altering `attribution_cid` and recomputing both
  the typed manifest digest and outer document checksum still fails closed
  against the supplied compiler-bound attribution. Local regression commit
  `48c278f`; focused and full 601-test verification passed with
  repository-local `git diff --check` (2026-07-25
  11:00 PDT / 18:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] Compiler-bound PeTTaChainer rule attribution now participates in the
  two-cycle clean-room reload gate. Attribution identity remains stable beside
  typed result and manifest identities, and cross-class result/manifest/
  attribution reads fail closed. Local regression commit `3835baf`; focused
  and full 601-test verification passed
  with repository-local `git diff --check` (2026-07-25 07:00 PDT / 14:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.

- [x] Compiler-bound PeTTaChainer rule attribution now has a create-once,
  checksummed JSON artifact boundary. Reload reconstructs the typed attribution
  and requires exact equality with the attribution derived from the supplied
  admitted result capture; a valid artifact cannot be paired with a different
  result. Local implementation commit `eb5a2fb`; focused and full 601-test
  verification passed with repository-local
  `git diff --check` (2026-07-25 05:00 PDT / 12:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Typed PeTTaChainer derived captures and compiler-bound rule attribution
  now require distinct fact and rule sentence/proof identities. A correctly
  rehashed artifact cannot present one compiler input as both TotalMP premises.
  Local implementation commit `19fb7a9`; fresh full 601-test verification
  passed with `git diff --check` (2026-07-25 03:00 PDT / 10:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.

- [x] Typed PeTTaChainer derived-result captures now bind each isolated stream
  capture to its exact stage role. Even with a recomputed capture and result
  digest, the validator cannot be relabeled as the runtime stage or vice
  versa. Local implementation commit `6cef687`; focused and full 601-test verification passed with `git diff
  --check` (2026-07-25 01:00 PDT / 08:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Typed PeTTaChainer derived captures and compiler-bound rule attribution
  now require fact and rule provenance to be mutually disjoint, in addition to
  each side being internally complete. Correctly rehashed artifacts cannot
  reuse a stamp or evidence-basis ID across both TotalMP premises. Focused and
  full 601-test verification passed with `git diff --check`; local commit
  `1198954` (2026-07-24 21:02 PDT / 2026-07-25 04:02 UTC). No runtime
  invocation, promotion/write, upstream/remote action, paid compute, or live
  integration.

- [x] Typed PeTTaChainer derived-result captures now require one evidence-basis
  ID per retained stamp on both fact and rule sides. A caller can no longer
  forge and correctly rehash a capture whose provenance collections are
  individually valid but have unequal cardinality. Local implementation commit
  `aabc3fa`; focused and full 601-test verification passed with `git
  diff --check` (2026-07-24 17:00 PDT / 2026-07-25 00:00 UTC). No runtime
  invocation, promotion/write, upstream/remote action, paid compute, or live
  integration.

- [x] Compiler-bound PeTTaChainer rule attribution now validates its retained
  stamp and evidence-basis collections independently of the content digest:
  both rule and fact sides require non-empty, sorted, unique typed tuples, so
  a caller cannot construct and correctly rehash malformed attribution.
  Local implementation commit `39d5975`; focused and full 601-test
  verification passed with `git diff --check`
  (2026-07-24 13:00 PDT / 20:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Literal-LF captured-result admission now has explicit CR and CRLF
  adversary coverage. Neither legacy Mac-style carriage-return framing nor
  platform newline translation can make a result atom appear as the required
  exact LF-delimited stdout record. Local regression commit `60aacb2`; focused
  and full 601-test verification passed, plus `git diff --check` (2026-07-24
  09:00 PDT / 16:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.

- [x] Implementation status now accurately marks typed PeTTaChainer
  capture/result persistence and create-once episode-manifest
  persistence/reload as complete. Remaining boundaries are trace/rule
  attribution, reviewed promotion/write, upstream repair adoption, and live
  integration (2026-07-24 07:00 PDT / 14:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Captured legacy-kernel result admission now recognizes only literal LF
  framing. Vertical-tab and Unicode line-separator controls can no longer turn
  an embedded result atom into an apparent complete output record through
  Python's broader `splitlines()` semantics. Focused 1 and full 601 tests
  passed, plus `git diff --check`; local implementation commit `f3c569f`
  (2026-07-24 05:00 PDT / 12:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] Captured legacy-kernel result admission now preserves exact stdout record
  bytes: leading or trailing horizontal whitespace no longer becomes acceptable
  through line trimming. This closes the documented verbatim process/result
  provenance boundary while retaining surrounding trace lines. Local commit
  `bf27ee5`; focused and
  full verification passed 1 and 601 tests, plus `git diff --check`
  (2026-07-24 03:00 PDT / 10:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.

- [x] The formerly open specialized compiled-input runtime gate is resolved by
  the completed PeTTaChainer branch: compiler-emitted inputs bind an immutable
  checked-add/query contract, bounded one-rule derivation, independently
  verified TotalMP truth, typed capture, and non-promoting manifest reload.
  The stock generic patham9 probe remains a documented negative result; no
  stderr/result gate was relaxed. Fresh 601-test verification and
  `git diff --check` passed (2026-07-24 01:00 PDT / 08:00 UTC). No promotion,
  memory write, upstream adoption, paid compute, or live integration.

- [x] Phase-1 clean-room process-capture admission now explicitly rejects archived stderr and return-code drift, completing the bounded capture adversary matrix alongside stdout and delivered-program identity. Local regression commit `6de6912`; focused 1 and full 600 tests passed, plus `git diff --check`. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Phase-1 clean-room reload now explicitly audits its filesystem effects. Each isolated archive has an exact allowlist before admission, unchanged after compiled/result/manifest/reference reload and frozen-query validation, and only the deliberately created stale adversary afterward. Local regression commit `e7602a9`; focused 1 and full 600 tests passed, plus `git diff --check`. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Phase-1 clean-room capture/reload gate is complete. The final combined-gate regression mutates the frozen Phase-0 runtime output after successful admission and proves byte-count/checksum rejection, complementing stable two-cycle identities and the stale, malformed, duplicate-anchor, wrong-class, provenance, cross-run, and post-reload assertion cases already covered. Local regression commit `cf8ed5d`; focused test passed. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Phase-1 clean-room reload now explicitly distinguishes a newly asserted post-reload memory from both the loaded compiled sentence and the archived derived result. A different statement/snapshot/chart produces distinct sentence and chart identities; the frozen replay validator and manifest admission both reject reuse of the archived derivation. Local regression commit `6ed4a63`; focused 1 and full 600 tests passed, plus `git diff --check`. No schema/runtime change, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Phase-1 clean-room reload now rejects duplicate logical snapshot anchors inside one content-addressed archive: two semantically different snapshot artifacts with valid distinct fingerprints but the same `snapshot_id` fail closed during lookup instead of selecting by filename/order. Local regression commit `2ef2505`; focused 1 and full 600 tests passed, plus `git diff --check`. No schema/runtime change, promotion/write, upstream/remote action, paid compute, or live integration.

- [x] Phase-1 clean-room reload now rejects a same-named cross-run descriptor: a second compiled state may reuse the archived episode, chart, context, snapshot, packet, and token IDs, but altered evidence content changes its chart fingerprint and compiled sentence. The archived validated result rejects the collision, and the manifest plus frozen program rejects it before admission. Local regression commit `96b736f`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] Phase-1 clean-room reload now covers the current PeTTaChainer derived-capture and episode-manifest artifact class over two isolated descriptor-anchored cycles. Result, validator/runtime capture, and manifest identities remain stable; the frozen query remains usable; promotion stays forbidden; wrong artifact classes and a valid but cross-contract descriptor are rejected. Local implementation commit `94d749c`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] Phase-1 clean-room manifest reload now independently closes a supplied validated result's stamp set and ordered evidence-basis IDs against the supplied compiled artifact. A forged but internally checksummed manifest/result pair with the same episode and chart identity is rejected instead of being admitted through digest self-consistency alone. Local implementation commit `ef9aeb3`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] Phase-1 clean-room manifest reload can now bind the exact archived kernel program, in addition to compiled-input, chart/context, stamp-map, and validated-result provenance. Supplying any byte-different program rejects admission through the manifest's `compiled_program_cid`; compiled sentences must occur exactly once and the validated query must remain present. Local implementation commit `58fa218`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] Frozen Phase-0 patham9 replay-anchor manifests now enter through the shared bounded, duplicate-safe, descriptor-anchored JSON admission boundary instead of direct `read_text`/`json.loads`. Duplicate object members fail before replay metadata can be interpreted. Local implementation commit `5baedac`; focused 2 and full 599 tests passed, plus `git diff --check`. Runtime replay, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] Legacy pi-PLN audit admission now has public-boundary regression closure for late parent-directory identity drift: after the bounded artifact read, a changed parent inode is rejected before the evidence snapshot is admitted. Local regression commit `48d3e49`; focused 1 and full 598 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] The four pi-PLN audit writers routed through the hardened create-once publisher now have public-boundary regressions: episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs all reject a group-writable parent before creating a second artifact. Local regression commit `b3cbf00`; focused 4 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.

- [x] PeTTaChainer create-once audit publication now has regression closure for the combined artifact-creation failure and parent-descriptor close failure. The creation error remains primary, the cleanup diagnostic is retained, and no artifact is created. Local implementation commit `fb6bfbb`; focused 1 and full 597 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer create-once publication now has regression closure for the combined artifact-stream open failure, artifact-descriptor close failure, and parent-descriptor close failure. The stream-open error remains primary, both cleanup diagnostics are retained in order, and the partial artifact is removed. Local implementation commit `d5d8f2a`; focused 1 and full 596 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer create-once audit publication now has regression closure for the combined initial parent-metadata lookup failure and parent-descriptor close failure: the metadata error remains primary, the cleanup diagnostic is attached, and no artifact is created. Local implementation commit `3f7326b`; focused 1 and full 596 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer create-once audit publication now has regression closure for a parent-directory descriptor close failure after successful file and directory fsync. The close error propagates, while the already-durable artifact remains readable and create-once rather than being removed or overwritten. Local implementation commit `1e36bdf`; focused 1 and full 595 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer audit-artifact admission now has regression closure for a parent-descriptor close failure after an otherwise successful bounded read: the close error propagates and the artifact is not admitted. Local implementation commit `5f4d675`; focused 1 and full 593 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer audit-artifact admission now has regression closure for the combined final parent-metadata revalidation failure and parent-descriptor close failure: the revalidation error remains primary and the cleanup diagnostic is attached. Local implementation commit `06e57c3`; focused 1 and full 591 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer audit-artifact admission now has regression closure for the combined initial parent-metadata failure and parent-descriptor close failure: the actionable metadata error remains primary and the cleanup diagnostic is attached. This validates local implementation commit `c50eb47`; focused 2 and full 590 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer audit-artifact admission now preserves unsafe-parent and missing/unopenable-artifact failures when closing the already-open parent descriptor also fails, attaching the close diagnostic instead of masking the actionable rejection. Local implementation commit `f07d5b1`; focused 2 and full 588 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer audit-artifact admission now preserves a primary stream read or metadata failure when closing the descriptor-backed binary stream also fails, attaching the close diagnostic instead of masking the actionable rejection. A close failure after an otherwise successful read still propagates. Local implementation commit `a84c480`; focused 3 and full 575 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer checksummed artifact admission now rejects hard-linked JSON files and treats link-count drift during the bounded descriptor read as a concurrent artifact change. This preserves the one-path/one-artifact assumption against mutation through an alias. Local implementation commit `a167fef`; focused 3 and full 573 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.

- [x] PeTTaChainer create-once persistence now preserves the primary publication failure when partial-artifact unlink or cleanup-directory fsync also fails, attaching the secondary cleanup diagnostic instead of masking the actionable cause. Python 3.10/3.11-compatible regressions cover both cleanup paths. Local implementation commit `fee498d`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.

- [x] PeTTaChainer create-once persistence now durably removes a partially written artifact when file flush/fsync fails: cleanup unlinks through the already-open parent descriptor and fsyncs that directory before propagating the failure, preventing a crash from resurrecting rejected output. Local implementation commit `0eaacc1`; focused regression and full 570 tests passed, plus `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.

- [x] PeTTaChainer create-once persistence now anchors exclusive artifact creation and parent-directory fsync to one already-open directory descriptor. This closes a parent-path replacement race between publication and durability sync while preserving existing failure cleanup semantics. Local implementation commit `019154a`; focused regression and full 570 tests passed, plus `git diff --check`; promotion/write, upstream, remote, paid-compute, and live integration remain closed.

- [x] PeTTaChainer create-once persistence now preserves a completed file-synced artifact when parent-directory fsync fails. The error still propagates, but the uncertain publication state cannot be silently deleted and later overwritten; pre-file-sync failures still clean up partial output. Local implementation commit `6aad801`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.

- [x] PeTTaChainer derived-capture and episode-manifest create-once persistence now durably publishes both content and directory entry: a shared writer fsyncs the completed artifact and its parent directory while retaining exclusive creation and cleanup-on-failure. Local implementation commit `5c1f0d7`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream adoption, remote action, paid compute, and live integration remain closed.

- [x] PeTTaChainer episode manifests now have create-once, checksummed JSON persistence. Reload reconstructs the typed budget and manifest invariants, then closes contract identity plus derived-result and both bounded stage-capture identities against supplied immutable inputs before admission. Local implementation commit `6bfc31e`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream adoption, and live integration remain closed.

- [x] The compiler-bound repaired PeTTaChainer result now adapts into a distinct immutable `PeTTaChainerEpisodeManifest` instead of weakening the stock patham9 manifest model. The adapter content-addresses the full checked-add/query contract and binds the typed result, both bounded stage identities, exact repair/source profile, runtime/controller identities, budget, seed, and timestamps; construction closes exact fact/rule sidecars and structurally forbids promotion authorization. Local implementation commit `7656d29`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Manifest persistence, promotion/write, upstream adoption, and live integration remain closed.

- [x] The compiler-bound repaired PeTTaChainer derivation capture now has create-once, checksummed JSON persistence. Reload reconstructs both nested stage captures and all typed result invariants, then closes episode/query identity plus exact fact/rule proof, stamp, and evidence-basis provenance against the supplied immutable `PeTTaChainerEpisodeContract`. Local implementation commit `57e60f0`; focused persistence regression and full 570 tests passed, plus `py_compile` and `git diff --check`. PeTTaChainer-specific EpisodeManifest adaptation, promotion/write, upstream adoption, and live integration remain closed.

- [x] The compiler-bound repaired derivation now closes into immutable typed `PeTTaChainerStageCapture` and `PeTTaChainerDerivedResultCapture` records. Construction requires one unique retained answer, exact compiler-derived proof/query/TotalMP STV identity, exact fact/rule stamps and evidence bases, and digest-bound validator/runtime stream identities. A fresh isolated pinned `e4db5ca` single-import probe produced result digest `f77be221...`; local implementation commit `011a4a0`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Persistence, EpisodeManifest adaptation, promotion/write, upstream adoption, and live integration remain closed.

- [x] The repaired one-rule derivation is now bound back to one immutable two-statement `PeTTaChainerEpisodeContract`. The new fail-closed wrapper requires exactly one compiler-emitted fact and one implication, a non-stored query target, content-addressed proof IDs, and retained stamp/evidence-basis sidecars; the existing runtime gate then requires the exact derived proof over those IDs and the admitted TotalMP truth formula. Local implementation commit `d5abd83`; focused 113 and full 568 tests passed, plus `py_compile` and `git diff --check`. EpisodeManifest construction, promotion/write, upstream adoption, and live integration remain closed.

- [x] The repaired PeTTaChainer path now closes one immutable compiler-emitted episode contract through exact stored-fact recall. Public validators, the exact single-import repair, internal storage, and the complete answer set all admitted; the one-step run returned one typed input fact. Local implementation commit `9036dd2`; focused 109 and full 564 tests passed, plus `py_compile` and `git diff --check`. The result is explicitly `stored-fact-retrieval`, not derived PLN inference; diagnostic interpretation, manifests, promotion/write, upstream adoption, and live integration remain closed.

- [x] The repaired PeTTaChainer exact-fact query gate now closes the complete answer set: every non-empty answer must structurally equal the stored fact, so expected-plus-unrelated output fails closed. A fresh one-step repaired probe returned one answer, one unique answer, and zero unexpected answers. Local implementation commit `4cb2482`; focused 104 and full 559 tests passed, plus `py_compile` and `git diff --check`. Inferred-result promotion, memory writes, upstream changes, and live integration remain closed.

- [x] The repaired PeTTaChainer path now passes a separately bounded exact stored-fact query gate. After one gated `compileadd` and an exact `&kb` membership check, a one-step query returned one unique proof/type/STV answer matching the added promoted fact (numeric rendering normalized `0.70` to `0.7`) in 0.391 s. Local implementation commit `95ade3f`; focused 102 and full 557 tests passed, plus `py_compile` and `git diff --check`. Runtime noise (608,129 stdout and 142 stderr characters) is retained in provenance; inferred-result promotion, memory writes, upstream changes, and live integration remain closed.

- [x] The repaired PeTTaChainer add path now passes its first real `compileadd`-only gate under the exact single-import repair. One promoted-fact statement completed in 0.362 s with one expected external output and one exact internalized `&kb` match. Local implementation commit `df61d85`; focused 99 and full 554 tests passed, plus `py_compile` and `git diff --check`. The gate fails closed on source drift or missing storage and stops before query compilation/execution. Query/result admission, promotion/write, upstream change, and live integration remain gated.

- [x] Full repaired PeTTaChainer `mm2compile` now completes through the real compile/conversion/collection entry point under the exact single-import gate. One promoted-fact statement returned one unique expected fact in 0.367 s; the new gate fails closed on source drift and stops before `compileadd` or query. Local implementation commit `4cf97bf`; focused 96 and full 551 tests passed, plus `py_compile` and `git diff --check`. The next bounded gate is a repaired `compileadd`-only retry; no upstream, result-admission, promotion/write, or live change.

- [x] The first post-repair PeTTaChainer downstream rung now shows public `compile` and direct `compile_` both returning one identical clause on the exact single-import candidate (previously 256 versus 128). This confirms the old public-wrapper 2x factor also collapses with duplicate-registration removal. Local implementation commit `0f59d71`; focused 92 and full 547 tests passed, plus `py_compile` and `git diff --check`. Fact-KB, predicate, annotation, `mm2stmt`, and collector rungs still require fresh measurement before another repair or `compileadd` retry. No upstream, write, query, promotion, or live change.

- [x] The first isolated PeTTaChainer source repair is now admitted under exact critical-file hashes. Removing only the second `chainer/compile` import from `context_generation.metta` reduced direct `compile_` from 128 duplicate-equivalent outputs to one normalized-equivalent clause, showing the earlier measured factors are coupled rather than independent repair effects. Reusable source/runtime gates and three regressions were added in local commit `a345255`; focused 90 and full 545 tests passed, plus `py_compile` and `git diff --check`. Downstream compile/collection rungs must be remeasured before another repair or `compileadd` retry. No upstream, write, query, promotion, or live change.

- [x] The measured PeTTaChainer concrete-fact fan-out now closes as a fail-closed repair plan: `1 literal * 8 fact-kb * 4 bidirectional classifier * 2 annotated head * 2 duplicate registration * 2 public wrapper = 256`, while the deduplicated collector closes as `1 * 2 mm2stmt overlap * 2 collection = 4`. `build_pettachainer_fact_fanout_repair_plan()` rejects count drift and orders an isolated duplicate-registration repair before any source-pattern repair or experimental set collapse. Local implementation commit `914083d`; focused 87 and full 542 tests passed, plus `py_compile` and `git diff --check`. No upstream change, set collapse, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] The final unexplained twofold factor inside one registered PeTTaChainer concrete-fact dispatcher is now attributed to its annotated `(@ $stmt (: $prf $Type $tv))` head. Two locally registered definitions with identical bodies returned 64 copies through the annotated head versus 32 through direct structural `(: $prf $Type $tv)` matching, with one unique clause in both cases. Local implementation commit `05fbb37`; focused 85 and full 540 tests passed, plus `py_compile` and `git diff --check`. Diagnostic only: no upstream matcher/import change, deduplication, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] The remaining twofold multiplicity in direct PeTTaChainer `compile_` is now attributed to duplicate module registration. Pinned imports load `chainer/compile` directly and again through `context_from_kb -> context_generation`; a single source-equivalent local fact definition returned 64 copies while the twice-registered direct `compile_` returned 128 copies of the same unique clause. Local implementation commit `8150d69`; focused 82 and full 537 tests passed, plus `py_compile` and `git diff --check`. Diagnostic only: no upstream import change, set collapse, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] The nested concrete-fact predicates inside direct PeTTaChainer `compile_` are now separated under an exact source-shape gate. With the already-unique literal fact branch, adding `bidirectional-implication-type?` raised the result from one to four identical clauses; the surrounding implication and variable-type predicates stayed at four. This assigns a 4x factor to bidirectional classification and leaves the remaining direct-dispatch multiplicity at the annotated definition/dispatch and separately measured `compile-fact-kb` boundaries. Local implementation commit `1f219a6`; focused 79 and full 534 tests passed, plus `py_compile` and `git diff --check`. No upstream semantic change, `compile`, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] The public PeTTaChainer `compile` wrapper is now separated from direct `compile_` dispatch under an exact source-shape gate. In one pinned runtime, public `compile` returned 256 copies while direct `compile_` returned 128 copies of the same single unique fact clause in 0.547 s, assigning one 2x factor to the wrapper/evaluator boundary and leaving 16x above the literal fact branch inside direct dispatch. Local implementation commit `546696a`; focused 76 and full 531 tests passed, plus `py_compile` and `git diff --check`. No upstream semantic change, set collapse, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] The remaining PeTTaChainer fact-branch multiplicity is now localized above the literal fact branch. A source-gated copied ladder replaced only the already-measured eight-copy `compile-fact-kb` result with its unique literal KB: the base clause, explicit-empty arm, and real empty `compile-outputs` arm each returned exactly one copy in 0.460 s. Since public `compile` returns 256 copies, the unexplained 32x factor lies in the wrapper/`compile_` dispatch path rather than the literal fact branch. Local implementation commit `4a2e9a7`; focused 72 and full 527 tests passed, plus `py_compile` and `git diff --check`. No upstream change, `compile` in the new ladder, `mm2compile`, `compileadd`, query/result admission, promotion/write, or live integration.

- [x] A source-gated deduplicated `mm2compile`-equivalent collector now isolates clear/convert/`ctx` collection from the compiler's 256-copy input fan-out. One canonical fact clause completed in 0.461 s and returned four copies of one unique expected fact, showing another 2x multiplicity around the already-explained two-arm `mm2stmt` output. Local implementation commit `fecb51c`; focused 65 and full 520 tests passed, plus `py_compile` and `git diff --check`. No upstream change, `compile`, `compileadd`, query/result admission, manifest, promotion/write, or live integration.

- [x] Phase-2 result admission and manifest construction now consume the same immutable `KernelProcessCapture` through `build_captured_episode_manifest()`. This removes the manual copy seam where a caller could validate one capture and record another capture's process outputs. Local implementation commit `9806fbb`; focused 1 and full 501 tests passed, plus `py_compile` and `git diff --check`. The constructor is non-promoting; real compiled-input runtime execution, rule/trace identity, persistence, promotion/write, and live integration remain separate gates.

- [x] The first fresh pinned Phase-0 replay now passes through the bounded subprocess runner and a typed exact-replay gate. `validate_phase0_reference_replay()` rejects nonzero exit, any stderr, byte-count drift, checksum drift, or missing semantic markers. A fresh local Smokes run returned 0 with empty stderr and reproduced the frozen 6,021-byte SHA-256 `fd5a6133...` exactly. Local implementation commit `bf2ea91`; focused 2 and full 499 tests passed, plus `py_compile` and `git diff --check`. This validates the stock reference replay only; Phase-2 `EpisodeManifest` construction, rule/trace identity, promotion/write, and live integration remain separate gates.

- [x] Phase-0 reference admission is now a typed fail-closed prerequisite to the first end-to-end episode gate. `validate_phase0_reference_artifact()` closes the frozen manifest schema, source/output hashes and byte count, determinism hashes, semantic marker/result, pinned runtime/kernel identities, and non-live boundary flags. The committed Smokes artifact at patham9 `55f1751` admits successfully. Local implementation commit `cdc3b5d`; focused 1 and full 498 tests passed, plus `py_compile` and `git diff --check`. No fresh kernel execution, inferred-belief promotion/write, or live integration.

- [x] Current progress slice hardened the read-only `live-goal-bridge --run-patham9-runtime` program-count provenance boundary. When a patham9/PLN runtime result includes program `handoff_sentence_count` or `sentence_count`, the bridge now rejects boolean/non-integer/negative counts, rejects handoff sentence counts that do not match the already admitted handoff item count, and rejects total sentence counts smaller than the admitted handoff before any GoalChainer appraisal. Verification: local implementation commit `8e79e1c`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- [x] Pinned the read-only `live-goal-bridge --run-patham9-runtime` to the exact multi-sentence derivation result/program schemas. Query-smoke or other non-equivalent artifacts now fail closed before GoalChainer appraisal instead of passing on any non-empty schema string. Verification: local implementation commit `f42d293`; full unittest discovery passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.


- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe check boundary. When `include_heuristic_memory_probe=True`, the bridge now requires downstream GoalChainer `checks.heuristic_with_memory_path_checked is True` in addition to the validated `heuristic_memory_probe` sidecar before emitting output, and records `checks.heuristic_memory_probe_checked` in the bridge artifact. Verification: local implementation commit `07e29bc`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 24 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 437 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

# PeTTa Intermediate Memory Store

- [x] The pinned PeTTaChainer source now closes the cause of the isolated fact-conversion doubling: `mm2stmt`'s specialized zero-premise arm and general premise-list arm both match `(() |- ($ccl))`. A source-drift-sensitive inspector records the exact definition and refuses that attribution when either arm changes. Local implementation commit `125cb6e`; focused 60 and full 515 tests passed, plus `py_compile` and `git diff --check`. No upstream semantic change, `mm2compile`/`compileadd`, query result, manifest, promotion/write, or live integration.

- [x] Phase-2 raw captures now have a fail-closed process/result admission boundary. `validate_kernel_capture_result()` requires a zero exit, empty stderr, and a caller-identified result atom present verbatim in bounded stdout before the existing typed validator closes query, STV, stamps, and evidence bases against immutable compiled inputs. Local implementation commit `b2be8c7`; focused 1 and full 500 tests passed, plus `py_compile` and `git diff --check`. EpisodeManifest construction/persistence, rule/trace identity, promotion/write, and live integration remain separate gates.

- [x] Phase-2 kernel capture now contains subprocess descendants as one process session. Timeout, output overflow, and normal direct-process completion kill the full process group before pipe-reader joins, preventing an inherited descendant pipe from extending capture beyond the bounded call. Focused 2 and full 496 tests passed, plus `py_compile` and `git diff --check`; no runtime semantic, promotion/write, or live-integration claim.

- [x] Phase-2 executable pinning now resolves the absolute executable path before both hashing and launch, so a symlink cannot be hashed through one path and then separately re-resolved by process creation. The capture records the resolved argv. Local implementation commit `d73d054`; focused 1 and full 495 tests passed, plus `py_compile` and `git diff --check`. Resolved-file replacement/TOCTOU remains explicitly outside this narrow boundary; no runtime semantic claim, promotion/write, or live integration.

- [x] Phase-2 kernel launch now supports opt-in exact executable SHA-256 pinning. A reviewed caller can require a lowercase digest for an absolute executable file; malformed pins, non-absolute paths, unreadable files, and digest mismatches fail before subprocess creation. Focused and full tests passed (495 total), plus `git diff --check`. This narrows executable provenance but does not eliminate filesystem replacement/TOCTOU risk, validate semantic output, authorize promotion/write, or enable live integration.

- [x] Phase-2 kernel launch now bounds and validates an optional explicit process environment before starting a subprocess. Keys/values must be strings, process-invalid NULs and `=` in keys are rejected, and aggregate UTF-8 input is capped at a positive 64 KiB default. Focused and full tests passed (494 total), plus `git diff --check`. No runtime semantic claim, promotion/write, or live integration.

- [x] Phase-2 kernel launch now bounds and validates the optional working-directory input before starting a subprocess. The runner rejects empty/non-path values, embedded NULs, and UTF-8 paths above a positive 4 KiB default ceiling. Local commit `b49e4ae`; focused 1 and full 493 tests passed, plus `py_compile` and `git diff --check`. This is a resource/launch boundary only: no patham9 execution, trace/rule claim, promotion/write, or live integration.

- [x] Phase-2 kernel launch now bounds the UTF-8 byte size of the complete argv and rejects embedded NULs before starting a subprocess. Local commit `c04bfaa`; focused 2 tests and full 492 tests passed, plus `py_compile` and `git diff --check`. This is a resource/launch boundary only: no patham9 execution in tests, trace/rule claim, promotion/write, or live integration.

- [x] Phase-2 now includes a bounded shell-free kernel subprocess/capture primitive. It accepts explicit argv and an already-assembled program, enforces timeout and per-stream byte ceilings, requires UTF-8 output, and returns raw immutable capture only; semantic result validation and manifest closure remain separate gates. No promotion/write/live integration or rule/trace claim.

- [x] Phase-2 declarative input validation now rejects patham9's own evaluator/control heads (`PLN.Config`, `PLN.Init`, `PLN.Query`, `PLN.Derive`) at any nesting depth in evidence statements and query terms. The head set was derived from pinned local patham9 revision `55f1751`; focused tests and all 488 tests pass, plus `py_compile` and `git diff --check`. No runtime execution or live/write/promotion boundary changed.

- [x] Added an opt-in final-program parse-check boundary to the deterministic stock patham9 query assembler. The hook receives only the complete bounded assembled program, propagates rejection before handoff, and is never invoked when omitted. Focused 47 and full 488 tests passed; `py_compile` and `git diff --check` passed. No kernel execution, rule/trace attribution, promotion/write, or live integration.

- Slug: `petta-memory`
- Status: `active`
- Created: `2026-06-27`
- Last reviewed: `2026-06-27`
- Owner: Benjamin Goertzel

## Purpose

Implement a PLN-ready intermediate PeTTa/MeTTa memory store for ProtomegaTron/OmegaClaw: a bounded symbolic layer between volatile prompt/working memory and broad vector/durable memory.

## Success criteria

- A local software repository implements an append-only `MemoryCluster` journal with deterministic bounded query functions.
- The schema distinguishes observed events, quoted claims, derived beliefs, hypotheses, decisions, commitments, boundaries, artifacts, status events, salience events, and provenance.
- The store exposes separate audit, prompt, and PLN-safe views.
- Raw quoted claims are not exported as PLN factual premises unless explicitly promoted.
- Tests cover valid append, malformed input rejection, cluster metadata requirements, query by id/type/about/status/role, prompt-view bounding, and PLN-view filtering.
- Integration path with OmegaClaw/ProtomegaTron is documented before any live agent write path is enabled.

## Scope

### In scope

- Local-first Python/MeTTa prototype.
- Append-only `.metta` journal format.
- Rebuildable indexes or text scanning.
- Validation strong enough to avoid corrupting the journal.
- Unit tests and small example clusters.
- Later PeTTa/PLN inference smoke tests over normalized atoms.

### Out of scope for v0

- New external authority or autonomous actions.
- Direct Telegram/GitHub/shell integration.
- Paid compute.
- Treating vector memory or project Markdown as canonical source for the symbolic store.
- Upstreaming into OmegaClaw before the local prototype is tested.

## Repository plan

- `iCog-Labs-Dev/metta-attention`: cloned for integration assessment at
  `repos/metta-attention`, inspected at
  `9196f38db749ddedeb591229dffddfa71664c38d` (2026-07-21). Recommended role:
  derived/disposable attention projection over canonical memory and OmegaSelf,
  not a truth store, authority mechanism, or destructive canonical-memory tier.
  Assessment: `docs/metta_attention_integration_assessment.md`.

GitHub repository: `https://github.com/bgoertzel-sing/petta-memory`.

Local repository path: `projects/petta-memory/repos/petta-memory`.

Visibility: public. Created and pushed on 2026-06-27 after Benjamin confirmed the recommended repo name/visibility.

## Current state

- [!] ProtoCosmo2 takeover documentation and a frozen-worktree verification run
  were completed 2026-08-10. The handoff worktree remains at `5b842f4`; the
  branch is 352 commits ahead of its configured upstream. A fresh suite run
  collected 698 tests but ended with one failure, one error, and eight skips
  because the isolated layout does not resolve at least one pinned sibling
  dependency path (and the provider-free patham9 gate emitted no semantic pass
  marker). Normalize dependency paths before accepting the historical clean
  698-pass baseline. Report/guide: `docs/handoff-2026-08-10/`; run evidence:
  `experiments/20260810T145211Z-protocosmo2-handoff-full-suite/`.

- [x] The PeTTaChainer fact branch is now decomposed beneath the 256-copy `compile` result. A source-gated bounded probe found `compile-fact-kb` returns eight copies of one unique `(kb MAIN Nil)` term, while `compile-outputs` returns zero adapters for the exact promoted fact. Local implementation commit `cbdb5de`; focused 69 and full 524 tests passed, plus `py_compile` and `git diff --check`. This explains one 8x factor but does not change upstream semantics or admit `compile`, `mm2compile`, `compileadd`, query, promotion/write, or live integration.

- [x] PeTTaChainer `mm2stmt` conversion and temporary-context inspection are now isolated from the already-observed compiler fan-out. A single source-equivalent fact clause converted in 0.469 s into two copies of one unique expected fact, and a separately cleared/read `ctx` remained empty; runtime initialization emitted 797,385 stdout and 168 stderr characters. Local implementation commit `4cca4cd`; focused 58 and full 513 tests passed, plus `py_compile` and `git diff --check`. This is diagnostic only: `compile`, `mm2compile`, `compileadd`, query/result admission, manifests, promotion/write, and live integration remain gated.

- [x] The exact compiler-emitted PeTTaChainer contract now has a bounded source-gated `compile` fact-dispatch probe below materialization and above `mm2compile`. It completed in 0.502 s but returned 256 copies of one unique base-fact clause and generated 796,897 stdout characters; retained samples are capped at 16. Local implementation commit `3ba8d3a`; focused 54 and full 509 tests passed, plus `py_compile` and `git diff --check`. This localizes duplicate fan-out before `mm2compile` context collection; no add/query result, manifest, promotion/write, or live integration was admitted.

- [x] Exact compiler-emitted PeTTaChainer add-path diagnosis now separates materialization from `mm2compile`. The one-statement lambda-free contract materialized as identity in 0.479 s, but produced 512 copies of one unique atom and 796,938 stdout characters; the next direct `mm2compile`/collapse rung timed out at 5 s. The profiler now retains counts plus at most 16 result samples instead of serializing the complete duplicate list. Local implementation commit `312efc2`; focused 51 and full 506 tests passed, plus `py_compile` and `git diff --check`; `compileadd`, query/result admission, manifest construction, promotion/write, and live integration remain gated.

- [x] The exact typed PeTTaChainer contract now has a bounded fail-closed runtime probe in local commit `d9ee9f5`. Public statement/query validators must return exact numeric `1.0` before isolated add/query, and timeout/error/malformed stages/empty answers cannot admit a result. Pinned local PeTTaChainer `e4db5ca` validated one exact contract but timed out in combined `compileadd`/query at 15 seconds. Focused 49 and full 504 tests passed, plus `py_compile` and `git diff --check`; no manifest, promotion/write, or live integration.

- [x] The first generic PeTTaChainer boundary now has an explicit deterministic input contract. `build_pettachainer_episode_contract()` maps immutable compiler Sentences to checked-add statements `(: pm-<full-sentence-digest> term (STV strength confidence))` and query `(: $prf term $tv)`, retaining patham9 stamps/evidence bases as typed audit sidecars. Local PeTTaChainer `check_stmt`/`check_query` returned `1.0` for the exact shapes; focused 60 and full 501 tests passed, plus `py_compile` and `git diff --check`. `compileadd`, query execution/result decoding, manifest construction, promotion/write, and live integration remain gated.

- [x] Phase-2 captures now commit to the exact complete program delivered on stdin, and captured manifest construction fails closed if that commitment differs from the supplied `complete_program`. Local implementation commit `904b707`; focused 60 and full 501 tests passed, plus `py_compile` and `git diff --check`. Real compiled-input inference, manifest persistence, rule/trace identity, promotion/write, and live integration remain separate gates.

- [x] Phase-2 launch byte ceilings now count OS framing (`NUL` per argv/cwd and `KEY=VALUE\0` environment entries), and executable pinning rechecks argv size after symlink resolution so a longer resolved pathname cannot bypass the pre-launch budget. Local implementation commit `5d637c7`; focused 4 and full 497 tests passed, plus `py_compile` and `git diff --check`. No patham9 inference, memory write/promotion, trace/rule claim, or live integration.

- [x] Phase-2 kernel capture now enforces its per-stream byte ceiling while reading and terminates an overflowing child, instead of buffering arbitrary output before checking. Concurrent stdin writing preserves the timeout boundary for children that do not consume large input. Local implementation commit `9899b1d`; full 495-test discovery passed, plus `py_compile` and `git diff --check`; no runtime semantic, promotion/write, or live-integration claim.

- [x] Phase-2 now has deterministic bounded stock patham9 query-program assembly in local commits `e0e2c16` and `9dc338b`. The assembler accepts only immutable compiler-emitted Sentences plus one canonical declarative query, supplies fixed PLN import/init/query controls, and enforces positive limits, a 10,000-step ceiling, a 100,000-entry ceiling for each queue, and total program-size bound. Focused 47 and full 488 tests passed; `py_compile` and `git diff --check` passed. It returns inert text only: no subprocess, trace/rule attribution, promotion/write, or live integration.

- [x] Phase 2 now has a complete typed SDS section 16.2 `EpisodeManifest` audit artifact in local commit `a8858d5`. It closes chart/snapshot/compiler/result identities, content-addresses the bounded supplied complete program and stamp map, records kernel/controller policy identities, seed/budget/timestamps/process outputs, and persists create-once with inner and outer digest validation. Every compiled Sentence and the validated query must occur in the program. Focused 46 and full 487 tests passed; `py_compile` and `git diff --check` passed. This captures a supplied run but does not execute patham9, decode rule/trace identity, promote a belief, write memory, or enable live integration.

- [x] Added an exact semantic replay-comparison gate for Phase-2 kernel outputs. `validate_exact_kernel_replay()` first closes the persisted expected result against the immutable compiled episode, validates a fresh bounded raw result through the existing parser, and requires identical typed result digest across query, truth value, stamps, and evidence bases. Local implementation commit `e979d52`; focused 44 tests and full 485 tests passed; `py_compile` and `git diff --check` passed. This compares supplied output only: it does not execute patham9, establish rule/trace identity, promote a belief, write memory, or enable live integration.

- [x] Validated Phase-2 patham9 result values now have a create-once checksummed persistence boundary. Reload requires exact episode/chart identity and stamp-derived evidence-basis closure against the immutable compiled inputs, and rejects recomputed-checksum semantic drift, unknown stamps, malformed collections, and unexpected envelope fields. Local implementation commit `0e8942d`; focused 43 tests and full 484 tests passed; `py_compile` and `git diff --check` passed. No runtime execution, trace/rule claim, complete manifest, promotion/write, or live OmegaClaw/GoalChainer integration.

- [x] Evidence snapshot v2 closes packet content into later compilation: each complete frozen packet has a canonical digest, the snapshot fingerprint derives from the ordered digest commitments and semantic context, and episode compilation rejects changed packet content even when packet and snapshot IDs are reused. Local implementation commit `ab7a50c`; focused 39 tests and full 480 tests passed; `py_compile` and `git diff --check` passed. No runtime derive/query, write/promotion, `compileadd`, patham9 source change, or live integration.

- [x] Completed the Atlas Phase-1 prior-cycling and compatibility-label boundaries. Canonical beta inversion/prior cycling is committed as `e7073cc`; the older patham9 `ec_projected_stv()` is explicitly labeled `adapter-weighted-v1` without changing serialized result dictionaries in `8b4ac1d`. Full unittest discovery passed 470 tests and `git diff --check` passed. No runtime derive, memory write/promotion, PeTTaChainer `compileadd`, patham9 source change, or live OmegaClaw/GoalChainer integration.

- [x] Current progress slice hardened the read-only `live-goal-bridge --run-patham9-runtime` semantic-marker audit boundary. The bridge now rejects patham9 runtime semantic marker counts that are boolean, non-integer, negative, missing for pass/fail counts, or semantically inconsistent (`passed_true_count <= 0`, nonzero false/error markers) before GoalChainer appraisal. Verification: local implementation commit `d75c466`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe/check consistency boundary. The bridge now rejects copied GoalChainer `checks.no_task_or_directive_claim` when present but not `True`, and rejects malformed optional `heuristic_memory_probe.parsed_memory_items` counts (bool/non-int/non-positive) before emitting output. Verification: local implementation commit `9f8d311`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 27 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 440 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer copied-sidecar boundary against nested directive/task-claim fields. The bridge now recursively rejects directive-shaped keys (`claim`, `task_claim`, `directive_claim`, `directive_report`, `plan`, `task_states`, `next`, `skill`) anywhere inside copied GoalChainer result/decision payload/checks/probe/decision/evidence/contextual-evidence containers before emitting output, so nested metadata cannot smuggle directive/task-claim artifacts through audit sidecars. Verification: local implementation commit `ca220ce`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.


- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer nested decision-evidence directive/task-claim sidecar boundary. The bridge already rejected directive/task-claim-shaped fields at the top-level GoalChainer result, decision payload, checks block, heuristic probe, and individual decisions; it now also rejects those fields inside copied `decision.evidence` objects and each `evidence.contextual_evidence` entry before emitting output. Verification: local implementation commit `84dc0c9`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- [x] Current progress slice hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe sidecar boundary. The bridge already rejected directive/task-claim-shaped fields at the top-level GoalChainer result, decision payload, checks block, and individual decisions; it now also rejects those fields inside the copied `heuristic_memory_probe` sidecar before emitting output. Verification: local implementation commit `9ca7ed0`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer checks sidecar boundary. The bridge already rejected directive/task-claim sidecars at the top-level GoalChainer result, `decision_payload`, and individual decision records; it now also rejects the same directive-shaped fields inside the copied `checks` block before emitting output. Verification: local implementation commit `9f3d241`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 26 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 439 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer per-decision directive/task-claim sidecar boundary. The bridge already rejected directive-looking fields at the GoalChainer result and decision-payload levels; it now also rejects those fields inside individual decision records before emitting output, so a downstream adapter cannot smuggle directive reports through a recommended/candidate decision sidecar. Verification: local implementation commit `0ee7260`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 25 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 438 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer directive/task-claim sidecar boundary. The bridge now rejects GoalChainer result or decision-payload fields that look like live directive/task-claim artifacts (`claim`, `task_claim`, `directive_claim`, `directive_report`, `plan`, `task_states`, `next`, `skill`) before emitting output, so a directive-capable adapter cannot smuggle task-claim sidecars through a read-only bridge artifact. Verification: local implementation commit `7b96891`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 25 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 438 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe check boundary. When `include_heuristic_memory_probe=True`, the bridge now requires downstream GoalChainer `checks.heuristic_with_memory_path_checked is True` in addition to the validated `heuristic_memory_probe` sidecar before emitting output, and records `checks.heuristic_memory_probe_checked` in the bridge artifact. Verification: local implementation commit `07e29bc`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 24 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 437 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket finite-number boundary. The bridge now rejects NaN/Infinity in contextual `support`/`opposition` EC counts and optional `derived_strength`/`derived_confidence` truth values before emitting an OmegaClaw-facing bridge artifact. Verification: local implementation commit `3d8aa4a`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket truth/provenance boundary. Decision `evidence.contextual_evidence` entries, when present, must now preserve optional derived truth values as bounded non-bool numbers in `[0,1]` and required non-empty string `belief_id`, `cluster_id`, and `promotion_event` provenance before bridge output is emitted, so malformed EC-derived appraisal summaries cannot cross into future OmegaClaw/operator-facing artifacts. Verification: local implementation commit `4bda953`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer contextual EvidencePacket EC-count boundary. Decision `evidence.contextual_evidence` entries, when present, must now include numeric non-bool, non-negative `support` and `opposition` counts before bridge output is emitted, so malformed EC summaries cannot cross into future OmegaClaw/operator-facing artifacts. Verification: local implementation commit `183b586`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer contextual-evidence audit boundary. Decision `evidence.contextual_evidence` sidecars, when present, must now be list-shaped and contain only object entries before bridge output is emitted, so malformed contextual EvidencePacket summaries cannot cross into future OmegaClaw/operator-facing artifacts. Verification: local implementation commit `477ce0a`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer decision evidence proof boundary. When a downstream decision includes `evidence.proofs`, every proof entry must now be a non-empty string; malformed object/empty proof entries fail closed before bridge output is emitted. Verification: local implementation commit `6eed79a`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer decision-evidence boundary for actionless decisions. Decision `evidence` sidecars are now validated for every decision record, even candidate/held/weak/blocked records that do not carry an `action_id`, so malformed non-object evidence or non-list `evidence.proofs` cannot bypass validation via the no-action-id path. Verification: local implementation commit `39c52f5`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer decision-evidence boundary. After validating decision statuses and action IDs, the bridge now rejects any decision `evidence` sidecar that is not object-shaped and any nested `evidence.proofs` field that is not list-shaped before emitting a bridge artifact. Verification: local implementation commit `adf97f6`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 22 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 435 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer heuristic-memory-probe boundary. When a downstream GoalChainer runner includes `heuristic_memory_probe`, the bridge now requires an object-shaped probe with non-empty string `schema`, `mode`, and `boundary`, plus exact `memory_proof_present is True` and `leak_check_safe is True`, before emitting an OmegaClaw-facing bridge artifact. Regression coverage proves malformed probe shape/metadata, missing memory proof, and unsafe leak-check claims fail closed. Verification: local implementation commit `5d3a9cc`; focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 21 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 434 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer decision-status boundary. After validating object-shaped decision entries, the bridge now requires every decision `status` to be a non-empty string from the known GoalChainer review vocabulary (`recommended`, `candidate`, `held`, `weak`, `blocked`) before selecting/emitting the recommended action, preventing malformed or newly invented statuses from crossing into the OmegaClaw-facing bridge artifact. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 20 tests; local implementation commit `0d376e9`; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 433 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardened the read-only `live-goal-bridge` GoalChainer decision action-id boundary. The bridge now rejects malformed non-empty/non-string `action_id` values on any decision record and rejects duplicate decision `action_id` values before emitting a bridge artifact, preventing ambiguous recommended/candidate drift for the same action. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 19 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 432 tests; `git diff --check` passed; local implementation commit `9559372` (not pushed). Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer recommendation boundary. The bridge now rejects multiple `status: recommended` decisions from the GoalChainer runner instead of silently selecting the first one, preserving a single auditable recommended action before future OmegaClaw review. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 19 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 432 tests; `git diff --check` passed; local implementation commit `7daf7c3` (not pushed). Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer boundary-check contract. After validating object-shaped GoalChainer output, the bridge now requires downstream `checks.no_memory_write is True` and `checks.no_live_directive_or_task_claim is True` before emitting a bridge artifact, so a malformed/incomplete GoalChainer adapter cannot be converted into a top-level bridge record that still claims no writes/task claims. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 18 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 431 tests; `git diff --check` passed; local implementation commit `11e98c8` (not pushed). Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer output boundary against malformed notes and recommended-decision drift. `decision_payload.notes` must now be list-shaped when present, and any recommended decision must include a non-empty string `action_id` before bridge output is emitted. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 17 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 430 tests; `git diff --check` passed; local implementation commit `4d6b1f4` (not pushed). Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only live bridge patham9 runtime top-level audit boundary. When `live-goal-bridge --run-patham9-runtime` receives a `passed` patham9 result, it now also requires a non-empty string result `schema` and exact integer `returncode: 0` before GoalChainer appraisal; bool, string, missing, or nonzero returncodes fail closed. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 15 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 428 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice hardens the read-only live bridge patham9 runtime audit boundary. When `live-goal-bridge --run-patham9-runtime` receives a `passed` patham9 result, it now also requires object-shaped `semantic_markers`, `semantic_passed: true`, an object-shaped `program`, and a non-empty string program schema before GoalChainer appraisal. Malformed audit fields now fail closed before recommendations are produced. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 14 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 427 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

- Current progress slice fixes the ThreadKeeper canary GoalChainer scenario so PR reconciliation is only modeled as an immediate required action when PR-reconciliation evidence is actually present in the handoff. A new regression proves canary-only admitted patham9 evidence recommends `install_threadkeeper_canary_on_protomegabot` directly and does not synthesize/default a `reconcile_threadkeeper_pr` action. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_goalchainer_smoke -v` passed 8 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 426 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice wires the ThreadKeeper project-control fixture through patham9-admitted evidence back into GoalChainer appraisal. `live-goal-bridge` now passes the admitted pi-PLN handoff into the precompiled GoalChainer gate; GoalChainer builds a dynamic ThreadKeeper project-control scenario when it sees the canary/reconciliation evidence, recommending `reconcile_threadkeeper_pr` immediately, keeping `install_threadkeeper_canary_on_protomegabot` as the next candidate/admissible action, and blocking redundant `ask_ben_again` / premature `remove_threadkeeper`. Runtime artifact: `repos/petta-memory/artifacts/live_goal_bridge_threadkeeper_feedback_20260709T135138Z/result.json` sha256 `40987bab24fa59414949bda89aa532280b4bcbacc64baacbb758535a54fb8749`. Verification: focused live-bridge tests passed 13 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 425 tests; `py_compile` and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no OmegaClaw skill/task claim.
- Current progress slice adds a ThreadKeeper canary/project-control fixture to the read-only live bridge validation path. `fixtures/threadkeeper_canary_decision.metta` now exercises promoted project-control evidence through journal -> PeTTaChainer handoff cache -> patham9/PLN handoff -> ranked/admitted gate -> optional patham9 runtime gate -> GoalChainer runner, with a regression proving query-relevance admits only `(Acceptable install_threadkeeper_canary_on_protomegabot)` before GoalChainer appraisal while the full GoalChainer handoff still preserves all promoted evidence items. Focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 12 tests; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 424 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice hardens the read-only live bridge against malformed GoalChainer scalar metadata. After object/container validation, `live-goal-bridge` now requires non-empty string `schema`, `mode`, and `boundary` fields from the GoalChainer runner before emitting a bridge artifact, converting missing/edited metadata into explicit `ValidationError`. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` (11 tests), full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (423 tests), and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice hardens the read-only live bridge against malformed GoalChainer decision-list drift. After requiring object-shaped GoalChainer result/payload/checks, `live-goal-bridge` now also rejects non-list `decision_payload.decisions` and non-object decision entries before selecting the recommended action, converting another possible malformed downstream gate shape into explicit `ValidationError`. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` (10 tests), full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (422 tests), and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice hardens the read-only live bridge after GoalChainer appraisal against malformed injected/local GoalChainer runner output. `live-goal-bridge` now requires GoalChainer to return object-shaped result, object-shaped `decision_payload`, and object-shaped `checks` before emitting a bridge artifact, converting malformed downstream-gate drift into `ValidationError` instead of incidental `KeyError`/attribute errors. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` (8 tests), full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (420 tests), and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice further hardens the read-only live bridge patham9 runtime boundary against malformed runner output. `live-goal-bridge --run-patham9-runtime` now requires the injected/local patham9 runtime gate to return an object before any GoalChainer appraisal, converting non-object runner drift into `ValidationError` and proving GoalChainer is not called. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` (5 tests), full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (417 tests), and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.
- Current progress slice hardens the read-only live bridge fail-closed boundary for the optional patham9/PLN runtime gate. When `live-goal-bridge --run-patham9-runtime` is enabled, a non-`passed` runtime smoke now raises `ValidationError` before GoalChainer appraisal, preventing downstream recommendations from being produced from a failed admitted-handoff proof gate. A test-injected GoalChainer runner verifies it is not called after patham9 failure. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v`, full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (416 tests), and `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no OmegaClaw skill/task claim.
- Current progress slice wires the read-only `live-goal-bridge` to optionally run local patham9/PLN over the admitted pi-PLN handoff with `--run-patham9-runtime`, bypassing PeTTaChainer `compileadd` for runtime proof. Artifact `repos/petta-memory/artifacts/live_goal_bridge_patham9_runtime_2026-07-08T1813Z.json` (sha256 `7777b0269807d12c218bd135dcaa401cafae718df6df7649f63f76cc6dfc3eb5`) records: 1 admitted patham9 item, bounded multi-sentence derivation smoke passed with semantic `Passed: true`/returncode 0, and GoalChainer recommended `publish_redacted_summary`; boundaries preserved: no memory write, no inferred-belief promotion, no OmegaClaw skill/task claim, no PeTTaChainer `compileadd`. Verification: `py_compile`, 415 unittest tests, and `git diff --check` passed.
- Current progress slice adds the first read-only live bridge from a `MediumMemoryStore` journal into local GoalChainer. New `live-goal-bridge` CLI consumes an append-only journal, builds the pi-PLN ranked/admitted handoff gate, and runs GoalChainer appraisal with the heuristic memory probe while preserving boundaries: no OmegaClaw skill loaded, no directive/task claim, no memory write, no inferred-belief promotion. Artifact `repos/petta-memory/artifacts/live_goal_bridge_2026-07-08T1830Z.json` recommends `publish_redacted_summary` from 2 GoalChainer evidence items and 1 admitted pi-PLN branch. Verification: `py_compile`, full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (414 tests), and `git diff --check` passed.
- Current progress slice hardened the non-live ranked/admitted inference-control gates against boolean/non-integer audit metadata drift. `ranked_inference_control_plan()` now rejects bool/non-integer source `item_count` before estimator/controller dispatch. `ranked_plan_admitted_handoff()` now rejects bool/non-integer top-level counts (`input_count`, `recommended_count`, `held_count`, `candidate_count`) and bool rank/item-index keys before branch-plan mirror checks or admitted premise copying. Focused ranked-plan tests pass 40 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 412 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live ranked inference-control plan gate against malformed source handoff drift before estimator/controller wrapper dispatch: `ranked_inference_control_plan()` now rejects non-list `items` and `item_count` mismatches before constructing the reviewed branch plan, preventing hidden count/container drift in the artifact that feeds `ranked_plan_admitted_handoff()`. Focused ranked-plan tests pass 35 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 407 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against malformed handoff item-record drift: `ranked_plan_admitted_handoff()` now rejects non-object source handoff `items` entries before branch-plan/source mirror checks or admitted-item copying, turning another possible malformed-plan `AttributeError` path into explicit `ValueError` audit failure. Focused ranked-plan tests pass 33 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 405 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against malformed container types before iteration: `ranked_plan_admitted_handoff()` now rejects non-list source handoff `items` and non-list `recommended_branches`, `held_branches`, or `branch_plan` partitions before count/mirror validation, turning a possible malformed-plan `AttributeError` path into explicit `ValueError` audit failures. Focused ranked-plan tests pass 31 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 403 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against ranked-plan rank-gap/order drift: `ranked_plan_admitted_handoff()` rejects audited `branch_plan` ranks that are not contiguous `1..candidate_count` before copying any admitted premises. Focused ranked-plan tests pass 29 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 401 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against duplicate rank/key drift across the audited plan and held partition: `ranked_plan_admitted_handoff()` rejects duplicate `branch_plan` ranks even when item indexes differ, plus duplicate held-branch ranks/items before any recommended premise is copied. Focused ranked-plan tests pass 27 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 399 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against stale source-handoff drift across the full audited branch plan: `ranked_plan_admitted_handoff()` now rejects `input_count` mismatches, `branch_plan` item indexes outside the handoff, and branch-plan `belief_id`/`term` mismatches against the current source handoff item before copying any admitted premises. Focused ranked-plan tests pass 23 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 395 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime invoked by the new gate, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against held-partition drift: `ranked_plan_admitted_handoff()` now rejects `held_branches` entries whose status is not `held` and requires each held branch to mirror the audited `branch_plan` by rank, item index, belief id, term, and status. Focused ranked-plan tests pass 20 cases; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 392 tests; `git diff --check` passed. Boundary remains non-live: no SWI/PeTTa/MeTTa runtime, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against malformed full-branch-plan records outside the recommended/held partition: `ranked_plan_admitted_handoff()` now rejects `branch_plan` entries with invalid status values and malformed rank/item-index key fields before copying admitted premises into a future derive handoff. Focused ranked-plan tests pass 18 cases; full stdlib unittest suite passes 390 tests; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff pre-derive gate against malformed `branch_plan` totals and partition drift: `ranked_plan_admitted_handoff()` now rejects `candidate_count` mismatches, duplicate `branch_plan` rank/item keys, and branch-plan recommended/held status counts that do not mirror the reviewed recommendation lists, in addition to the existing stale handoff and recommendation-list checks. Focused ranked-plan tests pass 16 cases; full stdlib unittest suite passes 388 tests; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against malformed ranked-plan counts and spliced recommendation records: `ranked_plan_admitted_handoff()` now rejects mismatched `recommended_count`/`held_count` values and requires each admitted recommendation to be mirrored consistently in `branch_plan` by rank, item index, status, belief id, and term. Focused ranked-plan tests pass 13 cases; full unittest suite passes 385 tests; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate against malformed recommended-list status: `ranked_plan_admitted_handoff()` rejects any item under `recommended_branches` whose branch status is not `recommended`, preventing copied/edited held branches from entering a later reviewed derive handoff. Focused ranked-plan tests pass 11 cases; full unittest suite passes 383 tests; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice hardens the non-live admitted-handoff gate by rejecting stale ranked plans where a recommended branch's source handoff item keeps the same `belief_id` but changes `term`; admission records now include the admitted term for audit before any future reviewed derive gate. Focused ranked-plan tests pass 9 cases; full unittest suite passes 381 tests; `git diff --check` passes. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice exposes the admitted-handoff subset as a non-live CLI gate: `pi-pln-admitted-handoff` composes store handoff -> `ranked_inference_control_plan()` -> `ranked_plan_admitted_handoff()` and emits only recommended branches in the existing patham9/PLN handoff schema for a later separately reviewed derive gate. README and CLI regression cover append-only store -> ranked plan -> admitted subset, preserving the no-runtime/no-derive boundary. Verification passes 380 stdlib unit tests plus `git diff --check`. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append beyond temp test stores, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice exposes the ranked inference-control plan as a non-live CLI gate: `pi-pln-ranked-plan` builds the store handoff and runs `ranked_inference_control_plan()` with estimator/controller thresholds, query relevance gating, reproducible seed, and branch caps. README documents this as the pre-`PLN.Derive` plan artifact. CLI round-trip coverage verifies store -> handoff -> ranked plan recommends the promoted `b1` branch while preserving the no-runtime/no-derive boundary. Verification passes 377 stdlib unit tests plus `git diff --check`. No SWI/PeTTa/MeTTa runtime invoked, no `PLN.Query`/`PLN.Derive`, no memory append beyond temp test stores, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path.
- Current progress slice adds a non-live ranked inference-control plan gate in `repos/petta-memory`: `ranked_inference_control_plan()` composes the PLN estimator/EDCall ranking with the continuation-predicate controller before any future `PLN.Derive` call. The gate returns recommended vs held branches with estimator probabilities, query relevance, controller decisions/checks, and explicit hold reasons (estimator threshold, query irrelevance, controller rejection/termination, missing controller decision). Tests add 5 unit cases plus a store -> handoff unified integration case that recommends only the high-support `MemoryTarget0` branch while holding irrelevant/conflicting branches. No SWI/PeTTa/MeTTa runtime invoked, no PLN.Query/PLN.Derive call, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 376 stdlib unit tests plus `git diff --check`.
- Current progress slice adds a unified inference-control integration test: `StoreRoundTripUnifiedInferenceControlTests` in `repos/petta-memory` exercises all eight inference-control patterns from the trueagi-io/chaining survey against a single realistic 4-belief store fixture with diverse domains (memory-architecture, reasoning, planning), STVs (0.92/0.80 high-support through 0.45/0.30 low-confidence), and EC counts (including conflicting 2/8 evidence). The fixture flows through the full pipeline: store -> pettachainer_handoff_cache -> patham9_pln_handoff_sentences -> each inference-control wrapper. Tests validate handoff diversity, per-pattern correctness on the richer input (probabilistic filter ranking and strict-threshold filtering, context selection domain isolation, chained pipeline composition, meta-learning shortcut preference, continuation predicate rejection of low-confidence, controlled backward chainer rejection and depth termination, PLN estimator ranking and EC ratio filtering, controller-as-chainer confirmation and rejection), and provenance preservation across all patterns. Local commit `a448fe6`. 10 new tests. No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 370 stdlib unit tests plus `git diff --check`.
- Current progress slice adds the first long-term inference-control mechanism for pi-PLN: `pln_estimator_wrapper()` in `repos/petta-memory` implements the long-term "PLN-based inference controller" pattern from the trueagi-io/chaining inference-control survey (commit `cd18b51`). The wrapper converts each handoff Sentence into PLN viability prior parameters (alpha/beta) derived from EC support/opposition counts when available, or from STV strength × confidence when EC is absent. It then Thompson-samples from the Beta(alpha, beta) posterior to produce sampled viability scores, and ranks branches by sampled viability into EDCall (Estimated Delayed Call) records for PLN.Derive exploration. The exploration_weight parameter controls the exploration/exploitation tradeoff by shrinking Beta parameters toward uniform Beta(1,1). CLI: `pi-pln-estimator`. Tests: 35 new tests (34 in `PlnEstimatorWrapperTests` covering schema, mode, boundary, sorting, EDCall structure, reproducibility, EC/STV prior sources, mean viability, sampling range, min_strength/confidence/domain/rule/ec-ratio filters, query target relevance, max_branches, empty handoff, validation, exploration weight scaling and variance, source pattern, policy structure, rejected items; 1 in `StoreRoundTripPlnEstimatorTests` covering store -> handoff -> PLN estimator round-trip with real promoted beliefs). No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 329 stdlib unit tests plus `git diff --check`.
- Current progress slice adds the fourth concrete inference-control mechanism: meta-learning benchmark. `build_meta_learning_benchmark_handoff()` and `run_meta_learning_benchmark()` in `repos/petta-memory` implement the near-term "meta-learning benchmark" pattern from the trueagi-io/chaining inference-control survey (commit `cd18b51`), inspired by the OpenCog classic meta-learning experiment. The benchmark creates a synthetic shortcut-vs-chain handoff (high-confidence direct belief vs lower-confidence transitive chain) and runs both the probabilistic inference filter and the chained inference-control pipeline against it, verifying the shortcut is correctly ranked first. CLI: `pi-pln-meta-learning-benchmark`. Tests: 27 new tests (10 in `MetaLearningBenchmarkHandoffTests`, 14 in `MetaLearningBenchmarkRunTests`, 1 in `StoreRoundTripMetaLearningBenchmarkTests` plus 2 existing store round-trip test classes). No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 252 stdlib unit tests plus `git diff --check`.
- Current progress slice adds the second inference-control mechanism for pi-PLN: `context_selection_wrapper()` in `repos/petta-memory` implements the near-term "context selection" pattern from the trueagi-io/chaining inference-control survey (commit `cd18b51`). Before sending Sentences to the patham9/PLN chainer, the wrapper filters contextual EvidencePackets by domain, cluster_id, or promotion_rule, and scores each remaining packet by an evidence-weighted relevance formula: `evidence_weight = (support + opposition) / (support + opposition + 2)`. Packets below a `min_packet_relevance` threshold are filtered out. Items with no EvidencePackets pass through unchanged. CLI: `pi-pln-context-select`. Tests: 16 new tests (15 in `ContextSelectionWrapperTests` covering schema, no-filter, domain/cluster/promotion_rule filters, no-match, min relevance, empty handoff, validation, boundary, policy criteria, packet summaries, combined filters, no-packet items) plus 1 in `StoreRoundTripContextSelectionTests` (store -> handoff -> context selection round-trip with real promoted beliefs). No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 208 stdlib unit tests plus `git diff --check`.
- Current progress slice adds the first concrete inference-control mechanism for pi-PLN: `probabilistic_inference_filter()` in `repos/petta-memory` implements the near-term "probabilistic filtering" pattern from the trueagi-io/chaining inference-control survey (commit `cd18b51`). The filter takes a `petta-memory-patham9-pln-handoff-v1` handoff, applies the already-tested EC projection formula to each Sentence, computes a composite score `(projected_strength * projected_confidence)`, and filters/ranks Sentences by `min_confidence` threshold and/or `top_k` before loading into the patham9/PLN chainer. CLI: `pi-pln-inference-filter`. Tests: 16 new tests in `ProbabilisticInferenceFilterTests` (filter schema, counts, EC projection, ranking, confidence threshold, top_k, combined filter, empty handoff, validation, boundary, policy) plus `StoreRoundTripInferenceFilterTests` (store -> handoff -> filter round-trip with real promoted beliefs). No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 192 stdlib unit tests plus `git diff --check`.
- Current progress slice adds local commit `cd18b51` with a trueagi-io/chaining inference-control pattern survey for pi-PLN wrapper. `survey_trueagi_chaining_inference_control()` and CLI `trueagi-inf-ctl-survey` map six concrete inference-control patterns from the checked-out trueagi-io/chaining repo (commit `bc9beb2`) to pi-PLN wrapper extension points: (1) PLN-based inference controller with Thompson sampling, (2) controlled backward chainer with context updaters and termination predicate, (3) meta-learning inference control benchmark, (4) controller-as-chainer (termination via another backward chainer), (5) continuation predicate (opt-in branch justification), (6) probabilistic backward chaining (ProbLog-inspired). All six patterns can be adopted at the wrapper boundary without modifying patham9/PLN source. Patterns categorized by adoption complexity: near-term (probabilistic filtering, meta-learning benchmark), medium-term (controlled chainer, continuation predicate), long-term (PLN estimator, controller-as-chainer). Tests: 8 new tests in `TrueagiChainingInferenceControlSurveyTests`. Verification: 176 tests pass; `git diff --check` passes.
- Current progress slice adds local commit `4650d42` with conflicting-EC and derivation EC projection smokes in `repos/petta-memory`. The conflicting-EC smoke verifies the wrapper formula lowers strength: strong base STV (0.94, 0.80) with opposing EC (1, 9) drops projected strength to 0.511429 while confidence rises to 0.833333. The derivation EC projection smoke extends to two-premise derivation: direct produces `((stv 0.9118 0.666) (0 1))` while projected produces `((stv 0.90660894 0.7499997) (0 1))`, confirming the formula influences derived results. Runtime artifacts: `artifacts/patham9_pln_ec_conflicting_projection_smoke_2026-07-05T1800Z.json` sha256 `e64d3abff53e8d8dff5e7ec62747c5b6192e9bf906cb68f5018f0a52440c3c2f` and `artifacts/patham9_pln_derivation_ec_projection_smoke_2026-07-05T1800Z.json` sha256 `c6a3134108bf8f613e22202646992f5a2c54784dec40ec46ee233a87341f9210` both pass. No memory append, inferred-belief promotion, patham9 source patch, OmegaClaw/GoalChainer live path was invoked. Verification passes 142 stdlib unit tests plus `git diff --check`.
- Current progress slice adds the first non-live wrapper-level EC projection formula gate for patham9/pi-PLN in `repos/petta-memory`: `ec_projected_stv(...)`, `patham9_pln_ec_projection_smoke_program(...)`, `run_patham9_pln_ec_projection_smoke(...)`, and CLI `patham9-pln-ec-projection-smoke` compare direct STV versus projected STV query smokes using a confidence-weighted blend formula. Runtime artifact `projects/petta-memory/artifacts/patham9_pln_ec_projection_smoke_2026-07-05T1600Z.json` sha256 `f6802b2b661273ec1fd09c4970142b54d660e63d56d99e92abcf218a6f67f23e` passed both direct (`(stv 0.91 0.74)`) and projected (`(stv 0.904703 0.833333)`) query smokes for `(Acceptable publish_redacted_summary)` with EC `(9 1)` support. The wrapper pre-projects contextual EvidencePacket counts into a blended STV before invoking patham9/PLN, keeping the chainer core unmodified. No memory append, inferred-belief promotion, patham9 source patch, OmegaClaw/GoalChainer live path was invoked. Verification passes 135 stdlib unit tests plus `git diff --check`.
- Current progress slice adds local commit `835bd50` with the second medium-term inference-control pattern for pi-PLN: `controlled_backward_chainer()` in `repos/petta-memory` implements the "controlled backward chainer" pattern from the trueagi-io/chaining inference-control survey. It builds on the continuation predicate by iterating it across simulated derivation steps with context updaters (accumulate_depth, accumulate_ec, fixed) that track depth and EC accumulation between steps, max_steps/max_branches safety caps, and a full derivation trace showing per-step decisions (continue/terminate/reject). CLI: `pi-pln-controlled-chainer`. Tests: 18 new tests (17 in `ControlledBackwardChainerTests` covering schema, boundary, all-continue-then-terminate, strength/confidence/domain/ec-ratio/promotion-rule filters, max_steps, accumulate_ec mode, fixed context mode, max_branches cap, empty handoff, validation errors, step trace structure, terminated branch structure, source pattern; 1 in `StoreRoundTripControlledBackwardChainerTests` covering store -> handoff -> controlled backward chainer round-trip with real promoted beliefs). No SWI/PeTTa/MeTTa runtime invoked, no memory append, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw/GoalChainer live path. Verification passes 294 stdlib unit tests plus `git diff --check`.
- Current progress slice adds a bounded non-live two-premise patham9/PLN derivation smoke in `repos/petta-memory`: `patham9_pln_derivation_smoke_program(...)`, `run_patham9_pln_derivation_smoke(...)`, and CLI `patham9-pln-derivation-smoke` load one generated promoted handoff Sentence plus one synthetic bridge implication into the local patham9/PLN chainer, requiring actual derivation rather than direct recall. Runtime artifact `projects/petta-memory/artifacts/patham9_pln_handoff_derivation_smoke_2026-07-05T1200Z.json` sha256 `7352b59ffec908f9752f174fc7c7102c5d5ce737589fe16bfe19314bfdd9e545` passed for `(PMDerivedFromHandoff (Acceptable publish_redacted_summary))` with result `((stv 0.9118 0.666) (0 1))`. Numeric runtime stamps remain mapped back to PMEvidence/synthetic-bridge provenance in the sidecar. Also fixed the existing query-smoke timeout path to classify using the bounded returncode instead of referencing a missing subprocess object. No PeTTaChainer `compileadd`, GoalChainer live path, OmegaClaw integration, memory append, or inferred-belief promotion was invoked. Verification passes 127 stdlib unit tests plus `git diff --check`.
- Current progress slice adds local commit `a653dea` with a bounded read-only patham9/PLN query smoke gate in `repos/petta-memory`: `patham9_pln_query_smoke_program(...)`, `run_patham9_pln_query_smoke(...)`, and CLI `patham9-pln-smoke` load one generated handoff Sentence into the local patham9/PLN chainer, parse semantic `Passed:` markers, and preserve original PMEvidence/EvidencePacket provenance in the JSON result sidecar. Runtime artifact `projects/petta-memory/artifacts/patham9_pln_handoff_query_smoke_2026-07-05T1000Z.json` sha256 `b37fe179482b5d758b2a7c2b8d6b6da1a2271e226cb04b528c051ab2a44352bd` passed for `(Acceptable publish_redacted_summary)` with result `((stv 0.91 0.74) (0))`. Decision: use numeric runtime stamps for patham9/PLN compatibility while preserving richer pi-PLN provenance metadata sidecar until EC projection formulas are reviewed. No PeTTaChainer `compileadd`, GoalChainer live path, OmegaClaw integration, memory append, or inferred-belief promotion was invoked. Verification passes 126 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `ad7fffa` adds a bounded non-live PeTTaChainer four-field right-payload arity/head materialize gate in `repos/petta-memory`: `materialize_four_field_right_payload_arity_rungs(...)` and `run_materialize_four_field_right_payload_arity_gate(...)` keep the all-sentinel two-argument nested Type in the second payload slot with generic left `PayloadA`, then grow the right sibling from atom/simple nested `RightPayload` through two-argument `RightPayload` before testing STV arities. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_four_field_right_payload_arity_gate_2026-07-05T0200Z.json` sha256 `5c0c35948008aba32eaf95754ca8a92b4b10761de6518a3ca4515317dbc19728` shows atom right payload, zero-arg `RightPayload`, and one-arg `RightPayload` materialize in ~0.43-0.46s, but two-argument `(RightPayload 1.0 1.0)` times out at 4s before STV-specific rungs. This narrows the blocker from STV-head-specific behavior to a generic right nested-payload arity-two sibling adjacent to a two-argument nested Type in a four-field wrapper. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 114 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `82c2cd9` adds a bounded non-live PeTTaChainer four-field neighbor-shape materialize gate in `repos/petta-memory`: `materialize_four_field_neighbor_shape_rungs(...)` and `run_materialize_four_field_neighbor_shape_gate(...)` keep the all-sentinel two-argument nested Type in the second payload slot while adding the left proof id and right truth-value/STV-like payload stepwise. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_four_field_neighbor_shape_gate_2026-07-05T0000Z.json` sha256 `b4aa2b5f3ebe512d258a49352b2cc0a493868c6dd606ba5cc10477c2b88fa9e0` shows generic payload siblings and proof-id + payload pass in ~0.47-0.49s, but `PayloadA + nested Type + (STV 1.0 1.0)` times out at 4s. This narrows the blocker from proof-id-specific neighbor shape to the combination of a two-argument nested Type with an adjacent STV-shaped right sibling in a four-field wrapper. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 112 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `2900386` adds a bounded non-live PeTTaChainer four-field nested-position materialize gate in `repos/petta-memory`: `materialize_four_field_nested_position_rungs(...)` and `run_materialize_four_field_nested_position_gate(...)` move the same all-sentinel two-argument nested Type through each slot of a synthetic four-field `ProofEnvelope` before returning to the proof-like payload/STV slot layout. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_four_field_nested_position_gate_2026-07-04T2200Z.json` sha256 `00dda1cfd8319db4edb5fc665a4d9b40af97493a032c1869cabc24d6a9bb8ac7` shows nested Type in slot 1, slot 2, and slot 3 with simple payload siblings all materialize as identity in ~0.48-0.49s, while the proof-like `(ProofEnvelope b-profile-000 (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))` still times out at 4s. This narrows the blocker from any four-field nested expression to the specific proof-like neighbor shape: proof id + two-argument nested Type + STV. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 110 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `53eb8e8` adds a bounded non-live PeTTaChainer generic four-field context arity gate in `repos/petta-memory`: `materialize_generic_four_field_context_arity_rungs(...)` and `run_materialize_generic_four_field_context_arity_gate(...)` keep the synthetic `ProofEnvelope` four-field wrapper fixed while increasing nested Type arity before mixed/original token controls. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_generic_four_field_context_arity_gate_2026-07-04T2000Z.json` sha256 `5877d1966b10c99d6eccd66a27e41e49f56b41aab365200b77486919ea6d9e9` shows `(ProofEnvelope proof (Requires) tv)` and `(ProofEnvelope proof (Requires TypeArgSentinel0) tv)` materialize in ~0.45-0.48s, but `(ProofEnvelope proof (Requires TypeArgSentinel0 TypeArgSentinel1) tv)` times out at 4s. This confirms the current materializer blocker is generic four-field list context plus two-argument nested subexpression arity, not PeTTaChainer `:` proof syntax or original argument tokens. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 108 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `e67d99c` adds a bounded non-live PeTTaChainer nested-Type context matrix gate in `repos/petta-memory`: `materialize_nested_type_context_matrix_rungs(...)` and `run_materialize_nested_type_context_matrix_gate(...)` keep an all-sentinel two-argument nested Type fixed and move it through adjacent contexts before returning to the `(: proof type tv)` shape. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_nested_type_context_matrix_gate_2026-07-04T1800Z.json` sha256 `1926d9f5af5ca5f1343844005ea5fd978edc3b081c19a2dfdefbcfa96af21acd` shows the nested Type alone, the two-field `(: proof type)` prefix, and a three-field `(ProofEnvelope proof type)` control materialize, but the generic four-field `(ProofEnvelope proof type (STV 1.0 1.0))` times out at 4s. This narrows the materializer blocker to generic four-field list context plus a two-argument nested subexpression, not the PeTTaChainer `:` head specifically. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 106 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `d28ab4e` adds a bounded non-live PeTTaChainer nested-Type arity/token matrix gate in `repos/petta-memory`: `materialize_nested_type_arity_matrix_rungs(...)` and `run_materialize_nested_type_arity_matrix_gate(...)` reorder the prior nested-Type diagnostics so all-sentinel arity rungs run before original argument-token combinations. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_nested_type_arity_matrix_gate_2026-07-04T1600Z.json` sha256 `d24401f89cef49eddb83eb6c03ae2990cb626883c7f2f45b01647238e980fa35` shows `(: b-profile-000 (Requires) (STV 1.0 1.0))` and `(: b-profile-000 (Requires TypeArgSentinel0) (STV 1.0 1.0))` materialize in ~0.47-0.49s, but the all-sentinel two-argument nested Type `(: b-profile-000 (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))` times out at 4s. This narrows the materializer blocker from the original `MemoryTarget0`/`PLNReadyViews` tokens to generic two-argument nested Type arity inside a full proof atom. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 104 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `bc32501` adds a bounded non-live PeTTaChainer nested-Type materialization ladder in `repos/petta-memory`: `materialize_nested_type_proof_rungs(...)` and `run_materialize_nested_type_ladder_gate(...)` keep full proof shape plus sentinel STV fixed while rebuilding `(Requires MemoryTarget0 PLNReadyViews)` under the proof Type field. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_nested_type_ladder_gate_2026-07-04T1400Z.json` sha256 `bc5aab720dde2427afb1fbf2ad66dba53c2abcb32022e06b1d0ee4a1f8e8c5f2` shows `(: b-profile-000 Requires (STV 1.0 1.0))`, `(: b-profile-000 (Requires) ...)`, and `(: b-profile-000 (Requires MemoryTarget0) ...)` materialize in ~0.49s, but `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))` times out at 4s. This narrows the materializer blocker to a full proof atom whose nested Type expression has at least two arguments, not the `Requires` head or first argument alone. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 101 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `e655c79` refines the bounded non-live PeTTaChainer `materialize-stmt-lambdas` proof-shape ladder with sentinel full-arity rungs in `repos/petta-memory`: after the already-passing type/STV subforms and proof prefixes, the gate now tests `(: proof ProofShapeSentinel (STV 1.0 1.0))`, then original type with sentinel STV, then sentinel type with original STV, before the exact full proof. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_proof_shape_sentinel_ladder_gate_2026-07-04T1200Z.json` sha256 `989cfce15fe4d7703f03e5f67cb0ecde858b191869d1ce062fe66798eefdd78c` shows the sentinel full-arity atom passes in ~0.44s, but the original `(Requires MemoryTarget0 PLNReadyViews)` type inside a full `(: proof type tv)` atom still times out at 4s even with `(STV 1.0 1.0)`. This narrows the materializer blocker to interaction between the full proof shape and the nested statement-type expression rather than top-level arity or STV alone. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write path was invoked. Verification passes 98 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `8fe569e` adds a bounded non-live PeTTaChainer `materialize-stmt-lambdas` proof-shape ladder gate in `repos/petta-memory`: `materialize_identity_proof_shape_rungs(...)` and `run_materialize_proof_shape_ladder_gate(...)` test the independent type/STV subforms, synthetic proof prefixes, and then the full proof statement without invoking `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal writes. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_proof_shape_ladder_gate_2026-07-04T1000Z.json` sha256 `43669be7cd99dd9fc618ed07297518dd53d1a22527d8fa5d8fb6c9f78553ef24` shows rungs 0-3 pass in ~0.47s each, but the complete four-field proof atom still times out at 4s. Verification passes 98 stdlib unit tests plus `git diff --check`.
- Current progress slice adds a bounded non-live `materialize-stmt-lambdas` identity ladder gate in `repos/petta-memory`: `run_materialize_identity_ladder_gate(...)` source-checks multiple lambda-free rungs, compares runtime output structurally while allowing PeTTa float rendering changes (`0.70` -> `0.7`), and stops at the first blocked rung. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_identity_ladder_gate_2026-07-04T0800Z.json` sha256 `2d3d76eed14378a1597bffd557df2429fe30d688542208b0c4ce6d332a7a3f01` shows `(Requires MemoryTarget0 PLNReadyViews)` and `(STV 0.70 0.55)` materialize successfully in ~0.46s each, but the full tiny proof statement still times out at 6s. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or memory write path was invoked. Verification passes 95 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `18e364a` adds a bounded non-live PeTTaChainer `materialize-stmt-lambdas` identity runtime gate in `repos/petta-memory`: `run_materialize_identity_gate(...)` source-checks that a statement is lambda-free, then runs only `!(materialize-stmt-lambdas <statement>)` in an isolated subprocess and compares output against the original statement. Runtime artifact `projects/petta-memory/artifacts/pettachainer_materialize_identity_runtime_gate_2026-07-04T0600Z.json` sha256 `df9a7339afad400e3262bf7e9eb289cc9b09fb41299024dc79a36f0de6cd5687` remains blocked: the tiny promoted-belief proof timed out at 6s. No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or memory write path was invoked. Verification passes 91 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `662845c` adds source-level `materialize-stmt-lambdas` identity inspection in `repos/petta-memory`: `inspect_materialize_stmt_lambdas_for_statement(...)` reads checked-out PeTTaChainer source and statically checks the tiny promoted-belief STV statement. Artifact `projects/petta-memory/artifacts/pettachainer_materialize_identity_source_inspection_2026-07-04T0400Z.json` sha256 `6a5c58ebe7a403dbf2838c0faa430cf80d5554650873aab50915c9e9f02ee682` confirms the statement has 0 `|->` lambda forms, 3 expression nodes / 8 atom nodes, and source-level materialization should be an identity walk; prior materialize timeouts are therefore more likely evaluator/recursive traversal overhead than user lambda execution. Verification passes 89 stdlib unit tests plus `git diff --check`.
- Current progress slice hardens the non-live PeTTa `static-import!` runtime microbenchmark in `repos/petta-memory`: the isolated loader stage now checks each expected generated Prolog fact directly against the consulted runtime predicate, not only against `scratch.pl` text/counts. Runtime artifact `projects/petta-memory/artifacts/petta_static_import_runtime_fact_check_microbenchmark_2026-07-04T0200Z.json` sha256 `e893ea1c2edacebf57c4aa4aaa677645890bed6eaddc3eacbd6bfc65543049e8` loaded 2 normalized scratch atoms into `pmbench_rtcheck/3`; generated facts matched and both exact runtime fact goals were queryable (`runtime_expected_facts_present: true`). Verification passes 88 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `1e81e10` parameterizes and hardens the non-live PeTTa `static-import!` microbenchmark space handling in `repos/petta-memory`: `run_static_import_microbenchmark(..., space=...)` now validates Prolog-safe predicate names, passes the selected space into the isolated runtime stage, computes expected facts for that space, and queries/counts the selected predicate instead of hard-coding `gckb/3`. A named-space runtime check loaded the same 2 normalized scratch atoms into `pmbench/3`; 2 expected facts matched (`facts_match: true`) with count 2. Artifact `projects/petta-memory/artifacts/petta_static_import_named_space_microbenchmark_2026-07-04T0000Z.json` sha256 `83e77667009e1a0250c814907c84699c073c2d1cb6fe614d73e80e75b1686e58`. Verification passes 87 stdlib unit tests plus `git diff --check`.
- Current progress slice local commits `294c8e4` + `5ce4ec0` add a non-live runtime static-import microbenchmark gate in `repos/petta-memory`: `run_static_import_microbenchmark(...)` consumes the previously designed normalized atoms, writes them to a temporary `scratch.metta` file, calls PeTTa's `static-import!` loader directly via janus_swi in a bounded subprocess, then verifies that the generated `.pl` fact lines match expected converted Prolog facts and the loaded `gckb/3` space predicate has the right fact count. The microbenchmark succeeds: 2 normalized atoms loaded, 2 expected facts matched (`facts_match: true`), completing in ~0.07s. This confirms `static-import!` is a viable bounded loader for Prolog-safe normalized atoms, though it remains a bulk data loader and not a PeTTaChainer `compileadd`/indexing API. Artifact `projects/petta-memory/artifacts/petta_static_import_microbenchmark_2026-07-03T2200Z.json` sha256 `f3c9aee668d31cd01595eb07071509ad51d54371b4cc2f0cd2c9b61e99d3a21a`. Verification passes 86 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `6513e27` adds a source-only static-import microbenchmark atom design in `repos/petta-memory`: `design_static_import_microbenchmark_atoms(...)` converts current STV/EvidencePacket examples into lowercase/underscore, three-argument top-level scratch atoms matching PeTTa `static-import!` converter constraints, while preserving original-to-normalized mapping metadata. It does not run SWI/qcompile/consult, does not append to journals, and does not claim PeTTaChainer `compileadd`/query success. Artifact `projects/petta-memory/artifacts/petta_static_import_microbenchmark_atom_design_2026-07-03T2000Z.json` sha256 `354c8b77447902098fd14848ec53fe7a15012d3252ea7e5de60d1703ea4762d8`. Verification passes 84 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `172b4c9` adds source-level PeTTa `static-import!` inspection in `repos/petta-memory`: `inspect_petta_static_import_source(...)` reads checked-out `repos/PeTTa/lib/lib_import.pl`, models its `.metta` line -> Prolog fact conversion for current petta-memory PeTTaChainer STV/EvidencePacket exports, and records that direct use is unsafe today because the loader is line-oriented/no-code/no-bangs, does not quote tokens, and current exports include uppercase symbols plus hyphenated ids that are unsafe as unquoted Prolog terms. Artifact `projects/petta-memory/artifacts/petta_static_import_source_inspection_2026-07-03T1800Z.json` sha256 `3c3e3829e284a7c837a0ad4be0850c685695c0e49199259d65713ad0d6b2866a`. Verification passes 83 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `1091b31` adds source-level PeTTaChainer `compile_` branch mapping for the tiny promoted-belief STV statement: `inspect_compile_dispatch_for_statement(...)` parses `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 0.70 0.55))` and checked-out upstream `compile.metta`/`logic_config.metta` without invoking SWI/PeTTaChainer runtime. It confirms the exported petta-memory proof shape should enter the `compile_` fact-assertion branch (`compile-fact-kb` + `compile-outputs`), not implication or bidirectional-rule branches, after `materialize-stmt-lambdas`/`mm2compile`. Artifact `projects/petta-memory/artifacts/pettachainer_compile_dispatch_fact_branch_2026-07-03T1600Z.json` sha256 `a0e512ae36bf875cb3938de1a5e9370716241ad4839c8548012ded4dc159a0e5`. Verification passes 82 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `2cd1b4c` adds source-level PeTTaChainer `compileadd` bottleneck mapping in `repos/petta-memory`: `inspect_compileadd_bottleneck_sources(...)` records exact checked-out upstream MeTTa definitions/imports for `compileadd`, `materialize-stmt-lambdas`, `mm2compile`, `compile_`, `index-source-implication`, and `maybe-process-on-add` without invoking SWI/PeTTaChainer runtime. Artifact `projects/petta-memory/artifacts/pettachainer_compileadd_source_bottleneck_2026-07-03T1400Z.json` sha256 `98a1812c5b678d3309d58f7c8b106500f2654e927e3f50b6a61c24323ceee561`. Verification passes 80 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `f6d7dbf` adds source-level PeTTaChainer add API inspection in `repos/petta-memory`: `inspect_pettachainer_add_api(...)` reads the checked-out `repos/PeTTaChainer` Python/MeTTa sources without invoking SWI/PeTTaChainer runtime and records that public add methods still route through `compileadd`/`compileadd-mine`; no public precompiled-add/cache API terms were found. Artifact `projects/petta-memory/artifacts/pettachainer_add_api_inspection_2026-07-03T1200Z.json` sha256 `b94c89a3af8ce2817e2b5b763d00b676c7e060ffa34c62417ea0e9d1a130d097`. Verification passes 79 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `0270fda` adds a second non-live GoalChainer EC policy fixture in `repos/petta-memory`: `fixtures/goalchainer_conflicting_ec_smoke.metta` exercises promoted `Acceptable publish_redacted_summary` STV evidence with opposing contextual `EvidencePacket (EC 1 9)` counts. The precompiled smoke still ranks `publish_redacted_summary` recommended, but lowers evidence strength from `0.94` to `0.511429` with `confidence=0.833333`, preserving provenance and `compileadd_not_invoked`/no-write/no-task checks. Artifact `projects/petta-memory/artifacts/goalchainer_precompiled_conflicting_ec_smoke_2026-07-03T1000Z.json` sha256 `5dfa832b854c7c4a427686f0419530ec76891c953ed9ac22f1f1e7212c9548bc`. Verification passes 78 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `ec84403` adds EC-aware appraisal to the precompiled non-live GoalChainer smoke gate in `repos/petta-memory`: matching `contextual-appraisal-evidence` `EvidencePacket (EC support opposition)` items for promoted `Acceptable` actions are folded into the STV action evidence as bounded derived strength/confidence, while preserving provenance and still avoiding GoalChainer CLI, PeTTaChainer `compileadd`/query, directives, OmegaClaw skills, and memory writes. Artifact `projects/petta-memory/artifacts/goalchainer_precompiled_ec_smoke_2026-07-03T0800Z.json` sha256 `ec34815dc6f2bbace492a9f6d92484df61775831e957cd0cacf0ce45a4ae654f`. Verification passes 77 stdlib unit tests plus `git diff --check`.
- Current progress slice adds a precompiled non-live GoalChainer smoke bypass in `repos/petta-memory`: `run_goalchainer_precompiled_handoff_smoke(...)` consumes promoted `Acceptable` STV items from `goalchainer-handoff-cache` via GoalChainer scenario/scoring/explanation modules only, avoiding GoalChainer CLI, PeTTaChainer `compileadd`/query, directives, execution, OmegaClaw skills, and memory writes. CLI `goalchainer-smoke` now uses this bypass by default; `--external-cli` retains the earlier blocked path. Artifact `projects/petta-memory/artifacts/goalchainer_precompiled_smoke_2026-07-03T0600Z.json` sha256 `9bad7a5bb956b6c1128f8e6dbb64c304bd430f3cc25830114f9ffe7b6fd39d0c`. Verification passes 77 stdlib unit tests plus `git diff --check`.
- Design source: `projects/hyperseed-formalizations/repos/hyperseed-formalizations/papers/0003-medium-petta-memory-plan/medium_petta_memory_plan.tex`, latest pushed branch `agent/protomegatron-formalization-0002`, commit `bfab423`.
- This project notebook was created on 2026-06-27 after Benjamin asked to start the memory upgrade as a software project.
- Public GitHub repo `https://github.com/bgoertzel-sing/petta-memory` was created and local `main` pushed on 2026-06-27.
- Local repository scaffold exists at `projects/petta-memory/repos/petta-memory` with commits:
  - `65a2e4e` Seed PeTTa memory prototype.
  - `82d8671` Add memory store CLI.
  - `3d60071` Apply design review hardening.
  - `51eb629` Harden PLN view and append safety.
  - `fa10642` Harden MemoryCluster atom parsing.
- Implemented standalone Python package with `.metta` cluster journal, CLI, examples, an e2e fixture, and stdlib `unittest` tests.
- GPT5.5-Pro design review advice was incorporated in commits `3d60071` and `51eb629`: explicit record delimiters, per-cluster schema version, cluster-aware query, append-only status supersession, explicit PLN promotion, file locking, duplicate ID rejection, safer PLN quote filtering, and stronger negative/epistemic tests.
- Branch `agent/parser-validation` commit `fa10642` replaces shallow line checks with a recursive S-expression parser for multiline nested atoms/comments, and the current working tree adds an optional caller-supplied parse-check seam for future PeTTa/MeTTa runtime validation.
- Local branch `agent/omegaclaw-wrapper-sketch` commit `1e2a109` adds a non-live OmegaClaw read-only MeTTa prompt-view wrapper sketch plus feature-flag/read-write-boundary notes; autonomous writes remain rejected and no OmegaClaw/external integration was changed.
- The same branch commit `22d5aa4` adds prompt-view relevance ordering by optional topic/status preferences plus salience/recency ordering; stdlib unittest passes 20 tests.
- Current local working tree on branch `agent/parser-validation` adds stricter PLN promotion metadata (`PromotionRule`, bounded `PromotionTrust`, `PromotionDomain`), optional normalized PLN mapping atoms via `pln-view --normalized`, and a generated bounded `MM-index`/CLI `index-view` for id/type/about/status/role retrieval edges. Empirical fixtures now check `MM-index` parity with direct id/type/about/status/role queries, prompted `MM-index-id` mention edges for valid identifier arguments, and prompt-view topic/status relevance under a tight character budget. Verification passes 32 stdlib unit tests plus `git diff --check`.
- The working tree now also documents proposed OmegaClaw Core migration/API names in `docs/omegaclaw_migration.md` and rejects negative prompt-view bounds at API/CLI level. Verification passes 34 stdlib unit tests plus `git diff --check`.
- Current progress slice tightens bounded retrieval/view output so prompt-view and generated `MM-index` snippets omit an over-budget atom instead of truncating mid-atom, preserving parseable complete atom lines. Verification passes 36 stdlib unit tests plus `git diff --check`.
- Latest progress slice adds an OmegaClaw-style non-live prompt/index fixture (`fixtures/omegaclaw_prompt_context.metta`) and regression coverage that runs `OmegaClawMemoryBridge.prompt_view_metta()` plus `MediumMemoryStore.index_view()` together under a bounded read-only policy. Verification passes 45 stdlib unit tests plus `git diff --check`. Previous slice hardened the non-live OmegaClaw prompt-view wrapper: `OmegaClawMemoryPolicy.view_id` must be a valid symbol id, and `PromptViewGeneratedAt` is emitted through the shared S-expression string escaper so caller-supplied timestamps cannot corrupt the read-only MeTTa envelope.
- Current progress slice adds local commit `a2dc693` with a bounded non-live GoalChainer smoke wrapper/CLI and fixture in `repos/petta-memory`: `run_goalchainer_handoff_smoke(...)` invokes only `goal_chainer.cli demo --json` under timeout, wraps selected handoff evidence provenance, and rejects directive/task-claim/execution payloads. The first external GoalChainer run with local PeTTa/SWI/PeTTaChainer still fails before producing a decision payload due to the known PeTTaChainer `compileadd` SWI `stack_limit=8g` blocker; archived failure artifact `projects/petta-memory/artifacts/goalchainer_smoke_failure_2026-07-03T0400Z.json` sha256 `a35c65c0e771a86551fd481dae1e837d2a1796eb43e424d76a8948087f4945cd`. Verification passed 75 stdlib unit tests plus `git diff --check`. No live OmegaClaw skill/task/memory path was touched.
- Current progress slice local commit `32746a2` adds a non-live GoalChainer handoff contract in `repos/petta-memory`: `MediumMemoryStore.goalchainer_handoff_cache(...)` and CLI `goalchainer-handoff-cache` repackage promoted PeTTaChainer handoff items as GoalChainer appraisal/acceptability evidence inputs, preserving belief/cluster/promotion provenance and explicitly disabling live OmegaClaw skills, task claims, memory writes, and inferred-belief status. `docs/goalchainer_handoff.md` records the non-live gate contract and next smoke proposal. Verification passes 72 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `10f2579` adds a non-live PeTTaChainer handoff cache in `repos/petta-memory`: `MediumMemoryStore.pettachainer_handoff_cache(...)` and CLI `pettachainer-handoff-cache` emit JSON containing promotion-eligible STV statements and EvidencePackets, labeled as `pln-ready-input-not-inferred-belief`, with optional runtime statement checking and `compileadd`/query still gated. Artifact `projects/petta-memory/artifacts/pettachainer_handoff_cache_2026-07-03T0000Z.json` (sha256 `fa6bccab591590c799685ff85c336b49329771183bc72433765ed37e1b0b97a2`) was generated from a size-2 profile workload using `PeTTaChainer.check_stmt == 1.0` for STV statements; EvidencePackets carry explicit non-negative EC counts. Verification passes 71 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `1fc6f04` decides the next bounded PeTTaChainer add path after direct-vs-eval probe timeouts: `summarize_compileadd_strategy(...)` now turns profile artifacts into a reproducible strategy summary. Artifact `projects/petta-memory/artifacts/pettachainer_compileadd_strategy_2026-07-02T2200Z.json` (sha256 `6261705d465c8ee94faea5f2d5d74f080e6440257482ddcb5f4d4f5e5013311d`) recommends a non-live `precompiled_statement_cache_gate`: cache checked promoted STV statements/EvidencePackets as handoff inputs, not inferred beliefs, while full PeTTaChainer `compileadd`/query remains gated pending upstream materialize/mm2compile instrumentation or a precompiled add API. Verification passes 69 stdlib unit tests plus `git diff --check`.
- Previous progress slice refined internal PeTTaChainer `compileadd` probes to compare direct subform invocation against the earlier eval-wrapped probe controls. Artifact `projects/petta-memory/artifacts/pettachainer_profile_compileadd_direct_probe_2026-07-02T2000Z.json` (sha256 `e7a92e21d635e72df346e0684371e847b7f613602f1fe09bd15cf176ff520307`) shows constructor/check_stmt succeeded; direct and eval-control `materialize-stmt-lambdas`/`mm2compile` both timed out at 5s, while `index-source-implication` and `maybe-process-on-add` completed quickly after initialization. Decision point is now sharper: the timeout is not merely the previous eval wrapper, so the next slice should choose a minimal/precompiled add path or add deeper upstream instrumentation around materialization. Verification passes 68 stdlib unit tests plus `git diff --check`.
- Previous progress slice adds PeTTaChainer constructor-only profiling before add-only/add+query runtime stages. Artifact `projects/petta-memory/artifacts/pettachainer_profile_init_2026-07-02T1601Z.json` (sha256 `fb9cc8c6ce7ee67015fa52e4074c6749095b3cca1a7f89e93b84c7d9838969bf`) shows constructor initialization succeeds in ~0.48s while proof add-only, proof add+query, contextual packet add-only, and contextual add+query still time out at 6s. Decision: the bottleneck is inside `compileadd`/add instrumentation, not PeTTaChainer construction or query/context projection. Verification passes 67 stdlib unit tests plus `git diff --check`.
- Current progress slice local commit `f43be64` extends the PeTTaChainer profiling harness with add-only bottleneck stages before combined add+query work: opt-in runtime profiling now records `proof_runtime_add_only` and `contextual_packet_add_only` in isolated subprocesses. Artifact `projects/petta-memory/artifacts/pettachainer_profile_contextual_2026-07-02T1400Z.json` (sha256 `6054d50ec9fff76c6107a6adfa9a495a9ef735189d09e154c07dc8a08b893b79`) shows size 1 `check_stmt` succeeds while proof add-only, proof add+query, contextual packet add-only, and contextual add+query all time out at 6s. Decision: the next bottleneck is PeTTaChainer compile/add or instrumentation, not query/contextual search yet. Verification passes 67 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `7a764d0` extends the PeTTaChainer profiling harness with subprocess-isolated runtime stages: optional `compileadd`/query/contextual work now uses `--stage-timeout-sec`, captures OS-level stdout/stderr byte counts, and records bounded timeout events instead of hanging the worker. Smoke artifact `projects/petta-memory/artifacts/pettachainer_profile_isolated_2026-07-02T1200Z.json` (sha256 `b51bbe7cc7c38908be36036b5e86b01de8202673d741e5344c07b3b63c9a9f73`) shows size 1 `check_stmt` succeeds while proof `compileadd`+query times out cleanly at 3s. Verification passes 66 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `9cb3002` adds a narrow PeTTaChainer profiling harness: `python -m petta_memory.pettachainer_profile` generates OmegaClaw-like promoted-belief clusters with explicit STV and EC counts, exports proof statements and EvidencePackets, and times store/export plus `check_stmt` validation. Artifact `projects/petta-memory/artifacts/pettachainer_profile_2026-07-02T1000Z.json` (sha256 `0dcb4a131439b1ef550275ef22bdfed289c6f574d13e9569b0e9892fcb10dacb`) records sizes 1/3/5; an attempted opt-in `compileadd`/contextual run exceeded the worker timeout/noise budget, so the next task is stage-isolated runtime profiling. Verification passes 64 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `0fda6d3` adds explicit PeTTaChainer EC/EvidencePacket support: `EvidenceSupportCount` and `EvidenceOppositionCount` are validated as non-negative numeric binary schema atoms, and `MediumMemoryStore.pettachainer_evidence_packet_view()` plus CLI `pettachainer-packets-view` emit PeTTaChainer-style `(EvidencePacket statement (EC pos neg) ((domain ...) (promotion-rule ...)) promotion-event)` atoms only for promoted beliefs with explicit counts. Verification passes 61 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `66aebbb` wires the optional parse-check seam to the local PeTTa runtime and drafts the live OmegaClaw integration review gate. `petta_memory.make_petta_parse_checker(...)` can be explicitly passed to `MediumMemoryStore(parse_checker=...)` so canonicalized clusters are checked with `PeTTa.process_metta_string` before append; runtime rejection is converted to `ValidationError` and leaves the journal unchanged. `docs/omegaclaw_migration.md` now lists the required live-adapter boundary review before any OmegaClaw wiring or write path. Verification passes 59 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `0460d3d` adds PeTTaChainer-specific normalized evidence export and the first project-specific PLN runtime smoke in `repos/petta-memory`: promoted `DerivedBelief`s can now be exported via `MediumMemoryStore.pettachainer_evidence_view()` or CLI `pettachainer-view` as `(: proof-id statement (STV strength confidence))`, with strength preserved and confidence capped by `PromotionTrust`; EC/EvidencePacket export is deferred until explicit support/opposition counts exist. `tests/test_pettachainer_smoke.py` configures the local SWI-Prolog 9.3.36 + Janus + PeTTaChainer checkout and validates the exported statement with `pettachainer.check_stmt(...) -> 1.0`. Verification passes 56 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `78478b3` tightens `Contains` read/write-boundary validation in `repos/petta-memory`: a cluster can no longer list its own `MemoryCluster` id as a contained record, preventing self-containment cycles from entering prompt/index/audit views. Verification passes 53 stdlib unit tests plus `git diff --check`.
- PLN runtime candidate checkout: `projects/petta-memory/repos/PeTTaChainer` tracks `https://github.com/MesTTo/PeTTaChainer` at `master` commit `e4db5cad60a3` (`Implement πPLN: paraconsistent contextual reasoning over PeTTaChainer`); dependency checkout `projects/petta-memory/repos/PeTTa` tracks `https://github.com/patham9/PeTTa` at `main` commit `d8d46920269c`. PeTTaChainer exposes a Python package plus bundled MeTTa runtime for πPLN/context-indexed evidence, `EC pos neg`, generated local contexts, and contextual queries. Local runtime setup now reuses `projects/omegaclaw/local/swipl-9.3.36` with Janus support, plus `repos/PeTTaChainer/.venv` with `janus-swi`, sibling `PeTTa`, and editable `PeTTaChainer`; `local/pettachainer-env.sh` activates the environment. Verification passed for `swipl --version`, `library(janus)`, `PeTTa.process_metta_string('!(+ 1 2)') -> ['3']`, and `pettachainer.check_stmt(...) -> 1.0`. Broad upstream test discovery is not yet a useful gate because it emits large PeTTa compilation traces and includes long/benchmark-like tests; project-specific smoke coverage is now present in `repos/petta-memory/tests/test_pettachainer_smoke.py`. As of 2026-07-04, PeTTaChainer is a semantic reference/comparison target rather than the critical path because its `compileadd`/`materialize-stmt-lambdas` path is blocked on tiny examples.
- Functional PLN chainer candidate checkout: `projects/petta-memory/repos/patham9-pln` tracks `https://github.com/patham9/PLN.git` (`trueagi-io/PLN`) at commit `55f1751d993f71b8a24da03e3aec94ab40789a59`. First local smoke used the existing PeTTa/SWI setup with `projects/petta-memory/repos/PeTTa` commit `d8d46920269ced70cd6236a5182d4d2409c1e12b`; `FlyingRaven` and `Smokes` pass when run from the PLN checkout after `sh build.sh`, while several examples/rule tests emit `Passed: false` despite shell status 0. Run record: `artifacts/patham9-pln-smoke-20260704/RUN.md`. This is now the leading functional base for a pi-PLN evidence/context extension track.
- Reference checkout: `projects/petta-memory/repos/trueagi-chaining` tracks `https://github.com/trueagi-io/chaining` at detached commit `bc9beb2672953e07971b3abecc1fe67651ecddc4` (2026-06-29, Nil Geisweiller). Pure-MeTTa PLN chaining experiments: PLN rule prototypes under four representation strategies (match/entail/equal/dependent-types), PLN-based inference controller (`pln-inf-ctl.metta`), backward-chaining continuation control experiments, probabilistic backward chaining. Reference material for the inference-control phase (roadmap item 4); no runtime integration yet.
- Previous progress slice pushed local commit `f9647bd` tightening delimited journal read validation: `clusters()` now rejects records whose `;;; BEGIN/END MemoryCluster <id>` envelope disagrees with the internal `(MemoryCluster <id>)` atom, preventing audit/query views from silently normalizing manually corrupted records. Verification passes 53 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `51045c3` tightens schema/retrieval relation arity validation: known binary predicates such as `SchemaVersion`, `About`, `StatusValue`, `PromotionTrust`, and `EvidenceFor` must have exactly subject/object arguments, preventing hidden extra fields that query/index/prompt/PLN code would otherwise ignore. Verification passes 52 stdlib unit tests plus `git diff --check`.
- Previous progress slice local commit `ba08f54` adds an explicit bounded `audit_view` API/CLI and tightens ID-declaration arity validation: audit output preserves complete canonical `MemoryCluster` records with delimiters, negative audit bounds are rejected, and unary ID-declaring predicates reject extra arguments before query/index code can collapse them to the first id. Verification passes 51 stdlib unit tests plus `git diff --check`.
- Earlier progress slice local commit `423a372` adds a separately feature-flagged OmegaClaw generated-index wrapper: `index_view_reads_enabled` defaults off, `OmegaClawMemoryBridge.index_view_metta()` emits a bounded read-only-derived `MM-index` envelope, and index wrapper ids/timestamps/bounds are validated or escaped. README and migration docs now distinguish prompt-context reads from generated-index retrieval diagnostics. Verification passes 47 stdlib unit tests plus `git diff --check`.

- 2026-07-09 cross-project replay gate replaced the OmegaClaw sidecar's Python-constructed synthetic evidence with a real bounded `MediumMemoryStore.goalchainer_handoff_cache()` export. Gate `projects/omegaclaw/artifacts/ggb-capacity-gates/20260709-goalchainer-real-petta-memory-replay/` loads a 1,273-byte copy of the previously archived promoted-belief journal, selects its two provenance-carrying STV/EC items under a four-item cap, and feeds one archived Protomegabot decision candidate to GoalChainer's deterministic heuristic-memory path. Harness passed 9/9; focused petta-memory tests passed 53, focused GoalChainer tests passed 52, and full petta-memory discovery passed 430. The journal SHA-256 remained unchanged; no live bridge or memory write/promotion occurred.

## Related projects

- `omegaclaw`: intended integration target for ProtomegaTron/OmegaClaw memory.
- `hyperseed-formalizations`: contains the design/formalization documents.
- `petta-chem`: separate PeTTa research project; may reuse PeTTa runtime conventions but should not be conflated with this memory subsystem.

## Risks

- **False formality:** symbolic claims may look more authoritative than raw text. Mitigation: explicit epistemic roles, truth values, and provenance.
- **PLN contamination:** raw quotes should not be premises. Mitigation: separate `MM-pln-view` with promotion rules.
- **Prompt bloat:** bounded prompt view only; never inject full log.
- **Schema sprawl:** keep v0 predicates minimal and testable.
- **Premature integration:** keep feature off in OmegaClaw until local tests pass.

## Open questions

- Should the package name be `petta_memory`, `medium_memory`, or `protomegatron_memory`?
- Which PLN implementation/runtime should be used for the first inference smoke test?

- 2026-07-11T10:01Z status update: `repos/petta-memory` now has an additional read-only live-bridge fail-closed check for GoalChainer payload metadata. `live-goal-bridge` validates optional scenario/runtime/explanation shape before emitting artifacts, with regression tests and full stdlib unittest coverage passing (439 tests). This is a small OmegaClaw/GoalChainer integration-wrapper hardening step; live writes, directives/task claims, inferred-belief promotion, patham9 source changes, and PeTTaChainer `compileadd` remain out of scope.
  - Local implementation commit in `repos/petta-memory`: `ab16409`.

## 2026-07-11 strategic pivot — atlas-indexed reversible πPLN SDS

Ben supplied the normative software design specification *Atlas-Indexed Reversible Evidence-Fibered Geodesic πPLN: A Wrapper-First Implementation on patham9 PLN with Native Geodesic-Control Interoperability* (dated 2026-07-12). Preserved source and extracted text: `library/atlas-indexed-reversible-pipln/`; PDF SHA-256 `1af20c7427b484a978507181c44fb32112257f029aa130c30f1c8a45d0d7f0d3`.

This is now the implementation contract for the patham9/πPLN track. The current wrappers remain compatibility baselines, but persistent packet evidence, semantic contexts/charts, deterministic evidence-basis stamps, projection policies, control, proof identity, replay, and promotion must migrate behind typed components. `ec_projected_stv()` is legacy `adapter-weighted-v1`, not canonical πPLN projection.

Most relevant Research Rules at this pivot: Rule 1 (validate estimators/identity machinery), Rule 2 (implement from the explicit SDS and invariants), Rule 3 (retain patham9 as the existing local kernel), and Rule 7 (capability-negotiated modular seams).

- [x] Added canonical piPLN beta round-trip and prior cycling. The inverse subtracts declared prior pseudo-counts before recovering empirical evidence, rejects materially negative recovered counts, and permits a new prior to be applied without prior-mass leakage. Fractional round-trip and reversible prior-cycle tests pass. Verification: focused 29 tests; full 469 tests; `git diff --check` passed. Provenance: progress worker, 2026-07-12 21:00 PDT / 2026-07-13 04:00 UTC.

- 2026-07-13T19:00 PDT: Phase-2 now has a bounded typed patham9 result validator that rejects malformed/nonfinite/injected output and closes every result stamp to compiled evidence-basis provenance. Focused 41 and full 482 tests passed; local commit `cc6f4d4`; manifest/runtime/trace/replay and all promotion/live paths remain gated.
- [x] Phase-2 kernel subprocess input is now independently bounded by encoded UTF-8 bytes before child launch, closing the gap between the assembler's character ceiling and the runner's actual stdin allocation. Focused 3 and full 491 tests passed; `py_compile` and `git diff --check` passed. No patham9 invocation, promotion/write, trace/rule claim, or live integration.
- [x] The repaired PeTTaChainer conversion/collection rungs now also collapse under the exact single-import candidate: one canonical fact produced one `mm2stmt` output and one copied-collector output, versus the baseline's two and four, even though the overlapping `mm2stmt` source is unchanged. Local implementation commit `28be231`; focused 94 and full 549 tests passed, plus `py_compile` and `git diff --check`. This retires a second source repair for now; full repaired `mm2compile` and then `compileadd` remain gated. No upstream, query/result, write/promotion, or live change.
- [x] Completed isolated PeTTaChainer stages now content-address both OS-level streams, and the repaired exact-fact query fails closed unless stdout/stderr byte counts and lowercase SHA-256 identities are complete. A fresh one-step probe still returned one exact answer and recorded stdout 608,129 bytes (`3eafb227...`) plus stderr 138 bytes (`3207c3f2...`). Local implementation commit `468d55a`; focused 106 and full 561 tests passed, plus `py_compile` and `git diff --check`. Diagnostic semantics, typed episode-result admission, promotion/write, upstream repair adoption, and live integration remain closed.
- [x] The repaired one-rule derivation now closes exact truth-formula provenance. Source gates content-address `TotalMpConclusionFormula` and `TotalMpFormula`, require the absent-complement `(STV 0.2 0.2)` fallback, and recompute every returned STV; the fresh answer matched `[0.7600000000000001, 0.52]`. Focused 111 and full 566 tests passed, plus `py_compile` and `git diff --check`. Immutable compiler rule binding, manifests, promotion/write, upstream adoption, and live integration remain closed.
- [x] PeTTaChainer derived-capture and episode-manifest reload now enforces a 1,000,000-byte ceiling before UTF-8 decode or JSON parsing, so an untrusted artifact cannot cause an unbounded read at this admission boundary. Local implementation commit `1d96182`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream adoption, and live integration remain closed.
- [x] Persisted PeTTaChainer capture/manifest admission now rejects symlinks and non-regular files before bounded read and strict JSON/provenance validation. Focused and full 570 tests passed; promotion/write, upstream adoption, and live integration remain closed.
- [x] PeTTaChainer artifact reload now opens candidate files nonblocking before checking descriptor type, so a caller-supplied FIFO fails closed instead of stalling the worker before the regular-file gate. Local implementation commit `e770f5e`; focused 115 and full 570 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain unchanged.
- [x] PeTTaChainer create-once persistence now preserves the primary publication failure when closing the parent-directory descriptor also fails, attaching the close diagnostic instead of masking the write/fsync cause. Local implementation commit `882f3fe`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.
- [x] PeTTaChainer artifact reload now preserves the primary admission/type failure when closing the still-owned artifact descriptor also fails, attaching the close diagnostic instead of masking why the artifact was rejected. Local implementation commit `0a9f0fd`; focused regression and full 570 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.
- [x] PeTTaChainer derived-capture and episode-manifest admission now compares descriptor identity, size, modification time, and change time before and after the bounded read, rejecting artifacts changed concurrently instead of validating a race-dependent byte stream. Local implementation commit `cbacab9`; focused 116 and full 571 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.
- [x] PeTTaChainer audit-artifact admission now requires the exact bytes delivered by the regular-file descriptor to match its stable `st_size`, closing short-read and volatile pseudo-file ambiguity even when before/after metadata is identical. Local implementation commit `178b759`; focused regression and full 572 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live integration remain closed.
- [x] PeTTaChainer audit-artifact admission now treats mode, owner, or group drift during the bounded descriptor read as a concurrent artifact change. Local implementation commit `6bcc26c`; focused regression and full 577 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer checksummed audit-artifact admission now rejects group- or world-writable files before reading them. This aligns reload with the create-once writer's owner-only publication boundary. Focused regression and full 578 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once audit-artifact publication now rejects a symlink supplied as the destination parent on platforms with `O_NOFOLLOW`, preventing caller-visible path redirection before the already descriptor-anchored exclusive create and durability sync. Local implementation commit `57ba221`; focused 1 and full 579 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once audit publication now rejects a group- or world-writable destination parent before artifact creation. This closes the adjacent multi-principal replacement/removal seam after the prior no-follow parent gate. Local implementation commit `893e837`; focused 1 and full 580 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once audit publication now rechecks the already-open parent directory descriptor after the artifact is file-synced and rejects newly group/world-writable permissions before directory fsync. The completed artifact is retained under the existing uncertain-publication/create-once rule. Local implementation commit `93e8fa0`; focused 2 and full 581 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once artifact publication now requires the already-open parent directory's device, inode, mode, link count, owner, and group identities to remain stable through file sync. Ownership or other metadata drift fails closed before directory fsync while retaining the file-synced create-once artifact. Local implementation commit `b53e7bb`; focused 2 and full 582 tests passed, plus `py_compile` and `git diff --check`. Promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer checksummed artifact admission now anchors the final filename lookup to an already-open, non-symlinked parent directory descriptor and rejects group/world-writable parents before reading. This prevents parent-path substitution or shared-directory mutation from selecting a different audit artifact. Local implementation commit `7eed3f6`; focused 3 and full 584 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer audit-artifact admission now requires the already-open trusted parent directory to retain its device, inode, mode, link count, owner, and group identity across the bounded descriptor read. Permission or ownership drift fails closed. Local implementation commit `39ba877`; focused 131 and full 586 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer checksummed artifact admission now closes the already-open parent descriptor when its initial metadata inspection fails, preserving the metadata error and attaching any secondary close diagnostic. Local implementation commit `c50eb47`; focused 1 and full 589 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer audit-artifact admission now has regression closure for combined trusted-parent metadata drift and parent-descriptor close failure: the drift rejection remains primary and the cleanup diagnostic is attached. Local implementation commit `8a12b6b`; focused 1 and full 592 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer audit-artifact admission now has regression closure for simultaneous leaf- and parent-descriptor cleanup failures after a pre-stream artifact rejection. The actionable permission rejection remains primary and retains both ordered cleanup diagnostics. Local implementation commit `664d592`; focused 1 and full 594 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer audit-artifact admission now has regression closure for simultaneous cleanup failures after an otherwise successful bounded read: the artifact-stream close error remains primary and the parent-descriptor close diagnostic is attached. Local implementation commit `827a0c0`; focused 1 and full 595 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once audit publication now preserves a primary write/flush/fsync failure when closing the descriptor-backed text stream also fails, attaching the close diagnostic instead of masking the actionable cause. A close failure after successful file sync still propagates while the immutable artifact remains create-once. Local implementation commit `ff313b6`; focused 1 and full 596 tests passed, plus `py_compile` and `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] PeTTaChainer create-once audit publication now explicitly closes the raw artifact descriptor when text-stream construction fails, preserves the stream-open error if descriptor close also fails, durably removes the rejected artifact, and attaches the cleanup diagnostic. Local implementation commit `be5c6d7`; focused 1 and full 596 tests passed, plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] The four legacy pi-PLN artifact writers (episode manifest, validated kernel result, evidence snapshot, and compiled episode inputs) now share the descriptor-anchored create-once durable publication boundary already used by PeTTaChainer captures. This removes pathname-reopen cleanup races and adds parent trust/stability, file-and-directory fsync, and failure-provenance behavior without changing schemas. Local implementation commit `fb7a71d`; full 597 tests passed plus `git diff --check`. Runtime, promotion/write, upstream, remote, paid-compute, and live-integration boundaries remain closed.
- [x] The four legacy pi-PLN audit readers now use the hardened bounded, descriptor-anchored JSON admission path rather than direct pathname reads. Public regressions prove episode manifests, validated kernel results, evidence snapshots, and compiled episode inputs reject a symlinked parent. Local commit `bfcc28b`; focused 4 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] The four legacy pi-PLN audit artifact readers now have public-boundary regressions proving that a valid checksummed episode manifest, validated kernel result, evidence snapshot, or compiled episode input is rejected once a hard-link alias exists. This closes the one-path/one-artifact admission contract against mutation through another pathname. Local regression commit `21ff1ce`; focused 4 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] All four legacy pi-PLN audit readers now have public-boundary regressions proving that a group-writable parent blocks admission of an existing episode manifest, validated kernel result, evidence snapshot, or compiled episode input. Local regression commit `57b2e66`; focused 4 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Legacy pi-PLN checksummed audit admission and create-once publication now require both the artifact and its trusted parent directory to be owned by the running user, closing stable cross-user artifact substitution that mode/link/drift checks alone did not reject. Local implementation commit `f726454`; focused 1 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Current-user ownership enforcement now has public-boundary regression coverage across all four legacy pi-PLN persistence routes. Evidence snapshots, compiled episode inputs, episode manifests, and validated kernel results each reject a foreign-owned parent for read/publication and a foreign-owned artifact for read, without creating a redirected artifact. Local regression commit `b45839b`; focused 3 and full 597 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Legacy pi-PLN audit admission now has public-boundary regression closure for late parent-directory identity drift: after the bounded artifact read, a changed parent inode is rejected before the evidence snapshot is admitted. Local regression commit `48d3e49`; focused 1 and full 598 tests passed, plus `git diff --check`. Runtime inference, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Phase-1 clean-room runtime capture/reload gate is complete. Two isolated
  reload cycles preserve current PeTTaChainer capture/manifest identities,
  legacy πPLN compiled/result/manifest identities, the frozen Phase-0 replay
  anchor, and frozen-query semantics. The combined gate rejects stale source
  and output, malformed and wrong-class descriptors, duplicate logical
  anchors, cross-run collisions, compiled/result/program/process-capture
  provenance drift, and confusion with a newly asserted post-reload memory;
  it also inventories the exact allowed filesystem effects. Completion commits
  `94d749c` through `10afdf1`; final regression commits `cf8ed5d` and
  `e7602a9`. Full 600 tests and `git diff --check` passed again on
  2026-07-23 17:00 PDT / 2026-07-24 00:00 UTC. No runtime execution,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] The Phase-1 clean-room reload regression now covers the frozen Phase-0 replay-anchor artifact class alongside legacy compiled inputs, validated results, and episode manifests. Two isolated cycles preserve source/output identity, while a stale source fails checksum admission before reuse. Focused 1 and full 600 tests passed, plus `git diff --check`. No runtime invocation, promotion/write, upstream/remote action, paid compute, or live integration was opened.
- [x] The Phase-1 clean-room reload regression now includes the frozen Phase-0 replay-anchor artifact class. Two isolated reload cycles preserve the anchor's exact source/output identities alongside compiled input, validated result, and episode-manifest identities; stale source content fails closed. Local commit `f84d45d`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime invocation, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] The Phase-1 clean-room reload gate now rejects a stale compiled runtime descriptor even when its outer document checksum is recomputed: changing the capture episode while retaining the frozen stamp/sentence provenance fails typed reconstruction. The same gate explicitly distinguishes the archived Phase-0 query target, captured derived query/result, and separately compiled post-reload assertion. Local regression commit `535b1db`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime invocation, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Phase-1 clean-room manifest reload now optionally closes the manifest against the separately admitted compiled inputs and validated result. Cross-run compiled descriptors and recomputed foreign results are rejected instead of relying only on each artifact's self-checksum. Local commit `0bb6d8b`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Phase-1 clean-room manifest reload now closes the archived manifest's chart and context IDs against the supplied compiled sentence sidecars, in addition to episode, stamp-map, and validated-result identity. A cross-run compiled descriptor with altered chart provenance fails before manifest admission. Local implementation commit `546318b`; focused 1 and full 600 tests passed, plus `git diff --check`. Runtime execution, promotion/write, upstream/remote action, paid compute, and live integration remain closed.
- [x] Phase-2 manifest reload can now close archived return code, stdout, stderr, and exact delivered-program identity against one supplied bounded `KernelProcessCapture`. Drift in either process output or program commitment fails before admission. Local commit `10afdf1`; focused 1 and full 600 tests passed, plus `git diff --check`. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Bounded pi-PLN process captures now reject malformed provenance at construction: argv must be a non-empty tuple of non-empty strings, return status must be an integer rather than a boolean/coercible value, streams must be text, and an optional delivered-program commitment must be a SHA-256 digest. Local implementation commit `09e774d`; focused 1 and full 601 tests passed, plus `git diff --check`. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Phase-2 raw kernel-result admission now requires the caller-supplied result atom to occur exactly once as a complete captured stdout line. Missing, duplicated, and larger-token-embedded matches fail closed before typed result validation. Local implementation commit `f3882ae`; focused 2 and full 601 tests passed, plus `git diff --check`. No runtime execution, promotion/write, upstream/remote action, paid compute, or live integration.
- [x] The admitted one-rule PeTTaChainer result now exposes a distinct immutable
  compiler-bound attribution record. It binds TotalMP plus the exact rule/fact
  sentence digests, proof IDs, stamps, evidence bases, and source result digest,
  while structurally forbidding any claim that opaque runtime diagnostics were
  decoded as a trace. Local implementation commit `e3a0d37`; focused 1 and full
  601 tests passed, plus `git diff --check` (2026-07-24 11:00 PDT / 18:00 UTC).
  General trace decoding, promotion/write, upstream/remote action, paid compute,
  and live integration remain closed.
- [x] Compiler-bound PeTTaChainer rule attribution now requires a one-to-one
  cardinality closure between each retained stamp tuple and its evidence-basis
  tuple. A correctly rehashed attribution can no longer omit or invent a basis
  while remaining structurally valid. Local implementation commit `e826c4e`;
  focused and full 601-test verification passed with `git diff --check`
  (2026-07-24 15:00 PDT / 22:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Typed PeTTaChainer derived-result captures now require tuple-backed
  fact/rule stamp and evidence-basis collections, matching their immutable
  schema. Correctly rehashing a capture no longer admits mutable lists at this
  provenance boundary. Local implementation commit `9f34631`; focused and
  full 601-test verification passed with `git diff --check` (2026-07-24
  19:00 PDT / 2026-07-25 02:00 UTC). No runtime invocation,
  promotion/write, upstream/remote action, paid compute, or live integration.
- [x] Compiler-bound PeTTaChainer derived captures and rule attributions now
  require distinct fact/rule sentence digests and proof IDs. A caller can no
  longer forge and correctly rehash a nominal one-rule TotalMP artifact that
  aliases the rule to the fact compiler identity. Local implementation commit
  `19fb7a9`; focused and full 601-test verification passed with `git diff
  --check` (2026-07-24 23:00 PDT /
  2026-07-25 06:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.
- [x] PeTTaChainer episode-manifest v2 now commits the compiler-bound TotalMP
  rule-attribution identity. Construction and reload require the supplied
  attribution to be exactly derivable from the supplied typed result, and a
  valid manifest paired with another valid result/attribution pair fails
  closed. Local implementation commit `9ef4fef`; focused and full 601-test
  verification passed with repository-local
  `git diff --check` (2026-07-25 09:02 PDT / 16:02 UTC). No runtime
  invocation, promotion/write, upstream/remote action, paid compute, or live
  integration.
- [x] PeTTaChainer episode-manifest contract binding now has a fully rehashed
  artifact adversary. Altering `contract_cid` and recomputing both the typed
  manifest digest and outer document checksum still fails closed against the
  supplied immutable compiler contract. Focused and full 601-test verification
  passed with repository-local `git diff --check`; local regression commit
  `effcba5` (2026-07-25 17:00 PDT / 2026-07-26 00:00 UTC). No runtime invocation, promotion/write,
  upstream/remote action, paid compute, or live integration.
- [x] PeTTaChainer episode-manifest validator-capture binding now has a fully
  rehashed artifact adversary. Altering `validator_capture_cid` and recomputing
  both the typed manifest digest and outer document checksum still fails
  closed against the supplied admitted result capture. Focused and full
  601-test verification passed with repository-local `git diff --check`; local
  regression commit `947367a` (2026-07-25 19:00 PDT / 2026-07-26 02:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.
- [x] PeTTaChainer episode-manifest runtime-capture binding now has a fully
  rehashed artifact adversary. Altering `runtime_capture_cid` and recomputing
  both the typed manifest digest and outer document checksum still fails
  closed against the supplied admitted result capture. Focused and full
  601-test verification passed with repository-local `git diff --check`; local
  regression commit `bc2338c` (2026-07-25 21:00 PDT / 2026-07-26 04:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.
- [x] PeTTaChainer episode-manifest episode anchoring now has a fully rehashed
  artifact adversary. Altering `episode_id` and recomputing both the typed
  manifest digest and outer document checksum still fails closed against the
  supplied compiler contract. Local regression commit `47022b3`; focused and
  full verification passed with repository-local `git diff --check`
  (2026-07-26 01:00 PDT / 08:00 UTC). No
  runtime invocation, promotion/write, upstream/remote action, paid compute,
  or live integration.
- [x] The provider-free usability gate now treats a dangling output-directory
  symlink as an existing operator-owned path. The gate rejects it before any
  target creation or ingestion, preserving the exact link text and leaving the
  missing target absent. Focused 2-test and full 603-test verification passed
  with repository-local `git diff --check`; local commit `63f9a2e`
  (2026-07-27 01:00 PDT / 08:00 UTC).
  No runtime invocation, promotion/write, upstream/remote action, paid compute,
  dependency change, or live integration.
- [x] The provider-free usability gate now treats a dangling output symlink as
  an occupied operator-selected path. It exits before ingestion/inference,
  preserves the exact link target, and creates no target directory. Focused 2
  and full 603-test verification passed with repository-local `git
  diff --check`; local regression commit `63f9a2e` (2026-07-27 01:00 PDT /
  08:00 UTC). No runtime invocation, promotion/write, upstream/remote action,
  paid compute, dependency change, or live integration.
- [x] The provider-free usability summary now explicitly records its
  `read-only` canary mode and false autonomous-write/promotion authority, so
  downstream audit consumers do not have to infer the non-live boundary from
  prose. Focused 5-test and full 606-test verification passed with
  repository-local `git diff --check`; local commit `81e13d7` (2026-07-27
  11:00 PDT / 18:00 UTC).
  No promotion/write, live integration, paid compute, dependency change, or
  remote action.
- [x] Frozen provider-free usability admission now semantically verifies the
  integrity-bound `inference.json` outcome against the summary claim. A fully
  rehashed failed inference can no longer be presented as passed. Focused
  7-test and full 613-test verification passed with repository-local `git
  diff --check`; local commit `ff3b552` (2026-07-27 23:00 PDT / 2026-07-28
  06:00 UTC); local commit `920fe33`. No runtime invocation, promotion/write,
  live integration,
  dependency change, or remote action.
- [x] Frozen provider-free usability inference admission now requires the exact
  producer result, classification, and semantic-marker member sets. Fully
  rehashed undeclared top-level and nested live-authority fields fail closed.
  Focused 11-test and full 617-test verification passed with repository-local
  `git diff --check`; local commit `15b11ce` (2026-07-28 05:05 PDT /
  12:05 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, or remote action.
- [x] Frozen provider-free usability admission now binds successful inference
  to the exact reviewed classifier identity and requires its success-path
  `log`/`reasons` fields to remain null/empty. A fully rehashed result relabeled
  to an unreviewed pass classifier fails closed. Focused 12-test and full
  618-test verification passed with repository-local `git diff --check`;
  local commit `eb90064` (2026-07-28 07:00 PDT / 14:00 UTC). No runtime invocation, canonical write,
  promotion, live integration, dependency change, or remote action.
- [x] Frozen provider-free usability inference admission now requires the
  exact producer source-item member set inside the provenance sidecar. A fully
  rehashed nested `promotion_authorized` claim fails closed. Focused 20-test
  and full 626-test verification passed with repository-local `git
  diff --check`; local commit `c4dcb95` (2026-07-28 21:00 PDT / 2026-07-29
  04:00 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, or remote action.
- [x] Frozen provider-free usability admission now binds the provenance
  source's pi-PLN extension to the exact producer boundary: context selection
  was not run, no contextual packets were admitted, and EC projection remains
  deferred. A fully rehashed claim that generated contexts were admitted fails
  closed. Focused 23-test and full 629-test verification passed with
  repository-local `git diff --check`; local commit `a6edd1b` (2026-07-29
  03:00 PDT / 10:00 UTC). No
  runtime invocation, canonical write, promotion, live integration, dependency
  change, or remote action.
- [x] Frozen provider-free usability admission now binds every semantic
  diagnostic line to an observed bounded stdout/stderr tail. A fully rehashed
  bundle carrying an invented authority-shaped diagnostic fails closed.
  Focused 29-test and full 635-test verification passed with repository-local
  `git diff --check`; local commit `e9c6fc3` (2026-07-29 15:00 PDT /
  22:00 UTC). No runtime
  invocation, canonical write, promotion, live integration, dependency
  change, paid compute, or remote action.
- [x] Frozen provider-free usability admission now independently recounts
  successful, failed, and error semantic markers from the bounded captured
  runtime tails. A fully rehashed result retaining a claimed pass count after
  removing the observed `Passed: true` marker fails closed. Focused 30-test and
  full 636-test verification passed with repository-local `git diff --check`
  in local commit `338c2aa` (2026-07-29 17:00 PDT / 2026-07-30 00:00 UTC). No
  runtime invocation, canonical write, promotion, live integration, dependency
  change, or remote action.
- [x] The frozen Phase-0 replay anchor now requires exactly one observed
  semantic result and exactly one successful marker in its integrity-bound
  output. A fully rehashed deterministic output containing a second
  `(Passed: #t)` fails closed. Focused reload and full 639-test verification
  passed with repository-local `git diff --check` (2026-07-30 03:01 PDT /
  10:01 UTC); local commit `08c67a6`. No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] Fresh Phase-0 replay now requires the normalized absolute executable
  launch identity emitted by the digest-pinned subprocess helper, in addition
  to the frozen executable digest. A manually reconstructed relative-path
  capture fails closed. Focused and full 639-test verification passed with
  repository-local `git diff --check` (2026-07-30 17:00 PDT / 2026-07-31
  00:00 UTC); local commit `8082999`. No external runtime invocation,
  promotion/write, live
  integration, dependency change, paid compute, or remote action.
- [x] Typed kernel captures now require every argv, stdout/stderr, cwd, and
  environment string to be valid UTF-8, matching the byte-counting, hashing,
  and strict-decoding boundary used by the bounded runner and Phase-0 replay.
  Focused 2-test and full 641-test verification passed with repository-local
  `git diff --check` (2026-07-31 03:00 PDT / 10:00 UTC); local commit
  `af1ec4d`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] The bounded kernel runner now rejects non-UTF-8 program, argv, cwd, and
  explicit-environment text as typed `ValueError`s before process launch,
  matching the reconstructed-capture boundary. No-launch regression checks
  plus the full 641-test suite and repository-local `git diff --check` passed
  (2026-07-31 05:00 PDT / 12:00 UTC); local commit `ed4d68d`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The UTF-8 process-environment boundary now has symmetric key/value
  regressions at both typed-capture reconstruction and the no-spawn runner
  gate. Surrogate-bearing environment keys can no longer regress unnoticed
  while value-only coverage passes. Focused 2-test and full 641-test
  verification passed with repository-local `git diff --check` (2026-07-31
  07:01 PDT / 14:01 UTC); local commit `12acaea`. No external runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] The bounded kernel working-directory boundary now resolves caller input
  to the exact absolute directory delivered to `Popen` and retained in the
  typed capture; relative/non-normalized reconstructed captures fail closed,
  and the byte ceiling is rechecked after resolution. Focused 2-test and full
  642-test verification passed with repository-local `git diff --check`
  (2026-07-31 11:00 PDT / 18:00 UTC). No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action; local commit `ef5136c`.
- [x] The bounded kernel runner now rejects scalar text/bytes and non-iterable
  `argv` inputs through its typed `ValueError` boundary, preventing a bare
  executable string from being split into one-character arguments. Focused and
  full 643-test verification passed with repository-local `git diff --check`
  (2026-07-31 17:00 PDT / 2026-08-01 00:00 UTC); local commit `a535e9a`. No
  external runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] The bounded kernel runner now consumes argv incrementally under its OS
  framing-byte ceiling, so an unbounded iterator fails closed instead of being
  materialized without limit before validation. Focused and full 643-test
  verification plus repository-local `git diff --check` passed (2026-07-31
  19:00 PDT / 2026-08-01 02:00 UTC); local commit `3818a3b`. No external
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] The bounded kernel runner now converts failures raised while consuming a
  caller-supplied argv iterator into its typed `ValueError` contract, retaining
  the original exception as cause and never reaching process launch. Focused
  and full 643-test verification passed with repository-local `git diff
  --check` (2026-07-31 21:00 PDT / 2026-08-01 04:00 UTC); local commit
  `9e1ee9c`. No external runtime,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel subprocess runner now normalizes failures raised while
  traversing a caller-supplied environment mapping into its typed `ValueError`
  contract before launch. A marker-backed focused regression, the full
  643-test suite, and repository-local `git diff --check` passed (2026-07-31
  23:00 PDT / 2026-08-01 06:00 UTC); local commit `10ab2fd`. No external
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] The bounded kernel subprocess runner now rejects malformed entries from
  caller-supplied environment iterators through its typed `ValueError`
  contract before process launch. A marker-backed focused regression, the full
  643-test suite, and repository-local `git diff --check` passed (2026-08-01
  01:02 PDT / 08:02 UTC); local commit `bfad0a9`. No external runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] The bounded kernel subprocess runner now rejects scalar values yielded
  by a hostile `Mapping.items()` implementation instead of silently unpacking
  a two-character string into an environment key/value pair. Marker-backed
  focused verification, the full 643-test suite, and repository-local `git
  diff --check` passed (2026-08-01 03:00 PDT / 10:00 UTC); local commit
  `776efe9`. No external runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] The bounded kernel subprocess runner now normalizes process-construction
  failures represented by `subprocess.SubprocessError` into its typed
  `ValueError` contract, retaining the original failure as the cause. Focused
  2-test and full 644-test verification passed with repository-local `git
  diff --check` (2026-08-01 07:01 PDT / 14:01 UTC); local commit `b7322fe`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] The bounded kernel subprocess runner now converts OS-level stdout/stderr
  read failures into its typed `ValueError` contract, retaining the original
  exception as the cause and terminating the isolated process group. A focused
  regression, the full 645-test suite, and repository-local `git diff --check`
  passed (2026-08-01 09:00 PDT / 16:00 UTC); local commit `43152c2`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel subprocess runner now normalizes every ordinary
  output-reader exception into its typed `ValueError` contract, rather than
  allowing an unexpected reader failure to escape a daemon thread and surface
  later as a missing-capture `KeyError`. Focused regression and the full
  645-test suite passed with repository-local `git diff --check` (2026-08-02
  20:11 PDT / 2026-08-03 03:11 UTC); local commit `9546ad1`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel subprocess runner now normalizes every ordinary
  stdin write/flush/close exception through its typed incomplete-delivery
  contract. An unexpected writer failure can no longer die only in a daemon
  thread and permit a false successful capture. Focused 2-test and full
  646-test verification passed with repository-local `git diff --check`
  (2026-08-02 21:21 PDT / 2026-08-03 04:21 UTC); local commit `cf31b9d`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] The bounded kernel subprocess runner now normalizes failure of the
  post-timeout reap through a typed `ValueError`, retaining the cleanup failure
  as its cause while the existing finalizer closes captured streams. Focused
  and full 648-test verification passed with repository-local `git diff
  --check` (2026-08-03 01:00 PDT / 08:00 UTC); local commit `80dc2fa`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel subprocess runner now normalizes unexpected worker
  `join()` cleanup failures through a typed `ValueError`, retains the original
  cause, and still attempts every worker join plus both captured-stream closes.
  Focused and full 651-test verification passed with repository-local `git
  diff --check` (2026-08-03 07:01 PDT / 14:01 UTC); local commit `6ac5199`.
  No external runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] The bounded kernel subprocess runner now normalizes capture-worker
  startup failures after child launch, kills and reaps the process, joins only
  successfully started workers, and closes both captured streams. Focused and
  full 652-test verification passed with repository-local `git diff --check`
  (2026-08-03 09:00 PDT / 16:00 UTC); local commit `3626e60`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel runner now normalizes capture-worker construction
  failures after child launch, kills/reaps the child, attempts closure of all
  three subprocess pipes, and separately normalizes cleanup failure. Focused
  2-test and full 654-test verification passed with repository-local `git
  diff --check` (2026-08-03 11:01 PDT / 18:01 UTC); local commit `55435a7`. No external runtime,
  promotion/write, live integration, dependency, paid compute, or remote
  action.
- [x] The bounded kernel runner now closes stdin as well as stdout/stderr during
  post-launch finalization, so a capture-worker startup failure cannot leave
  the unstarted writer's child pipe open. Focused and full 654-test
  verification passed with repository-local `git diff --check` (2026-08-03
  13:00 PDT / 20:00 UTC); local commit `0ae13bc`. No external runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] Worker-construction cleanup now preserves a failed process-group kill as
  the typed construction-cleanup cause instead of discarding it and reporting
  only the triggering thread-constructor failure. Focused and full 655-test
  verification passed with repository-local `git diff --check` (2026-08-03
  15:00 PDT / 22:00 UTC); local commit `15f5335`. No external runtime,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The bounded kernel subprocess runner now preserves a failed
  process-group termination as the primary cleanup failure when the ordinary
  direct-process wait also fails, instead of masking the higher-risk orphan
  condition behind the wait error. Focused and full 656-test verification
  passed with repository-local `git diff --check` (2026-08-03 17:01 PDT /
  2026-08-04 00:01 UTC); local commit `98e1f23`. No external runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] Timeout-path process-group termination failures now retain cleanup
  priority over the triggering timeout. The runner defers timeout
  classification until common finalization, so a failed kill is surfaced with
  its original cause after worker joins and pipe closure. Focused 3-test and
  full 657-test verification passed with repository-local `git diff --check`
  (2026-08-03 19:00 PDT / 2026-08-04 02:00 UTC); local commit `afa955e`. No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] The requested-pipe validation boundary now has an adversarial
  process-group termination regression: if malformed process construction
  omits a requested pipe and `killpg` fails, the runner preserves that failure
  as the cause of its typed cleanup error while still reaping the direct
  process and closing every supplied stream. Focused 86-test and full 661-test
  verification passed with repository-local `git diff --check` (2026-08-04
  03:00 PDT / 10:00 UTC); local commit `fc989fd`. No external runtime,
  promotion/write, live integration, dependency, paid compute, or remote
  action.
- [x] Requested-pipe validation now has an adversarial direct-child reap
  regression: if a malformed process construction omits a requested pipe and
  `wait()` fails, the runner preserves that failure as the cause of its typed
  pipe-validation cleanup error while still closing every supplied stream.
  Focused and full 662-test verification passed with repository-local `git
  diff --check` (2026-08-04 05:01 PDT / 12:01 UTC); local commit `d3f0851`.
  No external runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Completed the requested-pipe cleanup regression matrix for process-group
  kill and direct-process reap failures. Both failures retain the first cleanup
  cause through the typed validation error while every later cleanup action is
  still attempted. Focused 2-test and full 662-test verification passed with
  repository-local `git diff --check` (2026-08-04 07:01 PDT / 14:01 UTC);
  local commits `fc989fd` and `d3f0851`. This closes the concrete malformed-pipe
  follow-up; further speculative subprocess hardening remains frozen in favor
  of the bounded Phase-1 semantic capture/reload gate. No external runtime,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] The malformed requested-pipe cleanup boundary now has an already-exited
  child regression: `ProcessLookupError` from process-group kill is treated as
  benign without skipping direct-process reap or closure of every supplied
  stream, and the primary typed missing-pipe failure remains intact. Focused
  and full 663-test verification passed with repository-local `git diff
  --check` (2026-08-04 09:00 PDT / 16:00 UTC); local commit `2d3af71`. No
  external runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] Raw bounded kernel process evidence now has create-once checksummed v1
  persistence. Reload reconstructs the complete typed argv, return code,
  stdout/stderr, program/executable identities, working directory, and explicit
  environment before manifest admission; the two-cycle clean-room gate now
  reloads this artifact instead of manually reconstructing its capture. Focused
  2-test and full 664-test verification passed with repository-local `git diff
  --check` (2026-08-04 11:00 PDT / 18:00 UTC); local commit `b54a935`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or remote
  action.
- [x] Completed the bounded Phase-2 compiler/backend/validator/manifest/exact-
  replay milestone by adding capture-bound exact replay. Fresh semantic replay
  must now originate as exactly one complete result line in a successful
  `KernelProcessCapture` with empty stderr before its typed digest can match the
  immutable compiler-bound expected result. Focused and full 664-test
  verification passed with repository-local `git diff --check` (2026-08-04
  13:03 PDT / 20:03 UTC); local commit `453a83b`. General rule/trace identity stays deferred; no
  external runtime invocation, promotion/write, live integration, dependency,
  paid-compute, or remote action.
- [x] Episode-manifest construction now type-checks all five immutable audit
  dependencies (compiled inputs, validated result, pi chart, evidence snapshot,
  and episode budget) before dereferencing them. Malformed orchestration input
  fails through stable public `ValueError` boundaries instead of leaking
  `AttributeError`. Focused 1-test and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-04 19:10 PDT / 2026-08-05
  02:10 UTC); local commit `a125a1b`. No external runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] Episode-manifest reload now validates an optional complete program as a
  non-empty string before artifact I/O. Malformed replay callers therefore
  receive the stable program `ValueError` even when the requested artifact is
  absent, matching the precedence already established for typed replay
  dependencies. Focused and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-05 01:14 PDT / 08:14 UTC);
  local commit `ba763bd`. No
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] PeTTaChainer episode-manifest reload now validates its immutable
  contract, derived-result capture, and rule attribution before artifact I/O.
  Malformed orchestration inputs therefore fail through stable typed
  `ValueError` boundaries even when the artifact is missing. Focused and full
  664-test verification passed with repository-local `git diff --check`
  (2026-08-05 03:13 PDT / 10:13 UTC); local commit `bd086fb`. No external
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] PeTTaChainer episode-manifest writes now serialize and type-check the
  immutable manifest before creating missing parent directories. Malformed
  callers therefore fail without filesystem mutation. Focused 142-test and
  full 664-test verification passed with repository-local `git diff --check`
  (2026-08-05 07:01 PDT / 14:01 UTC); local commit `87e45c0`. No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] PeTTaChainer derived-result capture serialization now rejects malformed
  values through a typed `ValueError` before its writer creates a destination
  parent. Focused and full 664-test verification passed with repository-local
  `git diff --check` (2026-08-05 09:03 PDT / 16:03 UTC); local commit `8771716`.
  No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] PeTTaChainer rule-attribution persistence now validates and serializes
  the immutable attribution before creating destination directories. A
  regression proves malformed caller input raises the stable `ValueError`
  boundary without filesystem mutation. Focused and full 664-test verification
  passed with repository-local `git diff --check` (2026-08-05 11:00 PDT /
  18:00 UTC); local commit `c3de0a0`. No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] Stock pi-PLN episode-manifest serialization now rejects malformed
  manifests through a stable typed `ValueError` before creating destination
  parents. Focused and full 664-test verification passed with repository-local
  `git diff --check` (2026-08-05 13:04 PDT / 20:04 UTC); local commit `f7fba44`.
  No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] Validated patham9 kernel-result persistence now rejects malformed result
  objects before creating parent directories. The document builder exposes a
  stable typed `ValueError` boundary and the writer serializes fully before
  filesystem mutation. Focused and full 664-test verification passed with
  repository-local `git diff --check` (2026-08-05 15:01 PDT / 22:01 UTC);
  local commit `1974cc8`.
  No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] Evidence-snapshot serialization now validates its immutable typed input
  before creating parent directories, so malformed callers receive a stable
  `ValueError` without filesystem mutation. Focused and full 665-test
  verification passed with repository-local `git diff --check` (2026-08-05
  17:10 PDT / 2026-08-06 00:10 UTC); local commit `ecd38a8`. No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Immutable compiled episode-input persistence now type-checks and
  serializes the complete checksummed document before creating destination
  directories. A malformed-input regression proves the filesystem remains
  untouched. Focused and full 666-test verification passed with
  repository-local `git diff --check` (2026-08-05 19:00 PDT / 2026-08-06
  02:00 UTC); local commit `e012c48`. No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] Validated-result reload now type-checks its required immutable compiled
  inputs before artifact I/O. Malformed callers receive the stable `ValueError`
  boundary even when the artifact is absent. Focused and full 667-test
  verification passed with repository-local `git diff --check` (2026-08-05
  23:00 PDT / 2026-08-06 06:00 UTC); local commit `4eec465`. No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] PeTTaChainer derived-result clean-room reload now validates its required
  immutable episode contract before artifact I/O. A malformed contract paired
  with an absent artifact fails through a stable `ValueError` boundary instead
  of being masked by `FileNotFoundError`. Focused and full 667-test verification
  passed with repository-local `git diff --check` (2026-08-06 03:00 PDT /
  10:00 UTC); local commit `6cd83e5`. No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.

- [x] Evidence-snapshot reload now requires the exact declared top-level
  envelope, rejecting undeclared authority-shaped fields even when the
  payload checksum remains valid. Focused and full 667-test verification
  passed with repository-local `git diff --check` (2026-08-06 07:01 PDT /
  14:01 UTC); local commit `d956bc6`. No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] Pi-chart construction now type-checks its immutable context, policy, and
  evidence-snapshot dependencies before provenance field access. Malformed
  callers fail through stable `ValueError` contracts rather than incidental
  `AttributeError`s. Focused and full 668-test verification passed with
  repository-local `git diff --check` (2026-08-06 09:02 PDT / 16:02 UTC);
  local commit `fbf6ed5`. No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.
- [x] The deterministic π-PLN episode-input compiler now type-checks its
  immutable chart and evidence-snapshot dependencies before provenance field
  access. Malformed callers receive stable `ValueError` boundaries instead of
  incidental `AttributeError`s. Focused and full 669-test verification passed
  with repository-local `git diff --check` (2026-08-06 11:00 PDT / 18:00 UTC);
  local commit `225aade`. No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.
- [x] Deterministic episode compilation now type-checks every supplied
  `EvidencePacket` and `EvidenceBasis` before field access. Malformed members
  fail through stable `ValueError` contracts instead of leaking
  `AttributeError`. Focused and full 669-test verification passed with
  repository-local `git diff --check` (2026-08-06 13:01 PDT / 20:01 UTC);
  local commit `2f50b6b`.
  No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] Immutable compiled episode inputs now validate every stamp-map and
  compiled-sentence collection member before dereferencing it. Malformed
  reconstructed models fail through stable `ValueError` contracts instead of
  leaking `AttributeError` into PLN/PeTTaChainer adapters. Focused and full
  669-test verification passed with repository-local `git diff --check`
  (2026-08-06 15:00 PDT / 22:00 UTC); local commit `940f8d9`. No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] PeTTaChainer derived-result construction now type-checks its immutable
  fact, rule, validator-capture, and runtime-capture dependencies before field
  access. Malformed callers fail through stable `ValueError` boundaries rather
  than leaking `AttributeError`. Focused and full 669-test verification passed
  with repository-local `git diff --check` (2026-08-06 19:00 PDT / 2026-08-07
  02:00 UTC); local commit `020f1a4`. No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] PeTTaChainer episode-manifest construction now type-checks its immutable
  episode budget before digest field access. Malformed orchestration input
  fails through a stable `ValueError` instead of leaking `AttributeError`.
  Focused and full 669-test verification passed with repository-local `git
  diff --check`; local commit `0ec094f` (2026-08-06 21:03 PDT / 2026-08-07
  04:03 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] PeTTaChainer compiler-adapter statements now require every provenance
  stamp to be a non-negative integer (excluding booleans) and every evidence
  basis ID to be a non-empty string. Focused and full 671-test verification
  passed with repository-local `git diff --check`; local commit `2450609`
  (2026-08-07 01:00 PDT / 08:00 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] PeTTaChainer episode contracts now enforce one consistent bijection
  between stamps and evidence-basis ids across all checked-add statements, so
  individually valid reconstructed sidecars cannot contradict each other.
  Focused and full 672-test verification passed with repository-local `git
  diff --check`; local commit `03d58c1` (2026-08-07 05:01 PDT / 12:01 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] PeTTaChainer episode contracts now require their checked-add statement
  collection to be an immutable tuple, preventing a frozen contract from
  retaining a caller-mutable list. Focused and full 673-test verification
  passed with repository-local `git diff --check`; local commit `5a30718`
  (2026-08-07 07:01 PDT / 14:01 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] Manually reconstructed PeTTaChainer episode contracts now enforce the
  same aggregate one-million-character add/query atom ceiling as the compiler
  adapter, preventing direct callers from bypassing the bounded runtime-input
  contract. Focused and full 675-test verification passed with repository-local
  `git diff --check`; local commit `dde58b4` (2026-08-07 13:01 PDT / 20:01
  UTC). No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] Reconstructed PeTTaChainer episode contracts now enforce their aggregate
  checked-add statement character ceiling incrementally before allocating the
  proof-id uniqueness tuple/set or scanning provenance. An oversized repeated
  statement collection therefore fails at the resource boundary instead of a
  later semantic check. Focused and full 678-test verification passed with
  repository-local `git diff --check`; local commit `a8dc813` (2026-08-07
  19:00 PDT / 2026-08-08 02:00 UTC). No runtime invocation, promotion/write,
  live integration, dependency change, paid compute, or remote action.
- [x] PeTTaChainer episode contracts now type-check and bound query text before
  proof-id uniqueness and stamp/evidence provenance scans. An adversarial
  duplicate-statement contract therefore fails at the aggregate resource
  boundary instead of doing avoidable provenance work. Focused and full
  679-test verification passed with repository-local `git diff --check`;
  local commit `716292a` (2026-08-07 21:00 PDT / 2026-08-08 04:00 UTC). No
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] Reconstructed PeTTaChainer derived-result captures now type-check and
  bound query, atom, and proof text before canonical query parsing. Two
  parser-sentinel regressions and the full 681-test suite passed with
  repository-local `git diff --check` (2026-08-07 23:00 PDT / 2026-08-08
  06:00 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] Reconstructed stock pi-PLN validated results now type-check and bound
  their duplicate query term before canonical S-expression parsing. Focused
  and full 682-test verification passed with repository-local `git diff
  --check`; local commit `4020052` (2026-08-08 01:00 PDT / 08:00 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] Immutable evidence bases now require tuple-backed member-token and
  causal-group provenance collections, preventing reconstructed frozen bases
  from retaining caller-owned mutable lists. Focused and full 684-test
  verification passed with repository-local `git diff --check`; local commit
  `620ea50` (2026-08-08 15:00 PDT / 22:00 UTC). No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] Immutable evidence snapshots now require tuple-backed packet-id and
  content-digest collections, including tuple-backed nested digest pairs, so
  reconstructed frozen snapshots cannot retain caller-owned mutable lists.
  Focused and full 685-test verification passed with repository-local `git
  diff --check`; local commit `7ba8f1e` (2026-08-08 17:00 PDT / 2026-08-09
  00:00 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.
- [x] Immutable pi-PLN charts now require a typed `ChartPolicy` and a
  tuple-backed selected-packet collection, preventing malformed dependency
  dereferences and caller-owned mutation after reconstruction. Focused and
  full 688-test verification passed with repository-local `git diff --check`;
  local commit `a6c7fd1` (2026-08-08 23:00 PDT / 2026-08-09 06:00 UTC). No
  runtime invocation, promotion/write, live integration, dependency change,
  paid compute, or remote action.
- [x] Evidence-snapshot construction now type-checks every packet before
  reading packet identity or status, keeping malformed builder inputs within
  the stable `ValueError` boundary. Focused and full 689-test verification
  passed with repository-local `git diff --check`; local commit `da3cf8b`
  (2026-08-09 01:00 PDT / 08:00 UTC). No runtime invocation, promotion/write, live integration,
  dependency change, paid compute, or remote action.

- [x] Immutable pi-PLN charts now require a typed `ChartPolicy` and
  tuple-backed selected-packet collection, preventing malformed dependencies
  and caller-owned mutable lists at reconstruction. Focused and full 688-test
  verification passed with repository-local `git diff --check`; local commit
  `a6c7fd1` (2026-08-08 23:02 PDT / 2026-08-09 06:02 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Evidence-packet provenance identifiers now fail closed as non-empty
  strings before sorting/deduplication, preventing malformed token or parent
  identifiers from leaking comparison `TypeError`s. Focused and full 690-test
  verification passed with repository-local `git diff --check`; local commit
  `8b83035` (2026-08-09 03:02 PDT / 10:02 UTC). No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.
- [x] Immutable evidence tokens now validate optional provenance identifiers
  as non-empty strings when present and require an integer schema version,
  closing malformed reconstruction and `TypeError` paths. Focused and full
  691-test verification passed with repository-local `git diff --check`;
  local commit `d3cc023` (2026-08-09 05:00 PDT / 12:00 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Evidence basis provenance members now require non-empty string token and
  causal-group ids before sorting or set comparison, keeping malformed
  reconstructed bases inside the stable `ValueError` boundary. Focused and
  full 692-test verification passed with repository-local `git diff --check`
  (2026-08-09 07:03 PDT / 14:03 UTC); local commit `79e8264`. No runtime invocation,
  promotion/write, live integration, dependency change, paid compute, or
  remote action.
- [x] Deterministic stamp-map construction now type-checks every supplied
  `EvidenceBasis` before sorting or field access, so malformed reconstructed
  input fails through the public `ValueError` boundary instead of leaking an
  incidental attribute error. Focused and full 693-test verification passed
  with repository-local `git diff --check`; local commit `9be0d85`
  (2026-08-09 09:00 PDT / 16:00 UTC).
  No runtime invocation, promotion/write, live integration, dependency
  change, paid compute, or remote action.
- [x] Evidence-basis construction now type-checks its immutable packet and
  token inputs before provenance field access. Adversarial reconstructed
  objects fail through stable `ValueError` boundaries. Focused and full
  694-test verification passed with repository-local `git diff --check`;
  local commit `8e926d3` (2026-08-09 11:03 PDT / 18:03 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Exact evidence-capsule merging now type-checks both immutable capsules
  and every optional evidence-basis record before field access. Malformed
  reconstructed inputs fail through stable `ValueError` contracts instead of
  leaking `AttributeError`. Focused and full 696-test verification passed with
  repository-local `git diff --check`; local commit `9f61044` (2026-08-09
  15:00 PDT / 22:00 UTC). No runtime invocation, promotion/write, live
  integration, dependency change, paid compute, or remote action.
- [x] Immutable evidence snapshots now validate packet-id provenance members
  before uniqueness sorting, so mixed-type reconstructed identifiers fail
  through the stable `ValueError` boundary instead of leaking `TypeError`.
  Focused and full 698-test verification passed with repository-local `git
  diff --check`; local commit `e93f4bb` (2026-08-09 21:01 PDT / 2026-08-10 04:01 UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
- [x] Immutable evidence snapshots now require every packet-content digest
  entry to be an exact two-field tuple before unpacking, so reconstructed
  wrong-arity metadata fails through a stable `ValueError` boundary. Focused
  and full 698-test verification passed with repository-local `git diff
  --check`; local commit `5b842f4` (2026-08-09 23:00 PDT / 2026-08-10 06:00
  UTC). No runtime
  invocation, promotion/write, live integration, dependency change, paid
  compute, or remote action.
