# Monday playground clean-room run

## Status

PASS. The one-command playground completed with exit status 0. The edited
input changed `TASK-ARCHIVE` coverage from unknown to covered, and Hyperon
MeTTa returned exactly one matching acceptance-test/requirement pair:

```text
TASK-ARCHIVE coverage: [(test-25ae20d3b4 req-7e66c5c865)]
```

## Revision and environment

- Run time: 2026-07-28 06:30 UTC
- Repository revision: `990ced38ccd2f041bf0599bae6837a33fa6ccaff`
- OS: Linux pop-os 7.0.11-76070011-generic x86_64
- Python: 3.10.12
- Hyperon MeTTa: 0.2.10
- Hosted/paid compute: none

## Command

From `projects/specatom-hs/repos/specatom-hs`:

```bash
mkdir -p ../../experiments/20260728T063000Z-monday-playground
env PLAYGROUND_WORK_DIR="$PWD/../../experiments/20260728T063000Z-monday-playground/work" \
  /usr/bin/time -v bash scripts/run-playground.sh \
  > ../../experiments/20260728T063000Z-monday-playground/stdout.log \
  2> ../../experiments/20260728T063000Z-monday-playground/stderr.log
```

The command created a new virtual environment, installed the checkout,
compiled both bundled inputs, and ran the pinned backend query.

## Timing and resource result

- Exit status: 0 (also recorded in `exit-status.txt`)
- Wall time: 3.12 s
- User time: 2.85 s
- System time: 0.23 s
- Maximum resident set size: 76,184 KiB

The complete command output and `/usr/bin/time -v` record are preserved in
`stdout.log` and `stderr.log`.

## Observed semantics

| Input | Requirements | Acceptance tests | Coverage pass | Coverage unknown |
| --- | ---: | ---: | ---: | ---: |
| `task_list.plain` | 2 | 1 | 2 | 1 |
| `task_list_edited.plain` | 2 | 2 | 4 | 0 |

Both compilations had zero failing checks. The base input emitted 342 Pass,
0 Fail, and 4 Unknown checks; the edited input emitted 417 Pass, 0 Fail, and
4 Unknown checks. The backend join over `CoverageClaim`, `Covers`, and
`RequirementLabel` produced the single pair shown above.

## Artifact sizes and SHA-256

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `work/task_list.json` | 453,877 | `6129730b5b81de5e3e7d38b7a55d0ce92ecaa35ee19a92ac1aefdabaaa7d1697` |
| `work/task_list.metta` | 165,426 | `668f9d5c294c4977fe5d072b1597901ec55e265720b5394d056ee97a497dcfce` |
| `work/task_list.diag` | 11,006 | `bb328a4d95ac0854bdcb855574ec60e46f3f705f2dfd6ea7dc0b2bfcfce4206d` |
| `work/task_list_edited.json` | 551,933 | `c3196ff448b5a4ed78c5834070613d52c0c35fb88320eda854dbb0447f5d643c` |
| `work/task_list_edited.metta` | 201,112 | `e1628480dd2378d098d8097011d90945a7b654ca6ddb47cecc3b7bc88fb53b96` |
| `work/task_list_edited.diag` | 13,197 | `184816cc383e54c497eebd890ee46e4909448fe8c3574af49220cecc009cdb7a` |
| `stdout.log` | 1,617 | `8df56b971993730cdaa5037fcd8fb2f51476b57630428e8692dc0f5b4c68fda4` |
| `stderr.log` | 909 | `d304ffd320d23ebea2c27963c07cec04c79910853c7b4f849e07d26c8d3774ab` |

All generated JSON, MeTTa, and diagnostics files remain below the documented
interactive ceilings of 1 MB, 500 KB, and 50 KB respectively.
