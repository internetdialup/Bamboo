# Gemini Agent Rules

Use `SKILL.md` as the source of truth for `repo-cognition`.

This file exists so Gemini has a vendor-shaped hook without copying the whole Skill body. Do not fork the rules here. If the Skill changes, update `SKILL.md` and the references. Otherwise this becomes another drift point and the repo starts fighting the agent.

Gemini note: stay strict on wayfinding. Use the Skill to keep context retrieval tight and avoid pulling stale project memory into the active window.

Load:
- `SKILL.md`
- `references/context-entropy.md`
- `references/context-window.md`
- `references/context-rules.md`
- `references/context-token-limits.md`
