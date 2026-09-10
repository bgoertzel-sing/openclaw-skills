# Goal Relevance Governor — Full Reasoning Explanation Report
Generated: 2026-09-08

## Episode: episode_01_stale_codegen.json
Verdicts: {'STOP_STALE': 1}
Multi-hop: 2 chains, max_depth=2
Conflicts: 0

# Reasoning Explanations

Episode: 01-stale-codegen-worker
Timestamp: 2026-09-01T12:00:00+00:00

### t-p2m-codegen - STOP_STALE
**Task is stale and no longer relevant to active goals.**

**Evidence:**
  - all_direct_goals_terminal
  - Temporal staleness detected - goals goals=['g-initial-demo', 'g-build-omegaclaw'] may have shifted
  - Zero relevance - no active goal connection detected

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-build-omegaclaw (g-build-omegaclaw), g-initial-demo (g-initial-demo)

**Action:** Stop: goal is stale and no longer relevant. Consider abandoning.

_STI=12.9, LTI=63.3 | flagged stale_
---


## Episode: episode_02_chem_blocking.json
Verdicts: {'PAUSE_RECOVERABLY': 1, 'ESCALATE': 1}
Multi-hop: 4 chains, max_depth=2
Conflicts: 1

# Reasoning Explanations

Episode: 02-chem-blocking-restoration
Timestamp: 2026-08-20T14:00:00+00:00

### t-restore-agents - ESCALATE
**Task blocks critical goals and needs immediate attention.**

**Evidence:**
  - Task targets multiple active goals but produces no evidence
  - Task connected to 2 active goal(s)
  - High relevance score (0.939) - strongly connected to active goals

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-restore-agents (g-restore-agents), g-build-omegaclaw (g-build-omegaclaw)

**Resource conflicts:** contends with t-petta-chem (t-petta-chem) for r-shared-runtime (r-shared-runtime) (competing goals)

**Action:** Escalate: this task blocks critical goals. Prioritize immediately.

_STI=39.6, LTI=63.3_
---

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
---


## Episode: episode_03_premature_hardening.json
Verdicts: {'DEFER': 1}
Multi-hop: 1 chains, max_depth=1
Conflicts: 0

# Reasoning Explanations

Episode: 03-premature-hardening
Timestamp: 2026-08-25T10:00:00+00:00

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
---


## Episode: episode_04_overengineered_repair.json
Verdicts: {'REPLAN': 2}
Multi-hop: 4 chains, max_depth=2
Conflicts: 0

# Reasoning Explanations

Episode: 04-overengineered-repair
Timestamp: 2026-08-22T16:00:00+00:00

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
---

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


## Episode: episode_05_control_justified_long_running.json
Verdicts: {'CONTINUE': 1}
Multi-hop: 2 chains, max_depth=2
Conflicts: 0

# Reasoning Explanations

Episode: 05-control-justified-long-running
Timestamp: 2026-09-05T10:00:00+00:00

### t-run-benchmark - CONTINUE
**Task is justified and should continue running.**

**Evidence:**
  - healthy
  - Temporal staleness detected - goals goals=['g-wmtm-validation', 'g-build-omegaclaw'] may have shifted
  - High relevance score (0.925) - strongly connected to active goals
  - High short-term attention (STI=50.2) - system is focused here

**Multi-hop chains:** 2 chain(s) reaching 2 goal(s) at max depth 2: g-build-omegaclaw (g-build-omegaclaw), g-wmtm-validation (g-wmtm-validation)

**Action:** Proceed with current task as planned.

_STI=50.2, LTI=63.3 | flagged stale_
---

