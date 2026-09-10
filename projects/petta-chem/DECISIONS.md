# Decision Log

## D-20260718-dual-bootstrap-closure: close the registered program as negative

- Date: `2026-07-18`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / dedicated worker under standing scope
- Related evidence: `experiments/exp07/PREREG_DUAL_BOOTSTRAP.md` and
  `experiments/exp07/DUAL_BOOTSTRAP_REPORT.md`

### Decision

Close the dual-bootstrap program without adding seeds, ticks, chemistry,
selector changes, thresholds, or endpoints. Record the result as a failed
bounded guided causal RAF-uplift gate and retain `emergence-claim none`.

### Rationale

Weak Doob-h incidence was 9/32 versus 13/32 unguided and 0/32 shuffled, so it
missed the preregistered ten-seed advantage over each control. Although every
structural ablation collapsed weak incidence, guiding-term removal retained
unguided 13/32. The pathway is structurally necessary, but guidance causality
is not supported.

### Consequences

- The completed matrix is immutable and is not a pilot to extend.
- A successor must choose whether it studies the unexpected unguided closure
  or targets genuinely unguided emergence, then preregister before outcomes.
- Chemistry generation, selection, firing, replay, and detection remain
  PeTTa-native; Python remains harness/glue only.

## D-20260718-dual-bootstrap-successor: close replication and freeze an order-invariant bounded successor

- Date: `2026-07-18`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / dedicated worker under standing scope
- Related protocol: `experiments/exp07/PREREG_DUAL_BOOTSTRAP.md`

### Decision

Close ordered-replication cohort A and cohort B as distinct negative gates.
Do not pool, extend, or reinterpret them. Before implementing another outcome,
freeze a successor with a dual bootstrap, four-rule RAF, twelve-rule source,
order-invariant identity-addressed cap-8 generation, matched selection cost,
fresh seeds 201--232, and direct PeTTa chamber ticking.

### Rationale

Cohort A failed its treatment-control incidence threshold. Cohort B passed its
incidence separation but failed the guiding-term-removal threshold because
unguided RAF incidence was 8/16. A longer six-step frontier prospectively
targets accidental unguided completion, while identity-based bounded
generation makes source order a tested invariant rather than an implicit cap
mechanism.

### Consequences

- The two completed cohorts remain negative and separately labelled.
- Successor implementation must stop at fail-closed pre-run gates before any
  registered trajectory is constructed.
- Chemistry generation, selection, firing, and outcomes remain PeTTa-native;
  host code remains harness/glue only.
- No spontaneous-emergence claim follows from the designed successor.

### Revisit trigger

Revisit only after the frozen successor completes its registered endpoint and
causal gates without adaptive seed, horizon, pool, or threshold changes.

## D-20260715-first-class-binary-catalysis: RAF detection queries explicit PeTTa catalysis

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run: `20260716T022154Z-first-class-catalysis-exp04`

### Decision

Use an explicit binary PeTTa `(catalyzes Molecule RuleId)` relation as the only
catalysis interface for RAF detection. Keep template matching only as
provenance/materialization logic. Model no-catalysis ablation as an empty
relation passed through the same detector path.

### Rationale

A detector that reconstructs catalysis from host-side molecule structure makes
RAF closure partly circular and cannot support a clean causal ablation. Binary
catalysis gives a decidable reference without a tunable threshold.

### Consequence

The seeded exp04 fixture must reproduce RAF 15/core 2/ablation 0 from PeTTa
facts before exp07 emergence work. Graded catalysis is deferred until the
binary reference is stable. Passing this gate is not unseeded-emergence
evidence.

### Evidence

- `docs/first_class_catalysis.md`
- `projects/petta-chem/experiments/20260716T022154Z-first-class-catalysis-exp04/`

## D-20260715-emergence-first: Stop proactive kernel boundary extension and run the ACS experiment

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: twelve-rule checkpoint `7061403`; exp07 stochastic/Doob-h pilot

### Context

The PeTTa-native kernel has accumulated extensive deterministic boundary coverage, including twelve-rule chambers, stable bounded candidate generation, provenance, ownership, selection, ticking, replay-oriented event history, and candidate-cap guards. This is useful infrastructure, but it is not evidence of ACS emergence. Ben explicitly prioritized getting back to the scientific question.

### Decision

Freeze proactive source-list/arity hardening at the twelve-rule checkpoint and make ACS emergence the immediate main line. Further kernel hardening is demand-driven only. The next gate is a stochastic exp07 ensemble with native/unguided, weak Doob-h guidance, and matched shuffled-guidance controls, without terminal forcing.

### Evidence and claim gate

Measure ACS/RAF hit rate, first-hit time, persistence, productivity, diversity collapse, intervention/path cost, replay, and causal catalyst/rule ablation over fixed seeds. Guidance-associated terminal hits alone are diagnostic, not emergence. Retain `emergence-claim none` unless an uplift survives matched controls, robustness checks, and causal validation.

### Consequences

