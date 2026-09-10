# Run 20260717T155300Z: six-layer ePC outcome gate allocation attempt

- Project: `relaleap`
- Started: `2026-07-17T15:53:00Z`
- Finished: `2026-07-17T22:19:39Z`
- Status: `failed before readiness; stalled pod terminated`
- Provider: RunPod
- Approval: Ben's owner-authenticated message, “let us launch the new 6 layer run”
- Bound and frozen inputs:
  `../20260717T154506Z-epc-outcome-6layer-preflight/REMOTE_JOB.md`

## Intended execution

- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Source archive SHA-256:
  `8d05ef730b7137bf830f9f3efa5c16345012165ef97ded62828436cb05c0127c`
- GPU: one Community Cloud A100 PCIe 80 GB at no more than `$1.19/hour`
- Regions: one attempt in `CA-MTL-3`, then one fallback in `EU-RO-1`
- Storage: ephemeral only; no network volume
- Hard termination: five hours after allocation

## Allocation result

1. The first command used the display-name ordering `NVIDIA A100 PCIe 80GB`
   and failed before allocation with `Unknown GPU type`.
2. Retrying the correct provider GPU ID `NVIDIA A100 80GB PCIe` in
   `CA-MTL-3` failed before allocation: no instances available.
3. The single authorized fallback in `EU-RO-1` failed identically before
   allocation. Provider availability then reported both A100 PCIe and A100 SXM
   unavailable in Community and Secure Cloud.

No pod, volume, code transfer, data download, GPU time, or scientific result
was created in this first allocation sequence. Provider inventory at the
16:20 UTC heartbeat was empty.

## Fresh approval and expanded-region attempt

At `2026-07-17T21:26:34Z`, Ben gave a fresh owner-authenticated instruction:
“Expand region and if that doesnt work expand GPU type, lets get this done.”
The existing GPU type succeeded without a region restriction, so no GPU-type
fallback was attempted.

- Pod: `lop52u56xugpxk`
- Created: `2026-07-17T21:26:45Z`
- Resource: one Community Cloud A100 PCIe 80 GB in Canada at `$1.19/hour`
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
- Storage: 80 GB ephemeral container disk; zero pod/network volume
- Provider termination: `2026-07-18T02:26:43Z`

The provider never made the pod ready. At `2026-07-17T22:18Z`, after about 52
minutes, `runpodctl pod get` still reported `uptimeSeconds: 0` and SSH returned
`pod not ready`. The launch session had dropped its continuation; no local
launcher or monitor process was active. No source, data, or command was
transferred and no scientific runner started.

Heartbeat cleanup terminated only pod `lop52u56xugpxk` at approximately
`2026-07-17T22:19Z`. The provider confirmed `deleted: true`; a subsequent pod
inventory was empty. No job-created volume existed. The sole listed network
volume, `0z2ju2mbws` in `EU-SE-1`, was pre-existing and unrelated.

## Exit status and conclusion

- Initial allocation command exit status: nonzero for all three commands
- Expanded-region allocation exit status: zero, but readiness failed
- Scientific runner exit status: not started
- Conclusion: no scientific conclusion; the available allocation stalled
  before runtime readiness and was terminated to stop cost exposure
- Decision needed: investigate provider readiness or retry under a new bounded
  allocation. The fresh approval was consumed by this terminated pod and does
  not authorize an unattended replacement.
