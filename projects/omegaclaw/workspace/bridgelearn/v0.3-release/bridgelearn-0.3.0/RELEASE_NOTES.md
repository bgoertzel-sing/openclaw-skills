# BridgeLearn 0.3.0 release notes

BridgeLearn 0.3.0 incorporates the dynamic-curvature and momentum-control
revisions requested after the v0.2 critique.

## Principal additions

- A slow scalar sharpness plant identified by RLS rather than a static
  polynomial response in learning rate.
- Lower/center/upper curvature funnels, with upper-bound stability checks and
  lower-bound contraction promises.
- Two-timescale receding-horizon planning that rolls sharpness through every
  candidate bridge horizon.
- Static, dynamic, and gain-scheduled curvature models with adequacy selection,
  trust-region fallback, and catapult jump detection.
- Gray-box momentum identification that algebraically removes known time-varying
  learning-rate, momentum, and batch commands.
- Optional instrumental variables for noisy centered-state observations.
- Exact order-2 antithetic probes, two probe amplitudes, contrast/condition
  triggers, pair checkpointing, and realized-perturbation accounting.
- Companion/Jury stability geometry, damping regimes, the momentum cooling
  floor, Lyapunov-adapted covariance diagnostics, and conditional small-gain
  reports.
- A companion-aware step/momentum/batch actuator with shared dominant-sharpness
  constraints and compute-priced discrete resources.
- Expanded PyTorch metadata and safety gates for momentum/Adam channels.

## Validation

The clean source tree compiled and all 38 tests passed. A wheel was built and
installed in a separate virtual environment. No new scientific benchmark or
CAROM training run is claimed in this release; those experiments are a separate
next stage.

## Read first

- `README.md`
- `docs/SHARPNESS_AND_MOMENTUM.md`
- `docs/MIGRATION_0_3.md`
- `docs/CRITIQUE_RESPONSE.md`
- `docs/CAROM_INTEGRATION.md`
