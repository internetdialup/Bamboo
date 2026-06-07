# Documentation.md — Context Orientation Summary 2

Cold storage for older Knobs moved out of `docs/memory-ctx/ctx-orientation.md` when the hot log approached the 5000-character threshold.

Read this only when the current Knob references older scaffolding, prior release history, or the origin of the repo map.

---

## Knob: PLTRF GitHub Action — safety net closes the sequence — Sunday, June 7, 2026, 03:45 AM CDT

Last one in the sequence. Shipped `.github/workflows/pltrf-check.yml`. Runs on every push and PR. Scans the cold-start cascade (`CLAUDE.md`, `AGENT.md`, `Documentation.md`, `README.md`, `docs/repo-organization.md`, and all `behavior/ctx-*.md`) and asserts every repo-relative file path mentioned actually exists on disk. If any reference is broken, the build fails with a clear annotation pointing at which source doc references which missing file.

The matching is deliberatly scoped to paths that start with a known top-level folder (`behavior/`, `architecture/`, `agent-architecture/`, `docs/`, `skills/`, `workflows/`, `design/`, `.github/`). Bare filenames in prose like "see SKILL.md", sequence patterns like `-3.md`, template placeholders like `ctx-NAME.md`, and external-fork examples like `Trading-MCP-Algo/CHANGELOG.md` all get ignored — resolving them needs context the check doesn't have. Intentional placeholders (downstream-fork defaults, Backlog files) live in a `SKIP_LIST` at the top of the action.

Tested locally against the current state of the repo and it passes clean. Zero broken pointers. Confirmed it would catch a fake broken reference during development by introducing one and watching it fail.

PLTRF was discipline-only until this Knob — every rename, every new file, every move depended on me or the agent being meticulous. Now it's discipline plus a safety net. Broken pointers get caught in CI instead of waiting for a fresh agent to stumble into them six weeks later. README and Documentation.md got short notes mentioning the check is automated.

This wraps the 5-Knob refinement sequence post-Vision Synthesis Report. Across the arc: agent-mms filled (1), mirror layer killed (2), workflows split + entropy metrics relocated + CPP own home (3), Watchdog persona doc + Skill upgrade (4), and now CI enforcement (5). Five Knobs, five concrete refinements. The repo is materially less drift-prone than it was at the start of yesterday.

---

## Knob: Watchdog persona + Skill upgrade — Sunday, June 7, 2026, 03:20 AM CDT

The Watchdog finally has a face. Pulled the character, voice, and aggression-level dial out of the three different places they were scatered across — `memory-watchdog.md`, `agent-topology.md`, `agent-identity.md` — and into a canonical `architecture/memory/watchdog-persona.md`. The persona doc is where the dial lives now. Project owners set the float (0.0–1.0), the Skill reads it on each pass. Default is 0.5. Bands defined in the persona doc for what passive vs standard vs strict vs paranoid actually mean operationally.

Rewrote `skills/memory-watchdog/SKILL.md` so it's actually runnable, not just a description of what the Watchdog should do. Added the Aggression Level section at the top — agents check the persona for the current project's float before they run a pass, then apply rule strictness accordingly. Existing operational content (the Watchdog Pass, the Map Hygiene rules, the search patterns) stays, but it's now persona-aware. Skill loads the persona first.

Cleaned up `memory-watchdog.md` so it stops restating the personality. It carries the concept now — what the Watchdog IS and what it does — and points at the persona doc for voice and the Skill for runtime. The "why does the Watchdog have to be a file" question got a canonical answer in the persona doc, so the concept doc just summarizes and points.

Added a Watchdog entry to `ctx-lexicon.md` pointing at all three homes (persona, concept, runtime). Updated `repo-organization.md` to add `watchdog-persona.md` to the architecture/memory tree and tie the three files together in their descriptions.

This is the biggest authoring move in the refinement sequence. Closes the design-without-implementation gap for the Watchdog — it's now actually a thing an agent can run, not just something the docs talk about.

