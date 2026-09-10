# Design: Wire Protomega Slack Receiver into Hive Supervisor

**Status:** Draft for review — no changes to VM2 made under this design.
**Author:** ZeroBot (ProtoCosmo/Pop!_OS)
**Date:** 2026-09-01
**Reviewers:** Frontier model (Claude Fable or GPT-5.6-Sol), ProtoCosmo, Fixit Bunny

---

## 1. Problem Statement

The Protomega Slack receiver (`slack_live_launcher.py`) is currently running as a
detached `docker exec -d` process inside the proto-hive container. It works — two
consecutive successful canaries — but it has no crash recovery, no container-restart
survival, and no supervisor visibility. If the process dies, Slack goes silent until
someone manually restarts it.

Ben has authorized persistent Slack operation and requested a systematic design for
wiring it into the existing `hive_supervisor.py` restart loop, with review before any
changes are made.

## 2. Current Architecture (Observed)

### 2.1 hive_supervisor.py (42 lines, verbatim)

```python
IDENTITIES = {"protocosmo": 11001, "protocosmo2": 11002,
              "protomega": 11003, "protomega2": 11004}
# ...
def start(identity, uid):
    return subprocess.Popen(
        [sys.executable, "/opt/proto-hive/bin/agent_worker.py",
         "--identity", identity, "--mode", mode],
        preexec_fn=demote(uid))

# Main loop:
# - Spawns one agent_worker.py per identity
# - Restarts any agent_worker that exits (after 2s sleep)
# - SIGTERM/SIGINT → graceful stop of all children
```

**Key properties:**
- One process per identity, managed by a single supervisor loop.
- Automatic restart on crash (exit code ≠ None → sleep 2s → respawn).
- No exponential backoff, no max-retry limit, no alerting.
- Children run as demoted UIDs (setgroups→setgid→setuid→umask 077).

### 2.2 agent_worker.py (119 lines, verbatim)

Contains a `LAUNCHERS` dict mapping each identity to a command vector:

| Identity | UID | Launcher | Transport |
|---|---|---|---|
| protocosmo | 11001 | OpenClaw gateway node | Telegram |
| protocosmo2 | 11002 | protocosmo2_v2_live.py | Telegram |
| protomega | 11003 | phase6_private_canary_runner.py | Telegram |
| protomega2 | 11004 | phase6_private_canary_runner.py | Telegram |

**Activation gate:** An identity goes "live" only when all three conditions hold:
1. `--mode live` argument
2. `TELEGRAM_POLLING_ENABLED=1` in environment
3. `/hive/<identity>/activation/ENABLE-POLLING` marker file exists

If not activated, the worker publishes status `"idle"` and sleeps forever
(`while True: time.sleep(30)`). This is a safety feature — the supervisor can
be running but individual identities stay dormant until explicitly activated.

**Environment setup (non-protocosmo identities):**
```python
env["CHROMA_DB_PATH"] = str(root / "state" / "chroma_db")
env["OPENCLAW_DIST"] = "/opt/proto-hive/openclaw/dist"
```

**Status publishing:** Writes `"idle"` or `"active"` to
`/run/proto-hive/status/<identity>` (mode 0644, owned by the identity UID).

### 2.3 slack_live_launcher.py (the receiver, ~150 lines)

Currently runs as a standalone process. Key characteristics:

- **Paths:** `BIN=/hive/protomega/bin`, `STATE_DIR=/hive/protomega/state/slack-v2`,
  `SLACK_ENV=/hive/protomega/secrets/omegaclaw-slack.env`,
  `PROVIDER_ENV=/hive/protomega/secrets/omegaclaw-telegram.env`
- **Provider:** Calls `clean_responder.responder(text, provider_args, "slack-v2-live")`
  — the same clean provider handoff used for Telegram, just with a different source tag.
- **Safety gates:**
  1. Allowlist: only `SLACK_ALLOW_FROM` user IDs are ingested
  2. Bot filter: bot-authored messages (self or others) are dropped
  3. Cursor priming: on startup, cursor is set to `now` — backlog is never processed
  4. Ownership lock: `TokenOwnership(LOCK_FILE)` prevents concurrent instances
  5. Bounded runtime: `SLACK_LIVE_RUNTIME` env var (default 1800s = 30 min)
- **Signal handling:** SIGTERM/SIGINT → clean shutdown (state.close, exit 0)
- **Poll loop:** poll_once → respond_once (drain) → deliver_once (drain) → sleep

