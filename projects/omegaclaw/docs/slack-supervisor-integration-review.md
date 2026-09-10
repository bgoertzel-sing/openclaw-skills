# Expert Review: Slack Supervisor Integration Design

**Reviewer:** Sol (openrouter/z-ai/glm-5.2), acting as frontier model reviewer
**Date:** 2026-09-01
**Document reviewed:** `docs/slack-supervisor-integration-design.md`
**Verdict:** **Approve with conditions.** The design is fundamentally sound and is the right approach. Four issues must be resolved before implementation; two are blocking, two are advisory.

---

## 1. Concurrency Safety: Concurrent `clean_responder.responder()` from Two Processes

### Verdict: **SAFE, with one caveat to verify on the live system.**

The design correctly identifies the concern (Section 4.3) but under-specifies the analysis. Here is the full picture:

**What `clean_responder.responder()` actually does** (reconstructed from `slack_live_launcher.py` line 44 and `phase6_private_canary_runner.py` line 405):

The Slack receiver's `live_responder()` calls `clean_responder(text, _provider_args, "slack-v2-live")`, which is a **separate module** (`/hive/protomega/bin/clean_responder.py`) distinct from `phase6_private_canary_runner.py`'s `responder()` function. The Telegram path (protomega UID 11003) goes through `phase6_private_canary_runner.py`'s `responder()`, which spawns a subprocess (`subprocess.Popen`) with a unique session ID (`{session_prefix}-{int(time.time())}`), a unique prompt file (tempfile), and a clean env dict (token stripped). Each call is a fresh process invocation with no shared mutable state between calls.

**Therefore:** The two paths (Telegram and Slack) are not contending on the same in-memory state. Each provider invocation spawns its own subprocess tree. The Slack path calls a different module (`clean_responder.py`) which presumably also spawns a subprocess — it would need to be inspected on the VM to confirm, but given that the canary succeeded with the tag "slack-v2-live" and a real LLM response, it is functioning as an independent provider handoff.

**Shared resources to check:**

1. **Worker state directories.** `phase6_private_canary_runner.py` uses `--worker-state-dir /hive/protomega/state/protomega-worker-state` for Telegram. The Slack path uses `/hive/protomega/state/slack-v2/` for its own state. **No collision.** But `clean_responder.py` might write to a shared worker state path — this needs verification on the VM (`cat /hive/protomega/bin/clean_responder.py`).

2. **ChromaDB.** Both paths get `CHROMA_DB_PATH=/hive/<identity>/state/chroma_db` from `agent_worker.py`'s env setup. Since the Slack receiver would run as `protomega-slack` (UID 11005), its `CHROMA_DB_PATH` would be `/hive/protomega-slack/state/chroma_db` — **not the same path as protomega's**. This is correct isolation, but note that the design symlinks `state/slack-v2` → protomega's state dir, which is the SQLite Slack state, not the ChromaDB. The ChromaDB for protomega-slack would be empty/uninitialized. **This is fine** if `clean_responder.py` doesn't rely on ChromaDB for provider handoff (it likely doesn't — it's a provider bridge, not a RAG path).

3. **File-based locks.** The Slack receiver uses `TokenOwnership(LOCK_FILE)` with `fcntl.flock(LOCK_EX | LOCK_NB)` on `/hive/protomega/state/slack-v2/slack-token-owner.lock`. The Telegram path has no equivalent lock file. **No contention.**

4. **Concurrent provider invocations.** If a Telegram message and a Slack message arrive simultaneously, both spawn independent subprocess trees with different session IDs and different prompt files. The underlying OpenClaw/PeTTa runtime handles its own session isolation. **No race condition** unless the runtime has a global singleton (unlikely given the architecture).

**Caveat (non-blocking):** The design's Section 4.3 says "this is likely a non-issue since the provider handoff is designed to be per-call stateless." This is correct but should be verified by reading `clean_responder.py` on the VM before implementation, as the design itself acknowledges in Open Question #2 (Section 9). The verification is a 5-minute read.

**Risk rating:** Low. The architectural separation (subprocess-per-call, unique sessions, no shared mutable state) makes concurrent access safe.

---

## 2. Supervisor Integration Safety

### Verdict: **SAFE.** The design is purely additive and the supervisor's restart loop is simple enough to be obviously correct with a new entry.

### 2.1 Restart loop

