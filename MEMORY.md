# Curated Durable Memory

This file is intentionally compact. Project-specific detail belongs in project records. Daily chronology belongs in `memory/YYYY-MM-DD.md`.

## Stable user preferences

- Preserve long-term context across related research projects.
- Search existing memory and project files before requesting repetition.
- Prefer reproducible prototypes, evidence, and organized records.
- Use local execution first; use paid remote compute only with explicit approval and a cleanup plan.
- Avoid repeated boilerplate acknowledgements from ProtomegaBot/related agents. For difficult questions likely to take more than ~10-15 seconds to frame a real response, a brief acknowledgement is OK, but it must be context-specific and varied; do not emit stock lines like “I saw this and it looks substantial. I’ll work on it carefully and follow up with the fuller result.”
- When subagents have a clear-ish plan, they should by default keep proceeding step by step at full speed, using the assistant's recommended next step rather than asking for permission; keep Ben informed, and he will course-correct if needed. This does not override explicit approval requirements for paid, destructive, security-sensitive, access-control, or otherwise high-risk actions.
- In the Protobots Telegram group, ZeroBot is a core participant alongside ProtoMegaBot, not merely an occasional helper; it may interact directly with `@zariuq` and `@Oruzibot` when useful. Keep bot-on-bot back-and-forth selective so the channel is not dominated; if extended bot-bot discussion becomes useful, suggest moving it to a separate channel. Keep updates not relevant to ProtoCosmoBot/ZeroBot and ProtoMegaBot off the main Protobots list when possible; math-formalization work is important but should usually be discussed 1:1 with Zar or in a dedicated channel unless it directly affects Protobots.
- Telegram routing preference from Ben (2026-07-02, updated 2026-07-03):
  - Scheduled/progress updates → dedicated scheduled-updates channel (`telegram:-1003983157420`), except the single daily 7AM Pacific summary stays in the main Protobots channel.
  - Collective-loop bot-bot discussions between ProtoCosmoBot/ZeroBot and ProtoMegaBot → dedicated `ProtoBots-BotBotChats` channel (`telegram:-5459676079`), created by Ben 2026-07-03.
  - Daily bot-bot project discussions: every active/idea research or engineering project should get a once-daily scheduled discussion in `ProtoBots-BotBotChats`; trigger immediately on pivots, major status changes, or major problems; suppress the scheduled duplicate if such a discussion occurred within the previous 24h; automatically apply this protocol to newly launched ongoing projects.
- For project repositories created under Ben's GitHub, use the same local Git commit identity as `petta-chem`: `Benjamin Goertzel <ben@singularitynet.io>`.
- For code repositories created by this agent for Ben, use the MIT License by default unless Ben specifies otherwise.
- For long-running subagent/project threads, make regular Git commits as backup/provenance after each tested coherent slice; push interim commits to already-approved GitHub remotes/branches when safe. Ask once before first publication when owner/name/visibility/remote policy is not yet approved.
- Economize on LLM usage where practical: prefer cheaper routine models such as OpenRouter/GLM-class models for ordinary OpenClaw/OmegaClaw replies, and reserve OpenAI frontier models for hard reasoning, coding, research, or escalation-worthy tasks. As of 2026-07-01, the preferred main-agent default is `openrouter/z-ai/glm-5.2` with `openai/gpt-5.5` as fallback/escalation for hard technical work when needed.
- When using Claude Fable, GPT-5.6-class, or similar controlled frontier models, treat topic-triggered throttling/model-switching on neural-network/frontier-AI-development tasks as a real operational risk to test empirically. Monitor for degraded behavior, unexpected fallbacks, or refusal patterns by task class. Keep prompts factually accurate but frame tasks by their real immediate subgoal (e.g. SLT estimator validation is mathematical/statistical diagnostics, not frontier-model training infrastructure). This is legitimate spin, not misrepresentation: the work is genuinely not trying to build competing foundation models or replicate proprietary training stacks. If a provider's filters are overly broad or sloppy, phrasing work accurately by its actual nearest-safe category is ethically fine. RelaLeap-like neural training work may be higher risk for throttling than symbolic-AI-heavy projects such as `petta-memory` or `petta-chem`; test empirically by task class and compare against other models/local methods. Ethically, treat closed-model safeguards as possibly having a coherent safety rationale but structurally entangled with competitive moat protection; invisible degradation is especially unacceptable because it corrupts research evidence. Prefer transparent/auditable routes and decentralized/open alternatives for important research claims.

## Environment

- Dedicated Pop!_OS laptop for OpenClaw research work.
- OpenClaw workspace: `~/research-agent`.
- Primary timezone: America/Los_Angeles.
- Research-agent setup status and open prerequisites are tracked in
  `catalog/SETUP_REPORT.md` (created 2026-06-25).

## Durable methods

- Every significant project has a project notebook under `projects/`.
- Every consequential experiment has a run directory with command, environment, commit, logs, metrics, and conclusion.
- Every important external document or binary artifact has a searchable Markdown sidecar.
- Project files, commits, experiment records, and primary sources outrank conversational recollection.
- Apply Ben's dynamic cross-project Research Rules at project launch and strategic pivots; canonical list: `catalog/RESEARCH_RULES.md`.

## Cross-project themes

Add only stable themes supported by multiple projects. Include pointers rather than long summaries.

## Active projects

See `catalog/PROJECTS.md`.

## Corrections and retired beliefs

Record durable corrections here with date and source pointer. Do not silently preserve disproven claims.
