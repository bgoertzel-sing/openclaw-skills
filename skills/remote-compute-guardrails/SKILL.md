---
name: remote-compute-guardrails
description: Plan and control paid or remote compute on Runpod, ASI:Cloud, or similar providers. Use before provisioning, starting, resizing, using, or cleaning up a remote GPU/CPU resource, and when transferring code, data, or artifacts.
---

# Remote Compute Guardrails

The autonomous spend budget is USD 0.

## Approval gate

Before a cost-incurring action, present:

- provider/account context;
- requested resource, region, image/template, storage, and network needs;
- current price source and estimated cost for expected duration;
- maximum time/cost guardrail;
- code/data upload plan and privacy classification;
- stop versus terminate behavior;
- artifact return and verification plan.

Obtain explicit operator approval. A prior approval applies only to the described resource and bound.

## Job record

Create `REMOTE_JOB.md` or an experiment `RUN.md` before provisioning. Use project/run identifiers in resource names and labels. Record provider resource IDs immediately.

## Credentials

- Use provider CLI credential stores, secret references, or provider-managed secrets.
- Never put keys in commands, logs, Markdown, Git, container images, notebooks, or chat.
- Prefer restricted keys and the minimum API permissions.
- Do not upload unrelated local files, `.git` credential helpers, SSH private keys, or OpenClaw state.

## Execution

- Pin the source commit and image/template version.
- Transfer only required files, preferably with `rsync` over SSH.
- Run through a named `tmux` session or provider job mechanism.
- Capture environment, command, logs, metrics, and status.
- Monitor for failure and cost overrun; stop when the approved bound is reached.

## Cleanup

1. Retrieve artifacts to the declared local path.
2. Verify completeness and hashes or smoke tests.
3. Stop or terminate as approved. Remember that stopped resources may retain billable storage.
4. Remove unneeded volumes, endpoints, snapshots, and public services after confirmation.
5. Query provider state again and record cleanup evidence and final observed cost.

Do not leave a resource running while writing a summary.

## Provider notes

For Runpod, prefer official `runpodctl`, Runpod agent skills, or documented APIs. Run `runpodctl doctor` before use.

For ASI:Cloud, use only operator-provided/current documented base URLs, models, SSH methods, and provisioning interfaces. Do not invent missing API details.
