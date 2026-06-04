# Documentation.md

The canonical operating spec for AI-assisted repositories.

Use this file as the cross-project policy layer. It defines the minimum repo contract, document roles, mandatory rules, optional modules, anti-bloat guardrails, and the forking model. `README.md` explains a repo to humans. `AGENT.md` is the cold-start router for agents. `docs/context-orientation.md` is the running state log.

## 1. Purpose and Scope

`Documentation.md` exists to give projects a stable operating system for AI and human collaboration across vendors. It is not a product README and it is not a task workflow. It is the durable policy layer that should change slowly and apply broadly.

Use it to standardize:

- cold-start behavior
- context logging
- document ownership
- map hygiene
- secret handling
- handoff discipline
- repo forking and localization

Do not use it to store repo-specific implementation details, framework picks, or one-off task procedures.

## 2. Required Repo Contract

Every repo using this pattern should have these files:

- `README.md` for purpose, audience, usage, and working focus
- `AGENT.md` for cold-start order and routing
- `docs/context-orientation.md` for the active state log

Only include the folders the repo actually needs. Common modules are:

- `behavior/` for reasoning and context rules
- `workflows/` for repeatable procedures
- `skills/` for reusable agent capabilities
- `architecture/` for memory or systems architecture
- `design/` for UI and visual rules

If a folder is not serving the repo, do not create it just to match a template.

## 3. Document Roles

- `Documentation.md`: canonical operating policy for the repo or template it lives in
- `README.md`: human-facing project overview and adoption guide
- `AGENT.md`: short agent entrypoint that says what to read and in what order
- `docs/context-orientation.md`: newest-first log of meaningful repo state changes
- `behavior/`: durable reasoning rules and shared vocabulary
- `workflows/`: step-by-step procedures that implement policy without redefining it
- `skills/`: reusable capabilities, with pointers back to canonical docs instead of duplicated rule bodies
- `architecture/`: systems-level design, especially memory and governance architecture
- `design/`: project-specific UI, UX, and visual rules

The roles do not overlap. If two docs try to be authoritative for the same rule, collapse them into one source and point to it from everywhere else.

## 4. Mandatory Rules

- Read `AGENT.md` first on agent cold start, then follow its loading order.
- Keep canonical rules in one authoritative place. Prefer pointers over mirrors.
- Update `docs/context-orientation.md` after meaningful repo state changes, not for trivial noise.
- Keep newest entries at the top of `docs/context-orientation.md`.
- Never store secrets, API keys, tokens, or `.env` contents in docs, examples, or summaries.
- Do not commit `.env` files unless the user explicitly instructs it.
- Keep repo-specific implementation guidance local to that repo. Do not push local conventions back into the canonical base unless they are truly reusable.
- When folders or canonical files move, update every reference in the same change.
- When a new reusable Skill or module appears, update the relevant maps in the same change.

## 5. Optional Modules

These modules are opt-in. They are not default cold-start requirements unless the repo depends on them.

- `architecture/`: only when system architecture or memory architecture is part of the work
- `design/`: only when the repo owns UI, UX, or visual standards
- heavy workflow packs: only when the repo repeatedly performs those procedures
- `skills/`: only when the repo contains reusable capabilities worth carrying across projects

Optional modules should be documented as optional in both `README.md` and `AGENT.md`.

## 6. Anti-Bloat Rules

- Do not create a new doc if an existing doc can absorb the change without losing clarity.
- Do not duplicate canonical content into repo-local folders unless the local fork is intentionally diverging.
- Prefer one strong summary doc over many weak partial docs.
- Merge overlapping docs when they create retrieval ambiguity.
- Archive old context when the active log gets too large, but keep the hot log lean and current.
- Delete or replace stale pointer docs that no longer point anywhere real.

Documentation should make wayfinding cheaper. If a doc increases search cost without adding unique value, it is debt.

## 7. Forking Model

When a new project adopts this system:

1. Copy the minimum contract: `README.md`, `AGENT.md`, `docs/context-orientation.md`, and only the folders the project needs.
2. Localize `README.md` to the actual product or workspace immediately.
3. Keep `AGENT.md` short and repo-specific. It should route to the right materials, not restate the whole canon.
4. Copy only the canonical modules that the project will actively use.
5. Add repo-specific implementation structure early so the repo is not mostly policy docs.
6. Override workflows locally when the project needs a different procedure.
7. Keep reusable rules in the canonical source repo. Keep local execution details in the project repo.

## 8. Minimum Viable Repo Scaffold

Every new project should have both governance and working structure.

The minimum governance layer is:

- `README.md`
- `AGENT.md`
- `docs/context-orientation.md`

The minimum working structure depends on the product type, but it should include the real working folders early. A research repo should have research and data structure. An application repo should have source, tests, and runtime configuration. A design repo should have design assets and component rules.

If a new repo has policy docs but no concrete place to do the work, the setup is incomplete.
