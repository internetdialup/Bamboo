# Bamboo

The canonical operating spec for AI-assisted repositories. This file (`Bamboo.md` at the repo root) carries the policy layer; the brand is **Bamboo**.

Use this file as the cross-project policy layer. It defines the minimum repo contract, document roles, mandatory rules, optional modules, anti-bloat guardrails, and the forking model. `README.md` explains a repo to humans. `AGENT.md` is the cold-start router for agents. In downstream repos, `docs/ctx-orientation.md` is the default running state log. In this canonical source repo, the internal running state log lives under `docs/memory-ctx/ctx-orientation.md`.

## 1. Purpose and Scope

`Bamboo.md` exists to give projects a stable operating system for AI and human collaboration across vendors. It is not a product README and it is not a task workflow. It is the durable policy layer that should change slowly and apply broadly.

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
- `docs/ctx-orientation.md` for the active state log

Only include the folders the repo actually needs. Common modules are:

- `behavior/` for reasoning and context rules
- `workflows/` for repeatable procedures
- `skills/` for reusable agent capabilities
- `architecture/` for memory or systems architecture
- `agent-architecture/` for multi-agent role and orchestration guidance
- `design/` for UI and visual rules

If a folder is not serving the repo, do not create it just to match a template.

## 3. Document Roles

- `Bamboo.md`: canonical operating policy for the repo or template it lives in
- `README.md`: human-facing project overview and adoption guide
- `AGENT.md`: short agent entrypoint that says what to read and in what order
- `docs/ctx-orientation.md`: newest-first log of meaningful repo state changes
- `behavior/`: durable reasoning rules and shared vocabulary
- `workflows/`: step-by-step procedures that implement policy without redefining it
- `skills/`: reusable capabilities, with pointers back to canonical docs instead of duplicated rule bodies
- `architecture/`: systems-level design, especially memory and governance architecture
- `agent-architecture/`: multi-agent role, identity, and orchestration design
- `design/`: project-specific UI, UX, and visual rules

The roles do not overlap. If two docs try to be authoritative for the same rule, collapse them into one source and point to it from everywhere else.

This source repo uses `docs/memory-ctx/` for its own operational memory because the repository itself is documenting memory systems. That does not change the default downstream contract unless a fork intentionally adopts the same layout.

## 4. Mandatory Rules

- Read `AGENT.md` first on agent cold start, then follow its loading order.
- Keep canonical rules in one authoritative place. Prefer pointers over mirrors.
- Update `docs/ctx-orientation.md` after meaningful repo state changes, not for trivial noise.
- **Anti-Sycophancy Mandate**: Agents are strictly forbidden from "Blind Agreement." Every operator assumption must be audited with mathematical or structural verification before execution. Explicitly combat LLM degradation; if a logic path is flawed, push back.
- **The 40/40/20 Protocol**: All complex reporting must adhere to the 40/40/20 split: 40% Data Payload, 40% Analytical Reasoning, 20% Strict Formatting. This prevents hallucinations and ensures TUI/API stability.
- **L1 Cache (ACTIVE_STATE.md)**: Use a `.gitignore` d volatile scratchpad to store intra-knob micro-tasks and surviving session "respawns."
- Never store secrets, API keys, tokens, or `.env` contents in docs, examples, or summaries.
- Do not commit `.env` files unless the user explicitly instructs it.
- Keep repo-specific implementation guidance local to that repo. Do not push local conventions back into the canonical base unless they are truly reusable.
- When folders or canonical files move, update every reference in the same change.
- When a new reusable Skill or module appears, update the relevant maps in the same change.
- Map hygiene is enforced automatically. The `.github/workflows/pltrf-check.yml` action scans the cold-start cascade (`CLAUDE.md`, `AGENT.md`, this file, `README.md`, `docs/repo-organization.md`, and the `behavior/ctx-*.md` family) on every push and PR and fails the build if any referenced file is missing from disk. Intentional placeholders go in the action's `SKIP_LIST`.

## 5. Optional Modules

These modules are opt-in. They are not default cold-start requirements unless the repo depends on them.

- `architecture/`: **advanced add-on.** Only when the project explicitly has an ADM/RAG memory layer, or the work itself is auditing memory governance, drift, or Watchdog behavior. Most projects do not need this folder. Lived signal: zero of seven downstream forks adopted it.
- `agent-architecture/`: **advanced add-on.** Only when the project has a multi-agent topology with handoff or orchestration boundaries. Single-agent projects do not need this folder. Lived signal: zero of seven downstream forks adopted it.
- `design/`: only when the repo owns UI, UX, or visual standards
- heavy workflow packs: only when the repo repeatedly performs those procedures
- `skills/`: only when the repo contains reusable capabilities worth carrying across projects

Optional modules should be documented as optional in both `README.md` and `AGENT.md`. Advanced add-ons should be skipped on cold start unless the task explicitly demands them.

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

1. Copy the minimum contract: `README.md`, `AGENT.md`, `docs/ctx-orientation.md`, and only the folders the project needs.
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
- `docs/ctx-orientation.md`
- `ACTIVE_STATE.md` (Volatile L1 Cache - .gitignore d)

The minimum working structure depends on the product type, but it should include the real working folders early. A research repo should have research and data structure. An application repo should have source, tests, and runtime configuration. A design repo should have design assets and component rules.

If a new repo has policy docs but no concrete place to do the work, the setup is incomplete.
