(registered-n20-summary
  horizon (3 22)
  fixed-seeds (seed-7 seed-8 seed-9 seed-10)
  raf-incidence ((unguided 4) (weak-doob-h 4) (shuffled-guidance 4))
  first-hit-ticks
    ((unguided ((seed-7 5) (seed-8 3) (seed-9 8) (seed-10 10)))
     (weak-doob-h ((seed-7 3) (seed-8 3) (seed-9 8) (seed-10 8)))
     (shuffled-guidance ((seed-7 5) (seed-8 3) (seed-9 4) (seed-10 3))))
  productive-events
    ((unguided 32) (weak-doob-h 32) (shuffled-guidance 32))
  post-run-pool-identity passed
  causal-ablation guiding-term-removal-does-not-collapse-controls
  pivot all-arms-positive-pool-composition-not-guidance
  emergence-claim none)
