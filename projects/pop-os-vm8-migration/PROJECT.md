# Pop!_OS Proto-Hive Migration to ASI Replacement VMs

- Slug: `pop-os-vm8-migration`
- Status: `active`
- Created: `2026-08-11`
- Last reviewed: `2026-08-12`
- Owner: Benjamin Goertzel

## Purpose

Migrate the four Pop!_OS proto-hive identities—ProtoCosmo, ProtoCosmo2,
ProtoMega/Protomega, and ProtoMega2/Protomega2—to ASI:Cloud replacement VMs 1
and 2, preserving state, identity, routing, credentials, and rollback. VM8/VM7
were deactivated and are superseded as targets.

## Success criteria

- VM8 has pinned, reproducible runtimes and supervisors for all four identities.
- Staging never competes for a production Telegram update stream.
- Final cutover preserves each cursor and mutable state with exactly one receiver
  per bot identity.
- Fresh human-authored Telegram canaries pass for text and safe attachments.
- Services survive a supervisor restart and a VM reboot.
- The laptop remains a verified rollback target until the VM8 soak passes.
- A detailed operator handover exists for Ben's agents, covering the final
  VM1 topology, image/Compose identifiers, mounted data and secret categories,
  startup/status/backup/restore/rollback commands, validation evidence,
  known limitations, and any open work. It must contain no secret values.

## Scope

### In scope

- Read-only local inventory, dependency manifests, transfer plan, VM8 audit,
  staged synchronization, supervisor installation, controlled cutover, soak,
  rollback, and evidence capture.
- ProtoCosmo2 repair remains a prerequisite for assigning it the separate Iter
  upgrade lane, but Iter itself is not part of this migration workstream.

### Out of scope for now

- Migrating unrelated local projects/data.
- Provisioning, resizing, or retaining additional paid resources.
- Credential rotation itself; Ben deferred it until post-migration cleanup in
  Telegram 18367. Temporary credentials may be used within migration scope
  while preventing further disclosure.

## Current state

Elija corrected the target topology on 2026-08-12 (Telegram 18529-18533): the
complete four-agent laptop deployment migrates together to VM1. The agents are
not split across VMs. VM2 is reserved for separate prototyping and is outside
this migration's installation, staging, deployment, and cutover scope. Earlier
VM2 staging evidence is historical only; leave those disabled artifacts
untouched and do not add Docker or migration components there.

Ben authorized access and migration to replacement ASI:Cloud VM1 and VM2 on
2026-08-12 (Telegram 18266), then made this the primary task (18272). The
provider sheet reports each as 4 vCPU, 16 GiB RAM, and 128 GiB boot disk;
region, image, billing, and observed runtime state remain to be verified.
Credentials supplied in Telegram are temporary and must not be copied into
Git, project records, or command output. Immediate next step: bounded read-only
connectivity and host inventory on both replacements.

Ben directed on 2026-08-12 (Telegram 18367) that credential rotation is
post-migration cleanup and must not block staging or cutover. Continue using
the supplied temporary credentials within this migration scope without further
disclosure; re-escalate only for active misuse evidence, authentication failure
requiring replacement, or a platform-enforced blocker.

On 2026-08-12 Ben and Elija adopted Docker Compose as the primary deployment
path (Telegram 18398-18412). The revised plan packages pinned runtimes,
supervision, health checks, and receiver configuration in containers while
keeping per-identity state and secrets in bounded host mounts. Existing native
staging remains a fallback. Single-receiver cutover, fresh canaries, reboot
validation, soak, and laptop rollback remain mandatory acceptance gates. Plan:
`docs/revised-containerized-migration-plan.pdf` (ASCII LaTeX source alongside).
Ben explicitly adopted that PDF as the authoritative execution plan in
Telegram 18429. The persistent migration worker must follow its phases and
gates; its immediate action is Phase 0/1 mount reconciliation and a
credential-free local image/Compose build. Native systemd staging is fallback
only and must not continue as the primary implementation path.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|

## Environments

Document local virtual environments, containers, toolchain pins, datasets, and remote resources without credentials.

## Key results

- VM2 basic network baseline on 2026-08-18/19 found no infrastructure-level
  reliability problem: 20/20 SSH sessions, 60/60 DNS lookups, 80/80 HTTPS
  requests, 90/90 ICMP replies, and 10/10 small downloads passed; Telegram
  HTTPS averaged 110 ms and Telegram ICMP averaged 29 ms with zero loss. VM2
  stayed inert. This shifts diagnosis of the delayed cutover reply above the
  network layer. Evidence:
  `experiments/20260819T025848Z-vm2-network-latency-reliability/RUN.md`.

- Independent deterministic migration-status cron
  `8bdc49db-97e1-46bc-812b-a3b55781b0cf` now reports to the migration Telegram
  group every ten minutes without waiting for the long migration work cycle to
  finish. Its first acceptance run delivered successfully on 2026-08-12 22:32
  PDT while the worker was running.
- Seven-page revised containerized migration plan compiled successfully with
  Tectonic on 2026-08-12; source is ASCII-only and PDF text/visual checks
  passed. Evidence: `docs/revised-containerized-migration-plan.{tex,pdf}`.

## Open questions

- VM8 CPU/GPU, RAM, disk, region, OS image, network exposure, and current price.
- Whether VM8 is already running/billed and the approved 48-hour cost ceiling.
- Post-migration credential rotation ownership and timing.
- Desired post-cutover disposition: keep laptop stopped-but-ready for rollback,
  and for how long.

## Related projects and concepts

- `projects/omegaclaw/`: Omega runtime, transport, and active repair evidence.
- `projects/openclaw-omegaclaw-replication-kit/`: general replication guidance.

## Risks

- Duplicate Telegram receivers can lose/reorder updates or create spam.
- Copying broad OpenClaw state may leak unrelated credentials and conversations.
- The submitted archive contained live-looking secrets already exposed to model
  routes; reuse before rotation would compound the incident.
- VM cost and storage billing are presently unbounded/unknown.
- ProtoCosmo2 is online but not yet accepted for substantive long requests.
- Stale plan text assigns agents to VM2; current execution must follow the
  later VM1-only topology correction above.