---

## Knob: README tagline swap — Sunday, June 7, 2026, 03:00 AM CDT

Swapped the line under the README title. Old version read like a brochure — *Canonical documentation and agent-governance starter for AI-assisted repositories.* New version reads like me: *Your Multi-Agent Orchestrator for AI Governance in AI-assisted repos, and projects.* Same scope, different vibe. The README is the first thing a forker sees and the old line was doing it no favors.

---

## Knob: structural moves — workflows split + entropy metrics + CPP own home + voice directive — Sunday, June 7, 2026, 02:50 AM CDT

Three structural moves in one shot, plus a small standing rule tucked into CLAUDE.md. Workflows split got the sharpening it needed — `project-setup.md` is now explicitly first-time bootstrap, `project-context.md` is explicitly ongoing governance. Cross-refs at the top of each, and the "Agent Context Rules" section in project-context got refocused to assume the orientation file already exists. New forks land in setup; running projects land in context. No more guessing which doc applies when.

Computing Entropy math (retrieval entropy + corpus entropy, all the softmax stuff) moved out of `behavior/ctx-entropy.md` into a new `architecture/memory/memory-entropy-metrics.md`. Right content, correct home. ctx-entropy keeps the *definition* of entropy as a direction; the metrics doc carries the *measurement* the Watchdog actually acts on. Replaced the math block in ctx-entropy with a four-line pointer. Updated ctx-utility and repo-organization so the index reflects where the computation lives now.

CPP earned its own doc. It used to be a section inside `architecture/workflow-tools.md` — now it's `workflows/cpp.md` with explicit triggers (branch close, phase rollover, prod deploy), anti-patterns, and cross-refs to the Watchdog. Added CPP, MVS, and MMS entries to `behavior/ctx-lexicon.md` so the decoder ring stays current.

Also tucked a voice directive into CLAUDE.md under the ghost-writer bullet. Future Claude sessions get explicit guidance to sound like me, not a corporate changelog. Direct, light contractions, occasional sentence fragments to keep the output from reading too polished. Applies to commits, Knob entries, and author-voiced README sections only. Agent-facing rules content stays clean.

---

## Knob: killed the mirror layer in skills/repo-cognition/references/ — Sunday, June 7, 2026, 02:30 AM CDT

Replaced the four byte-near mirror files in `skills/repo-cognition/references/` (`ctx-rules.md`, `ctx-entropy.md`, `ctx-window.md`, `ctx-token-limits.md`) with seven-line SEE-ALSO pointer stubs. Each stub names what it used to be, points at the canonical home in `behavior/`, and explains why the mirror layer was Drift fuel in the first place. The pattern was the exact one `ctx-entropy.md` explicitly warns against — two files describing the same concept under different paths — and it had been quietly sitting inside `repo-cognition` since the Skill was first scaffolded.

Updated the Skill itself and all three vendor overlays in the same commit. `SKILL.md`, `CLAUDE.md`, `CODEX.md`, and `GEMINI.md` now name canonical paths under `behavior/` in their Load lists (including the new `ctx-lexicon.md` from the prior Knob) instead of the now-thin `references/` stubs. The `references/` directory stays in place so any older external link still resolves, but the Skill no longer asks agents to load from it. `docs/repo-organization.md` description of `references/` updated to reflect the new pointer-layer role.

---

## Knob: agent-mms filled + memory-adm Backlog section — Sunday, June 7, 2026, 02:15 AM CDT

First Knob in the post–Vision Synthesis refinement sequence. Filled `agent-architecture/agent-mms.md` with the Agent Memory Management System content: Memory Value Scores (0.0–1.0 scoring of artifacts against the active Knob), hot/warm/cold tiering at the per-agent level that feeds the same LTIP/CWM disciplines from `behavior/`, Watchdog interaction via the repo memory layer (agents stay sovereign over their own working memory until handoff), parallel-agent memory isolation rules that mirror the anti-conflict rules in `agent-topology.md`, and the three summarization triggers (Knob transition, compaction event, handoff). The file went from a 1-line placeholder to a full sibling of `agent-identity.md` and `agent-topology.md`.

