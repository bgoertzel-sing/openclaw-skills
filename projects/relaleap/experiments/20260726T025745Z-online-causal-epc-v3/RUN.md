# Run 20260726T025745Z-online-causal-epc-v3: corrected curvature confirmation

- Project: `relaleap`
- Started: `2026-07-26T02:57:45Z`
- Finished: `2026-07-26T03:59:04Z`
- Status: `complete; Phase 0 passed, contingent Shakespeare promotion failed`
- Local or remote: `local CPU`
- Working directory: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-online-v3`

## Question

Does the v2 online causal-support estimator pass a confirmation on untouched
seeds when interaction is measured by sign-insensitive Hutchinson curvature
magnitude and the theorem-relevant vector `H_B g_A - H_A g_B`, while curvature
sign and cross-task ablations are retained as classifications rather than
promotion gates?

## Preregistered protocol

- Code base: v2 commit `4ca1b5e`, branch `agent/online-causal-epc-v3`.
- Final implementation commit: `b490f52`.
- Frozen confirmation seeds: `8147, 12289, 24593`. These were selected and
  recorded before executing the revised Phase-0 gate.
- Arms: `ordinary, ratio, multi, full, oracle`.
- Updates: 150 Task-A plus 150 Task-B updates per arm and seed.
- Curvature probes: 16 seeded Rademacher probes per module.
- Phase 1: run Shakespeare only if every Phase-0 gate below passes.
- Compute: local CPU only; no remote or paid resources.

## Frozen Phase-0 gates

1. Support recovery AUC at least `.85` in every seed, with the planted category
   ordering correct.
2. Oracle gate specificity at least `.8` for protected block 0 and unprotected
   block 1.
3. Hutchinson RMS/squared curvature-overlap magnitude is strictly nonzero for
   every module and seed.
4. `||H_B g_A - H_A g_B||` is strictly nonzero for every module and seed.
5. Zeroing block 0 raises Task-A loss by at least `.1` nat, and zeroing block 1
   raises Task-B loss by at least `.1` nat, in every seed.
6. Mean oracle forgetting is strictly lower than mean ordinary-ePC forgetting.

Signed `tr(H_A H_B)` is classified cooperative/antagonistic but is not a gate.
Cross-task ablation deltas are classified facilitative/suppressive but are not
bounded or gated.

## Research rules

Rules 1, 2, 5, and 7 are primary: validate the estimators on analytic tests,
keep diagnostic semantics explicit, preserve exact reproducibility, and expose
the curvature diagnostics through modular functions.

## Inputs and evidence

- Command: `command.sh`
- Git state: `git.txt` (to be captured)
- Environment: `env.txt` (to be captured)
- Standard output/error: `stdout.log`, `stderr.log`
- Machine-readable result: `artifacts/results.json`
- Status: `status.json`
- Contingent Shakespeare command: `phase1.sh`

## Results

### Phase 0

All seven revised gates passed on every frozen seed.

| Gate | Observation | Pass |
|---|---|---:|
| support recovery | AUC `1.0` in all seeds; category ordering correct | yes |
| oracle specificity | block 0 protected and block 1 unprotected at >= `.8` | yes |
| curvature magnitude | all 9 module/seed RMS and squared overlaps nonzero | yes |
| commutator vector | all 9 `||H_B g_A - H_A g_B||` values nonzero | yes |
| own-task load-bearing | block-0/A deltas `.1904` to `.2429`; block-1/B `.4391` to `.4821` nat | yes |
| oracle retention | mean forgetting `.06972` vs ordinary `.20097` | yes |

Curvature signs were mixed as intended: block 0 was cooperative in two seeds
and antagonistic in one; block 1 was antagonistic in all three; shared was
cooperative in all three. RMS overlap ranged from `.00106` to `.08658`;
normalized overlap ranged from `.1603` to `.5360`. Commutator norms ranged from
`.000440` to `.12455`.

Cross-task ablations were reported, not gated. Block 1 on Task A was
facilitative in all seeds (`-.0462` to `-.0603` nat). Block 0 on Task B was
suppressive in all seeds (`.00122` to `.00277` nat).

### Contingent Shakespeare phase

Phase 0 opened the preregistered contingency, so the established local
five-arm Shakespeare runner was executed for all 15 arm/seed records. It
finished with exit status 0 in `56:58.69` wall time. Its existing six-check
promotion gate failed 2/6:

- full-causal mean forgetting was `4.89747`, worse than ordinary ePC
  `4.85953`;
- full-causal finite-update commutator was `7.2649e-7`, worse than ordinary
  `6.8075e-7`;
- Task-B tolerance, leakage, entropy-rank, and credit-wavefront checks passed.

The oracle-support Shakespeare arm also worsened mean forgetting to `5.14250`.
This does not negate the synthetic confirmation; it rejects promotion of the
current Shakespeare causal-routing configuration.

### Verification and artifacts

- Focused diagnostics: `8 passed`.
- Full repository suite: `432 passed, 1 skipped`, exit 0. Log SHA-256:
  `a4d3f7fb004e0231ddce42d50bc3bfb268a50926d0fe8f44692c0f079925b4ef`.
- Phase-0 result SHA-256:
  `8cdbda46675bb166df2681ba58b613ff2e52ba24dd3ce881accc5ae92e219009`
- Shakespeare result SHA-256:
  `8260070ed59b8198d4a992db22882b7a4bbdb267fd14c842400c752cd98704eb`
- Phase-0 command SHA-256:
  `18d1fe581447a208ae39a25e8cfe3c5144f5e392ff6f865a9293f1734a45a32f`
- Shakespeare command SHA-256:
  `38917c9769967e130a6fde7380e1f60490bd9b6ebaf7de3f4487747d0b3f7d93`

## Interpretation

**Observation:** The corrected sign-insensitive diagnostics are nonzero for
every planted module, despite both cooperative and antagonistic signed traces.
Support recovery, oracle gate action, own-task load-bearing effects, and the
oracle forgetting advantage all replicated on untouched seeds.

**Inference:** The v2 Phase-0 failures were caused by mis-specified signed
curvature and cross-effect gates, not by failure of the planted support
estimator. Nonzero interaction and theorem-relevant commutator vectors coexist
with indefinite curvature and facilitative cross-task effects.

**Observation:** The contingent Shakespeare configuration did not improve
aggregate forgetting or the finite-update commutator, and its oracle support
arm worsened forgetting.

**Inference:** Passing the planted identification fixture is necessary but not
sufficient for useful real-text routing. Do not promote this Shakespeare
configuration.

**Hypothesis:** The Shakespeare support intervention is not aligned with
retention utility; the large seed variation and worse oracle forgetting suggest
that better support labels alone do not repair the current routing objective.

## Stop condition

If any revised Phase-0 gate fails, stop and do not run Shakespeare.

The stop condition did not trigger. Shakespeare ran and failed its own
promotion gate; stop before any scale-up or paid compute.
