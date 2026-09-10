# Tasks

## Immediate

- [x] 2026-06-28: Benjamin confirmed private GitHub repos under `bgoertzel-sing` for `zerobot-recovery` and `protomegabot-recovery`.
- [x] 2026-06-28: Created local repo staging directories for `zerobot-recovery` and `protomegabot-recovery`.
- [x] 2026-06-28: Generated initial sanitized contents using backup scripts.
- [x] 2026-06-28: Ran lightweight secret scan and inspected staged file list.
- [x] 2026-06-28: Created private GitHub repos and pushed initial commits after confirmation.
- [x] 2026-07-07: Repaired stalled backup path: tightened false-positive-prone `sk-` scanner, excluded/deleted venv-like local trees from Protomegabot snapshot, added fetch/rebase-before-push handling, and pushed fresh snapshots (`zerobot-recovery` `2ef932d`, `protomegabot-recovery` `25c8b3c`).

## Automation

- [x] 2026-07-15: Repaired the misleading scheduler failure by pinning the cron
  worker to `openai/gpt-5.5` and requiring an explicit `NO_REPLY` success
  response after verification. Forced validation passed; both recovery
  repositories were refreshed and synchronized.
- [x] 2026-06-28: Added daily scheduler after first successful manual backup/push: OpenClaw cron `Daily agent recovery GitHub backup` (`5ae59dd5-dfe3-4ace-999d-a08ca153325e`) at 03:30 America/Vancouver.
- [x] 2026-07-07: Scheduler fails closed on secret-scan warnings, but scanner now avoids known hyphenated-ID false positives and excludes venv-like trees that previously created noisy SPDX matches.
- [x] 2026-07-23: First restore-smoke drill completed. Both repos cloned
  into throwaway `/tmp/restore-drill-2026-07-23/`, RESTORE.md followed top to
  bottom, secret scan clean, all manifest files present. Findings: ZeroBot
  repo PASS (130 files, 7 core context files in `openclaw-context/`, 39 memory
  files, 18 project notebooks, `RESTORE.md` accurate). ProtoMegaBot repo PASS
  (44 files, omegaclaw notebooks + local wrappers + RUNBOOK present,
  upstream repo pointers resolve, `RESTORE.md` accurate). Neither repo had a
  `LAST_BACKUP` marker — added marker write to `push-recovery-repos.sh`.
  Throwaway dir deleted.

- [x] 2026-07-23: Added `LAST_BACKUP` timestamp marker to
  `push-recovery-repos.sh`. Each repo now gets a `LAST_BACKUP` file with
  `YYYY-MM-DDTHH:MM:SSZ|ok|<short-hash>|<file-count>` committed after every
  push, so backup health is verifiable from the repo itself.

- [x] Restore check cadence: first Saturday of each month, rotating owner
  between ZeroBot and ProtoMegaBot. Formalized in `RESTORE_DRILL_CHECKLIST.md`
  with pass/fail criteria, alert path, and per-repo checks. 2026-07-28.

- [x] **2026-08-02:** First scheduled monthly restore drill completed one day
  late by ProtomegaTron. Both recovery repositories passed all five checks;
  evidence is in `drill-reports/2026-08-02.md`. Four non-blocking restoration-
  documentation findings remain as follow-up work.

- [x] **2026-08-03:** Verified live backup-cron failure-alert routing. Cron
  `5ae59dd5-dfe3-4ace-999d-a08ca153325e` has success delivery disabled and a
  separate failure alert configured after one error to ProtoBots-updates
  (`telegram:-1003983157420`) with a 24-hour cooldown. The observed
  `not-requested` status followed a successful run and is expected; it does not
  indicate missing failure routing. A real failure delivery has not been
  induced merely to test notification transport.

- [x] Resolve the four non-blocking restore-documentation findings listed in
  `drill-reports/2026-08-02.md`: two RESTORE.md paths, the missing
  `conversation-governor` remote pointer, and 13 absolute symlinks. All four
  closed at commit `adb1013` on 2026-08-06; see drill report action items.

## Later

- [ ] Add optional encrypted artifact path if Benjamin wants larger state preserved.
- [ ] Periodically test restoration instructions on a clean machine or container.
