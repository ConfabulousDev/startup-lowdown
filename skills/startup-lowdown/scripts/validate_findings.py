#!/usr/bin/env python3
"""Validate a startup-lowdown workspace: entity.json and findings/*.json.

Usage:
    python3 scripts/validate_findings.py <workspace-dir>

Checks the rules in assets/finding.schema.json and references/evidence-rules.md
that matter most, with messages that say how to fix each problem. Exit code 0
means valid. Standard library only.
"""

import json
import re
import sys
from pathlib import Path

DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
FULL_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FINDING_ID = re.compile(r"^[a-z0-9-]+:\d{3}$")
TOPIC = re.compile(r"^[a-z0-9_]+$")
NUMBER = re.compile(r"\d[\d,.]*")
DATE_IN_TEXT = re.compile(r"\b\d{4}-\d{2}(-\d{2})?\b")
YEAR = re.compile(r"^(19|20)\d{2}$")
EVIDENCE = {"fact", "reported", "claimed", "inferred"}
CONFIDENCE = {"high", "medium", "low"}
POLARITY = {"positive", "neutral", "negative"}
COVERAGE_STATUS = {"ok", "partial", "blocked", "not_found", "skipped"}
ENTITY_REQUIRED = ["name", "domain", "legal_names", "founders", "status", "same_name_entities"]
FINDINGS_REQUIRED = ["module", "company", "generated_at", "coverage", "findings"]
FINDING_REQUIRED = ["id", "topic", "claim", "as_of", "evidence", "confidence", "polarity", "sources"]
MAX_QUOTE_CHARS = 300


def check_entity(path, errors):
    try:
        entity = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"{path}: cannot read JSON ({e})")
        return
    for key in ENTITY_REQUIRED:
        if key not in entity:
            errors.append(f"{path}: missing '{key}'. See references/entity-resolution.md.")
    if not entity.get("legal_names"):
        errors.append(f"{path}: 'legal_names' is empty. Look in the privacy policy, terms, site footer, "
                      f"or press page; if truly not found, record [\"unknown\"] and say where you looked.")


def check_source(where, source, errors):
    if not isinstance(source, dict):
        errors.append(f"{where}: each source must be an object with 'url' and 'accessed'.")
        return
    if not source.get("url"):
        errors.append(f"{where}: source missing 'url'.")
    if not FULL_DATE.match(str(source.get("accessed", ""))):
        errors.append(f"{where}: source 'accessed' must be YYYY-MM-DD.")
    if source.get("published") and not DATE.match(str(source["published"])):
        errors.append(f"{where}: source 'published' must be YYYY, YYYY-MM, or YYYY-MM-DD.")
    if len(source.get("quote", "")) > MAX_QUOTE_CHARS:
        errors.append(f"{where}: quote longer than {MAX_QUOTE_CHARS} characters; shorten it.")


def claim_numbers(claim):
    """Numbers stated in a claim, ignoring dates, bare years, and zero, with commas removed."""
    text = DATE_IN_TEXT.sub(" ", claim)
    numbers = {n.strip(".,").replace(",", "") for n in NUMBER.findall(text)}
    return {n for n in numbers if n and n != "0" and not YEAR.match(n)}


def check_finding(where, f, ids, errors):
    for key in FINDING_REQUIRED:
        if key not in f:
            errors.append(f"{where}: missing '{key}'.")
    if not FINDING_ID.match(str(f.get("id", ""))):
        errors.append(f"{where}: id must look like '<module>:001'.")
    elif f["id"] in ids:
        errors.append(f"{where}: duplicate id {f['id']}.")
    ids.add(f.get("id"))
    if not TOPIC.match(str(f.get("topic", ""))):
        errors.append(f"{where}: topic must be lowercase_with_underscores.")
    if not DATE.match(str(f.get("as_of", ""))):
        errors.append(f"{where}: as_of must be YYYY, YYYY-MM, or YYYY-MM-DD (when the claim was true, not today).")
    evidence = f.get("evidence")
    if evidence not in EVIDENCE:
        errors.append(f"{where}: evidence must be one of {sorted(EVIDENCE)}.")
    if f.get("confidence") not in CONFIDENCE:
        errors.append(f"{where}: confidence must be one of {sorted(CONFIDENCE)}.")
    if f.get("polarity") not in POLARITY:
        errors.append(f"{where}: polarity must be one of {sorted(POLARITY)}.")
    sources = f.get("sources", [])
    if not isinstance(sources, list):
        errors.append(f"{where}: sources must be a list.")
        sources = []
    for i, source in enumerate(sources):
        check_source(f"{where} source[{i}]", source, errors)
    if evidence in {"fact", "reported", "claimed"} and not sources:
        errors.append(f"{where}: '{evidence}' needs at least one source. Add one or reclassify.")
    if evidence == "inferred" and not (f.get("derived_from") and f.get("reasoning")):
        errors.append(f"{where}: 'inferred' needs 'derived_from' (finding ids) and 'reasoning'.")
    numbers = claim_numbers(str(f.get("claim", "")))
    if evidence in {"fact", "reported", "claimed"} and numbers:
        quotes = " ".join(s.get("quote", "") for s in sources if isinstance(s, dict)).replace(",", "")
        if not any(n in quotes for n in numbers):
            errors.append(f"{where}: the claim states {sorted(numbers)} but no source quote contains any of them. "
                          f"Quote the passage that states the number, or make the finding 'inferred'.")
    if f.get("polarity") == "negative" and f.get("people") and evidence == "inferred":
        errors.append(f"{where}: negative claim about {f['people']} rests on inference. "
                      f"Cite a source or drop it (evidence-rules.md, People).")
    return f.get("derived_from", [])


def check_findings_file(path, ids, references, errors):
    try:
        doc = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"{path}: cannot read JSON ({e})")
        return
    for key in FINDINGS_REQUIRED:
        if key not in doc:
            errors.append(f"{path}: missing '{key}'.")
    if doc.get("module") and doc["module"] != path.stem:
        errors.append(f"{path}: module '{doc['module']}' does not match file name '{path.stem}'.")
    coverage = doc.get("coverage", [])
    if not coverage:
        errors.append(f"{path}: 'coverage' is empty. Record every source tried, including failures.")
    for i, entry in enumerate(coverage):
        if entry.get("status") not in COVERAGE_STATUS:
            errors.append(f"{path} coverage[{i}]: status must be one of {sorted(COVERAGE_STATUS)}.")
    for i, finding in enumerate(doc.get("findings", [])):
        where = f"{path.name} {finding.get('id', f'findings[{i}]')}"
        for ref in check_finding(where, finding, ids, errors):
            references.append((where, ref))


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_findings.py <workspace-dir>", file=sys.stderr)
        sys.exit(2)
    workspace = Path(sys.argv[1])
    errors = []
    entity = workspace / "entity.json"
    if entity.exists():
        check_entity(entity, errors)
    else:
        errors.append(f"{entity}: missing. Run entity resolution first.")
    files = sorted((workspace / "findings").glob("*.json"))
    if not files:
        errors.append(f"{workspace / 'findings'}: no findings files.")
    ids, references = set(), []
    for path in files:
        check_findings_file(path, ids, references, errors)
    for where, ref in references:
        if ref not in ids:
            errors.append(f"{where}: derived_from refers to unknown finding {ref}.")
    if errors:
        print(f"{len(errors)} problem(s):")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print(f"OK: entity.json and {len(files)} findings file(s), {len(ids)} findings.")


if __name__ == "__main__":
    main()
