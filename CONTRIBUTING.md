# Contributing

Issues and pull requests are welcome.

## Principles

- **Agent-agnostic.** Keep to the [Agent Skills](https://agentskills.io) format. No dependency on one agent or browser tool.
- **Fewer words.** Sharpen or remove an instruction before adding one.
- **Cited evidence.** Every claim in a report needs a source, including causes and consequences.
- **Privacy.** Professional information only, no contact details, read-only browsing.

## Checks

```sh
uvx --from skills-ref==0.1.1 agentskills validate skills/startup-lowdown
python3 -m py_compile skills/startup-lowdown/scripts/*.py
python3 .github/check_manifests.py
```

## Releasing

1. Set the version in `skills/startup-lowdown/SKILL.md` (`metadata.version`), `plugin.json`, `.claude-plugin/plugin.json`, and `gemini-extension.json`. CI rejects mismatches.
2. Merge to `main`, then run `gh release create vX.Y.Z --generate-notes` or push the tag.
3. CI checks the tag against the version and attaches `startup-lowdown.zip` (skill folder at the root) and `startup-lowdown-flat.zip` (`SKILL.md` at the root).

## Issues

State what the skill did and what you expected. Don't paste full reports or details about private individuals.
