---
name: clarify
description: Clarify the problem, scope, and observable success criteria before implementation when a report or issue leaves consequential questions unresolved.
---

# Clarify

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Turn a report or issue into a problem the worker and agent understand the same way. A confirmed root cause is not required.

1. Read the issue, existing investigation, and relevant project instructions. Inspect enough current code or evidence to distinguish reported symptoms from confirmed facts. Reuse established scope and slice dependencies.
2. State who is affected, actual versus expected behavior, the desired outcome, scope boundaries, and observable success criteria. Keep hypotheses separate from evidence and record the source revision when code matters.
3. Ask only questions whose answers change scope, success, or the next action. Use the environment's user-question tool when available; otherwise ask in chat. Offer a recommendation and its tradeoff in language the worker can assess. Do not ask them to supply facts you can inspect.
4. Summarize the agreed problem and remaining uncertainties in the existing issue handoff or the project's designated plan location. Do not change an external issue without authorization. When no location is prescribed, provide a concise handoff in chat.

Proceed to a handoff once success and scope are clear enough. Uncertainty about implementation belongs in `implement`; do not demand certainty about every detail. Reuse existing answers instead of running a fixed interview.

Output the problem, scope, success criteria, evidence, and only the unresolved decisions that matter. Do not implement the solution within clarification itself.

## Next steps

- If the problem is clear, an existing ticket identifies the work, and implementation is requested, invoke `implement`. Pass the agreed problem, scope, success criteria, evidence, and relevant issue or plan reference.
- If implementation is requested but no ticket exists, explain that `implement` needs one and offer `create-linear-issue`; do not invent or silently publish a ticket.
- If the worker wants the clarified work registered as an issue, invoke `create-linear-issue` with the same handoff. Reuse the investigation rather than repeating the interview.
- If only clarification was requested, report the result and stop. When the desired continuation is genuinely unclear, offer implementation or issue creation as the relevant choices and ask once. Continue within existing authorization without asking again.

Resolve the selected skill from the installed skills and load its instructions before proceeding. If it is unavailable, report the missing skill and provide the handoff; do not pretend it ran.
