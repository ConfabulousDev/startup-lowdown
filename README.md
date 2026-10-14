# startup-lowdown

Thinking about a job at a startup? Ask your AI agent, and get back a cited report on the company: funding and runway, leadership, growth, what employees say, red flags, what to ask, and whom to ask for a backchannel.

## Quickstart

```sh
npx skills add ConfabulousDev/startup-lowdown -g
```

Pick your agents when asked (Claude Code, Codex, Cursor, and dozens more). Then, in any folder, ask:

> Acme (acme.com) wants me to join their engineering team. What am I getting into?

In 10–20 minutes you get `startup-lowdown/acme/report.md`. A run makes a few hundred searches and page fetches, so expect it to use a real share of your plan's limits.

## The report

Every claim links to its source.

- **Bottom line**: would an investor who could back only this company do it, and what to find out next.
- **Flags**: red, yellow, and green, each explained.
- **Money, people, leadership, product**: rounds and runway, headcount and layoffs, founders' track records, what works.
- **Timeline and records**: recent events; court, labor, and layoff-notice checks.
- **What employees say**: recurring themes from reviews and forums.
- **What to ask**: the five most consequential questions, marked friendly or direct.
- **Backchannel**: whom to ask, why, and what to ask, with a draft message.

## Install as a plugin

Plugins update with the repository.

**Claude Code** (terminal, and the Code tab in the Claude desktop app):

```sh
claude plugin marketplace add ConfabulousDev/startup-lowdown
claude plugin install startup-lowdown@confabulous-dev
```

**Claude desktop app** (chat and Cowork): **Customize → Plugins → Add marketplace**, enter `ConfabulousDev/startup-lowdown`, then **Install**. Turn on **Settings → Capabilities → Code execution and file creation**.

**Codex** (terminal and the Codex app):

```sh
codex plugin marketplace add ConfabulousDev/startup-lowdown
codex plugin add startup-lowdown@confabulous-dev
```

Start a new session or chat afterwards.

<details>
<summary>Other agents and apps</summary>

| Agent | Install |
|---|---|
| GitHub Copilot CLI | `copilot plugin install ConfabulousDev/startup-lowdown` |
| VS Code | **Chat: Install Plugin From Source** → `https://github.com/ConfabulousDev/startup-lowdown` |
| Cursor | **Customize → From GitHub Repository** → the repository URL |
| Gemini CLI | `gemini extensions install https://github.com/ConfabulousDev/startup-lowdown` |
| Hermes Agent | `hermes skills install ConfabulousDev/startup-lowdown/skills/startup-lowdown` |
| OpenClaw | `openclaw plugins install git:ConfabulousDev/startup-lowdown` |
| GitHub CLI | `gh skill install ConfabulousDev/startup-lowdown startup-lowdown` |

Apps that take an upload, from the [latest release](https://github.com/ConfabulousDev/startup-lowdown/releases/latest):

| App | File |
|---|---|
| Claude (web, mobile), ChatGPT, Manus | `startup-lowdown.zip`. Claude requires code execution to be on. |
| Microsoft 365 Copilot, Perplexity | `startup-lowdown-flat.zip` |

Anything else: copy `skills/startup-lowdown/` into the agent's skills folder, such as `~/.agents/skills/`.

</details>

## Use

Ask in your own words, with the company and its website:

- "A recruiter from Acme (acme.com) reached out about a sales role. Is it worth a call?"
- "I have an offer from Acme to join the engineering team. What would I be getting into?"

Your area (engineering, sales, …) is optional; it shifts emphasis, not scope. Your agent needs web search and page fetching. Python 3 is optional: the skill runs two small standard-library scripts when it can, and works without them.

## Better with a browser (optional)

LinkedIn, Glassdoor, Crunchbase, and paid news need you signed in. If your agent has a browser tool (Claude in Chrome, the Claude desktop app's browser, [Playwright MCP](https://github.com/microsoft/playwright-mcp), …), the skill asks up front whether to use it, which sites to include, and whether it may open LinkedIn profiles (LinkedIn notifies the people viewed). Sign in when asked; after that the run is unattended.

The agent is told to read only and stay on the sites you picked, but nothing enforces this: a browser tool can reach every site its profile is signed into. Use a profile signed into research sites only.

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
