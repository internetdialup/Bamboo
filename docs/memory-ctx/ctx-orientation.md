# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `ctx-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: cherry-picked user-model.md from dangling branch — Sunday, June 7, 2026, 04:50 AM CDT

The dangling `knob/memory-split-ltip-canonical` branch carried one unique commit adding `behavior/user-model.md`. The rest of the branch's content (memory-drift, memory-watchdog, workflow-tools) had been independantly rebuilt on main since the branch was created back on May 28. So instead of merging the whole stale branch, I cherry-picked just the doc and adapted it to current naming.

`behavior/user-model.md` lives on main now. The agent has a focused "user view" doc that sits next to the ctx-* family — context-side disciplines on one side, user-side disciplines on the other. Three sections: Analyze User Behavior, Talk to the User, User Psychology. Cross-references inside the doc updated from `context-*.md` to `ctx-*.md` to match current naming.

Updated `behavior/ctx-utility.md` (added user-model.md as a sibling entry) and `docs/repo-organization.md` (added it under the behavior/ section description). No cold-start order change — this fits the gated tier where agents pull it on demand when modeling the user is part of the work.

Tried to delete the dangling remote branch in the same Knob but the action got blocked by the auto-mode classifier — destroying remote branches needs explicit user authorization. The question is surfaced back to the user separately. For now the branch stays on origin with its one commit intact; user-model.md is preserved on main regardless.

---

## Knob: fork-resync workflow doc — Sunday, June 7, 2026, 04:35 AM CDT

Wrote `workflows/fork-resync.md` — the procedure for catching a fork up to a canonical structural change. Covers when to resync (rename, folder move, new doc family, discipline shift), the pre-flight checklist (read the canonical Knob entry, check PLTRF CI is green, clean working tree, note fork-specific deviations), the procedure itself (single atomic commit per fork, no orphan pointers, no rewriting historical Knob entries), and the anti-patterns to avoid.

The honest take: I'm not touching the seven downstream forks directly. Each one has its own state — local changes, in-flight branches, custom adaptions — and resyncing them is a per-fork judgment call I shouldn't make alone. The doc gives you the recipe so any fork can be brought current when you're ready, on whatever schedule you decide.

Cross-referenced from `project-setup.md` (first-time bootstrap, see fork-resync for every sync after) and surfaced in `docs/repo-organization.md` under the workflows section. New forks land in setup; existing forks needing catch-up land here.

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

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
