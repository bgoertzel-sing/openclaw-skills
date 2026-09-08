---
name: "subagent-execution-contract"
description: "Artifact-backed launch, progress, recovery, and verification contract for one-off and persistent subagents."
---

# Subagent Execution Contract

Use this skill whenever delegating implementation, research execution, document production, or other artifact-bearing work to one-off or persistent subagents.

## Core invariant

A subagent is progressing only when independently verifiable evidence exists. Narrative status is never evidence by itself.

Evidence is one or more of:

- a concrete artifact path with observed size/hash or diff;
- a running process/session identifier with fresh output;
- a test/command record with exit status and log path;
- a committed, reviewable change;
- an external job identifier whose state the parent independently checks.

## Parent pre-dispatch contract

Before dispatch, specify:

1. exact workspace and target repository/worktree;
2. bounded deliverable and explicit non-goals;
3. acceptance test;
4. first command;
5. evidence path(s);
6. authority boundaries, especially paid compute, external writes, destructive actions, and secrets;
7. completion status vocabulary below.

For implementation work, require an isolated branch/worktree when the repository policy calls for it. Preserve existing user changes.

## Mandatory startup handshake

The subagent's first actions are read-only sanity checks:

1. `pwd`;
2. target workspace existence and repository identity;
3. `git status --short --branch` when applicable;
4. read the target task/spec and one relevant source or test file;
5. verify write/tool access with a non-destructive mechanism appropriate to the task before promising implementation.

The subagent must return or record a startup checkpoint containing workspace, branch, first inspected file, and next command.

If any startup command/tool is rejected, unavailable, or cannot reach the intended workspace, stop immediately with `BLOCKED_ENVIRONMENT`. Include the exact failed operation and error, and state explicitly that no artifact was produced. Do not emit a normal completion summary.

## Status vocabulary

Use exactly one terminal status:

- `COMPLETE_VERIFIED`: acceptance test passed and evidence paths are supplied.
- `PARTIAL_EVIDENCE`: concrete artifacts exist but acceptance is not yet met; list the next command.
- `BLOCKED_ENVIRONMENT`: tool, relay, workspace, dependency, or runtime prevented meaningful execution.
- `BLOCKED_AUTHORITY`: progress needs user approval or materially expanded authority.
- `BLOCKED_SPEC`: a missing decision would materially change the implementation.
- `FAILED_TEST`: implementation exists but the acceptance test failed; preserve logs/artifacts.

A plain `complete`, `done`, or narrative result without the status and evidence is protocol-invalid.

## One-off subagents

- The first checkpoint must occur after the startup handshake and before extended reasoning.
- For tasks expected to exceed one checkpoint, produce the first concrete artifact early: a focused test, skeleton, ledger, or source change.
- Never treat analysis-only output as implementation completion.
- Before `COMPLETE_VERIFIED`, run the narrowest acceptance test, report its exact command/exit status, and identify changed artifacts.
- The parent independently checks repository status, artifact existence/hash, and the claimed test result before accepting completion.

## Persistent subagents

Persistent workers additionally require:

1. a durable obligation record containing deliverable, acceptance test, next command, and evidence path;
2. a stable session/worker identifier and restart instructions;
3. bounded checkpoint cadence by meaningful work unit or at least every 30 minutes during active execution;
4. tested coherent commits/checkpoints after each slice when appropriate;
5. heartbeat records that distinguish `active_with_new_evidence`, `alive_no_new_evidence`, and terminal statuses;
6. a stall rule: two consecutive expected checkpoints without new evidence triggers parent inspection; three triggers restart/replacement or an explicit blocker report;
7. resumability: record current branch/commit, dirty state, running process, last successful command, next command, and artifact/log locations;
8. clean handoff: no duplicate worker may mutate the same worktree concurrently.

An alive process without new artifacts is not progress. A persistent worker must never silently transform a blocked state into a completion-shaped message.

## Parent verification gate

Before relaying success to the user, the parent must independently verify, as applicable:

- exact expected files exist;
- `git status`/diff matches the task scope;
- artifact hashes or schemas validate;
- acceptance command exits zero and intended assertions/metrics pass;
- claimed external jobs exist or are terminated as stated;
- no paid resource remains unintentionally active;
- durable task/project records are updated.

If verification fails, report `not done` and continue/recover; do not forward the subagent's claim as fact.

## Recovery behavior

- `BLOCKED_ENVIRONMENT`: parent tests the same minimal operation. If parent works, take over directly or launch a fresh worker only after checking the relay path. If parent also fails, preserve the blocker and avoid repeated blind respawns.
- No artifacts after a supposed implementation turn: classify as orchestration failure, tighten the deliverable to one concrete slice, and do not count the turn as progress.
- Partial artifacts: inspect and continue from them; do not restart from scratch unless unsafe or invalid.
- Persistent stall: capture logs/status, prevent concurrent mutation, resume from the last verified checkpoint or replace the worker with an explicit handoff.

## Reporting

User-facing updates must separate:

- Observed evidence;
- Inferred state;
- Remaining acceptance gap;
- Next active command.

Never say "working on it" until an implementation process/test is actually running or a concrete artifact has been created.