Same Knob restructured `architecture/memory/memory-adm.md`. The "Planned, not yet written" references to `memory-context-preservation.md` and `memory-manifest.md` moved into a dedicated `# Backlog` section with one-line rationale each. They read as deliberate design intent now instead of broken pointers an agent might chase. Updated the pointer descriptions in `docs/repo-organization.md` (agent-mms.md is now a real doc, not a placeholder) and `agent-architecture/agent-identity.md` (the intro line that names the trio of agent-architecture docs now names MMS too).

---

## Knob: lived signal refinements — lexicon, format flex, narrate rule, README recipe — Sunday, June 7, 2026, 02:02 AM CDT

Applied the refinements from the Lived Signal Report in one atomic move. Created `behavior/ctx-lexicon.md` as the single canonical decoder ring for terminology (Knob, Bump, Entropy, Wayfinding, Decay, Drift, Bloat, Collapse, Saturation, Active Working Memory, Repository Memory, CTX) and operational acronyms (PLTRF, LTIP, STIP, CWM, CTL, ADM, RAG, CRUD). The glossary that used to live inside `ctx-rules.md` moved here in full — agents and humans now have one place to decode the vocabulary instead of mining it from prose. Cold-start order in `CLAUDE.md`, `AGENT.md`, and `docs/repo-organization.md` now points at the lexicon as item 5.

Loosened the Knob entry format in `ctx-rules.md`. The rigid `## Knob: Title — Date` template was the single biggest signal in the fork audit — every fork ignored it and grew its own shape. The Format section now lists three invariants (date, narrative, cross-refs) and five tested shape variants pulled from real forks: Knob block, semver release block, agent handoff signature, dated priority block, and guardrail/runbook entry. Forkers pick the shape that fits their project; stay consistent inside one log to avoid drift.

Demoted `architecture/` and `agent-architecture/` to explicit advanced add-on status across the cold-start cascade (`CLAUDE.md`, `AGENT.md`, `Documentation.md`, `docs/repo-organization.md`). The audit showed zero of seven downstream forks adopted either folder. Single-agent projects and projects without an ADM/RAG memory layer skip both on cold start. Folders stay in place physically; only the gating language sharpened.

Added a vendor-neutral **narrate-compression directive** as section 8 of `AGENT.md`, with a mirroring bullet in `CLAUDE.md`. Auto-compaction has been silent by default; the new rule says when an agent compresses (or detects imminent compression), it states which orientation log it will re-read and what active Knob it will reconstitute from. Closes the Phase C invisibility gap from the Lived Signal audit — the user reported Claude saying the log helped during compaction, but the transcripts came up empty because Claude never said so out loud.

Strengthened the **Commit attribution** bullet in `CLAUDE.md` with the rationale: contributors on GitHub are publicly visible, and seeing Claude in the list credit-shifts the work away from the user. Treat the user as the visible author; Claude is the ghost-writer and publisher, not the credited contributor. The rule already existed from the prior Knob; this Bump just locks in the *why*.

Added a **Fork in 5 Minutes** section to the top of `README.md`, ghost-written in a warmer voice per user direction. Replaces the previous "How To Adopt It" section. Walks a forker through what to copy, what to skip, the two edits to make, and the one rule that survives every fork (every Bump earns a dated entry). Closes the productization gap surfaced in the honest assessment — forks were standardless because the recipe wasn't written down.

Two orphan pointers from the prior `memory-context/` → `memory-ctx/` rename were also fixed in `docs/repo-organization.md` (the tree diagram and the docs/ section). PLTRF discipline pass. No `Co-Authored-By: Claude` trailer.

---

## Knob: ctx- rename + CTX acronym + ghost-writer policy — Saturday, June 6, 2026, 06:27 PM CDT

