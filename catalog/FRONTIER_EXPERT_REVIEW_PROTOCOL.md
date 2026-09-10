# Frontier Expert Review Protocol

Date adopted: 2026-07-27  
Decision owner: Benjamin Goertzel

## Purpose

Automated frontier-model reviews must evaluate whether a project is advancing
its original scientific or engineering goals, not merely summarize recent
activity or suggest incremental extensions. The petta-chem review failure is
the motivating counterexample: routine rule accretion was accepted although an
independent Fable review recognized that it was strategically unproductive.

## Required staged workflow

### Stage 0 — Evidence packet

Create a systematic, reproducible PDF describing:

- original and current project goals;
- starting theories/design documents (attach the most relevant one or two);
- work completed, including failed and negative results;
- exact experimental setup, code/commit/data identities, and limitations;
- current plan, unresolved decisions, and resource constraints;
- an explicit “activity versus goal progress” table.

The packet must be self-contained enough for an expert model to detect a
locally productive but globally useless loop.

### Stage 1 — Independent diagnosis

Give the frontier model the evidence packet and original documents. Do **not**
ask for a coding plan in this query. Ask it to:

1. assess results and direction against the original and overall goals;
2. identify activity that is not producing decision-relevant information;
3. explain successes, failures, and anomalies theoretically or mathematically
   where possible;
4. state whether the evidence changes its underlying model of the project;
5. identify missing controls, invalid estimators, alternative hypotheses, and
   the strongest falsification tests;
6. separate observed facts, inferences, hypotheses, and recommendations.

This separation reduces anchoring on the incumbent implementation plan.

### Stage 2 — Adjudication

Compare the diagnosis against project records and measured evidence. Preserve
disagreement rather than averaging it away. If the diagnosis implies no
strategic change, record why. If it implies a pivot, freeze the diagnosis
before requesting a new plan.

### Stage 3 — Revised agent plan

In a separate model query, supply the frozen diagnosis and ask for a revised,
dependency-ordered plan for coding agents. Require:

- smallest decision-relevant experiments first;
- explicit stop, pivot, and acceptance gates;
- validation of detectors/estimators against an independent oracle;
- named artifacts, tests, commands, and evidence paths;
- separation of local/zero-cost work from approval-gated external actions;
- prohibition on further feature accretion unless it resolves a named
  uncertainty.

### Stage 4 — Optional executable probe

When useful and safe, ask the frontier model to run a bounded sandbox
experiment or provide minimal code that tests a disputed mechanism. Treat
supplied outputs as unverified until reproduced in the project environment.

## Automation policy

- A single-pass “review progress and propose next steps” prompt is deprecated.
- Expert review must be at least two model calls: diagnosis, then planning.
- Preserve prompts, model/route metadata, attached document hashes, responses,
  and adjudication.
- Prefer independent reviews by two frontier models for high-impact pivots;
  record disagreements explicitly.
- Review quality is assessed by whether the review catches known planted or
  retrospective strategic failure modes, not by eloquence or plan length.
- No review may authorize paid compute, deployment, merging, or semantic
  changes; existing approval gates remain in force.
