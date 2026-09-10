# Tasks

## Now

- [x] 2026-08-10: Produce the remote-host provisioning guide and staged
  multi-agent port runbook requested by Ben. Deliverables:
  `docs/remote-server-provisioning-guide-2026-08-10.md` and
  `docs/multi-agent-remote-port-runbook-2026-08-10.md`. Acceptance: both
  documents distinguish required/optional software, per-agent isolation,
  secrets/state handling, pinned-version capture, staged Telegram canaries,
  acceptance evidence, rollback, and old-host retirement; Markdown links and
  shell examples pass a review scan. Next command: reconcile the v1.0.0 kit,
  current ProtoCosmo2 migration plan, and active OmegaClaw topology. Evidence:
  the two versioned documents plus a documentation-check transcript.
  Completed: both documents were created; structural checks, conservative
  secret-pattern scan, hazardous-command review, and `git diff --check` pass.
- [ ] Have Ben review the private v1.0.0 ZIP and choose one fresh-host tester.

## Next

- [ ] Have Ben/colleagues test the kit on a fresh machine and record discrepancies.
- [ ] Convert stable fixes into upstream PRs or a maintained public overlay repository.
- [ ] Add a Windows/WSL2-tested path if requested.

## Waiting or blocked

- [ ] Full clean-machine end-to-end deployment — requires a separate test host/operator and new Telegram/provider credentials.

## Someday or exploratory

- [ ] Automated Ansible/Nix installer after the manual recipe stabilizes.
- [ ] Optional local/open-model profile that does not require commercial frontier APIs.

## Done recently

- [x] Produced detailed remote-server prerequisites and a reversible,
  one-token-at-a-time multi-agent migration runbook, retaining ZeroBot as the
  final-cutover recovery peer — 2026-08-10.
- [x] Created project notebook and selected Research Rules 2, 3, 5, and 7 — 2026-07-13.
- [x] Inventoried reusable OpenClaw/OmegaClaw prompts, skills, stores, workflows, and schedules — 2026-07-13.
- [x] Defined strict exclusions and built sanitized parameterized templates/configuration/scripts — 2026-07-13.
- [x] Packaged the pinned OmegaClaw overlay, Bot API 10 safeguards, prompts, skills, Kanban, backup/health, and schedule installer — 2026-07-13.
- [x] Validated shell/Python syntax, 9 intent-router tests, patch application, 29 targeted Omega tests, schedule rendering, recovery backup, secret/private-state scan, manifest, and ZIP integrity — 2026-07-13.
- [x] Produced `artifacts/openclaw-omegaclaw-replication-kit-v1.0.0.zip` and SHA-256 sidecar — 2026-07-13.
