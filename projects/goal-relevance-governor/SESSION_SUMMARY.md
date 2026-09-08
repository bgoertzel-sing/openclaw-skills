# Session Summary — 2026-09-08

## ECAN Staleness LTI Decay + Eviction Floor

### Commits (4 pushed to agent/protomega-long-document-repair):

1. **4db9035** — `feat: ECAN staleness LTI decay`
   - ECANAttentionAllocator accepts optional `now` parameter
   - Nodes with as_of > 14 days get LTI × 0.5 (STALENESS_LTI_DECAY)
   - Stale goals become natural eviction candidates over time
   - Mirrors PLN-Verdict Bridge staleness confidence decay
   - New test: `test_lti_staleness_decay`

2. **af79d61** — `fix: pass now to ECANAttentionAllocator in IntegratedGovernorPipeline`
   - Ensures staleness LTI decay activates in full pipeline mode

3. **4b78088** — `feat: add LTI_FLOOR eviction threshold`
   - New constant: LTI_FLOOR = 5.0
   - Nodes with LTI < LTI_FLOOR become eviction candidates (even if STI > STI_FLOOR)
   - VLTI nodes still protected from eviction

4. **af5662a** — `test: add test_lti_floor_eviction`
   - Verifies LTI floor eviction logic with manual LTI override

### Test Results
- 200 tests pass, 170 subtests pass (1.40s)
- Full pipeline verified on all 6 replay episodes
- Episode 1: t-p2m-codegen EVICT (STI=5.6, LTI=57.2, STOP_STALE)
- Episode 4: t-process-inspector + t-launch-wrappers EVICT (STI=-1.6, REPLAN)

### Key Architecture
```
Staleness → LTI Decay (×0.5) → LTI_FLOOR check → Eviction Candidate
                                                    ↓
                                              VLTI protection
```

### Next Steps
- Deeper PLN/Atomspace integration (exploratory)
- Awaiting Ben approval for live enforcement
- Consider dynamic LTI_FLOOR based on working memory pressure
