# Monthly Restore Drill Checklist

**Cadence:** First Saturday of each month, alternating owner each drill: ProtomegaTron → ZeroBot → ProtomegaTron → … (August 2026 was ProtomegaTron; September 2026 is ZeroBot).

**Scope:** Non-destructive clone + walkthrough of both recovery repos.

---

## Pre-drill

- [ ] Confirm LAST_BACKUP markers in both repos are ≤ 48 h old.
- [ ] Note current HEAD commit hashes for both repos.

## Per-repo (repeat for zerobot-recovery and protomegabot-recovery)

### 1. Clean clone
- [ ] Clone into a throwaway directory (`/tmp/restore-drill-YYYY-MM-DD/<repo>`).
- [ ] Verify clone succeeds and HEAD matches the noted hash.

### 2. RESTORE.md walkthrough
- [ ] Read RESTORE.md top to bottom.
- [ ] Verify every referenced file/path exists in the repo.
- [ ] Verify every referenced upstream URL resolves (HTTP 200 or redirect to valid target).
- [ ] Flag any step that references a tool, version, or path that no longer exists.

### 3. MANIFEST.md completeness
- [ ] Compare MANIFEST.md entries against actual repo contents.
- [ ] Flag missing files or undocumented additions.

### 4. Secret scan
- [ ] Run the project's secret scanner against the cloned tree.
- [ ] Confirm zero true-positive secret detections.

### 5. LAST_BACKUP marker
- [ ] Verify LAST_BACKUP file exists and parses correctly (`timestamp|ok|hash|count`).
- [ ] Verify marker timestamp is ≤ 48 h old.
- [ ] Verify marker hash matches HEAD.
- [ ] Verify file count is within ±10% of previous drill (flag large swings).

## Post-drill

- [ ] Delete throwaway directory.
- [ ] Write drill report: date, owner, per-repo PASS/FAIL, any findings.
- [ ] Commit drill report to the agent-recovery project notes.
- [ ] If any FAIL: file a task in TASKS.md and alert via ProtoBots-BotBotChats.

## Pass/Fail criteria

| Check | PASS | FAIL |
|---|---|---|
| Clone | Succeeds, HEAD matches | Clone fails or hash mismatch |
| RESTORE.md | All steps valid, all refs resolve | Any broken ref or stale step |
| MANIFEST.md | All entries present, no undocumented files | Missing or undocumented entries |
| Secret scan | Zero true positives | Any true-positive secret detected |
| LAST_BACKUP | Exists, fresh (≤ 48 h), hash matches HEAD | Missing, stale, or hash mismatch |

**Repo verdict:** PASS iff all five checks pass. Otherwise FAIL with itemized findings.

**Drill verdict:** PASS iff both repos pass. Otherwise FAIL.

## Alert path

1. Drill owner writes report to `projects/agent-recovery/drill-reports/YYYY-MM-DD.md`.
2. PASS: brief summary posted to ProtoBots-BotBotChats (`telegram:-5459676079`).
3. FAIL: detailed finding posted to ProtoBots-BotBotChats + task filed in TASKS.md + ping Ben if secret leak detected.
4. Backup cron failure (daily): alert to ProtoBots-updates (`telegram:-1003983157420`).
