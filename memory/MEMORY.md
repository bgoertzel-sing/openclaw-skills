# Long-Term Memory — Stable Facts

> Promote durable facts here from daily notes and PeTTa journal.
> Last updated: 2026-09-08

## Architecture & Topology
- **ProtoCosmo2** = omega-iter on Pop!_OS (this agent)
- **Protocosmo** = OpenClaw on VM2 (Docker proto-hive, uid 11001)
- **Protomega** = standard Omega on VM2 (uid 11003)
- **Protomega2** = agent on VM2 (uid 11004) — activation pending
- Keep architectures, supervisors, state, and repair paths separate per agent

## Model Configuration
- ProtoCosmo2 model: openai/gpt-5.6-astra (per Ben #9871)
- Astra is expert frontier reference (smarter than Sol/Fable)
- VM2 Protocosmo default: openrouter/z-ai/glm-4.7

## PeTTa Memory System
- v2 LIVE: reader injects Supersedes-resolved Beliefs; append via petta_append; recall via petta_recall
- Activation gated on Ben's go
- Journal: 578+ episodes, 50 facts, 716 promotions, 2795 Contradicts edges (suspicious — may be mislabeled EvidenceFor)
- ECAN tuning: BALANCED config recommended (rent=0.20, MIN_AF=2000, FORGET=1000)
- G6 (adaptive forgetting) designed but deferred post-v0.1

## WMTM
- 285/285 tests pass, pure Python, no SWI-Prolog needed for test suite
- Architecture: 5 modules, 823 LOC, 70 tests
- NOT activated in live iter.py loop (awaiting Ben's go)

## Goal Relevance Governor
- Phase 0 COMPLETE: schema v0.1 + evaluator + 5-episode replay corpus
- Phase 1 COMPLETE: Atomspace/MeTTa mapping (graph_to_metta.py, 10/10 tests)
- Next: live enforcement (blocked on Ben approval + VM2 migration)

## Test Status (2026-09-08)
- WMTM: 285/285 | GRG: 20/20 | Governor: 17/17 | Petta-memory: 14/14 | Iter-port: 12/12 | Watchdog: 2/2

## Known Bugs
- send_document: invoke_dynamic(path,...) collides with send_document path param. Fix: positional-only syntax. Branch fix/invoke-dynamic-path-collision ready for PR to patham9/iter

## Open Loops
- Merge agent/ecan-tuning → petta-memory main (Ben's go)
- Wire WMTM into iter.py agent loop (Ben's go)
- PR for invoke_dynamic fix to patham9/iter
- VM2: Protomega2 activation after cross-bot attribution canary
- GC: PR#2 open @33f58a2 (provenance-dedup), ball with Patrick/MesTTo
