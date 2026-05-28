# Repo Organization

A map of this repository. It describes what each folder is for, what lives inside it, and the order an agent (or a human) should consult things when picking the repo up cold. Pair this with `AGENT.md` at the root, which is the operational cold-start file. `AGENT.md` tells an agent *how* to enter the repo. This file tells it *where things are*.

This is `Documentation.md`. Not a project repo. It is the canonical library of `.md` files that get forked into projects to give AI agents a consistent set of standards across vendors (Claude, Codex, Gemini, GPT, Copilot, and so on). Treat the tree below as a stable contract. Renames propagate everywhere they are referenced in the same commit. New folders get an entry in this file and an entry in `AGENT.md` if they belong on the cold-start path.

---

## Top-level layout

```
Repository-md/
├── README.md                    # What this repo is, who it's for, what it does
├── AGENT.md                     # Cold-start file for any agent landing in the repo
├── CLAUDE.md                    # Claude-specific cold-start overlay (sits on top of AGENT.md)
├── LICENSE
├── docs/                        # Operational memory for this repo itself
│   ├── repo-organization.md     # ← this file. The map.
│   └── context-orientation.md   # Per-Knob change log. The Knob-by-Knob history.
├── behavior/                    # The rules an agent obeys. Cold-start required.
├── architecture/                # Framework-level memory + workflow protocols. Cold-start required.
├── skills/                      # Portable AI capabilities. Cross-vendor.
├── workflows/                   # DevOps and project lifecycle patterns.
└── design/                      # Project-specific UI/UX rules. Skip on cold start.
```

Five working folders plus `docs/`. The five folders are deliberate. They map to five different jobs an agent has to do, and they do not bleed into each other.

---

## docs/

Operational memory for *this* repository. Distinct from the `behavior/` rules, which describe how agents should think about context in *any* project they fork this into. `docs/` is the in-house version: the map of this repo, and the running log of Knobs as they get committed.

- `repo-organization.md` — this file. The folder map. Updates when a new top-level folder or canonical file spawns.
- `context-orientation.md` — the running per-Knob log. Each commit / bump / version push earns a one-to-two paragraph summary with date and timestamp. When the file exceeds 5000 characters, the rule is to spawn `context-ori-summary-2.md` and continue, then `-3.md`, `-4.md`, `-5.md` as the project grows. Cold storage for past Knobs. The current Knob and the last three stay hot in `context-orientation.md`.

The reason these live in `docs/` rather than at the root is to keep the root clean for the cold-start surface (README, AGENT, CLAUDE) and to give the project a consistent home for its own operational memory regardless of which vendor's agent is reading it.

---

## behavior/

The foundational rules. Everything an agent has to internalize before it touches the rest of the repo. Read this first on cold start, no matter what task is in front of you.

- `context-rules.md` — hard operational rules, behavioral constraints, retrieval policies. Also holds the working glossary of framework terminology (Knob, Bump, Entropy, Context Window, Drift, Bloat, Saturation, Wayfinding, Collapse, Decay). Foundational layer.
- `context-entropy.md` — the preservation view. How context survives across Knobs, agent handoffs, and human hiatus. Defines PLTRF, LTIP, STIP, and the hot/warm/cold tiering. Holds the worked examples (the v0.9.31 shader-engine recovery, the ui-refactor knob in Usage Menubar) that anchor the vocabulary.
- `context-window.md` (CWM) — the active memory view. Treats the context window as virtual RAM. Saturation, drift, compression, prioritization, trimming near limits, Token awareness.
- `context-token-limits.md` (CTL) — the Token economy view. Scoring requests on a 1–10 scale (Impact, Complexity, Relevance to current Knob), wayfinding, context optimization at runtime, conservation practices.
- `context-utility.md` — the index for this folder. Short pointers to what each doc covers. Update this when a new `context-NAME.md` doc spawns.
- `user-model.md` — the user view. How the agent reads, models, and adapts to the person on the other side of the prompt. Analyze User Behavior, Talk to the User, User Psychology. Sits alongside the four context-* docs as the human-facing layer.

Rules sets the foundation, entropy preserves across time, window manages the live session, token-limits prices the cost of pulling things back in, and user-model reads the person on the other side. Read them in that order on cold start. Re-read selectively when a Knob is in motion.

---

## architecture/

Framework-level memory + workflow protocols. Rides alongside `behavior/` rules — `behavior/` governs how the agent thinks inside a single session, `architecture/` governs how memory survives across multi-agent handoffs, branch merges, and long project hiatuses. Cold-start required when the task touches handoff discipline, multi-agent orchestration, or long-running memory.

