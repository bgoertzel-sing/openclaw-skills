#!/usr/bin/env bash
set -euo pipefail

# Self-install the Channel Registry into an OpenClaw agent workspace.
# Usage: install.sh [workspace_dir] [agent_name]
# Reads openclaw.json channel configs for all transports and generates channels.yaml.

WORKSPACE="${1:-$(pwd)}"
CONFIG="${OPENCLAW_CONFIG:-$HOME/.openclaw/openclaw.json}"
OUTPUT="$WORKSPACE/channels.yaml"

if [[ ! -f "$CONFIG" ]]; then
  echo "ERROR: openclaw.json not found at $CONFIG" >&2
  exit 1
fi

python3 -c "
import json

with open('$CONFIG') as f:
    cfg = json.load(f)

channels = cfg.get('channels', {})
registry = []

for transport, tcfg in channels.items():
    if transport == 'telegram':
        for uid in tcfg.get('allowFrom', []):
            registry.append({
                'id': str(uid), 'name': 'ben-dm', 'transport': 'telegram',
                'type': 'private', 'purpose': \"Ben's direct messages\",
                'require_mention': False, 'can_send': True, 'can_receive': True,
                'notes': 'Primary 1:1 channel with Ben',
            })
        for gid, gcfg in tcfg.get('groups', {}).items():
            if gid == '*':
                continue
            sp = gcfg.get('systemPrompt', '').lower()
            # Match most specific keywords first
            name = 'unknown'
            if 'updates' in sp or 'progress' in sp:
                name = 'updates'
            elif 'botbot' in sp or 'bot-bot' in sp:
                name = 'botbotchats'
            elif 'philosophy' in sp:
                name = 'bot-philosophy'
            elif 'protobot' in sp or 'protomega' in sp:
                name = 'protobots'
            registry.append({
                'id': str(gid), 'name': name, 'transport': 'telegram',
                'type': 'supergroup',
                'purpose': gcfg.get('systemPrompt', '').split('.')[0][:100] if gcfg.get('systemPrompt') else 'unknown',
                'require_mention': gcfg.get('requireMention', False),
                'can_send': gcfg.get('groupPolicy', 'open') == 'open',
                'can_receive': gcfg.get('groupPolicy', 'open') == 'open',
                'notes': '',
            })
    elif transport == 'slack':
        for sid, scfg in tcfg.get('channels', {}).items():
            registry.append({
                'id': str(sid), 'name': scfg.get('name', sid), 'transport': 'slack',
                'type': 'channel', 'purpose': scfg.get('purpose', ''),
                'require_mention': scfg.get('requireMention', False),
                'can_send': True, 'can_receive': True,
                'notes': scfg.get('notes', ''),
            })

with open('$OUTPUT', 'w') as f:
    f.write('# Channel Registry (auto-generated)\n\nchannels:\n')
    for ch in registry:
        f.write(f'  - id: \"{ch[\"id\"]}\"\n')
        f.write(f'    name: \"{ch[\"name\"]}\"\n')
        f.write(f'    transport: \"{ch[\"transport\"]}\"\n')
        f.write(f'    type: \"{ch[\"type\"]}\"\n')
        f.write(f'    purpose: \"{ch[\"purpose\"]}\"\n')
        f.write(f'    require_mention: {str(ch[\"require_mention\"]).lower()}\n')
        f.write(f'    can_send: {str(ch[\"can_send\"]).lower()}\n')
        f.write(f'    can_receive: {str(ch[\"can_receive\"]).lower()}\n')
        f.write(f'    notes: \"{ch[\"notes\"]}\"\n\n')

print(f'Generated {len(registry)} channels')
"

echo "Registry: $OUTPUT"
