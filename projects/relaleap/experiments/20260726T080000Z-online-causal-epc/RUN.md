# Online causal-support + soft-gating ePC

- Status: `complete; Phase 0 failed closed; Phase 1 not executed`
- Compute: local CPU only; no paid or remote resources
- Repository: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding`
- Branch/base: `agent/online-causal-epc` / `4b0a425`
- Seeds: `1729, 3253, 6421`

## Frozen question and protocol

Does an online gradient-ratio/cosine/Fisher estimator recover the known planted
support partition, do sigmoid gates act on that partition and shrink the
mixed-Hessian diagnostic, and does oracle routing improve Task-A retention
without losing Task-B learning? Five arms use identical initial parameters,
batches, optimizer, schedule, and unit learning/KD mass: ordinary, ratio-only,
multi-signal, full (multi-signal plus commutator slot), and oracle.

The planted fixture has disjoint A/B token ranges, 32-dimensional embeddings,
two routed residual MLP blocks, and a shared embedding/final layer. Block 0 is
A-only, block 1 B-only, and embedding/final are shared. Exact block-zero
ablations audit whether these pathways are load-bearing.

Phase 0 passes only if, for every seed: support AUC is at least .90 with correct
A/shared/B ordering; oracle sigmoid gates protect block 0 and not block 1;
gated mixed-Hessian trace is strictly smaller; and mean oracle forgetting is
strictly lower than ordinary. Phase 1 (the frozen prior Shakespeare five-arm
battery, 2,000 updates) is forbidden if any Phase 0 check fails.

## Exact commands

See `command.sh`. Raw output is `artifacts/results.json`.

## Results

Execution exited 0 in 6.99 s (peak RSS 289,016 KiB). All 15 arm/seed records
were produced with `kd_mass=1.0`. Focused tests passed 8/8 and the complete
suite passed 429 with 1 skipped. Implementation commit: `83abac8`.

| arm | mean A final | mean B final | mean forgetting |
|---|---:|---:|---:|
| ordinary | .693783 | .693801 | .002554 |
| ratio | .693095 | .694062 | .001866 |
| multi | .693219 | .693995 | .001991 |
| full | .693219 | .693995 | .001991 |
| oracle | .693001 | .694104 | .001773 |

| Phase 0 check | observation | pass |
|---|---|---:|
| support recovery | AUC 1.0 and A/shared/B score ordering in all seeds | yes |
| gate action | oracle protected block 0 and not block 1 in all seeds | yes |
| mixed-Hessian shrinkage | protected-block trace was 0 before and after gating | no |
| oracle advantage | forgetting .001773 vs .002554 ordinary | yes |

The load-bearing audit independently failed: block-zero loss changes had the
expected exact off-task zero, but the on-task signed effect was negative in two
of three A seeds and two of three B seeds. Thus the trained pathways were not
reliably useful, even though routing and gradient support labels were recovered.

## Gate decision

`phase0_pass=false`. Per the frozen protocol, Shakespeare Phase 1 was not
executed. No promotion claim is made.

## Interpretation

- **Observed:** online gradient magnitudes perfectly separated the architecturally
  routed blocks, sigmoid gates acted on the oracle labels, and oracle routing
  slightly reduced mean forgetting.
- **Observed:** architectural disjointness made the protected block's cross-task
  mixed Hessian identically zero, so strict shrinkage was impossible; exact
  ablations did not establish reliably load-bearing learned pathways.
- **Inferred:** this fixture confounds support identifiability with zero baseline
  interaction and is not a valid positive control for the requested theorem
  diagnostic.
- **Hypothesis:** a repaired fixture needs nonzero but controlled cross-path
  coupling plus a task construction that reliably trains both paths below
  chance before the estimator/gating comparison is meaningful.

The runner's `full` arm reserves the full-stack label but is behaviorally equal
to the multi-signal arm in this stopped Phase-0 implementation; periodic CKA
and HVP utilities are unit-tested but the run stops before the requested
200-step HVP cadence. These are implementation limitations, not hidden
positive evidence.

## Artifacts and hashes

- `artifacts/results.json`: `f2e3bed24701c48e7961cc179ec705bddddd53d4e9f0d8be260872f2a831d5a7`
- `command.sh`: `c5f52fd192de716e2a29d1700ecc43e577b4adc8d0ddb3baa9dc6c8122fa9172`
- `stdout.log`: `bdeeb43130f0f20590161ba5b26c6713839272b0a9567cab9a9847a1c70c1141`
- `stderr.log`: `e5189373126f9b8224513ca05db7d9d88525b2a6c10fb4d06792517fb322eec0`
