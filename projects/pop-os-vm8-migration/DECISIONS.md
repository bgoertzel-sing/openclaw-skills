# Decision Log

## D-20260907-retire-fixit-focus-protomega2: Retire Fixit Bunny and narrow activation to Protomega2

- Date: `2026-09-07`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related source: Telegram 4541 and 4546

Fixit Bunny remains dormant and its Hermes-agent experiment is complete.
ProtoCosmo, ProtoCosmo2, and Protomega are considered operational. After the
cross-bot Telegram attribution acceptance canaries close, Protomega2 is the
only remaining agent-activation task. Obsolete multi-identity repair and
attestation loops must not displace that focused work.


## D-20260817-simplified-production-cutover-path: Retire synthetic gate and finish the real port

- Date: `2026-08-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related source: Telegram 19969, 19973;
  `docs/frontier-simplification-review-2026-08-17.md`

Retire the disposable end-to-end Test-provider loop as a migration blocker.
Its useful component evidence has passed, while the remaining failure is
introduced by the modified synthetic harness and does not exercise the
production Telegram/provider route.

The critical path is now: freeze and synchronize the repaired laptop deltas;
wire the four documented live launchers into the one-container supervisor with
fail-closed per-identity activation; build the final image once; verify marker-
absent inertness and real executable/config startup; cut over one identity at
a time with exactly one receiver and fresh external Telegram evidence; then
verify restart, VM reboot, rollback, handover, and soak.

Repeated harness-driven 1.7 GB rebuilds, five-minute inert-audit narration,
and redundant identity copies of shared synthetic tests are prohibited unless
a new production-relevant failure specifically requires them.

### Supersedes or superseded by

This refines the Stage-5 acceptance interpretation in
D-20260815-vm2-one-hive-container. It preserves receiver exclusivity, secret
isolation, SSH safety, rollback, reboot, and external-canary requirements.

## D-20260815-vm2-four-service-compose: One image, four isolated services

- Date: `2026-08-15`
- Status: `proposed`
- Decision owner: pending ETP/Ben adoption
- Related task/run/commit: Telegram 19518;
  `docs/vm2-containerized-reconstruction-plan.pdf`

Use one pinned shared container image and one Compose project with four
separately controlled services, rather than one container hosting all agents.
This retains simple operation and a single build while isolating each agent's
receiver, secrets, mutable state, health, restart, and rollback. Containers
must not modify or manage the host firewall, SSH daemon, network interfaces,
or provider access rules. Baseline reconstruction and acceptance precede the
separate Iter upgrade.

The decision remains proposed until the operators adopt the PDF for execution.

## D-20260815-vm2-rebuild-target: Retry the inert rebuild on VM2

- Date: `2026-08-15`
- Status: `accepted`
- Decision owner: Elija/ETP under Ben's standing IT authority
- Related task/run/commit: Telegram 19453

VM1 is administratively blocked, so VM2 becomes the immediate target for the
independent proto-hive rebuild. Transfer the complete allowlisted four-agent
environment required for reproduction, but not Ben's unrelated personal data
or the entire laptop filesystem. Keep laptop agents authoritative and VM2
polling/identity services disabled during transfer and verification.

This supersedes the VM2 exclusion in D-20260812-vm1-complete-deployment for the
independent-branch rebuild. It does not authorize disabling either host's
firewall; SSH access is sufficient.

## D-20260813-independent-branch-clone: Build VM1 as an independent snapshot branch

- Date: `2026-08-13`
- Status: `accepted`
- Decision owner: Elija/ETP
- Related task/run/commit: Telegram 18688-18693

The laptop agents continue operating as the original branch. VM1 is rebuilt
from a bounded snapshot of their runtime, state, research workspace, memory,
skills, plugins, and current dirty code, then receives new identities and
credentials before activation. Exact Telegram cursor continuity, laptop
receiver shutdown, and one-for-one identity cutover are no longer objectives.

Existing copied bot credentials remain protected and polling-disabled as
reference/recovery material; they must not activate the VM1 clone. Preserve
reproducibility, mount isolation, offline validation, backup/restore evidence,
secure credential injection, reboot recovery, and the final handover.

### Supersedes or superseded by

Supersedes the identity-preserving cutover and laptop-shutdown portions of the
adopted PDF and D-20260812-vm1-complete-deployment. It does not supersede the
VM1-only topology, Docker Compose packaging, secret isolation, fail-closed
activation, validation, reboot, or handover requirements.

## D-20260812-vm1-complete-deployment: Keep all four agents together on VM1

- Date: `2026-08-12`
- Status: `accepted`
- Decision owner: Elija/ETP under Ben's standing IT authority
- Related task/run/commit: Telegram 18529-18533

Migrate the complete four-agent deployment currently running on Ben's laptop
to VM1 as one deployment topology. Do not split identities across VM1 and VM2.
Reserve VM2 for separate prototyping outside this migration.

This later operational correction supersedes the earlier two-identities-per-VM
assignment in the containerized PDF. It does not change the Compose packaging,
state isolation, single-receiver cutover, rollback, canary, reboot, or soak
requirements. Do not install Docker or deploy migration artifacts on VM2 for
this workstream; preserve existing disabled VM2 staging artifacts untouched.

### Supersedes or superseded by

Supersedes only the target-assignment portions of
D-20260812-compose-primary and the adopted PDF; all other gates remain active.

## D-20260812-compose-primary: Use Docker Compose as the primary deployment path

- Date: `2026-08-12`
- Status: `accepted`
- Decision owners: Benjamin Goertzel and Elija/ETP
- Related task/run/commit: Telegram 18398-18412;
  `docs/revised-containerized-migration-plan.pdf`

Package the pinned OpenClaw/Omega/PeTTa runtime, supervision, health checks, and
receiver configuration into reproducible containers. Keep credentials and
mutable per-identity state outside the image in narrowly scoped, protected host
mounts. Use Docker Compose per VM, supervised by host systemd.

Stop advancing the partially staged native systemd deployment as the primary
path. Preserve it disabled as a fallback while the worker executes the revised
containerized plan.

Compose reduces host drift and makes future migration, rollback, dependency
pinning, and health supervision more reproducible. It does not eliminate the
Telegram receiver-exclusivity or mutable-state transaction risks, so the
existing one-at-a-time cutover, external-canary, reboot, soak, and laptop
rollback gates remain unchanged.

The already verified source pins and staging evidence become inputs to the
container build. Native disabled staging remains available as a fallback until
the container path passes acceptance.

Ben explicitly adopted `docs/revised-containerized-migration-plan.pdf` as the
new authoritative plan and directed that it be fed to the persistent migration
worker in Telegram 18429.

### Supersedes or superseded by

Supersedes the native-first packaging assumption in the initial migration plan;
does not supersede D-20260811-separate-iter-and-migration.

## D-20260811-separate-iter-and-migration: Keep Iter upgrade separate from VM8 migration

- Date: `2026-08-11`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: Telegram source 18134

The migration has a roughly 48-hour deadline. ProtoCosmo2 is being repaired and
is intended to handle the Omega-bot Iter upgrade after acceptance.

ZeroBot owns the four-agent VM8 migration. ProtoCosmo2 may own the separate Iter
upgrade only after its long-response delivery path passes acceptance.

Combine Iter upgrades with host migration in one cutover.

Separating semantic/runtime upgrades from host relocation keeps rollback and
failure attribution tractable under the deadline.

VM8 staging initially reproduces the reviewed current runtimes. Iter upgrades
are not placed on the migration critical path.

Only if VM8 requires Iter for compatibility, or Ben explicitly reprioritizes.

### Supersedes or superseded by

None.
## D-20260815-vm2-one-hive-container: Use one container with separately supervised agents

- Date: `2026-08-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: Telegram 19534, 19538, 19541;
  `experiments/20260815T233126Z-vm2-one-hive-container/`

