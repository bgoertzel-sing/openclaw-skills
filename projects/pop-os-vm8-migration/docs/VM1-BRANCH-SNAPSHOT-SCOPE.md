# VM1 independent-branch snapshot scope

The snapshot is an inert, credential-free seed for rebuilding the four-agent
stack on VM1 as a new independent branch. It is not a runnable copy and must
not activate the copied Telegram identities.

## Included

- Workspace governance and identity Markdown, memory, catalog, notebooks,
  decisions, tasks, skills, plugins, scripts, tests, templates, and root Git
  metadata, including dirty/untracked working files that survive exclusions.
- Current `projects/omegaclaw` and `projects/protomegabot2` source/configuration
  work, including their Git metadata and uncommitted code.
- Small supporting repositories and project records needed to understand or
  reproduce the stack.
- Non-secret Codex configuration and installed skill definitions only.

## Excluded

- All `.env`, secret, credential, key, token, access-sheet, authentication,
  and known-host files; `.openclaw` provider profiles; SSH/GitHub credentials.
- `scratch/`, `archive/`, media, logs, caches, shell snapshots, session logs,
  live databases, and temporary files.
- Virtual environments, `node_modules`, compiled/build directories, container
  layers, dependency caches, large experiment artifacts, datasets, model
  weights, Chroma/vector databases, and nested source clones already pinned by
  the container build.
- Live OpenClaw sessions/state already copied separately into protected VM1
  identity mounts.

## Activation rule

Extract beneath an inert mode-protected snapshot root. Do not mount it into a
receiver container or create `ENABLE-POLLING`. New provider and Telegram
credentials plus new state roots must be assigned before clone activation.
