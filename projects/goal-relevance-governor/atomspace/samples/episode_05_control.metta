;; episode_05_control -- Executable MeTTa Atomspace (v0.3)
;; Expected verdict: CONTINUE
;; Main task: t_control

(: t_control Task)
(t_control "Control task" active reversible)
(: g_control Goal)
(g_control "Control goal" intermediate active 2 medium)
(contributes_to t_control g_control)

