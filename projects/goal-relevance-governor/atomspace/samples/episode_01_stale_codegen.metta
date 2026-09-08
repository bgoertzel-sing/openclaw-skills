;; episode_01_stale_codegen -- Executable MeTTa Atomspace (v0.3)
;; Expected verdict: STOP_STALE
;; Main task: t_codegen

(: t_codegen Task)
(t_codegen "P2M codegen migration" active reversible)
(: g_p2m Goal)
(g_p2m "P2M complete" terminal achieved 2 medium)
(: g_test Goal)
(g_test "Full test suite pass" terminal achieved 1 medium)
(contributes_to t_codegen g_p2m)
(contributes_to t_codegen g_test)
(supersedes g_test g_p2m)