The supervisor's restart loop (Appendix A, lines 28-34) iterates `IDENTITIES.items()`, polls each child, and respawns dead ones. Adding a fifth entry to `IDENTITIES` does not change the loop's behavior for existing entries. The `start()` function takes `identity` and `uid` as parameters — no global state mutation. **No risk to existing identities.**

### 2.2 Demotion logic

`demote(uid)` calls `os.setgroups([]); os.setgid(10001); os.setuid(uid); os.umask(0o077)`. UID 11005 would need to exist as a user inside the container (or at least be a valid UID for `setuid`). The existing design's Open Question #3 asks to verify this. **Action:** Run `getent passwd 11005` inside the container. If no entry exists, `setuid(11005)` will still succeed (Linux allows setuid to any numeric UID), but `setgid(10001)` requires group 10001 to exist — it already does for the other identities, so this is fine.

**No risk.** The demotion is per-process and doesn't affect existing identities.

### 2.3 Env propagation

The supervisor calls `subprocess.Popen([sys.executable, "/opt/proto-hive/bin/agent_worker.py", "--identity", identity, "--mode", mode], preexec_fn=demote(uid))`. The child inherits the supervisor's environment. The supervisor gets its env from the Docker container's `environment` block (per `compose.live.yaml`: `TELEGRAM_POLLING_ENABLED: "1"`). **This is the critical path for the new env var — see Section 3 below.**

### 2.4 Status publishing

`agent_worker.py` writes status to `/run/proto-hive/status/<identity>`. The new identity `protomega-slack` would publish to `/run/proto-hive/status/protomega-slack`. This works — the `status` directory is created by the supervisor with mode 0733, and each worker creates its own file. **No collision risk.**

### 2.5 Supervisor restart behavior on crash loop

If `slack_live_launcher.py` crashes immediately (e.g., bad env file), the supervisor will restart it every 2 seconds indefinitely. There is **no exponential backoff and no max-retry limit** (noted correctly in Section 2.1). This is pre-existing behavior shared by all identities — not a new risk introduced by this design. However, a crash-looping Slack receiver will generate log spam. **Advisory:** Consider adding a crash-rate circuit breaker to the supervisor in a future iteration, but do not block this design on it.

---

## 3. Activation Gate Design

### Verdict: **SOUND, but the env var propagation path has a concrete gap that must be fixed.**

### 3.1 Marker file

The `ENABLE-SLACK` marker file at `/hive/protomega-slack/activation/ENABLE-SLACK` is a parallel to the existing `ENABLE-POLLING` marker. The if-branch in `agent_worker.py` (Section 4.1.3) correctly checks identity before selecting the marker and env var name. This is clean and doesn't affect the existing activation gate.

### 3.2 Env var propagation — **BLOCKING ISSUE**

The `compose.live.yaml` shows:
```yaml
environment:
  TELEGRAM_POLLING_ENABLED: "1"
```

This is the **only** env var set in the container environment. `SLACK_POLLING_ENABLED` is **not present**. The design's Open Question #1 (Section 9) correctly flags this but leaves it unresolved.

**The env var MUST be added to `compose.live.yaml`** (or to the container's environment via `docker exec` runtime update, but that won't survive container restart). The concrete fix:

```yaml
environment:
  TELEGRAM_POLLING_ENABLED: "1"
  SLACK_POLLING_ENABLED: "1"
```

Without this, `agent_worker.py`'s check `os.environ.get("SLACK_POLLING_ENABLED") == "1"` will fail, the worker will go idle, and Slack will be silent. **This is the most likely failure mode during implementation.**

The design's Section 5.1 step 5 says "This env var must be set in the supervisor's environment" but doesn't specify how. The answer is: **edit `compose.live.yaml` on the VM host** (at `/opt/proto-hive-runtime/` or wherever the compose file lives) and recreate the container (`docker compose up -d` with the updated compose file). This requires a container restart, which will briefly interrupt all four existing identities. Schedule accordingly.

**Alternatively**, `agent_worker.py` could source env vars from a per-identity env file (e.g., `/hive/protomega-slack/config/activation.env`), but this would require code changes beyond the current design and is not worth the complexity for a single boolean.

### 3.3 Marker file persistence

The `/hive/` path is mounted from `/opt/proto-hive-runtime` (per `compose.live.yaml`: `volumes: - /opt/proto-hive-runtime:/hive:rw`). This is a host bind mount, so marker files persist across container restarts. **This is correct.** The design's Open Question #5 is answered by the compose file: `/hive/protomega-slack/activation/` is on the persistent volume.

