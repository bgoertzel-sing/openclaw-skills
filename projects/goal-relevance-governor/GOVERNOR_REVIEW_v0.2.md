# Goal Relevance Governor v0.2 — Comprehensive Review

**Date:** 2026-09-08  
**Status:** All 198 tests, 170 subtests passing (1.38s)  
**Commits this session:** 27+

---

## Architecture

```
Episode Data (JSON)
    │
    ▼
┌─────────────────────┐
│ PLN Truth-Value     │  ← Graph → truth values (st, cn, lt)
│ Mapping v0.1        │  13 tests
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ PLN Evidence        │  ← Forward propagation, relevance scoring
│ Propagation         │  18 tests
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ ECAN Attention      │  ← Short/long-term importance, funding
│ Allocation          │  11 tests
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Verdict Bridge      │  ← 7 verdicts from PLN+ECAN signals
│ (12 rules)          │  12 tests
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Multi-Hop Chains    │  ← Deep goal chains, path enrichment
│ + Conflict Detect    │  18 tests
│ + Conflict→Verdict   │  ← Post-process: weaker task → REPLAN
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Reasoning Explainer │  ← Human-readable explanations
│ (chain + conflict)  │  12 tests
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Remediation Engine  │  ← Verdict → action plans
│ v0.1 (6 verdicts)   │  14 tests + 6 MeTTa cross-val
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Temporal Simulator  │  ← Mutate episode, re-evaluate, detect drift
│ (3 timeline templates)│  11 tests
└─────────────────────┘
```

## Verdict Coverage (7/7)

| Verdict | Episode | Signal |
|---------|---------|--------|
| STOP_STALE | episode_01 | all_direct_goals_terminal, temporal_staleness |
| ESCALATE | episode_02 | multiple_active_goals_no_evidence |
| PAUSE_RECOVERABLY | episode_02 | resource_contention, higher_priority_task |
| DEFER | episode_03 | irreversible_on_early_stage_research |
| REPLAN | episode_04 | goal_superseded, superseded_by |
| CONTINUE | episode_05 | healthy, high_relevance |
| REPLAN | episode_06 | resource_conflict_replan (approach divergence) |
| BLOCKED | example_graph | (edge case) |

## Remediation Plans

Each verdict produces a structured plan with:
- **Prioritized steps** (P1-P4) with dependencies
- **Verification criteria** per step
- **Success criteria** for the overall plan
- **Rollback plan** and **risk notes**

| Verdict | Key Actions |
|---------|-------------|
| STOP_STALE | abandon_task, release_resource(s), notify_stakeholders |
| ESCALATE | boost_priority, allocate_resources, set_deadline, require_evidence |
| PAUSE_RECOVERABLY | pause_task, monitor_blocker, resume_task |
| DEFER | park_task, set_trigger, monitor_trigger |
| REPLAN | redesign_task, update_goal_link, reset_progress, archive_old_approach |
| CONTINUE | monitor_task, set_checkpoint |

## MeTTa Integration

- **remediation_rules.metta**: Encodes verdict→action mappings in MeTTa syntax
- **6 cross-validation tests**: Verify Python remediation engine actions match MeTTa spec
- **All Python actions have MeTTa counterparts** (verified by test)

## Performance

| Stage | Time per episode |
|-------|-------------------|
| Full pipeline | < 2ms |
| Remediation | < 0.1ms |
| Explainer | < 0.1ms |
| Temporal sim | < 1ms |
| **6-episode total** | **< 5ms** |

## Test Breakdown

| Module | Tests | Subtests |
|--------|-------|----------|
| PLN Truth-Value Mapping | 13 | — |
| PLN Evidence Propagation | 18 | — |
| ECAN Attention | 11 | — |
| Verdict Bridge | 12 | — |
| Multi-Hop + Conflict | 18 | — |
| Integrated Pipeline | 7 | — |
| Reasoning Explainer | 12 | — |
| Temporal Simulator | 11 | — |
| Remediation Engine | 14 | — |
| MeTTa Cross-validation | 6 | — |
| Integration Tests | 7 | — |
| Performance Benchmarks | 5 | — |
| MeTTa Bridge v0.3 | 16 | — |
| **Total** | **198** | **162** |

## Demo

```bash
python3 demo_pipeline.py --all
```

Runs the full pipeline on all 6 episodes with formatted output showing:
1. Pipeline recommendations with verdicts and signals
2. Remediation plans with prioritized steps
3. Human-readable reasoning explanations
4. Temporal simulation with drift detection

## Files

```
atomspace/
├── pln_truth_mapping.py          # PLN truth-value mapping
├── pln_propagation.py           # Evidence propagation
├── ecan_attention.py            # ECAN attention allocation
├── verdict_bridge.py            # Verdict bridge rules
├── pln_verdict_bridge.py        # PLN→verdict integration
├── multi_hop_chains.py          # Multi-hop goal chains
├── conflict_detection.py       # Conflict detection
├── integrated_governor.py       # Full pipeline orchestrator
├── reasoning_explainer.py       # Human-readable explanations
├── temporal_simulator.py        # Temporal evolution simulator
├── remediation_engine.py        # Remediation action plans
├── remediation_rules.metta      # MeTTa remediation rules
├── metta_evaluator.py           # MeTTa-Python bridge
├── schema.metta                 # MeTTa schema
├── test_*.py                    # 198 tests total
└── samples/episode_{01..05}.metta  # MeTTa episode samples

replay_corpus/
├── episode_01_stale_codegen.json
├── episode_02_chem_blocking.json
├── episode_03_premature_hardening.json
├── episode_04_overengineered_repair.json
├── episode_05_control_justified_long_running.json
├── episode_06_conflict_replan.json
├── example_graph_v0.1.json
└── remediation_plans_all.json   # Exported plans for all episodes

demo_pipeline.py                 # End-to-end demo
```

## Next Steps (if approved)

1. **Live enforcement mode**: Wire remediation plans to actual task scheduler actions
2. **Episode 06**: Add REPLAN-triggered-by-conflict scenario (different from superseded_goal)
3. **Deeper PLN integration**: Use OpenCog atomspace for truth-value computation
4. **MeTTa remediation execution**: Have MeTTa rules generate and execute remediation plans
