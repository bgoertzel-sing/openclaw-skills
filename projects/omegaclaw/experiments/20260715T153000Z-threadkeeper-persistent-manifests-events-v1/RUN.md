# Experiment: ThreadKeeper Persistent Worker — Durable Manifests, Events, Status APIs

**Run ID:** 20260715T153000Z-threadkeeper-persistent-manifests-events-v1
**Date:** 2026-07-15
**Branch:** `agent/threadkeeper-persistent-workers`
**Commit:** `f82d168`
**Base:** `7aa49e1` (lifecycle contract), `a2c62eb` (ThreadKeeper hardening)
**Worktree:** `projects/omegaclaw/worktrees/threadkeeper-persistent-workers`

## Objective

Implement the second provider-free slice: versioned durable task/event
manifests and read-only status APIs with fail-closed integrity, preserving
bounded `delegate` unchanged.

## Environment

- OS: Linux 7.0.11-76070011-generic (x64)
- Python: 3.10.12
- pytest: 9.1.1
- No provider calls, no network, no Telegram, no ProtoMegaBot access.

## What was implemented

1. **`create_task_manifest(root, manifest)`** — atomically creates an immutable
   `manifest.json` under `tasks/<id>/` with version tags, SHA-256
   self-integrity, and strict field validation. Uses `os.link` for
   create-if-absent semantics; rejects symlinks and non-regular files.

2. **`append_task_event(root, task_id, ...)`** — appends one CAS-checked
   lifecycle event to `events.jsonl`. Enforces:
   - Expected version / prior-state compare-and-swap.
   - Hash chain (`previous_event_sha256`).
   - Idempotent replay for duplicate `event_id` with matching fields.
   - Legal transition check via `transition_decision`.
   - File locking with `fcntl.flock` on POSIX.
   - Size limits on individual events and total log.

3. **`worker_status(root, task_id)`** — read-only projection that replays
   the event chain from the manifest, verifying every hash, version, and
   transition. Returns a bounded `status.v1` record.

4. **`list_worker_statuses(root, limit)`** — lists verified task statuses
   with fail-closed rejection of symlinks, non-directory entries, and
   corrupted tasks.

## Tests

```
11 persistent-worker lifecycle/storage tests:
  - Complete state-pair truth table (13×13)
  - MeTTa/Python terminal set parity
  - MeTTa/Python transition set parity
  - Terminal states have no outgoing transitions
  - Unknown and malformed states fail closed
  - Manifest + event + status round-trip
  - Event replay idempotent and CAS-checked
  - Denied transition does not append
  - Tampered manifest/event fails status closed
  - Symlink task entry fails list closed
  - Unknown versions and oversized logs fail closed

5 existing subagent hardening regression tests (delegate unchanged):

Total: 16 passed, 0 failed, 0 errors
```

## Commands

```bash
python3 -m py_compile src/persistent_worker.py
python3 -m pytest tests/test_persistent_worker_lifecycle.py -v
python3 -m pytest tests/ -v
git diff --check
git add docs/persistent-workers.md src/persistent_worker.py tests/test_persistent_worker_lifecycle.py
git commit -m "Implement durable task manifests, event logs, and read-only status APIs"
```

## Result

PASS — all 16 tests green, compile clean, `delegate` unchanged, no
provider/process/Telegram effects.

## Next phase

Spawn and cancellation surface: `spawn-persistent` that creates one durable
task via the existing validated queue path; idempotent cancel requests and
intervention tests.
