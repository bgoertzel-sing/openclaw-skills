# Remote Compute Operating Procedure

## Providers

The procedure applies to Runpod, ASI:Cloud, and similar GPU/CPU clouds.

Runpod currently offers official agent skills and `runpodctl`. ASI:Cloud advertises per-hour GPU VMs and OpenAI-compatible inference; exact account endpoints and provisioning interfaces must be verified from current official documentation or the operator's account.

## Decide whether remote compute is needed

Use local execution when it is adequate. Remote compute is justified by GPU memory, runtime, parallelism, reproducibility against a target image, or isolation requirements. Do not use it merely because a provider integration exists.

## Approval packet

Before provisioning, provide:

- project and experiment question;
- provider and resource specification;
- source of current price;
- estimated duration and total cost;
- hard maximum time/cost;
- storage and egress implications;
- image/template and dependency plan;
- code/data sensitivity and transfer method;
- cleanup rule.

Approval must be explicit and specific. The default budget is zero.

## Prepare reproducibly

1. Commit or otherwise pin the code state.
2. Create an experiment and remote-job record.
3. Pin image/template and dependency versions.
4. Build a deterministic entry script.
5. Define output paths and success criteria.
6. Test a small local or cheap smoke run when possible.

## Provision and connect

- Give the resource a project/run name.
- Record resource ID, region, GPU, storage, price, and creation time immediately.
- Use provider CLI/API or an operator-reviewed interface.
- Use SSH keys, not passwords, when VM access is required.
- Restrict public ports and inbound access.

## Transfer

Prefer `rsync` over SSH for resumable transfers. Exclude credentials, unrelated files, local caches, `.openclaw`, SSH private keys, and environment files. Validate source commit and data hashes remotely.

## Execute and monitor

- Run in `tmux` or a provider job abstraction.
- Capture command, stdout, stderr, exit status, GPU/CPU metrics, and relevant provider events.
- Set a deadline/timeout and monitor spend.
- Stop on unexpected data exposure, cost growth, repeated failure, or the approved bound.

## Retrieve and verify

- Copy results into the experiment artifact directory.
- Check hashes, file counts, and a semantic smoke test.
- Record missing/corrupted outputs before cleanup if debugging requires remote state.

## Cleanup

- Stop or terminate according to provider semantics and the approval packet.
- Delete unneeded volumes, endpoints, snapshots, and public services.
- Verify provider state with a fresh list/query.
- Record final cost and cleanup timestamp.

For Runpod, stopping a Pod can leave storage charges; terminate resources that are no longer needed after artifact verification.

## Serverless inference adapters

For an OpenAI-compatible endpoint such as ASI:Cloud inference:

- store base URL and model alias as non-secret configuration;
- store API key through a secret reference;
- run a low-cost health/model-list request if documented;
- capture request configuration without message secrets;
- bound retries, concurrency, and token use;
- do not assume full API parity until tested.
