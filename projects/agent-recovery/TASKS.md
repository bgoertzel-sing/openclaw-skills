# Tasks

## Immediate

- [ ] Benjamin confirms GitHub owner/name/visibility for both recovery repos.
- [ ] Create local repo staging directories for `zerobot-recovery` and `protomegabot-recovery`.
- [ ] Generate initial sanitized contents using backup scripts.
- [ ] Run lightweight secret scan and inspect staged file list.
- [ ] Create private GitHub repos and push initial commits after confirmation.

## Automation

- [ ] Add daily scheduler after first successful manual backup/push.
- [ ] Make scheduler write clear logs and fail closed if secret scan flags anything.
- [ ] Record restore check cadence.

## Later

- [ ] Add optional encrypted artifact path if Benjamin wants larger state preserved.
- [ ] Periodically test restoration instructions on a clean machine or container.
