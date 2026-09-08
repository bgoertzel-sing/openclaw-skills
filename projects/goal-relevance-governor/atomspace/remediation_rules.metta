;; Remediation Rules v0.1 (MeTTa)
;; ==============================
;; Maps verdicts to ordered remediation actions.
;; Each rule produces a list of action atoms that the RemediationEngine should execute.

;; STOP_STALE: abandon task, release resources, notify stakeholders
(remediation STOP_STALE
  (abandon_task)
  (release_all_resources)
  (notify_stakeholders))

;; ESCALATE: boost priority, allocate resources, set deadline, require evidence
(remediation ESCALATE
  (boost_priority critical)
  (allocate_resources)
  (set_deadline)
  (require_evidence))

;; PAUSE_RECOVERABLY: pause task, monitor blocker, resume when resolved
(remediation PAUSE_RECOVERABLY
  (pause_task)
  (monitor_blocker)
  (resume_task_when_free))

;; DEFER: park task, set trigger condition, monitor trigger
(remediation DEFER
  (park_task)
  (set_trigger_condition)
  (monitor_trigger))

;; REPLAN: redesign task, update goal link, reset progress, archive old approach
(remediation REPLAN
  (redesign_task)
  (update_goal_link)
  (reset_progress)
  (archive_old_approach))

;; CONTINUE: monitor task, set next checkpoint
(remediation CONTINUE
  (monitor_task)
  (set_checkpoint))

;; Query: given a verdict, return its action sequence
(= (get_remediation $verdict)
  (match
    (bind $actions
      (remediation $verdict $actions)
      $actions)))

;; Query: given a verdict, return the first (highest priority) action
(= (get_first_action $verdict)
  (match
    (bind $first
      (remediation $verdict $first $rest)
      $first)))

;; Query: check if a verdict requires resource management
(= (requires_resources $verdict)
  (match
    (remediation $verdict $actions)
    (member (release_all_resources) $actions)))
