# Thetaone Skills

Eight composable agent skills for evidence-based development. Built from Thetaone's working practices; project conventions stay in the project.

| Skill | Outcome |
| --- | --- |
| `create-linear-issue` | Investigated Linear issues and verifiable vertical slices |
| `clarify` | A clear problem, scope, and success criteria |
| `implement` | Reviewed plan, worktree implementation, checks, and authorized PR handoff |
| `smart-commit` | Traceable commit and push |
| `create-pr` | A complete, reviewable PR |
| `review-pr` | Requirement and quality review; evidence-based feedback handling |
| `verify` | Deployment and runtime verification without code changes |
| `ste-explain` | Clear explanations with precise evidence and conditions |

A typical path is issue → clarify → implement → commit → PR → review → deployment → verify. Every skill is independently callable; this is not a mandatory pipeline. `ste-explain` can support any stage. Deployment itself follows the target project's process.

## Install

Clone this private repository with an account that has access:

```sh
git clone https://github.com/Metalingo/thetaone-skills.git
```

Each directory under `skills/` is a standalone skill whose entrypoint is `SKILL.md`. Install or copy the selected directories into the skill location supported by your agent. Keep the entire directory together. For Codex, a user-level example is:

```sh
mkdir -p ~/.codex/skills
cp -R thetaone-skills/skills/clarify ~/.codex/skills/
```

For Claude Code, a user-level example is:

```sh
mkdir -p ~/.claude/skills
cp -R thetaone-skills/skills/clarify ~/.claude/skills/
```

Check for an existing skill with the same name before copying; do not overwrite customizations unintentionally. Install the other directories the same way. Invoke a skill by its name through your agent's skill interface. Installing these files does not configure connectors or grant access.

## Project setup

The skills read the target project's instructions and existing documents. Supply only what the workflow needs:

- Issue workflow: investigation base, Linear destination and issue conventions.
- Implementation: worktree/setup commands, plan location, required checks, and review gates.
- Git and PR workflow: protected/base branches, commit rules, PR template, labels, assignee, and issue-link syntax.
- Verification: environment mapping, deployment identity and rollout checks, telemetry locations, and success criteria.

Reuse existing documentation; no Thetaone-specific filenames are required. Linear access is needed to publish issues, Git hosting access to publish PRs, and the project's deployment/observability access to verify releases. `verify` reports **unable to verify** when evidence or access is insufficient. It does not require AWS, GitHub Actions, EAS, Sentry, or PostHog specifically.

Skills ask the worker when a decision changes scope or requires judgment. They use a question tool when available, with a chat fallback. Existing authorization is preserved; installation alone does not authorize external writes, merge, deployment, or real-world test side effects.

## Maintenance

Keep entrypoints short. Put provider-specific commands in the consuming project's documentation rather than these shared skills. Validate local files with:

```sh
bun run validate
```

The check validates packaging and frontmatter, not agent behavior. These are initial drafts; evaluate them on real tasks before treating their outcomes as proven. No external issue, PR, payment, notification, or deployment is created by validation.

## Origins

`create-linear-issue`, `smart-commit`, `review-pr`, and `ste-explain` adapt Thetaone's existing language-pilot skills. `clarify`, `implement`, `verify`, and `create-pr` were developed from the team's agreed workflow. External skill collections informed the discussion; their source files are not vendored here. `ste-explain` adapts plain-language principles and does not claim formal ASD-STE100 compliance.