---

## 4. State and Symlink Safety

### Verdict: **SAFE with one race condition to address.**

### 4.1 State symlink

The design symlinks `/hive/protomega-slack/state/slack-v2` → `/hive/protomega/state/slack-v2/`. This preserves the SQLite cursor and the ownership lock file across the identity boundary. **This is correct and necessary** — if the state dir were copied or recreated, the cursor would reset and the lock file would be stale.

### 4.2 Ownership lock race

The `TokenOwnership` lock uses `fcntl.flock(LOCK_EX | LOCK_NB)` on a file inside the symlinked state dir. If the old detached receiver (UID 11003) is still running when the new supervised receiver (UID 11005) starts, the new one will get `OwnershipError("slack token already has a local owner")` and exit. The supervisor will restart it, and it will keep failing until the old process dies or releases the lock.

**This is correct behavior** — it prevents dual receivers. The activation procedure (Section 5.1 step 1: "Stop the current detached receiver") must be completed before starting the supervised one. The design already specifies this. **No race condition.**

**However:** `fcntl.flock` is per-file-handle, not per-process. The lock is released when the file descriptor is closed (which happens on process death, including `kill -9`). The design's claim in Section 6 ("Ownership lock stale after crash: Low risk — TokenOwnership uses fcntl/flock — released automatically on process death") is **correct**. `flock`-based locks are kernel-managed and released on process termination regardless of signal.

### 4.3 SQLite cursor continuity

The SQLite database at `/hive/protomega/state/slack-v2/slack-durable-state.sqlite3` uses WAL mode (`PRAGMA journal_mode=WAL`). If two processes attempt to write to a WAL-mode SQLite database concurrently, one will get `SQLITE_BUSY` and retry (or fail, depending on busy_timeout). 

**Potential issue:** If the old receiver is killed mid-transaction and the new one starts immediately, WAL recovery might not have completed. However, `DurableState.recover()` calls `UPDATE inbox SET status='queued' WHERE status='processing'` and `UPDATE outbox SET status='uncertain' WHERE status='sending'` — this is a standard crash-recovery pattern. SQLite WAL is designed for this. **No risk.**

### 4.4 Secrets symlinks

Symlinking `omegaclaw-slack.env` and `omegaclaw-telegram.env` from `/hive/protomega/secrets/` is correct — the secrets remain owned by UID 11003 (protomega), but the symlink at `/hive/protomega-slack/secrets/` would be accessible by UID 11005 (protomega-slack). 

**Permission check:** The secrets files must be readable by UID 11005. Currently they are mode 0600 (owner-only). If owned by UID 11003, UID 11005 **cannot read them** — `setuid(11005)` drops the ability to read files owned by 11003 unless the file has group-read or other-read permissions. The `SlackTransport.from_env_file()` method explicitly checks for mode 0600 and rejects anything else.

**BLOCKING ISSUE:** The design does not address file permissions on the symlinked secrets. Two options:
1. **Change ownership** of the secrets files to 11005:11001 — but this breaks the protomega identity's access (protomega UID 11003 would lose access unless group 10001 has read permission).
2. **Set group-read** on the secrets files (mode 0640) and ensure both UIDs are in group 10001 — but `demote()` calls `os.setgroups([])` which **clears all supplementary groups**. So group-read won't work either.
3. **Make the secrets files world-readable** (mode 0644) — **unacceptable** for secret material.
4. **Copy the secrets** instead of symlinking — but the design explicitly chose symlinks to avoid duplicating secrets.

**Resolution:** The simplest safe approach is to **make the secrets files owned by UID 11005, group 10001, mode 0400** (or 0600), and have protomega's Slack receiver access them via the symlink. But this would break protomega's own access if it ever needs to read them. Since protomega (11003) doesn't read the Slack env file, this is actually fine — the Slack env file is only needed by the Slack receiver. 

Wait — the `PROVIDER_ENV` (`omegaclaw-telegram.env`) IS read by the Slack receiver (`_provider_args = SimpleNamespace(env=PROVIDER_ENV)`) AND by the Telegram poller. If we chown it to 11005, the Telegram poller (UID 11003) loses access.

**Actual resolution:** The `omegaclaw-telegram.env` file must be readable by both UID 11003 and UID 11005. The cleanest solution is:
- Set file mode to 0440 (group-read only)
- Set group to 10001
- **Fix `demote()` to NOT clear supplementary groups** — or add group 10001 back after setgroups.