Refactored the `context-` filename prefix to `ctx-` across the repo and renamed the `docs/memory-context/` folder to `docs/memory-ctx/`. Twelve files moved via `git mv` (six in `behavior/`, two in `docs/memory-ctx/`, four in `skills/repo-cognition/references/`) plus the folder itself. Path and identifier references in every doc inside the Documentation.md radius — CLAUDE.md, AGENT.md, README.md, Documentation.md, docs/repo-organization.md, the skill files, the workflow docs, and the architecture/memory docs — were updated in lockstep so no orphan pointers were left behind. The standalone word "context" in prose was preserved per the user's rule; only doc-name references and folder paths flipped.

Introduced CTX as a canonical acronym. Definition lives in the glossary inside `behavior/ctx-rules.md` alongside Knob, Bump, Entropy, and the other foundational terms. A one-sentence gloss was added to the cold-start sections of both `CLAUDE.md` and `AGENT.md` so a fresh agent encounters the acronym before relying on it. The rename is the kind of move `behavior/ctx-entropy.md` explicitly warns against — Drift starts when renames stack without their references — so all of it landed in a single atomic commit under PLTRF discipline.

Same Knob also added a **Ghost-writer for commits and Knob entries** bullet to `CLAUDE.md`. The user writes commit drafts and Bump entries in rambling first-person voice; Claude reshapes them into the per-Bump format while preserving voice and intent, killing filler, and never adding scope or inventing rationale. Codifying it in `CLAUDE.md` means future Claude sessions inherit the role without being re-briefed.

---

## Knob: commit attribution policy + history scrub — Saturday, June 6, 2026, 05:49 PM CDT

Added an explicit **Commit attribution** directive to `CLAUDE.md` under "Claude-shaped operating notes": no `Co-Authored-By: Claude` (or any Anthropic-noreply) trailers on commits in this repo. The rule overrides the system-default trailer injection and covers amend, rebase, squash, and all future commits. Scope is Claude-only by user preference; `AGENT.md` and the other vendor overlays were intentionally left alone.

History scrub paired with the policy: the trailer existed on exactly one commit, `67ba545` (docs: add user-model.md + LTRP retirement + architecture/ cold-start integration, May 28). That commit was not on `main` — it was the tip of an unmerged exploratory branch `knob/memory-split-ltip-canonical` carrying 352 lines of un-merged content (user-model.md, memory-drift.md, memory-watchdog.md, workflow-tools.md, and supporting edits). Ran `git filter-branch --msg-filter` on that branch only, stripped the trailer, force-pushed back to origin. New SHA `3a8d7bd` replaces `67ba545`. Branch and its content preserved; trailer gone. Two surfaces — the historical artifact and the forward-looking rule — closed in the same Knob.

---

## Knob: memory-context normalization + agent topology — Thursday, June 4, 2026, 04:44 AM CDT

Normalized this repo's internal memory path to `docs/memory-ctx/` and propagated the rename through the cold-start docs, canonical maps, and memory Skills. `README.md`, `AGENT.md`, `Documentation.md`, `CLAUDE.md`, `docs/repo-organization.md`, and the relevant workflow and Skill docs now distinguish between this repo's internal memory layout and the default downstream template contract, which still points project forks at `docs/ctx-orientation.md` unless they intentionally adopt the same folder structure.

Added `agent-architecture/agent-topology.md` as the source of truth for multi-agent squad structure. The new doc defines a practical startup tech-squad topology with core lanes, optional lanes, ownership boundaries, handoff expectations, escalation rules, and anti-conflict rules for parallel work. Also added a light cross-reference in `agent-identity.md` so identity stays about persona while topology owns coordination.

---

## Knob: canonical Documentation root + thinner fork contract — Wednesday, June 3, 2026, 09:18 PM CDT

Added a literal root `Documentation.md` and made it the canonical operating spec for this repository pattern. `README.md` now stays human-facing, `AGENT.md` is reduced to cold-start routing, and generic policy was pulled out of `workflows/project-setup.md` so setup procedure no longer competes with the source of truth.

