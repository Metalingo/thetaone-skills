---
name: implement
description: Plan, review the plan, and implement a defined change in a Git worktree, then complete appropriate checks and the authorized commit and PR workflow.
---

# Implement

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Own planning, plan review, implementation, and local verification as one workflow. Adapt depth to the change.

## Establish the work

Read project instructions, the issue or clarified problem, and relevant code. Reuse the issue's slices and dependencies; do not create a parallel dependency scheme. Select the requested slice. Confirm a real unmet prerequisite before declaring it blocked. Continue independent work when possible.

Use a suitable existing worktree or create one from the latest project-designated base. Use managed worktree tools when available. Record the base revision and keep unrelated work intact. Follow project setup instructions.

## Plan and challenge

Persist a short plan in the project's designated location, or `docs/plan/` when none exists. Include the outcome, affected boundaries, implementation approach, meaningful checks, and material uncertainties. Reuse an existing plan when appropriate.

Review the plan against the acceptance criteria, current contracts, failure behavior, and testability. Compare alternatives only when the choice matters. If confidence is insufficient, implementation is difficult enough to require worker judgment, or a new blocker changes scope, ask with concrete evidence, options, and a recommendation. Use a user-question tool if available. Follow required project review gates; existing authorization should not trigger repeated confirmation.

## Execute and verify

Implement the agreed scope. For bugs, reproduce the failure before fixing it when feasible. Prefer focused behavior tests; apply project-required checks. Investigate failures rather than weakening tests or bypassing hooks. Update affected operational documentation when behavior or usage changes.

If evidence invalidates the plan, revise the affected decision and ask only when the worker must choose. Do not silently broaden the issue or work around an unmet dependency.

## Finish

Record the worktree, branch, base revision, material decisions, check results, and remaining limits in the plan. Keep this brief enough to resume from.

## Delivery flow

For an authorized end-to-end delivery request, invoke the installed skills in order, loading each skill's instructions rather than merely imitating its name:

1. `smart-commit`: pass the worktree, branch, intended changes, and check results. Confirm the pushed commit before continuing.
2. `create-pr`: pass the pushed branch and commit, base, issue or slice, plan, and verification results. Reuse an existing matching PR.
3. `review-pr`: pass the PR and originating acceptance criteria. Report its verdict and let the worker decide any new response; do not start an approval-chasing loop.

These skills remain standalone when called directly; this workflow owns their sequencing. A local-only request or a project approval gate takes precedence. If a required skill is unavailable, follow the equivalent project procedure within existing authorization and disclose the fallback; otherwise report the exact blocked step. Do not merge or deploy without authorization.

Report changed behavior, checks actually run, and the PR or pending step. Explain that `verify` is the next check after deployment to the intended environment, passing the PR or release identity and success criteria. Invoke it only when release verification is included in the request and deployment is ready; otherwise leave that action to the worker. Do not poll indefinitely for deployment. Local tests and PR approval do not establish deployment success.
