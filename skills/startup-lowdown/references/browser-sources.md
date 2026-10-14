# Browser sources

Answer: what do the sources the user opened to you in their browser add? Run this module only if the user opted in.

Use whatever browser tool you have. It acts as the user, in their logged-in sessions, so follow the access rules in `references/evidence-rules.md` strictly. The user signed in and cleared human checks at the start; if a source still shows a login page, CAPTCHA, unusual-activity warning, or rate limit, stop that source, log it as `blocked`, and move on without asking. When done, close the tabs you opened and disconnect from the browser if your tool can.

## Must-do checks

1. **Each source the user picked**, as below. Use only those sources; log the rest as `skipped`.
2. **Pages other modules could not open:** once they finish, every `blocked` URL in their `coverage`. Record what each page says as new findings, which replace the snippet-based ones.

## LinkedIn

- **Company page:** size band, headquarters, and recent posts (launches, hires, layoffs).
- **People tab:** the employee count on LinkedIn, and its breakdown by function and by location. Insights (headcount over time, attrition) if the account shows them.
- **Turnover:** People search filtered to past employees: how many, from which functions, when they left, and where they went.
- **Profiles:** only if the user agreed. They give tenure, prior roles, and moves. Open the founders', the leaders', and those of past and current employees in the user's area, up to about 20, so the report can state how long people stay and where they go. Name only the people `references/evidence-rules.md` puts in scope; count the rest.

## Glassdoor

Confirm the page is this company. Overall rating, review count, CEO approval, and how the rating moved over the last two years. Read the reviews from the last 12 months; summarize recurring themes, with dates.

## Crunchbase

Rounds, investors, valuations, and headcount history. It is an aggregator: use it to corroborate and to find leads for primary sources.

## Caplight, Forge, EquityZen, or Hiive

Recent prices for the company's shares and their trend against the last round's price. They mark what the market thinks the company is worth, not the value of the user's equity.

## Similarweb

Website traffic over the last two years and its trend, beside the competitors other modules named.

## Paywalled news

Open the original articles behind snippets or blocked pages that other modules relied on, especially for layoffs, exits, and funding.

## X

Posts by founders and executives from the last 12 months, and search for the company with "laid off", "left", or "joined", for departures and layoffs.

## Reddit, Indeed, Wellfound, and other sites

Reddit threads about working there; Indeed reviews; the Wellfound profile's team and funding. For any other site the user named, take what bears on the company's prospects, people, or sentiment.