- `memory.md` — the foundational memory rules layer. Hot/cold storage, memory layer examples table, memory failure states list, management best practices.
- `memory-drift.md` — Memory Drift (gradual loss of memory coherence over a project's lifecycle, distinct from mid-session Context Drift) + Memory Rot (stale files compounding into encroachment on active context). How to notice drift ahead of time, how to avoid Memory Rot.
- `memory-watchdog.md` — the Memory Watchdog 🐕. Gatekeeper for memory + context, auditor of standards, runner of sanitization. Adjustable aggression level. The shepherd that guards the gates.
- `workflow-tools.md` — Workflow Tools governance + CPP (Context Preservation Protocol) + Canonical AI Agent Profile + Frictionless Behavior Standards. How agents adapt across vendor IDEs without fragmenting.

The four docs cross-reference each other heavily. `workflow-tools.md` repeatedly invokes the Watchdog as the canonical decision-maker for memory archiving. `memory-drift.md` describes the failure mode the Watchdog defends against. Treat the folder as a tight cluster, not a list.

---

## skills/

Portable AI capabilities. Designed to be vendor-agnostic — the same Skill applies whether the agent is running on Claude, Codex, Gemini, GPT, or anything else.

- `skill-map.md` — the index for the folder. Currently a stub; gets fleshed out as skills accumulate.
- `repo-cognition/` — the first skill. Establishes operational rules and retrieval systems for AI-assisted repositories.
  - `SKILL.md` — the canonical Skill definition (with the YAML frontmatter Skills require).
  - `CLAUDE.md`, `CODEX.md`, `GEMINI.md` — vendor-specific overlays of the same Skill. Same content, different framing per vendor's conventions.
  - `references/` — the underlying reference docs the Skill points at: `context-entropy.md`, `context-rules.md`, `context-token-limits.md`, `context-window.md`. Mirrors of (or pointers to) the canonical docs in `behavior/`.

Pattern for adding a new skill: spawn a folder under `skills/`, drop in a `SKILL.md` with frontmatter, add vendor overlays as needed, point at references rather than re-defining the canonical concepts. Then update `skill-map.md`.

---

## workflows/

DevOps and project lifecycle patterns. Forkable, overridable per project. If a forked project disagrees with a workflow doc, defer to the fork.

- `project-setup.md` — the project initialization playbook. Project structure choices (React, Swift, Next.js, etc.), dependencies, backend services, branch naming, version tagging, license selection, README scaffolding, secret-handling rules. Includes the foundational rule that `.env` files never get committed without explicit user direction.
- `project-context.md` — context entropy and memory rules for project-level work. How agents should create and maintain `context-orientation.md` (or `project-context.md` — interchangeable) inside a forked project's `docs/` folder, how to handle Knobs, how to handle the 5000-character threshold, git push/pull rules for handoff, branch and worktree naming conventions, Token usage discipline at the project level.

Both docs are written for the project-fork case, not for `Documentation.md` itself. The `Documentation.md` repo follows the same rules but applies them to its own evolution as a documentation library.

---

## design/

Project-specific UI and visual rules. Skip on cold start unless the task is design or UI work. The rest of the repo does not depend on these files.

- `general-design-rules.md` — top-level design directives.
- `ui-ux.md` — UI/UX principles.
- `ui-ux-heuristics.md` — heuristics for evaluating UI/UX decisions.
- `components/` — per-component specs.
  - `component-model.md` — the component model itself.
  - `component-button.md` — button spec.
  - `component-nav-header.md` — nav header spec.

When a forked project does design work, these become the starting point. Override per project as needed.

---

## Cold-start order

For an agent landing in this repo for the first time:

1. `README.md` — what this repo is.
2. `AGENT.md` — how to enter it.
3. `CLAUDE.md` — vendor-specific overlay (if running on Claude).
4. `behavior/context-rules.md` → `context-entropy.md` → `context-window.md` → `context-token-limits.md` → `context-utility.md` → `user-model.md`.
5. `architecture/memory.md` → `memory-drift.md` → `memory-watchdog.md` → `workflow-tools.md`.
6. `docs/context-orientation.md` — what changed recently and why.
7. `skills/skill-map.md` and the relevant `SKILL.md` files under `skills/`.
8. `workflows/` — only if the task touches setup or context governance.
9. `design/` — only if the task is design work.

This file lives in `docs/` and is itself part of the cold-start map. When you add a folder or rename one, update this file in the same commit that does the rename. That is the PLTRF discipline applied to the map itself.

---

## Maintenance rules

- New top-level folder → add a section here, add a pointer in `AGENT.md`, commit in the same change.
- New canonical doc inside an existing folder → add a bullet under that folder's section.
- Rename → propagate to every reference in the same commit. No orphan references.
- This file gets re-audited every few Knobs. If a section describes something that no longer exists, fix it or remove it. Stale maps are worse than no map.
- Treat this as the structural source of truth for the repo layout. `AGENT.md` is the behavioral source of truth. `context-orientation.md` is the temporal source of truth. They do not duplicate each other.
