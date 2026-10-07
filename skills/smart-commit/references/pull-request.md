# Pull Request

Use after commit and push, or for a PR-only request on an already pushed branch.

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
- Report the PR link, compared commit, and material verification gaps. Do not approve, merge, enable auto-merge, or deploy as part of this skill. Return the PR and compared commit to the smart-commit workflow; do not invoke review yourself.
