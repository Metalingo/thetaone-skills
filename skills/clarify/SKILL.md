---
name: clarify
description: Clarify the problem, scope, and observable success criteria before implementation when a report or issue leaves consequential questions unresolved.
---

# Clarify

Turn a report or issue into a problem the worker and agent understand the same way. A confirmed root cause is not required.

1. Read the issue, existing investigation, and relevant project instructions. Inspect enough current code or evidence to distinguish reported symptoms from confirmed facts. Reuse established scope and slice dependencies.
2. State who is affected, actual versus expected behavior, the desired outcome, scope boundaries, and observable success criteria. Keep hypotheses separate from evidence and record the source revision when code matters.
3. Ask only questions whose answers change scope, success, or the next action. Use the environment's user-question tool when available; otherwise ask in chat. Offer a recommendation and its tradeoff in language the worker can assess. Do not ask them to supply facts you can inspect.
4. Summarize the agreed problem and remaining uncertainties in the existing issue handoff or the project's designated plan location. Do not change an external issue without authorization. When no location is prescribed, provide a concise handoff in chat.

Proceed to a handoff once success and scope are clear enough. Uncertainty about implementation belongs in `implement`; do not demand certainty about every detail. Reuse existing answers instead of running a fixed interview.

Output the problem, scope, success criteria, evidence, and only the unresolved decisions that matter. This skill does not implement the solution or automatically create issues.
