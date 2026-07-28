# Decision Log

## D-20260725-structural-pivot: Make relevance-stratified structural memory the experiment

- Date: `2026-07-25`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (supplied runbook)
- Related task/run/commit: `TASKS.md`;
  `experiments/20260725T-structural-rewrite/RUN.md`

### Decision

Replace future execution of the 0/A/B/C/D experiment with 0/S/A/C/D.
Drop the output-head Stage B, stratify every substantive measurement by
chroma-derived RELATED/UNRELATED spans, and use matched retrieval versus a
length-matched wrong-history control as Stage A's decision point. Train the
Stage D adapter only on RELATED spans and keep the MusicGen backbone frozen.

### Rationale

Uniform span sampling can average sparse long-range structure into a null, and
the random control separates relevance from generic extra-context benefit.
This tests a capability claim rather than the earlier speed/interface claim.

### Consequences

Stage D is forbidden unless Stage A passes. The old implementation remains for
provenance, but the structural script and copied runbook are authoritative.

## D-20260725-frozen-preparation: Preserve experimental choices while repairing validity

- Date: `2026-07-25`
- Status: `accepted`
- Decision owner: delegated research agent
- Related task/run/commit: `TASKS.md`; source runbook §6

### Context

The supplied implementation has alignment, metric, timing, and data-split
defects, while the runbook freezes backbone, comparisons, noise model,
evaluation triple, and scoring.

### Decision

Repair validity and diagnostics without changing frozen choices. Treat a worse
held-out Stage D adapter as a valid negative result; flag divergence only for
non-finite or consistently worsening late loss. Add a Stage C no-noise
oracle-initialized coding check while retaining `warm_prev >= cold` at every
finite SNR. Do not require cold-start success: basin entry remains necessary
even for an exact product code.

### Alternatives considered

Changing model architecture or experiment design; rejected as out of scope.

### Rationale and evidence

Library `SOURCE.md` audit and runbook §§5–7. Research Rules 1, 2, 5, and 7.

### Consequences

GPU execution remains blocked until local evidence and an approval-ready,
hard-capped proposal exist.

### Revisit trigger

A required fix would alter a frozen choice, or installed AudioCraft semantics
contradict the alignment specification.

### Supersedes or superseded by

None.

## D-20260727-smoke-r2-low-support-nll-amendment: Stratify the smoke NLL band by support

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (Telegram message 13726)
- Related task/run/commit: `TASKS.md`;
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`; `7afd4c4`

### Decision

For the approved eight-track Stage 0/S/A replacement smoke only, apply the
ordinary 1.5--6.0 NLL band independently to a stratum only when it has at
least four spans. Preserve the unconditional `<0.5` alignment-bug stop and
the existing `>8` broken-conditioning stop. Report smaller strata as
support-insufficient. Do not run Stage C, D, or the full corpus under this
approval.

### Rationale

The prior fail-closed smoke had twelve RELATED spans in band but exactly one
UNRELATED span at 1.23--1.27. A single span cannot establish a stratum-wide
sanity distribution, while values below 0.5 or above 8 remain strong plumbing
warnings at any sample size.

### Consequences

Commit `7afd4c4` implements and tests the amended gate. Provisioning remains
conditional on the specifically approved RTX 3090 being live at a price within
the four-hour/USD-3 bound; no substitute is authorized.
