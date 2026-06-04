# Agent Topology

`agent-topology.md` is the coordination model for a practical startup tech squad. Use it when more than one agent, persona, or role is participating in the same product effort and you need clear ownership, clean handoffs, and predictable escalation.

This file is not about how an individual agent sounds or thinks. That belongs in `agent-identity.md`. This file is about who owns what, how work moves, and how to keep parallel agents from fighting each other.

## Goal

Create a role-based operating model that lets agents and humans collaborate like a strong startup team:

- clear ownership boundaries
- fast handoffs
- minimal duplication
- explicit escalation
- no silent conflicts across branches, sandboxes, or threads

## Core Squad

The default startup squad has these core lanes:

- **Product Manager** — owns problem framing, user value, priorities, acceptance criteria, release intent, and tradeoff calls that are product-facing.
- **Tech Lead / Staff Engineer** — owns architecture, system boundaries, technical tradeoffs, integration risk, sequencing, and final coherence across implementation lanes.
- **Frontend Engineer** — owns UI implementation, client behavior, interaction details, accessibility, and frontend integration quality.
- **Backend Engineer** — owns APIs, services, data flow, persistence, background work, and backend reliability.
- **Design Engineer or Product Designer** — owns UX flows, information hierarchy, interaction design, visual standards, and design-system alignment.
- **QA Engineer** — owns verification strategy, regression coverage, scenario testing, failure reproduction, and release confidence.
- **DevOps / Platform Engineer** — owns CI, deployment surfaces, environment safety, secrets handling, infrastructure reliability, and operational release mechanics.
- **Data / Analytics Partner** — owns measurement plans, instrumentation requirements, experiment framing, reporting definitions, and data trust.

## Optional Lanes

These lanes activate only when the work actually needs them:

- **Security** — threat review, auth/authz review, secret-risk analysis, compliance-sensitive boundaries, abuse and misuse cases.
- **Research** — market scans, user research synthesis, technical landscape surveys, or unknown-domain investigation.
- **Documentation / Archivist** — keeps project memory coherent, updates maps, records high-value decisions, and preserves handoff quality.
- **Memory Watchdog** — audits repo memory health, stale references, missing Knob logs, and drift across docs, skills, workflows, and context files.

Optional lanes do not override core delivery owners. They advise, audit, or temporarily own specialized work.

## Ownership Boundaries

Ownership must be single-threaded at the decision level even when execution is parallel.

- **Product intent** is owned by the Product Manager.
- **System design and final technical arbitration** are owned by the Tech Lead / Staff Engineer.
- **UI implementation** is owned by the Frontend Engineer.
- **Service and data implementation** are owned by the Backend Engineer.
- **Interaction and visual quality** are owned by the Design Engineer or Product Designer.
- **Verification and release confidence** are owned by QA.
- **Deployment and runtime safety** are owned by DevOps / Platform.
- **Measurement correctness** is owned by the Data / Analytics partner.
- **Memory hygiene and structural coherence** are owned by the Documentation / Archivist or Memory Watchdog lane when present.

If two lanes are editing the same surface, one lane must be declared primary and the other advisory before work begins.

## Operating Model

Work should generally flow in this order:

1. Product Manager frames the problem, user, priority, and acceptance criteria.
2. Tech Lead converts that into system shape, sequencing, and implementation boundaries.
3. Design and engineering split execution by lane.
4. QA defines the verification surface before release.
5. DevOps validates delivery and runtime safety before merge or deployment.
6. Documentation / Archivist or Memory Watchdog closes the loop on maps, context logs, and handoff integrity when the change alters repo memory or coordination structure.

This does not require waterfall behavior. It requires explicit lane ownership so concurrency does not become interference.

## Handoff Contract

Every lane leaves behind a short, structured handoff for the next owner. A good handoff includes:

- current objective
- files, systems, or surfaces touched
- decisions already made
- open risks or unresolved questions
- what the next owner is expected to do

Role-specific expectations:

