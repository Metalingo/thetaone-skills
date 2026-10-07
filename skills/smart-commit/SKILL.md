---
name: smart-commit
description: Commit the requested changes, push the working branch, and create or update its pull request as one workflow; honor narrower commit-only or no-PR requests.
---

# Smart Commit

## Communication

When explaining findings or asking the worker a question, use the installed `ste-explain` skill through the environment's skill mechanism, or read its SKILL.md if no invocation tool exists. Load it once and apply it alongside this workflow, preserving required templates. If it is unavailable, keep terms consistent, put conditions before actions, and distinguish evidence from assumptions; do not block the task on installation.

Default scope is commit → push → create or update the PR. Honor explicit limits such as commit-only, push-only, or no PR, and project authorization rules. A PR-only request can use this skill too: skip completed stages rather than making an empty commit.

Before committing, establish the project-designated PR base and a suitable working branch. If on a protected/base branch, create a working branch according to project rules while preserving changes. Explicit authorization to push directly does not require a meaningless PR from a branch to itself.

## Commit and push

1. Read repository commit rules and inspect status, staged and unstaged diffs, relevant untracked files, and recent commit style. Establish the intended branch and remote. Exclude unrelated work, credentials, generated clutter, and local configuration.
2. Stage only the requested changes. If unrelated intents require a grouping decision, propose the split and ask; many files alone do not require multiple commits.
3. Run required focused checks and honor Git hooks. Investigate hook failures and fix relevant causes; never bypass hooks with `--no-verify` or equivalent. Stop and report a blocker if the fix requires unrelated changes.
4. Write an imperative conventional subject, following project language and length rules. Explain what changed and why, material impact, related issues, verification, and useful rollback notes. Scale the body to the change; do not fill empty sections or duplicate the diff.
5. Commit, inspect the resulting commit, and push to the intended working branch. Set upstream for a new branch as needed. Never push directly to project-protected branches such as `main` or `staging` without explicit authorization. Do not infer that every branch is protected.
6. Verify the remote head matches the local commit before proceeding to the PR. If no new changes exist, check for already committed or pushed work that still needs delivery.

Do not force push, rewrite others' work, bypass branch rules, or switch authentication methods to evade a failure. On a rejected push, inspect remote divergence and preserve local work; ask when resolution needs a history or scope decision. Use only permission options supported by the current environment.

## Create or update the PR

Read [references/pull-request.md](references/pull-request.md) and follow it for the pushed change. Preserve issue scope and project conventions. If the branch has no changes against its base, report that no PR is needed rather than creating one. If PR creation is blocked, retain the successful commit and push and report the exact remaining step.

## Finish

Report the commit, branch, push result, PR link, checks, and material limits. Do not approve, merge, enable auto-merge, or deploy. When called directly, stop here. When called by `implement`, return the PR and compared commit so that caller can invoke `review-pr`.
