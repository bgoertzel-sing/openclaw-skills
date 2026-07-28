# Run 20260727T140304Z-smoke-r2

- Project: `hdc-musicgen`
- Status: `terminated before execution; local handoff only`
- Local or remote: `former RunPod Secure Cloud pod vbu5r47gstyl16 (deleted)`
- Source commit: `8907d0fcba2897be48d435f49f501661ab4d8f4b`

## Question

On an eight-track real-audio subset, do Stage 0/S/A pass the amended,
support-aware smoke gate while retaining alignment and conditioning stops?

## Result so far

**Observed:** RunPod preflight was healthy and later offered an RTX 3090; pod
`vbu5r47gstyl16` was created in CZ at USD 0.50/hour. After two refused SSH
connections, no Stage 0/S/A command, data transfer, or GPU work occurred.
`runpodctl pod delete` returned `deleted: true`; the subsequent pod list was
empty and lookup returned 404. No stage artifacts exist.

## Next command

Do not provision or contact a provider from this handoff. A future attempt
requires a fresh, explicit availability/cost authorization and its own
provider/resource/cost/data/stop plan.

See `REMOTE_JOB.md` for the approval, policy amendment, and cleanup plan.
