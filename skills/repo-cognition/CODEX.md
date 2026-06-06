# Codex Agent Rules

Use `SKILL.md` as the source of truth for `repo-cognition`.

This file exists so Codex has a vendor-shaped hook without copying the whole Skill body. Do not fork the rules here. If the Skill changes, update `SKILL.md` and the references. Otherwise this becomes another drift point and the repo starts fighting the agent.

Codex note: inspect first, retrieve only what the active Knob needs, and keep the repo memory clean when you touch the files.

Load:
- `SKILL.md`
- `references/ctx-entropy.md`
- `references/ctx-window.md`
- `references/ctx-rules.md`
- `references/ctx-token-limits.md`
