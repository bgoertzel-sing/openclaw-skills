Execute the VM1 Proto-hive independent-branch rebuild. Work actively; do not
merely report or plan.

Before acting, read completely:

- `/home/openclaw/research-agent/AGENTS.md`
- `skills/active-agent-upgrades-and-repairs/SKILL.md`
- `skills/remote-compute-guardrails/SKILL.md`
- `projects/pop-os-vm8-migration/docs/revised-containerized-migration-plan.tex`
- `projects/pop-os-vm8-migration/{PROJECT.md,TASKS.md,DECISIONS.md}`
- the migration experiment `RUN.md`
- `docs/VM1-BRANCH-SNAPSHOT-SCOPE.md`
- `docs/CRON-STATUS-CONTRACT.md`

Authoritative amendments:

1. All four agents belong on VM1; VM2 is out of scope and must remain
   untouched.
2. VM1 is a new independent branch while laptop agents continue. Strict
   cursor continuity, laptop shutdown, and identity-preserving receiver
   cutover are no longer objectives. Existing copied credentials remain inert
   reference material and must never activate the clone. New identities,
   provider credentials, Telegram credentials, and state roots are required
   before activation.
3. Docker Compose remains the primary deployment. Maintain per-agent config,
   secret, state, workspace, activation, and log isolation; fail closed without
   an activation marker; never place secrets in images, Git, Compose YAML,
   logs, commands, Markdown, or chat.

Find the first unmet amended critical-path gate and execute one bounded action:

1. Complete and SHA-256-verify the inert independent-branch workspace snapshot
   on VM1.
2. Finish the VM1-only four-service Compose render, image digest/inventory and
   minimum provider-free image acceptance.
3. Map the protected copied state plus workspace snapshot into four isolated
   clone roots and start services offline with polling impossible.
4. Validate mounts, local readiness, backup/restore and supervisor restart.
5. After explicit new-identity/credential assignment, activate clones in a
   controlled sequence and run external canaries.
6. Reboot/recovery, soak, and final `VM1-MIGRATION-HANDOVER.md`.

Do not redo completed bulk-copy verification unless evidence changed. Do not
spend cycles on VM2, offline package bundles, optional hardening, GitHub setup,
or documentation polish outside the required handover. Preserve unrelated
dirty work. Use persistent/resumable jobs for work longer than a cycle. Start
durable checkpointing by minute 8 and finish within 10 minutes. Update
`TASKS.md` and the migration `RUN.md` with evidence, current amended PDF gate,
and exact next action.

Return exactly one concise summary following `CRON-STATUS-CONTRACT.md`. Do not
announce or send messages yourself; the independent reporter handles routine
group delivery. Do not output command chatter or secret material. Never return
`NO_REPLY`.
