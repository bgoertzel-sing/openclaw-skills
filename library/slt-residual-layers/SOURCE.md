# Source: SLT and Residual Layers

- Type: `PDF`
- Authors/organization: Ben Goertzel / ChatGPT conversation export (as forwarded in Telegram)
- Publication/version date: 2026-07-02
- Retrieved: `2026-07-02`
- Canonical URL or identifier: Telegram attachment `SLT and Residual Layers.pdf`; visible source URL in PDF text: `https://chatgpt.com/c/6a46ad45-5bd4-83ea-aaf9-79bca7f5e110`
- Local source path: `library/slt-residual-layers/SLT-and-Residual-Layers.pdf`
- Extracted text path: `library/slt-residual-layers/extracted.txt`
- SHA-256: PDF `bffc373dc65f02649269dde1d6cbe0ec0128d618e2cee9d2a021d17af82989c4`; extracted text `38c4510dbbe54d032832c5528da04dc3da1121011020f29103100b520f0dea7e`
- License/access constraints: local project guidance from forwarded chat/PDF; do not redistribute without confirmation.
- Privacy tier: `local-private`
- Tags: RelaLeap, SLT, residual layers, transformer residuals, local learning coefficient, commutator, Hessian, basis pregate
- Related projects: RelaLeap; OmegaClaw/Protobots coordination

## Summary

Ben forwarded this document as the new direction for the RelaLeap project. The document reframes RelaLeap as an SLT-informed structure-learning problem over candidate residual factorizations. The key shift is away from selecting a basis because it reconstructs teacher residuals well, and toward promoting only residual columns/factorizations whose local evidence decomposes, whose interaction remainder is dominated, whose causal fingerprints are stable, and whose update fields approximately commute.

## Key claims or contents

- A residual layer is disentangled when excess loss locally factorizes as `K(theta) ≈ sum_c K_c(theta_c) + R(theta)`, with small/dominated interaction remainder `R`; LLC/free-energy additivity is the central validation signal, not raw activation separability.
- Candidate bases should be scored by an SLT/free-energy style pregate: validation loss plus estimated LLC, prior/simple-structure penalty, commutator leakage, off-support gradient leakage, support regret, and interaction/Hessian coupling.
- The next RelaLeap pregate should compare seven matched arms: same-router flat value control; SVD/low-rank dense control; orthogonal sparse-coding diagnostic basis; non-orthogonal learned dictionary; CE-gradient-aligned dictionary; Fisher/Gauss-Newton-aligned dictionary; rank-one atom dictionary with on-center/off-surround column formation.
- The transformer hidden state may remain superposed; the operational target is a sparse, context-dependent residual factorization whose evidence geometry decomposes.
- The document includes coding-agent-facing implementation suggestions for files, arm classes, coefficient modes, configs, audits, and interpretation rules for each arm.

## Methods or implementation details

Suggested software structure includes a common `BasisArm` interface with `fit`, `encode`, `decode`, `forward_residual`, and `audit` methods; shared residual caches containing hidden states, dense teacher residuals, logits, targets, context features, masks, and metadata; a unified `PregateScore`; and audit modules for LLC estimation, Hessian/Fisher surrogates, commutators, leakage, support regret, and causal fingerprints.

## Limitations and uncertainties

- The source is a generated research guidance document, not a completed experimental result.
- LLC estimates and Hessian/Fisher/commutator diagnostics will be approximate; the first implementation should treat them as ranking/audit signals rather than theorem-level guarantees.
- RelaLeap work is currently noted as MacBook-side with a worktree cleanup blocker in `catalog/KANBAN.md`; local OpenClaw does not appear to contain the active RelaLeap repository.

## Relevance to current work

This is the current mandate for the next RelaLeap experimental sequence: implement an SLT/causal-factorization pregate and run the seven-arm comparison with matched metrics and fail-closed promotion criteria.

## Quotations or excerpts

> "Do not promote a residual basis because it reconstructs well. Promote it because R is small..."

> "The residual columns are therefore best understood as local charts on the transformer’s failure modes, not as global semantic features."

## Follow-up questions

- Where is the active RelaLeap repository/worktree and which subagent/session should receive the concrete coding mandate?
- Should the first coding slice implement only the shared pregate/audit scaffold, or also the flat/SVD controls as executable baselines?
