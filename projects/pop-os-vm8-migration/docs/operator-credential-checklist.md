# Operator credential and integration checklist

- Updated: 2026-08-12
- Scope: Docker Compose deployment of the four proto-hive identities to ASI
  replacement VM1 and VM2.
- Audience: Elija / migration operator.
- Safety: this file lists credential names and destinations only. Never enter
  secret values in this file, Git, Compose YAML, an image layer, or group chat.

This is the current verified inventory. Most live bot credentials and state are
being transferred as a bounded migration delta, so they should **not** need to
be typed again. The operator should manually establish only the items marked
`manual` or `confirm` below.

## Quick checklist

| Item | Target | Action | Required before |
|---|---|---|---|
| VM SSH access/private key | VM1 and VM2 host | `confirm`; retain outside containers | Host administration |
| ASI inference bearer token | One token/profile per VM | `manual` secret injection | Provider-backed smoke |
| ProtoCosmo Telegram bot token | VM1 | `copy/confirm` from bounded OpenClaw export | ProtoCosmo cutover |
| ProtoCosmo2 Telegram bot token | VM1 | `copy`; already present in staged delta | ProtoCosmo2 cutover |
| Protomega Telegram bot token | VM2 | `copy` from laptop secret file | Protomega cutover |
| Protomega2 Telegram bot token | VM2 | `copy` from laptop secret file | Protomega2 cutover |
| Telegram API ID/hash | VM2, Protomega only | `copy if MTProto is enabled`; otherwise retain but unused | MTProto transport only |
| OpenClaw gateway token | Internal runtime secret | `copy/derive`; never expose publicly | Omega-to-OpenClaw calls |
| OpenAI/Codex/provider auth profiles | VM1/VM2 as assigned | `confirm` in bounded ProtoCosmo export and provider configuration | Model canaries |
| Telegram allowed chats/users and policy JSON | Per identity | `copy/verify`; configuration, not secret | Receiver start |
| GitHub/`gh` authentication | Hosts | Elija handles separately; not on migration critical path | Repository administration only |

## Host and ASI credentials

### VM1 and VM2 SSH

- Keep each SSH private key on the administrator workstation or approved secret
  store, mode `0600`.
- Do not mount SSH private keys into the OpenClaw containers unless a specific
  agent capability later requires outbound SSH.
- The servers already contain the corresponding public authorization; this is
  a host-access prerequisite, not an application secret.
- Verify without printing key material: connect to each expected host and run
  `hostname` plus a read-only container/service status command.

### ASI inference API

Each replacement VM was issued a distinct bearer token and inference-user ID
for `https://llm.c.singularitynet.io`. Establish these as Docker/host secrets,
not Compose environment literals. Preserve the matching inference user for
embeddings requests.

Required logical fields per VM:

- inference base URL;
- bearer token;
- inference user ID;
- selected chat model ID;
- selected embedding model ID and matching user field, if embeddings are used.

Verify with a redacted `/v1/models` request and then one bounded chat request;
record only HTTP status, model ID, request ID, and latency.

## Per-identity application credentials

### VM1 — ProtoCosmo / ZeroBot

- Telegram bot token at the OpenClaw configuration secret reference
  `channels.telegram.botToken`.
- OpenClaw gateway authentication token for internal callers.
- Model-provider/OpenAI-Codex authentication profile(s) actually referenced by
  the exported agent configuration.
- Any connector/app OAuth credentials required by enabled integrations.

Disposition: use a **bounded OpenClaw export**. Do not copy the entire
`~/.openclaw` tree (currently about 21 GiB and containing unrelated state and
credentials). The final export review must enumerate effective provider profile
names and enabled connector credential names before cutover; values remain in
the secret mount only.

Verify: config validation succeeds with secret values redacted; provider-free
startup passes; then a model request and fresh Telegram canary pass after the
laptop receiver is stopped.

### VM1 — ProtoCosmo2

