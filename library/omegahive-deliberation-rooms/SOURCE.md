# Source: OmegaHive Deliberation Rooms

- Type: `PDF`
- Authors/organization: Cassio Pennachin, drafted with the OmegaHive design-partner session
- Publication/version date: 2026-07-29
- Retrieved: `2026-08-14`
- Canonical URL or identifier: user-supplied design PDF
- Local source path: `library/omegahive-deliberation-rooms/omegahive-deliberation-rooms-2026-07-29.pdf`
- SHA-256: `8c6d6b3916d7353b5e7818fab2a20abe98d8c8a6d553df936316fec44419e762`
- License/access constraints: user-supplied; no license stated
- Privacy tier: `local-private`
- Tags: `omegahive`, `deliberation`, `rooms`, `wake-based-agents`, `conversation-governor`, `slack`
- Related projects: `projects/omegahive-conversation-governor`, `projects/omegaclaw`

## Summary

Defines wake-based multi-seat deliberation rooms for OmegaHive. Chat is a
temporary deliberation surface; committed files and the event ledger remain
the durable source of truth. Seats are task-scoped and non-resident. A room
opens with a question, roster, and synthesizer, and closes with committed
conclusion references or explicit abandonment. The proposed MVP uses Slack
because bots can see other bots and preserve native seat identity.

## Key claims or contents

- Non-resident, wake-based seats dissolve several failure generators of
  resident conversational systems (Sections 1, 3, and 5; pp. 1--4).
- Nothing said in a room becomes real until it lands through the committed
  write path (Section 4, p. 3).
- Deliberation landing rate is the principal operational metric: conclusions
  committed divided by rooms opened (Section 3, p. 2).
- Rooms are explicitly not a task queue, write path, durable knowledge store,
  or resident listener (Section 3, p. 2).
- The Slack MVP cannot validate automated wake behavior at scale, chat as a
  general operating surface, multi-human/privacy boundaries, or full
  Telegram identity clarity (Section 7, p. 5).
- Telegram requires a degraded bridge-bot design because Telegram bots cannot
  see other bot messages (Section 8, pp. 5--6).

## Methods or implementation details

One Slack channel per deliberation; one app/token per seat; pull-on-wake
history reading; manual live-span wakes first and per-turn wakes second; a
designated synthesizer commits conclusions and archives the transcript. The
ledger records only open and close events, not message traffic.

## Limitations and uncertainties

The MVP addresses deliberation topology and conversation failure modes, not
goal selection, cross-project priority arbitration, task relevance, resource
conflicts, or opportunity-cost scheduling. Its claims about automated wakes
remain untested until wakes automate. Telegram loses native per-seat identity
and introduces a bridge bottleneck.

## Relevance to current work

Deliberation rooms can supply the human/multi-seat review surface for creating
and revising a goal graph and for resolving ambiguous strategic decisions.
They do not obviate a goal-relevance governor: the graph/evaluator is needed
to detect when active work no longer advances current priorities and to
trigger a room only when deliberation is warranted.

## Quotations or excerpts

“Nothing said in a room is real until it is committed through the write path.”

## Follow-up questions

- Should goal/priority changes be a new typed committed artifact or ordinary
  decision/order files with a goal-graph projection?
- Which relevance verdicts can execute automatically, and which should open a
  deliberation room?
- Can retrospective replay of recent failures establish useful trigger and
  false-positive thresholds before live scheduling authority is granted?
