# 03 — OpenClaw workspace and configuration

## Install

```bash
npm install -g openclaw@2026.6.10
openclaw onboard --install-daemon
```

Use official OpenClaw release provenance and inspect any installer before executing it. The npm command above avoids piping a remote script into a shell.

## Bootstrap

`bootstrap-workspace.sh` creates only generic context/policy, catalog, project templates, skills, plugin source, and helpers. It refuses to overwrite an existing workspace unless `FORCE=1`; back up and diff before using that override.

After bootstrap, review:

- `AGENTS.md`: operating/approval/reproducibility policy
- `SOUL.md`: epistemic/persona style
- `IDENTITY.md`, `USER.md`, `TOOLS.md`: recipient-controlled identity/profile/environment
- `HEARTBEAT.md`: brief read-only checks
- `MEMORY.md` and `memory/README.md`: durable-memory boundary
- `catalog/RESEARCH_RULES.md`, `catalog/PROJECTS.md`, `catalog/KANBAN.md`
- every installed skill and plugin

## Configuration

`templates/openclaw-config/openclaw.example.json5` is an **example/merge source**, not a whole-machine replacement. OpenClaw schemas change. On the target version:

```bash
openclaw config schema > /tmp/openclaw-schema.json
openclaw config patch --file ./your-reviewed.patch.json5 --dry-run
openclaw config patch --file ./your-reviewed.patch.json5
openclaw config validate
```

Keep Gateway `bind: "loopback"`; enable the OpenAI-compatible chat/responses endpoint for OmegaClaw. Generate a random Gateway token and expose it to OpenClaw and OmegaClaw through protected service/environment configuration. Use `openclaw secrets configure`, SecretRefs, and:

```bash
openclaw secrets audit
openclaw secrets reload
```

Never put actual tokens into the example JSON5.

## Skills and plugins

Workspace skills live at `<WORKSPACE>/skills`; they can override same-named managed skills. Run:

```bash
openclaw skills check
openclaw plugins validate <WORKSPACE>/plugins/intent-model-router
openclaw plugins doctor
```

The intent model router is shipped **disabled**. Configure current recipient-selected model IDs/pricing/budgets and pass its tests before enabling. Automatic paid frontier escalation remains off by default.

## Memory and auxiliary stores

Canonical placement:

- chronology/open loops → `memory/YYYY-MM-DD.md`
- stable cross-project preferences/facts → `MEMORY.md`
- project state/results → `projects/<slug>/`
- external sources/provenance → `library/<slug>/`
- indexes/status summaries → `catalog/`
- unverified consolidation proposals → `DREAMS.md` if adopted

Search before writing, preserve provenance/epistemic status, and resolve contradictions. Semantic/vector search supplements source inspection. Build optional QMD or other indexes only after checking current OpenClaw docs/config schema; do not copy another person's vector index.

## Model policy

- economical routine model for ordinary traffic and scheduler jobs;
- stronger coding/reasoning model for hard implementation/research;
- expensive independent frontier model only for selective expert reviews or escalation;
- explicit local cost telemetry/budget; no silent automatic spend;
- provider failover improves availability, not epistemic independence—use distinct review lanes when independence matters.
