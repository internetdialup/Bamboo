# Claude Agent Rules

Use `SKILL.md` as the source of truth for `repo-cognition`.

This file exists so Claude has a vendor-shaped hook without copying the whole Skill body. Do not fork the rules here. If the Skill changes, update `SKILL.md` and the references. Otherwise this becomes another drift point and the repo starts fighting the agent.

Claude note: keep the Skill loaded as a working discipline, not a wall of duplicated memory. Pull the exact reference doc the current Knob names.

Load (canonical paths at the repo root):
- `SKILL.md`
- `behavior/ctx-rules.md`
- `behavior/ctx-lexicon.md`
- `behavior/ctx-entropy.md`
- `behavior/ctx-window.md`
- `behavior/ctx-token-limits.md`

The `references/` folder inside this Skill used to mirror the behavior docs. It is now a thin pointer layer — load canonical instead.
