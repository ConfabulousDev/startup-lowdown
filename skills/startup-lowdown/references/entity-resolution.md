# Entity resolution

Pin down exactly which company this is before any module runs. Output: `entity.json` (shape below).

## Steps

1. **Anchor on the domain.** Every other identifier must tie back to it.
2. **Find the legal name(s)** that records use: privacy policy and terms ("operated by …"), footer copyright, press page, job-posting EEO text. Record former names and why the name changed.
3. **Find founders and current leadership** from the company's own about, team, and author pages, then press. Note anyone in early coverage but missing now.
4. **Run the high-stakes searches now**, since acquisitions, exits, and layoffs can be days old: "<company>" with "acquired", "layoffs", "lawsuit", and "CEO", plus each founder's name. Record what they turn up in `early_signals` and set `status`, then move on: following up is the modules' job. If acquired, also record:
   - who runs it now: check the CEO's and CTO's own posts and the newsroom for exits and successors;
   - what was actually bought: read the deal filing or announcement in full; units carved out before the sale are not part of the company;
   - the acquirer's name, which later modules search too.
5. **List same-name entities**, only with evidence they are distinct companies (different domain, founders, or city). A misreported figure about this company is a source conflict, not a new entity.
6. **Locate profiles** (YC, LinkedIn, GitHub, job board) and confirm each points at the anchor domain.
7. **Check the user's premises** ("it's YC-backed") and record the result.

## entity.json

```json
{
  "name": "Lumen",
  "domain": "lumen.example",
  "legal_names": ["Brightfold Labs, Inc."],
  "former_names": ["Brightfold"],
  "hq_city": "Seattle, WA",
  "founded": "2021",
  "founders": [{"name": "…", "role": "CEO", "source": "https://…"}],
  "leadership": [{"name": "…", "role": "…", "source": "https://…"}],
  "status": "acquired",
  "parent": {"name": "…", "closed": "2026-05", "scope": "all of Lumen except its Atlas product", "source": "https://…"},
  "profiles": {"linkedin": "https://…", "github": "https://…", "jobs": "https://…"},
  "same_name_entities": [
    {"name": "Lumen Health, Inc.", "domain": "lumenhealth.example", "distinguishing": "Denver telehealth company; different founders"}
  ],
  "early_signals": [{"date": "2026-04", "signal": "TechCrunch: 15% layoff", "source": "https://…"}],
  "premise_checks": [{"premise": "YC-backed", "result": "not in YC directory", "source": "https://…"}],
  "sources_checked": ["privacy policy", "footer", "about page"]
}
```

`status` is `independent`, `acquired`, `public`, or `defunct`. If no legal name is found, use `["unknown"]` and list where you looked.
