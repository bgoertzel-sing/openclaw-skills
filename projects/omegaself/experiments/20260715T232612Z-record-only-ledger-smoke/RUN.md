# Run 20260715T232612Z-record-only-ledger-smoke: record-only-ledger-smoke

- Project: `omegaself`
- Started: `2026-07-15T23:26:12Z`
- Finished: `2026-07-15T23:26:13Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/omegaself/repos/protomegabot2-omegaclaw-record-only`

## Question

When explicitly enabled in an isolated artifact directory, does the bridge append and verify all Phase-2 observation kinds while exposing the root hash?

## Hypothesis or expected behavior

Cycle start, parsed calls, dispatch receipt, policy load, and reasoner invocation should form a valid five-record chain without granting authority.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: startup verified the empty genesis root, five synthetic record-only events appended, and final verification returned 5 records with root `3e300753c800f7c225e0785b1d77fc264162fcd144c253b5f183f678a1d19a42`. The ledger file SHA-256 is `cb4c1487ee549b7a98147cd98799ee85181c93bdb8f13d8cd016596084a9f795`. The policy observation remains explicitly `unverified`; the reasoner observation has `governance_decision: null`. This is a synthetic test ledger, not live self-belief or authorization evidence.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Native loop execution remains gated on a working SWI-Prolog/PeTTa runtime. Proceed next with evidence closure/applicability unit integration in the isolated branch.
