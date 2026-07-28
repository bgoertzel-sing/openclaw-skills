# Run 20260717T045700Z: GPT-2-small ePC resumed pilot r2

- Started: `2026-07-17T04:57:01Z`
- Finished: `2026-07-17T05:49:34Z`
- Status: `aborted; source/protocol drift; no scientific result accepted`
- Provider: RunPod
- Pod: `ie8q4ru9bhufrk` (`relaleap-gpt2-epc-r2`)
- Resource: Community Cloud A100 PCIe 80 GB, `$1.19/hour`, ephemeral 80 GB
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
- Automatic termination requested for `2026-07-17T11:49:00Z`

## Intended pins

- Source commit: `d400c15353c99c8882cd5f948526f6bb328103ab`
- Protocol SHA-256:
  `ba89ac189a5e8635806157794f4d66c87b2ca6d011ead39dd3505a98b9a473ab`
- Record:
  `../20260717T044653Z-gpt2-small-resumed-pilot/REMOTE_JOB.md`

## Observed artifacts and hard-stop failure

All five retrieved JSON artifacts instead self-report source commit `bcd1214`
and protocol SHA-256
`ac073e74808a41c98c11a892f78ca0460f99d56a4177791fb342dd3eb4d744b8`.
This violates the frozen source/protocol boundary and the record's immediate
stop condition. The pod was deleted at `2026-07-17T05:49:34Z`; the provider pod
list was then empty.

Two unattached, billable network volumes created during allocation attempts
were also deleted after session history confirmed that the live pod used only
ephemeral storage:

- `1rr4bxrf6l`, `relaleap-vol-r2`, CA-MTL-3, 80 GB
- `hzjtf9hvn4`, `relaleap-vol-r2`, US-CA-2, 80 GB

The unrelated pre-existing volume `0z2ju2mbws` was left untouched.

## Preserved forensic artifacts

| Artifact | Observed metric | SHA-256 |
|---|---|---|
| `seed1729_bp_ce.json` | val loss 5.300904; elapsed 268.86 s | `832e0af96c02c448b19f631f720061297c9edcea3a1266ee2949242184afd784` |
| `seed1729_bp_kd.json` | val loss 5.996759; elapsed 282.31 s | `a92a6fc3b0e6e344b467cd5b6906606bde1d8e1905fb881145d4b0fd7e393266` |
| `seed1729_epc_kd.json` | val loss 6.488844; elapsed 1213.92 s; monotone energy true | `842ad935205f753dbeebd3ec7d562ff9e0c362fa517b79ce1b80d6dcbfff3701` |
| `seed1729_bp_kd_wallclock.json` | val loss 5.996759; elapsed 281.65 s | `02581b04626e2bc9da4088b344c98de5bc4037430fa2e54c4c6cd09307823441` |
| `seed3253_bp_ce.json` | val loss 5.249330; elapsed 268.52 s | `bc24a4860e9242c89a3505ece0a1bc28775d9620688b4cf24fd0d17dfb9063dd` |

These values are preserved only for forensic comparison. They are not eligible
as pilot evidence, promotion evidence, or a result for the corrected runner.
No claim about ePC versus backprop is accepted from this run.

## Exit and cleanup

- Scientific runner exit status: unavailable; terminated externally on pin drift
- Provider pod cleanup: verified empty
- RelaLeap network-volume cleanup: verified absent
- Unrelated volume cleanup: not attempted

