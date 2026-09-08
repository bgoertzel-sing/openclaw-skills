# Temporal Evolution Simulator — Verdict Drift Report

## episode_01_stale_codegen.json (stale timeline)
All correct: True
Verdict drift events: 0

### Step 0: Initial state: task active, one goal achieved
  Verdicts: {'t-p2m-codegen': 'STOP_STALE'}
  Correct: True

### Step 1: All goals now terminal - task definitely stale
  Verdicts: {'t-p2m-codegen': 'STOP_STALE'}
  Correct: True

### Step 2: Task marked completed
  Verdicts: {}
  Correct: True

---

## episode_02_chem_blocking.json (conflict timeline)
All correct: True
Verdict drift events: 0

### Step 0: Initial state: two tasks contending for resource
  Verdicts: {'t-restore-agents': 'ESCALATE', 't-petta-chem': 'PAUSE_RECOVERABLY'}
  Correct: True

### Step 1: Higher-priority task completed, resource freed
  Verdicts: {'t-petta-chem': 'PAUSE_RECOVERABLY'}
  Correct: True

### Step 2: Petta-chem resumes without contention
  Verdicts: {'t-petta-chem': 'PAUSE_RECOVERABLY'}
  Correct: True

---

## episode_03_premature_hardening.json (premature timeline)
All correct: True
Verdict drift events: 0

### Step 0: Initial state: task is premature
  Verdicts: {'t-hardening-guards': 'DEFER'}
  Correct: True

### Step 1: Project stage advanced to implementation
  Verdicts: {'t-hardening-guards': 'DEFER'}
  Correct: True

---