## 3. Design Options Considered

### Option A: New supervised identity "protomega-slack" (RECOMMENDED)

Add a fifth identity `protomega-slack` (UID 11005) to both `hive_supervisor.py`
and `agent_worker.py`. The supervisor's existing restart loop manages it. The
Slack receiver runs as its own process, fully decoupled from the protomega
Telegram poller.

**Pros:**
- Minimal, purely additive change to existing code (new dict entries, no logic changes)
- Crash of Slack receiver cannot affect protomega's Telegram path (different process)
- Supervisor's restart loop is already battle-tested
- Status publishing works out of the box (`/run/proto-hive/status/protomega-slack`)
- Activation gate prevents accidental startup during maintenance

**Cons:**
- Requires new `/hive/protomega-slack/{config,state,secrets}` directory tree
- One more process for the supervisor to manage

### Option B: Co-spawn inside existing protomega agent_worker

Have `agent_worker.py` launch both the Telegram poller and the Slack receiver
as child processes when `--identity protomega` is used.

**Pros:** No new identity, no new dirs.

**Cons:** Coupling — if Slack crashes and the worker exits, Telegram also
restarts (and vice versa). The agent_worker.py would need significant
modification to track two children. Higher blast radius.

### Option C: Standalone watchdog (no supervisor integration)

A separate lightweight watchdog process (cron, systemd, or custom script)
that monitors and restarts the Slack receiver independently.

**Pros:** Zero changes to supervisor/agent_worker.

**Cons:** Adds a new component to maintain. Doesn't benefit from the
supervisor's existing health-check and status infrastructure. Divergent
operational patterns.

### Option D: systemd unit inside the container

Wrap the Slack receiver in a systemd service.

**Cons:** proto-hive container doesn't run systemd (PID 1 is the supervisor).
Would require adding systemd to the container, which is a large and risky
change. Rejected.

**Decision: Option A.** It's the lowest-risk change that achieves the goal.
The rest of this document details the implementation.

## 4. Detailed Implementation (Option A)

### 4.1 New identity: "protomega-slack" (UID 11005)

#### 4.1.1 Directory tree

Create inside the proto-hive container:

```
/hive/protomega-slack/
├── activation/
│   └── ENABLE-SLACK          # marker file (empty, mode 0644)
├── config/
│   └── openclaw.json          # minimal config (can be symlink to protomega's)
├── secrets/
│   ├── omegaclaw-slack.env    # symlink → /hive/protomega/secrets/omegaclaw-slack.env
│   └── omegaclaw-telegram.env # symlink → /hive/protomega/secrets/omegaclaw-telegram.env
└── state/
    └── slack-v2/              # symlink → /hive/protomega/state/slack-v2/
                              # (preserves cursor continuity — critical)
```

**Why symlinks for secrets and state?** The Slack env file, provider env file,
and the durable SQLite state all belong to protomega. Using symlinks avoids
duplicating secrets and preserves the cursor/database across the identity
boundary. The `state/slack-v2` symlink is especially important — it ensures
the cursor and ownership lock file are shared, preventing a race condition
where two instances could start with different state dirs.

**Ownership:** `chown -R 11005:10001 /hive/protomega-slack/` with `umask 077`.

#### 4.1.2 Changes to hive_supervisor.py

One line added to the `IDENTITIES` dict:

```python
IDENTITIES = {
    "protocosmo": 11001,
    "protocosmo2": 11002,
    "protomega": 11003,
    "protomega2": 11004,
    "protomega-slack": 11005,   # NEW
}
```

No other changes to the supervisor. The restart loop, signal handling,
and demotion logic are unchanged.

#### 4.1.3 Changes to agent_worker.py

Add a LAUNCHERS entry and an activation gate:

```python
LAUNCHERS = {
    # ... existing entries unchanged ...
    "protomega-slack": OMEGA_COMMON + [
        "/hive/protomega/bin/slack_live_launcher.py",
    ],
}
```

The activation gate needs a Slack-specific variant. Currently:

```python
marker = root / "activation" / "ENABLE-POLLING"
activated = args.mode == "live" \
    and os.environ.get("TELEGRAM_POLLING_ENABLED") == "1" \
    and marker.is_file()
```

Add a parallel check for Slack:

