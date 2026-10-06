# Repository Guidance

This repository distributes agent skills, not product-specific operational rules.

- Use English for skill instructions and shared documentation; answer users in their language.
- Keep each skill focused and independently callable. Preserve the agreed division of responsibility in README.md.
- Keep project-specific branches, account identifiers, providers, and commands in the consuming project's documentation.
- Do not add a mandatory interview, approval loop, or framework for every edge case. Ask only for consequential missing decisions and preserve existing authorization.
- Changes to `verify` must preserve its prohibition on code, instrumentation, configuration, and deployment changes.
- Validate with `bun run validate`. For behavior changes, review realistic scenarios and clearly distinguish simulated checks from live execution.
- Do not commit or push unless requested. Never bypass Git hooks. Do not merge or deploy as part of skill maintenance.
