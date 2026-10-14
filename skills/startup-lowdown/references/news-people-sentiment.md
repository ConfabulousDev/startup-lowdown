# News, people, and sentiment

Answer: what has happened recently, who runs the company and with what track record, what does it sell and how well does it work, what do employees say, and whom could the user ask?

## Must-do checks

1. **The company's own pages:** homepage, about, press or newsroom, and blog. Record current positioning in its own words, and date each event from the original post.
2. **Negative news:** start from `early_signals` in `entity.json`, then extend to legal and former names with "fired", "allegations", "breach", "outage", "down round", and to the acquirer if acquired.
3. **Employee sentiment:** try each source below.

## Timeline

Material events from the last 12 months first, then earlier: launches, pivots, renames, partnerships, acquisitions, leadership changes, controversies. Give the business reason where a source states it (why the pivot, why the rename).

## People

- **Founders:** for each one, the company's own bio or author page first, then press. Prior roles, prior companies and their outcomes, education, recognition; verify claimed exits. Summarize what their recent posts and talks say about where they're taking the company. Estimate age from degree years when none is published (`inferred`).
- **Leadership:** current executives, when each started, and anyone who left in the last two years, especially within a year of joining.
- **Leaders of the user's area**, if given: tenure and professional history.

## Employee sentiment

```
- [ ] Glassdoor
- [ ] Indeed reviews
- [ ] Reddit (company name in r/cscareerquestions, r/ExperiencedDevs)
- [ ] Hacker News: https://hn.algolia.com/api/v1/search?query=<company>
```

Confirm each profile is this company, summarize recurring themes, and note how much there is to go on; a few reviews are anecdotes.

## Product and technology

What the company sells, to whom, and evidence that it works: named customers, pricing, usage claims checked against open data (GitHub, PyPI, npm). Engineering practice from the blog, GitHub org, talks, and postings.

If the product is built on an open-source core, assess the project itself: read the README, architecture docs, and a sample of core code; release cadence; who contributes now versus a year ago, and how many are outside the company; issue backlog and responsiveness; license; and what the paid product adds on top. Judge its quality and viability, not just its stars.

## Backchannel candidates

Each with a reason and what to ask them: former employees who left 6–24 months ago, especially from the user's area; current employees in that area; founders in the same investors' portfolios; named customers.
