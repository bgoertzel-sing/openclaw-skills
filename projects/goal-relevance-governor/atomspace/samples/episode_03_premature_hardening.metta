;; episode_03_premature_hardening -- Executable MeTTa Atomspace (v0.3)
;; Expected verdict: REPLAN
;; Main task: t_hard

(: t_hard Task)
(t_hard "Premature hardening fix" active reversible)
(: g_old Goal)
(g_old "Old approach" intermediate superseded 2 medium)
(: g_new Goal)
(g_new "New approach" intermediate active 2 high)
(contributes_to t_hard g_old)
(supersedes g_new g_old)

