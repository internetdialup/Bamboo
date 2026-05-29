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
│   ├── context-orientation.md   # Hot per-Knob change log.
│   └── context-ori-summary-2.md # Cold storage for older Knobs.
├── behavior/                    # The rules an agent obeys. Cold-start required.
├── architecture/                # Memory architecture, ADM/RAG, Watchdog, workflow tools.
│   ├── workflow-tools.md        # Tool/workflow memory friction.
│   └── memory/                  # Memory operating layer.
│       ├── memory.md
│       ├── memory-adm.md
│       ├── memory-rag.md
│       ├── memory-crud.md
│       ├── memory-drift.md
│       └── memory-watchdog.md
├── skills/                      # Portable AI capabilities. Cross-vendor.
│   ├── skill-map.md
│   ├── repo-cognition/
│   ├── memory-context/
│   └── memory-watchdog/
├── workflows/                   # DevOps and project lifecycle patterns.
└── design/                      # Project-specific UI/UX rules. Skip on cold start.
```

Five working folders plus `docs/`. The five folders are deliberate. They map to different jobs an agent has to do, and they do not bleed into each other.

---

## docs/

Operational memory for *this* repository. Distinct from the `behavior/` rules, which describe how agents should think about context in *any* project they fork this into. `docs/` is the in-house version: the map of this repo, and the running log of Knobs as they get committed.

- `repo-organization.md` — this file. The folder map. Updates when a new top-level folder or canonical file spawns.
- `context-orientation.md` — the running per-Knob log. Each commit / bump / version push earns a one-to-two paragraph summary with date and timestamp. When the file exceeds 5000 characters, the rule is to spawn `context-ori-summary-2.md` and continue, then `-3.md`, `-4.md`, `-5.md` as the project grows. The hot file stays current and lean.
- `context-ori-summary-2.md` — cold storage for older Knobs rolled out of `context-orientation.md`.

The reason these live in `docs/` rather than at the root is to keep the root clean for the cold-start surface (README, AGENT, CLAUDE) and to give the project a consistent home for its own operational memory regardless of which vendor's agent is reading it.

---

## behavior/

The foundational rules. Everything an agent has to internalize before it touches the rest of the repo. Read this first on cold start, no matter what task is in front of you.

- `context-rules.md` — hard operational rules, behavioral constraints, retrieval policies. Also holds the working glossary of framework terminology (Knob, Bump, Entropy, Context Window, Drift, Bloat, Saturation, Wayfinding, Collapse, Decay). Foundational layer.
- `context-entropy.md` — the preservation view. How context survives across Knobs, agent handoffs, and human hiatus. Defines PLTRF, LTIP, STIP, and the hot/warm/cold tiering. Holds the worked examples (the v0.9.31 shader-engine recovery, the ui-refactor knob in Usage Menubar) that anchor the vocabulary.
- `context-window.md` (CWM) — the active memory view. Treats the context window as virtual RAM. Saturation, drift, compression, prioritization, trimming near limits, Token awareness.
- `context-token-limits.md` (CTL) — the Token economy view. Scoring requests on a 1–10 scale (Impact, Complexity, Relevance to current Knob), wayfinding, context optimization at runtime, conservation practices.
- `context-utility.md` — the index for this folder. Short pointers to what each doc covers. Update this when a new `context-NAME.md` doc spawns.

These four docs share vocabulary on purpose. Rules sets the foundation, entropy preserves across time, window manages the live session, and token-limits prices the cost of pulling things back in. Read them in that order on cold start. Re-read selectively when a Knob is in motion.

---

## architecture/

The memory architecture layer. This is where the repo talks about Memory, ADM, RAG, CRUD, Drift, Watchdog, and Workflow Tools as systems instead of one-off rules. Do not ingest this whole folder on ordinary cold start. Pull it when the work is memory governance, context audits, drift prevention, ADM/RAG retrieval, Watchdog behavior, or workflow-tool alignment.

- `workflow-tools.md` — how IDEs, CLIs, desktop apps, browsers, APIs, and sandboxes affect memory debt and project drift.
- `memory/` — the memory operating layer. This is the home for the memory docs, not the top level of `architecture/`.
  - `memory.md` — the broad memory standard. Hot/cold memory, STIP and LTIP, handoffs, failure states, and the memory layer table.
  - `memory-adm.md` — Active Dreaming Memory. Episodic memory chapters, offline refresh, and how ADM works with RAG and the Watchdog.
  - `memory-rag.md` — RAG as semantic and procedural memory. Retrieval that supports ADM and the Watchdog without pretending it is the whole memory system.
  - `memory-crud.md` — the Create, Read, Update, Delete/Destroy rule for keeping memory files alive and not stale.
  - `memory-drift.md` — how memory drifts, rots, repeats itself, and starts to make the repo harder to navigate.
  - `memory-watchdog.md` — the Watchdog concept. A file-level auditor for memory standards, secret awareness, context decay, and repository hygiene.

This folder is selective cold-start material. If the task is normal repo navigation, `behavior/` is enough. If the task is about the memory system itself, this folder comes warm.

---

## skills/

Portable AI capabilities. Designed to be vendor-agnostic — the same Skill applies whether the agent is running on Claude, Codex, Gemini, GPT, or anything else.

- `skill-map.md` — the index for the folder. Quick map, not a giant catalog.
- `repo-cognition/` — the base repo cognition Skill. Establishes operational rules and retrieval systems for AI-assisted repositories.
  - `SKILL.md` — the canonical Skill definition (with the YAML frontmatter Skills require).
  - `CLAUDE.md`, `CODEX.md`, `GEMINI.md` — thin vendor overlays. They point at `SKILL.md` instead of copying the full rule body.
  - `references/` — the underlying reference docs the Skill points at: `context-entropy.md`, `context-rules.md`, `context-token-limits.md`, `context-window.md`. Mirrors of (or pointers to) the canonical docs in `behavior/`.
- `memory-context/` — the memory retrieval and handoff Skill. Use it for ADM/RAG alignment, Knob-aware loading, hot/warm/cold memory, and project state reconstruction.
- `memory-watchdog/` — the memory hygiene Skill. Use it for stale maps, broken references, missing Knob logs, duplicated concepts, old paths, and drift audits.

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
4. `behavior/context-rules.md` → `context-entropy.md` → `context-window.md` → `context-token-limits.md` → `context-utility.md`.
5. `architecture/` — only if the task touches memory architecture, ADM, RAG, drift, Watchdog, audits, or workflow governance.
6. `skills/skill-map.md` and the relevant `SKILL.md` files under `skills/`.
7. `docs/context-orientation.md` — what changed recently and why.
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

## Map Hygiene

This is the ruthless part. If the repo is going to be useful as OSS governance, the maps have to stay boringly accurate.

- New folder or moved file gets map updates in the same change.
- New Skill gets `skills/skill-map.md` and `docs/repo-organization.md` updates.
- New architecture memory doc gets this map and the relevant Skill pointer updated.
- Every Bump that changes repo structure gets a `docs/context-orientation.md` entry.
- Run stale-reference scans before finishing. Broken references are memory rot.
