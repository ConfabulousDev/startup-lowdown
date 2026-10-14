#!/usr/bin/env python3
"""Summarize a company's open roles from public applicant-tracking-system job boards.

Usage:
    python3 scripts/job_boards.py <board-slug> [<board-slug> ...]

Tries each slug on Ashby, Greenhouse, and Lever, whose public job-board APIs
need no login. Slugs are usually the company name as it appears in job URLs
(jobs.ashbyhq.com/<slug>, job-boards.greenhouse.io/<slug>, jobs.lever.co/<slug>).

Output: JSON on stdout with, per board found, the open-role count broken down
by department, location, and workplace type, posting dates, titles, and
identity hints. Slugs are not unique to a company: different companies with
the same name can own the same slug on different boards, so check the
identity hints against the company before using a board. Standard library only.
"""

import html
import json
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone

BOARDS = {
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}",
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
}
USER_AGENT = "startup-lowdown/0.1 (+https://github.com/ConfabulousDev/startup-lowdown)"
# Enough of a job description to recognize which company wrote it.
EXCERPT_CHARS = 300


def fetch_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def plain(markup):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(markup or ""))).strip()


def from_ashby(data):
    for job in data.get("jobs", []):
        if job.get("isListed") is False:
            continue
        yield {
            "title": job.get("title"),
            "department": job.get("department") or job.get("team"),
            "location": job.get("location"),
            "workplace": job.get("workplaceType") or ("Remote" if job.get("isRemote") else None),
            "posted": (job.get("publishedAt") or "")[:10] or None,
            "url": job.get("jobUrl"),
            "company_name": None,
            "text": job.get("descriptionPlain"),
        }


def from_greenhouse(data):
    for job in data.get("jobs", []):
        departments = job.get("departments") or [{}]
        yield {
            "title": job.get("title"),
            "department": departments[0].get("name"),
            "location": (job.get("location") or {}).get("name"),
            "workplace": None,
            "posted": (job.get("first_published") or job.get("updated_at") or "")[:10] or None,
            "url": job.get("absolute_url"),
            "company_name": job.get("company_name"),
            "text": plain(job.get("content")),
        }


def from_lever(data):
    for job in data:
        categories = job.get("categories") or {}
        created = job.get("createdAt")
        yield {
            "title": job.get("text"),
            "department": categories.get("department") or categories.get("team"),
            "location": categories.get("location"),
            "workplace": job.get("workplaceType"),
            "posted": datetime.fromtimestamp(created / 1000, timezone.utc).date().isoformat() if created else None,
            "url": job.get("hostedUrl"),
            "company_name": None,
            "text": job.get("descriptionPlain"),
        }


PARSERS = {"ashby": from_ashby, "greenhouse": from_greenhouse, "lever": from_lever}


def summarize(board, slug, jobs):
    dates = sorted(j["posted"] for j in jobs if j["posted"])
    return {
        "board": board,
        "slug": slug,
        "url": BOARDS[board].format(slug=slug),
        "open_roles": len(jobs),
        "by_department": Counter(j["department"] or "unspecified" for j in jobs).most_common(),
        "by_location": Counter(j["location"] or "unspecified" for j in jobs).most_common(),
        "by_workplace": Counter(j["workplace"] or "unspecified" for j in jobs).most_common(),
        "oldest_posting": dates[0] if dates else None,
        "newest_posting": dates[-1] if dates else None,
        "titles": sorted(j["title"] for j in jobs if j["title"]),
        "identity_hints": {
            "company_name": next((j["company_name"] for j in jobs if j["company_name"]), None),
            "sample_job_url": jobs[0]["url"] if jobs else None,
            "sample_description": (jobs[0]["text"] or "")[:EXCERPT_CHARS] if jobs else None,
        },
    }


def main():
    slugs = sys.argv[1:]
    if not slugs:
        print("Usage: job_boards.py <board-slug> [<board-slug> ...]", file=sys.stderr)
        sys.exit(2)
    found, tried = [], []
    for slug in slugs:
        for board, template in BOARDS.items():
            url = template.format(slug=slug)
            try:
                data = fetch_json(url)
            except (urllib.error.URLError, json.JSONDecodeError) as e:
                tried.append({"board": board, "slug": slug, "status": f"error: {e}"})
                continue
            if data is None or (board == "greenhouse" and not data.get("jobs") and not data.get("meta")):
                tried.append({"board": board, "slug": slug, "status": "not_found"})
                continue
            found.append(summarize(board, slug, list(PARSERS[board](data))))
            tried.append({"board": board, "slug": slug, "status": "ok"})
    json.dump({"boards": found, "tried": tried}, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
