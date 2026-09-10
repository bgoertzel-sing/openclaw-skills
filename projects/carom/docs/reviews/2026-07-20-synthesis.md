# Fable/Sol synthesis: closing CAROM's learned-heteroclinic gap

Date: 2026-07-20

## Convergent conclusion

Both reviewers regard 86.5% as a real and promising learning result, but reject
the stronger interpretation that CAROM has already learned a stable
heteroclinic channel. Their central diagnosis is that the 13.1-point gap to the
fixed chain is not causally identified: exposure/dwell/overlap differences and
evaluation weaknesses may explain it before graph-learning difficulty does.

## Ranked experiment ladder

### E0: repair the instrument (mandatory)

- Fixed evaluation corpus shared by all arms and seeds.
- Separate train/evaluation Python and PyTorch RNGs; deterministic evaluation.
- At least five seeds; bootstrap confidence intervals and paired comparisons.
- Accuracy by program depth, command, pair, synonym, and padded/noop position.
- Per-example dominant-mode sequence, dwell times, overlaps, skips, reversals,
  revisits, terminal trapping, integrated exposure, and workspace-update norm.

Go/no-go: proceed only if the fixed-chain advantage survives paired evaluation
and the trajectory metrics reproduce across seeds.

### E1: exposure-normalized controller ablation

Compare the existing mixture

\[
  \beta_k(t)=\sum_m a_m(t)\rho_k(c_m)
\]

with

\[
  \widetilde\beta_k(t)=g\,
  \frac{\sum_m a_m(t)\rho_k(c_m)}{\epsilon+\sum_m a_m(t)},
\]

using fixed and learned gain variants. Add trajectory replay controls that
equalize integrated exposure per command and total workspace-update norm.

Decision: if normalization closes most of the gap, treat dwell/exposure as the
primary cause and optimize that mechanism before changing graph learning.

### E2: mode-specific fitness

Replace the broadcast workspace scalar with a mode-specific score such as

\[
  \sigma_m=\mathrm{MLP}[\mathrm{pool}(w),e(c_m),e(m),
  \mathrm{pool}(w)\odot e(c_m)].
\]

Ablate workspace, command, and position features separately. Keep the
inhibition matrix randomly initialized rather than seeding it from the fixed
chain.

Decision: require improved learned-arm accuracy plus improved order/dwell
metrics without merely increasing total exposure.

### E3: direction-free channel regularization

Small factorial sweep over generic penalties:

- overlap/sparsity: discourage simultaneous high activity;
- switching/progress: discourage frozen modes and excessive dwell;
- revisit penalty: discourage returning to previously dominant modes;
- terminal penalty: discourage trapping after the required computation;
- activity-mass/exposure target: constrain total control mass.

Crucially, none may name a successor pair or encode `m -> m+1`.

Decision: select by held-out accuracy jointly with sequence validity, not
accuracy alone.

### E4: causal trajectory interventions

- Clamp the learned model to fixed-chain trajectories.
- Replay learned trajectories through the fixed-chain-trained operator core.
- Swap learned and fixed inhibition matrices while holding the operator core.
- Time-warp trajectories while preserving integrated exposure.

These distinguish controller timing, transition graph, and operator-core
compensation.

### E5: SHC validation, only after accuracy improves

Test near-zero-floor deterministic dynamics, perturbation recovery, dwell-time
scaling, transition reproducibility, and local invasion/stability estimates.
Until those pass, use “heteroclinic-like metastable controller,” not “stable
heteroclinic channel.”

## Proposed immediate experiment

Implement E0 and E1 together as a CPU-small/GPU-confirmatory matrix. The first
scientific question should be: **Does the learned-versus-fixed gap survive when
the two controllers have matched activity mass, command exposure, workspace
update norm, evaluation examples, and RNG state?** This is narrower and more
informative than a blind hyperparameter sweep.