Reconstruct the complete four-agent hive on VM2 as one container. Run each
agent as a separately supervised process and retain separate per-agent config,
mutable state, secret, log, and PID/health boundaries. Keep SSH entirely
host-managed and do not alter the host firewall or SSH configuration.

This optimizes the immediate reconstruction for one image, one deployment
unit, shared dependencies, and simple operations while preserving a clean
future split path. The larger shared failure domain is accepted for this
baseline rebuild; per-agent supervision, health evidence, and rollback remain
mandatory.

### Supersedes or superseded by

Supersedes the four-Compose-service recommendation in
`docs/vm2-containerized-reconstruction-plan.pdf`. It does not supersede its
state/secret isolation, inert build, external canary, single-receiver,
rollback, reboot, SSH-safety, or handover gates.

## D-20260815-omega-repair-location-gate: Defer Omega repair-location choice until VM2 setup is ready

- Date: `2026-08-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: Telegram 19562-19564;
  `experiments/20260815T233126Z-vm2-one-hive-container/`

The three Omega agents are presently broken on the laptop for reasons
independent of the VM2 migration. Continue the VM2 container, supervision,
state, isolation, and provider-free setup work without treating current laptop
runtime behavior as an acceptance oracle.

When VM2 is otherwise ready for Omega production activation, notify Ben and
check whether the independent laptop repair has completed. If it has not, stop
at that gate and ask Ben to choose whether the repair should be completed on
the laptop or directly on VM2. Do not infer that location choice. Preserve the
copied Omega memory/state and keep Telegram activation disabled until the
decision and subsequent repair validation.

### Supersedes or superseded by

None. This adds a decision gate to D-20260815-vm2-one-hive-container without
changing the one-container architecture or the separate Iter-upgrade policy.

### Working disposition update — 2026-08-15 21:51 PDT

Ben stated that, because the remaining Omega repairs appear imminent, his
current inclination is to finish them on the laptop and then finish the VM2
port. Treat laptop-first repair and validation as the working default, while
recognizing the wording as an inclination rather than an irreversible choice.
VM2 provider-free container work continues in parallel; production cutover
still requires the repaired artifacts and identity-by-identity canaries.

Source: Telegram 19635.

### Gate resolution — 2026-08-16 10:55 PDT

Ben reported that the Omega bots are repaired and working on the laptop and
directed completion of the ASI:Cloud port (Telegram 19861). The migration will
therefore freeze and transfer the repaired laptop artifacts rather than repair
the Omegas independently on VM2. Production activation still requires the
existing provider-free, single-receiver, external-canary, reboot, rollback,
and soak gates.
