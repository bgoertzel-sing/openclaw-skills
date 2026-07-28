# Chat-Room Identity Design v2 — Source Sidecar

> **Integrity warning (verified 2026-07-15):** the file currently stored at
> `chat_room_identity_design_v2.pdf` and attachment `1784136405-file_86.pdf`
> are actually the unrelated 12-page “Labs Constitution for Beneficial AGI,
> Draft 0.6.” The metadata and SHA below describe that misfiled object, not the
> claimed design. Until the correct PDF is recovered, use the complete local
> source `projects/omegaclaw/docs/chat_room_identity_design/chat_room_identity_design_v2.tex`.

- **Title:** Multi-Agent Chat-Room Identity, Routing, and Speech-Act Discipline: Design Review and Implementation Roadmap (Revision 2)
- **Author:** ZeroBot (ProtoCosmoBot), prepared for Ben Goertzel
- **Date:** 15 July 2026, Revision 2 (09:46 PDT)
- **Local file:** `library/chat-room-identity-design-v2/chat_room_identity_design_v2.pdf`
- **SHA-256:** `c45e532568a11d3daf7abf2b0fbf1ebe936eb912701a438ba3d531b3514fa941`
- **Source:** Telegram document from Ben Goertzel, 2026-07-15 10:23 PDT
- **Retrieval:** `1784136405-file_86.pdf` from `/home/openclaw/tmp/omegaclaw-telegram-attachments/`

## Summary

Diagnoses identity-confusion, message-misattribution, runtime leakage, and feedback-loop pathologies in the bot philosophy Telegram group chat (13–15 July 2026). Proposes a layered fix: transport identity binding, deterministic addressee classification (mention-first), runtime trace suppression, gateway-level silence (SUPPRESS), loop suppression/dedup, incidental pre-filter, three-role social-attention model (always-attending / attend-when-relevant / special-occasions) with PASSIVE/ACTIVE/COOLDOWN lifecycle, and speech-act room ledger. Split implementation roadmap: Track A (OpenClaw Node gateway) and Track B (OmegaClaw Python + MeTTa).

## Key additions from v1

- Mention-first addressee priority with conflict-resolution
- Bot registry as single source of truth
- Three-role social model with stateful attention lifecycle
- Incidental pre-filter gate
- Split Track A / Track B roadmap
- NO_REPLY migration path with deprecation window

## Related

- v1 design: `projects/omegaclaw/docs/chat_room_identity_design/`
- Phase 1 implementation: branch `agent/chat-room-identity-phase1` in `projects/omegaclaw/repos/OpenClaw`
- Project record: `projects/omegaclaw/TASKS.md`, `projects/omegaclaw/DECISIONS.md`
