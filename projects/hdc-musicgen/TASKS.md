# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] **Scheduled post-commit closure audit (2026-08-20 19:45Z, local only).** After
  reviewing the durable notebook and latest completed GPU run
  (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0), verified the
  post-`eb39c96` state: full local suite passed 26/26 in 1.02 s, worktree
  `git status --short` empty, `git diff --check` passed, and worktree
  `hdc_musicgen_structural.py` SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a`
  resolves to Git blob `ffafd741d2e58abeb0217af2ea94b67b8824affe`, remains
  byte-identical to pin `74287d9` and the immutable A40-retry bundle (whose
  `artifacts/local-sync/` remains empty). The explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the support-aware NLL policy remains frozen; no source,
  test, threshold, or decision changed. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-20 19:45Z entry).

- [x] **Scheduled closure audit (2026-08-20 15:43Z, local only).** After
  reviewing the durable notebook and latest completed GPU run
  (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0), verified the
  post-`eb39c96` state: full local suite passed 26/26 in 0.81 s, worktree
  `git status --short` empty, `git diff --check` passed, and worktree
  `hdc_musicgen_structural.py` SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a` remains
  byte-identical to pin `74287d9` and the retained A40-retry bundle. The
  explicit filesystem gate confirmed `smoke-r2/artifacts/` remains absent.
  Smoke-r2 remains terminally a no-result and the support-aware NLL policy
  remains frozen; no source, test, threshold, or decision changed. No
  provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-20 15:43Z entry).

- [x] **Scheduled closure audit (2026-08-20 11:43Z, local only).** After
  reviewing the durable notebook and latest completed GPU run
  (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0), verified the
  post-`eb39c96` state: full local suite passed 26/26 in 0.87 s, worktree
  `git status --short` empty, `git diff --check` passed, and worktree
  `hdc_musicgen_structural.py` SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a` remains
  byte-identical to pin `74287d9` and the retained A40-retry bundle (whose
  `artifacts/local-sync/` remains empty). The explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the support-aware NLL policy remains frozen; no source,
  test, threshold, or decision changed. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-20 11:43Z entry).

- [x] **Scheduled closure audit (2026-08-20 07:36Z, local only).** After
  reviewing the durable notebook and latest completed GPU run
  (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0), verified the
  post-`eb39c96` state: full local suite passed 26/26 in 0.88 s, worktree
  `git status --short` empty, `git diff --check` passed, and worktree
  `hdc_musicgen_structural.py` SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a` remains
  byte-identical to pin `74287d9` and the immutable A40-retry bundle. The
  explicit filesystem gate confirmed `smoke-r2/artifacts/` remains absent.
  Smoke-r2 remains terminally a no-result and the support-aware NLL policy
  remains frozen; no source, test, threshold, or decision changed. No
  provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-20 07:36Z entry).

