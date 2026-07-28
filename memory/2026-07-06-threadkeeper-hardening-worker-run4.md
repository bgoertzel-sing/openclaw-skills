# 2026-07-06 ThreadKeeper Hardening Worker (run 4)

## Summary

ThreadKeeper branch `agent/threadkeeper-hardening-next` commit `c6f9708` pushed to `fork/agent/threadkeeper-hardening-next`: **Add workspace file size cap for write-file and append-file**. 144 focused mock tests passing.

## Changes

- **Workspace file size cap**: Added `OMEGACLAW_SUBAGENT_MAX_FILE_SIZE_CHARS` (default 100000 = ~100KB, 0 disables) to cap the resulting file size for `write-file` and `append-file`. This closes a gap where:
  - `append-file` reads the ENTIRE existing file into memory before appending — a file grown to hundreds of MB through repeated appends would cause memory exhaustion on the next append call
  - Neither tool checked total file size, allowing unbounded disk growth from repeated append-file calls
- **`write-file`**: rejects content exceeding the cap before any disk write
- **`append-file`**: checks existing file size via `os.path.getsize()` before reading into memory (preventing memory exhaustion), then checks resulting size (existing + new + newline) before writing. File is left unchanged on cap violation (fail-closed).
- 7 focused tests added (144 total): write-file content exceeding cap, write-file under cap, write-file cap disabled at 0, append-file existing file exceeding cap (no read), append-file resulting file exceeding cap (no write), append-file under cap, append-file cap disabled at 0.

## Verification

- `git diff --check`
- `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`
- Focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`144 passed`)
- `origin/pr-1` remains an ancestor (76 commits ahead)
- Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff

## Constraints

No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.
