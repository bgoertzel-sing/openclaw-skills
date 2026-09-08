# Goal Relevance Governor — Comprehensive Review
Date: 2026-09-08
Version: v0.2 (PLN + ECAN + Multi-hop + Conflict + Explanation + Temporal)

---

## Episode Summary

| Episode | Type | Verdict | Chains | Max Depth | Conflicts | STI |
|---------|------|---------|--------|-----------|-----------|-----|
| stale | episode_01_stale_codegen.json | STOP_STALE:1 | 2 | 2 | 0 | 12.9 |
| conflict | episode_02_chem_blocking.json | PAUSE_RECOVERABLY:1, ESCALATE:1 | 4 | 2 | 1 | 39.6 |
| premature | episode_03_premature_hardening.json | DEFER:1 | 1 | 1 | 0 | 44.2 |
| overengineered | episode_04_overengineered_repair.json | REPLAN:2 | 4 | 2 | 0 | 3.0 |
| control | episode_05_control_justified_long_running.json | CONTINUE:1 | 2 | 2 | 0 | 50.2 |

---

## Episode: stale (episode_01_stale_codegen.json)

### t-p2m-codegen - STOP_STALE
**Task is stale and no longer relevant to active goals.**

**Evidence:**
  - all_direct_goals_terminal
  - Temporal staleness detected - goals goals=['g-initial-demo', 'g-build-omegaclaw'] may have shifted
  - Zero relevance - no active goal connection detected

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-initial-demo (g-initial-demo), g-build-omegaclaw (g-build-omegaclaw)

**Action:** Stop: goal is stale and no longer relevant. Consider abandoning.

_STI=12.9, LTI=63.3 | flagged stale_

### Temporal Simulation

**Step 0:** Initial state: task active, one goal achieved
- Verdicts: {'t-p2m-codegen': 'STOP_STALE'}

**Step 1:** All goals now terminal - task definitely stale
- Verdicts: {'t-p2m-codegen': 'STOP_STALE'}

**Step 2:** Task marked completed
- Verdicts: {}

---

## Episode: conflict (episode_02_chem_blocking.json)

### t-restore-agents - ESCALATE
**Task blocks critical goals and needs immediate attention.**

**Evidence:**
  - Task targets multiple active goals but produces no evidence
  - Task connected to 2 active goal(s)
  - High relevance score (0.939) - strongly connected to active goals

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-build-omegaclaw (g-build-omegaclaw), g-restore-agents (g-restore-agents)

**Resource conflicts:** contends with t-petta-chem (t-petta-chem) for r-shared-runtime (r-shared-runtime) (competing goals)

**Action:** Escalate: this task blocks critical goals. Prioritize immediately.

_STI=39.6, LTI=63.3_

### t-petta-chem - PAUSE_RECOVERABLY
**Task is paused due to recoverable blockers.**

**Evidence:**
  - Resource contention detected - another task needs the same resource
  - Contended resource: r-shared-runtime (r-shared-runtime)
  - Higher priority task t-restore-agents (t-restore-agents) takes precedence
  - Temporal staleness detected - goals goals=['g-long-horizon-research'] may have shifted
  - Low relevance (0.246) - weakly connected to goals

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-long-horizon-research (g-long-horizon-research), g-build-omegaclaw (g-build-omegaclaw)

**Resource conflicts:** contends with t-restore-agents (t-restore-agents) for r-shared-runtime (r-shared-runtime) (competing goals)

**Action:** Pause task — it may recover. Re-evaluate after addressing blockers.

_STI=27.8, LTI=63.3 | flagged stale_

### Temporal Simulation

**Step 0:** Initial state: two tasks contending for resource
- Verdicts: {'t-restore-agents': 'ESCALATE', 't-petta-chem': 'PAUSE_RECOVERABLY'}

**Step 1:** Higher-priority task completed, resource freed
- Verdicts: {'t-petta-chem': 'ESCALATE'}

