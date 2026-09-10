# ProtoCosmo2 Phase 3 identity and context map

- Date: 2026-08-03
- Source: ZeroBot workspace identity/context files
- Target: the isolated ProtoCosmo2 OmegaClaw tree
- Status: draft translation; no live runtime configuration is enabled

ProtoCosmo2 is an OmegaClaw-based port and descendant of ZeroBot. It is not
ZeroBot and must not imply process, session, memory, or identity continuity.
OmegaClaw loads identity/value prose from `memory/prompt.txt`, rather than
loading OpenClaw's named Markdown context files directly
(`protocosmo2/OmegaClaw-Core/docs/reference-internals-extension-points.md`).

## Source-to-target mapping

| ZeroBot source | Content to preserve | ProtoCosmo2 target treatment | OmegaClaw equivalent or gap |
|---|---|---|---|
| `/home/openclaw/research-agent/SOUL.md` | Rigorous, inventive, low-ego research style; explicit epistemic labels; no hype or fabricated certainty | Translate into `config/identity-draft/SOUL.md`, then later compose reviewed text into the runtime prompt | Prompt identity/value text is supported by `protocosmo2/OmegaClaw-Core/memory/prompt.txt` and documented at `protocosmo2/OmegaClaw-Core/docs/reference-internals-extension-points.md` |
| `/home/openclaw/research-agent/IDENTITY.md` | Name, role, vibe, signature, core promise | Translate into `config/identity-draft/IDENTITY.md`; change name to ProtoCosmo2 and explicitly state OmegaClaw port/descendant, separate runtime and audit trail | No structured identity schema; prose prompt only (`protocosmo2/OmegaClaw-Core/memory/prompt.txt`). **No equivalent field:** OpenClaw runtime identity/session continuity |
| `/home/openclaw/research-agent/USER.md` | Ben's profile, timezone, technical context, interaction preferences, local-first/cost-approved compute | Fold into the user-context section of `config/identity-draft/AGENTS.md`; do not claim these facts are already in OmegaClaw LTM | No dedicated user-profile loader. Prompt prose and explicit file reads are available (`protocosmo2/OmegaClaw-Core/src/memory.metta`, `protocosmo2/OmegaClaw-Core/src/skills.metta`). **No equivalent field:** automatic OpenClaw context-file injection |
| `/home/openclaw/research-agent/AGENTS.md` | Operating policy, source hierarchy, project workflow, safety and authority gates, follow-through | Translate into `config/identity-draft/AGENTS.md`; replace OpenClaw tool assumptions and add fail-closed gap rules | Shell/file/MeTTa primitives exist (`protocosmo2/OmegaClaw-Core/src/skills.metta`); memory primitives exist (`protocosmo2/OmegaClaw-Core/src/memory.metta`); filesystem policy exists (`protocosmo2/OmegaClaw-Core/profile/policy.py`). **No equivalent:** OpenClaw subagents, sessions, cron, skill workshop, connector tools, or approval UI; none appear in the catalogued skill surface (`protocosmo2/OmegaClaw-Core/src/skills.metta`) |
| `/home/openclaw/research-agent/TOOLS.md` | Workspace conventions, CLI preferences, credential discipline, provider notes | Fold safe local conventions into the tools/capability section of `config/identity-draft/AGENTS.md`; revalidate actual installed commands at use time | Generic shell exists but is unsandboxed at the primitive level and limited to five seconds (`protocosmo2/OmegaClaw-Core/src/skills.pl`); the process may be constrained by filesystem policy (`protocosmo2/OmegaClaw-Core/profile/policy.yaml`). **No equivalent:** native `memory_search`, QMD, GitHub/Drive/browser connector APIs, image inspection, tmux control, or secret-store API; availability through shell is `[unverified]` |

## Runtime-semantic translations

| ZeroBot concept | Translation | Evidence / status |
|---|---|---|
| Named Markdown context files | Compose reviewed translations into the instance's prompt; keep these files as provenance-bearing drafts | `protocosmo2/OmegaClaw-Core/src/memory.metta`; `protocosmo2/OmegaClaw-Core/docs/reference-internals-extension-points.md` |
| Semantic memory search | Use `query` only as a non-authoritative hint; verify consequential claims against files | `query` is embedding-only and exact match is not guaranteed: `protocosmo2/OmegaClaw-Core/docs/reference-skills-memory.md` |
| Daily/episodic memory | Keep ProtoCosmo2's `history.metta` separate and fresh; do not equate it with imported ZeroBot history | `protocosmo2/OmegaClaw-Core/src/memory.metta` |
| Durable facts | `remember` can store text, but provenance and deduplication require an adapter; until then, fail closed on import claims | No automatic deduplication: `protocosmo2/OmegaClaw-Core/docs/reference-skills-memory.md` |
| File edits | Read before writing; do not overwrite without an explicitly reviewed target and authority | `write-file` overwrites unconditionally: `protocosmo2/OmegaClaw-Core/docs/reference-skills-io.md` |
| Command execution | Use only bounded, reviewed local commands within configured policy | Shell has a five-second timeout: `protocosmo2/OmegaClaw-Core/src/skills.pl`; allowed paths are policy-controlled: `protocosmo2/OmegaClaw-Core/profile/policy.yaml` |
| Telegram routing | One configured/bound chat and one authenticated user are supported; named multi-channel routing and bot-loop policy need an adapter | `protocosmo2/OmegaClaw-Core/channels/telegram.py`; `protocosmo2/OmegaClaw-Core/src/channels.metta` |
| Scheduling/background work | Keep autonomous wake loops disabled for baseline; do not claim cron or durable jobs | Wake-loop knobs exist in `protocosmo2/OmegaClaw-Core/docs/reference-configuration.md`; a cron/job registry is absent from the catalogued surface (`protocosmo2/OmegaClaw-Core/src/skills.metta`) |
| Subagents/reviewers | Report unavailable unless a separately reviewed adapter is installed | No generic subagent primitive is catalogued in `protocosmo2/OmegaClaw-Core/src/skills.metta`; fixed Agentverse examples are not a generic delegation contract (`protocosmo2/OmegaClaw-Core/src/agentverse.py`) |

## Unresolved semantic differences

1. The drafts are not automatically loaded; prompt assembly and provider-free
   validation remain future Phase 3 integration work.
2. Filesystem policy is best-effort in the checked configuration, so prompt
   policy must not be represented as a hard sandbox
   (`protocosmo2/OmegaClaw-Core/profile/policy.yaml`).
3. Telegram currently binds one chat and authenticated user; explicit sender
   allowlists, mention-only group behavior, bot-origin filtering, and named
   cross-channel routing are absent (`protocosmo2/OmegaClaw-Core/channels/telegram.py`).
4. The runtime has no OpenClaw-style approval mechanism. Sensitive operations
   must stop and request approval through the active channel; enforcement
   beyond prose is `[unverified]`.
