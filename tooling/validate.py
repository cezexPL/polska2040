#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "research" / "schemas"


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_records(label: str, records: list[dict], schema_name: str, errors: list[str]):
    schema = load_json(SCHEMA_DIR / schema_name)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    seen: set[str] = set()
    for index, record in enumerate(records):
        record_id = record.get("id", f"index-{index}")
        if record_id in seen:
            errors.append(f"{label}: duplicate id {record_id}")
        seen.add(record_id)
        for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path)
            errors.append(f"{label}:{record_id}:{location}: {error.message}")


def check_internal_links(errors: list[str]):
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if clean_target and not (path.parent / clean_target).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")


def check_sensitive_patterns(errors: list[str]):
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "github token": re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
        "openai key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        "password assignment": re.compile(r"(?i)password\s*[:=]\s*[^\s<]{8,}"),
    }
    for path in ROOT.rglob("*"):
        relative_parts = path.relative_to(ROOT).parts
        if (
            not path.is_file()
            or any(part in {".git", ".venv", "dist", "build", "__pycache__"} for part in relative_parts)
            or path.stat().st_size > 2_000_000
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible {label}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    sources = load_yaml(ROOT / "research" / "sources.yaml").get("sources", [])
    claims = load_yaml(ROOT / "research" / "claims.yaml").get("claims", [])
    decisions = load_yaml(ROOT / "research" / "decisions.yaml").get("decisions", [])
    artifacts = load_yaml(ROOT / "documents" / "manifest.yaml").get("artifacts", [])

    validate_records("sources", sources, "source.schema.json", errors)
    validate_records("claims", claims, "claim.schema.json", errors)
    validate_records("decisions", decisions, "decision.schema.json", errors)
    validate_records("artifacts", artifacts, "artifact.schema.json", errors)

    source_ids = {source["id"] for source in sources}
    claim_ids = {claim["id"] for claim in claims}

    for claim in claims:
        missing_sources = set(claim.get("source_ids", [])) - source_ids
        if missing_sources:
            errors.append(f"{claim['id']}: unknown sources {sorted(missing_sources)}")
        if claim.get("status") == "verified":
            if claim.get("type") == "FACT" and not claim.get("source_ids"):
                errors.append(f"{claim['id']}: verified FACT without a source")
            if not claim.get("reviewer"):
                errors.append(f"{claim['id']}: verified claim without reviewer")
            if claim.get("author") == claim.get("reviewer"):
                errors.append(f"{claim['id']}: author cannot review own claim")
        if claim.get("status") != "verified" and claim.get("used_in"):
            warnings.append(f"{claim['id']}: non-verified claim is used in {claim['used_in']}")

    for decision in decisions:
        missing_claims = set(decision.get("evidence_claim_ids", [])) - claim_ids
        if missing_claims:
            errors.append(f"{decision['id']}: unknown claims {sorted(missing_claims)}")

    for artifact in artifacts:
        source_path = ROOT / artifact["source"]
        if not source_path.exists():
            errors.append(f"artifact {artifact['id']}: missing {artifact['source']}")

    check_internal_links(errors)
    check_sensitive_patterns(errors)

    print(f"Validated {len(sources)} sources, {len(claims)} claims, {len(decisions)} decisions and {len(artifacts)} artifacts.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
