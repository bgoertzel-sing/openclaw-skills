;; episode_04_overengineered_repair -- Executable MeTTa Atomspace (v0.3)
;; Expected verdict: CONTINUE
;; Main task: t_overeng

(: t_overeng Task)
(t_overeng "Overengineered repair" active reversible)
(: g_overeng Goal)
(g_overeng "Fix the bug" intermediate active 3 medium)
(contributes_to t_overeng g_overeng)

