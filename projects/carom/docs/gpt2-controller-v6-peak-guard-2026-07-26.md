# CAROM GPT-2 controller v6 peak-LR analysis

The v5 error is a sign reversal localized to the high-LR regime. At update
600, parent LR was `0.001836` (91.8% of the `0.002` schedule peak). The
mean-gradient forecast ranked 1.5x best, while held-out continuations worsened
monotonically at large scales and ranked 0.25x best. At update 1200, parent LR
was `0.000197` (9.8% of peak); forecast and held-out oracle both selected 0.5x.

The two calibration checkpoints therefore do not support a learned
update-index boundary. They do support a narrow safety rule: forecasts trained
on eight-update mean gradients are not trusted when the current LR is at least
75% of the schedule peak. V6 selects 0.25x inside that region and retains the
v5 forecast argmin elsewhere.

This rule retrospectively selects the held-out oracle at both v5 checkpoints.
That is a constructed replay, not independent evidence of utility. Activation
still requires new common-random held-out continuations containing multiple
checkpoints on the rising flank, peak, falling flank, and low-LR tail. A
wider-range learned controller would need those peak-LR examples explicitly;
v5 had only two decision points and cannot identify a reliable boundary.
