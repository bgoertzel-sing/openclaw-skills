;; =============================================================================
;; PROTOMEGATRON ACTIVE PROJECT PLAN
;; =============================================================================
;; Daily-refreshed Kanban plan for ProtomegaTron's active work tracks.
;; Updated 2026-07-29. Run `directive-board project-plan.metta` for status.

(meta plan (id "PROTO-2026Q3") (title "ProtomegaTron Active Projects") (status "active") (author "agent:protomegatron"))

;; ---------------------------------------------------------------------------
;; Agents & resources
;; ---------------------------------------------------------------------------
(given agent-protomegatron)
(given agent-protocosmobot)

;; ---------------------------------------------------------------------------
;; Track A: petta-memory ↔ protomega2bot integration
;; ---------------------------------------------------------------------------
(given task-ingestion-adapter)
(given task-provider-free-roundtrip)
(given task-shadow-mode)
(given task-staging-deploy)

(given no-deps-ingestion-adapter)

;; Staging approved by Ben 2026-07-29; token rotation requirement dropped 2026-07-27
(given staging-approved)

(normally r-ingestion   (and task-ingestion-adapter no-deps-ingestion-adapter)                   ready-ingestion-adapter)
(normally r-roundtrip   (and task-provider-free-roundtrip completed-ingestion-adapter)            ready-provider-free-roundtrip)
(normally r-shadow      (and task-shadow-mode completed-provider-free-roundtrip)                  ready-shadow-mode)
(normally r-staging     (and task-staging-deploy completed-shadow-mode staging-approved)          ready-staging-deploy)

;; ---------------------------------------------------------------------------
;; Track B: Hyperseed formalization (ongoing)
;; ---------------------------------------------------------------------------
(given task-hyperseed-substack)
(given task-hyperseed-self-observation)
(given task-hyperseed-abstraction)

(given no-deps-hyperseed-substack)
(given no-deps-hyperseed-self-observation)

(normally r-substack    (and task-hyperseed-substack no-deps-hyperseed-substack)                  ready-hyperseed-substack)
(normally r-selfobs     (and task-hyperseed-self-observation no-deps-hyperseed-self-observation)  ready-hyperseed-self-observation)
(normally r-abstract    (and task-hyperseed-abstraction completed-hyperseed-substack completed-hyperseed-self-observation) ready-hyperseed-abstraction)

;; ---------------------------------------------------------------------------
;; Track C: ThreadKeeper hardening review
;; ---------------------------------------------------------------------------
(given task-tk-suite-run)
(given task-tk-pr-split)
(given task-tk-boundary-audit)

(given no-deps-tk-suite-run)

(normally r-tk-suite    (and task-tk-suite-run no-deps-tk-suite-run)                             ready-tk-suite-run)
(normally r-tk-split    (and task-tk-pr-split completed-tk-suite-run)                            ready-tk-pr-split)
(normally r-tk-audit    (and task-tk-boundary-audit completed-tk-suite-run)                      ready-tk-boundary-audit)

;; ---------------------------------------------------------------------------
;; Track D: Agent-recovery restore drill (due 2026-08-01)
;; ---------------------------------------------------------------------------
(given task-alert-routing-verify)
(given task-restore-drill)

(given no-deps-alert-routing-verify)

(normally r-alert       (and task-alert-routing-verify no-deps-alert-routing-verify)             ready-alert-routing-verify)
(normally r-drill       (and task-restore-drill completed-alert-routing-verify)                  ready-restore-drill)

;; ---------------------------------------------------------------------------
;; Track E: plain2metta repo work
;; ---------------------------------------------------------------------------
(given task-plain2metta)
(given no-deps-plain2metta)

(normally r-plain2metta (and task-plain2metta no-deps-plain2metta)                               ready-plain2metta)

;; ---------------------------------------------------------------------------
;; Assignments
;; ---------------------------------------------------------------------------
(normally assign-ingestion   (and ready-ingestion-adapter agent-protomegatron)       assign-to-ingestion-adapter-protomegatron)
(normally assign-substack    (and ready-hyperseed-substack agent-protomegatron)       assign-to-hyperseed-substack-protomegatron)
(normally assign-selfobs     (and ready-hyperseed-self-observation agent-protomegatron) assign-to-hyperseed-selfobs-protomegatron)
(normally assign-tk-suite    (and ready-tk-suite-run agent-protocosmobot)             assign-to-tk-suite-protocosmobot)
(normally assign-alert       (and ready-alert-routing-verify agent-protomegatron)     assign-to-alert-routing-protomegatron)
(normally assign-plain2metta (and ready-plain2metta agent-protomegatron)              assign-to-plain2metta-protomegatron)

;; ---------------------------------------------------------------------------
;; Daily Kanban-refresh recurrence (meta-task, self-referential)
;; ---------------------------------------------------------------------------
(given task-kanban-refresh)
(given no-deps-kanban-refresh)
(given kanban-recurrence-active)

(normally r-kanban (and task-kanban-refresh no-deps-kanban-refresh kanban-recurrence-active) ready-kanban-refresh)
(normally assign-kanban (and ready-kanban-refresh agent-protomegatron) assign-to-kanban-refresh-protomegatron)
