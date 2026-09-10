# V4 functional gate: nonlinear Torch

- Status: COMPLETE — INCONCLUSIVE
- Started (UTC): 2026-07-28T16:21:49Z
- Completed (UTC): 2026-07-28T16:36:50Z
- Project: RelaLeap
- Question: Does the float64 CPU `approximate_full_state_AD` tangent predict
  actual paired CRN `torch.optim.Adam` intervention effects better than the
  frozen-D baseline on the frozen nonlinear V4-0 fixtures?
- Implementation:
  `projects/omegaclaw/workspace/relaleap-v4/comcrit/comcrit/`
- Command: `command.sh`
- Raw result: `artifacts/results.json`
- Logs: `stdout.log`, `stderr.log`

Attempt 1 exited 2 before experiment execution because `command.sh` did not
change into the implementation directory. Its logs are retained as
`*.attempt1.*`; the corrected command changes directory before invoking the
same frozen runner.

Attempt 2 completed, but pre-verdict review found that the synergy report used
the final propagated tangent rather than the injected one-step tangent, and
that a failed frozen 5-sigma admission precheck was labelled `FAIL` rather
than `INCONCLUSIVE`. The raw attempt-2 record is retained as `*.attempt2.*`
and `artifacts/results.attempt2.json`. Attempt 3 changes only these two
reporting/implementation defects; no fixture setting or threshold changed.

The gate and thresholds are those frozen in
`docs/causal_critic_v4_c4prime_execution_plan_20260727.md`; they were not
changed for this run.

## Conclusion

**INCONCLUSIVE.** The frozen family-admission precheck requires median
strong-action effect at least 5 sigma. B1 input permutation measured 5.741
sigma, but B2 output shift measured 3.033 sigma and B1 high-LR stress measured
0.868 sigma. Therefore the confirmation-like metrics below are descriptive
and cannot declare a V4-0 pass or fail.

Across horizons 1/2/5/10/25, full-state Spearman was respectively
0.99998/0.99996/0.99996/0.99995/0.99987 for B1, versus frozen-D
0.99998/0.99975/0.99635/0.98880/0.95391; 0.99994/0.99994/0.99984/
0.99991/0.99949 for B2, versus 0.99994/0.99728/0.98763/0.97107/0.90357;
and 0.99992/0.99824/0.98952/0.99853/0.96859 for high-LR B1, versus
0.99992/0.46333/0.57338/0.47350/0.19645. Full-state median relative error
was at most 0.42% in the ordinary-LR families and 2.64% in stress, while
frozen-D reached 89.3% and 99.9%. One-step planted-pair synergy Spearman was
0.9987/0.9996/0.9987. The aligned zero-gradient control produced exactly zero
effects and a 0% false-beneficial rate.

All other recorded frozen checks were true: rank >= .5, identified sign AUROC
>= .75, synergy rank >= .6, null false-benefit <=5%, an h<=5 valid cell,
full-state non-inferiority in every cell, and >=.15 stress-cell improvement.
They do not override the failed admission precheck.

## Reproducibility and evidence

- Exit status: 0; wall time: 361.41 s; peak RSS: 307532 KiB.
- Result SHA-256:
  `3e8be47bbb947c4092cea3e5fa0c32d9b09de5c327db518e391021b0c1e9444e`.
- Focused tests: `2 passed`.
- Full packaged suite: `7 passed, 4 failed, 1 skipped`; the four retained
  failures are the previously documented Torch optimizer-replica bit-exactness
  conformance diagnostics. See `tests.log`.
- Environment and repository state: `env.txt`.
- Final raw evidence: `artifacts/results.json`, `stdout.log`, `stderr.log`,
  `time.txt`, `exit_status.txt`.
- The attempt-2 output is retained because it exposed the corrected synergy
  reporting defect: `artifacts/results.attempt2.json`.
