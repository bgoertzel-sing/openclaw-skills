# ASI:Cloud VM8 migration job

- Provider: ASI:Cloud
- Resource: already-provisioned VM8 (`rnd-auto-elija-first-8-19e88e087a`)
- Approved by: Benjamin Goertzel, Telegram source 18137
- Approval window: 72 hours beginning 2026-08-11 12:31 PDT
- Approved spend: existing VM8 charges only; no resize, added storage,
  additional resource, or other incremental spend without a new approval
- Region/image/resource shape/storage/current price: not yet observable
- Remote address from operator archive: recorded only in the local SSH secret
  context; not duplicated here
- Credential handling: key extracted only to private OpenClaw state (directory
  mode 0700, key mode 0600); never copied to Git, Markdown, logs, or commands
  by value. Previously exposed material must be rotated before production
  cutover.

## Transfer and privacy plan

Inventory locally first. Transfer only pinned code, declared dependencies,
required per-agent mutable state, and narrowly selected secret references over
SSH/rsync. Exclude unrelated projects, caches, browser data, broad OpenClaw
session history, credential helpers, and archive material. Stage without
production Telegram polling.

## Stop, rollback, and artifacts

Laptop remains the rollback owner until VM8 passes per-identity external
canaries, supervisor restart, VM reboot, and soak. Stop the VM8 receivers—not
the VM itself—on any failed identity gate, then restore that identity on the
laptop. Return evidence to this project under `experiments/` and keep no secret
values in artifacts.

## First access attempt

At 2026-08-11 approximately 12:33 PDT, a bounded SSH connection to the
operator-supplied VM8 address timed out on TCP/22 after 10 seconds. No remote
command ran and no remote state changed. Next: verify current VM8 power/network
state and SSH address/port in the ASI:Cloud control plane.

## VM7 fallback probe

Ben authorized a read-only VM7 fallback probe in Telegram source 18141 under
the same existing-resource/no-resize constraints. The VM7 key was isolated and
validated in private OpenClaw state. Its operator-supplied endpoint likewise
timed out on TCP/22 after 10 seconds. No remote command ran and no remote state
changed. The common failure across adjacent VM7/VM8 endpoints suggests a
provider power/network/security-group or endpoint/port issue rather than an SSH
key-authentication failure.

## Replacement VM2 reconstruction

- Provider/account: ASI:Cloud, operator-provided replacement account context.
- Resource: already-provisioned VM2
  `rnd-auto-elija-first-2-60ce4d65a6`; observed Ubuntu 22.04, x86_64, 4 vCPU,
  16 GiB RAM. Provider sheet reports 128 GiB boot storage; region, image ID,
  and current price are not exposed through SSH.
- Authorization: Ben authorized access and migration to replacement VM1/VM2
  in Telegram 18266 and directed autonomous progress in 19458 and 19541.
  Elija explicitly authorized Docker installation on the VMs in 18499.
- Spend boundary: use this already-running VM2 only. No provisioning, resize,
  added storage, paid endpoint, or other incremental resource is authorized.
  This reconstruction introduces no known incremental provider cost; the
  existing VM charge is operator-controlled and price remains unobserved.
- Data/privacy: the accepted allowlisted agent snapshot and mount trees are
  already on VM2. Do not upload unrelated personal data, SSH keys, browser or
  keyring material. Secrets remain in protected host mounts and never enter
  image layers, Git, logs, or command arguments.
- Stop/rollback: on failed activation, stop the one hive container and remove
  polling activation; retain VM2 and its copied state unless the operator
  separately directs provider cleanup. Laptop receivers remain the rollback
  owner through acceptance and soak.
- Evidence return: non-secret receipts under
  `experiments/20260815T233126Z-vm2-one-hive-container/`.
