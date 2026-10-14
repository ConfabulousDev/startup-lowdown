# startup-lowdown

An [Agent Skill](https://agentskills.io) that researches a startup for anyone considering a job there, from a recruiter's first message to an offer in hand. It produces a cited report: funding, leadership, growth, employee sentiment, red flags, questions to ask, and backchannel candidates.

## Report

Every claim links to its source.

- **Bottom line**: whether an investor who could back only this company would, and what to find out next.
- **The company**: product, customers, history.
- **Flags**: red, yellow, and green, each explained.
- **Money and prospects**: rounds, investors, revenue signals, estimated runway.
- **People and growth**: headcount trend, layoffs, open roles, locations.
- **Leadership**: founders' track records, executive turnover.
- **Product and technology**: what works, what doesn't, engineering quality.
- **Timeline and records**: recent events; court, labor, and layoff-notice checks.
- **What employees say**: recurring themes from reviews and forums.
- **What to ask**: the five most consequential questions, marked friendly or direct.
- **Backchannel**: whom to ask, why, and what to ask, with a draft message.

## Install

Requires an agent with web search and page fetching. Script execution and a browser are optional.

Any agent that supports skills:

```sh
npx skills add ConfabulousDev/startup-lowdown
# or
gh skill install ConfabulousDev/startup-lowdown startup-lowdown
```

As a plugin or extension:

| Agent | Command |
|---|---|
| Claude Code | `/plugin marketplace add ConfabulousDev/startup-lowdown`, then `/plugin install startup-lowdown@confabulous-dev` |
| Codex, ChatGPT desktop | `codex plugin marketplace add ConfabulousDev/startup-lowdown`, then install from `/plugins` |
| GitHub Copilot CLI | `copilot plugin install ConfabulousDev/startup-lowdown` |
| VS Code | **Chat: Install Plugin From Source** → `https://github.com/ConfabulousDev/startup-lowdown` |
| Cursor | **Customize → From GitHub Repository** → the repository URL |
| Gemini CLI | `gemini extensions install https://github.com/ConfabulousDev/startup-lowdown` |
| Hermes Agent | `hermes skills install ConfabulousDev/startup-lowdown/skills/startup-lowdown` |
| OpenClaw | `openclaw plugins install git:ConfabulousDev/startup-lowdown` |

As an upload, from the [latest release](https://github.com/ConfabulousDev/startup-lowdown/releases/latest):

| App | File |
|---|---|
| Claude (web, desktop, mobile), ChatGPT, Manus | `startup-lowdown.zip`. Claude requires code execution to be on. |
| Microsoft 365 Copilot, Perplexity | `startup-lowdown-flat.zip` |

Other agents: copy `skills/startup-lowdown/` into the agent's skills folder, such as `~/.agents/skills/`.

## Use

Ask in your own words:

- "A recruiter from Acme (acme.com) reached out about a sales role. Is it worth a call?"
- "I have an offer from Acme to join the engineering team. What would I be getting into?"

Provide the company and its website. Your area (engineering, sales, …) is optional; it shifts emphasis, not scope. The report is written to `startup-lowdown/<company>/report.md` in the working folder.

## Browser (optional)

Sites behind a login (LinkedIn, Glassdoor, Crunchbase, paid news) need a browser tool connected to your agent, such as [Playwright MCP](https://github.com/microsoft/playwright-mcp) with its browser extension. Before research starts, the skill asks:

1. whether to use the browser;
2. which sites to include;
3. whether it may open LinkedIn profiles (LinkedIn notifies the people viewed);
4. that you sign in to those sites.

After that, the run is unattended.

The agent is instructed to read only and to stay on the sites you picked. Nothing enforces this: a browser tool can reach every site its browser profile is signed into. Use a profile signed into research sites only.

## Responsible use

- Follow the terms of the sites you research.
- Reports name only founders, executives, board members, investors, and team leaders, using professional information. They never include contact details.
- Reports can be wrong or out of date. Verify before you rely on or share one.

## Disclaimer

Use at your own risk. Provided as is, without warranty. Not legal, financial, or career advice. Not affiliated with any company or site named.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security problems as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). Maintained by Confabulous Software LLC.
