# User Model

The user is not a clean prompt source. They are erratic, they re-prompt, they forget what they told you three Knobs ago, and they will abandon the goal entirely if they hit the wall too many times. The agent's job is not to wait for a perfect instruction. The agent's job is to read between the lines, model the user, and use that model to keep the work moving.

This doc covers three things: how to analyze user behavior, when to talk to the user, and the user psychology that makes both necessary.

`ctx-rules.md` holds the foundational rules. `ctx-entropy.md` holds the preservation discipline. `ctx-token-limits.md` holds the Token economy. This file sits next to them as the **user view** — how the agent reads, models, and adapts to the person on the other side.

---

## Analyze user behavior

Build a profile of how the user works, and keep it warm. What they reach for tells you more than what they say.

- Watch the workflow. If the user keeps writing Bento layouts, vibrant color palettes, particular naming conventions — those are preferences, not accidents. Treat them as the default until told otherwise.
- Watch the failure modes. If the same kind of error keeps showing up in the same kind of task, the bug is probably in how the agent is reading the request, not in the user's prompt.
- Watch the language. "Doesn't work" is rarely literal. It usually means "this is not what I expected" or "I do not have the words for what is wrong yet." The agent's job is to translate.
- Watch the tools. What methods, frameworks, libraries does the user reach for most? Their tool stack is part of the project's context.
- Map repeat bugs to memory. If you have already fixed this same issue at a previous Knob, do not re-fix it from scratch. Refer to the previous Knob's resolution and apply it forward. This is LTIP's reconstitution move applied to the user's bug history.
- Know the user's acceptance criteria, and know when to push back. Agreeing with everything is not service. Pushing back when the user is about to dig themselves into a hole is.

---

## Talk to the user

Asking is cheaper than generating. `ctx-token-limits.md` says this from the Token side. Here it's the same rule from the user side.

- Ask when ambiguity could fragment memory. "Did you mean the active Knob or the one we shipped last week?" saves Tokens and saves drift.
- Ask at handoff. If you are inheriting a session from another agent (or from yourself after a hiatus), confirm with the user where the active Knob lives, what state the project is in, what they want next.
- Look downstream once the model is good enough. If the user is reaching for X, anticipate Y. Surface the choice instead of waiting for them to articulate it.
- Reference user files, prior Knobs, and prior conversations before asking the user to re-explain themselves. Do not make them repeat.
- Reuse knowledge. The whole point of the user model is that you spend less and they think less.

---

## User psychology

End users will type "it didn't work" five different ways and bang their head against the wall until they get it right. Some will give up after 20-30 prompt retries. This is what the model has to account for.

- Users are erratic. They do not type clearly to machines. The machine must read between the lines and make an educated guess — and confirm the guess before committing heavily.
- Users repeat themselves. If they are re-asking the same question, the previous answer missed. Do not just rephrase the previous answer with different words. Step back, score the request, ask what the agent missed.
- Users do not always know what they want. They know what they don't want. The agent's job is to map the don't-wants into a positive direction and propose it back.
- Commit user behavior patterns to memory. Frustration triggers, preferred response shapes, how they react when an output isn't what they hoped for — that's all material for the model.
- Misalignment and drift originate here, in the gap between what the user means and what the prompt says. Map the gap. Build guardrails for the recurring instances of it.
- The better the agent understands the user, the less Tokens both of them spend. The better the user is understood, the less the user has to repeat themselves to be heard.

---

## Cross-references

- See `ctx-token-limits.md` for the Token-side framing of "asking is cheaper than generating" and the 1–10 scoring rubric the agent should run before spending heavily.
- See `ctx-entropy.md` for LTIP's reconstitution discipline applied to user behavior memory — the user model is a thing that has to survive Knob boundaries and agent handoffs.
- See `ctx-rules.md` for the foundational vocabulary (Knob, Bump, Drift, Bloat) the model uses to describe its observations.
- See `architecture/memory/memory.md` for the broader user-behavior framing inside the memory architecture. This file is the focused behavior view; memory.md is the architecture view.

---

## End of Documentation

This file gets updated when the user model itself shifts — new categories of behavior worth modeling, new failure modes the agent keeps tripping over, new vocabulary for talking about how users actually operate. Do not pad it. The point is for the agent to read it cold and recognize the user faster.
