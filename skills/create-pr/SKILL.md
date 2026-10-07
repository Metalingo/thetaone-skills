---
name: create-pr
description: Create or update a pull request for a pushed branch when the user asks to open a PR or prepare an existing PR for review. Follow the target repository's PR conventions.
---

# Create PR

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Turn a pushed change into a reviewable PR. Commit and push belong to `smart-commit`; review belongs to `review-pr`. Use those skills only when available and authorized by the requested workflow.

## Establish the change

- Read the repository instructions, PR guideline, and applicable template. Derive the base branch, title/body language, labels, assignee, issue-link syntax, and required sections from them. Do not carry conventions over from another project.
- Confirm the repository, remote head branch, and intended base. Inspect the remote comparison and identify the exact head commit. Local uncommitted or unpushed work is not part of the PR; report it when relevant to the requested change.
- Use existing issue and slice scope. Describe additional work honestly; do not silently redefine acceptance criteria or create a new dependency scheme.
- Resolve facts from the repository and available tools first. Ask the worker only about consequential ambiguity that evidence and current instructions cannot resolve, such as conflicting base-branch intent or an unclear scope decision. Use a question tool when available.

## Prepare the PR

- Search for an existing PR for the same repository, head, and base. Update the matching open PR when the request covers that change; report a matching closed or merged PR before deciding whether new work is needed.
- Lead with the problem and resulting behavior. Explain implementation choices only where they help review. Include the linked issue, verification results, and material limits; satisfy the repository template without copying a generic template over it.
- Distinguish checks actually run from suggested checks. State which commit was tested when known, and keep local checks, CI status, and deployed behavior separate. Do not infer deployment success from PR creation or passing CI.
- Apply required labels and assignee using repository policy. Preserve unrelated existing PR metadata and human-authored content when updating.

## Publish and hand off

- Create or update the PR within existing user authorization. If publication is not authorized, prepare the complete title and body before asking. Respect requested draft status and repository readiness rules.
- Recheck the remote head before publication. If it changed, inspect the new diff and refresh the description and validation claims first. Never overwrite another contributor's branch to restore an earlier snapshot.
- If creation times out or returns an ambiguous result, query existing PRs before retrying. Stop and report unresolved authentication, permission, or policy failures; do not bypass checks.
- Verify the returned PR's head, base, title/body, and required metadata. Attach the PR to the current task when the environment supports it.
- Report the PR link, compared commit, and material verification gaps. Do not approve, merge, enable auto-merge, or deploy as part of this skill. When called directly, stop after the PR report. When called by `implement`, return the PR and compared commit so that caller can invoke `review-pr`; do not invoke it yourself.