**Step 2:** Petta-chem resumes without contention
- Verdicts: {'t-petta-chem': 'ESCALATE'}

**Verdict Drift:**
- Step 1: t-petta-chem changed PAUSE_RECOVERABLY → ESCALATE

---

## Episode: premature (episode_03_premature_hardening.json)

### t-hardening-guards - DEFER
**Task is deferred - premature given current state.**

**Evidence:**
  - irreversible_on_early_stage_research
  - project_kind=exploratory_research
  - stage=E0_exploration
  - Moderate relevance (0.341) - partially connected to goals
  - High short-term attention (STI=44.2) - system is focused here

**Multi-hop chains:** 1 chain(s) reaching 1 goal(s) at max depth 1: g-build-omegaclaw (g-build-omegaclaw)

**Action:** Defer this task in favor of higher-priority work.

_STI=44.2, LTI=44.3_

### Temporal Simulation

**Step 0:** Initial state: task is premature
- Verdicts: {'t-hardening-guards': 'DEFER'}

**Step 1:** Project stage advanced to implementation
- Verdicts: {'t-hardening-guards': 'CONTINUE'}

**Verdict Drift:**
- Step 1: t-hardening-guards changed DEFER → CONTINUE

---

## Episode: overengineered (episode_04_overengineered_repair.json)

### t-process-inspector - REPLAN
**Task needs replanning - approach is not working.**

**Evidence:**
  - goal_superseded
  - superseded_goal=g-restore-agents-original
  - superseded_by=g-restore-agents-v2
  - Zero relevance - no active goal connection detected
  - Low short-term attention (STI=3.0) - system has deprioritized this

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-build-omegaclaw (g-build-omegaclaw), g-restore-agents-original (g-restore-agents-original)

**Action:** Replan: the task approach needs revision before proceeding.

_STI=3.0, LTI=63.3 | eviction candidate_

### t-launch-wrappers - REPLAN
**Task needs replanning - approach is not working.**

**Evidence:**
  - goal_superseded
  - superseded_goal=g-restore-agents-original
  - superseded_by=g-restore-agents-v2
  - Zero relevance - no active goal connection detected
  - Low short-term attention (STI=3.0) - system has deprioritized this

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-build-omegaclaw (g-build-omegaclaw), g-restore-agents-original (g-restore-agents-original)

**Action:** Replan: the task approach needs revision before proceeding.

_STI=3.0, LTI=63.3 | eviction candidate_

---

## Episode: control (episode_05_control_justified_long_running.json)

### t-run-benchmark - CONTINUE
**Task is justified and should continue running.**

**Evidence:**
  - healthy
  - Temporal staleness detected - goals goals=['g-wmtm-validation', 'g-build-omegaclaw'] may have shifted
  - High relevance score (0.925) - strongly connected to active goals
  - High short-term attention (STI=50.2) - system is focused here

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-wmtm-validation (g-wmtm-validation), g-build-omegaclaw (g-build-omegaclaw)

**Action:** Proceed with current task as planned.

_STI=50.2, LTI=63.3 | flagged stale_

---

## Architecture Summary

```
Episode Data (JSON)
        │
        ▼
┌─────────────────────┐
│  PLN Truth Values    │  ← pln_truth_mapping.py
│  (AND/OR/NOT, TV)    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  ECAN Attention      │  ← ecan.py
│  (STI/LTI spread)    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Verdict Bridge      │  ← verdict_bridge.py
│  (7 verdict rules)   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Multi-hop Chains    │  ← pln_multihop.py
│  (DFS task→goal)     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Conflict Detection  │  ← pln_multihop.py
│  (resource contention)│
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Reasoning Explainer │  ← reasoning_explainer.py
│  (human-readable)    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Temporal Simulator  │  ← temporal_simulator.py
│  (state mutations)   │
└─────────────────────┘
```

**Total tests: 166 tests, 132 subtests — ALL PASSING**
**Git commits this session: 16**