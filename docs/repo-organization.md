# Repo Organization

A map of this repository. It describes what each folder is for, what lives inside it, and the order an agent (or a human) should consult things when picking the repo up cold. Pair this with `AGENT.md` at the root, which is the operational cold-start file. `AGENT.md` tells an agent *how* to enter the repo. This file tells it *where things are*.

This is `Documentation.md`. Not a project repo. It is the canonical library of `.md` files that get forked into projects to give AI agents a consistent set of standards across vendors (Claude, Codex, Gemini, GPT, Copilot, and so on). `Documentation.md` at the repo root is the policy source. `README.md` is the human overview. `AGENT.md` is the cold-start router. Treat the tree below as a stable contract. Renames propagate everywhere they are referenced in the same commit. New folders get an entry in this file and an entry in `AGENT.md` if they belong on the cold-start path.

---

## Top-level layout

```
Repository-md/
├── Documentation.md            # Canonical operating spec for repos using this system
├── README.md                    # What this repo is, who it's for, what it does
├── AGENT.md                     # Cold-start router for any agent landing in the repo
├── CLAUDE.md                    # Claude-specific cold-start overlay (sits on top of AGENT.md)
├── LICENSE
├── agent-architecture/          # ADVANCED ADD-ON. Multi-agent role design and orchestration. Skip unless multi-agent.
│   ├── agent-identity.md
│   ├── agent-topology.md
│   └── agent-mms.md
├── docs/                        # Operational memory for this repo itself
│   ├── repo-organization.md     # ← this file. The map.
│   └── memory-ctx/
│       ├── ctx-orientation.md   # Hot per-Knob change log.
│       └── ctx-ori-summary-2.md # Cold storage for older Knobs.
├── behavior/                    # The rules an agent obeys. Cold-start required.
├── architecture/                # ADVANCED ADD-ON. ADM/RAG, Watchdog, workflow tools. Skip unless memory-system work.
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

Six working folders plus `docs/`. The folders are deliberate. They map to different jobs an agent has to do, and they do not bleed into each other. Downstream repos should copy only the folders they actually need.

---

## docs/

Operational memory for *this* repository. Distinct from the `behavior/` rules, which describe how agents should think about context in *any* project they fork this into. `docs/` is the in-house version: the map of this repo, and the running log of Knobs as they get committed.

- `repo-organization.md` — this file. The folder map. Updates when a new top-level folder or canonical file spawns.
- `memory-ctx/` — this repo's internal memory log folder.
  - `ctx-orientation.md` — the running per-Knob log. Each commit / bump / version push earns a one-to-two paragraph summary with date and timestamp. When the file exceeds 5000 characters, the rule is to spawn `ctx-ori-summary-2.md` and continue, then `-3.md`, `-4.md`, `-5.md` as the project grows. The hot file stays current and lean.
  - `ctx-ori-summary-2.md` — cold storage for older Knobs rolled out of `ctx-orientation.md`.

The reason these live in `docs/` rather than at the root is to keep the root clean for the cold-start surface (`Documentation.md`, `README.md`, `AGENT.md`, `CLAUDE.md`) and to give the project a consistent home for its own operational memory regardless of which vendor's agent is reading it. This repo uses `docs/memory-ctx/` internally because the repository itself is documenting memory systems; downstream repos still default to `docs/ctx-orientation.md` unless they intentionally adopt the same layout.

---

## agent-architecture/ — advanced add-on

Multi-agent operating model docs. **Skip on cold-start unless the project has a multi-agent topology with handoff or orchestration boundaries.** Single-agent projects do not need this folder. Pull it when the task is explicitly about agent roles, identity, orchestration, handoffs, or parallel work boundaries.

- `agent-identity.md` — how an agent adopts a role-shaped working identity.
- `agent-topology.md` — the coordination model for a practical startup tech squad: role lanes, ownership, handoffs, escalation, and anti-conflict rules.
- `agent-mms.md` — the Agent Memory Management System. How each agent scores its own working memory (Memory Value Scores), how MVS feeds hot/warm/cold tiering at the per-agent level, how the Watchdog interacts via the repo memory layer, parallel-agent memory isolation rules, and the three summarization triggers (Knob transition, compaction event, handoff).

---

## behavior/

The foundational rules. Everything an agent has to internalize before it touches the rest of the repo. Read this first on cold start, no matter what task is in front of you.

- `ctx-rules.md` — hard operational rules, behavioral constraints, retrieval policies. Holds the canonical Format section that describes the five Bump-entry shape variants (Knob block, semver release, agent handoff, dated priority, guardrail/runbook). Foundational layer.
- `ctx-lexicon.md` — the decoder ring. Single canonical home for framework terminology (Knob, Bump, Entropy, Wayfinding, Decay, Drift, Bloat, Collapse, Saturation, Context Window, Active Working Memory, Repository Memory, CTX) and operational acronyms (PLTRF, LTIP, STIP, CWM, CTL, ADM, RAG, CRUD). Load it when you encounter a term you don't recognize.
- `ctx-entropy.md` — the preservation view. How context survives across Knobs, agent handoffs, and human hiatus. Defines PLTRF, LTIP, STIP, and the hot/warm/cold tiering. Holds the worked examples (the v0.9.31 shader-engine recovery, the ui-refactor knob in Usage Menubar) that anchor the vocabulary.
- `ctx-window.md` (CWM) — the active memory view. Treats the context window as virtual RAM. Saturation, drift, compression, prioritization, trimming near limits, Token awareness.
- `ctx-token-limits.md` (CTL) — the Token economy view. Scoring requests on a 1–10 scale (Impact, Complexity, Relevance to current Knob), wayfinding, context optimization at runtime, conservation practices.
- `ctx-utility.md` — the index for this folder. Short pointers to what each doc covers. Update this when a new `ctx-NAME.md` doc spawns.

These five docs share vocabulary on purpose. Rules sets the foundation, lexicon decodes the language, entropy preserves across time, window manages the live session, and token-limits prices the cost of pulling things back in. Read them in that order on cold start. Re-read selectively when a Knob is in motion.

---

## architecture/ — advanced add-on

The memory architecture layer. This is where the repo talks about Memory, ADM, RAG, CRUD, Drift, Watchdog, and Workflow Tools as systems instead of one-off rules. **Skip on cold-start unless the project explicitly has an ADM/RAG memory layer or the current work is auditing memory governance.** Most projects do not need this folder. Pull it when the work is memory governance, context audits, drift prevention, ADM/RAG retrieval, Watchdog behavior, or workflow-tool alignment.

- `workflow-tools.md` — how IDEs, CLIs, desktop apps, browsers, APIs, and sandboxes affect memory debt and project drift.
- `memory/` — the memory operating layer. This is the home for the memory docs, not the top level of `architecture/`.
  - `memory.md` — the broad memory standard. Hot/cold memory, STIP and LTIP, handoffs, failure states, and the memory layer table.
  - `memory-adm.md` — Active Dreaming Memory. Episodic memory chapters, offline refresh, and how ADM works with RAG and the Watchdog.
  - `memory-rag.md` — RAG as semantic and procedural memory. Retrieval that supports ADM and the Watchdog without pretending it is the whole memory system.
  - `memory-crud.md` — the Create, Read, Update, Delete/Destroy rule for keeping memory files alive and not stale.
  - `memory-drift.md` — how memory drifts, rots, repeats itself, and starts to make the repo harder to navigate.
  - `memory-watchdog.md` — the Watchdog concept. A file-level auditor for memory standards, secret awareness, context decay, and repository hygiene.
  - `memory-entropy-metrics.md` — measurement architecture for Context Entropy. Retrieval Entropy (softmax over top-k candidates) and Corpus Entropy (near-duplicate fraction). The number that triggers the compression sweep instead of acting on a feeling.

This folder is selective cold-start material. If the task is normal repo navigation, `behavior/` is enough. If the task is about the memory system itself, this folder comes warm.

---

## skills/

Portable AI capabilities. Designed to be vendor-agnostic — the same Skill applies whether the agent is running on Claude, Codex, Gemini, GPT, or anything else.

- `skill-map.md` — the index for the folder. Quick map, not a giant catalog.
- `repo-cognition/` — the base repo cognition Skill. Establishes operational rules and retrieval systems for AI-assisted repositories.
  - `SKILL.md` — the canonical Skill definition (with the YAML frontmatter Skills require).
  - `CLAUDE.md`, `CODEX.md`, `GEMINI.md` — thin vendor overlays. They point at `SKILL.md` instead of copying the full rule body.
  - `references/` — thin pointer stubs (`ctx-entropy.md`, `ctx-rules.md`, `ctx-token-limits.md`, `ctx-window.md`) that each point at the canonical `behavior/ctx-*.md`. The Skill and its vendor overlays now load canonical paths directly; these stubs stay so any older link still resolves. Used to be byte-near mirrors — that was Drift fuel and got cleaned up.
- `memory-context/` — the memory retrieval and handoff Skill. Use it for ADM/RAG alignment, Knob-aware loading, hot/warm/cold memory, and project state reconstruction.
- `memory-watchdog/` — the memory hygiene Skill. Use it for stale maps, broken references, missing Knob logs, duplicated concepts, old paths, and drift audits.

Pattern for adding a new skill: spawn a folder under `skills/`, drop in a `SKILL.md` with frontmatter, add vendor overlays as needed, point at references rather than re-defining the canonical concepts. Then update `skill-map.md`.

---

## workflows/

DevOps and project lifecycle patterns. Forkable, overridable per project. If a forked project disagrees with a workflow doc, defer to the fork.

- `project-setup.md` — **first-time** project initialization procedure. How to apply the `Documentation.md` contract in a new repo without redefining the policy. 8-step bootstrap.
- `project-context.md` — **ongoing** context governance once the repo is running. The 5000-char threshold, the 20-document threshold, Git push/pull rules for handoff, branch and worktree naming, Token discipline at the project level. Setup-only content lives in `project-setup.md`; ongoing-only content lives here.
- `cpp.md` — Context Preservation Protocol. The workflow that keeps project memory alive across the big transitions — branch closes, phase rollovers, production deploys. Triggers, anti-patterns, archiving standards. Used to live as a section inside `architecture/workflow-tools.md`; got its own home when the named concept earned it.

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

1. `README.md` — what this repo is and how to adopt it.
2. `AGENT.md` — how to enter it.
3. `Documentation.md` — the policy source.
4. `docs/memory-ctx/ctx-orientation.md` — what changed recently and why in this repo.
5. `CLAUDE.md` — vendor-specific overlay (if running on Claude).
6. `behavior/ctx-rules.md` → `ctx-lexicon.md` → `ctx-entropy.md` → `ctx-window.md` → `ctx-token-limits.md` → `ctx-utility.md`.
7. `architecture/` — **advanced add-on.** Skip unless the project has an ADM/RAG memory layer or the task is auditing memory governance.
8. `agent-architecture/` — **advanced add-on.** Skip unless the project has a multi-agent topology.
9. `skills/skill-map.md` and the relevant `SKILL.md` files under `skills/`.
10. `workflows/` — only if the task touches setup or context governance.
11. `design/` — only if the task is design work.

This file lives in `docs/` and is itself part of the cold-start map. When you add a folder or rename one, update this file in the same commit that does the rename. That is the PLTRF discipline applied to the map itself.

---

## Maintenance rules

- New top-level folder → add a section here, add a pointer in `AGENT.md`, commit in the same change.
- New canonical doc inside an existing folder → add a bullet under that folder's section.
- Rename → propagate to every reference in the same commit. No orphan references.
- This file gets re-audited every few Knobs. If a section describes something that no longer exists, fix it or remove it. Stale maps are worse than no map.
- Treat this as the structural source of truth for the repo layout. `AGENT.md` is the behavioral source of truth. `docs/memory-ctx/ctx-orientation.md` is the temporal source of truth for this repo. They do not duplicate each other.

## Map Hygiene

This is the ruthless part. If the repo is going to be useful as OSS governance, the maps have to stay boringly accurate.

- New folder or moved file gets map updates in the same change.
- New Skill gets `skills/skill-map.md` and `docs/repo-organization.md` updates.
- New architecture memory doc gets this map and the relevant Skill pointer updated.
- Every Bump that changes repo structure gets a `docs/memory-ctx/ctx-orientation.md` entry in this repo, or a `docs/ctx-orientation.md` entry in downstream repos unless they intentionally use a memory-context folder.
- Run stale-reference scans before finishing. Broken references are memory rot.
