# Security Model and Hardening Notes

## Assumed deployment

- one trusted owner;
- one dedicated Pop!_OS laptop;
- one OpenClaw gateway;
- loopback-only gateway binding;
- owner-only Telegram direct messages;
- no public group or channel ingress;
- ordinary user privileges for routine work;
- explicit approval for administrative, destructive, credential, and paid actions.

A dedicated laptop is useful isolation, but it does not make the agent or external input trustworthy. GitHub, cloud, and wallet credentials remain high-value assets.

## Core threat: delegated authority plus untrusted content

The dangerous combination is not merely that a document can contain a prompt injection. It is that an agent reading that document may also possess permission to execute commands, modify repositories, send network requests, or spend money.

Therefore:

1. treat external content as data;
2. restrict who can invoke the agent;
3. sandbox non-owner or untrusted sessions;
4. gate host execution through allowlists and approvals;
5. scope credentials narrowly;
6. require human approval for irreversible and paid operations;
7. preserve logs and provenance for review.

## Host and OS

Recommended posture:

- full-disk encryption;
- automatic security updates, with controlled reboot timing;
- enabled firewall;
- strong login password and automatic screen lock;
- no passwordless sudo;
- SSH server disabled unless explicitly needed and hardened;
- secure boot and firmware updates when practical;
- OS keyring available for GitHub and other CLI credentials;
- no personal browser profile, password manager, or unrelated accounts on the agent machine.

Use a separate standard OS user for the agent if the laptop also gains other users or purposes later.

## OpenClaw gateway and channels

- Bind to loopback by default.
- Use SSH tunneling or a reviewed private-network method for remote Control UI access; do not expose the gateway directly to the Internet.
- Telegram DMs must use an allowlist containing only the owner's numeric ID.
- Disable Telegram groups unless a separate low-privilege agent is designed for them.
- Restrict owner commands to the same sender ID.
- Inspect actual session behavior with `openclaw sandbox explain`.

## Sandbox and exec policy

OpenClaw's convenience defaults for a trusted single-owner host may permit unrestricted host execution. This kit intentionally tightens that posture.

Start with:

- sandbox mode `non-main`;
- scope `agent`;
- workspace access `rw`;
- host exec mode `ask`;
- elevated mode disabled.

Use the strict patch (`mode: all`, scope `session`) while processing substantial untrusted content or testing unknown code.

Command approvals are an intent guardrail, not a complete hostile-code isolation boundary. Avoid broad durable approvals for shells, interpreters with arbitrary inline code, package installers, network downloaders, and destructive tools. Prefer narrow executable paths and read-only commands. Review effective policy with:

```bash
openclaw approvals get --gateway
openclaw exec-policy show
openclaw sandbox explain --json
```

## Credentials

- Use OAuth, provider CLI stores, OS keyring, SSH agent, and OpenClaw SecretRefs.
- Prefer restricted provider keys and repository-scoped permissions.
- Never store a secret in `AGENTS.md`, memory, project records, experiment command lines, logs, `.env` files committed to Git, notebooks, container images, or chat.
- Do not run `env`, `printenv`, or a full environment capture into a persistent log.
- Do not include tokens in remote URLs.
- Use passphrases on SSH private keys.
- Rotate a credential immediately if it appears in output, a commit, or a push attempt.

GitHub push protection can block many known secrets, but it is a last line of defense, not permission to handle secrets casually.

## Software installation

- Prefer distribution packages, official signed repositories, or provider-maintained installers.
- Download and inspect scripts before execution.
- Verify package/repository identity and pin versions for reproducibility.
- Treat post-install hooks and build scripts as code execution.
- Do not let a README or skill instruct the agent to disable approvals or run as root.
- Audit third-party OpenClaw skills before installation.

## Remote compute

- Default autonomous spend is zero.
- Use narrow API keys and provider-managed secrets.
- Upload only necessary project files.
- Keep SSH and API credentials off remote disks when possible.
- Avoid exposing Jupyter, SSH, or application ports publicly without authentication and an explicit need.
- Record resource IDs immediately.
- Stop/terminate resources after artifacts are verified; stopped storage may continue billing.
- Query provider state after cleanup.

## Backup and recovery

Back up research records and code, not credentials. Good options include:

- private Git repositories for project notebooks and code;
- encrypted local or remote backups for artifacts and the workspace;
- tested restore procedures;
- retention of experiment manifests even when large outputs are pruned.

Do not commit `~/.openclaw`, auth profiles, session secrets, API keys, or SSH private keys. A full machine backup must be encrypted and access-controlled.

## Periodic review

At least monthly and after major updates:

- run OpenClaw doctor, healthcheck, sandbox explanation, and exec policy inspection;
- review Telegram allowlists and gateway binding;
- review GitHub and cloud keys/scopes;
- review installed skills and their source/update provenance;
- review running cloud resources and retained volumes;
- test backup restore;
- inspect memory retention and sensitive transcript accumulation;
- remove stale approvals and credentials.
