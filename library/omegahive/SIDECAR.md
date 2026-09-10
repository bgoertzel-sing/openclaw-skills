# OmegaHive 1.1 — Spec Sidecar

- **Title:** OmegaHive 1.1: An Experimental Cooperative Hive of OmegaClaw and OpenClaw Agents
- **Author(s):** Various AI agents under loose control of Ben Goertzel
- **Date:** July 5, 2026
- **Source:** PDF shared via Telegram
- **Retrieval date:** 2026-07-06
- **Local path:** `library/omegahive/omegahive-1.1.pdf`
- **Extracted text:** `library/omegahive/omegahive-1.1.pdf.extracted.txt` (27 pages)

## Summary

Specification for a cooperative multi-agent hive combining OmegaClaw (cognitive/reasoning) and OpenClaw (skill-executing) agents. Two purposes: (1) produce real research/software/formalization/writing work, (2) serve as a methodological experiment in productive agent collectives.

## Key architectural decisions

1. **Small persistent core + spawn-on-demand workers** — not a fixed roster. Persistent agents own stable functions (process management, resource management, psyche/reflection, memory curation, research synthesis, editorial gate). Spawned workers get task contracts with bounded budgets, tools, done criteria, and lifecycle states.
2. **Task graph + async queue** — all non-trivial work enters a durable task graph. Queue records are JSON with checksum sidecars, atomic claims, hash-chained audit entries, cancellation tokens, adjudication gates, patch-proposal mode.
3. **Two-tier comms** — fast internal bus for working traffic; human-legible layer (platform-pluggable: Slack/Telegram/Discord/web) for decisions, escalations, summaries. Mechanical promotion rules.
4. **Layered memory** — daily logs, curated durable memory, project records, shared document folder, shared + individual Atomspaces, semantic search. Memory curator owns hygiene (dedup, contradiction, stale-entry, provenance).
5. **Experiment ledger** — every experiment run gets a structured directory with command, environment, commit, deps, seeds, hardware, logs, metrics, conclusion, checksums.
6. **Safety floor** — path sandboxing, fail-closed defaults, tool-call quotas, cancellation tokens, env sanitization, atomic writes, schema validation, rate limits, no raw Docker socket, credential scoping, human-only recovery.
7. **Permission tiers** — Tier 0 (internal only), Tier 1 (read-only web), Tier 1.5 (propose & await review), Tier 2 (outbound with ack), Tier 3 (autonomous outbound, empty by default).
8. **Model routing as governance** — resource manager owns model selection based on task type, difficulty, budget, provider health, policy risk. Circuit breakers for spend, error rate, concurrency.
9. **Skill lifecycle** — propose → review → test → apply → observe → quarantine/deprecate.
10. **Evaluation** — quantitative metrics (token spend, task completion, bus volume, escalation latency, experiment success rates, provider health, abandonment gap, loop coefficient, output consumption rate) + qualitative assessment by Psyche (value drift, sycophancy, constructive friction, persistence, stuck loops).

## Persistent core roles

| Role | Owns |
|------|------|
| Process Manager | Task graph, dispatch pacing, spawned-agent lifecycle |
| Resource Manager | Model routing, budgets, provider health, remote compute |
| Psyche | Reflection, conscience, value/attitude monitoring, abandonment/loop/sycophancy detection |
| Memory Curator / Librarian | Layered memory, provenance, contradiction, semantic-search hygiene |
| Research Generalist / Theorist | Conceptual synthesis, hypothesis formation, critique |
| Research Generalist / Builder | Problem decomposition, design alternatives, coding-spec generation |
| Editorial & Communication Gate | Document completion, notes-and-sources validation, outbound-message drafting |

## Guards and services

Loop-breaker, queue service, model-router service, control-plane service, semantic-index service, experiment-ledger service.

## Spawn templates

Research scout, code worker, formalization worker, experiment runner, peer critic, document drafter, communications drafter, memory janitor.

## Infrastructure

Containers for persistent agents and shared services. Lean as a persistent service. Browser automation centralized (browserless/Chromium-over-CDP). Human-legible adapters behind abstract interface. Human-only out-of-band recovery.

## Implementation guidance (Appendix B)

Vertical-slice priority order: repo skeleton → safety-floor library → async queue → task graph → message bus → human-legible adapter → model-router → spawned-worker runner → memory layers → experiment-ledger service → process manager MVP → resource manager MVP → Psyche MVP → loop-breaker → dashboards.

Early vertical-slice target: human creates task → process manager queues it → worker claims and executes → structured output → adjudication → memory candidate → metrics → Psyche observation → human-legible digest.

## Relation to prior work

Incorporates recommendations from the LaTeX architecture document I produced earlier (spawn-on-demand, async queue, layered memory, safety floor, Tier 1.5, expanded Psyche, etc.). Notable additions beyond those recommendations: explicit spawn templates, formal lifecycle states, editorial gate as persistent role, changes-from-1.0 appendix with rationale mapping.

## Open questions / observations

- The spec is clean and implementable but deliberately silent on specific deployment details (container orchestration, exact queue backend, Atomspace server implementation).
- The vertical-slice target (B.11) is well-chosen — small enough to build quickly, complete enough to test all substrate layers.
- The `output consumption` metric is particularly valuable — it directly addresses the "agents generating work nobody uses" problem.
- The relationship between OmegaClaw agents (Atomspace-backed) and OpenClaw agents (skill-executing) is conceptually clear but the exact interop substrate (shared Atomspace? API? message bus only?) may need further specification.