But modifying `demote()` affects all identities, which the design explicitly avoids. The alternative: **use a bind mount or hard copy for the secrets, not a symlink.** The design should use:
```bash
cp /hive/protomega/secrets/omegaclaw-telegram.env /hive/protomega-slack/secrets/omegaclaw-telegram.env
chown 11005:10001 /hive/protomega-slack/secrets/omegaclaw-telegram.env
chmod 0600 /hive/protomega-slack/secrets/omegaclaw-telegram.env
```

For `omegaclaw-slack.env`, only the Slack receiver reads it, so chowning to 11005 is fine (either symlink or copy works).

**This is a real blocking issue that the design does not address.** The `os.setgroups([])` in `demote()` is the root cause — it strips group membership, making group-read useless. The design must either:
- Copy secrets with appropriate ownership (recommended, minimal blast radius), or
- Modify `demote()` to retain group 10001 (larger blast radius, affects all identities).

### 4.5 Stale lock after container restart

On container restart, the supervisor respawns all workers. The old Slack receiver process is dead (killed by container stop). `flock` is released by the kernel. The new receiver acquires the lock cleanly. `prime_cursor()` advances the cursor past all existing messages. **No stale lock risk.** The design's Section 6 risk table is correct on this point.

---

## 5. Missing Controls and Blind Spots

### 5.1 No healthcheck update — **ADVISING**

The container's `healthcheck.py` (per `compose.live.yaml`) runs `python3 /opt/proto-hive/bin/healthcheck.py`. If this script monitors `/run/proto-hive/status/*` for health, it should be updated to include `protomega-slack`. The design's Open Question #6 flags this but doesn't resolve it. **Action:** Inspect `healthcheck.py` on the VM and add `protomega-slack` to its identity list if applicable.

### 5.2 No log path specification — **MINOR**

The current detached receiver logs to stdout, which Docker captures as json-file logs. Under the supervisor, `agent_worker.py` uses `subprocess.call()` (not `Popen`) for non-protocosmo identities, meaning the child's stdout/stderr are inherited by the supervisor. The supervisor's stdout goes to Docker logs. **This is fine** — logs will appear in `docker logs proto-hive` with the other identities. The design doesn't need to specify a separate log path.

However, the current persistent instance logs to `/hive/protomega/state/slack-v2/slack-live-persistent.log` (per `memory/2026-09-01.md`). Under supervision, this redirect would be lost. **Not a problem** — Docker's json-file driver is better for log management. But update any log-grep scripts that look at the old path.

### 5.3 No crash-loop alerting — **PRE-EXISTING, NOT INTRODUCED**

If the Slack receiver crash-loops (e.g., Slack token revoked, Slack API down), the supervisor will restart it every 2 seconds indefinitely, generating log spam and consuming CPU. There is no alerting mechanism. This is a pre-existing limitation of `hive_supervisor.py` shared by all identities. **Not introduced by this design.** But worth noting for future improvement.

### 5.4 No graceful shutdown of Slack receiver on supervisor SIGTERM — **VERIFY**

When the supervisor receives SIGTERM, it calls `child.terminate()` on all children (Section 2.1). `agent_worker.py` for non-protocosmo identities does `raise SystemExit(subprocess.call(LAUNCHERS[args.identity], env=env))` — the `call()` blocks until the child exits. So SIGTERM → `agent_worker.py` gets SIGTERM → `subprocess.call`'s child (slack_live_launcher.py) gets SIGTERM. The Slack receiver's signal handler calls `state.close()` and `sys.exit(0)`. 

**This is correct** — graceful shutdown works through the signal chain. The supervisor's 10-second wait timeout (`child.wait(timeout=10)`) is sufficient for SQLite WAL checkpoint + close.

### 5.5 No consideration of Slack API rate limits under crash-loop — **MINOR**

If the receiver crash-loops, each restart calls `auth.test` (to get bot_user_id) and `conversations.history` (to prime cursor). Slack's rate limit for `conversations.history` is ~1 request per second for most apps. A 2-second restart loop would hit this rate. **Risk:** Slack could temporarily rate-limit the bot token. **Mitigation:** The `prime_cursor()` call is lightweight (one API call), and 2-second spacing is within Slack's tier limits. **Not a blocker.**

### 5.6 No consideration of ChromaDB initialization for protomega-slack — **VERIFY**

