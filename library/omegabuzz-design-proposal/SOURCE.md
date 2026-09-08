# Source: OmegaBuzz — Comprehensive Design Proposal

- Type: `PDF`
- Authors/organization: Prepared for Benjamin Goertzel and BGI Labs; author not specified in supplied PDF metadata
- Publication/version date: 2026-07-30, version 0.1
- Retrieved: `2026-07-30`
- Canonical URL or identifier: Telegram attachment `OmegaBuzz_Design_Proposal---f6d81279-eae3-4d3e-a7a6-278ad952e8c7.pdf`
- Local source path: `library/omegabuzz-design-proposal/omegabuzz-design-proposal-2026-07-30.pdf`
- SHA-256: `9bf01df1719d81ecd7fe9a641d29779eb3d75dc8b4f3bff7f8c0615b773a1e10`
- License/access constraints: Attached in the Bot Philosophy Telegram group. The proposal says Buzz is Apache-2.0 and Scout redistribution/code incorporation needs an explicit license/relicense decision; verify upstream claims against pinned sources before implementation.
- Privacy tier: `local-private`
- Tags: `OmegaBuzz`, `OmegaHive`, `Buzz`, `Scout`, `AtomSpace`, `Hyperon`, `provenance`, `governance`, `resident-learners`
- Related projects: `omegaclaw`, `omegahive-conversation-governor`, `petta-memory`, `hyperseed-formalizations`

## Summary

Comprehensive 98-page proposal for a human-agent collaboration platform that combines Buzz as a signed collaboration substrate, OmegaHive organizational objects and governance, layered AtomSpace/MeTTa/PLN memory, Scout-style provenance navigation, and an agent/hive dashboard. It proposes a phased implementation from contracts and Buzz hardening to a single-hive MVP, semantic memory/context navigation, Resident Learners, then multi-hive and cross-community federation.

## Key claims or contents

- The central conceptual distinction is among authorship, visibility, epistemic standing, and organizational authority (Executive Summary, pp. 2–3).
- The canonicality matrix assigns different authorities to signed event history, object/Git artifacts, private/working AtomSpaces, durable admitted claims, action manifests, and policy/delegation state (Section 4.2, pp. 10–12).
- It favors a Buzz downstream distribution with sidecar services and only a small upstream patch stack (Section 3.5, pp. 8–9).
- It recognizes public Buzz gaps as scoped auth, enforced rate limiting, approval suspension/resumption, and richer audit hooks (Section 3.1.1, p. 7).
- It places Resident Learners in a separately governed tier with a charter, attention/egress controls, visible consent, and a staged shadow-to-budgeted-speech experiment (Sections 9.5–9.6, pp. 35–36; Section 14.8, p. 59).
- Phase 0 requires contract/threat-model work, event schemas, scoped auth, rate limit, approval resumption, replayable projectors, Scout licensing resolution, and hostile-content fixtures. Phase 1 adds a single-hive organizational MVP; Phase 2 adds AtomSpace/Scout (Sections 15.2–15.4, pp. 60–61).

## Methods or implementation details

The proposal describes typed signed events with idempotency/correlation, checkpointed/replayable projectors, signed snapshots, a Key and Capability Broker, Policy and Action Broker, Memory Admission Service, Archive Projector, Context Broker, and federation gateway. It includes schema sketches, APIs, an engineering backlog, coding-agent roles, and a test matrix.

## Limitations and uncertainties

The document is a design proposal, not an implementation claim. Upstream Buzz/Scout state is reported as reviewed on 2026-07-30 but needs repository URL, branch, and commit-SHA provenance to make the baseline reproducible. The proposal itself records Scout licensing uncertainty. The "first vertical slice" in the executive summary includes semantic memory and Scout, while the roadmap places those in Phase 2; this should be resolved into explicit slice boundaries before implementation.

## Relevance to current work

Extends the existing OmegaHive conversation-governor and Resident Learner work into a product/system architecture. Its authority membrane and staged Resident Learner model are materially compatible with `projects/omegahive-conversation-governor/docs/resident-learner-minimal-governor.pdf` but should be reconciled through explicit executable invariants.

## Review artifacts

- Concise synthesis of the ProtoCosmoBot and ProtomegaBot reviews: `projects/omegahive-conversation-governor/docs/omegabuzz-feedback-brief-20260730.pdf` (compiled and visually checked on 2026-07-30; SHA-256 `b68956cf6e2a18274e4b7e37e47e7c61a3b14b691bbe8305a162e32a58e424ea`).

## Follow-up questions

- What ordering/CAS semantics resolve competing valid signed transitions on the same mutable object?
- Which minimal Slice-0 acceptance gates precede any dashboard, AtomSpace, federation, or Resident Learner implementation?
- How are private/quarantined memory reads prevented from becoming undisclosed inputs to consequential commitments?
- Which exact Buzz and Scout commits are the implementation baselines, and what legal decision governs Scout reuse?
