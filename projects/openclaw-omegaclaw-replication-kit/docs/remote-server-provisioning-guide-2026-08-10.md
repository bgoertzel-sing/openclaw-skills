# Remote Server Provisioning Guide for the ProtoCosmo and ProtoMega Agents

- Date: 2026-08-10
- Audience: the trusted administrator preparing the new remote host
- Scope: ZeroBot/ProtoCosmo, ProtoCosmo2, ProtoMega/Protomega, and later
  ProtoMega-family agent instances
- Companion runbook: `multi-agent-remote-port-runbook-2026-08-10.md`
- Status: operator guide; exact source commits and credentials must be frozen
  at migration time

## 1. Purpose

Prepare a Linux server on which several OpenClaw- and OmegaClaw-based research
agents can be installed, tested, and operated without sharing credentials,
Telegram cursors, writable memory databases, process locks, or mutable runtime
history.

The host is not ready merely because the programs start. Readiness means each
agent can independently receive a fresh externally initiated Telegram event,
run its intended model/tool loop, and deliver the correlated reply to the
originating chat, while the other agents remain isolated.

This guide intentionally does not contain tokens, keys, chat IDs, account
identifiers, or private memory. Those must be installed separately through an
approved secret channel.

## 2. Recommended deployment shape

Use one dedicated Linux VM or bare-metal host with separate runtime cells:

```text
Internet
  |-- outbound HTTPS --> Telegram Bot API
  |-- outbound HTTPS --> approved model APIs and Git remotes
  |-- restricted SSH --> administrator

Host
  |-- OpenClaw gateway(s), bound to loopback only
  |-- zerobot cell
  |-- protocosmo2 cell
  |-- protomega cell
  `-- future protomega cell(s)

Each cell
  |-- unique Unix user or strongly isolated service account
  |-- unique workspace and configuration root
  |-- unique state, session, queue, cursor, attachment and index roots
  |-- unique logs, PID/lock files, backup namespace and service unit
  `-- exactly one Telegram receiver for its bot token
```

Best practice is a separate Unix account per live bot. If that is operationally
impractical, use one unprivileged account with mode-0700 per-agent roots and
strictly separate service units. Do not run agent services as root.

Do not put multiple agents in one writable OpenClaw state directory. Do not
share OmegaClaw Chroma/episode stores. Shared Git repositories should be
read-only or accessed through separate worktrees/branches; shared project
Markdown should have an explicit single writer.

## 3. Capacity planning

### 3.1 API-backed inference profile

A practical initial host for four agents is:

- Linux x86-64;
- 8 modern vCPUs minimum, 16 preferred for concurrent builds/tests;
- 32 GiB RAM minimum, 64 GiB preferred if several Python/Torch/embedding
  processes may overlap;
- 200 GiB fast SSD minimum, 500 GiB preferred for repositories, isolated
  environments, indexes, artifacts, and backup staging;
- no GPU required when model inference is provided through remote APIs;
- stable low-latency network and enough egress quota for model APIs, Git, npm,
  Python packages, and backups.

The initial canary should impose concurrency limits even on a larger server.
Measure peak RSS, disk growth, provider latency, and queue depth before raising
limits.

### 3.2 Local-model profile

Local Ollama or other model inference is optional and should not be silently
mixed into the base migration. Size GPU VRAM, system RAM, storage, drivers, and
model cache only after choosing exact models and concurrency. Treat GPU/cloud
cost and driver installation as a separate approved change.

## 4. Operating system and base security

Recommended baseline:

- a supported Ubuntu/Pop!_OS-family LTS or equivalent Linux distribution;
- full-disk or provider-volume encryption where available;
- automatic security updates or a documented patch cadence;
- NTP/time synchronization and the intended local timezone;
- SSH keys only, no password login, restricted administrator allowlist;
- host firewall denying unsolicited inbound traffic;
- encrypted, tested off-host backups;
- monitoring for disk, memory, process restarts, failed units, and clock drift.

Telegram polling and remote model APIs normally require outbound TCP 443 only.
The OpenClaw Gateway/OpenAI-compatible endpoint must bind to `127.0.0.1` (or a
private Unix socket) and must not be exposed to the public Internet. If remote
administration needs a web/status endpoint, use SSH forwarding or a reviewed
private overlay such as Tailscale, with authentication and an explicit
allowlist.

The administrator should record:

- provider, region, instance/host identifier, CPU, RAM, disks, encryption and
  backup policy;
- OS release, kernel, architecture, timezone and NTP status;
- firewall and listening-port inventory;
- administrator and service-account ownership;
- restore and host-rebuild procedure.

## 5. Required system software

Start from the versions pinned in the migration manifest. The following is the
known reference family, not permission to substitute untested latest versions:

| Component | Required/reference | Purpose |
|---|---|---|
| Git | current supported; reference 2.34.1 | repositories and provenance |
| Node.js | 22.19+; Node 24 preferred/reference | OpenClaw runtime |
| npm | version compatible with pinned Node | OpenClaw/plugins |
| OpenClaw | freeze the currently deployed release; observed source host 2026.7.1 | gateway, tools, channels, schedules |
| Python | 3.10+ with `venv` and headers; pin exact minor | OmegaClaw, adapters, tests |
| SWI-Prolog | 9.3+ with Janus/Python; reference 9.3.36 | PeTTa/OmegaClaw |
| PeTTa | pin exact reviewed commit | MeTTa runtime |
| OmegaClaw-Core | pin each deployed branch/commit | ProtoCosmo2/Protomega loops |
| Bash/coreutils | distro-supported | supervisors and verification |

Install or make available:

```text
git curl ca-certificates build-essential pkg-config
python3 python3-venv python3-dev
jq rsync unzip zip tar xz-utils
sqlite3
flock timeout sha256sum awk sed grep
```

Useful operator tools:

```text
openssh-client tmux ripgrep fd-find yq gh lsof strace
```

Example Ubuntu-family package installation, to be reviewed and run by the
administrator:

```bash
sudo apt update
sudo apt install --no-install-recommends \
  git curl ca-certificates build-essential pkg-config \
  python3 python3-venv python3-dev \
  jq rsync unzip zip tar xz-utils sqlite3 \
  tmux ripgrep fd-find lsof
```

The distribution SWI-Prolog package may be too old or lack a working Janus
build. Use an official package or a source build of the frozen SWI release only
after reviewing provenance and build instructions. Do not install unreviewed
`curl | sh` scripts.

Verify and save output:

```bash
uname -a
cat /etc/os-release
node --version
npm --version
python3 --version
git --version
swipl --version
```

Also verify SWI libraries required by the current stack (historically `janus`,
`process`, `filesex`, `pcre`, and `uuid`) and the Python imports declared by the
pinned repositories. Do not infer compatibility from version strings alone.

## 6. Accounts and directory layout

Create an administrator-controlled top-level location, then one private tree
per agent. Example only:

```text
/srv/proto-agents/
  releases/                 # immutable, versioned source releases
  shared-readonly/          # optional reviewed immutable corpora
  zerobot/
    workspace config state sessions queues attachments indexes logs run backups
  protocosmo2/
    workspace config state sessions queues attachments indexes logs run backups
  protomega/
    workspace config state sessions queues attachments indexes logs run backups
  staging/
    zerobot ...             # never points at production mutable roots
```

Requirements:

- agent roots and secret directories: mode `0700`;
- secret files: mode `0600`, owned by the corresponding service account;
- logs must omit secret values and prompt bodies unless explicitly required;
- release directories should be immutable to service accounts after install;
- production and staging must not share history, queues, offsets, databases,
  attachments, vector stores, logs, PID files, or backup destinations;
- each service has a unique working directory, environment file, unit name,
  restart policy, resource limits, and shutdown timeout.

Keep repository checkouts and Python/Node environments pinned per release.
Avoid a single mutable global virtual environment.

## 7. Credentials and external prerequisites

The administrator and Ben must arrange, outside this document:

- one unique Telegram bot token per agent identity;
- the approved bot usernames and human/group chat IDs;
- Telegram group membership, privacy/read settings, and Bot API bot-to-bot
  configuration where required;
- model-provider credentials and route names;
- a separate OpenClaw Gateway authentication token per trust boundary;
- GitHub access only where private repositories require it;
- optional backup-encryption keys stored outside the host.

Never copy credentials from Telegram transcripts, shell history, repository
files, old logs, `~/.openclaw`, or an archive. Prefer newly issued/rotated
credentials on the new host. Inject them through the platform secret store,
systemd credentials, or protected environment files. Record only key names,
owners, permissions, rotation dates, and successful identity probes—not secret
values.

Before enabling Telegram polling, resolve which host owns each token. One bot
token must have exactly one live `getUpdates` consumer.

## 8. OpenClaw installation requirements

For each OpenClaw runtime:

1. Install the exact frozen OpenClaw version under the intended Node version.
2. Create a clean workspace from reviewed templates; do not copy the old
   `~/.openclaw` tree.
3. Install only the inventoried skills/plugins and pin their source/digests.
4. Merge reviewed configuration into generated defaults; do not overwrite
   unknown working settings wholesale.
5. Configure provider and channel secrets through SecretRefs/protected files.
6. Bind Gateway interfaces to loopback.
7. Give each instance separate config/state/session/log roots and ports.
8. Validate config, secrets, plugins, skills, gateway, and channel probes before
   importing personal memory or enabling live traffic.

