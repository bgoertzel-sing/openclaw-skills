# GGB Capacity Gate to PeTTa Run-Contract Mapping

- Created: 2026-07-01
- Purpose: a thin bridge from `GGB_CAPACITY_GATE_TEMPLATE.md` records to the `petta-chem` v0.1 run-contract atom pattern, so Protobot capacity upgrades can later be serialized/queryable as PeTTa-shaped evidence without making `petta-chem` responsible for OmegaClaw governance.
- Source contract inspected: `projects/petta-chem/repos/petta-chem/src/run_contract.metta` and `experiments/run_contract/README.md`.

## Scope and non-goals

This is a mapping sketch, not a live integration. It does not change OmegaClaw runtime behavior, Telegram permissions, secrets, ThreadKeeper PR #1, or `petta-chem` experiment semantics. The immediate use is to make future GGB gate records easier to render as atoms and compare across ThreadKeeper, `petta-memory`, and `petta-chem` gates.

## Field mapping

| GGB gate-template field | PeTTa run-contract target | Notes |
|---|---|---|
| Gate slug + date/time | `run-id` in all contract atoms | Use stable slugs such as `ggb-20260701-petta-chem-run-contract`; keep date in slug for artifact lookup. |
| Capacity IDs | `experiment` or gate-specific parameter atom | For multi-capacity gates, use `experiment ggb-capacity-gate` and add separate `(ggb-capacities <run-id> (...))` rather than overloading `experiment`. |
| Related systems | gate-specific parameter/metric atoms | Example: `(ggb-related-systems <run-id> (OmegaClaw ThreadKeeper petta-memory))`. |
| Task contract: objective / allowed paths / forbidden actions / done criteria | `CONFIG.metta` companion atoms plus `run-config` | Keep `run-config` small for compatibility; store richer fields as `(ggb-task-contract ...)`, `(ggb-allowed-paths ...)`, `(ggb-forbidden-actions ...)`, `(ggb-done-criteria ...)`. |
| Budget/compute constraints | config/manifest companion atoms | Example: `(ggb-budget <run-id> no-paid-remote-compute local-only)`. Unknown budget or unapproved remote compute should map to summary status `blocked`/`failed`, not `passed`. |
| Inputs and fixtures | `run-manifest` plus `EVENTS.metta`/fixture atoms | Branch/commit baselines and commands belong in `run-manifest`; fixture filenames can be explicit `(ggb-fixture <run-id> <path> <hash-or-unknown>)` atoms. |
| Procedure | ordered event atoms | Use `EVENTS.metta` for step records like `(ggb-procedure-step <run-id> 1 inspect-sources passed)`. |
| Artifacts changed | event/manifest companion atoms | Store file paths as `(ggb-artifact-changed <run-id> <path> <kind>)`; transcript/run-record pointers as `(ggb-transcript <run-id> <path>)`. |
| Checks run | `METRICS.metta` and/or ordered check atoms | Use `(ggb-check <run-id> <label> <command-or-method> <status>)`; aggregate counts can be `metric` atoms. |
| Observed behavior / metrics / records produced | `METRICS.metta` plus domain-specific atoms | Preserve domain records such as ThreadKeeper structured returns or `petta-memory` `MM-index` atoms as pointers or quoted fixtures; avoid flattening away the original evidence. |
| Comparison/control result | `ABLATIONS.metta` or control/comparison atoms | For causal or scientific gates use `ablation`; for software gates use `(ggb-control-comparison <run-id> <control> <result>)`. |
| Gate status | `run-summary` status | Allowed statuses should include `passed`, `failed`, `partial`, `blocked`; `replay-ok?` should be true only when commands/artifacts are reproducible locally. |
| Evidence / known failure modes / uncertainty / follow-up task | `SUMMARY.metta` companion atoms | Use `(ggb-evidence ...)`, `(ggb-failure-mode ...)`, `(ggb-uncertainty ...)`, `(ggb-follow-up ...)` beside `run-summary`. |

## Minimal atom shape for a GGB gate

```metta
(run-config <run-id> ggb-capacity-gate <capacity-ids> <time-budget-or-na> <artifact-budget-or-na> <control-mode>)
(run-manifest <run-id> <config-hash> <repo-ref-or-project-record> <runtime-ref> <command-or-method> <exit-status>)
(run-summary <run-id> <passed|failed|partial|blocked> <short-conclusion> <replay-ok?>)
(run-record <run-id> <config> <manifest> <events> <abundances-or-na> <metrics> <acs-or-na> <ablations-or-controls> <summary>)
```

For non-chemistry gates, keep the existing `run-record` slots for compatibility and use `na` or empty lists for chemistry-specific sections (`abundances`, `acs-candidates`) while adding GGB-specific companion atoms in the corresponding files. This preserves the `petta-chem` evidence pattern without pretending software governance tests have molecule abundances.

## First candidate serializer path

1. Keep authoring human gate records as `RUN.md` under `projects/omegaclaw/artifacts/ggb-capacity-gates/<slug>/`.
2. Add optional sibling files later: `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta` using the mapping above.
3. Start with one already-archived gate, preferably `20260701-petta-chem-run-contract`, because its source evidence already follows the run-contract convention.
4. Test with a small parser/grep smoke first: all required files exist, one `run-summary` status is present, and every check in `RUN.md` has a corresponding `ggb-check` atom.

## Runtime validation status

As of 2026-07-13, `projects/omegaclaw/local/check-ggb-gate-petta-runtime.py` implements bounded real local PeTTa load/query gates for the canonical positional shape above and one current keyword-shaped ThreadKeeper fixture. It first applies the lightweight sibling-fixture checker, then loads `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, and `SUMMARY.metta` together. For positional records it queries `run-summary` plus passed `ggb-check` labels; for simple keyword records it extracts one balanced top-level summary, gate ID/status, and passing gate-local checks, then queries their exact source atom shapes. `20260701-petta-chem-run-contract` and `20260713-threadkeeper-unicode-control-arg-hardening` pass. This is representative runtime coverage, not normalization of all historical keyword variants; define an explicit neutral schema before broadening universal assertions.

## Open design questions

- Whether to define these GGB companion atoms in OmegaClaw only, or add a neutral `ggb_gate_contract.metta` fixture outside `petta-chem`.
- Whether `partial` gates should set `replay-ok? True` when checks are reproducible but capacity coverage is incomplete. Recommended: yes, if the artifact is locally replayable and the limitation is explicitly in `run-summary`/`ggb-uncertainty`.
- How much original evidence to quote into atoms versus link by path; recommended default is path + hash for large transcripts and quoted atoms only for small fixtures.
