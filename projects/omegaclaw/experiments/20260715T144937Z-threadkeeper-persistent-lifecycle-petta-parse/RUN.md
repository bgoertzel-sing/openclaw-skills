# Run 20260715T144937Z-threadkeeper-persistent-lifecycle-petta-parse: threadkeeper-persistent-lifecycle-petta-parse

- Project: `omegaclaw`
- Started: `2026-07-15T14:49:37Z`
- Finished: `2026-07-15T14:49:37Z`
- Status: `invalidated`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegaclaw/worktrees/threadkeeper-persistent-workers`

## Question

Does the first MeTTa lifecycle policy parse under the pinned local PeTTa/SWI
runtime, and does its compiled form represent an unambiguous verdict?

## Hypothesis or expected behavior

The file should parse and compile each policy query to one deterministic
ALLOW/DENY or True/False result.

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
- The process exited 0 and parsed all clauses, but inspection of the generated
  Prolog exposed an ambiguous/incorrect transition expression: ALLOW and DENY
  were captured inside a partially applied `or`, rather than as the two `if`
  branches.

## Interpretation

Exit status alone was a false success signal. The initial specific-clause plus
fallback design was already replaced by a single total expression to avoid
multi-match results, but this first rewrite had a parenthesis error that still
parsed into the wrong semantics. This run is invalidated and preserved as a
failure-literacy record; the corrected gate is
`20260715T145130Z-threadkeeper-persistent-lifecycle-v1-fixed`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Require generated-clause inspection or direct query assertions in addition to
parse/exit checks for MeTTa policy gates.
