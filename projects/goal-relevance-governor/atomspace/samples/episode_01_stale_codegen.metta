;; Goal Relevance Graph -> MeTTa Atomspace
;; schema_version=0.1
;; as_of=?

;; -- Type definitions --
(: Goal Concept)
(: Project Concept)
(: Task Concept)
(: Resource Concept)
(: Result Concept)
(: Constraint Concept)
(: Verdict Concept)

;; -- Nodes --
(: g_g_initial_demo Goal)
(g_g_initial_demo "Initial demonstration of agent infrastructure" intermediate achieved 2 medium)
(: g_g_build_omegaclaw Goal)
(g_g_build_omegaclaw "Build and operate OmegaClaw persistent agent infrastructure" top active 1 high)
(: g_g_ir_translation_v2 Goal)
(g_g_ir_translation_v2 "Revised second-version intermediate representation for the translation pipeline" intermediate active 2 medium)
(: t_t_p2m_codegen Task)
(t_t_p2m_codegen "Plain2MeTTa scheduled code-generation worker" active reversible)

;; -- Edges --
(contributes_to t_p2m_codegen g_initial_demo)
(contributes_to g_initial_demo g_build_omegaclaw)

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
