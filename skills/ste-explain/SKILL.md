---
name: ste-explain
description: Explain technical concepts, investigation findings, and development results with consistent terms, explicit conditions, and clear evidence. Use when explaining development work or when the user requests ste-explain, including alongside other skills.
---

# STE Explain

Help the reader understand what happens, assess the evidence, and decide what to do next without guessing. Adapt ASD-STE100 principles to development communication in the reader's language. This skill does not establish formal ASD-STE100 compliance.

## Scope and precedence

- Apply these principles to user-facing explanations, progress updates, and development reports. Do not rewrite code, identifiers, quotations, logs, or product copy merely to match this style.
- Preserve the active skill's required workflow, output sections, and repository language rules. Honor the user's requested style or format. Improve the wording within those constraints.
- This skill does not authorize implementation, additional tests, deployment, or external messages. Report available evidence; do not expand the task to complete a report template.

## Writing rules

- Lead with the result, answer, or decision the reader needs. Explain the relevant user-visible behavior before implementation details when that helps the reader.
- Use one name for each concept. Preserve actual UI labels and technical identifiers. Explain unfamiliar technical terms briefly on first use; do not replace precise terms with misleading analogies.
- Put a condition before the action or result it controls. Name the actor and target when they would otherwise be unclear. Use active voice for instructions.
- Separate independent instructions. Keep necessary causal relationships and exceptions together; do not fragment every explanation into isolated sentences.
- Replace vague claims such as "optimized," "handled," or "completed" with the behavior that changed. Include thresholds or quantities only when the evidence provides them.
- Distinguish observations from hypotheses, expected effects, and recommendations where confusion is possible. Use ordinary wording rather than mandatory labels on every sentence.
- Preserve conditions, exceptions, numbers, uncertainty, and supporting references. Never invent missing behavior, requirements, or verification results to make an explanation feel complete. Ask only when missing information is necessary for the requested work; otherwise state the limit.
- Keep simple answers short. Use lists for steps, tables for comparisons, and diagrams for relationships when they make the explanation easier to understand. Do not create an interactive artifact or video by default.

## Development-specific distinctions

- State what was verified and what remains unverified when reporting a result. Passing automated tests does not establish device behavior, production recovery, or measured performance improvement.
- Use completion terms precisely: a local edit, a passing test, a commit, a PR, and a deployment are different states. Identify the environment when relevant; do not collapse staging and production into "deployed."
- Name the relevant app or service when "backend" or "app" is ambiguous. Confirm the current implementation before asserting ownership or behavior.
- Link to the relevant file, test result, or other evidence when it helps the reader assess a claim. Do not bury the explanation in an inventory of tool calls.

## Adapt to the task

Use these as prompts for selecting useful information, not mandatory headings:

- Concept: meaning, relevant use, concrete example, and limitations.
- Investigation: symptom, observed facts, possible cause, and next useful check.
- Change report: changed behavior, reason, verification, and remaining uncertainty.
- Design comparison: decision, meaningful differences, recommendation, and conditions that could change it.

Before sending, check whether the reader can distinguish what is known, what changed, and what still needs a decision or verification. Remove irrelevant detail without deleting required review sections or material limitations.

## Example: development report

The following is hypothetical. Use these details only when the actual evidence supports them.

**Before**

> Optimized the home carousel for Android. Virtualization is complete and tests pass.

**After**

> The home carousel now creates cards near the visible area instead of creating every card at once. This reduces the initial number of mounted cards.
>
> The related automated tests passed. We have not measured scrolling performance on an Android device. Delayed card appearance and scroll position still need device verification.

The revised explanation separates the implementation change from an unmeasured performance outcome. Translate the explanation into the user's language as required; do not mechanically apply English word-count or grammar restrictions to Korean.
