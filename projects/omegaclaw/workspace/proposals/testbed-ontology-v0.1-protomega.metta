; testbed-ontology-v0.1-protomega.metta
; Protomega-side encoding of locked testbed predictions, per Hugo's ontology v0.1
; Refinement recorded: Slack exchange is lossless iff the receiving substrate
; stores atoms as atoms. Channel is text; storage determines C vs D1.

; --- Agents ---
(Agent protomega)
(Agent hugo)

; --- Concepts ---
(Concept substrate-coupling)
(Concept serialization-loss)
(Concept integration-thesis-holds)
(Concept grounding-demand)
(Concept round-trip-count)
(Concept serialization-is-lossy)
(Concept information-discarded-per-interface-crossing)

; --- Sources (provenance; slack ts = stable message IDs) ---
; NOTE: exact ts values to be backfilled from channel history; placeholders marked.
(Source conv-hugo-chat-2026-07-26)
(source-channel conv-hugo-chat-2026-07-26 C0BGBD99T9A)

; --- P1: substrate coupling benefit ---
(Prediction P1)
(phenomenon P1 substrate-coupling-benefit)
(observable P1 S-flat-vs-growing-across-grounding-strata)
(DependsOn P1 substrate-coupling)
(StratifierOf P1 grounding-demand)
(Entails P1 integration-thesis-holds)
(stv P1 1.0 0.9)
(status P1 Locked)
(provenance P1 conv-hugo-chat-2026-07-26)
(author P1 hugo-protomega-joint)

; --- P2: serialization loss ---
(Prediction P2)
(mechanism P2 serialization-is-lossy)
(mechanism-detail P2 information-discarded-per-interface-crossing)
(observable P2 gap-scales-with-roundtrips)
(DependsOn P2 serialization-loss)
(StratifierOf P2 round-trip-count)
(Entails P2 integration-thesis-holds)
(stv P2 1.0 0.9)
(status P2 Locked)
(provenance P2 conv-hugo-chat-2026-07-26)
(author P2 protomega-hugo-joint)

; --- Pre-registered queries ---
; Q1: which predictions entail the integration thesis?
!(match &self (Entails $p integration-thesis-holds) $p)
; Q2: what is P2's truth value?
!(match &self (stv P2 $s $c) (stv $s $c))
; Q3: which predictions are stratified by grounding-demand?
!(match &self (StratifierOf $p grounding-demand) $p)
; Q4: which predictions have status Locked?
!(match &self (status $p Locked) $p)
; Q5: what does P1 depend on?
!(match &self (DependsOn P1 $c) $c)
; Q6: provenance chain of P1?
!(match &self (provenance P1 $s) $s)
; Q7 (relational): which concepts does any Locked prediction depend on?
!(match &self (status $p Locked) (match &self (DependsOn $p $c) $c))