- [x] **Scheduled post-commit fail-closed closure audit (2026-08-20 03:31Z,
  local only).** After reviewing the durable notebook and latest completed
  GPU run (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0),
  verified the post-`eb39c96` state: full local suite passed 26/26 in 0.81–
  0.82 s, worktree `git status --short` empty, `git diff --check` passed,
  and runtime source resolution byte-held: worktree
  `hdc_musicgen_structural.py` SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a`
  equals Git blob `ffafd741d2e58abeb0217af2ea94b67b8824affe`, identical to
  pin `74287d9` and the immutable A40-retry bundle. The explicit filesystem
  gate confirmed `smoke-r2/artifacts/` remains absent. Smoke-r2 remains
  terminally a no-result and the support-aware NLL policy remains frozen; no
  source, test, threshold, or decision changed. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-20 03:31Z entry).

- [x] **Scheduled test-hardening commit and hash reconciliation
  (2026-08-19 23:30Z, local only).** After reviewing the durable notebook
  and latest completed GPU run (`20260730T203550Z-full-corpus-r5`, fail-closed
  at Stage 0), committed the retained +111-line test-only NLL-policy
  hardening diff as `eb39c96` on `agent/direct-recurrence-stage0-gate`
  (boundary, sparse-stop, non-finite, four-span-threshold, and
  missing-aggregate coverage; no gate/source change). Full local suite
  passed 26/26 in 0.79 s before and after; `git status --short` empty and
  `git diff --check` passed. Worktree runtime source SHA-256
  `e1da8a357a7abe6e410173708a1807c591d20d54c041a4a9e90a512df4cdf24a` remains
  byte-identical to pin `74287d9` and the immutable A40-retry bundle; the
  committed test file (`783d42f7...`) matches the previously retained diff
  content, so no frozen-artifact byte changed. `smoke-r2/artifacts/` remains
  absent; smoke-r2 is terminally a no-result and the support-aware NLL policy
  stays frozen. No provider, network, remote resource, corpus download, or
  paid action occurred. Evidence: `NOTES.md` (2026-08-19 23:30Z entry).

- [x] **Scheduled A40-retry bundle integrity audit (2026-08-19 19:25Z,
  local only).** After reviewing the durable notebook and latest completed
  GPU run (`20260730T203550Z-full-corpus-r5`, fail-closed at Stage 0),
  verified the retained `20260803T214500Z-direct-recurrence-a40-retry`
  bundle: its runtime source resolves to Git blob
  `ffafd741d2e58abeb0217af2ea94b67b8824affe`, byte-identical to prospective
  pin `74287d9`; bundle test/runbook SHA-256s recorded; retry
  `artifacts/local-sync/` empty (no execution occurred); full local suite
  passed 26/26 in 0.87 s; `git diff --check` passed; retained test-only diff
  SHA-256 unchanged
  (`61c1962a238df6ef7be119d160d753e4d6f0582c30f9a4cd027f8ff1f9425f32`);
  `smoke-r2/artifacts/` remains absent. The approved reliable run retains a
  valid hash-stable source basis; smoke-r2 remains terminally a no-result
  and the support-aware NLL policy remains frozen. No source, test,
  threshold, or decision changed; no provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-19 19:25Z entry).

- [x] **Scheduled smoke-r2 chronology reconciliation (2026-08-19 15:21Z,
  local only).** After reviewing the latest completed GPU run
  (`20260730T203550Z-full-corpus-r5`), reconciled a contradiction between the
  smoke-r2 summary and its retained remote-job chronology. Pod
  `vbu5r47gstyl16` did receive code/audio and begin dependency setup; the
  replacement `2jh6oxjzogdexe` did not. Neither pod started Stage 0/S/A, both
  were deleted, and `smoke-r2/artifacts/` remains absent. Corrected the
  canonical PROJECT/RUN/current closure language without changing the
  terminal no-result, accepted NLL policy, source, tests, thresholds, or
  frozen decisions. `git diff --check` passed. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-19 15:21Z entry) and the retained `smoke-r2/REMOTE_JOB.md`.

- [x] **Scheduled historical Stage-A policy replay (2026-08-19 06:39Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  replayed the frozen support-aware gate against both retained Stage-A summary
  artifacts. The original 12-RELATED/1-UNRELATED smoke changes only from its
  stored pre-amendment NLL failure to a supported-policy pass; smoke-r3 remains
  a pass. In both cases the scientific relevance gate remains true, only the
  RELATED stratum is band-checked, UNRELATED is support-insufficient, and no
  non-finite, missing-condition, or unconditional alignment stop fires. The
  two-case canonical replay hashes to
  `74d7313417942d0a8ad7205e00697b216a8a2d158270451e51cb784771f7f580`;
  the full local suite passed 26/26, `git diff --check` passed, and the
  smoke-r2 artifacts gate remained absent. A first runner attempt using the
  minimal project venv stopped before import because NumPy/pytest are absent;
  the successful replay used the established system test environment. No
  source, test, artifact, threshold, or frozen decision changed. No provider,
  network, remote resource, corpus download, or paid action occurred.
  Evidence: `NOTES.md` (2026-08-19 06:39Z entry).

- [x] **Scheduled frozen-boundary matrix audit (2026-08-19 02:37Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  exercised ten exact/adjacent Stage-A NLL boundaries across sparse support
  (`n=3`) and supported strata (`n=4`): unconditional `0.5`/`8.0`, ordinary
  `1.5`/`6.0`, their just-outside failures, and the support transition at a
  value of `1.2`. The matrix passed 10/10 and hashes to
  `e5573c603a072d7c77fa6ebdba93ef50c91ff86020636c0e141b20abd0a8cfed`;
  the full local suite passed 26/26, `git diff --check` passed, the runtime
  source remained byte-identical to prospective pin `74287d9`, the retained
  test-only diff hash remained unchanged, and the smoke-r2 artifacts gate
  remained absent. No source, test, threshold, or frozen decision changed.
  No provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-19 02:37Z entry).

- [x] **Scheduled frozen-runtime integrity audit (2026-08-18 22:35Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  verified that the working-tree `hdc_musicgen_structural.py` and the file at
  prospective pin `74287d9` have the identical Git blob
  `ffafd741d2e58abeb0217af2ea94b67b8824affe`. All 10 focused Stage-A tests
  passed, the full local suite passed 26/26, `git diff --check` passed, the
  retained test-only diff still hashes to
  `61c1962a238df6ef7be119d160d753e4d6f0582c30f9a4cd027f8ff1f9425f32`,
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. No source, tests, threshold, or frozen decision changed. Smoke-r2
  remains terminally a no-result. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-18
  22:35Z entry).

- [x] **Scheduled retained-policy integrity audit (2026-08-18 18:35Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  hashed the retained 111-line test-only policy hardening diff as
  `61c1962a238df6ef7be119d160d753e4d6f0582c30f9a4cd027f8ff1f9425f32`;
  `git diff --check` passed, all 19 focused Stage-A regressions passed, the
  full local suite passed 26/26, and the explicit filesystem gate confirmed
  `smoke-r2/artifacts/` remains absent. No source, tests, threshold, or frozen
  decision changed. Smoke-r2 remains terminally a no-result. No provider,
  network, remote resource, corpus download, or paid action occurred.
  Evidence: `NOTES.md` (2026-08-18 18:35Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-18 14:34Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  all 19 focused Stage-A policy regressions passed; the full local suite passed
  26/26; `git diff --check` passed; and the explicit filesystem gate confirmed
  `smoke-r2/artifacts/` remains absent. The pre-existing 111-line test-file
  diff remains retained test-only policy hardening; this audit changed no
  source, tests, threshold, or frozen decision. Smoke-r2 remains terminally a
  no-result. No provider, network, remote resource, corpus download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-18 14:34Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-18 10:33Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-18 10:33Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-18 06:32Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-18 06:32Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-18 02:32Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-18 02:32Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 22:30Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 22:30Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 18:30Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 18:30Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 14:30Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 14:30Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 10:30Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 10:30Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 06:27Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 06:27Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-17 02:25Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-17 02:25Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 22:25Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 22:25Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 18:24Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 18:24Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 14:24Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 14:24Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 10:24Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 10:24Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 06:22Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 06:22Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-16 02:22Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-16 02:22Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 22:21Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-15 22:21Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 18:21Z, local only).**
  After reviewing the latest completed GPU run (`20260730T203550Z-full-corpus-r5`),
  four cross-stratum Stage-A regressions covering unconditional bounds,
  non-finite values, the supported ordinary band, and missing aggregates
  passed 4/4; the full local suite passed 26/26; `git diff --check` passed;
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. The pre-existing 111-line test-file diff remains retained test-only
  policy hardening; this audit changed no source, tests, threshold, or frozen
  decision. Smoke-r2 remains terminally a no-result. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-15 18:21Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 14:20Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. The pre-existing 111-line
  test-file diff remains the retained test-only policy hardening recorded by
  prior audits. This is verification only: smoke-r2 remains terminally a
  no-result and the accepted support-aware NLL policy remains frozen. No
  provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-15 14:20Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 10:19Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. The pre-existing 111-line
  test-file diff remains the retained test-only policy hardening recorded by
  prior audits. This is verification only: smoke-r2 remains terminally a
  no-result and the accepted support-aware NLL policy remains frozen. No
  provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-15 10:19Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 06:19Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. The existing test-file diff
  remains the retained test-only policy hardening recorded by prior audits.
  This is verification only: smoke-r2 remains terminally a no-result and the
  accepted support-aware NLL policy remains frozen. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-15 06:19Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-15 02:19Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. The existing test-file diff
  is the retained test-only policy hardening recorded by prior audits. This is
  verification only: smoke-r2 remains terminally a no-result and the accepted
  support-aware NLL policy remains frozen. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-15 02:19Z entry).

- [x] **Scheduled fail-closed closure audit (2026-08-14 22:19Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. This is verification only:
  smoke-r2 remains terminally a no-result and the accepted support-aware NLL
  policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-14 22:19Z
  entry).

- [x] **Scheduled fail-closed policy audit (2026-08-14 18:19Z, local only).**
  At prospective direct-recurrence pin `74287d9`, four cross-stratum Stage-A
  regressions covering unconditional bounds, non-finite values, the supported
  ordinary band, and missing aggregates passed 4/4; the full local suite
  passed 26/26; `git diff --check` passed; and the explicit filesystem gate
  confirmed `smoke-r2/artifacts/` remains absent. This is verification only:
  smoke-r2 remains terminally a no-result and the accepted support-aware NLL
  policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-14 18:19Z
  entry).

- [x] **Scheduled closure audit (2026-08-14 14:03Z, local only).**
  At prospective direct-recurrence pin `74287d9`, nine explicit Stage-A
  support/NLL policy tests passed 9/9, the full local suite passed 26/26,
  `git diff --check` passed, and the explicit filesystem gate confirmed
  `smoke-r2/artifacts/` remains absent. This is verification only: smoke-r2
  remains terminally a no-result and the accepted support-aware NLL policy
  remains frozen. No provider, network, remote resource, corpus download, or
  paid action occurred. Evidence: `NOTES.md` (2026-08-14 14:03Z entry).

- [x] **Post-endpoint-hardening closure verification (2026-08-14 09:55Z, local only).**
  At prospective direct-recurrence pin `74287d9`, all ten focused Stage-A
  tests passed, the full local suite passed 26/26, `git diff --check` passed,
  and the explicit filesystem gate confirmed `smoke-r2/artifacts/` remains
  absent. This verifies the accumulated test-only NLL-policy hardening without
  changing runtime code or the frozen policy; smoke-r2 remains terminally a
  no-result. No provider, network, remote resource, corpus download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-14 09:55Z entry).

- [x] **Cross-stratum inclusive NLL-band endpoint regression (2026-08-14 05:46Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  ordinary Stage-A band regression to prove that exact inclusive endpoints
  `1.50` and `6.00` pass independently for every aggregate in both RELATED
  and UNRELATED strata at the frozen four-span support threshold. Ten focused
  Stage-A tests passed 10/10, the full local suite passed 26/26, `git diff
  --check` passed, and `smoke-r2/artifacts/` remains absent. This is test-only
  hardening; smoke-r2 remains terminally a no-result and the accepted NLL
  policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-14 05:46Z
  entry).

- [x] **Cross-stratum supported NLL-band regression (2026-08-14 01:44Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  ordinary Stage-A band regression to prove that `1.49` and `6.01` fail
  closed independently for every aggregate in both RELATED and UNRELATED
  strata at the frozen four-span support threshold. Ten focused Stage-A
  tests passed 10/10, the full local suite passed 26/26, `git diff --check`
  passed, and `smoke-r2/artifacts/` remains absent. This is test-only
  hardening; smoke-r2 remains terminally a no-result and the accepted NLL
  policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-14
  01:44Z entry).

- [x] **Cross-stratum unconditional NLL-stop regression (2026-08-13 21:25Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  unconditional Stage-A regression to prove that `<0.5` and `>8` NLL values
  fail closed independently for every aggregate in both RELATED and
  UNRELATED strata, with the explicit alignment/broken-conditioning stop set.
  Ten focused Stage-A tests passed 10/10, the full local suite passed 26/26,
  `git diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the
  accepted NLL policy remains frozen. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-13
  21:25Z entry).

- [x] **Cross-stratum non-finite NLL regression (2026-08-13 17:20Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  non-finite Stage-A regression to prove that `NaN`, positive infinity, and
  negative infinity each fail closed independently for every aggregate in
  both RELATED and UNRELATED strata. Ten focused Stage-A tests passed 10/10,
  the full local suite passed 26/26, `git diff --check` passed, and
  `smoke-r2/artifacts/` remains absent. This is test-only hardening;
  smoke-r2 remains terminally a no-result and the accepted NLL policy remains
  frozen. No provider, network, remote resource, corpus download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-13 17:20Z entry).

