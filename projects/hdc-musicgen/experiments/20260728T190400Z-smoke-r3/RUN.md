# Run 20260728T190400Z-smoke-r3

- Status: `completed; artifacts locally verified; pod terminated`
- Question: Does the amended eight-track MusicGen Stage 0/S/A smoke execute
  cleanly and report the preregistered related-versus-unrelated measurements?
- Source: `8907d0f`; pod `xgv04sy1g9a3q8`; cap 8 hours / USD 5.

## Execution evidence

- At 2026-07-28T19:07Z, transferred a Git archive of the pinned source and
  exactly eight explicit-CC MP3 files. The remote SHA-256 values matched the
  local selection manifest.
- The recorded completion in `REMOTE_JOB.md` states exit 0 at 2026-07-28T23:41Z
  and pod deletion at 2026-07-28T23:44Z. Local-only reconciliation on
  2026-07-29 independently matched all seven returned result-file hashes and
  all eight retained-input hashes in `artifacts/remote-sync/SHA256SUMS` against
  the synced artifacts and the pre-existing local corpus, respectively.
- Stage 0 correctly reported smoke mode (8 tracks, 24 minutes; full 20-track/
  60-minute corpus gate not evaluated as a pass). Stage S passed: RELATED
  0.985981 versus UNRELATED 0.493875, separation 0.492106. Stage A passed
  under the accepted support-aware policy: RELATED relevance gain 0.054186
  nats/token (48 spans); UNRELATED n=1 is support-insufficient, with neither
  non-finite nor `<0.5` alignment-bug stop triggered. Stage C/D were not run.