```python
if args.identity == "protomega-slack":
    marker = root / "activation" / "ENABLE-SLACK"
    activated = args.mode == "live" \
        and os.environ.get("SLACK_POLLING_ENABLED") == "1" \
        and marker.is_file()
```

This must be inserted **before** the existing activation check, or the
existing check must be generalized to handle both activation types. The
cleanest approach is to compute `activated` per-identity:

```python
if args.identity == "protomega-slack":
    marker = root / "activation" / "ENABLE-SLACK"
    activated = args.mode == "live" \
        and os.environ.get("SLACK_POLLING_ENABLED") == "1" \
        and marker.is_file()
else:
    marker = root / "activation" / "ENABLE-POLLING"
    activated = args.mode == "live" \
        and os.environ.get("TELEGRAM_POLLING_ENABLED") == "1" \
        and marker.is_file()
```

Everything else in agent_worker.py (env setup, status publishing,
require_stable_child, the final subprocess.call) works unchanged.

#### 4.1.4 Changes to slack_live_launcher.py

Two changes:

**1. Remove the bounded runtime default (make unbounded by default):**

```python
# Before:
RUNTIME_SECONDS = int(os.environ.get("SLACK_LIVE_RUNTIME", "1800"))
# ...
while time.time() - start_time < RUNTIME_SECONDS:

# After:
RUNTIME_SECONDS = int(os.environ.get("SLACK_LIVE_RUNTIME", "0"))
# ...
while RUNTIME_SECONDS == 0 or time.time() - start_time < RUNTIME_SECONDS:
```

`SLACK_LIVE_RUNTIME=0` means unbounded (supervisor manages lifecycle).
Canary testing can still set `SLACK_LIVE_RUNTIME=1800` for a bounded window.

**2. Remove `OPENCLAW_DIST` setdefault** (agent_worker.py already sets it):

```python
# This line can be removed since agent_worker.py sets it for non-protocosmo
# identities. Keeping it as setdefault is harmless (won't override), so this
# is optional cleanup, not a functional change.
os.environ.setdefault("OPENCLAW_DIST", "/opt/proto-hive/openclaw/dist")
```

**No other changes to the launcher.** The safety gates (allowlist, bot filter,
cursor priming, ownership lock, signal handling) remain exactly as-is.

### 4.2 What does NOT change

- `hive_supervisor.py` restart loop logic — unchanged
- `hive_supervisor.py` signal handling — unchanged
- `agent_worker.py` env setup for existing identities — unchanged
- `agent_worker.py` status publishing — unchanged (just works for the new identity)
- `slack_live_launcher.py` safety gates — unchanged
- `slack_live_launcher.py` provider handoff — unchanged
- All Telegram paths — completely untouched
- protomega's own agent_worker entry — unchanged

### 4.3 Concurrent provider access

Both the protomega Telegram poller (UID 11003) and the Slack receiver
(UID 11005) call `clean_responder.responder()`. Questions to verify during
review:

1. Is `clean_responder.responder()` thread-safe / reentrant across processes?
   It should be stateless per-call (each call is a fresh provider invocation),
   but this needs verification by inspecting `clean_responder.py`.
2. Is there a shared resource (file, socket, lock) that both paths contend on?
3. If both a Telegram message and a Slack message arrive simultaneously, do
   they get independent provider sessions, or is there serialization?

**Mitigation if not safe:** Add a process-level lock in `clean_responder.py`
or use different session prefixes. But this is likely a non-issue since the
provider handoff is designed to be per-call stateless.

## 5. Activation / Deactivation Procedure

### 5.1 First activation (after code changes are deployed)

1. **Stop the current detached receiver** (SIGTERM the existing process).
2. **Deploy the code changes** to `/opt/proto-hive/bin/agent_worker.py` and
   `/hive/protomega/bin/slack_live_launcher.py` inside the container.
3. **Create the directory tree** (Section 4.1.1).
4. **Create the marker file:** `touch /hive/protomega-slack/activation/ENABLE-SLACK`
5. **Restart the supervisor** with `SLACK_POLLING_ENABLED=1` in the environment:
   - This env var must be set in the supervisor's environment (e.g., in the
     systemd unit or whatever starts `hive_supervisor.py`).
   - Alternatively, set it in `/hive/protomega-slack/config/` and have
     agent_worker.py source it. (This needs design — see Open Questions.)
6. **Verify:** Check `/run/proto-hive/status/protomega-slack` shows `active`.
   Check the log for `[SLACK-LIVE] Ready for canary (real provider)`.
