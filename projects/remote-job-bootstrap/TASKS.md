# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] **RunPod historical incident report for Ben (2026-08-06).**
  Deliverable: a source-backed PDF of documented RunPod attempts, outcomes,
  contributing agent/process failures, current remediation, and the exact
  current `runpodctl` skill as an appendix. Acceptance: generated PDF opens,
  source table links every material claim to a project record/session or local
  command receipt, and no credentials/private keys are reproduced. Next
  command: inventory remote-job records and historical session transcripts.
  Evidence: `docs/runpod-historical-incident-report-20260806.pdf` (9 pages,
  SHA-256 `7bbe3c13f4e78ea1927d265d57da7abfb8251cf0d51a9f0304beb5636f625848`);
  source `docs/runpod-historical-incident-report-20260806.tex`.

- [x] Inspect `runpodctl 2.8.0-22dc71f` pod-create serialization without
  provisioning. Deliverable: source-backed comparison of omitted `--ports`,
  explicit `22/tcp`, omitted `--ssh`, and explicit `--ssh`, plus any retained
  historical pod-spec evidence. Acceptance: exact source revision, commands,
  sanitized outputs, interpretation, and limitations recorded in a local
  experiment; no provider mutation or spend. Next command: locate the official
  `runpodctl` source revision and trace the pod-create request builder. Evidence
  path: `experiments/20260731T145013Z-runpodctl-payload-inspection/`.
  Completed 2026-07-31: installed-binary loopback capture proved omitted
  `--ssh` still sends `startSsh:true`, while omitted `--ports` removes the
  field. Archived exact commands also proved at least two readiness failures
  already used `22/tcp`, so port omission is not a sufficient general cause.

- [x] Run the approved raw-image B arm against the successful template SSH
  control. Deliverable: control-plane, direct TCP, and authenticated-SSH
  evidence from the identical underlying image launched via `--image`, with
  explicit ports/SSH but no template startup inheritance. Acceptance: result
  recorded under `experiments/20260731T140535Z-raw-image-ssh-ab/`, pod
  terminated within 10 minutes, and post-cleanup pod list excludes it.
  Completed 2026-07-31: TCP and authenticated SSH passed, PID 1 included
  `/start.sh`, and the pod was deleted after about 48 seconds. No further
  command; evidence path: `experiments/20260731T140535Z-raw-image-ssh-ab/`.

- [x] Run the approved template-based Secure RTX 4090 SSH canary.
  Deliverable: control-plane, direct TCP, and authenticated-SSH evidence from
  one `runpod-torch-v280` pod with explicit `8888/http,22/tcp` ports and SSH.
  Acceptance: results and pod ID recorded under
  `experiments/20260731T133317Z-template-ssh-canary/`, pod terminated within
  10 minutes, and the post-cleanup pod list excludes it. No further command;
  the recorded `command.sh` is retained for provenance. Evidence path:
  `experiments/20260731T133317Z-template-ssh-canary/`. Completed 2026-07-31:
  TCP and authenticated SSH passed; the remote reported RTX 4090; pod deleted
  after about 74 seconds and the post-cleanup list was empty.

- [x] Create and populate the approved public GitHub bootstrap repository.
  Deliverable: public repository, initial reviewed commit, and immutable
  release assets for the frozen MusicGen and RelaLeap bundles. Acceptance:
  remote owner/name explicitly confirmed; every asset downloads without
  credentials and matches its published SHA-256; secret and accidental-file
  scans pass. Completed 2026-07-29: public repo commit `8cad73d`, release
  `v0.1.0`; anonymous HTTPS downloads matched `SHA256SUMS`. Evidence:
  `PROJECT.md` and `releases/v0.1.0/`.

## Next

- [ ] Implement and run a harmless no-GPU startup/return transport probe before
  either scientific job. Local acceptance passed at bootstrap commit
  `9192df1`: public source fetch/hash, probe archive, pinned `runpodctl`
  hash, and Croc receive all passed without SSH. Remaining acceptance:
  provider startup semantics and Croc return observed from a bounded remote
  pod; exact logs and hashes retained. Approved 2026-07-29 by Benjamin
  Goertzel (Telegram message 14638): Secure A40, at most 30 minutes/USD 0.22.
  The remote attempt failed: no returned probe archive, and the subsequent
  three-pod debugging sequence exceeded the original one-pod/30-minute/USD
  0.22 envelope. All probe pods were removed. Evidence:
  `experiments/20260729T1555Z-remote-transport-probe/`. Next: redesign the
  observable startup/logging seam, propose a fresh bounded envelope, and wait
  for explicit approval before another remote resource is created.

## Waiting or blocked

- [ ] None.

## Someday or exploratory

- [ ]

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.