- Do not extend to thirteen-rule chambers merely for another boundary milestone.
- Use the hardened exp00 kernel and existing ACS scanners as infrastructure for exp07.
- Treat the eight-candidate ceiling and ordering as explicit experimental factors or robustness checks, not automatic disqualifiers.
- Preserve the PeTTa-native kernel and thin-host-harness boundary.

### Revisit trigger

Revisit kernel hardening only if the stochastic pilot exposes a reproducible semantic/runtime blocker or if ACS evidence depends materially on a current bound.

## D-20260626-petta-native-kernel: Build the chemistry kernel in PeTTa from the start

- Date: `2026-06-26`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: Telegram clarification on 2026-06-26; `projects/petta-chem/TASKS.md`

### Context

ZeroBot suggested a hybrid implementation path in which Python host code would implement the first chemistry kernel while emitting PeTTa/MeTTa-style atoms. Benjamin rejected that interpretation and clarified that the algorithmic chemistry system itself should be built in PeTTa from the start.

### Decision

Implement the algorithmic chemistry kernel in PeTTa from the beginning. Python may be used for experimental wrapping only: running batches, loading configuration files, saving data, plotting, filesystem logistics, or other harness duties.

### Alternatives considered

- Python-first kernel with PeTTa/MeTTa-shaped atom protocol.
- Mixed host-kernel implementation where core matching/scoring/firing lives outside PeTTa.

### Rationale and evidence

Benjamin's explicit clarification: “build the algorithmic chemistry system in PeTTa right from the start -- NOT in python. You can use python for some experimental wrapping -- as a harness for running experiments, saving data, loading configuration files or whatever.” He added that implementing the chemistry in Python would make a mess that is cumbersome to check for errors and would still require a PeTTa port later.

### Consequences

- exp00 must be designed around PeTTa-native chemistry behavior, not a Python simulation that merely exports atoms.
- Harness code is acceptable but should remain thin and replaceable.
- Repository inspection should focus on the practical PeTTa runtime path and test strategy.

### Revisit trigger

Revisit only if PeTTa runtime limitations make the specified exp00 impossible or scientifically misleading; prefer narrowing exp00 rather than moving the chemistry kernel to Python.

### Supersedes or superseded by

Supersedes the tentative Python-kernel/hybrid recommendation made in chat before Benjamin's clarification.

## D-20260626-runtime-swi-petta: Use PeTTa on SWI-Prolog 9.3.x for version 0.1

- Date: `2026-06-26`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Related task/run/commit: `projects/petta-chem/repos/petta-chem/docs/runtime.md`; exp00 smoke runner

### Context

The project needs a PeTTa-native kernel from the start. During OmegaClaw setup, the local workstation obtained a working PeTTa runtime with SWI-Prolog 9.3.36. PeTTa's upstream `examples/fib.metta` smoke test passed, and OmegaClaw initialized and ran its mock loop on the same stack.

### Decision

Use the locally validated PeTTa implementation running on SWI-Prolog 9.3.x as the version-0.1 runtime for `petta-chem`. Keep the chemistry kernel in PeTTa `.metta` files. Use Python only as optional thin harness/glue for configs, batch execution, storage, plotting, or filesystem logistics.

### Alternatives considered

- Python-first chemistry kernel emitting PeTTa-shaped atoms.
- Waiting for another Hyperon-family runtime before beginning exp00.
- Starting with Docker-only runtime wiring.

### Rationale and evidence

The local PeTTa/SWI stack is already installed and tested. This makes it the lowest-friction path that satisfies Benjamin's PeTTa-first constraint while preserving future seams for MORK or other acceleration.

### Consequences

- exp00 starts as executable PeTTa tests, not a Python simulation.
- Every consequential run should record the PeTTa commit, SWI version, command, and output.
- Runtime docs live in the implementation repo at `docs/runtime.md`.

### Revisit trigger

Revisit if PeTTa/SWI cannot express or test deterministic replay and ACS detection without misleading semantics or unacceptable fragility.

### Supersedes or superseded by

Complements `D-20260626-petta-native-kernel`.

## D-20260626-abstract-first: Start with abstract PeTTa chemistry before semantic/music/MORK integration

- Date: `2026-06-26`
- Status: `proposed`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Related task/run/commit: `library/petta-abstract-algorithmic-chemistry/SOURCE.md`

### Context

Benjamin provided a June 2026 design PDF for initial abstract algorithmic chemistry experiments in PeTTa. The document argues for proving replayable, causally testable ACS dynamics in a bounded symbolic chemistry before adding semantic graph chemistry, music molecules, MORK execution, PLN, MOSES, or other larger subsystems.

### Decision

Use the PDF as the seed specification for `projects/petta-chem`. Treat version 0.1 as an abstract PeTTa/Atomspace-shaped chemistry focused on deterministic replay, planted ACS recovery, random polymer ACS emergence tests, and intervention/ablation evidence.

### Alternatives considered

- Begin directly with semantic graph chemistry.
- Begin directly with music chemistry.
- Couple the prototype tightly to MORK from the start.
- Build a large open-ended chemistry system before validating replay and ACS detection.

### Rationale and evidence

