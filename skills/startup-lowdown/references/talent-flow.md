# Talent flow

Answer: is the company growing or shrinking, what is it hiring for, and where and how do people work?

## Must-do checks

1. **Job boards.** Find the board from the careers page links and run `scripts/job_boards.py <slug>`, or open the board directly. Also check YC's Work at a Startup and the lead investors' job boards. Discard any board whose `identity_hints` do not match `entity.json`; slugs are shared across same-name companies. If acquired, check the acquirer's board too.
2. **Headcount history** from the company's own statements, current and archived. List archived copies of the about and careers pages with `https://web.archive.org/cdx/search/cdx?url=<domain>/about&output=json&fl=timestamp&collapse=timestamp:6` and open `https://web.archive.org/web/<timestamp>/<url>`.
3. **Layoffs and leadership changes:** search "<company> layoffs" and the names of departed or new executives. Check the person's own posts and the company newsroom before calling a change unconfirmed. An executive gone within a year of joining is material.

## Headcount

Build a dated series and state the trend. Rank sources: company statements; figures implied by reported layoffs (`inferred`); YC or LinkedIn counts; aggregators (Revelio, TrueUp, Tracxn, Owler) only to corroborate, since they often merge same-name companies.

## Open roles

Report total roles, mix by function (the user's area in detail, if given), locations, and workplace type, and compare with an archived snapshot if one exists. A collapse in openings is a strong signal; long-open or reposted roles are a weak one. Before saying no role of a type is open, check every board above.

## Work model

Office cities, remote or hybrid policy, and in-office days, from postings and any return-to-office news.
