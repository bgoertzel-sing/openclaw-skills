# Post-implementation upstream provenance inspection

Ben relayed after the clean-room prototype passed that Mesto identified
`https://github.com/MesTTo/metta-on-mork` as the relevant implementation
repository. The repository was inspected after, not before, the prototype was
written and tested.

Pinned evidence is preserved at
`../../../../../../library/metta-on-mork-2026/` and summarized in its
`SOURCE.md`.

## Classification

| Item | Actual committed upstream code? | Reusable here? | Reason |
| --- | --- | --- | --- |
| Two-layer ePC settle | Yes | As a separately attributed synthetic reference | NumPy/Torch oracle plus MORK rules exist under `demos/pcgraph/` |
| End-of-settle local update | Yes | Conceptually; not copied | `m1` applies local outer-product folds after `K=16` |
| Update-every-tick iPC | Yes | No for frozen `T=1` adapter | Different learning doctrine (`m2`) |
| Cell/state schema and rule generator | Yes | Potential later MORK seam | GPL code; uses a fixed XOR graph and MORK-specific sinks |
| GPT-2 forward implementation | Not in this repository's visible trees | No | README reports/links it, but committed implementation is absent here |
| PC--GPT-2 homotopy settle/update | Not found in visible branches/history | No | No GPT-2 training code, scheduler, or AdamW state |
| Production checkpoints/config/data/telemetry | Not found | No | Required identities and artifacts remain absent |

## Relation to this clean-room prototype

No source from `metta-on-mork` was copied or adapted into `pcstep.py`. The
clean-room prototype remains a paper-derived, independently invented fixture.
Its overlap with pcgraph is conceptual (zero-initialized error settlement,
separate local weight updates) and was already fixed in `ASSUMPTIONS.md`
before repository inspection.

Important differences:

- clean-room fixture: float64, linear 2-layer scalar-output regression,
  `T=1`, AdamW-style optimizer state, explicit gate/RNG/batch-plan snapshots;
- upstream pcgraph: float32, tanh `2-2-2` XOR, normally `K=16`, direct
  learning-rate folds, hidden plus output error in its primary jpc-native
  path, MORK phase cells, and no comcrit-style pure optimizer-state boundary.

Therefore the upstream code improves provenance and supplies a genuine toy
reference, but it does not retroactively turn this artifact into Mesto-code
reproduction or production-checkpoint compatibility.
