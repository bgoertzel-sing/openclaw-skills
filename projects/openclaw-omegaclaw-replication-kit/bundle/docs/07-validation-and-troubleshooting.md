# 07 — Validation and troubleshooting

## Before credentials/live traffic

```bash
./scripts/verify-kit.sh
openclaw config validate
openclaw secrets audit
openclaw skills check
openclaw plugins doctor
```

Verify the Omega patch against a clean pinned base by setting `OMEGA_BASE_REPO`. Run Omega's included tests after installation:

```bash
cd ~/research-agent/projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core
../../.venv/bin/python -m pytest -q Autotests/test_channels_metta_send.py \
  Autotests/test_message_envelope.py Autotests/test_health_check.py \
  Autotests/test_botapi10_safeguards.py
```

Run broader upstream tests as practical and record dependency/platform discrepancies.

## Runtime checks

```bash
openclaw status
openclaw gateway status
openclaw channels status --probe
openclaw cron list --json
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh status
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh health
pgrep -af 'telegram_mtproto_bridge.py'   # expected: no output
```

Then execute the eight canaries in `02-telegram-bot-api-10.md`. Capture timestamps, source/target chat IDs (in a private report), update IDs, transport outcome, and visible-delivery observation. Test two-chat concurrency rather than assuming it.

## Common failures

### Bot message not received

- bot-to-bot mode not enabled for **both** bots in BotFather MiniApp;
- BotFather privacy/mention policy blocks the event;
- target group absent from allowlist;
- sender/group policy blocks sibling bot;
- another process is consuming `getUpdates` for the same token;
- stale Telegram update offset.

### Model generated `(send ...)` but no Telegram message

Inspect Python transport send-result logs. Confirm the patched `src/channels.metta` delegates every evaluated send to Python and that transport deduplication is scoped per chat. Check API error/permissions/target ID. Do not count generation as delivery.

### Replies appear in wrong chat

Stop automation. Reproduce with simultaneous DM/group messages. Verify immutable message envelopes and that send uses the originating chat ID, not mutable global state. Do not deploy a retry that falls back to another chat.

### Bot loop/storm

Stop one/both runtimes; disable schedules. Confirm self ID from `getMe`, explicit mention/expected-turn gating, one-second-or-greater per-sender cooldown, bounded chain depth, and daily 24-hour suppression. Re-enable with one canary only.

### `database is locked`

A second process is opening a shared SQLite/Telethon/session database. This recipe requires no Telethon/MTProto process. Terminate duplicate owners and do not share writable session databases.

### macOS dependency failure

The OpenClaw half is portable, but this OmegaClaw stack is Linux-tested. Use a Linux VM/container rather than weakening/removing security dependencies without an independent compatibility review.

## Acceptance criteria

- clean secret/private-state scan and readable archive manifest;
- OpenClaw config validates and channel probe succeeds;
- Omega tests pass on recorded commits/environment;
- one worker, zero MTProto bridges, one poller/token;
- owner DM, reciprocal bot-originated, two-chat concurrency, and scheduled-updates canaries visibly pass;
- schedules are non-duplicated and correctly routed;
- backup restores into a disposable directory;
- at least one daily project discussion and one expert-review artifact are substantive and bounded.
