# E4 Input-Derived Symbolic Extractor Disposition

## Outcome

The deployment-time provenance gap is closed for the reduced synthetic
grammar. A lightweight analyzer reads only the raw input tensor, decodes the
four public one-hot blocks, applies seeded extraction errors, compiles
non-label-equivalent subset/parity/implication constraints, and sends them
through the confirmed direct-logit sink.

The frozen primary at 90% requested extraction accuracy passes the deployment
headroom gate:

- mean defined-seed CS task-loss `G=2.32074`, above `0.20`;
- `3/3` defined confirmation seeds individually pass (`3.31286, 1.97012,
  1.67924`);
- mean CS task accuracy improves from FF `94.22%` to `96.09%`;
- the subset statement leaves exactly two labels possible;
- every provenance and non-label-equivalence audit passes.

Two of five confirmation seeds had `|TC_loss-FF_loss|<0.01`, so their raw
metrics remain recorded but G is undefined under the pre-existing denominator
rule. The frozen robustness requirement was three passing defined seeds.

## Provenance result

The extractor function has no factor-label or target-label parameter. It
accepts only raw inputs, requested accuracy, seed, and the public block count.
The compiler consumes only extracted readings. Ground-truth factors are
consulted after construction solely to audit realized accuracy.

Across all calibration and confirmation runs, clean input readings exactly
matched the synthetic grammar factors. At confirmation, requested/realized CS
extraction accuracies were:

| Requested | Realized |
|---:|---:|
| 1.00 | 1.0000 |
| 0.95 | 0.9570 |
| 0.90 | 0.9039 |
| 0.80 | 0.8188 |
| 0.70 | 0.7016 |

This establishes the full deployment path on this encoding:

`raw input → noisy symbolic extraction → relational mask → direct-logit sink`.

## Noise and relation results

Confirmation CS task-loss G:

| Source | p=1.0 | p=0.95 | p=0.9 | p=0.8 | p=0.7 |
|---|---:|---:|---:|---:|---:|
| subset3_123 | 3.8670 | 3.1933 | 2.3207 | 1.2846 | -0.9850 |
| parity_03 | 2.3564 | 1.8283 | 1.1998 | 0.1955 | -0.5074 |
| implication_2_1 | 0.8454 | 0.6096 | 0.2610 | 0.1279 | -0.3239 |

The primary retains `60.0%` of its clean input-derived recovery at 90%
accuracy and remains well above the gate at 80%. All three relation families
clear the gate at 90%, although the implication margin is small. At 70%,
every source is harmful on mean G; extraction quality is therefore a real
deployment condition, not merely an implementation detail.

## Oracle comparison

The clean input-derived subset result (`G=3.8670`) is close to the prior
known-factor primary confirmation (`G=3.7433`) and exactly reproduces oracle
masks in unit tests. The values use different seed cohorts, so their small
difference is not interpreted as an improvement. Relative to its same-seed
clean input benchmark, 90% extraction reduces G by `1.5463` (`40.0%`) while
retaining material recovery.

## Evidence

- Protocol: `docs/e4_symbolic_extractor_protocol.md`
- Calibration:
  `experiments/20260724T224751Z-e4-symbolic-extractor-calibration/`
- Confirmation:
  `experiments/20260724T225008Z-e4-symbolic-extractor-confirmation/`
- Frozen code/config commit:
  `5377d1ec9b369c239e87adcf9dfa94af9764fbb7`
- Focused tests: `17 passed`
- Full suite: `203 passed`

## Scope

This is genuine input-derived provenance for the deliberately transparent
one-hot synthetic grammar. It does not demonstrate extraction from natural
language or latent neural representations. The deployment claim is therefore:
given an explicit symbolic surface encoding with at least roughly 80--90%
factor-reading accuracy, non-label-equivalent input-derived constraints
recover substantial headroom through the direct-logit sink.
