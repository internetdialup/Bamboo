# Claude Agent Rules

Use `SKILL.md` as the source of truth for `repo-cognition`.

This file exists so Claude has a vendor-shaped hook without copying the whole Skill body. Do not fork the rules here. If the Skill changes, update `SKILL.md` and the references. Otherwise this becomes another drift point and the repo starts fighting the agent.

Claude note: keep the Skill loaded as a working discipline, not a wall of duplicated memory. Pull the exact reference doc the current Knob names.

Load:
- `SKILL.md`
- `references/ctx-entropy.md`
- `references/ctx-window.md`
- `references/ctx-rules.md`
- `references/ctx-token-limits.md`