The PDF's rationale is that abstract molecules and catalytic rewrite rules allow fast, interpretable experiments and reduce confounds from graph normalization, truth propagation, language realization, or musical scoring. It also emphasizes that MORK seams should be preserved as interfaces rather than blocking the first implementation.

### Consequences

- Version 0.1 must prioritize event logs, seed discipline, snapshot/replay, conservative ACS detection, and controls.
- MORK/semantic/music code is postponed until the abstract substrate yields validated evidence.
- Implementation tasks should be milestone-sized and test-gated.

### Revisit trigger

Revisit if exp01 cannot recover planted ACSs, exp02 only yields trivial/hand-coded ACSs, deterministic replay remains unreliable, or PeTTa integration constraints make the abstract-first design impractical.

### Supersedes or superseded by

None.
## D-20260727-neutral-model-reset: Stop generator accretion; validate neutral chemistry before further guidance

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Evidence: `docs/petta_chem_external_review_2026-07-26.pdf`, especially
  Recommendations 0--5; current generator-only commits `17db9f8` through
  `851189a`.

### Context

The 26 July external review found that the implemented substrate has credible
replay and useful controlled negative results, but no evidence of spontaneous
ACS/RAF emergence.  The strongest constructed weak-Doob result failed its
independent replication; a successor made weak guidance worse than unguided.
The review therefore identifies continued feature/source-list expansion and
further pathway-specific guidance studies as an increasingly narrow dead end.
Nevertheless, the recurring worker continued nine generator-only commits from
33 to 41 rules after the review, each explicitly reporting no chemistry or
scientific-result change.

### Decision

Freeze proactive generator/source-list/arity growth and defer exp08 in its
current constructed-pathway form.  Make the next scientific line a neutral,
pathway-independent random catalytic reaction-system model plus an independent
small-system RAF oracle.  Calibrate the model across a finite-size control
parameter and report structural RAF, dynamical reachability,
active/persistent RAF, and causal/productive endpoints separately.  Defer new
Schrödinger-bridge/Doob guidance work until an exact small-state
bridge/control baseline and applicability-aware controls can be validated.

### Consequences

- Existing exp00--exp07, their scanners, and the bridge artifacts are retained
  as controls and validation infrastructure; none is discarded or re-labelled.
- The recurring worker must not add another fixed rule-count milestone unless a
  named neutral-model or oracle requirement demonstrates the dependency.
- Do not mutate or execute the untracked `exp08/`, `scratch_cat.metta`, or
  `chem_catalysis.metta` material without a separately reviewed task; their
  provenance remains unresolved.
- The next deliverable is a frozen neutral-model/oracle protocol, not a new
  guidance outcome.

### Revisit trigger

Revisit bridge/control work only after the oracle and neutral-calibration gates
are passed, or after an independently reproduced result establishes that the
constructed pathway is itself the scientific target.

### Supersedes or superseded by

Supersedes D-20260710's ordering of work, not its conceptual insight: the
bridge/Doob framing remains a later diagnostic, but the review requires an
unbiased calibration and exact control baseline first.

## D-20260710-bridge-pivot: Pivot main effort to Schrödinger-bridge / Doob-h-transform diagnostics

- Date: `2026-07-10`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Related task/run/commit: exp06 consolidation commit `06f7371`; exp07 scaffold

### Context

The unguided/random PeTTa chemistry tracks are mostly ACS-negative under the current conservative scanners. exp02 reports 0 active cycles through 5-rule scans across 120 generated-unplanted family records, while exp04 is success-biased and catalysis-map-sensitive rather than an unbiased emergence result. exp04 nevertheless provides an engineered ACS-rich terminal fixture with maximal RAF 15 and greedy core `(lCD lBCD2)`. exp06 already named initial/terminal states and intervention variables, and its consolidation marks the candidate-cap route as not ACS-positive.

### Decision

Pivot the main experimental effort to a Schrödinger-bridge / Doob-h-transform diagnostic formulation, inspired by Ben's "Let's Get Chemical" substack post. Use old ACS scanners as validation/control infrastructure, while exp07 and successors organize search around initial/terminal state distributions and intervention-cost vectors.

### Rationale and evidence

- exp02 generated-unplanted scans are ACS-negative across the tested cycle scanners and 120 family records.
- exp04 provides a positive, inspectable, engineered terminal fixture but remains success-biased and catalysis-map-sensitive.
- exp06 names the relevant intervention variables and consolidates `candidate-cap-route not-acs-positive`.
- Bridge/Doob framing gives a structured way to search favorable-condition paths without pretending they are spontaneous emergence.

### Consequences

- exp07 becomes the next main experiment family.
- Chemistry remains PeTTa-native; Python remains harness/bookkeeping only.
- No emergence claim is made from bridge/path construction.
- Existing ACS scanners remain required controls and terminal-condition checks.

### Revisit trigger

Revisit if exp07 bridge diagnostics collapse to hand-coded terminal forcing, cannot be validated by ACS scanners, or a new unguided PeTTa regime produces reproducible causal ACS evidence.

### Supersedes or superseded by

Complements the PeTTa-native-kernel and abstract-first decisions; narrows the near-term search strategy after exp06 consolidation.
