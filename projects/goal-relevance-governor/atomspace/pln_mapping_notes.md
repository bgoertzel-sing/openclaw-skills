# PLN / AtomSpace Mapping — Exploratory Notes

## Goal
Map the GRG (Goal Relevance Governor) graph schema to OpenCog's AtomSpace
/ PLN (Probabilistic Logic Networks) concepts, enabling probabilistic
relevance reasoning over the task-goal graph.

## Current State (2026-09-08)
- MeTTa-Python bridge evaluator v0.3: working, 16/16 tests, 5/5 cross-validated
- Uses MeTTa `match` for graph queries, Python for verdict cascade
- No PLN/probabilistic reasoning yet — purely symbolic

## Mapping: GRG Schema → AtomSpace Concepts

| GRG Concept | AtomSpace Type | PLN Role |
|---|---|---|
| Task | ConceptNode | Subject of evaluation |
| Goal | ConceptNode | Target state |
| contributes_to | EvaluationLink / InheritanceLink | Means-ends relation |
| supersedes | EvaluationLink | Goal replacement |
| blocks | EvaluationLink | Constraint relation |
| holds | EvaluationLink | Resource possession |
| status (active/achieved/...) | PredicateNode | State predicate |
| rank (1-5) | NumberNode | Priority weight |
| urgency | ConceptNode | Time pressure |

## PLN Inference Rules (proposed)

1. **Relevance propagation**: If task T contributes_to goal G, and G is active,
   then T is relevant (truth value = strength of contributes_to link).

2. **Staleness inference**: If all goals of T have status=achieved/cancelled,
   infer STOP_STALE with TV=(1,1) (certain).

3. **Supersession propagation**: If G_new supersedes G_old, and T contributes_to
   G_old, then T's relevance to G_old is reduced (TV strength decreases).

4. **Blocking inference**: If constraint C blocks T, and C is hard,
   infer BLOCKED with high confidence.

5. **Resource conflict**: If T1 and T2 both hold exclusive resource R,
   infer mutual exclusivity — higher-priority task gets resource.

## Implementation Path

### Option A: Pure MeTTa + PLN rules
- Define PLN inference rules as MeTTa equations
- Use MeTTa's built-in matching for forward chaining
- Challenge: MeTTa doesn't have native truth value / probability support

### Option B: Python bridge + PLN truth values
- Extend metta_evaluator.py to track truth values
- Use Python for probabilistic aggregation
- Simpler, but less declarative

### Option C: OpenCog AtomSpace (full PLN)
- Port graph to OpenCog AtomSpace
- Use URE (Unified Rule Engine) for inference
- Most powerful, but heavy dependency

## Recommendation
Start with Option B (extend Python bridge with truth values),
then evaluate whether Option C is needed for complex probabilistic
reasoning. Option A is currently impractical due to MeTTa's lack
of truth value support.

## Next Steps
1. Add truth value tracking to MeTTaEvaluator (strength, confidence)
2. Define probabilistic versions of verdict rules
3. Test with ambiguous cases (e.g., goal 70% achieved)
4. Evaluate whether URE/full PLN is needed
