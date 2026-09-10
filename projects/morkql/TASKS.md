# Tasks

## Now
- [x] Create local `repos/morkql` implementation repository with MIT license and first frontend slice. Commit `c5c1ef6`: dependency-free parser/typed AST, `find` + long-query sugar, set forms, equality/inequality/safe negation, deterministic alpha-normalization, structured safety diagnostics, finite reference evaluator, deterministic explain output; 9 tests pass.
- [ ] Identify and pin canonical Morkl/Zippy sources referenced by the spec. PathMap is pinned at `233fbbac7c7b8d8b2414b54689a2da4331d234c7`.
- [x] Install an isolated Rust nightly toolchain after provenance review; reproduce smallest upstream MORK smoke. Rust nightly 1.99.0 installed via rustup (userspace, `~/.cargo/bin`). `cargo build` succeeds; kernel tests pass; upstream `eval` workspace test has pre-existing import error at pinned commit.
- [ ] Implement schemas, relation arity checks, variable range restriction, and structured errors.
- [ ] Implement logical/reference evaluator for differential testing.

## Next
- [ ] Lower positive `find` to typed Core/MQT plan.
- [ ] Add set forms and positive Datalog-style rules with stratification/finite-range scaffolding.
- [ ] Implement deterministic explain-plan schema and compile certificate skeleton.
- [ ] Connect target AST to pinned MORK/Morkl runtime and compare results.

## Deferred
- [ ] petta-memory integration.
- [ ] petta-chem integration.
- [ ] Paid Runpod execution unless explicitly approved with cost and cleanup plan.
