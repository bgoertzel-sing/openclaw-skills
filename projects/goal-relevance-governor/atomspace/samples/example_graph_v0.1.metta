;; Goal Relevance Graph -> MeTTa Atomspace
;; schema_version=0.1
;; as_of=2026-09-08T01:40:00Z

;; -- Type definitions --
(: Goal Concept)
(: Project Concept)
(: Task Concept)
(: Resource Concept)
(: Result Concept)
(: Constraint Concept)
(: Verdict Concept)

;; -- Nodes --
(: g_g_build_omegaclaw Goal)
(g_g_build_omegaclaw "Build and operate OmegaClaw persistent agent infrastructure" top active 1 high)
(: g_g_initial_demo Goal)
(g_g_initial_demo "Initial demonstration of agent infrastructure" intermediate achieved 1 medium)
(: g_g_ir_translation Goal)
(g_g_ir_translation "IR translation layer for WMTM" intermediate active 2 medium)
(: p_p_conversation_governor Project)
(p_p_conversation_governor "OmegaHive Conversation Governor" confirmatory_research E1_signal_validation)
(: t_t_stale_codegen Task)
(t_t_stale_codegen "Plain2MeTTa code-generation worker" active reversible)
(: t_t_wmtm_tests Task)
(t_t_wmtm_tests "Run WMTM test suite" active reversible)
(: t_t_hardening Task)
(t_t_hardening "Production hardening of egress pipeline" active irreversible)
(: t_t_blocked_task Task)
(t_t_blocked_task "Deploy canary to production" active checkpointable)
(: t_t_no_goal Task)
(t_t_no_goal "Orphaned refactoring task" active reversible)
(: r_r_shared_runtime Resource)
(r_r_shared_runtime "Shared symbolic-language runtime (SWI-Prolog)" process True)
(: res_res_wmtm_285 Result)
(res_res_wmtm_285 "WMTM 285/285 tests pass")
(: c_c_ben_attendance Constraint)
(c_c_ben_attendance "Operator attendance required for live canary")

;; -- Edges --
(contributes_to t_t_stale_codegen g_g_initial_demo)
(contributes_to t_t_wmtm_tests g_g_ir_translation)
(contributes_to t_t_wmtm_tests g_g_build_omegaclaw)
(contributes_to t_t_hardening g_g_build_omegaclaw)
(part_of t_t_hardening p_p_conversation_governor)
(contributes_to t_t_blocked_task g_g_ir_translation)
(blocks c_c_ben_attendance t_t_blocked_task)
(occupies t_t_wmtm_tests r_r_shared_runtime)
(occupies t_t_hardening r_r_shared_runtime)
(provides_evidence_for res_res_wmtm_285 g_g_ir_translation)

;; -- Verdict rules (declarative, not yet executed) --

;; Rule 1: STOP_STALE -- task has no active parent goal
(= (check_stop_stale $task)
   (let $goals (direct_goals $task)
        (if (== $goals ())
            (verdict $task STOP_STALE)
            (if (all_inactive $goals)
                (verdict $task STOP_STALE)
                (empty)))))

;; Rule 2: BLOCKED -- constraint blocks task
(= (check_blocked $task)
   (let $blockers (blocking_constraints $task)
        (if (not (== $blockers ()))
            (verdict $task BLOCKED)
            (empty))))

;; Rule 3: PAUSE_RECOVERABLY -- holds exclusive resource needed by higher-priority task
(= (check_pause_recoverably $task)
   (let $resources (occupied_exclusive_resources $task)
        (let $holders (resource_holders $resources)
             (if (any_higher_priority $holders $task)
                 (if (is_checkpointable $task)
                     (verdict $task PAUSE_RECOVERABLY)
                     (empty))
                 (empty)))))

;; Rule 4: DEFER -- premature irreversible hardening on early-stage research
(= (check_defer $task)
   (let $project (project_of $task)
        (if (and (is_exploratory $project)
                 (is_early_stage $project)
                 (is_irreversible $task))
            (verdict $task DEFER)
            (empty))))

;; Rule 5: REPLAN -- parent goal superseded
(= (check_replan $task)
   (let $goals (transitive_goals $task)
        (if (any_superseded $goals)
            (verdict $task REPLAN)
            (empty))))

;; Rule 6: ESCALATE -- multiple active goals, no evidence
(= (check_escalate $task)
   (let $goals (active_goals $task)
        (if (and (> (length $goals) 1)
                 (not (has_evidence $task))
                 (is_active $task))
            (verdict $task ESCALATE)
            (empty))))

;; Default: CONTINUE
(= (evaluate_task $task)
   (superpose
    ((check_stop_stale $task)
     (check_blocked $task)
     (check_pause_recoverably $task)
     (check_defer $task)
     (check_replan $task)
     (check_escalate $task)
     (verdict $task CONTINUE))))