Secret file logical keys:

- `TG_BOT_TOKEN`
- `PROTOCOSMO2_CANARY_CONFIG` (path/reference; not itself a token)

The bounded credential/config/state delta is already staged with file mode
`0600` and state directories mode `0700`. No manual token re-entry should be
needed unless the staged secret is intentionally replaced.

Verify: key-presence and permission checks only, then one-receiver cutover and
a fresh Telegram canary.

### VM2 — Protomega

Secret/config keys:

- `OMEGACLAW_TG_BOT_TOKEN`
- `TELEGRAM_API_ID`
- `TELEGRAM_API_HASH`
- `TG_RECEIVE_TRANSPORT`
- `TG_SYNC_POLL`
- `TG_USE_MTPROTO`

Only the bot token is required for Bot API polling. The Telegram API ID/hash
are required when MTProto is enabled. The transport flags are non-secret but
must remain consistent.

Verify: effective transport mode and key presence without values; after the
laptop owner is stopped, perform a fresh Telegram canary and prove exactly one
receiver exists.

### VM2 — Protomega2 / ProtoMegaBot2

Secret/config keys:

- `PROTOMEGABOT2_TG_BOT_TOKEN`
- `OPENCLAW_GATEWAY_TOKEN`
- `OPENCLAW_GATEWAY_BASE_URL`
- `OPENCLAW_MODEL`
- `OPENCLAW_SUBPROCESS`
- `TG_CHAT_ID`
- `TG_PRIVATE_ONLY`
- `PROTOMEGABOT2_TOKEN_SECURITY_STATUS`
- `HF_HUB_OFFLINE`
- `TRANSFORMERS_OFFLINE`

The bot and gateway tokens are secret. URLs, model selection, chat/policy, and
offline flags are configuration and should be kept in versioned non-secret
configuration where practical.

Verify: gateway authentication succeeds internally, then perform the
one-receiver Telegram cutover and fresh canary.

## Docker placement

- Put secret values in Docker secrets or root-owned host files mounted
  read-only into the relevant container.
- Keep routing/policy/model names in non-secret Compose/config files.
- Use separate secret files and state volumes per identity; never share Telegram
  tokens, cursors, session stores, or PID/lock files.
- Ensure secret mounts are excluded from images, build context, Git, backups
  intended for sharing, logs, diagnostics, and Markdown evidence.
- Containers should start polling-disabled until the corresponding laptop
  receiver has stopped and its final state delta has been applied.

## Items Elija does not need to recreate for this migration

- GitHub/`gh` login and repository administration (handled separately by
  Elija).
- Telegram bot creation or bot usernames, unless a bot token is deliberately
  replaced.
- Existing routing IDs and policy documents; these are copied and verified.
- Mutable Telegram cursors/state; these move via final per-identity delta, not
  manual transcription.
- SSH private keys inside containers.

## Final operator acceptance

- [ ] Both VM SSH logins work from the administrator workstation.
- [ ] Each VM has its own ASI token/user mapping and provider smoke passes.
- [ ] Four distinct Telegram bot-token references exist; no values appear in
  Compose output or logs.
- [ ] ProtoCosmo bounded export enumerates all active provider/auth profile and
  connector secret names.
- [ ] Internal OpenClaw gateway token works only on the intended private path.
- [ ] Per-identity secret mounts are read-only and permission-restricted.
- [ ] Routing policy/chat allowlists match the laptop baseline.
- [ ] Each cutover proves the laptop receiver stopped before its VM receiver
  starts, and exactly one receiver remains.
- [ ] Fresh text and attachment canaries, restart, reboot, and soak checks pass.

## Evidence sources

- `docs/local-inventory.md`
- `experiments/20260812T144852Z-vm1-vm2-migration/IDENTITY_DELTA_MANIFEST.md`
- `experiments/20260812T144852Z-vm1-vm2-migration/RUN.md`
