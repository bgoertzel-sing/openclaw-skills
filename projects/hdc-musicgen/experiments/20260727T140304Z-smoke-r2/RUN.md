# Run 20260727T140304Z-smoke-r2

- Project: `hdc-musicgen`
- Status: `both pods terminated before Stage 0/S/A; no-result`
- Local or remote: `former RunPod Secure Cloud pods vbu5r47gstyl16 and 2jh6oxjzogdexe (deleted)`
- Source commit: `8907d0fcba2897be48d435f49f501661ab4d8f4b`

## Question

On an eight-track real-audio subset, do Stage 0/S/A pass the amended,
support-aware smoke gate while retaining alignment and conditioning stops?

## Result

**Observed:** RunPod preflight was healthy and later offered an RTX 3090. Pod
`vbu5r47gstyl16` received the code and retained audio corpus and began
dependency setup, but later became SSH-unreachable before any Stage 0/S/A
command started; deletion returned `deleted: true`, followed by an empty list
and provider 404. Replacement pod `2jh6oxjzogdexe` exposed a healthy GPU and
local sshd through the web terminal, but provider SSH routing never supplied a
usable shell; it was deleted before transfer, dependency installation, or any
Stage 0/S/A command, and the subsequent all-pods list omitted it. No stage
artifacts exist, so the run is a terminal no-result. See `REMOTE_JOB.md` for
the retained chronology.

## Next command

Do not provision or contact a provider from this handoff. A future attempt
requires a fresh, explicit availability/cost authorization and its own
provider/resource/cost/data/stop plan.

See `REMOTE_JOB.md` for the approval, policy amendment, and cleanup plan.
