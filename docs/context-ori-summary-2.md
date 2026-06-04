# Documentation.md — Context Orientation Summary 2

Cold storage for older Knobs moved out of `docs/context-orientation.md` when the hot log approached the 5000-character threshold.

Read this only when the current Knob references older scaffolding, prior release history, or the origin of the repo map.

---

## Knob: docs scaffolding + CLAUDE overlay — Friday, May 22, 2026

Created `docs/repo-organization.md` as the structural map of the four-folder layout (`behavior/`, `skills/`, `workflows/`, `design/`) plus `docs/` for this repo's own operational memory. The file describes what each folder is for, what lives inside it, and the cold-start consultation order. It is meant to be the structural source of truth for the repo while `AGENT.md` remains the behavioral source of truth and `context-orientation.md` remains the temporal source of truth. The three do not duplicate each other.

Replaced the empty root `CLAUDE.md` with a Claude-specific cold-start overlay that sits on top of `AGENT.md`. It walks through the cold-start order Claude should follow, calls out the Skills format used in `skills/`, and codifies the user's standing preferences: every Bump gets a one-to-two paragraph summary in `docs/context-orientation.md`, and overflow past 5000 characters spawns `context-ori-summary-2.md` onward. Also initialized `context-orientation.md` as part of the same Knob, since the directive required it to exist for future Bumps to log against.

---

## Prior history

Entries before this Knob live in commit history. Notable prior Bumps:

- **5.16.26** — Added and rewrote Context documents, Updated Skills folder, created `AGENT.md`. The behavior/ docs and the cold-start file were established at this point.
- **5.11.26** — Initial release of `Documentation.md`. Repo scaffolding and intent set.

These are recorded here for traceability but were not logged Knob-by-Knob at the time.
