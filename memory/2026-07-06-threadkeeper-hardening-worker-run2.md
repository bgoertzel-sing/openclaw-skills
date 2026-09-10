# 2026-07-06 ThreadKeeper Hardening Worker (run 2)

## Summary

ThreadKeeper branch `agent/threadkeeper-hardening-next` commit `ca98d36` pushed to `fork/agent/threadkeeper-hardening-next`: **Add run index entry bounding with rotation**. 129 focused mock tests passing.

## Changes

- **Run index entry bounding**: Added `OMEGACLAW_SUBAGENT_MAX_INDEX_ENTRIES` (default 0 = disabled) to cap the number of entries in `index.jsonl`. When non-zero, the index is rotated after each append to keep only the most recent N entries. The hash chain is recomputed for retained entries (first retained entry gets `previous_entry_sha256=""`). This prevents unbounded audit log growth in long-running @Protomegabot deployments. `verify_subagent_run_index` still passes on the retained portion after rotation.

- 5 focused tests added: rotation truncates to cap, disabled when 0, no rotation under cap, rotated index verifies correctly, single-entry cap.

## Verification

- `git diff --check`: clean
- `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`: OK
- Focused mock pytest via `local/threadkeeper-pytest-venv`: 129 passed
- `origin/pr-1` remains an ancestor (73 commits ahead)
- Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff

## Constraints

No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.
