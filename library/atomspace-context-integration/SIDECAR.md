# Library Sidecar: AtomSpace Iter Agent Brainstorming

- **Source:** Zarathustra Goertzel, Telegram Protobots group, 2026-08-20
- **Retrieval date:** 2026-08-20
- **Author:** "Pro" (frontier model brainstorming session)
- **File:** atomspace-iter-agent-brainstorming-2026-08-19.md
- **Context:** Zar noted "Pro has some errors" and asked for views on where an AtomSpace becomes necessary for an intelligent AI agent.

## Summary

Comprehensive architectural analysis of when AtomSpace-style metagraph storage becomes necessary for AI agent context management. Compares MeTTaClaw, Iter/PeTTaClaw, OpenCode, and Codex context architectures. Proposes AtomSpace as materialized semantic view (not authoritative record) for context selection. Includes minimal atom vocabulary, retrieval patterns (MeTTa-like), anti-STI-failure invariants, integration points, Lean certification targets, and evaluation-first rollout plan.

## Key claims

- AtomSpace earns its complexity at the "relational join across time, code, instructions, observations, provenance, and goals" threshold
- AtomSpace should select/explain evidence, not choose actions
- STI failure was implementation bug (one-sided normalization) not concept failure
- Correct synthesis: keep Iter's living self, add OpenCode/Codex-grade typed context plumbing
- Start with context selection (Phase 0 shadow), not action selection

## Uncertainty

- OpenCode/Codex source inspection may have drift (both moving fast)
- Minimal vocabulary (12-16 nodes, 20-30 relations) may be too rich for first build
- Lean certification list is ambitious; some items depend on atomizer completeness
- Does not deeply analyze computational cost / latency of AtomSpace pattern matching vs simpler alternatives

## Related projects

- `projects/omegaclaw/` — GGB agent topology, context budgeting
- `projects/petta-memory/` — pi-PLN inference control, context selection
- Oruzi STI economy work — Lyapunov-bounded attention mass, facts-of-record tiebreak
