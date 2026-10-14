# Synthesis

Turn `entity.json` and `findings/*.json` into the report. Work from these files, not raw pages, and add no facts while writing: if something is missing, record a finding first.

## Steps

1. **Reconcile modules.** Where findings disagree, use the better-sourced one. If one module found an event another logged as not found, the finding wins; fix the coverage note.
2. **Estimate runway** as an `inferred` range, unless the company has stated its cash position or profitability:
   - cash: equity raised in the last two priced rounds, plus debt if known;
   - burn: headcount times $200K–$300K fully loaded per US employee (adjust for non-US teams);
   - revenue: chain the dated revenue claims (a base figure times later growth multiples) and subtract it from burn; with no base figure or conflicting claims, give a high and a low scenario and say which the company's hiring behavior supports.
   Report months remaining as a range, plus months since the last raise. If acquired, skip runway and assess the parent instead.
3. **Flag** material findings red, yellow, or green, and explain each:
   - **Red:** co-founder departures, layoffs in the last 12 months, a down round or a sale well below the last valuation, runway under 12 months, several employment suits, a collapse in openings or headcount.
   - **Yellow:** over 24 months since the last raise without a profitability claim, executive turnover, pivots, unverifiable growth claims, thin or mixed sentiment, a recent acquisition.
   - **Green:** verified growth, a recent raise from strong investors, stable leadership, consistently positive sentiment, a strong product or technology.
   A flag about an event (lawsuit, layoff, departure) needs a source you actually opened, not just a snippet.
4. **Skeptic pass.** For each flag, ask what would overturn it and whether that was checked. Downgrade anything resting on one source, a third-party estimate, or a profile that may be a same-name company.
5. **Next steps.** Pick the five questions whose answers would most change the user's decision, each tied to a flag or gap and marked 🤝 friendly (safe with a recruiter or any interviewer) or 🎯 direct (for founders, a late round, or a backchannel). If a check is one you could run yourself (LinkedIn, GitHub, reading the founders' posts), run it, record a finding, and report the result; leave to the user only what needs their own network or conversations. Ask about a sensitive finding without citing it: "how do the founders handle disagreement?" probes a harsh review without quoting it. Nothing about pay, equity, work model, or the duties of the user's job.
6. **Write** the report from `assets/report-template.md`.

## Style

Write emphatically, precisely, and concisely: state each conclusion plainly and once, with exact figures and dates, and cut every word that adds nothing. A reader should get the picture in five minutes, reading top to bottom, without needing anything outside the report. Lead with the bottom line; put detail in tables. Headlines, flags, and questions claim no more than the evidence beneath them.

Show answers, not the research process:

- Filter same-name companies silently. Never mention them or figures you discarded.
- Translate raw metrics into what they mean: "reached the Hacker News front page", not "550 points"; "two engineers carry most of the code", not commit counts.
- Give business color (why the rename, why the pivot), not technical minutiae such as security advisories or release notes.
- Blocked sources and gaps go in the addendum, named as sources, never as tools or scripts.
- Cite each sentence with the source URLs of the findings it uses, never finding ids or module names.