---
name: create-linear-issue
description: Investigate a reported problem and create a self-contained Linear issue, with verifiable vertical slices when the work spans systems.
---

# Create Linear Issue

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Create a ticket another worker can start from: why the work matters, the confirmed current state, scope, and observable success. Implementation choices belong in the implementation plan and PR.

## Investigate

Read project instructions and the report. Resolve the project-designated investigation base and fetch its latest ref; record the revision. Inspect actual relevant files rather than unrelated uncommitted work. Include file/line evidence and available read-only runtime evidence. Identify hypotheses and unavailable evidence explicitly. If code access is missing, report the limitation and prepare a draft; do not present unverified claims as an investigated ticket.

Ask for missing consequential product decisions using a user-question tool when available. Reuse existing context. For work spanning systems or contracts, describe the current component/data flow and ownership, without prescribing the future implementation.

## Shape the issue

Keep the main body short: problem, expected versus actual behavior, impact, investigation summary, scope, and success criteria. Put detailed evidence below it, including revision and relevant links. Use the target Linear tool's supported formatting. Do not add PR closing keywords to the issue.

For substantial cross-system work, use a parent for the overall problem and thin, verifiable end-to-end sub-issues. Each slice states its scope, success criteria, and known predecessors; approximately one slice per PR. Do not split merely by backend/client/database layers. A truly separate deployment prerequisite can be its own task. Reuse existing slices instead of duplicating them, and record only evidenced dependencies.

## Create and verify

Discover available Linear tools and current workspace metadata. Resolve the team, active project, status, labels, and assignee from project conventions or explicit user choices. Do not hardcode cycle names, team identifiers, status names, or priority numbers. Ask when destination remains ambiguous. Do not create a project or change connector configuration as an implicit prerequisite.

Search for an existing matching issue before creation. The user's request to create an issue authorizes the issue and necessary slice creation; do not add a redundant approval step. Set the actual parent relationship on each slice and register confirmed predecessors using Linear's native blocking relationships. Create predecessors first when IDs are needed to link dependent issues. If the available tool cannot set a relationship, record the parent or predecessor issue ID in the body and disclose the limitation; do not claim a native relationship was set. Read back created issues and relationships, including dependency direction. If a response times out, search for the attempted issue before retrying to avoid duplicates. Stop on permission or authentication failures and retain the draft.

Return issue IDs and links, destination, and slice dependencies. When called directly, stop after this report and leave the next action to the worker. Do not automatically invoke clarification or implementation. When called from another skill, return the issue links to that caller.