- [x] **Cross-stratum missing-aggregate NLL regression (2026-08-13 12:49Z, local only).**
  At prospective direct-recurrence pin `74287d9`, added a focused regression
  proving that omission of any one Stage-A aggregate (`window`, `matched`,
  `random`, or `full`) fails closed independently in either the RELATED or
  UNRELATED stratum. Ten focused Stage-A tests passed 10/10, the full local
  suite passed 26/26, `git diff --check` passed, and `smoke-r2/artifacts/`
  remains absent. This is test-only hardening; smoke-r2 remains terminally a
  no-result and the accepted NLL policy remains frozen. No provider, network,
  remote resource, corpus download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-13 12:49Z entry).

- [x] **Cross-condition infinity NLL regression (2026-08-13 08:37Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  sparse non-finite regression to prove that `NaN`, positive infinity, and
  negative infinity each fail closed independently for every Stage-A
  aggregate (`window`, `matched`, `random`, and `full`). Nine focused Stage-A
  tests passed 9/9, the full local suite passed 25/25, `git diff --check`
  passed, and `smoke-r2/artifacts/` remains absent. This is test-only
  hardening; smoke-r2 remains terminally a no-result and the accepted NLL
  policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-13 08:37Z
  entry).

- [x] **Post-hardening closure verification (2026-08-13 04:29Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the retained full local
  suite passed 25/25, `git diff --check` passed, and the explicit filesystem
  gate confirmed `smoke-r2/artifacts/` remains absent. This verifies the
  accumulated test-only hardening without changing runtime code or the
  accepted support-aware policy; smoke-r2 remains terminally a no-result. No
  provider, network, remote resource, corpus download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-13 04:29Z entry).

- [x] **Cross-condition sparse non-finite NLL regression (2026-08-13 00:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, added a focused regression
  proving that a non-finite NLL in a one-span stratum fails closed independently
  for every Stage-A aggregate (`window`, `matched`, `random`, and `full`). Nine
  focused Stage-A tests passed 9/9, the full local suite passed 25/25, `git
  diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the accepted
  NLL policy remains frozen. No provider, network, remote resource, corpus
  download, or paid action occurred. Evidence: `NOTES.md` (2026-08-13 00:24Z
  entry).

- [x] **Cross-condition supported NLL-band regression (2026-08-12 20:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, added a focused regression
  proving that the frozen ordinary `1.5--6.0` band at four spans applies
  independently to every Stage-A aggregate (`window`, `matched`, `random`,
  and `full`). Seven focused policy tests passed 7/7, the full local suite
  passed 24/24, `git diff --check` passed, and `smoke-r2/artifacts/` remains
  absent. This is test-only hardening; smoke-r2 remains terminally a no-result
  and the accepted NLL policy remains frozen. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-12 20:24Z entry).

- [x] **Cross-condition sparse-NLL stop regression (2026-08-12 16:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, added a focused regression
  proving that the frozen unconditional `<0.5` and `>8` sparse-stratum stops
  apply independently to every Stage-A aggregate (`window`, `matched`,
  `random`, and `full`), not only `window`. Six focused policy tests passed
  6/6, the full local suite passed 23/23, `git diff --check` passed, and
  `smoke-r2/artifacts/` remains absent. This is test-only hardening;
  smoke-r2 remains terminally a no-result and the accepted NLL policy remains
  frozen. No provider, network, remote resource, corpus download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-12 16:24Z entry).

- [x] **Adjacent NLL-support boundary regression (2026-08-12 12:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, added a focused regression
  for the exact support transition omitted by the retained suite: an
  ordinary-band NLL of `1.20` is reported support-insufficient and allowed at
  three spans, then fails closed when only `n_spans` changes to four. The five
  focused policy tests passed 5/5, the full local suite passed 22/22, `git
  diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the
  accepted NLL policy remains frozen. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-12
  12:24Z entry).

- [x] **Unconditional sparse-NLL endpoint regression (2026-08-12 08:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  support-aware policy tests to prove that exact sparse-stratum NLL endpoints
  `0.50` and `8.00` do not trigger the frozen unconditional `<0.5` / `>8`
  stops, while the adjacent `0.49` and `8.01` values still fail closed. The
  four focused policy tests passed 4/4, the full local suite passed 21/21,
  `git diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the
  accepted NLL policy remains frozen. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-12
  08:24Z entry).

- [x] **Inclusive NLL-band endpoint regression (2026-08-12 04:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  minimum-support policy test to prove that exact NLL endpoints `1.50` and
  `6.00` pass the inclusive ordinary band at exactly four spans, complementing
  the existing `1.49` and `6.01` failures. The four focused policy tests
  passed 4/4, the full local suite passed 21/21, `git diff --check` passed,
  and `smoke-r2/artifacts/` remains absent. This is test-only hardening;
  smoke-r2 remains terminally a no-result and the accepted NLL policy remains
  frozen. No provider, network, remote resource, corpus download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-12 04:24Z entry).

- [x] **Maximum-support NLL-band boundary regression (2026-08-12 00:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the retained
  minimum-support test to prove that NLL `6.01` fails the ordinary band at
  exactly four spans, symmetrically with the existing `1.49` check. The four
  focused policy tests passed 4/4, the full local suite passed 21/21, `git
  diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the
  accepted NLL policy remains frozen. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-12
  00:24Z entry).

- [x] **Minimum-support NLL-band boundary regression (2026-08-11 20:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, extended the focused
  smoke-policy test to prove that an NLL of `1.49` fails the ordinary band at
  exactly four spans, while the existing one-span `1.2` case remains
  support-insufficient and allowed absent an unconditional stop. The four
  focused policy tests passed 4/4, the full local suite passed 21/21, `git
  diff --check` passed, and `smoke-r2/artifacts/` remains absent. This is
  test-only hardening; smoke-r2 remains terminally a no-result and the
  accepted NLL policy remains frozen. No provider, network, remote resource,
  corpus download, or paid action occurred. Evidence: `NOTES.md` (2026-08-11
  20:24Z entry).

- [x] **Post-hardening closure verification (2026-08-11 16:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the full local suite passed
  21/21 in 2.53 s with the retained sparse `>8` NLL regression present.
  `git diff --check` passed, and the explicit filesystem gate confirmed
  `smoke-r2/artifacts/` remains absent. This verifies the test-only hardening
  without changing the accepted support-aware policy or runtime code;
  smoke-r2 remains terminally a no-result. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-11 16:24Z entry).

- [x] **Sparse high-NLL fail-closed regression (2026-08-11 12:24Z, local only).**
  Added the previously absent focused test for the frozen unconditional `>8`
  broken-conditioning stop in a one-span stratum. The four focused policy
  tests passed 4/4 in 1.94 s, the full local suite passed 21/21 in 2.41 s,
  and `git diff --check` passed. This test-only change preserves the accepted
  support-aware amendment and closes its complementary sparse-NLL boundary;
  smoke-r2 remains terminally a no-result. No provider, network, remote
  resource, corpus download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-11 12:24Z entry).

- [x] **Targeted NLL-policy closure regression (2026-08-11 08:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the three focused Stage-A
  policy tests passed 3/3 in 2.23 s: supported-stratum banding retains the
  unconditional `<0.5` stop, non-finite sparse NLL fails closed, and missing
  aggregate NLL fails closed. `git diff --check` passed, the pre-test worktree
  was clean, and `smoke-r2/artifacts/` remains absent. Smoke-r2 therefore
  remains terminally a no-result and the accepted NLL policy remains frozen.
  No provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-11 08:24Z entry).

- [x] **Continuation closure regression (2026-08-11 04:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 2.29 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-11 04:24Z entry).

- [x] **Continuation closure regression (2026-08-11 00:24Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 2.70 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-11 00:24Z entry).

- [x] **Continuation closure regression (2026-08-10 20:22Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 2.95 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 20:22Z entry).

- [x] **Continuation closure regression (2026-08-10 16:22Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 2.26 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 16:22Z entry).

- [x] **Continuation closure regression (2026-08-10 12:21Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.74 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 12:21Z entry).

- [x] **Continuation closure regression (2026-08-10 08:21Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.84 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 08:21Z entry).

- [x] **Continuation closure regression (2026-08-10 04:21Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.73 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 04:21Z entry).

- [x] **Continuation closure regression (2026-08-10 00:21Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.80 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-10 00:21Z entry).

- [x] **Continuation closure regression (2026-08-09 20:18Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.73 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 20:18Z entry).

- [x] **Continuation closure regression (2026-08-09 16:17Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.80 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 16:17Z entry).

- [x] **Continuation closure regression (2026-08-09 12:17Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.59 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 12:17Z entry).

