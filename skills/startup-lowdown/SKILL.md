---
name: startup-lowdown
description: "Researches a startup from a prospective employee's point of view and produces a cited, holistic due-diligence report covering funding and runway, headcount trends, investors, revenue signals, founder and leadership track record, product and technology, news and lawsuits, employee sentiment, and backchannel reference candidates. Use at any stage of considering a job at a startup or private company, from a recruiter's first message through interviews to an offer in hand, or when someone asks what it is really like to work there."
license: MIT
compatibility: "Requires web search and web page fetching. Script execution and a logged-in browser are optional and improve coverage."
metadata:
  author: "Confabulous Software LLC"
  version: "0.7.0"
---

# Startup Lowdown

Give the user an outside, holistic read on a company they might work for, whether a recruiter just reached out or an offer is in hand: its real situation and prospects, the risks, what to ask and check, and whom to ask for a backchannel reference. The pitch is designed to persuade; find what it leaves out, without overstating bad news either.

## Before you start

Read [references/evidence-rules.md](references/evidence-rules.md). Every step follows it.

Inputs:

- **Company and website** (required). Ask for the website only if the name is ambiguous.
- **Area** (optional): the function the user would join, such as engineering, product, or sales. It sets emphasis (that team's leaders, churn, and questions), not scope. Ignore titles and seniority; this is not a role-fit review.

Browser access is optional, and off unless the user opts in. Without it, research runs on public search and page fetching: every module but `browser-sources` runs in full, and pages that need the browser are logged as `blocked`. With it, the run can also read sites that open fully only in the user's own browser, such as LinkedIn and Glassdoor.

If you have a browser tool, ask whether to use it, and say in the question that it is optional and the research goes ahead without it. Each question in this setup needs an explicit answer: if one is skipped, dismissed, or unclear, ask it again; never take silence as yes or no, and start no research until setup is done. If no, skip the rest of this browser setup. If yes, ask in one message which of these to include, and use only those:

- LinkedIn, and whether you may open people's profiles (LinkedIn shows them who viewed)
- Glassdoor
- Crunchbase
- Caplight, Forge, EquityZen, or Hiive (private-share prices)
- Similarweb (website traffic)
- News sites they subscribe to
- X
- Reddit, Indeed, or Wellfound
- Any other site they name

Then ask the user, in one message, whether they want to sign in, in that browser, to any picked site they have an account on. Signing in is optional too: signed-in visits are challenged less and see more, and a site they don't sign in to is read as a visitor would see it. Open each picked site once, ask them to clear any human check still showing (and any login page, for sites they chose to sign in to), and check again once they say they're done. From then on the run is unattended: never stop to ask again.

If you have no browser tool, say that a few sources need one, that it is optional, and ask whether the user wants to connect a browser first or go ahead without it.

Ask for nothing else. The report vets the company, not the job: leave out the user's pay, equity, offer terms, and day-to-day work, which are for their own conversations with the company.

## Workflow

```
- [ ] 1. Create workspace startup-lowdown/<company-slug>/findings/ (or where the user asks)
- [ ] 2. Resolve the entity → entity.json
- [ ] 3. Run research modules → findings/<module>.json
- [ ] 4. Validate: python3 scripts/validate_findings.py <workspace>
- [ ] 5. Synthesize → report.md
```

**Step 2** comes first and alone: follow [references/entity-resolution.md](references/entity-resolution.md). Every module depends on its legal names, status, and same-name list.

**Step 3:** run the modules below, reading each reference first, even when step 2 already found the headline (an acquisition, a layoff); the headline is where the research starts. Each writes findings in the format of [assets/finding.schema.json](assets/finding.schema.json):

| Module | Reference | Covers |
|---|---|---|
| `capital` | [references/capital.md](references/capital.md) | Rounds, investors, valuations, revenue claims, acquisition terms |
| `talent-flow` | [references/talent-flow.md](references/talent-flow.md) | Headcount over time, layoffs, leadership changes, open roles, work model |
| `records-sweep` | [references/records-sweep.md](references/records-sweep.md) | WARN notices, courts, labor, regulators, breaches |
| `news-people-sentiment` | [references/news-people-sentiment.md](references/news-people-sentiment.md) | Timeline, positioning, founders and leaders, sentiment, product and technology, backchannel candidates |
| `browser-sources` | [references/browser-sources.md](references/browser-sources.md) | The browser sources the user picked, and pages the other modules could not open |

Each module works from `entity.json` and writes its own file, so they can run in any order or at once. Run `browser-sources` only if the user opted in; it is the only module that uses the browser, and it opens the other modules' blocked pages once they finish.

**Search is a shared, limited budget.** Fetch known URLs and APIs directly instead of searching for them, run must-do checks first, and stop a line of inquiry once it stops producing new primary sources. When search runs out, use https://news.google.com/rss/search?q=<query> and https://hn.algolia.com/api/v1/search?query=<query>; if the fetch tool refuses a site (web.archive.org, some APIs), try `curl`.

**Step 4:** fix everything the validator reports. Without script execution, check the files against the evidence rules by hand.

**Step 5:** follow [references/synthesis.md](references/synthesis.md) and [assets/report-template.md](assets/report-template.md). If you cannot write `report.md`, return the report as text. End with the bottom line, the flags, and the report's full path. If your environment can publish a private page or document, publish the report there too and give the link.

## Scripts

Standard-library Python 3, all optional; modules give the fallback.

- `scripts/job_boards.py <slug> …`: open roles from Ashby, Greenhouse, and Lever, with identity hints.
- `scripts/validate_findings.py <workspace>`: checks `entity.json` and findings against the evidence rules.

## Gotchas

- **Same-name companies contaminate everything**: aggregators, review sites, and job-board slugs. Tie every third-party fact to the anchor domain or legal name.
- **Many sites block fetching** (Glassdoor, Business Insider, Forbes, Crunchbase, PitchBook). Use search snippets, and log the page as `blocked` for `browser-sources`.
- **The user may already be connected to the company** (an employee, contributor, or author). If you notice this, mention it once in your reply, never in the report, and leave them out of the research.
