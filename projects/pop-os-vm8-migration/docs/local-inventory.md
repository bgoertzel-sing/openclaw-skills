# Local proto-hive inventory

- Captured: `2026-08-12 16:44-16:48 PDT`
- Host: Pop!_OS laptop, user `openclaw`
- Method: read-only `ps`, `systemctl`, `jq` key selection, `stat`, `du`, `git`,
  `ss`, and `crontab` inspection. Secret values were not read or recorded.
- Status: production laptop remains authoritative. No receiver was stopped,
  restarted, or reconfigured during this inventory.

## Receiver topology

| Identity | Receiver and PID | Owning supervisor | Credential reference | Separate mutable state |
|---|---|---|---|---|
| ProtoCosmo / ZeroBot | `openclaw-gateway`, PID `3412314`, parent PID 1 | system unit `openclaw-agent.service`; `Restart=always` | OpenClaw secret reference `/channels/telegram/botToken` | `/home/openclaw/.openclaw/` (21 GiB total; broad tree includes unrelated runtime state and must not be bulk-copied) |
| ProtoCosmo2 | `phase6_private_canary_runner.py`, PID `3479126`, parent shell `3479113` | `projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh` with per-launch overrides | `/home/openclaw/.openclaw/protocosmo2.env` (mode 0600; value not inspected) | `/home/openclaw/.openclaw/protocosmo2-canary-state` (328 KiB), `/home/openclaw/.openclaw/protocosmo2-worker-state` (180 KiB) |
| ProtoMega / Protomega | `phase6_private_canary_runner.py`, PID `3479355`, parent shell `3479342` | `projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh` defaults | `/home/openclaw/.openclaw/omegaclaw-telegram.env` (mode 0600; value not inspected) | `/home/openclaw/.openclaw/protomega-outer-state` (236 KiB), `projects/omegaclaw/local/protomega-worker-state` (104 KiB) |
| ProtoMega2 / Protomega2 | `phase6_private_canary_runner.py`, PID `3436822`, parent shell `3436815` | `projects/omegaclaw/local/protomega2-outer-telegram-supervisor.sh` | `/home/openclaw/.openclaw/protomegabot2.env` (mode 0600; value not inspected) | `/home/openclaw/.openclaw/protomega2-outer-state` (156 KiB), `projects/omegaclaw/local/protomega2-worker-state` (100 KiB) |

The two processes whose parent command names contain `protomega-outer` are not
duplicate receivers for one identity: their runner arguments identify distinct
bot IDs, usernames, environment files, configs, state roots, and identities
(ProtoCosmo2 versus Protomega). At capture time, the process table showed one
receiver for each intended identity.

## Code and dependency pins

| Tree | Observed HEAD | Dirty entries | Use |
|---|---|---:|---|
| `projects/omegaclaw` | `42c0461b41d9f9d382c966b982a94249040b529c` | 1000 | shared notebook/runtime tree; dirty and unsuitable as an implicit deployment pin |
| `projects/omegaclaw/repos/PeTTa` | `4ce1d0ea58855abb772b911278312c8846e5cc08` | 7 | Protomega and Protomega2 PeTTa runtime |
| `projects/omegaclaw/worktrees/protocosmo2-phase6-live` | `f6cec1e25bc40b0ebead6fc8f40e89818119ff3c` | 0 | clean transport core used by all three Omega receivers; ProtoCosmo2 also uses it as core |
| `projects/protomegabot2` | `32ca916d6bdc29373e5a379972cda7a5eed275e8` | 29 | ProtoMega2 project checkout; not the observed live runner core |

Observed runtime dependencies include Python 3, Bash, SWI-Prolog/PeTTa, the
OmegaClaw core, and the OpenClaw Node gateway. The exact install manifest is
not yet frozen; deployment must use reviewed clean commits or a checksummed
file manifest, not the dirty `projects/omegaclaw` tree wholesale.

## Non-secret configuration and routing

- OpenClaw Telegram is enabled with allowlist DM and group policies. Its system
  service listens on loopback TCP 18789 and 42795.
- ProtoCosmo2 config identity is `ProtoCosmo2`; its allowed destinations are
  the owner DM and one group.
- Protomega config identity is `ProtomegaTron`; its allowed destinations are
  the owner DM and six groups.
- Protomega2 config identity is `ProtoMegaBot2`; its allowed destinations are
  the owner DM and one group.
- No proto-hive entries were returned by the inspected user crontab. The
  OpenClaw system service is the only installed proto-hive systemd unit found;
  the three Omega receivers are shell-supervised processes.

## Staging and rollback boundary

Safe staging may copy reviewed code, identity/policy documents, and dependency
manifests. It must exclude credential files, Telegram polling, cursor/state
directories, sessions, attachments, logs, PID/lock files, Chroma/vector stores,
and the broad 21 GiB OpenClaw mutable tree. Each VM staging launcher must start
with Telegram polling disabled and fresh, VM-local mock state.

Laptop rollback owners are `openclaw-agent.service` for ProtoCosmo and the two
Omega supervisor scripts above for the other three identities. Their current
processes and mutable state remain intact. Before each eventual cutover, capture
a final per-identity cursor/state backup and stop exactly that identity's laptop
receiver through its owning supervisor; never start the VM receiver first.

## Remaining inventory gaps

- Freeze a minimal, checksummed deployment manifest from clean source commits.
- Enumerate package versions and model/provider secret *names* needed per VM.
- Assign the two identities per VM and write disabled systemd staging units.
- Verify rollback start/status commands for each shell supervisor without
  disturbing the live receivers.
