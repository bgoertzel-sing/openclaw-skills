# P1B exact planted-PCFG CPU smoke

- Date: 2026-07-28
- Repository: `repos/hdc-cgcct-probes`, branch `agent/p0-core`
- Commit: `b4593f4144e10acd56675b96f88a70e77bf40d7e`
- Scope: local CPU implementation/smoke only; no remote resource provisioned

Implemented the exact finite planted-PCFG enumerator and deterministic
70/15/15 hash split, a six-block pre-norm causal decoder with the frozen
`128/4/512/6` architecture and dropout zero, final-hierarchy residual
extraction, and deterministic closed-form ridge readout selection with
sign-normalized output.

Verification:

```text
python3 -m pytest -q
22 passed

python3 scripts/run_p1b_manifest.py --output artifacts/p1b-manifest.json
manifest_scientific_sha256=72b5e9ba07fec6fc732b3e3b726cfa933d45b25ea3a39d2fbabec4b74290fecd
manifest_file_sha256=59a374f2945a524bdbe4b802ccfa6e4aceded966a7ba78a0ed55e9a893136fcc
samples=36864
```

An independent manifest replay was byte-identical. It contains the prescribed
2,048/512/512 samples per `(H,J)` stratum for `H={4,6}`, with no identity
overlap.

Two invocations of:

```text
python3 scripts/run_p1b_cpu_smoke.py --output artifacts/p1b-smoke-{a,b}.json
```

were byte-identical with SHA-256
`158c3a1dbe6956c90ec3c25bc4eaf7ceaba7507f7a8f08dda4dcb7fb72fda042`.
The smoke performed one AdamW update using the frozen model architecture,
verified finite loss/residuals, extracted the final hierarchy-token residual,
and exercised stable artifact/replay behavior. Peak observed RSS was
312,908 KiB.

This clears the local implementation smoke precondition, but it does not yet
authorize provisioning: `REMOTE_JOB.md` still lacks the exact live RunPod
GPU/price/image/storage/transfer command required immediately before launch.
No calibration or confirmation seed was run.
