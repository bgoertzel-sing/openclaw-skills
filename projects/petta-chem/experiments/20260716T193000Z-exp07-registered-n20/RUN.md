# exp07 registered N=20 matrix

- Time: 2026-07-16 12:30 PDT / 19:30 UTC
- Preregistration: `repos/petta-chem/experiments/exp07/PREREG.md`
- Arms: unguided, weak Doob-h, shuffled guidance
- Seeds: seed-7, seed-8, seed-9, seed-10
- Horizon: ticks 3--22, fixed before execution
- Replenishment: A/B/C reset to 2/1/1 before ticks 8, 13, 18
- Candidate cap: 2
- Chemistry: PeTTa-native; shared strength-1 pool, arm-specific categorical mass only

## Result

All 12 trajectories reached state tick 23 and replayed exactly. Each seed
produced 8 events, hence 32 events per arm. RAF incidence was 4/4 in every arm.
First-hit ticks were:

- unguided: 5, 3, 8, 10
- weak Doob-h: 3, 3, 8, 8
- shuffled guidance: 5, 3, 4, 3

The bounded detector specializes the canonical RAF conditions to the two-rule
food-generated chamber and reads catalysis from fired event relations: a
singleton closes when product equals catalyst, or the pair closes through
AB/AC cross-catalysis. Post-run pool identity passed.

This is the preregistered all-arms-positive branch. The shared pool supports
closure independently of guidance, guiding-term removal does not collapse the
controls, and `emergence-claim none` remains. The prescribed next action is a
preregistered richer chamber/pool redesign, not a horizon extension.

## Checks

- `scripts/run_exp00.sh`: pass, 153 reported assertions
- `scripts/run_exp07.sh`: pass, 141 reported assertions
- `git diff --check`: pass

Exact terminal chambers and event histories are reproducible by querying
`exp07-registered-terminal-chamber` in `src/chem_exp07.metta`; the committed
smoke pins the aggregate result.
