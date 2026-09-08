# Goal Relevance Governor — Architecture

## Overview

The Goal Relevance Governor is a read-only shadow system that evaluates
whether active tasks remain relevant to their parent goals. It combines
rule-based heuristics with probabilistic logic (PLN) and economic
attention allocation (ECAN) to produce actionable verdicts.

## System Layers

```
┌─────────────────────────────────────────────────────────┐
│                   Input: Graph JSON                      │
│  (goals, projects, tasks, resources, results, edges)    │
└──────────────────────┬──────────────────────────────────┘
                       │
          ┌────────────▼────────────┐
          │   Layer 1: PLN          │
          │   (pln_propagation.py)  │
          │                         │
          │   • Truth values (s,c)  │
          │   • Relevance scores    │
          │   • Evidence propagation│
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │   Layer 2: ECAN         │
          │   (ecan_attention.py)   │
          │                         │
          │   • STI from PLN rel    │
          │   • LTI from PLN conf   │
          │   • Rent + decay + spread│
          │   • Eviction candidates │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │   Layer 3: Verdict      │
          │   (pln_verdict_bridge)  │
          │                         │
          │   • Rule-based verdicts │
          │   • PLN confidence mod  │
          │   • Temporal staleness  │
          │   • Priority bands      │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │   Integrated Pipeline   │
          │   (integrated_governor) │
          │                         │
          │   • Unified result      │
          │   • Recommendations     │
          │   • Executive summary   │
          │   • JSON export         │
          └─────────────────────────┘
```

## Verdict Types

| Verdict | Meaning | When |
|---------|---------|------|
| CONTINUE | Proceed as planned | High relevance, active goals |
| ACCELERATE | Increase priority | High relevance + unblocked |
| PAUSE_RECOVERABLY | Pause temporarily | Blocked but recoverable |
| DEFER | Defer to higher priority | Low relevance, alternatives exist |
| REPLAN | Revise approach | Overengineered / wrong direction |
| STOP_STALE | Abandon | Goal stale (>14 days inactive) |
| ESCALATE | Prioritize immediately | Blocks critical goals |
| BLOCKED | Blocked by dependency | Unresolved blocker |

## PLN Truth Values

Each node gets a `TruthValue(strength, confidence)`:
- **strength**: How true/relevant the node is (0-1)
- **confidence**: How certain we are (0-1)

Propagation:
- AND (conjunction): min strength, confidence product
- OR (disjunction): max strength, confidence product
- NOT (negation): 1-strength, same confidence
- Evidence: accumulated from incoming edges

## ECAN Attention

Each node gets `AttentionValue(sti, lti, vlti)`:
- **STI** (Short-Term Importance): From PLN relevance, decays each cycle
- **LTI** (Long-Term Importance): From PLN confidence, decays slowly
- **VLTI** (Very Long-Term Importance): Rent-free for terminal nodes

Dynamics per cycle:
1. Rent: Non-VLTI nodes pay RENT from STI
2. Decay: STI *= (1 - STI_DECAY), LTI *= (1 - LTI_DECAY)
3. Spread: STI flows along edges (SPREAD_FACTOR)
4. Eviction: Nodes below STI_FLOOR become eviction candidates

## MeTTa Bridge

The MeTTa-Python Bridge (v0.3) provides a declarative alternative:
- `schema.metta`: Verdict rules in MeTTa syntax
- `metta_evaluator.py`: Evaluates MeTTa against graph data
- Cross-validated against pure-Python evaluator (5/5 episodes match)

## Test Coverage

| Module | Tests | Status |
|--------|-------|--------|
| relevance_evaluator | 81 | ✅ |
| pln_propagation | 18 | ✅ |
| pln_truth_mapping | 13 | ✅ |
| pln_verdict_bridge | 12 | ✅ |
| ecan_attention | 13 | ✅ |
| integrated_governor | 7 | ✅ |
| metta_evaluator | 16 | ✅ |
| graph_to_metta | 5 | ✅ |
| **Total** | **165** | ✅ |

(Note: pytest counts 113 test functions; subtests expand to 185+)

## Replay Corpus

5 episodes covering the full verdict spectrum:
1. Stale codegen → STOP_STALE
2. Chem blocking → ESCALATE + PAUSE_RECOVERABLY
3. Premature hardening → DEFER
4. Overengineered repair → REPLAN
5. Justified long-running → CONTINUE (control)

## Integration Points

- **WMTM**: ECAN can allocate attention across cognitive cycles
- **Conversation Governor**: Verdicts can inform egress decisions
- **Iter-port**: Pipeline can run as a periodic background evaluator

## Future Directions

1. **Live enforcement**: Actually interrupting/prioritizing tasks
2. **Deeper PLN chains**: Multi-hop probabilistic reasoning
3. **Learning**: Adjusting PLN weights from historical outcomes
4. **WMTM ECAN**: Attention allocation for cognitive cycles
