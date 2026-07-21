#!/usr/bin/env python3
"""Fail-closed checks for claim use and publication completeness.

This is intentionally narrower than editorial review. It catches the classes
of error that are easy to introduce during multi-agent synthesis: references
to missing or unverified claims, unregistered external links, missing executive
summaries, stale placeholders in reviewed artifacts and malformed decks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CLAIM_PATTERN = re.compile(r"\bCLM-[0-9]{4}\b")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:do uzupełnienia|treść zostanie uzupełniona|zostanie uzupełnione|lorem ipsum)\b",
    re.IGNORECASE,
)
MONEY_OR_RATIO_PATTERN = re.compile(
    r"(?:\b\d+(?:[.,]\d+)?\s*(?:%|mln|mld|PLN|EUR|zł|euro)\b)",
    re.IGNORECASE,
)
SCENARIO_MARKERS = ("SCENARIUSZ", "REKOMENDACJA", "PROPOZYCJA", "UNKNOWN")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def slide_count(text: str) -> int:
    return len([part for part in re.split(r"\n---\s*\n", text) if part.strip()])


def expected_slide_range(target: str | None) -> tuple[int, int] | None:
    if not target:
        return None
    numbers = [int(item) for item in re.findall(r"\d+", target)]
    if not numbers:
        return None
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    return min(numbers[0], numbers[1]), max(numbers[0], numbers[1])


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    claims = {
        record["id"]: record
        for record in load_yaml(ROOT / "research" / "claims.yaml").get("claims", [])
    }
    sources = load_yaml(ROOT / "research" / "sources.yaml").get("sources", [])
    registered_urls = {record["url"].rstrip("/") for record in sources}
    artifacts = load_yaml(ROOT / "documents" / "manifest.yaml").get("artifacts", [])

    for artifact in artifacts:
        path = ROOT / artifact["source"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        artifact_id = artifact["id"]

        if artifact["kind"] != "deck" and "Executive Summary" not in text:
            errors.append(f"{artifact_id}: missing visible Executive Summary")

        placeholders = list(PLACEHOLDER_PATTERN.finditer(text))
        if placeholders:
            message = f"{artifact_id}: {len(placeholders)} editorial placeholder(s) remain"
            if artifact["status"] in {"reviewed", "release-candidate"}:
                errors.append(message)
            else:
                warnings.append(message)

        referenced_claims = set(CLAIM_PATTERN.findall(text))
        for claim_id in sorted(referenced_claims):
            claim = claims.get(claim_id)
            if claim is None:
                errors.append(f"{artifact_id}: references missing {claim_id}")
            elif claim["status"] != "verified":
                errors.append(
                    f"{artifact_id}: references {claim_id} with status {claim['status']}"
                )

        for url in LINK_PATTERN.findall(text):
            normalized = url.rstrip("/")
            if normalized not in registered_urls:
                errors.append(f"{artifact_id}: external link is not registered: {url}")

        for line_number, line in enumerate(text.splitlines(), start=1):
            if MONEY_OR_RATIO_PATTERN.search(line):
                has_claim = bool(CLAIM_PATTERN.search(line))
                labelled = any(marker in line.upper() for marker in SCENARIO_MARKERS)
                if not has_claim and not labelled:
                    warnings.append(
                        f"{artifact_id}:{line_number}: amount or ratio lacks CLM id/scenario label"
                    )

        if artifact["kind"] == "deck":
            expected = expected_slide_range(artifact.get("target_length"))
            actual = slide_count(text)
            if expected and not (expected[0] <= actual <= expected[1]):
                warnings.append(
                    f"{artifact_id}: {actual} slides; target is {expected[0]}-{expected[1]}"
                )

    print(
        f"Audited {len(artifacts)} artifacts against {len(claims)} claims and "
        f"{len(registered_urls)} registered source URLs."
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Content audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