This also tightened the fork contract. Downstream repos are expected to carry the minimum governance layer, copy only the modules they actively need, and add real working folders early so the repo does not become mostly process docs. Updated `docs/repo-organization.md` to reflect the new root file and cold-start order.

---

## Knob: memory Skills + map hygiene — Thursday, May 28, 2026, 07:52 PM CDT

Added two separate Skills instead of bloating `repo-cognition`: `memory-context` for Knob-aware retrieval, ADM/RAG alignment, hot/warm/cold memory, and handoffs; `memory-watchdog` for stale maps, broken references, missing Knob entries, duplicate concepts, and memory rot. Updated `skills/skill-map.md` so Skills are now mapped instead of living behind a stub.

Added Map Hygiene rules to `docs/repo-organization.md`. New folders, moved files, new Skills, and new architecture memory docs now have explicit map-update expectations. This is the OSS governance edge of the repo: if the map lies, the memory system rots.

---

## Knob: ADM/RAG memory folder — Thursday, May 28, 2026

Moved the memory architecture docs into `architecture/memory/` so Memory, Drift, Watchdog, ADM, RAG, and CRUD live in one place instead of scattering across the top of `architecture/`. `workflow-tools.md` stays directly under `architecture/` because it is about tool friction and workflow surfaces, not the memory store itself.

Added the first pass of ADM, RAG, and CRUD memory docs. ADM carries episodic chapters and active memory banks. RAG carries semantic and procedural memory. CRUD is the keep-it-alive loop so stale memory gets created, read, updated, or destroyed instead of quietly rotting.

---

## Knob: architecture map + PLTRF cleanup — Thursday, May 28, 2026, 06:53 PM CDT

Added `architecture/` to the repo's cold-start map as the fifth working folder. It now shows up in `README.md`, `AGENT.md`, `CLAUDE.md`, and `docs/repo-organization.md`, but it is selective cold-start material. Agents load it when memory itself is the work: drift, Watchdog, audits, workflow governance, or memory architecture. Otherwise it stays cold so the Token budget does not get eaten just because a folder exists.

Cleaned up early PLTRF drift before it became normal. Fixed the broken `references/ctx-token-limits.md` pointers, corrected the long-term preservation acronym split, synced the repo-cognition reference mirrors back to canonical `behavior/`, and turned the Codex/Claude/Gemini overlays into thin wrappers around `SKILL.md`. Same hooks, fewer duplicated rules, less chance the repo becomes the thing the agent fights.

---

## Knob: docs scaffolding + CLAUDE overlay — Friday, May 22, 2026

Created `docs/repo-organization.md` as the structural map of the four-folder layout (`behavior/`, `skills/`, `workflows/`, `design/`) plus `docs/` for this repo's own operational memory. The file describes what each folder is for, what lives inside it, and the cold-start consultation order. It is meant to be the structural source of truth for the repo while `AGENT.md` remains the behavioral source of truth and `ctx-orientation.md` remains the temporal source of truth. The three do not duplicate each other.

Replaced the empty root `CLAUDE.md` with a Claude-specific cold-start overlay that sits on top of `AGENT.md`. It walks through the cold-start order Claude should follow, calls out the Skills format used in `skills/`, and codifies the user's standing preferences: every Bump gets a one-to-two paragraph summary in the repo's active context log, and overflow past 5000 characters spawns `ctx-ori-summary-2.md` onward. Also initialized `ctx-orientation.md` as part of the same Knob, since the directive required it to exist for future Bumps to log against.

---

## Prior history

Entries before this Knob live in commit history. Notable prior Bumps:

- **5.16.26** — Added and rewrote Context documents, Updated Skills folder, created `AGENT.md`. The behavior/ docs and the cold-start file were established at this point.
- **5.11.26** — Initial release of `Documentation.md`. Repo scaffolding and intent set.

These are recorded here for traceability but were not logged Knob-by-Knob at the time.