7. **Canary:** Ben sends a test message. Confirm `polled=1 responded=1 delivered=1`.

### 5.2 Deactivation (emergency rollback)

1. `rm /hive/protomega-slack/activation/ENABLE-SLACK`
2. SIGTERM the protomega-slack worker process (supervisor will restart it,
   but it will go idle because the marker is gone).
3. Alternatively, remove `"protomega-slack"` from IDENTITIES temporarily
   (requires supervisor restart).

### 5.3 Supervisor restart safety

When the supervisor restarts (e.g., container reboot):

1. It spawns all five agent_worker processes.
2. protomega-slack's agent_worker checks activation gate.
3. If `SLACK_POLLING_ENABLED=1` and marker exists → starts receiver.
4. Receiver primes cursor (backlog ignored) → ready for new messages.
5. If activation gate is not met → goes idle, no Slack polling.

This is safe: a supervisor crash + restart does not cause backlog processing.

## 6. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Breaking existing Telegram paths during code edit | Low (additive change) | High | No logic changes to existing identity entries; review diff line-by-line |
| Concurrent provider access conflict | Low (stateless design) | Medium | Verify clean_responder.py; add lock if needed |
| Slack receiver crash loop (e.g., bad env file) | Medium | Low | Supervisor restarts; cursor priming prevents backlog; status shows crash pattern |
| Supervisor can't pass SLACK_POLLING_ENABLED env | Medium | Medium | Need to verify how supervisor gets its env (systemd? docker?) — see Open Questions |
| State dir symlink breaks cursor continuity | Low | Medium | Use `readlink -f` verification before first activation |
| Ownership lock stale after crash | Low | Low | TokenOwnership uses fcntl/flock — released automatically on process death |

## 7. Testing Plan

### 7.1 Pre-deployment (offline / dry-run)

1. **Diff review:** All changes are additive to dicts + one new if-branch. Verify
   no existing line is modified except the two new entries.
2. **Directory tree validation:** Create the tree, verify symlinks resolve,
   verify permissions (uid 11005, mode 0700).
3. **Launcher dry-run:** Run `slack_live_launcher.py` with `SLACK_LIVE_RUNTIME=1`
   to verify it starts, primes cursor, and exits cleanly within 1 second.
4. **Agent_worker dry-run:** Run `agent_worker.py --identity protomega-slack --mode offline`
   and verify it publishes "idle" without starting the receiver.

### 7.2 Deployment (canary)

1. Stop the current detached receiver.
2. Deploy changes.
3. Activate with marker + env var.
4. Restart supervisor (or just the protomega-slack worker).
5. Ben sends a canary message.
6. Verify: exactly one reply, log shows `polled=1 responded=1 delivered=1`,
   status shows `active`.
7. Wait 5 minutes, send a second message — verifies the process is stable
   and not just working on first launch.

### 7.3 Crash recovery test

1. After canary success, `kill -9` the slack_live_launcher process.
2. Verify supervisor restarts it within ~3 seconds.
3. Verify cursor priming prevents backlog processing.
4. Send another message — verify it's handled by the restarted process.

### 7.4 Channel isolation test

1. While Slack receiver is active, send a Telegram message to ProtomegaTron.
2. Verify Telegram reply is delivered (no interference).
3. Send a Slack message.
4. Verify Slack reply is delivered.
5. Confirm no cross-channel leakage.

## 8. Rollback Plan

If anything goes wrong:

1. `rm /hive/protomega-slack/activation/ENABLE-SLACK` → receiver goes idle.
2. Remove `"protomega-slack": 11005` from IDENTITIES in hive_supervisor.py.
3. Restart supervisor (only the affected identity is removed; others continue).
4. Start the detached receiver manually (the old approach) as a fallback:
   ```
   docker exec -d -u 11003 proto-hive sh -c \
     "SLACK_LIVE_RUNTIME=2592000 python3 /hive/protomega/bin/slack_live_launcher.py"
   ```
5. No data loss — the state dir and cursor are untouched.

## 9. Open Questions (for reviewers)

1. **Supervisor environment:** How does `hive_supervisor.py` receive its
   environment variables? Is it started by Docker, systemd, or a script?
   The `SLACK_POLLING_ENABLED=1` env var needs to reach the supervisor process.
   If it's a Docker container, it may need to be added to the container's env
   or to the supervisor's startup script. **Action:** Inspect how the container
   is started (`docker inspect proto-hive` or the host systemd unit).

