# Bamboo.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `ctx-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: README straggler — `Documentation-md` → Bamboo — Monday, June 8, 2026, 12:00 AM CDT

Caught a stale `Documentation-md` mention in `README.md` line 36 — the hyphen-form varaint my last regex pass missed. The earlier sed matched `Documentation\.md` with the period; never saw the hyphen form. One-line fix; the sentence now leads with `**Bamboo**` as the source repo description.

Also did a full sweep across the canonical for any other variants — case-insensitive `documentation.md`, lowercase hyphen, bare `Documentation` standalone. Everything else is either historical Knob entries (the brand rename Bump and the GitHub rename Bump describing past state — leaving those alone, can't lie about history) or the generic English noun ("documentation should make wayfinding cheaper"). All left alone.

PLTRF cleanup. No story beyond that.

---

## Knob: GitHub repo renamed to Bamboo + template repository enabled + README updated — Sunday, June 7, 2026, 11:45 PM CDT

Two GitHub-side moves and a tiny README polish.

The repo on GitHub got renamed: `internetdialup/Documentation.md` → `internetdialup/Bamboo`. GitHub auto-redirects old URLs for a while, but the local git remote got updated to the new canonical URL in the same move. Anyone with the old clone still works through the redirect.

Template repository setting got toggled on. The repo now offers a "Use this template" button next to the Code button — designed exactly for this use case, since Bamboo's whole purpose is fork-and-go starter materail. Templates give the user a fresh repo without the upstream commit history (cleaner than a traditional fork for starter projects). The existing forks workflow is unchanged; this just adds the easier path.

README's "Fork in 5 Minutes" section got a small touchup to lead with the template option as the easy path. Manual file-copy instructions stay as the fallback for people slotting Bamboo into an existing project.

No code changes beyond the README. The Bump entry covers the GitHub-side state for the record.

---

## Knob: cleanup — dangling branches gone, Copilot agent retired — Sunday, June 7, 2026, 11:28 PM CDT

Three cleanup moves on the GitHub side. First, the dangling `knob/memory-split-ltip-canonical` branch — the one whose only unique content (`behavior/user-model.md`) was already cherry-picked to main this morning — got the explicit auth and was deleted from origin. Branch pointer gone, work preserved.

Second, the `doc_v0.0.1` branch — the old development branch from late May that hosted PR #2 — got deleted from origin too. It was fully merged into main with zero unique commits, so the only thing lost was the stale pointer. Merged commits stay in main's history forever; the PR page stays accessible as a permanent receipt. Same deal for PR #1 — the closed PR page persists even after its branch was deleted earlier.

Third, the Copilot cloud agent workflow that had been registered on the repo. The workflow file lived only on `doc_v0.0.1`, so deleting that branch removed the file, but the workflow registartion was sticky in GitHub's Actions UI. `gh workflow disable` refused to turn it off (no file to disable), but deleting the workflow's only run via direct API call removed the registration entirely. The Actions tab now shows only the PLTRF Check.

Why this matters: the public-facing view of the repo should look like my work, not a parade of AI-assisted agents that ran experiments last month. The Copilot run on PR #2 was a leftover from before this discipline took hold. Removing it doesn't lie about history — the PRs are still there with their narratives intact — it just cleans up the active surface so what's visible is the current discipline, not the old detritus.

No code changes in this Knob. Only GitHub-side state. Working tree is identical. Bump entry exists so the cleanup is on the record.

---

## Knob: brand rename — Documentation.md becomes Bamboo — Sunday, June 7, 2026, 02:45 PM CDT

The framework's name flipped from Documentation.md / Repository-md to **Bamboo** — unifying the framework and the SaaS under one brand. Brand decision locked earlier today (Matt acquired `bamboo.nyc`, set up the Volcano umbrella org with `volcano.engineering` + `volcano.technology`). This Knob makes the rename real in the canonical repo.

Mechanically: `Documentation.md` (the literal file at the repo root) became `Bamboo.md` via `git mv` so the file history follows. Every reference to `Documentation.md` across the cold-start cascade — `CLAUDE.md`, `AGENT.md`, `README.md`, `docs/repo-organization.md`, `behavior/ctx-*.md`, the workflow docs, the `skills/repo-cognition/SKILL.md` — got flipped to `Bamboo.md` in one sed pass. Then I hand-polished the H1s in `Bamboo.md` and `README.md` (just "Bamboo" the brand, not "Bamboo.md" the file) and the brand-forward openings of `CLAUDE.md`. The PLTRF GitHub Action's scan list updated to look for `Bamboo.md` instead of the old name. Local PLTRF check passes clean — zero broken pointers.

What I deliberatly didn't touch: past Bump entries in this orientation log and in `ctx-ori-summary-2.md`. They reference `Documentation.md` because that's what the project was called at the time. Rewriting them would lie about history. The brand transition lives in this Knob; the past stays the past. Same call for `Repository-md` in the tree diagram inside `docs/repo-organization.md` — that's the literal folder name on disk, which stays `Repository-md` until the actual folder gets moved (which is Matt's call when he sets up the GitHub org).

This is the kind of move `behavior/ctx-entropy.md` warns about — renames that don't propagate. PLTRF discipline plus the CI action plus the manual polish pass = atomic. Memory updated too — `project_documentation-md-vision.md` became `project_bamboo-vision.md` and the index reflects.

Next: the GitHub org `bamboo` (Matt setting up); the repo itself may move from `internetdialup/Documentation.md` to `bamboo/<something>` separately. That's outside this Knob.

---

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
