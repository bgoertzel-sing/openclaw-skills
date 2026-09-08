# ProtoCosmo2 skill migration inventory

Source inspected read-only: `experiments/protocosmo2-phase1-snapshot/skills/`.
The newer `protocosmo2/imported/skills/` directory is empty. This is a
classification of the 19 preserved snapshot skills, not a migration. No live
runtime, credential, Telegram identity, or legacy PeTTa path was accessed.
The SHA-256 of the lexically sorted `sha256sum` manifest for the 19 `SKILL.md`
files is `c3f43e356897560f9647c628af1e93290d7652eb150840d9ba45a087b39f4959`.

## KEEP

These are useful, text-only operating playbooks and do not depend on the
quarantined Omega runtime. Before reuse, prefer the current workspace copy
where one exists and compare versions rather than copying an older duplicate.

- `experiment-ledger`
- `follow-through-contract`
- `hyperon-workbench`
- `knowledge-curation`
- `remote-compute-guardrails`
- `repository-operations`
- `research-library`
- `research-projects`
- `research-rules-checklist`

## REIMPLEMENT

The intent is useful, but the preserved text binds to OpenClaw-specific tools,
mutable global files, cron/session behavior, browser installation assumptions,
or concrete channel registries. Recreate only the smallest needed interface on
top of clean upstream facilities after ordinary conversation passes.

- `cross-agent-kanban`: retain compact project visibility; replace direct
  OpenClaw cron/session/tool assumptions.
- `google-drive`: retain structured Drive access only through an approved
  connector/credential boundary; do not carry credential-path assumptions.
- `kanban-task-board`: consolidate with the workspace project/task records;
  remove live cron/session coupling.
- `playwright`: use an approved isolated browser tool when actually needed;
  do not carry package/browser installation assumptions into Omega.
- `telegram-channel-registry`: retain symbolic destination lookup, but rebuild
  as a thin adapter with no embedded IDs and immutable origin routing.

## DROP

These encode autonomous scheduling, persistent/nested supervision, or a
mandatory agent-review controller. They overlap the broken runtime pattern or
are unnecessary for restoring ordinary conversation.

- `daily-bot-bot-project-discussions`
- `persistent-subagent-orchestration`
- `plain-spec-governor`
- `recurring-project-progress-worker`
- `subagent-execution-contract`

## Explicit exclusions

No snapshot skill is named `private_canary`, `deferred-job`,
`OpenClawFileBridge`, `phase5`, `phase6`, or `acceptance-controller`. Those
runtime components and all bespoke nested supervisors remain excluded by
architecture, even if related prose appears elsewhere.

## Migration gate

Do not install or copy any item yet. After the clean upstream conversational
baseline passes, compare each KEEP item with the current canonical workspace
skill, select exact bytes deliberately, and test in the isolated ProtoCosmo2
staging config. REIMPLEMENT items require a small spec and provider-free test.
