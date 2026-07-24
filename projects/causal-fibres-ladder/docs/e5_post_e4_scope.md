# E5 scope after the E4 channel diagnostic (calibration + confirmation)

Date: 2026-07-24
Updated: 2026-07-24 (confirmation)

The E5 W1/W2 standalone MORK `linalg` kernel evidence remains valid:
six-layer forward parity and five-step relaxation parity pass. Actual in-store
hosting remains blocked by the missing typed tensor resource/sink adapter.

The E4 diagnostic is now confirmed on three disjoint seeds. The logit/hidden
ratio is `2.16--2.18` (calibration `2.46`); `|both−logit|` is below `1.5e-5`;
all 9 weight series are strictly increasing through 5×; and the full4/two-cap
ratio is exactly `2.0`. This sharpens W4:

1. Separate constraint retrieval from neural injection. MORK/MeTTa should
   return factor bindings or constraint residuals with provenance; a typed
   numerical sink applies them.
2. Prioritize a direct-logit constraint sink before a hidden-state relaxation
   sink. On the reduced rig, logit injection delivers about 2.2--2.5 times the
   headroom recovery of hidden settlement, and adding hidden settlement to the
   logit path changes G by at most `1.5e-5` (confirmed on disjoint seeds).
3. Parameterize constraint weight and anchor weight explicitly. The tested
   range did not saturate through 5x.
4. Preserve information provenance. Full4 is label-equivalent on the
   synthetic grammar, so W4 must distinguish observed/deployable bindings from
   diagnostic ground-truth constraints.
5. Meter query expressions, returned bindings, tensor transfers, sink
   operations, and latency separately. Do not hide the store-to-tensor bridge
   in kernel timing.

W3 sparsified-gradient maintenance and W5 cost accounting remain open.
No new MORK implementation is authorized by this scope note; the next
engineering prerequisite is a reviewed typed tensor resource and logit-sink
interface.