`agent_worker.py` sets `CHROMA_DB_PATH=/hive/protomega-slack/state/chroma_db` for the new identity. This directory doesn't exist yet. `phase6_private_canary_runner.py` (the launcher for protomega identities) might fail if ChromaDB isn't initialized. But wait — `protomega-slack`'s launcher is `slack_live_launcher.py`, NOT `phase6_private_canary_runner.py`. The launcher path is `OMEGA_COMMON + ["/hive/protomega/bin/slack_live_launcher.py"]`. 

But `OMEGA_COMMON` is `["/usr/bin/python3", "/opt/proto-hive/bin/phase6_private_canary_runner.py"]`. **This means `phase6_private_canary_runner.py` is the first element of the command vector, and `slack_live_launcher.py` would be passed as an argument to it.** This is **WRONG** — `phase6_private_canary_runner.py` is a complete script with its own argparse, not a wrapper. It would interpret `slack_live_launcher.py` as an unknown argument.

**Wait** — let me re-read the LAUNCHERS dict more carefully. Looking at existing entries:

```python
OMEGA_COMMON = ["/usr/bin/python3", "/opt/proto-hive/bin/phase6_private_canary_runner.py"]
"protomega": OMEGA_COMMON + ["--env", ..., "--config", ..., ...]
```

So `protomega`'s launch vector is: `python3 phase6_private_canary_runner.py --env ... --config ... ...`

The proposed `protomega-slack` entry is:
```python
"protomega-slack": OMEGA_COMMON + ["/hive/protomega/bin/slack_live_launcher.py"]
```

This would execute: `python3 phase6_private_canary_runner.py /hive/protomega/bin/slack_live_launcher.py`

**This is a BUG in the design.** `phase6_private_canary_runner.py` would not know what to do with a positional argument that's a path to another script. It would either ignore it (if argparse allows extra positionals) or error out.

**BLOCKING ISSUE:** The LAUNCHERS entry for `protomega-slack` must NOT prepend `OMEGA_COMMON`. It should be:
```python
"protomega-slack": ["/usr/bin/python3", "/hive/protomega/bin/slack_live_launcher.py"]
```

