# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `context-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: ADM/RAG memory folder — Thursday, May 28, 2026

Moved the memory architecture docs into `architecture/memory/` so Memory, Drift, Watchdog, ADM, RAG, and CRUD live in one place instead of scattering across the top of `architecture/`. `workflow-tools.md` stays directly under `architecture/` because it is about tool friction and workflow surfaces, not the memory store itself.

Added the first pass of ADM, RAG, and CRUD memory docs. ADM carries episodic chapters and active memory banks. RAG carries semantic and procedural memory. CRUD is the keep-it-alive loop so stale memory gets created, read, updated, or destroyed instead of quietly rotting.

---

## Knob: architecture map + PLTRF cleanup — Thursday, May 28, 2026, 06:53 PM CDT

Added `architecture/` to the repo's cold-start map as the fifth working folder. It now shows up in `README.md`, `AGENT.md`, `CLAUDE.md`, and `docs/repo-organization.md`, but it is selective cold-start material. Agents load it when memory itself is the work: drift, Watchdog, audits, workflow governance, or memory architecture. Otherwise it stays cold so the Token budget does not get eaten just because a folder exists.

Cleaned up early PLTRF drift before it became normal. Fixed the broken `references/context-token-limits.md` pointers, corrected the long-term preservation acronym split, synced the repo-cognition reference mirrors back to canonical `behavior/`, and turned the Codex/Claude/Gemini overlays into thin wrappers around `SKILL.md`. Same hooks, fewer duplicated rules, less chance the repo becomes the thing the agent fights.

---

## Knob: docs scaffolding + CLAUDE overlay — Friday, May 22, 2026

Created `docs/repo-organization.md` as the structural map of the four-folder layout (`behavior/`, `skills/`, `workflows/`, `design/`) plus `docs/` for this repo's own operational memory. The file describes what each folder is for, what lives inside it, and the cold-start consultation order. It is meant to be the structural source of truth for the repo while `AGENT.md` remains the behavioral source of truth and this file (`context-orientation.md`) remains the temporal source of truth. The three do not duplicate each other.

Replaced the empty root `CLAUDE.md` with a Claude-specific cold-start overlay that sits on top of `AGENT.md`. It walks through the cold-start order Claude should follow, calls out the Skills format used in `skills/`, and codifies the user's standing preferences: every Bump gets a one-to-two paragraph summary in this file, and overflow past 5000 characters spawns `context-ori-summary-2.md` onward. Also initialized this `context-orientation.md` file as part of the same Knob, since the directive required it to exist for future Bumps to log against.

---

## Prior history

Entries before this Knob live in commit history and in `README.md`'s "Updates" section. Notable prior Bumps:

- **5.16.26** — Added and rewrote Context documents, Updated Skills folder, created `AGENT.md`. The behavior/ docs and the cold-start file were established at this point.
- **5.11.26** — Initial release of `Documentation.md`. Repo scaffolding and intent set.

These are recorded here for traceability but were not logged Knob-by-Knob at the time. Future Bumps follow the format above.

---

## Format

Each entry uses this shape:

```
## Knob: <short tag> — <Day, Month DD, YYYY>

<One paragraph describing what changed and why.>

<Optional second paragraph for cross-references, follow-up Knobs, or context that
will matter to the next agent picking this up.>
```

Keep entries narrow. The point is the *next* agent (or you, after a hiatus) should be able to scan this file and rebuild the working state without reading every commit diff. If an entry needs more than two paragraphs, it probably belongs in its own doc with a pointer from here.
