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

Choose one installation method per agent to avoid duplicate skills. No manual file copying is needed. Installing skills does not configure connectors or grant access to your services.

### Codex and other agents: skills CLI

Run from the project where you want to use the skills:

```sh
npx skills@latest add Metalingo/thetaone-skills
```

The installer lets you select skills and target agents. With Bun, use `bunx skills@latest add Metalingo/thetaone-skills` instead. To preview or install a specific skill:

```sh
npx skills@latest add Metalingo/thetaone-skills --list
npx skills@latest add Metalingo/thetaone-skills --skill clarify --agent codex
```

Add `--global` for user-level installation. Check for existing skills with the same names before installing. Use `npx skills check` and `npx skills update` to check and apply available updates; the update command can affect other skills managed by that installer too.

### Claude Code: marketplace plugin

Inside Claude Code:

```text
/plugin marketplace add Metalingo/thetaone-skills
/plugin install thetaone-skills@thetaone
```

This installs all eight skills as one plugin. Start a new session after installation. Plugin commands are namespaced, for example `/thetaone-skills:clarify` and `/thetaone-skills:implement`; the underlying skill names remain unchanged.

To refresh the marketplace and update the plugin from a terminal:

```sh
claude plugin marketplace update thetaone
claude plugin update thetaone-skills@thetaone
```

This is a self-hosted marketplace on GitHub, not an official Anthropic directory listing. An official listing requires a separate submission and acceptance. Codex users can use the skills CLI; this repository does not yet ship a native Codex plugin.

## Distribution and releases

The skill files under `skills/` are the single source for both installation methods. The Claude manifest declares the plugin version; bump it for published plugin changes. Validate, commit, push, then tag the same commit for a release. Do not label a version behavior-tested until representative tasks have been evaluated.

For a pinned skills installation, use the published tag's GitHub tree URL instead of the default branch. Only reference tags that actually exist. A public repository is not an official marketplace endorsement, and directory/search indexing is separate from direct installation.

Before broad redistribution, the maintainer should choose and add a license; this initial repository does not yet grant an explicit open-source license.

Installation references: [skills CLI](https://github.com/vercel-labs/skills), [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

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
claude plugin validate .
```

The check validates packaging and frontmatter, not agent behavior. These are initial drafts; evaluate them on real tasks before treating their outcomes as proven. No external issue, PR, payment, notification, or deployment is created by validation.

## Origins

`create-linear-issue`, `smart-commit`, `review-pr`, and `ste-explain` adapt Thetaone's existing language-pilot skills. `clarify`, `implement`, `verify`, and `create-pr` were developed from the team's agreed workflow. External skill collections informed the discussion; their source files are not vendored here. `ste-explain` adapts plain-language principles and does not claim formal ASD-STE100 compliance.
