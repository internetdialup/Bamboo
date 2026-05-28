# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `context-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: user-model split + LTRP retirement + architecture/ cold-start integration — Thursday, May 28, 2026

Net-new user-modeling content (Analyze User Behavior, Talk to the User, User Psychology) extracted from `architecture/memory.md` into a new `behavior/user-model.md` alongside the four context-* docs. The original `memory.md` stays in place — `architecture/` is a real working folder with siblings (memory-drift, memory-watchdog, workflow-tools added the same week). The earlier draft of this Knob proposed deleting `architecture/`; that was wrong and got reverted before merge.

Vocabulary canonicalized: `LTRP` retired via a clarifier in `context-rules.md`, plus a small canonical-terms glossary block added with one-line entries for **Watchdog**, **Memory Drift**, **Memory Rot**, and **CPP** — each pointing at its canonical home in `architecture/`. `Canonical AI Agent Profile` intentionally not canonicalized yet; awaiting more usage.

Same Knob wires `architecture/` into the cold-start path. `README.md`, `AGENT.md`, `CLAUDE.md`, `docs/repo-organization.md`, and `behavior/context-utility.md` updated so cold-start agents see the folder as part of the standard set ("five working folders" replaces "four"). PLTRF discipline applied to the change itself — every cross-reference lands atomically in this single commit.

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
