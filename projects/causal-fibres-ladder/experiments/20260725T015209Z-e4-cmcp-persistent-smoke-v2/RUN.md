# Run 20260725T015209Z-e4-cmcp-persistent-smoke-v2: e4-cmcp-persistent-smoke-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T01:52:09Z`
- Finished: `2026-07-25T01:52:23Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the E4/CMCP persistent-ledger implementation complete the frozen
eight-episode duplicate-burst protocol and emit all required arm metrics while
leaving model parameters unchanged?

## Hypothesis or expected behavior

The runner should emit eight episodes for naive, CMCP, direction-only, and
oracle accounting. Naive precision should inflate under recurring duplicates;
CMCP should suppress duplicate contributions while retaining new innovations.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seed: `61001`.
- Configuration: `configs/e4_cmcp_persistent_calibration_v1.json`.
- Code base: commit `9ed922d` plus the recorded dirty implementation diff.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

The artifact contains eight episodes and all four arms. Every arm/episode has
current task loss/accuracy, ECE, Brier, effective precision, episode-1
retention, and task-loss headroom. Model weights remained unchanged.

Episode-8 effective precision was naive `26.0`, CMCP `6.08905`,
direction-only `1.0`, and oracle `9.0`. CMCP versus naive episode-8 ECE was
`0.20604` versus `0.30972`; episode-1 retention accuracy was `0.85938` versus
`0.72656`; and current accuracy was `0.85156` versus `0.20313`. Artifact
SHA-256: `aa6206eed66333683a8fc4dfd6b1bc5739df96c90175672d5bac79436a04a253`.

## Interpretation

The implementation and output contract pass this smoke. CMCP materially limits
the naive duplicate burst on this seed, but does not stabilize in the
provisional `[1,3]` band because the protocol deliberately adds one genuinely
new innovation per episode. Oracle precision reaches `9.0` for the same
reason. Those provisional CMCP/oracle ranges cannot be frozen without either
changing the evidence semantics or contradicting the stated protocol.

This is a one-seed operational result, not calibration or confirmation.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run all three calibration seeds, summarize episode trajectories, and freeze
confirmation thresholds from the resulting evidence rather than the
incompatible provisional precision ranges.
