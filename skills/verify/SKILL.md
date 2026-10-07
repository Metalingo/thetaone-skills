---
name: verify
description: Verify that a specified change reached the intended environment and achieved its acceptance criteria using deployment records and runtime evidence, without changing code.
---

# Verify

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Determine whether a deployed change works. Do not edit product code, add instrumentation, change configuration, deploy, or repair the implementation through this skill.

## Locate the deployed change

Read the issue or PR acceptance criteria and the project's deployment and observability documentation. Identify the target environment and the expected commit, artifact, or release. Discover the project's actual tools rather than assuming GitHub Actions, AWS, or EAS.

Trace the change through the delivery record to the running release. A merged PR, green CI run, submitted build, or published update alone does not prove the intended runtime is serving it. Check the appropriate deployment, rollout, or client update identity. If deployment cannot be confirmed, report **unable to verify** and the missing evidence.

## Assess behavior

Map each success criterion to existing evidence: application logs, error tracking, analytics, traces, or an authorized test scenario. Scope queries to the relevant environment, release, time window, and population. State the observation window. Absence of errors is useful only when the relevant path actually ran and telemetry covers it.

Prefer read-only observation. If a scenario sends notifications, charges money, or changes real data, establish the permitted account, environment, and action before running it. A request to inspect logs is not authorization for those side effects; do not ask about them when no such action is needed.

If access, collection delay, sampling, or missing events prevents a supported conclusion, stop that check with **unable to verify**. Do not add an elaborate waiting protocol or invent a clean bill of health. A short bounded recheck is appropriate only when evidence indicates it can resolve the question.

## Verdict and handoff

For each criterion, report **passed**, **failed**, or **unable to verify**, with its evidence and limitation. Overall: failed if a criterion has contrary evidence; otherwise unable to verify if any required criterion lacks evidence; passed only when all required criteria are supported.

Report release identity, environment, observation window, and relevant evidence links. Do not close an issue merely because no errors were found.

## Observability follow-up

When verification requires new or corrected instrumentation, invoke the installed `create-linear-issue` skill and follow its investigation and duplicate-check workflow to create the follow-up issue. This is the defined follow-up for this verification workflow; do not ask for redundant confirmation when issue creation is already authorized. An explicit read-only/no-issue request or project approval rule takes precedence.

Pass the original issue or PR, environment and release, failed or unverified criterion, observed evidence, missing logs/events, and the expected verification method. Return the created issue link with the verdict; creating an issue does not turn an unverified result into a pass. Do not implement the change or automatically continue to `implement`.

If the issue skill or Linear access is unavailable, or a necessary destination decision is unresolved, preserve an issue-ready handoff and state the blocker. Missing access or a collection delay alone does not justify an instrumentation issue; create one when evidence shows implementation is needed. Other confirmed product failures should be reported with their evidence for the worker's next decision.
