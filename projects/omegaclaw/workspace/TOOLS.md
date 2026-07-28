# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup: camera names and locations, SSH hosts and aliases, preferred TTS voices, speaker/room names, device nicknames, anything environment-specific.

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

### Slack (BGI Labs workspace, #hugo-chat C0BGBD99T9A)

- Mike Archbold → U0BG1E3B3B5; Hugo-Bot → U0BGG0S76Q6; me (Protomega Goertzelbot) → U0BKHHZ8QD7.
- **Preference (Mike, 2026-07-24):** send Slack messages as a single burst, not streamed/edited previews. The streaming is gateway-side (`channels.slack.streaming.mode: off` for this channel) — I can't toggle it from within a session; an admin (Ben/ZeroBot) must set it. Until then, keep replies compact so the first preview chunk carries the point.
- My ingress filters bot-authored messages: I never see Hugo's posts directly; humans (Mike/Haley) relay them. Fix = allow `bot_message` events in my Slack ingress (gateway config).
- Hugo's fixes (2026-07-24): mention syntax `<@U...>` instead of literal `@Name`; handling `message_changed` events to read my streamed edits.

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)
