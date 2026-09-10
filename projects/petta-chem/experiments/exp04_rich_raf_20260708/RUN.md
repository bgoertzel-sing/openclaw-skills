# exp04 rich RAF exploratory run — 2026-07-08

Status: complete.

## Question

Does a deliberately success-biased but non-planted rich symbolic chemistry combining all four directions produce autocatalytic structure?

Directions combined:

1. Richer rules: ligation, cleavage, and modification.
2. Structured catalysis: specificity-filtered deterministic template matching.
3. Larger/longer setting: 20 rules, 56 ticks, food replenishment floor 3.
4. RAF detection: maximal RAF pruning plus greedy core minimization.

## Code and environment

- Repository: `projects/petta-chem/repos/petta-chem`
- Branch: `agent/exp04-rich-chemistry`
- Code commit under review: `6005677` plus uncommitted harness refinement at run time.
- Runtime: local Python 3 harness mirroring the PeTTa exp04 rule pool; PeTTa smoke also passes via `scripts/run_exp04.sh`.

## Command

```bash
./command.sh
```

Prepared command:

```bash
cd /home/openclaw/research-agent/projects/petta-chem/repos/petta-chem
python3 experiments/exp04/run_rich_raf.py --ticks 56 --out /home/openclaw/research-agent/projects/petta-chem/experiments/exp04_rich_raf_20260708/metrics.json
```

## Result

The host-computed RAF detector found autocatalytic structure:

- Maximal RAF after pruning: **15 rules**.
- Greedy minimized RAF core: **2 rules**: `lCD`, `lBCD2`.
- Core RAF check: **true**.
- No-catalysis control: **0-rule RAF**.
- 56-tick dynamics: **56 events** with basal seeding plus catalyzed events.
- Food floor: maintained (`A,B,C,D >= 3`).

First dynamic events include basal seeding of `lAB`, then catalyzed `lABC1`, `lAB`, `cABC1`; later `lCD`, `mCD`, and `cBCD` become active. This is more interesting than the initial over-narrow AC-only side-loop observed before retaining a slow basal trickle.

## Interpretation

This is the first positive exp04-style RAF result in the petta-chem line. It is not yet a claim of unbiased spontaneous ACS emergence: the configuration is intentionally success-biased through structured template catalysis and a hand-designed rich rule pool. But it does demonstrate that combining richer chemistry, template catalysis, larger pools/runs, and RAF detection can produce inspectable autocatalytic structure where prior strict product-as-catalyst cycle scans over simple generated-unplanted rules found zero.

## Artifacts

- `metrics.json`: full rule list, pruning trace, minimized RAF core, dynamic event sample, final abundances.
- `stdout.txt`, `stderr.txt`, `exit_status.txt`, `time.txt`: command capture.

## Next reduction

Run a parameter sweep lowering bias:

1. Compare deterministic template catalysis against randomized/partially shuffled catalyst assignments.
2. Vary basal reaction interval/rate.
3. Generate multiple rule pools instead of using this hand-designed motif.
4. Record maximal RAF size, minimized RAF size, event diversity, and no-catalysis/shuffled-control rates.
