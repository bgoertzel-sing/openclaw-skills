# VM2 operator access and ProtoCosmo administration

- Updated: 2026-08-19
- Scope: ASI VM2 access from the Pop!_OS OpenClaw host
- Credential rule: never paste the VM2 private key into chat or a command line

## From the Pop!_OS terminal

The reviewed helper reads the existing Elija-supplied VM2 address and private
key into a temporary mode-0600 file, uses it for one SSH session, and deletes
the temporary directory on exit.

```bash
VM2_ADMIN=/home/openclaw/research-agent/projects/pop-os-vm8-migration/experiments/20260815T233126Z-vm2-one-hive-container/vm2-admin.sh
```

Read-only status:

```bash
sudo "$VM2_ADMIN" status
```

Interactive VM2 root login:

```bash
sudo "$VM2_ADMIN" login
```

Recent ProtoCosmo gateway logs:

```bash
sudo "$VM2_ADMIN" logs
```

Restart an already activated ProtoCosmo gateway:

```bash
sudo "$VM2_ADMIN" restart
```

`restart` is deliberately fail-closed. It requires both the existing
ProtoCosmo activation marker and exactly one existing `proto-hive` container.
It will not activate an inert VM2 or perform a cutover. It waits up to 90
seconds for Docker health to become `healthy` and prints a pass/fail receipt.

## From Ben's MacBook

The MacBook does not yet have a verified VM2 SSH profile or private key. Do not
send the key through Telegram. Establish MacBook access later by securely
installing the existing VM2 private key in `~/.ssh/` with mode `0600`, pinning
the verified host key, and adding a named `Host vm2-proto-hive` entry. Until
that credential handoff is completed and tested, administer VM2 through the
Pop!_OS helper above.

## Recovery boundary

During the current rollback state VM2 should report zero activation markers,
zero containers, and `gateway=inert`. Do not use raw Compose commands to start
it. Production cutover and rollback remain controlled by the reviewed boundary
operator scripts on Pop!_OS.
