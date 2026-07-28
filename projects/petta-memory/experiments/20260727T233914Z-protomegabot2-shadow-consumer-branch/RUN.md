# Run 20260727T233914Z-protomegabot2-shadow-consumer-branch: protomegabot2-shadow-consumer-branch

- Project: `petta-memory`
- Started: `2026-07-27T23:39:14Z`
- Finished: `2026-07-27T23:39:14Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/protomegabot2/projects/protomegabot2/worktrees/petta-memory-shadow-consumer`

## Question

Can ProtoMegaBot2 consume a complete PeTTa-memory usability bundle through a
narrow public read-only interface, reproduce the same candidate context after
restart, and leave every source artifact unchanged?

## Hypothesis or expected behavior

The frozen schema-v2 bundle will be admitted, one known episode and recorded
pi-PLN pass result will produce deterministic bounded context, and before/after
source hashes will match exactly.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: deterministic provider-free bundle generated
  from PeTTa-memory commit `41dfdda`; no random seed.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Output JSON SHA-256:
  `2d9c58fe53d2f2242cae2931847a3c36a34b5f904f65063a2145deac9ca6356e`.

## Interpretation

**Observed:** the consumer admitted the integrity-bound bundle, retrieved
clusters `mc-e2e-request`, `mc-e2e-commitment`, and `mc-e2e-artifact`, consumed
the recorded `passed` inference, and emitted bounded prompt/index context.
Two independent invocations were byte-identical. The complete source-artifact
hash inventory was identical before and after, and no ThreadKeeper state was
opened.

**Reproduced:** eight focused positive/adversarial tests passed separately,
covering restart equivalence, tampering, malformed summary JSON, wrong schema,
missing artifacts, and undeclared/ambiguous artifacts.

**Boundary:** provider, Telegram, canonical-memory writes, promotion, and live
ProtoMegaBot2 activation remained disabled.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it. The referenced
source bundle is the output of
`20260727T233708Z-protomegabot2-shadow-source-bundle`.

## Follow-up

Use this adapter in one bounded private `@protomega2bot` response only after the
separate staging credential and supervisor gates pass.