Representative checks (adapt to the frozen release's CLI):

```bash
openclaw config validate
openclaw secrets audit
openclaw skills check
openclaw plugins doctor
openclaw gateway status
openclaw channels status --probe
openclaw cron list --json
```

Do not install schedules until the agent passes its private and group canaries.

## 9. OmegaClaw/PeTTa installation requirements

For each OmegaClaw-based bot:

1. Clone PeTTa and OmegaClaw-Core at the exact manifest commits.
2. Review and apply only the required maintained overlay/patches.
3. Create a dedicated Python virtual environment and install the pinned
   requirements.
4. Point the `OpenClaw` provider to a loopback Gateway endpoint, historically:

   ```text
   OPENCLAW_GATEWAY_BASE_URL=http://127.0.0.1:<unique-port>/v1
   OPENCLAW_MODEL=openclaw/default
   OPENCLAW_SESSION_PER_CALL=true
   ```

5. Supply the gateway token through protected runtime configuration.
6. Allocate separate OmegaClaw memory, Chroma, episode, Telegram offset,
   outbox, lock, log and artifact paths for every instance.
7. Use the current outer Telegram transport/contract implementation associated
   with the frozen agent commit; the 2026-07 replication-kit patch is useful
   provenance but must not overwrite newer reviewed runtime work.
8. Disable legacy MTProto/Telethon receive bridges unless a new architecture
   explicitly requires and reviews them.

Expected per-token topology:

```text
Telegram Bot API long poll -> one outer transport -> one agent loop
MTProto receive bridges: 0
competing Bot API pollers: 0
```

Run repository-focused tests, PeTTa smoke tests, compiler checks, and the
provider-free transport suite before any live token is installed.

## 10. Service supervision

Use one owning supervisor per service—preferably systemd user or system units
with `User=` set to the unprivileged agent account. Do not stack systemd,
cron, shell supervisors, and watchdog restart actions over the same process.

Each unit should define:

- explicit executable and working directory;
- protected environment/credential source;
- unique state/runtime directories;
- bounded restart backoff and start-limit behavior;
- graceful stop timeout followed by bounded termination;
- conservative file permissions/umask;
- CPU, memory, process and file-descriptor limits appropriate to the workload;
- logging destination and rotation policy;
- dependency ordering for the loopback Gateway where applicable.

Readiness has two levels:

1. process topology: exactly the intended workers/listeners are alive;
2. end-to-end readiness: a fresh external event is correlated through ingress,
   agent/provider/action, Telegram delivery receipt, and visible destination.

## 11. Backup and restore

Maintain two classes of backup:

1. **Sanitized recovery skeleton:** policies, identities, skills, templates,
   catalogs, project Markdown, manifests, and install scripts; excludes secrets,
   raw sessions, caches, runtime databases, logs, and model weights.
2. **Encrypted private state backup:** explicitly selected repositories,
   artifacts, memory stores, and databases, with access control and retention.

Back up each agent independently. A backup is not accepted until restored into
a disposable isolated root and checked for manifest integrity and basic
readability. Never restore a Telegram cursor or live queue blindly while the old
receiver is active.

## 12. Host provisioning acceptance checklist

The host is ready for migration only when all applicable items are recorded:

- [ ] OS, kernel, architecture, time sync, firewall and listening ports audited.
- [ ] CPU/RAM/disk capacity and monitoring configured.
- [ ] Dedicated unprivileged runtime identities and private directory roots exist.
- [ ] Production and staging mutable paths are demonstrably distinct.
- [ ] Git, Node/npm, Python/venv, SWI/Janus and operator tools pass version/smoke checks.
- [ ] Pinned OpenClaw, PeTTa and OmegaClaw sources can be installed without secrets.
- [ ] Gateway endpoints bind only to loopback/private sockets.
- [ ] One service unit and one receiver ownership record exists per bot token.
- [ ] Secret injection, rotation and revocation procedures are agreed.
- [ ] Off-host encrypted backup and disposable restore test pass.
- [ ] Provider-free tests pass before live credentials are installed.
- [ ] No agent schedules or autonomous paid compute are enabled.
- [ ] A rollback host/commit/config/state snapshot is identified.

## 13. What the administrator should hand back

Provide a non-secret provisioning record containing:

- host specification and OS/package versions;
- service accounts, directory map and permissions;
- source repositories, commits, patch digests and dirty-state notes;
- non-secret effective configuration and loopback port allocation;
- unit-file names and process topology;
- exact test commands, outputs and exit codes;
- secret key names/owners/permissions (never values);
- backup/restore test result;
- open discrepancies and rollback target.

That record becomes the input to the staged port runbook. It is not yet
authorization to transfer production identities or start live Telegram polling.

