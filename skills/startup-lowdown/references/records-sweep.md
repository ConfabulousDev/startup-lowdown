# Records sweep

Answer: what do public records show that press might not? This module makes "no bad news" mean "looked and found nothing".

Search every legal and former name, plus the brand, and the acquirer if acquired. Prefer the direct URLs below over web search.

## Must-do checks

```
- [ ] WARN notices in HQ and major-office states. California: edd.ca.gov WARN reports (xlsx/pdf). Others: state labor sites, warntracker.com.
- [ ] Courts: https://www.courtlistener.com/api/rest/v4/search/?q="<legal name>" (type=r for dockets)
- [ ] Labor: https://www.nlrb.gov/search/case/<name>
- [ ] Breaches: California AG list (oag.ca.gov/privacy/databreach/list) and "<company> breach"
- [ ] Regulators: "<legal name>" with FTC, "attorney general", "consent order", "settlement"
```

## Reading results

- A WARN notice covers one site above a size threshold, so it usually undercounts; report it and the company-wide total separately.
- For a court case, record type, filing date, status, and parties, from the docket itself. A case that names the company only in passing (for example, a suit against a customer) is a different finding from one against the company.
- Patent suits from non-practicing entities are routine. Employment, wage, discrimination, consumer, and securities suits matter more; patterns matter most.
- Report what was filed and how it ended; do not judge the merits.