- [x] **Continuation closure regression (2026-08-09 08:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.62 s. `git diff --check` passed, the pre-test
  worktree `git status --short` was empty, and the explicit filesystem gate
  confirms `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 08:15Z entry).

- [x] **Continuation closure regression (2026-08-09 04:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.90 s. `git diff --check` passed, the pre-test
  `git status --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 04:15Z entry).

- [x] **Continuation closure regression (2026-08-09 00:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.03 s. `git diff --check` passed, the pre-test
  `git status --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-09 00:15Z entry).

- [x] **Continuation closure regression (2026-08-08 20:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.71 s. `git diff --check` passed, the pre-test
  `git status --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-08 20:15Z entry).

- [x] **Continuation closure regression (2026-08-08 16:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.99 s. `git diff --check` passed, the pre-test
  `git status --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-08 16:15Z entry).

- [x] **Continuation closure regression (2026-08-08 12:15Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.90 s. `git diff --check` passed, the pre-test
  `git status --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-08 12:15Z entry).

- [x] **Continuation closure regression (2026-08-08 08:14Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.94 s. `git diff --check` passed, `git status
  --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. `REMOTE_JOB.md` continues to record
  both pods deleted before execution with no artifacts. Smoke-r2 remains
  terminally a no-result and the hardened support-aware NLL policy remains
  frozen. No provider, network, remote-resource, corpus-download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-08 08:14Z entry).

- [x] **Continuation closure regression (2026-08-08 04:14Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.93 s. `git diff --check` passed, `git status
  --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-08 04:14Z entry).

- [x] **Continuation closure regression (2026-08-08 00:14Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.80 s. `git diff --check` passed, `git status
  --short` was empty, and the explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-08 00:14Z entry).

