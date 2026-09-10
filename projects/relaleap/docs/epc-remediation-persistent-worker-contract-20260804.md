# ePC Remediation Persistent Worker Contract

Date: 2026-08-04
Owner: Benjamin Goertzel
Parent session: `agent:main:telegram:direct:402314199`
Worker session: `relaleap-epc-remediation`

## Objective

Execute, in order, the remediation programme in Appendix A of the supplied
diagnostic preserved at
`../../library/relaleap-epc-diagnosis-20260804/diagnosis.pdf`: standing rules,
mechanism gates MG-1--MG-8, M0, C1, C2, and C3. Treat the document's diagnoses
and thresholds as hypotheses/proposed contracts until independently checked
against primary sources, reference code, analytic controls, and the existing
RelaLeap implementation.

## Milestones

1. **A0 source and instrument audit:** read the EO/ePC paper and reference
   implementation; write the required method summary; determine sPC versus
   EO/ePC identity from code; audit r5 NLL units, uniform/untrained/oracle
   baselines, train/eval correspondence, and perturbation target independence.
2. **MG implementation:** implement and test MG-1--MG-8, including convergence
   residuals and fixed-point conditioning. Preserve historical failures as
   named regressions where feasible.
3. **M0:** run analytic float64 deep-linear equivalence at declared depths,
   widths, and lambda values for both legacy and corrected paths.
4. **C1:** after M0 passes, port/wrap the reference EO implementation and
   execute conversion-by-homotopy on a competent transformer using a shared,
   modular graph definition.
5. **C2:** run the preregistered cap-readiness battery along the admissible
   lambda path.
6. **C3:** only if C1/C2 admit a lambda window, execute the matched-cap
   falsifier with disjoint exploration/selection/confirmation seeds.

Each milestone begins with a frozen plain-language specification and an
experiment ledger. Failure of a gate is an informative milestone outcome; do
not weaken or tune a frozen gate on its science seeds. A failed milestone may
require a bounded repair and rerun, but must not be silently skipped.

## Authority and non-goals

- Local read/write, branches/worktrees, tests, CPU experiments, paper/reference
  retrieval, and coherent local commits are authorized.
- Preserve unrelated dirty work. Use an isolated task branch/worktree for
  implementation.
- No public push, PR, release, remote message, paid service, or GPU provisioning
  without new explicit authorization.
- If GPU compute becomes scientifically justified, stop with
  `BLOCKED_AUTHORITY` and send the parent a proposal stating provider/account,
  hardware/count, image, storage/region, duration, estimated cost, data plan,
  stop/termination conditions, and artifact-return path. The parent will ask
  Ben. Continue any independent CPU-safe work meanwhile.
- Do not claim the external diagnosis is correct until the corresponding audit
  or mechanism gate supplies evidence.

## Persistence, evidence, and reporting

- Work inexorably through the next admissible step. Do not wait for routine
  choices; make and record conservative assumptions.
- On every activation, reload this contract, `PROJECT.md`, `TASKS.md`,
  `DECISIONS.md`, recent relevant `RUN.md` files, and the last worker state.
- Maintain `experiments/epc-remediation-worker/STATE.md` with current milestone,
  branch/commit, dirty state, last command/result, evidence paths, next command,
  heartbeat classification, and blockers.
- Write a checkpoint after each meaningful unit and at least every 30 minutes
  of active work. Use `active_with_new_evidence`, `alive_no_new_evidence`, or
  the terminal vocabulary from the subagent execution contract.
- Two expected checkpoints without new evidence trigger self-audit; three
  require a restart/recovery record or explicit blocker. Never run two writers
  on the same worktree.
- At each completed milestone, write the concise report into `STATE.md` with
  `COMPLETE_VERIFIED`, observed evidence, exact acceptance command/result,
  artifact paths/hashes, scientific interpretation, remaining uncertainty, and
  the next milestone. The parent-side monitor relays newly recorded milestones
  to Ben. Direct `sessions_send` and cross-session cron wake are unavailable
  under scheduler isolation; do not repeatedly attempt either route. Record
  genuine blockers in `STATE.md` immediately.
- Continue automatically after reporting unless the next step crosses an
  authority boundary or depends on a material decision that cannot safely be
  inferred.

## Acceptance

The programme is complete only when C3 reaches a verified terminal result or
an earlier stage produces a scientifically decisive, properly validated
terminal failure that makes later stages inadmissible. All results must be
reproducible from recorded commits, commands, environments, configurations,
seeds, and machine-readable artifacts.

## First command

Perform the mandatory startup handshake, create the worker state and A0
experiment ledger, then inspect the legacy relaxation variables and r5 metric
reduction before making any scientific claim.
