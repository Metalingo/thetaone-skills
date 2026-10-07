---
name: implement
description: Implement an existing Linear issue or equivalent ticket in a Git worktree, then complete tests, commit, push, PR creation, and PR review as the default workflow.
---

# Implement

Take an existing ticket through planning, implementation, checks, `smart-commit` (commit, push, PR), and `review-pr`. Invoking this skill requests the whole workflow; do not ask for separate permission at each stage. Merge and deployment are outside this workflow.

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

## Start from the ticket

Read the referenced ticket, acceptance criteria, linked evidence, and relevant project instructions and code. Resolve a ticket already supplied in conversation without asking again. If no ticket can be identified, request its link or identifier; do not invent scope or silently create a ticket. This is required input, not an approval gate.

Use the ticket's existing slices and dependencies. Work on the selected ticket or slice without creating a second breakdown or dependency scheme.

Use a suitable existing Git worktree or create one from the latest project-designated base. Use managed worktree tools when available. Record the ticket, worktree, branch, and base revision. Preserve unrelated work and follow project setup instructions. Worktrees are part of this skill across projects, not a language-pilot-specific convention.

## Plan, review, and implement

Persist a concise plan in the project's designated location, or `docs/plan/` if none exists. Reuse an existing plan. Include the intended outcome, affected boundaries, approach, and meaningful checks.

Review the plan against the ticket, current contracts, failure behavior, and testability, then proceed. Do not introduce a worker approval gate merely because planning is complete, implementation is difficult, or confidence needs improvement. Investigate uncertainties with available code, documents, and focused experiments.

Implement the ticket's scope. For bugs, reproduce the failure before fixing it when feasible. Run required checks and focused behavior tests. Fix routine implementation and test failures without asking the worker to choose ordinary technical details. Do not weaken tests or bypass hooks. Update affected documentation and keep the plan's decisions and check results current.

## When to pause

The workflow's decision-blocking condition is new evidence that changes the agreed work: a newly discovered fact, or an assumption or supporting evidence shown to be wrong. Pause the affected work when this changes scope, acceptance criteria, dependencies, or the viability of the approach and requires a worker decision. Do not silently expand scope or continue on a disproven premise.

Explain the new fact, the previous assumption, its impact, and the recommended next step. Use a user-question tool when available; otherwise ask in chat. Continue independent work that does not depend on the answer. Resume when the decision is resolved.

Routine technical uncertainty and stage transitions are not blockers. Actual access or tool failures must still be reported truthfully: attempt an available authorized alternative, and preserve completed work if execution is impossible. This skill does not override explicit user limits or higher-priority repository rules.

## Deliver by default

Load and invoke the installed skills in this order without another end-to-end request:

1. `smart-commit`: pass the ticket or slice, worktree, branch, base, plan, intended changes, and check results. Complete commit, push, and PR creation or update. Confirm the returned PR and compared commit before continuing.
2. `review-pr`: pass the PR and ticket acceptance criteria. Complete the review and report its findings and verdict. This step is part of the task, not an optional suggestion after PR creation.

When called here, these skills are stages of this workflow; their standalone stopping points do not end `implement`. If a skill is unavailable, follow the equivalent project procedure and disclose the fallback. Do not invent a successful commit, PR, or review. Do not start an indefinite fix/review loop to obtain approval.

## Completion

Complete the task by reporting the ticket, PR, commit, checks, review verdict, and material remaining findings. Record the handoff in the plan. Do not claim completion after local edits or tests alone, and do not equate a completed review with an approval.

After the project's deployment process, recommend `verify` with the PR or release identity, target environment, and acceptance criteria. Do not wait for, trigger, or verify deployment as part of the default workflow.
