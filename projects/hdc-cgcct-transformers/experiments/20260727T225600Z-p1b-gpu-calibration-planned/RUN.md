# P1B three-seed GPU calibration

- Provider resource: RunPod pod `qy0rbiqrd3xvbf`
- GPU: one NVIDIA GeForce RTX 3090, 24 GiB
- Image: `runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`
- Price: USD 0.22/hour
- Created: 2026-07-29T00:03:24Z
- Terminated and deletion verified: 2026-07-29T00:22Z
- Nested source commit used for the completed artifacts: `a031645`

The exact three calibration seeds `12011`, `13121`, and `14251` completed.
Their returned raw artifacts passed local hash and finite-array verification:

```text
12011 b117ec174ae096fd6ce9e66562ac57f4f08f238981752c615c3315d60464f62b
13121 570ff9a4ba6fcaf4d867eabe16fea6edbc1b432ea225c4a5897356e8fc1b5381
14251 7607b6e9e22121cfebaf9170dab0f15b2d9dddfb2735f197397d3452ceb31cfe
```

Each artifact is scientifically gate-eligible, contains 14 frozen
dimension/arm cells, and reports a 177,209,344-byte peak GPU allocation.
`artifacts/criteria.json` freezes the calibration-seed payload hashes before
any confirmation seed is opened. No confirmation seed was run.

The planned `rsync` transfer failed because the pinned image lacks remote
`rsync`; transfer and retrieval used an SSH tar stream with the same source
exclusions. A duplicate local resume attempt was stopped immediately after
the pre-existing `COMPLETE` marker and completed artifacts were discovered;
the returned completed artifact timestamps predate that attempt.