Or, if `slack_live_launcher.py` needs the `OMEGA_COMMON` prefix for some reason (it doesn't — it has its own `if __name__ == "__main__": main()`), the design must explain why. As written, this will not work.

### 5.7 No consideration of `OPENCLAW_DIST` env var — **ADDRESSED but verify**

The design's Section 4.1.4 notes that `agent_worker.py` sets `OPENCLAW_DIST` for non-protocosmo identities, and `slack_live_launcher.py` has a `setdefault` that's now redundant. This is correct — `agent_worker.py` line 93 sets `env["OPENCLAW_DIST"] = "/opt/proto-hive/openclaw/dist"` for all non-protocosmo identities. The `protomega-slack` identity would get this env var. **This is fine.**

But note that the current `slack_live_launcher.py` also calls `os.environ.setdefault("OPENCLAW_DIST", ...)` — keeping it is harmless (setdefault won't override). The design correctly marks this as optional cleanup.

### 5.8 No consideration of `arm_parent_death_signal()` — **RELEVANT**

`phase6_private_canary_runner.py` calls `arm_parent_death_signal()` which checks `OMEGACLAW_EXPECTED_PARENT_PID`. This is set by... let me check. The Telegram path uses `phase6_private_canary_runner.py` as the launcher, so it has this check. But `slack_live_launcher.py` does NOT have this check. Under the supervisor, the parent PID is the `agent_worker.py` process. If the supervisor is killed (not gracefully stopped), the Slack receiver would continue running as an orphan.

**This is a real gap.** The Telegram receivers die when their parent dies because `arm_parent_death_signal()` sets `PR_SET_PDEATHSIG`. The Slack receiver lacks this. **Action:** Add `arm_parent_death_signal()` equivalent to `slack_live_launcher.py`, or set `OMEGACLAW_EXPECTED_PARENT_PID` in the env and add the check.

Alternatively, the supervisor's `stop()` handler sends SIGTERM to all children, and the Docker container's `restart: unless-stopped` means a container kill will restart everything. But if the supervisor process itself is killed (not the container), the Slack receiver could orphan.

**Advisory (not blocking):** Add parent-death signal handling to `slack_live_launcher.py` for consistency with the Telegram path.

### 5.9 No consideration of Docker `pids_limit` — **MINOR**

The compose file sets `pids_limit: 512` for four workers. Adding a fifth worker increases the process count. Each worker spawns provider subprocesses. `slack_live_launcher.py` itself spawns `clean_responder` subprocesses. With five identities, 512 PIDs should still be sufficient (the comment says "four workers plus transient turns"), but the margin is reduced. **Not a blocker** — 512 is generous for this workload.

---

## 6. Strategic Assessment

### Verdict: **Option A is the correct choice.** No alternative approach is better.

**Why Option A is right:**

1. **Minimal blast radius.** The change is purely additive: one dict entry in `IDENTITIES`, one entry in `LAUNCHERS`, one if-branch in the activation gate. No existing line of code is modified. If the new identity fails, the other four are completely unaffected.

2. **Process isolation.** A crash in the Slack receiver cannot affect the Telegram poller because they are separate processes under separate UIDs. Option B (co-spawn) would couple them — a Slack crash could restart the Telegram path, which is unacceptable.

3. **Supervisor is already proven.** The supervisor has been running four identities through container restarts. Adding a fifth is the lowest-risk way to get crash recovery.

4. **Activation gate is elegant.** The marker file + env var pattern means the identity can be activated/deactivated without code changes — just file creation/removal. This is the same pattern used for Telegram, so operators already understand it.

5. **Rollback is trivial.** Remove the marker file, remove the dict entry, restart. The state directory and cursor are untouched. The old detached-receiver approach can be resumed as a fallback.

**Why the alternatives are worse:**

- **Option B (co-spawn):** Coupling two transports in one process is architecturally wrong. The Telegram path uses `phase6_private_canary_runner.py` which has its own `arm_parent_death_signal()`, session management, and arg parsing. Bolting the Slack receiver onto it would require significant refactoring and would couple crash recovery.

- **Option C (standalone watchdog):** Adds a new component to maintain. Doesn't benefit from the supervisor's status publishing, demotion, or signal handling. Divergent operational patterns.

- **Option D (systemd):** Correctly rejected — no systemd in the container.

**No better alternative exists.** The design is the right approach.

---

## Summary of Required Actions Before Implementation

### Blocking issues (must fix before deploying):

1. **LAUNCHERS entry bug (Section 5.6):** The proposed `"protomega-slack": OMEGA_COMMON + ["/hive/protomega/bin/slack_live_launcher.py"]` will not work because `OMEGA_COMMON` prepends `phase6_private_canary_runner.py`, which is not a wrapper. Fix:
   ```python
   "protomega-slack": ["/usr/bin/python3", "/hive/protomega/bin/slack_live_launcher.py"]
   ```

2. **Secrets file permissions (Section 4.4):** Symlinks to secrets owned by UID 11003 will be unreadable by UID 11005 because `demote()` calls `os.setgroups([])`, stripping group access. **Copy the secrets** to `/hive/protomega-slack/secrets/` with `chown 11005:10001, chmod 0600` instead of symlinking. This means the secrets need manual sync if they change, but for a Slack bot token and Telegram env file, this is acceptable (they rarely change).

3. **Env var in compose.live.yaml (Section 3.2):** Add `SLACK_POLLING_ENABLED: "1"` to the container's environment block. Without this, the activation gate will fail silently and the worker will go idle.

### Advisory issues (should fix but not blocking):

4. **Add parent-death signal handling (Section 5.8):** Port `arm_parent_death_signal()` from `phase6_private_canary_runner.py` to `slack_live_launcher.py` to ensure the receiver dies if its parent (`agent_worker.py`) is killed.

5. **Verify `clean_responder.py` source (Section 1):** Read the actual `/hive/protomega/bin/clean_responder.py` on the VM to confirm it is stateless per-call. The architecture strongly suggests it is, but this should be verified before relying on it.

6. **Update healthcheck (Section 5.1):** If `healthcheck.py` monitors identity statuses, add `protomega-slack` to its check list.

7. **Verify UID 11005 availability (Section 9, Q3):** Run `getent passwd 11005` inside the container. `setuid` will work with any numeric UID, but it's good hygiene to confirm no collision.

---

**Bottom line:** The design is architecturally sound and Option A is the right strategic choice. Three blocking implementation details (LAUNCHERS vector, secrets permissions, compose env var) need fixing before deployment. None of them require rethinking the design — they're concrete fixes to oversights in the implementation plan. Fix those three, follow the testing plan in Section 7, and this will work.