- [x] **Continuation closure regression (2026-08-07 20:14Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.95 s. `git diff --check` passed and `git
  status --short` was empty. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent. Smoke-r2 remains terminally a
  no-result and the hardened support-aware NLL policy remains frozen. No
  provider, network, remote-resource, corpus-download, or paid action
  occurred. Evidence: `NOTES.md` (2026-08-07 20:14Z entry).

- [x] **Continuation closure regression (2026-08-07 16:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.78 s. `git status --short` and `git diff
  --check` were clean. The filesystem gate confirms `smoke-r2/artifacts/`
  remains absent; `REMOTE_JOB.md` line 4 records both provisioned pods deleted
  before execution with no artifacts. Smoke-r2 remains terminally a no-result
  and the hardened support-aware NLL policy remains frozen. No provider,
  network, remote-resource, corpus-download, or paid action occurred.
  Evidence: `NOTES.md` (2026-08-07 16:13Z entry).

- [x] **Continuation closure regression (2026-08-07 12:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.92 s. `git status --short` was empty and
  `git diff --check` passed. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent; `REMOTE_JOB.md` records both pods
  deleted before execution, no Stage 0/S/A command, and no artifacts.
  Smoke-r2 remains terminally a no-result and the hardened support-aware NLL
  policy remains frozen. No provider, network, remote-resource,
  corpus-download, or paid action occurred. Evidence: `NOTES.md`
  (2026-08-07 12:13Z entry).

- [x] **Continuation closure regression (2026-08-07 08:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.98 s. `git status --short` was empty and
  `git diff --check` passed. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent, while `REMOTE_JOB.md` line 4 records
  both provisioned pods deleted before execution with no artifacts. Smoke-r2
  remains a terminal no-result and the hardened support-aware NLL policy
  remains frozen. No provider, network, remote-resource, corpus-download, or
  paid action occurred. Evidence: `NOTES.md` (2026-08-07 08:13Z entry).

- [x] **Continuation closure regression (2026-08-07 04:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.76 s. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent, and its `REMOTE_JOB.md` records both
  provisioned pods deleted before execution with no artifacts. Before this
  documentation update, `git status --short` was empty and `git diff --check`
  passed. Smoke-r2 remains a terminal no-result and the hardened
  support-aware NLL policy remains frozen. No provider, network,
  remote-resource, corpus-download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-07 04:13Z entry).

- [x] **Continuation closure regression (2026-08-07 00:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 1.10 s; `git status --short` was empty and `git
  diff --check` passed. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent, while `REMOTE_JOB.md` line 4 records
  both pods deleted before execution and no artifacts. Smoke-r2 remains a
  terminal no-result and the hardened support-aware NLL policy remains
  frozen. No provider, network, remote-resource, corpus-download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-07 00:13Z entry).

- [x] **Continuation closure regression (2026-08-06 20:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.92 s; `git status --short` was empty and `git
  diff --check` passed. The filesystem gate confirms `smoke-r2/artifacts/`
  remains absent, while `REMOTE_JOB.md` line 4 records both pods deleted before
  execution and no artifacts. Smoke-r2 remains terminally a no-result and the
  hardened support-aware NLL policy remains frozen. No provider, network,
  remote-resource, corpus-download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-06 20:13Z entry).

- [x] **Continuation closure regression (2026-08-06 16:11Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.82 s; `git status --short` was empty and `git
  diff --check` passed. The filesystem gate confirms `smoke-r2/artifacts/`
  remains absent, while `REMOTE_JOB.md` records both pods deleted before
  transfer, dependency installation, or Stage 0/S/A. Smoke-r2 remains
  terminally a no-result and the hardened support-aware NLL policy remains
  frozen. No provider, network, remote-resource, corpus-download, or paid
  action occurred. Evidence: `NOTES.md` (2026-08-06 16:11Z entry).

- [x] **Continuation closure regression (2026-08-06 12:11Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.86 s; `git status --short` was empty and
  `git diff --check` passed. The policy tests explicitly cover supported
  strata, non-finite sparse NLL, and missing aggregate NLL conditions. The
  filesystem gate confirms `smoke-r2/artifacts/` remains absent, and
  `REMOTE_JOB.md` records both pods deleted before transfer, dependency
  installation, or Stage 0/S/A. Smoke-r2 remains terminally a no-result and
  the hardened support-aware NLL policy remains frozen. No provider, network,
  remote-resource, corpus-download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-06 12:11Z entry).

- [x] **Continuation closure regression (2026-08-06 08:11Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.85 s; `git status --short` was empty and `git
  diff --check` passed. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent, while `REMOTE_JOB.md` records both pods
  deleted before execution, no Stage 0/S/A command, and no GPU work. Smoke-r2
  remains terminally a no-result and the hardened support-aware NLL policy
  remains frozen. No provider, network, remote-resource, corpus-download, or
  paid action occurred. Evidence: `NOTES.md` (2026-08-06 08:11Z entry).

- [x] **Continuation closure regression (2026-08-06 04:11Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q` passed 20/20 in 0.85 s; `git status --short` was empty and
  `git diff --check` passed. The explicit filesystem gate confirms
  `smoke-r2/artifacts/` remains absent, while `REMOTE_JOB.md` records both
  pods deleted before any transfer, dependency installation, or Stage 0/S/A
  command. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy remains frozen. No provider, network,
  remote-resource, corpus-download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-06 04:11Z entry).

- [x] **Continuation closure regression (2026-08-06 00:11Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q test_hdc_musicgen_structural.py` passed 13/13 in 0.84 s; `git
  status --short` was empty and `git diff --check` passed. The explicit
  filesystem gate confirms `smoke-r2/artifacts/` is absent, while
  `REMOTE_JOB.md` records both pods deleted before execution and no Stage
  0/S/A command started. Smoke-r2 remains terminally a no-result and the
  hardened support-aware NLL policy remains frozen. No provider, network,
  remote-resource, corpus-download, or paid action occurred. Evidence:
  `NOTES.md` (2026-08-06 00:11Z entry).

- [x] **Continuation closure regression (2026-08-05 20:07Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q test_hdc_musicgen_structural.py` passed 13/13 in 0.95 s; `git
  status --short` was empty and `git diff --check` passed. The explicit
  filesystem gate again confirms `smoke-r2/artifacts/` is absent. Smoke-r2
  remains terminally a no-result and the hardened support-aware NLL policy
  remains frozen. No provider, network, remote-resource, corpus-download, or
  paid action occurred. Evidence: `NOTES.md` (2026-08-05 20:07Z entry).

- [x] **Continuation closure regression (2026-08-05 16:00Z, local only).**
  At prospective direct-recurrence pin `74287d9`, `PYTHONPATH=. python3 -m
  pytest -q test_hdc_musicgen_structural.py` passed 13/13 in 1.04 s; `git
  status --short` and `git diff --check` were clean. `smoke-r2/artifacts/`
  remains absent, and `REMOTE_JOB.md` records both pods deleted before
  execution, with no Stage 0/S/A command started. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy stays frozen. No
  provider, network, remote-resource, or corpus-download action occurred.
  Evidence: `NOTES.md` (2026-08-05 16:00Z entry).

- [x] **Continuation closure regression (2026-08-05 11:58Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.84 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods deleted before execution, with no Stage 0/S/A command
  started. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-05 11:58Z entry).

- [x] **Continuation closure regression (2026-08-05 08:59Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.87 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods deleted before execution, with no Stage 0/S/A command
  started. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-05 08:59Z entry).

- [x] **Continuation closure regression (2026-08-05 04:45Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 1.76 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods as deleted before transfer, dependency installation, or
  Stage 0/S/A. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-05 04:45Z entry).

- [x] **Continuation closure regression (2026-08-05 00:13Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 1.83 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods as deleted before execution. Smoke-r2 remains terminally
  a no-result and the hardened support-aware NLL policy stays frozen. No
  provider, network, remote-resource, or corpus-download action occurred.
  Evidence: `NOTES.md` (2026-08-05 00:13Z entry).

- [x] **Continuation closure regression (2026-08-04 20:09Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 1.62 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, while `REMOTE_JOB.md`
  records both pods deleted before transfer, dependency installation, or
  Stage 0/S/A. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-04 20:09Z entry).

- [x] **Continuation closure regression (2026-08-04 16:06Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.76 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods deleted before transfer, dependency installation, or
  Stage 0/S/A. Smoke-r2 remains terminally a no-result and the hardened
  support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-04 16:06Z entry).

- [x] **Continuation closure regression (2026-08-04 12:06Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.82 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/artifacts/` remains absent, and `REMOTE_JOB.md`
  records both pods deleted before transfer, dependency installation, or
  Stage 0/S/A. Smoke-r2 is terminally a no-result and the hardened
  support-aware NLL policy remains frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-04 12:06Z entry).

- [x] **Continuation closure regression (2026-08-04 08:06Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.76 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/REMOTE_JOB.md` again records both pods deleted before
  transfer, dependency installation, or Stage 0/S/A, and
  `smoke-r2/artifacts/` remains absent. Smoke-r2 is terminally a no-result and
  the hardened support-aware NLL policy remains frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-04 08:06Z entry).

- [x] **Continuation closure regression (2026-08-04 04:06Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.83 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/REMOTE_JOB.md` records both pods deleted before
  transfer, dependency installation, or Stage 0/S/A, and
  `smoke-r2/artifacts/` remains absent. Smoke-r2 is terminally a no-result;
  the hardened support-aware NLL policy stays frozen. No provider, network,
  remote-resource, or corpus-download action occurred. Evidence: `NOTES.md`
  (2026-08-04 04:06Z entry).

- [x] **Continuation closure regression (2026-08-04 00:06Z, local only).**
  At prospective direct-recurrence pin `74287d9`, the focused structural
  suite passed 13/13 in 0.81 s; `git status --short` and `git diff --check`
  were clean. `smoke-r2/REMOTE_JOB.md` confirms both pods were deleted before
  transfer, dependency installation, or Stage 0/S/A, and
  `smoke-r2/artifacts/` remains absent. The smoke-r2 handoff is terminally a
  no-result and the hardened support-aware NLL policy remains frozen; no
  provider, network, remote-resource, or corpus-download action occurred.
  Evidence: `NOTES.md` (2026-08-04 entry).

- [ ] **Ben 2026-08-03: approved reliable direct-recurrence run.** Deliverable:
  execute the frozen MusicGen direct-recurrence protocol sequentially on a
  Secure high-stock A40 within 15 hours / USD 6.60, with atomic stage artifacts
  evacuated locally and hash-verified at every checkpoint. Acceptance:
  SSH-stability, bootstrap, source/input, and provider-free return tests pass;
  scientific stages either meet frozen gates or stop fail-closed; artifacts are
  retrieved and the pod is terminated. Next command: freeze and test the
  checkpoint-evacuation bundle. Evidence: new 20260803 reliable-run experiment
  directory.

- [ ] **Ben 2026-08-02: prepare and launch a reliable MusicGen GPU run.**
  Deliverable: immutable direct-recurrence-gate bundle with locally exercised
  bootstrap, transport, heartbeat, artifact-return/hash verification, and
  externally enforced termination; then one explicitly approved priced GPU
  run. Acceptance: all provider-free launch/return failure injections pass,
  current offer/cost envelope is approved, scientific stages execute or fail
  closed, artifacts return and verify, and the resource is confirmed absent.
  Next command: reconcile the `74287d9` gate worktree with the latest frozen
  source and build the no-science round-trip preflight. Evidence: a new
  reliability-preflight experiment and subsequent REMOTE_JOB record.

- [x] Diagnose whether the full-corpus r5 Stage-0 persistence failure is a
  valid corpus-recurrence gate. A deterministic provider-free calibration
  triplicated all encoded tracks, creating exact long-range recurrence while
  changing adjacent-token persistence by at most `6.56e-06`. Thus the metric
  cannot diagnose recurrence or select a corpus. It does not establish why the
  residual codebooks are below 0.05, nor justify waiving that threshold.
  Evidence: `experiments/20260731T004101Z-persistence-proxy-calibration/`.
- [x] Design and validate the prospective direct recurrence gate. Commit
  `74287d9` makes Stage 0 a coverage/codec-integrity gate and Stage S the
  cross-window chroma recurrence gate; exact-repeat/nonrepeat controls and the
  complete local suite passed 20/20. Evidence:
  `experiments/20260731T004951Z-direct-recurrence-gate-validation/`.
- [x] **Repair r4 launch-path defect (2026-07-30):** retrieved the published
  v0.2.0 asset after its SHA-256 check, made a provenance-preserving derivative
  that requires `HDC_MUSICGEN_ROOT` rather than hard-coding r3, and archived it
  as `musicgen-full-corpus-v2-r4-pathfix.tar.gz` (SHA-256
  `0eafde1a0182cc7348c810417631b00f8f86e347ade3aca84382319ad748a485`).
  Shell syntax and temporary root/output launch-path checks pass. A fresh paid
  approval is still required because this is a changed bundle; evidence:
  `experiments/20260730T175100Z-full-corpus-r4/repaired-source/`.
  Latest local evidence (2026-07-30): the r4 `launcher.log` proves the stale
  r3 `cd` is inside the released asset, while the r4 command passes its r4
  root correctly. Pin `41022d5` and the local workspace contain no
  `run_full_corpus.sh`, so the checked-out source cannot produce a repaired
  bundle or checksum. The fail-closed approval request for public-asset
  retrieval (or local provision of the exact asset) is recorded in `NOTES.md`;
  no network/provider/data action was taken.

- [x] **Full-corpus r4 fail-closed launch (2026-07-30):** Secure L40S pod
  `0hrzjkacaswlb6`, EU-NL-1, was provisioned under Ben's USD 15 cap (USD
  0.99/hour; 15-hour automatic termination requested). SSH, source/import,
  input hash, and 11/11 focused gates passed. The stage launcher failed before
  Stage 0 on the hard-coded r3 path. Logs/inputs were retrieved and hash
  verified; deletion returned true, direct lookup 404, and inventory `[]`.
  No scientific stage or result was produced. Evidence:
  `experiments/20260730T175100Z-full-corpus-r4/`.

- [ ] **SSH-free transport probe (approved 2026-07-30):** Ben approved one
  Secure L40S (48 GiB) no-science probe, 30 minutes / USD 0.50 maximum.  It
  may download only the public immutable source bundle and return a tiny
  synthetic artifact; no MusicGen stage or audio input may run.  Local
  preflight passed 18/18 tests on 2026-07-30.  Do not provision until the
  pod-side startup/receiver harness is executable and the Croc return
  procedure is locally observed; terminate immediately on startup, source
  hash, or return-hash failure.  Evidence: Telegram approval 15018 and
  `docs/ssh-free-runpod-bootstrap-v1.md`.  Latest local static audit
  (2026-07-30): the r3 bootstrap passes `bash -n`, and `runpodctl` exposes
  `send <file> --code` / `receive <code>`, but no tracked probe harness
  packages a synthetic artifact, supplies a rendezvous code, invokes either
  command, or verifies a returned hash.  The transport gate therefore remains
  fail-closed; no provider or network command was run.  See `NOTES.md`.

- [ ] Reattempt the repaired full-corpus bundle only after fresh paid-run
  approval and a transport/reachability gate. The approved r3 pod
  `z7vwtijqtxhidc` remained SSH-unready across five observations and was
  deleted fail-closed on 2026-07-30 before any transfer, bootstrap, test, or
  scientific stage; it produced no artifacts. Public release `v0.2.0` remains
  available, but the terminated authorization does not cover another pod.
  Original deliverable required two
  fresh approvals: public release publication and a paid RunPod envelope.
  Deliverable: public source-only release `v0.2.0` on
  `bgoertzel-sing/runpod-ssh-free-bootstrap`, then one Secure RTX 4090 run
  using direct SSH. Acceptance: release asset/checksum is anonymously
  retrievable; bootstrap preflight reports `AUDIOCRAFT_IMPORT_OK`; the 24
  inputs verify; all stage artifacts return and hash-verify; pod is terminated
  on completion/failure/bound. Frozen local release commit: `5dc5d7f`; source
  asset SHA-256:
  `e0b544f9d5b2b189103832bd7edf6427d971ff45ca6a46eae70d1663646aebee`.
  Next action: establish a reachable transport path, then request a fresh
  exact provider/resource/price/time/cost authorization. Evidence:
  `experiments/20260730T072300Z-full-corpus-r3/`.

- [x] Repair and locally validate the failed full-corpus r2 bootstrap before
  proposing any paid retry. Deliverable: a complete pinned AudioCraft import
  dependency set and a wrapper that reports the actual pipeline exit status.
  Acceptance: a fresh isolated environment imports the same AudioCraft path
  used by Stage 0; dependency consistency check passes; focused tests pass;
  injected success/failure commands yield `PIPELINE_EXIT:0` and a nonzero
  `PIPELINE_EXIT` respectively; evidence and exact commands are preserved in
  a new experiment record. Next command: inspect the r2 launch wrapper and
  construct the smallest local clean-environment reproduction. Evidence:
  `experiments/20260730T001926Z-full-corpus-r2-bootstrap-repair/`. Completed:
  explicit `click` plus exact Stage-0 import gate; fail-closed compatibility
  audit passed; focused tests 11/11; status fixtures preserved exit 0 and
  injected exit 23; syntax/compile/diff checks passed. No provider contacted.

- [ ] Validate an SSH-free RunPod bootstrap transport before another MusicGen
  GPU attempt. Deliverable: a source/artifact transport design, a harmless
  no-science startup/return probe, and an immutable-bundle verification path
  that does not put credentials on the pod. Acceptance: bootstrap source and
  returned tiny artifact hashes verify without SSH; startup command semantics
  are observed rather than assumed; a fresh paid scientific run is requested
  only after these transport gates pass. Next action: Ben selects public
  GitHub publication, an existing private artifact location, or manual web
  terminal/Croc fallback. Evidence:
  `docs/ssh-free-runpod-bootstrap-v1.md`.

- [x] **Direct-SSH transport alternative validated (2026-07-30):** the
  approved Secure L40S probe `435eptadaqn406` exposed direct SSH; a remote
  fixed synthetic artifact returned through rsync and passed local SHA-256
  verification.  The pod was deleted and immediate lookup returned 404.
  This clears the reachable transport prerequisite for the full-corpus run;
  it does not itself authorize that larger scientific job.  Evidence:
  `experiments/20260730T170552Z-l40s-ssh-transport-probe/`.

- [x] Freeze a restart-safe full-corpus 0/S/A/C/D MusicGen runbook. Completed
  at source commit `cb126876`: Stage 0, A, and D emit deterministic recovery
  artifacts at bounded intervals; focused structural tests pass 10/10.
  Evidence: `experiments/20260728T210000Z-full-corpus-r1/`.
- [ ] Execute the full 24-track explicit-CC corpus run only after a fresh
  RunPod resource/price/cost/time approval. Acceptance: Stage 0 gate is
  evaluated on >=20 tracks and >=60 encoded minutes; later stages obey their
  fail-closed gates; partial artifacts are synced every 10 minutes; returned
  artifacts/hashes are verified and pod is terminated. Next command: query
  current RunPod RTX 4090 availability and price after approval. Evidence:
  `experiments/20260728T210000Z-full-corpus-r1/`.
  Latest evidence (2026-07-29): approved r2 pod `fxm155vje2ye5p` reached the
  frozen 11/11 focused-test pass but failed closed before Stage 0 when
  AudioCraft/spaCy imported the omitted `click` dependency. No checkpoint or
  JSON gate output was produced. The two logs were retrieved and SHA-256
  verified; the pod was deleted and provider inventory returned `[]`.
  Reproduce the full import locally/remotely without paid science and repair
  true exit-status propagation before requesting another run. Evidence:
  `experiments/20260729T235932Z-full-corpus-r2/`.
  Local repair completed in
  `experiments/20260730T001926Z-full-corpus-r2-bootstrap-repair/`; next action
  is freeze a new immutable bundle and obtain a fresh exact paid-run approval.

- [x] **Closed — do not re-provision smoke-r2:** the first provisioned pod
  received code/audio and began dependency setup, while the replacement did
  not; neither pod started Stage 0/S/A, both were deleted, and the run has no
  stage artifacts. This is a terminal no-result rather than a pending handoff.
  Any future MusicGen run is a new activity requiring fresh explicit
  provider/resource/price/cost/time/data/stop authorization. The prior RTX
  3090 pod `vbu5r47gstyl16` was
  terminated on 2026-07-28 after SSH refused twice, before any stage command
  began; provider list was empty and lookup was 404. Acceptance: only eight
  existing explicit-CC tracks run through Stages 0/S/A; retrieve and verify
  artifacts, then terminate the pod. Next command: `runpodctl gpu list`.
  Evidence:
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`.
- [x] Persistent local-only continuation worker: inspect and validate the
  smoke-r2 handoff, reproduce or analyze locally where possible, and prepare a
  bounded decision note. It must not create, resume, or retain paid remote
  compute without a new explicit approval. Acceptance: each tick records an
  evidence-backed next action or a precise approval request in the project
  record. Scheduler lane: `HDC MusicGen continuation worker`. Latest evidence
  (2026-08-03 20:05Z): at direct-recurrence pin `74287d9`, the focused
  structural suite passed 13/13 in 0.83 s; `git status --short` and `git diff
  --check` were clean. `smoke-r2/REMOTE_JOB.md` confirms both pods were
  deleted before transfer, dependency installation, or Stage 0/S/A, and an
  explicit filesystem check confirms no `artifacts/` directory. Smoke-r2
  remains terminally no-result and the hardened NLL policy remains frozen; no
  provider, network, remote-resource, or data-download action occurred.
  Latest evidence (2026-08-03): at `74287d9`, the focused pure-logic suite passed 13/13 in
  0.93 s and status/diff checks were clean. `smoke-r2/REMOTE_JOB.md` records
  both pods deleted before transfer or Stage 0/S/A, while the run directory
  has no artifacts. Smoke-r2 remains terminally no-result and the hardened
  NLL policy remains frozen; no provider/network/data action occurred. See
  `NOTES.md`.
  Latest evidence (2026-08-03): `REMOTE_JOB.md` again identifies both pods as
  deleted before execution and `smoke-r2/artifacts/` remains absent. At
  prospective pin `74287d9`, `test_hdc_musicgen_structural.py` passed 13/13 in
  0.81 s; `git diff --check` and status were clean. This closure regression
  preserves the fail-closed frozen NLL policy and authorizes no remote action.
  Earlier evidence
  (2026-07-27): local JSON audit reconfirmed the NLL failure is confined to one
  UNRELATED span (all four values 1.23326–1.26837; n=1), while RELATED (n=12)
  is in-band and passes relevance. The frozen runbook has no small-stratum
  exception; gate remains fail-closed. Latest evidence (2026-07-27): a local
  replay of the frozen `stageA_gate()` exactly reproduced `gate_pass=true` but
  `nll_sanity_pass=false`; focused pure-logic tests passed 7/7. The runbook's
  “roughly” wording cannot override the executable's strict all-aggregate
  band without an owner amendment. Latest evidence (2026-07-27): the approved
  low-support amendment at `7afd4c4` lets a non-finite sparse-stratum NLL
  evade its numeric stops; a local uncommitted fail-closed repair and
  regression pass 9/9. The remote source pin must be updated/accepted before
  smoke-r2 can launch. Latest evidence (2026-07-27): local replay of the
  accepted `8907d0f` gate against the retrieved smoke-r1 summary passed the
  9/9 focused suite and yields a passing NLL sanity result only because
  RELATED (n=12) is checked and UNRELATED (n=1) is explicitly reported
  support-insufficient; both non-finite and `<0.5` stops remain false. No
  remote resource was contacted by this worker. Latest evidence (2026-07-27):
  local source/manifest audit identifies the deterministic MP3-only `--limit
  8` selection and its selection-record SHA-256
  `60183005efa4dd7b8864bdbf7c24dae7667e563f20fb6d78f5e1c293a86e27e3`;
  focused gate tests pass 9/9. Retrieved Stage-0 evidence must verify these
  inputs before smoke-r2 can be accepted. See `NOTES.md` for the bounded
  handoff. Latest evidence (2026-07-28): documentation reconciliation confirms
  `vbu5r47gstyl16` was deleted after two SSH refusals, with empty-list/404
  cleanup evidence and no stage artifacts; pinned-source focused tests pass
  9/9 locally and `git diff --check` is clean. This worker did not contact a
  provider or alter the pre-existing unrelated worktree modification. Latest
  evidence (2026-07-28): the same remote handoff also records a later pod
  `2jh6oxjzogdexe` as provisioned but lacks a terminal status, while the
  project RUN describes only the deleted earlier pod. Local pin `8907d0f`
  focused tests again passed 9/9 and `git diff --check` was clean. Treat the
  replacement's status as unverified and block all remote action pending a
  fresh explicit status/cleanup authorization; see `NOTES.md`.
  Latest evidence (2026-07-28): the pinned gate suite passed 9/9 locally,
  `git diff --check` was clean, and the smoke-r2 run directory contains no
  retrieved artifacts. This reconfirms that `2jh6oxjzogdexe` has no local
  execution or retrieval evidence; do not contact it without the precise
  status-and-cleanup authorization in `NOTES.md`.
  Latest evidence (2026-07-28): Ben supplied that authorization; account
  metadata showed `2jh6oxjzogdexe` RUNNING at USD 0.50/hour immediately before
  `runpodctl pod delete` returned `deleted: true`, and a subsequent all-pods
  list omitted it. No remote execution/artifact evidence exists. The old
  status/cleanup blocker is resolved; a fresh MusicGen launch still requires
  its separately recorded availability/cost/reachability check.
  Latest evidence (2026-07-28): local terminal-state reconciliation against
  `REMOTE_JOB.md` confirms both smoke-r2 pods were deleted before any Stage
  0/S/A command: `vbu5r47gstyl16` after SSH refusal and `2jh6oxjzogdexe` after
  unusable provider routing. At pin `8907d0f`, focused fail-closed tests pass
  9/9 in 0.75 s, `git diff --check` is clean, and this run has no retrieved
  `artifacts/` directory. No provider was contacted. A future launch needs a
  new explicit authorization naming RunPod (or another provider), exact GPU,
  current price and hard cost/time cap, the existing eight explicit-CC tracks
  only, and immediate gate-failure/retrieval/termination stops.
  Latest evidence (2026-07-28): static local audit of the later smoke-r3
  handoff found `remote_run.sh` redirects to
  `/workspace/hdc-musicgen-r3-results/environment.txt` before creating that
  directory (and has no `mkdir -p`); with `set -euo pipefail`, this is a
  pre-Stage-0 failure unless setup already created it. Gate tests at pin
  `8907d0f` pass 9/9 (0.88 s), but no local smoke-r3 artifacts exist. Treat
  r3 results as unverified; require logs, `environment.txt`, Stage-0/S/A JSON,
  selected-input hashes, and checksums before acceptance. No provider contact
  or remote change occurred in this worker.
  Latest evidence (2026-07-28): a local boundary audit at full-run pin
  `cb126876` showed that a supported stratum with all four aggregate NLL
  fields absent could pass via Python `all([])`. Commit `41022d5` now fails
  closed with an explicit missing-condition stop and regression; focused tests
  pass 11/11. This local hardening is not retroactive to any already-launched
  pin; accept future artifacts only when all four aggregate NLL values are
  present, finite, and subject to the frozen support-aware policy. No provider
  was contacted or altered.
  Latest evidence (2026-07-28): at local HEAD `41022d5`, the focused
  structural suite again passed 11/11 in 0.76 s, including the missing-
  aggregate regression. `git status --short` reports only the pre-existing
  unrelated `hdc_musicgen_experiments.py` modification, which this worker did
  not alter. No provider or network action occurred; future paid execution
  still needs fresh explicit provider/resource/price/cost/time/data/stop
  authorization. Latest evidence (2026-07-29): local-only checksum
  reconciliation of smoke-r3 matched 7/7 returned result files and 8/8
  retained existing-input MP3s against `artifacts/remote-sync/SHA256SUMS`;
  `exit_status` is 0. Stage S passed (separation 0.492106) and the accepted
  support-aware Stage-A gate passed (RELATED gain 0.054186, n=48; UNRELATED
  n=1 support-insufficient; no non-finite or `<0.5` stop). The stale r3 RUN
  status is corrected; Stage 0 remains smoke-only and Stage C/D were not run.
  No provider, network, remote-resource, or data-download action occurred.
  Latest evidence (2026-07-29): smoke-r3's returned Stage-A summary was
  checked against the later aggregate-completeness hardening: both RELATED
  and UNRELATED contain all four finite `window/matched/random/full` NLL
  aggregates (2 strata × 4 fields). At local pin `41022d5`, the focused suite
  passed 11/11 in 0.76 s and `git diff --check` was clean. This confirms the
  verified r3 acceptance does not depend on the older pin's `all([])` gap; it
  does not expand its smoke-only support or authorize a future run. Latest
  evidence (2026-07-29): terminal-state reconciliation reconfirmed both
  smoke-r2 pods were deleted before any transfer or Stage 0/S/A execution;
  its `artifacts/` directory is absent and the stale remote-job header was
  corrected. At HEAD `41022d5`, focused fail-closed tests passed 11/11 in
  0.94 s and `git diff --check` passed. The smoke-r2 handoff is closed as a
  no-result; no provider/network/remote-resource/data-download action
  occurred, and any paid relaunch still requires fresh explicit approval.
  Latest evidence (2026-07-29): a local replay of HEAD `41022d5` against the
  verified smoke-r3 Stage-A summary returned `gate_pass=true` and
  `nll_sanity_pass=true`, with RELATED alone band-checked and UNRELATED
  explicitly support-insufficient; all eight aggregate fields were present
  and numeric, and non-finite/missing-aggregate/alignment stops were false.
  Focused tests passed 11/11 in 0.77 s and `git diff --check` passed. This
  validates the accepted hardened policy only; it does not authorize remote
  action or expand the smoke result.
  Latest evidence (2026-07-29): independent local replay at `41022d5` of the
  verified r3 `stageA_summary.json` returned `gate_pass=true` and
  `nll_sanity_pass=true`; only RELATED was band-checked, UNRELATED was
  support-insufficient, and non-finite/missing-aggregate/alignment stops were
  all false. The focused suite passed 11/11 in 0.82 s and `git diff --check`
  passed; the only repository change remains the pre-existing unrelated
  `hdc_musicgen_experiments.py` modification. No provider, network, remote
  resource, or data-download action occurred.
  Latest evidence (2026-07-30): final local reconciliation confirms
  `smoke-r2/REMOTE_JOB.md` records both provisioned pods deleted before
  execution and `smoke-r2/artifacts/` is absent, so no Stage 0/S/A result
  exists. At `41022d5`, the focused fail-closed suite passed 11/11 in 0.77 s
  and `git diff --check` passed; only the pre-existing unrelated
  `hdc_musicgen_experiments.py` modification remains. The smoke-r2 handoff is
  closed as a no-result; no provider, network, remote resource, or data
  download was used.
  Latest evidence (2026-07-30): independent local boundary revalidation
  reconfirmed the run has no `artifacts/` directory and its remote record says
  both pods were deleted before execution (no Stage 0/S/A command or GPU
  work). At `41022d5`, focused fail-closed tests passed 11/11 in 0.79 s and
  `git diff --check` passed; the only worktree change is the pre-existing,
  untouched unrelated `hdc_musicgen_experiments.py` modification. No
  provider, network, remote resource, or data download was used.
  Latest evidence (2026-07-30): repeated the terminal boundary check against
  `REMOTE_JOB.md` lines 4/24 (both pods deleted pre-execution; no Stage 0/S/A
  or GPU work) and confirmed `artifacts/` is absent. At `41022d5`, the focused
  support-aware/missing-aggregate suite passed 11/11 in 0.78 s and `git diff
  --check` passed. The handoff remains closed as a no-result; no provider,
  network, remote resource, or data download was used.
  Latest evidence (2026-07-30): a bare module import is intentionally invalid
  because this CLI parses its required stage at module load; the focused
  loader supplies inert `stageS --device cpu` arguments and is the valid
  pure-logic harness. The 11/11 result therefore revalidates the frozen,
  support-aware/missing-aggregate policy without touching the pre-existing
  unrelated worktree change. `smoke-r2` remains a no-result: both pods were
  deleted pre-execution and its `artifacts/` directory is absent. No provider,
  network, remote resource, or data download was used.
  Latest evidence (2026-07-30): at prospective direct-recurrence pin
  `74287d9`, the structural suite passed 13/13 in 0.78 s. A local replay of
  the verified smoke-r3 Stage-A summary returned `gate_pass=true` and
  `nll_sanity_pass=true`: RELATED alone was band-checked (gain
  `0.0541862746`), UNRELATED was support-insufficient at one span (gain
  `0.0009179115`), and non-finite/missing-condition/alignment stops were all
  false. `git diff --check` passed with a clean worktree. This validates the
  accepted policy only; smoke-r2 remains a terminal no-result and no remote,
  provider, or data action is authorized. See `NOTES.md`.
  Latest evidence (2026-07-31): at the same prospective pin, the complete
  local suite passed 20/20 in 0.80 s. A direct gate boundary replay accepted
  in-band RELATED (`n=4`) with low-support UNRELATED (`n=1`) explicitly
  reported, while a sparse `0.49` alignment value and sparse `NaN` each failed
  NLL sanity. `git diff --check` passed with a clean worktree. This confirms
  the direct-recurrence amendment preserves the accepted hardened NLL policy;
  smoke-r2 remains a terminal no-result and no remote action is authorized.
  Latest evidence (2026-07-31): at direct-gate pin `74287d9`, the complete
  local suite again passed 20/20 in 0.88 s and `git diff --check` passed with
  a clean worktree. Static execution-path review confirms Stage A reads and
  fails on a false `stageS_summary.json.gate_pass`; Stage S sets that gate only
  with cross-window RELATED/UNRELATED separation >=0.15, and RELATED requires
  cosine >=0.80. No provider, network, remote resource, or data download was
  used; prospective validation does not reopen smoke-r2 or r5.
  Latest evidence (2026-07-31): at direct-gate pin `74287d9`, the focused
  structural/NLL suite passed 13/13 in 0.87 s and `git diff --check` passed
  with a clean worktree. This includes the support-aware low-support handling,
  unconditional sparse non-finite/alignment stops, and missing-aggregate
  fail-closed regression. The smoke-r2 handoff remains closed as a no-result;
  no provider, network, remote resource, or data-download action occurred.
  Latest evidence (2026-07-31): ancestry at prospective pin `74287d9`
  confirms it contains hardened-policy commits `8907d0f` and `41022d5`; the
  full local suite passed 20/20 in 0.85 s and the worktree was clean. An
  isolated sparse-UNRELATED boundary replay with `window=8.01` returned
  `nll_sanity_pass=false` and `nll_alignment_bug_stop=true`, proving low
  support does not waive the unconditional `>8` stop. See `NOTES.md`. No
  provider, network, remote resource, or data download was used.
  Latest evidence (2026-07-31): SHA-256 verification passed for all 12 r5
  result files. The returned 22 tensors/metadata entries total 66.0 minutes,
  are valid finite `4 x 9000` tokens in `[0,2048)`, and pass `74287d9`'s
  prospective `codec_token_sanity()`/`data_gate()`; its full suite passed
  20/20 in 0.85 s with a clean worktree. This is explicitly non-retroactive:
  r5 remains failed at its original persistence gate and has no Stage-S
  artifact; any fresh run still needs approval. See `NOTES.md`. No provider,
  network, remote resource, or data download was used.
  Final local closure (2026-07-31): at prospective pin `74287d9`, the focused
  support-aware/missing-aggregate suite passed 13/13 in 0.88 s and `git diff
  --check` passed. `smoke-r2/REMOTE_JOB.md` records both pods deleted before
  execution, and its `artifacts/` directory remains absent. Therefore the
  smoke-r2 handoff is a terminal no-result and the hardened NLL policy is
  frozen/accepted; do not reopen either under this worker. Any new MusicGen
  run requires a fresh explicit provider/resource/price/cost/time/data/stop
  authorization.
  Latest evidence (2026-08-01): at `74287d9`, the complete local suite passed
  20/20 in 0.85 s with clean `git diff --check` and status. A boundary replay
  passed sparse in-band UNRELATED NLL but failed sparse `0.49`, `8.01`, and
  `NaN`, preserving unconditional alignment/non-finite stops. `PROJECT.md`
  was reconciled to mark smoke-r2 terminally no-result and the NLL policy
  resolved; no provider, remote, network, or data action occurred.
  Latest evidence (2026-08-01): closure regression at `74287d9` passed the
  focused structural suite 13/13 in 0.86 s; `git status --short` was empty and
  `git diff --check` passed. This reconfirms the frozen policy safeguards and
  does not reopen smoke-r2; no provider, network, remote resource, or data
  download was used.
  Latest evidence (2026-08-02): closure regression at `74287d9` passed
  `test_hdc_musicgen_structural.py` 13/13 in 0.81 s; `git status --short` was
  empty and `git diff --check` passed. Smoke-r2 remains terminally no-result,
  and the support-aware NLL policy remains frozen with fail-closed safeguards.
  No provider, network, remote resource, corpus download, or paid action was
  used.
- [x] Prepare a replacement RunPod proposal for the 8-track full-length
  smoke-r2, including a runbook amendment for the one-span smoke NLL policy.
  The attempted continuation pod `mkiku77kmu4rf9` was unreachable (SSH
  refused) and terminated at 2026-07-27T08:47Z; RunPod then returned an empty
  pod list and 404 for the ID. Acceptance: an explicit amended gate and fresh
  provider/resource/time/cost approval are recorded before provisioning.
  Owner approval recorded 2026-07-27; live RTX 3090 availability remains the
  only provisioning blocker. Evidence:
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`.
- [x] Resolve the smoke-only absolute-NLL sanity policy before any new paid
  resource. Ben accepted D-20260727-smoke-r2-low-support-nll-amendment:
  apply the 1.5–6.0 band only to strata with >=4 spans; report smaller strata
  as support-insufficient; keep unconditional finite, `<0.5`, and `>8` stops.
  The later `41022d5` hardening also rejects missing aggregate fields. Evidence:
  `DECISIONS.md`, `NOTES.md`, and the verified smoke-r3 aggregate audit
  (2 strata × 4 finite fields; focused suite 11/11). This decision does not
  authorize another paid run.

## Next

- [ ] After approval only, download the selected license-clean ≥20-track set.

## Waiting or blocked

- [ ]

## Someday or exploratory

- [ ]

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] Executed the approved frozen GPU job fail-closed through smoke Stage A:
  prepared 24 license-explicit tracks, passed Stage S separation, stopped on
  the absolute-NLL sanity gate, retrieved and hashed all partial artifacts,
  and terminated the RunPod pod with empty-list/404 confirmation
  (2026-07-26). Evidence:
  `experiments/20260726T043220Z-gpu-run/RUN.md`.
- [x] Implemented Ben's structural-memory runbook as a new 0/S/A/C/D script,
  copied the authoritative runbook, added six focused tests, retained seven
  passing legacy tests, and updated project/run records (2026-07-25). Evidence:
  `experiments/20260725T-structural-rewrite/RUN.md`.
- [x] Prepared fixed code, 7 regression tests, four deterministic WAV
  fixtures, documented partial local smoke, and frozen remote proposal at
  commit `59eade2` (2026-07-25).
- [x] Ben explicitly approved RunPod RTX 3090 execution with an 18-hour
  timeout and USD 25 hard cap (2026-07-26). Evidence:
  `experiments/20260726T043220Z-gpu-run/REMOTE_JOB.md`.
