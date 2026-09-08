;; episode_02_chem_blocking -- Executable MeTTa Atomspace (v0.3)
;; Expected verdict: BLOCKED
;; Main task: t_chem

(: t_chem Task)
(t_chem "Chemistry RL training" active reversible)
(: g_chem Goal)
(g_chem "Chem RL converged" intermediate active 2 high)
(contributes_to t_chem g_chem)
(: c_gpu Constraint)
(c_gpu "GPU unavailable" hard)
(blocks c_gpu t_chem)

