---
name: memory-watchdog
description: repository memory watchdog skill for auditing stale maps, broken references, missing Knob logs, memory rot, context drift, duplicate documentation, secret-risk surfaces, and AI governance hygiene in long-running repos.
---

# Memory Watchdog

This Skill is the repo hygiene auditor.

The Watchdog exists because memory rots quietly. A file moves. A map does not. A Skill points at an old reference. A Knob gets logged in README but not in `context-orientation.md`. Then six weeks later the repo becomes the thing the agent fights.

Use this Skill when:
- adding, moving, or renaming docs
- adding or changing Skills
- changing `architecture/`, `behavior/`, `docs/`, or cold-start files
- auditing stale references or broken paths
- checking if a Knob was logged
- checking whether memory and maps still agree
- preparing OSS governance docs that need to stay coherent over time

## Watchdog Pass

Run the pass before and after memory/documentation changes:

1. Check the files that changed.
2. Check the maps that should know about those files.
3. Check the active Knob log.
4. Search for stale old paths.
5. Search for duplicated concepts that now have two names.
6. Check that Skills point at canonical docs instead of stale copies.
7. Check for secret-risk language or files when workflows touch `.env`, API keys, or private context.

The Watchdog should be strict about structure and light about voice. Do not over-polish the writing. Fix the drift.

## Map Hygiene Rules

- New folder or moved file gets map updates in the same change.
- New Skill gets `skills/skill-map.md` and `docs/repo-organization.md` updates.
- New architecture memory doc gets `docs/repo-organization.md` and the relevant Skill pointer updated.
- Every Bump that changes repo structure gets a `docs/context-orientation.md` entry.
- If `docs/context-orientation.md` crosses 5000 characters, roll older entries into the next summary file.
- Broken references are memory rot. Fix them before they become normal.

## Search Patterns

Use searches like these when auditing:

```bash
rg -n "old-file-name|old-folder-name" .
rg -n "memory-context|memory-watchdog" skills docs README.md AGENT.md CLAUDE.md
rg -n "context-token-limit\\.md|architecture/memory\\.md|architecture/memory-watchdog\\.md" .
find skills -maxdepth 3 -type f -print | sort
```

Adjust the names to the current Knob. The point is not the exact command. The point is to catch drift before handoff.

## Canonical References

Read only what the audit needs:
- `docs/repo-organization.md`
- `docs/context-orientation.md`
- `skills/skill-map.md`
- `AGENT.md`
- `CLAUDE.md`
- `architecture/memory/memory-watchdog.md`
- `architecture/memory/memory-drift.md`
- `architecture/memory/memory-crud.md`

If the Watchdog finds conflict, report the conflict plainly and patch the source of truth. Do not create a second explanation to hide the first broken one.
