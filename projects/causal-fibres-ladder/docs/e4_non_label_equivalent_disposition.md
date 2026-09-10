# E4 non-label-equivalent symbolic-source disposition

## Outcome

The direct-logit Stage-4 inversion clears the specified `G>0.20` deployment
headroom gate without label-equivalent information.

After three-seed calibration, `partial3_123` was frozen as the primary source.
It supplies object number, tense, and negation while withholding subject
number, so every message leaves exactly two of the 16 labels possible. On five
disjoint confirmation seeds, four had a defined headroom denominator and all
four passed individually. Mean CS task-loss recovery was
`G=3.7433 ± 1.5123`; mean task accuracy rose from FF `82.19%` to `88.91%`.

An additional frozen absolute accuracy threshold of `95%` failed. This does
not negate the requested `G>0.20` headroom gate, but it prevents calling the
whole composite confirmation battery an unqualified pass. The substrate was
highly variable across these seeds (FF accuracy `45.31%` to `100%`).

## What the source reveals

Every symbolic statement was compiled to an allowed-class mask, and runtime
auditing required at least two allowed labels per example:

| Family | Best confirmation condition | Labels left | Mean CS G | CS accuracy |
|---|---|---:|---:|---:|
| Partial factors | `partial3_023` | 2 | 4.6395 | 90.78% |
| Frozen primary | `partial3_123` | 2 | 3.7433 | 88.91% |
| Relational parity | `parity_03` | 8 | 3.6570 | 90.94% |
| Implication | `implication_2_1` | 12 | 0.4474 | 82.19% |
| Noisy 3-factor, p=0.1 | `noisy3_p0p1` | 2 | 1.3494 | 83.59% |

All 28 measured conditions passed the non-label-equivalence audit. Partial
factor recovery scaled with information fraction: mean G was `1.2906`,
`2.5854`, and `3.8842` for one, two, and three factors.

Noise produced the expected degradation: `G=2.7881` at `p=0`, `1.3494` at
`p=0.1`, `0.1102` at `p=0.2`, and `-3.4463` at `p=0.5`. On this fixed 5x
sink, the material gate survives 10% noise but not 20%.

## Scientific disposition

The earlier label-equivalent caveat is resolved narrowly but decisively:
four true factors are not necessary for the direct-logit channel to recover
material task-loss headroom. Even parity and implication messages that leave
8 or 12 labels possible clear the gate.

This validates the Stage-4 inversion as a constraint-channel result, not as a
complete deployed system. The experiment generated symbolic messages from
known synthetic factors. A real deployment still needs a provenance-aware
upstream source that can emit such partial or relational facts without access
to the target label.

## Evidence

- Calibration:
  `experiments/20260724T220707Z-e4-non-label-equivalent-calibration/`
- Confirmation:
  `experiments/20260724T221117Z-e4-non-label-equivalent-confirmation/`
- Frozen implementation/config commit:
  `90be2a9cf59d2d557932d4349f520124f6944058`
- Full repository tests: `197 passed`.
