# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `ctx-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: ctx-rules.md voice tightening — Sunday, June 7, 2026, 04:20 AM CDT

Tightened the Operational Governance section in `behavior/ctx-rules.md`. The block was drifting into metaphor — *Software development is a marathon, not a sprint*, *Context is our fuel*, *LOCKED-IN and FROZEN* in all caps. Cold-start material should be terser than that.

Kept the Matt-isms that earned their place — "we lose our way," "Context is the fuel. Limited supply.", "discard the dead weight." Cut the cliché. Killed the LOCKED-IN ALL CAPS. Collapsed the meandring "Therefore, agents must be able to work with..." sentence into something direct. Net result is shorter, sharper, still sounds like me. Section dropped from roughly 480 words to about 210.

The doc is agent-facing rules content; voice tweaks belong in author-voiced surfaces, not in canonical doctrine that other agents read as instructions.

---

## Knob: log migration — hot file back under cap — Sunday, June 7, 2026, 04:05 AM CDT

The hot orientation log was sitting at over 10,000 characters — twice the 5000-char threshold. Time to migrate. Pulled the ten oldest Knobs out of `docs/memory-ctx/ctx-orientation.md` and prepended them at the top of `docs/memory-ctx/ctx-ori-summary-2.md` in newest-first order so the cold archive stays scannable. The hot file now holds the current Knob plus the last three — exactly what the discipline calls for.

Worth noting: this Knob itself triggers another migration in the same shape. With this entry added, the hot file goes back over the count, so the oldest of that set (structural moves) gets moved to summary-2 in the same commit. Steady-state behvaior — every Bump moves one out the bottom. Keeps the hot file lean automatically as long as the discipline holds.

No other changes in this Knob. Pure log hygiene.

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

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
