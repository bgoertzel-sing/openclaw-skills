---
name: "telegram-channel-registry"
description: "Transport-agnostic channel registry with cross-channel send for Telegram, Slack, Discord, and future transports."
---

# Channel Registry

## Purpose

Maintains a canonical, queryable list of all messaging channels the agent participates in across all transports (Telegram, Slack, Discord, etc.). Enables cross-channel sending without hardcoding chat IDs.

## Registry File

Lives at `workspace/channels.yaml`. Agent-specific.

### Schema

```yaml
channels:
  - id: "402314199"
    name: "ben-dm"
    transport: "telegram"
    type: "private"
    purpose: "Ben's direct messages"
    require_mention: false
    can_send: true
    can_receive: true
    notes: "Primary 1:1 channel"

  - id: "-5366386580"
    name: "bot-philosophy"
    transport: "telegram"
    type: "supergroup"
    purpose: "Philosophical discussions"
    require_mention: false
    can_send: true
    can_receive: true
    notes: "Philosophy channel"

  - id: "C0123456789"
    name: "research-updates"
    transport: "slack"
    type: "channel"
    purpose: "Research progress updates"
    require_mention: false
    can_send: true
    can_receive: true
    notes: "Slack channel (placeholder until configured)"
```

## Operations

- `channel-registry lookup <name>` → returns `transport:id` (e.g. `telegram:-5366386580`)
- `channel-registry send <name> <message>` → sends via message tool
- `channel-registry list [--transport telegram|slack|...]` → lists channels
- `channel-registry sync` → reads openclaw.json for all transports, updates registry

## Self-install

`install.sh` reads `openclaw.json` channel configs for all transports (telegram, slack, discord when configured) and generates `channels.yaml`. Works for ZeroBot and ProtoMegaBot.

## Usage

1. `channel-registry lookup bot-philosophy` → `telegram:-5366386580`
2. `message(action=send, target=telegram:-5366386580, message="...")`

## Multi-transport

- Telegram: numeric IDs (positive DM, negative groups)
- Slack: channel IDs start with `C`, DMs with `D`
- Discord: snowflake IDs
- Registry normalizes to `transport:id` for message tool's `target` parameter
- New transports added by extending sync to read their config section
