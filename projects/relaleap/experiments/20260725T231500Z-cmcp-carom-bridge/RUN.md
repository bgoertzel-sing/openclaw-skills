# CMCP bridge Step 5: E2/E3 and CAROM convergence audit

- Status: complete
- Project: `relaleap`
- Started: 2026-07-25T23:15:00Z
- Execution: local, read-only evidence analysis plus durable report

## Question

Do Steps 1-4 and existing E2/E3/CAROM evidence support a shared bookkeeping
principle between CMCP packet weighting and CAROM workspace governance, rather
than merely a shared gate/replay type signature?

## Frozen evidence standard

The convergence hypothesis is supported only if existing artifacts establish
all three:

1. an explicit assimilation/maintenance or plasticity/replay split;
2. credit or workspace mass allocated according to measured marginal novelty
   or previously unclaimed frontier, rather than labels/types alone;
3. an outcome benefit under a mass-matched or otherwise identifying comparison.

Missing evidence is recorded as a gap, not filled by conceptual analogy. The
audit will inspect repository E2/E3/CAROM implementations, tests, project
records, and Steps 1-4 results. No new performance experiment is preregistered
for this analytical step.

## Results

The frozen three-part standard did not pass:

1. CMCP has an explicit assimilation/maintenance representation, but the
   calibrated bridge exercised assimilation only and CAROM E2/E3 has no
   homologous replay ledger.
2. CMCP response novelty is measured conditionally and has narrow
   mass-matched outcome evidence. CAROM E2/E3 workspace fitness and
   direction-free penalties do not measure marginal novelty relative to
   previously claimed workspace evidence.
3. CAROM has no completed E2/E3 scientific outcome: CPU was infeasible at the
   frozen scale, the initial GPU attempt had no result, and the compiled
   campaign stopped at 16/25 arms under its bound.

**Conclusion:** convergence is not supported; the present relationship is an
architectural analogy and a testable hypothesis, not an earned theoretical
unification. See `ANALYSIS.md` for the evidence matrix and proposed falsifiable
bridge experiment.

## Verification and provenance

- Implementation commit: `12caf1b` on `agent/cmcp-epc-kd-bridge`.
- Focused final suite: `8 passed in 2.88s`.
- Full repository suite, run from repository root with `PYTHONPATH=src`:
  `420 passed, 1 skipped in 20.60s`.
- An initial full-suite invocation from the workspace root failed during
  collection because repository-local `scripts` was absent from the import
  path; the corrected repository-root command passed. This was an invocation
  issue, not a product test failure.
- `git diff --check` passed before commit.
- `ANALYSIS.md` SHA-256:
  `51a205fcf558522d191020016cc5423956867a7cd60a8412984d5edf06dd7ca7`.
- No remote compute or paid resource was used for any of Steps 1--5.