2. **clean_responder.py thread safety:** Is `responder(text, provider_args, tag)`
   safe for concurrent calls from two processes? Need to read the source.

3. **UID allocation:** Is 11005 the correct next UID? Verify no collision with
   any existing UID inside the container (`getent passwd` in the container).

4. **Log persistence:** Currently logging to `/hive/protomega/state/slack-v2/`
   via the launcher's stdout. Should the supervisor-managed instance log to a
   different location? Or is the current path fine (appended via stdout redirect)?

5. **Marker file lifecycle:** The `ENABLE-SLACK` marker should persist across
   container restarts (it lives in the mounted volume). Verify that
   `/hive/protomega-slack/activation/` is on the persistent volume, not an
   ephemeral container filesystem.

6. **Health check integration:** The supervisor publishes status to
   `/run/proto-hive/status/<identity>`. Is there a health-check script that
   monitors these? Should it be updated to include `protomega-slack`?

## 10. Implementation Order (after review approval)

1. **Read-only:** Verify open questions (supervisor env, clean_responder source,
   UID availability, volume persistence).
2. **Create directory tree** inside container (no code changes yet).
3. **Edit agent_worker.py** — add LAUNCHERS entry + activation branch.
4. **Edit slack_live_launcher.py** — change default runtime to 0 (unbounded).
5. **Edit hive_supervisor.py** — add IDENTITIES entry.
6. **Stop current detached receiver.**
7. **Create marker file.**
8. **Restart supervisor** (or send SIGHUP if it supports reload — it doesn't,
   so full restart of the supervisor process).
9. **Canary test** (Section 7.2).
10. **Crash recovery test** (Section 7.3).
11. **Channel isolation test** (Section 7.4).
12. **Update project records** with evidence.

**Estimated time:** 30-45 minutes for steps 1-8, 15 minutes for tests.

---

## Appendix A: Source code references (verbatim, as observed 2026-09-01)

### hive_supervisor.py (complete, 42 lines)

```python
#!/usr/bin/env python3
import os, signal, subprocess, sys, time
from pathlib import Path

IDENTITIES = {"protocosmo": 11001, "protocosmo2": 11002,
              "protomega": 11003, "protomega2": 11004}
mode = sys.argv[1]
runtime = Path("/run/proto-hive")
(runtime / "status").mkdir(parents=True, exist_ok=True)
(runtime / "status").chmod(0o733)
children = {}
stopping = False

def demote(uid):
    def apply():
        os.setgroups([]); os.setgid(10001); os.setuid(uid); os.umask(0o077)
    return apply

def start(identity, uid):
    return subprocess.Popen(
        [sys.executable, "/opt/proto-hive/bin/agent_worker.py",
         "--identity", identity, "--mode", mode],
        preexec_fn=demote(uid))

def stop(_signum, _frame):
    global stopping
    stopping = True
    for child in children.values():
        if child.poll() is None: child.terminate()

signal.signal(signal.SIGTERM, stop)
signal.signal(signal.SIGINT, stop)
for identity, uid in IDENTITIES.items():
    children[identity] = start(identity, uid)
while not stopping:
    for identity, child in list(children.items()):
        code = child.poll()
        if code is not None:
            time.sleep(2)
            children[identity] = start(identity, IDENTITIES[identity])
    time.sleep(1)
for child in children.values():
    try: child.wait(timeout=10)
    except subprocess.TimeoutExpired: child.kill()
```

### agent_worker.py (relevant sections)

See Section 2.2 for the full file. The key sections for this design:
- LAUNCHERS dict (lines ~12-46)
- Activation gate (lines ~86-89)
- Env setup for non-protocosmo identities (lines ~92-107)
- Status publishing (lines ~62-70)

### slack_live_launcher.py

See Section 2.3 for the full file. Key sections:
- Runtime bound (line 28: `RUNTIME_SECONDS = int(os.environ.get("SLACK_LIVE_RUNTIME", "1800"))`)
- Main loop (line ~115: `while time.time() - start_time < RUNTIME_SECONDS:`)
- Safety gates: allowlist (lines ~96-103), bot filter (in protomega_slack_runner_v2.py),
  cursor priming (line ~109), ownership lock (line ~106), signal handling (lines ~98-101)
