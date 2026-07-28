# 2026-07-26 — RelaLeap online causal-support Phase 0

Implemented online gradient-ratio/cosine/Fisher support scoring, CKA and
Hutchinson utilities, sigmoid gradient gates, a planted routed fixture, tests,
and a five-arm local runner at `agent/online-causal-epc` commit `83abac8`.
Phase 0 failed closed: support AUC/gate action/oracle retention passed, but the
protected mixed-Hessian baseline was identically zero and signed ablations did
not establish load-bearing pathways. Shakespeare was not run. Full suite:
429 passed, 1 skipped. Evidence:
`projects/relaleap/experiments/20260726T080000Z-online-causal-epc/`.
