# Bach AAAI 2018 motivation tutorial: OmegaClaw assessment

Date: 2026-07-19
Evidence: `library/bach-aaai2018-modeling-emotion-motivation/`; page numbers below are tutorial slide/PDF page numbers.

## Claims actually made

- Motivation reflects needs, produces goals and directed behavior, and need not be emotional; emotion instead modulates perception, cognition, and action, receives valence from motivation and its object from cognition (p. 45).
- All goals serve at least one hard-wired demand; drives span physiological, social, and cognitive demands, while goals are learned affordances for satisfying or frustrating those needs (pp. 46–60).
- Changes in demand produce pleasure/distress proportional to the change. Those signals reinforce behavioral and episodic sequences and define appetitive/aversive goals (p. 53). Anticipated rewards also guide action through certainty, skill, delay, memories, and expectations (pp. 69, 74–77).
- Affect is a cognitive-system configuration. Its modulators include arousal, selection/securing thresholds, resolution, competence, certainty, and demand-derived pleasure/distress/valence; the modulation controls width, depth, and bias of perception, memory, planning, and action selection (pp. 86–90).
- Affective state is emergent from modulation; named emotions are directed affect plus configurations of those variables, not primitive labels (pp. 89, 96–98). Modulators have bounded level, baseline, volatility, and decay (pp. 95, 99–101).

## Agreements with the current OmegaSelf/Hyperseed direction

- The MetaMo/OmegaClaw split `X = G × M`, with appraisal updating modulators before decision, matches Bach's separation of needs/motives from emotion-as-modulation.
- The Hyperseed proposal to let arousal/coordination alter inference breadth and to make prediction a costly action is directly supported by Bach's claim that affect controls cognitive width, depth, bias, and complexity.
- `petta-memory` is a natural evidence seam: memories and expectations affect anticipated reward, while immutable evidence packets can keep appraisal replayable. GoalChainer remains the candidate decision/task-claim layer; ThreadKeeper remains the bounded effects and audit layer.
- OmegaSelf's event ledger and replay-equivalence gates are a good substrate for modulator dynamics because baseline, volatility, decay, and evidence identity must be explicit to distinguish state evolution from prompt drift.

## Tensions and cautions

- Bach assumes predefined needs and ultimately need-serving goals. MetaMo's individuation/transcendence overgoals and OmegaSelf's policy/evidence governance are broader normative commitments; they should not be silently reduced to scalar reward or declared hard-wired without a separate design decision.
- The tutorial supplies an architectural/computational proposal, not empirical validation that its chosen needs or equations are complete. Named-emotion examples should therefore remain explanatory projections, not runtime truth labels.
- Current GoalChainer heuristic scoring is largely stateless. Calling it motivation would overclaim until it carries bounded need state, temporal updates, anticipated outcomes, and evidence-linked appraisal.

## Next non-live empirical gate

Build a provider-free `motivation-state-v0.1` replay fixture with two cognitive needs only (competence and uncertainty reduction), explicit value/weight/decay plus valence, arousal, certainty, resolution, selection threshold, and securing rate. Feed one immutable `petta-memory` evidence snapshot into appraisal, rank a fixed set of GoalChainer candidate inference/tasks, and emit candidate-only ThreadKeeper records.

Pass conditions: identical input hashes reproduce the same state transition and ranking; record order is invariant; stale/mutated evidence, out-of-range/non-finite modulators, or missing temporal provenance fail closed; raising uncertainty urgency monotonically increases the designated information-gathering candidate under otherwise fixed inputs; no memory promotion, task claim, provider call, Telegram egress, or runtime wiring occurs. This gate tests the Bach/MetaMo interface without adopting his complete need taxonomy or changing live motivation.