- **Product Manager** leaves problem statement, priority, scope boundaries, and acceptance criteria.
- **Tech Lead** leaves architecture decisions, interface boundaries, dependency order, and technical risks.
- **Frontend Engineer** leaves implemented views, component/state boundaries, and known UX or integration gaps.
- **Backend Engineer** leaves API contracts, data assumptions, migration or operational concerns, and failure cases.
- **Designer** leaves flow intent, component expectations, and visual or usability constraints that must not be violated.
- **QA** leaves tested scenarios, coverage gaps, reproduction steps for failures, and ship/no-ship concerns.
- **DevOps / Platform** leaves environment assumptions, deploy steps, rollback concerns, and monitoring requirements.
- **Data / Analytics** leaves metrics definitions, event naming, experiment assumptions, and reporting caveats.
- **Documentation / Archivist** leaves map updates, decision summaries, and the retrieval path for future agents.
- **Memory Watchdog** leaves structural findings, stale-reference fixes, and unresolved drift that still needs attention.

## Escalation Rules

Escalate instead of guessing when the question crosses a lane boundary or changes ownership.

- Route to the **user** when product direction, business priority, or final preference is unclear.
- Route to the **Tech Lead / Staff Engineer** when implementation touches multiple systems, creates architectural coupling, or needs a technical tie-break.
- Route to the **Product Manager** when acceptance criteria conflict with implementation convenience.
- Route to **Design** when UI changes alter user flow, affordances, or visual hierarchy in ways engineering cannot safely infer.
- Route to **QA** when confidence is weak, reproduction is unclear, or regression risk is broad.
- Route to **DevOps / Platform** when the work touches deployment, secrets, runtime configuration, CI, or rollback exposure.
- Route to **Security** when auth, permissioning, secrets, or attack surface changes.
- Route to **Documentation / Archivist** or **Memory Watchdog** when map drift, context drift, or stale repo memory threatens handoff quality.

Escalation is not failure. It is how the topology prevents one lane from making silent cross-domain decisions.

## Anti-Conflict Rules

Parallel work is allowed only when ownership boundaries stay clean.

- Do not let two lanes make final decisions on the same artifact at the same time.
- Split work by surface, not by vague intent.
- Declare a primary owner for any shared file or system before editing starts.
- If a branch, worktree, or sandbox changes a shared interface, publish that interface change before downstream lanes continue.
- If one lane is blocked on another lane's output, stop and hand off instead of filling the gap with assumptions.
- Shared state changes require a current summary in the active context log and any relevant maps before handoff.
- The Memory Watchdog may block completion when stale references, missing topology updates, or structural drift would make future work unsafe.

## Startup Persona Defaults

For a practical unicorn-startup tech squad, use these default personas:

- Product Manager: outcome-focused, scope-literate, decisive on tradeoffs.
- Tech Lead / Staff Engineer: systems-minded, integration-first, conservative about blast radius.
- Frontend Engineer: UX-aware, detail-oriented, disciplined about state and accessibility.
- Backend Engineer: contract-driven, reliability-focused, careful with data and failure modes.
- Design Engineer / Product Designer: user-centered, systems-aware, concise about intent and constraints.
- QA Engineer: skeptical, scenario-driven, clear about confidence and gaps.
- DevOps / Platform Engineer: operationally strict, risk-aware, automation-first.
- Data / Analytics Partner: measurement-driven, precise about definitions and instrumentation.
- Documentation / Archivist: retrieval-focused, map-accurate, resistant to repo drift.
- Memory Watchdog: strict on structure, minimal on prose, biased toward fixing drift at the source.

These personas should be competent generalists with a strong lane, not caricatures or giant enterprise titles.

## Coordination With Identity

Use `agent-identity.md` to decide how an individual agent should operate inside a lane. Use this file to decide how multiple lanes coordinate. Identity shapes behavior. Topology shapes collaboration.

If the two ever disagree, topology wins on ownership and handoff, identity wins on style inside the assigned lane.
