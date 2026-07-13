# 02 — Telegram Bot API 10 bot-to-bot setup

## Create and enable

1. Create **two distinct bots** with `@BotFather`: one for OpenClaw and one for OmegaClaw. Store their tokens separately.
2. In BotFather's **MiniApp** (not only the legacy text menus), open each bot and enable **Bot-to-Bot Communication** for both.
3. Create a private dedicated bot-discussion group and add both bots plus the owner.
4. Create a scheduled-updates group/channel; optionally a separate human-summary group.
5. If you want bots to receive ordinary group messages rather than commands/mentions/replies only, disable BotFather privacy for that bot. The safer default here is explicit mentions in the bot room.
6. Obtain numeric IDs using a controlled test/update or OpenClaw channel diagnostics. Supergroup IDs usually begin `-100...`. Do not paste tokens into public ID bots.

## OpenClaw side

- Use a SecretRef for `TELEGRAM_BOT_TOKEN`.
- Owner DM policy is allowlist.
- Main human groups should be allowlisted and mention-gated.
- The dedicated bot room must accept the sibling bot sender. The example uses `groupPolicy: "open"` **only for that private dedicated group**, with `requireMention: true`. If your OpenClaw version supports a bot-sender allowlist there, prefer that.
- Use one long-polling OpenClaw process for the OpenClaw token.

## OmegaClaw side

- Fill `omegaclaw-telegram.env` locally and `chmod 600` it.
- `TG_RECEIVE_TRANSPORT=bot_api`, `TG_USE_MTPROTO=false`, `TG_SYNC_POLL=false`.
- `TG_CHAT_IDS` explicitly lists allowed DM/groups.
- `TG_ALLOWED_USER_IDS` lists human owners/operators. The patched Bot API 10 path separately permits bot-originated messages in allowed groups while filtering self-originated updates.
- Run exactly one OmegaClaw worker/token consumer.

## Required controls

- resolve self ID with `getMe` and ignore it;
- deduplicate update/message IDs;
- group replies only for explicit mentions, replies, expected counterpart turns, or scheduled seeds;
- maintain immutable source-chat envelopes;
- bounded per-sender cooldown and a maximum interaction chain;
- cap output length and suppress equivalent daily discussions for 24 hours;
- never reroute a failed send to another chat;
- record Telegram send success/failure without logging message content or tokens.

## Live canary order

1. Owner DM → OpenClaw → owner-visible response.
2. Owner DM → OmegaClaw → owner-visible response.
3. Owner-authored bot-room mention → each bot separately.
4. OpenClaw bot-originated mention of OmegaClaw → Omega receives, processes, sends, and the owner sees the reply.
5. Omega bot-originated mention of OpenClaw → reciprocal test.
6. Simultaneous owner DM and bot-room messages → verify each reply remains in its source chat.
7. Scheduled-updates canary → verify correct channel.
8. Observe for at least one schedule cycle before widening automation.

A generated `(send ...)` expression proves only model intent. Require a successful Telegram API result/log **and visible delivery**.
