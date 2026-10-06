---
name: verify
description: Verify that a specified change reached the intended environment and achieved its acceptance criteria using deployment records and runtime evidence, without changing code.
---

# Verify

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

Report release identity, environment, observation window, and relevant evidence links. When implementation or instrumentation is needed, describe the missing evidence, required logs/events, and expected verification method. Hand off through `create-linear-issue` when requested and available, or provide an issue-ready summary. Never fix it within this skill. Do not close an issue merely because no errors were found.
