"""Check that every JSON manifest parses and that all versions match SKILL.md.

Run from the repository root. Exits non-zero with one line per problem.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "startup-lowdown" / "SKILL.md"


def skill_version():
    front = SKILL.read_text().split("---")[1]
    match = re.search(r'^\s+version:\s*"?([^"\n]+)"?\s*$', front, re.M)
    return match.group(1) if match else None


def versions(node, path=""):
    """Yield (json path, value) for every "version" key in a manifest."""
    if isinstance(node, dict):
        for key, value in node.items():
            where = f"{path}.{key}" if path else key
            if key == "version" and isinstance(value, str):
                yield where, value
            else:
                yield from versions(value, where)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from versions(item, f"{path}[{i}]")


def main():
    problems = []
    expected = skill_version()
    if not expected:
        problems.append(f"{SKILL.relative_to(ROOT)}: no metadata.version")
    manifests = [p for p in ROOT.rglob("*.json")
                 if ".git" not in p.parts and "skills" not in p.parts]
    for manifest in sorted(manifests):
        name = manifest.relative_to(ROOT)
        try:
            data = json.loads(manifest.read_text())
        except json.JSONDecodeError as err:
            problems.append(f"{name}: invalid JSON: {err}")
            continue
        for where, value in versions(data):
            if expected and value != expected:
                problems.append(f"{name}: {where} is {value}, SKILL.md says {expected}")
    for problem in problems:
        print(problem)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
