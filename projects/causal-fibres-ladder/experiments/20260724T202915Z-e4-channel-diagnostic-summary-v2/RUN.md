# Run 20260724T202915Z-e4-channel-diagnostic-summary-v2: e4-channel-diagnostic-summary-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:29:15Z`
- Finished: `2026-07-24T20:29:16Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Is the prior weak E4 symbolic recovery primarily limited by incomplete
factor information, low constraint weight, or hidden-state settlement?

## Hypothesis or expected behavior

Full four-factor information should exceed two-factor caps if completeness
binds; recovery should increase with weight if consistency penalties dominate;
and direct-logit injection should exceed hidden settlement if the settlement
channel is the bottleneck. This is exploratory and does not revise the frozen
E4 gate.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Durable v2 inputs: corrected per-factor-normalized seed records for
  `12011,13121,14251`, enumerated in `command.sh`.
- Grid: three masks, four multipliers, three channels, ID and CS.
- Repository commit: `6ee569a`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Result SHA256:
  `7921b5bb19722c17dc3e3b65d0d737f209305dacd5868f1f52acfefc172060f7`.
- Reproduction replay produced the identical SHA256 and byte-for-byte
  aggregate output.
- CS baselines: FF loss/accuracy `1.04947/0.95052`; diagnostic TC
  `1.03227/0.96094`.
- At 1x hidden, full4 G=`0.37686` versus two-cap mean `0.18833`.
- At 1x full4, logit G=`0.92634` versus hidden `0.37686` (ratio `2.458`).
- All nine mask/channel series increase strictly through 5x.
- Best CS condition: full4/5x/both, loss `0.97079`, accuracy `0.98438`,
  factor-bit accuracy `0.98893`, task-loss G=`4.55170`.
- Both and direct-logit are numerically indistinguishable:
  maximum absolute G difference `1.16e-5`.

## Interpretation

All three diagnosed factors matter, but the dominant limitations are
constraint strength and the hidden channel. After holding per-factor weight
constant, full4 produces almost exactly twice the recovery of the mean
two-factor cap at matched weight/channel. Recovery remains approximately
linear and strictly increasing through 5x, so the original 1x constraint was
too weak relative to consistency penalties. Direct-logit injection provides
about 2.44--2.46 times hidden-channel recovery; adding hidden settlement to
the logit path changes essentially nothing, identifying hidden settlement as
the channel bottleneck on this rig.

G above one is possible because the full-information direct constraint
outperforms the hidden-state TC diagnostic anchor on task loss. Full4 uniquely
identifies the class in this synthetic grammar, so this is a diagnostic upper
case, not deployability evidence. The original frozen E4 negative result
stands.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

If E4 is redesigned prospectively, test a deployable source of complete
constraints and calibrate constraint/anchor scale explicitly. A direct-logit
constraint adapter is the highest-value next prototype; deeper hidden
settlement alone is not.
