# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `ctx-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

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

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
