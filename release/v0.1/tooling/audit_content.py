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
DECISION_PATTERN = re.compile(r"\bDEC-[0-9]{4}\b")
DEFINITION_PATTERN = re.compile(r"\bDEF-[0-9]{4}\b")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:do uzupełnienia|treść zostanie uzupełniona|zostanie uzupełnione|lorem ipsum)\b",
    re.IGNORECASE,
)
MONEY_OR_RATIO_PATTERN = re.compile(
    r"(?:\b\d+(?:[.,]\d+)?\s*(?:%|mln|mld|PLN|EUR|zł|euro)\b)",
    re.IGNORECASE,
)
SCENARIO_MARKERS = (
    "SCENARIUSZ",
    "REKOMENDACJA",
    "PROPOZYCJA",
    "HIPOTEZA",
    "INFERENCE",
    "HYPOTHESIS",
    "RECOMMENDATION",
    "UNKNOWN",
)
CAUSAL_PATTERN = re.compile(
    r"(?:najszybsz\w*\s+efekt|motor\s+produktywno(?:ści|sci)|"
    r"fastest\s+(?:effect|impact)|early\s+impact\s+will\s+come|"
    r"drives?\s+productivity)",
    re.IGNORECASE,
)


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


def check_raci_sections(errors: list[str]) -> None:
    sections = {
        "documents/core/governance-law.md": "## 4. Funkcjonalny RACI",
        "documents/core/implementation-roadmap.md": "## 8. RACI i odpowiedzialność",
        "documents/briefs/ministerial-briefs.md": "## 9. Macierz zależności resortowych",
    }
    role_pattern = re.compile(r"^(?:A|R|C|I)(?:/(?:A|R|C|I))*$")
    for relative_path, heading in sections.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if heading not in text:
            errors.append(f"{relative_path}: missing controlled RACI section")
            continue
        section = text.split(heading, 1)[1].split("\n## ", 1)[0]
        for line_number, line in enumerate(section.splitlines(), start=1):
            if not line.startswith("|") or re.match(r"^\|[-: |]+\|$", line):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            role_cells = [cell for cell in cells[1:] if role_pattern.fullmatch(cell)]
            if not role_cells:
                continue
            accountable = sum("A" in cell.split("/") for cell in role_cells)
            if accountable != 1:
                errors.append(
                    f"{relative_path}:{heading}: RACI row '{cells[0]}' has "
                    f"{accountable} accountable cells; expected exactly one"
                )

    governance = (ROOT / "documents/core/governance-law.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "documents/core/implementation-roadmap.md").read_text(encoding="utf-8")
    if "| protokół testu | I | C | I | R | A/R | C | C |" not in governance:
        errors.append("governance-law: controlled owner for test protocol changed")
    if "| protokół testu | I | C | A | R | I | C | C |" not in roadmap:
        errors.append("implementation-roadmap: test protocol owner conflicts with governance")


def check_hard_gates_and_competence(errors: list[str]) -> None:
    pilot = (ROOT / "documents/templates/regional-pilot-card.md").read_text(
        encoding="utf-8"
    )
    province = (ROOT / "documents/templates/voivodeship-data-template.md").read_text(
        encoding="utf-8"
    )
    president = (ROOT / "documents/briefs/president-bbn.md").read_text(encoding="utf-8")
    if "Wyjątek może zatwierdzić" in pilot:
        errors.append("regional-pilot-card: hard PASS/FAIL gate contains a waiver")
    if "Nie ma wyjątku pozwalającego ominąć bramkę" not in pilot:
        errors.append("regional-pilot-card: non-waivable hard-gate rule is missing")
    if "każdy rezultat w RACI ma dokładnie jedno uzupełnione `A`" not in province:
        errors.append("voivodeship-data-template: final QA lacks one-A RACI control")
    if "Prezydent i BBN powinni rekomendować" in president:
        errors.append("president-bbn-brief: BBN is presented as a co-decision-maker")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    claims = {
        record["id"]: record
        for record in load_yaml(ROOT / "research" / "claims.yaml").get("claims", [])
    }
    decisions = {
        record["id"]: record
        for record in load_yaml(ROOT / "research" / "decisions.yaml").get("decisions", [])
    }
    definitions = {
        record["id"]: record
        for record in load_yaml(ROOT / "research" / "definitions.yaml").get("definitions", [])
    }
    sources = load_yaml(ROOT / "research" / "sources.yaml").get("sources", [])
    registered_urls = {record["url"].rstrip("/") for record in sources}
    artifacts = load_yaml(ROOT / "documents" / "manifest.yaml").get("artifacts", [])

    check_raci_sections(errors)
    check_hard_gates_and_competence(errors)

    for artifact in artifacts:
        path = ROOT / artifact["source"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        artifact_id = artifact["id"]

        if (
            artifact.get("language") == "en"
            and "assets/generated/delivery-cycle.svg" in text
        ):
            errors.append(
                f"{artifact_id}: English artifact references the Polish delivery-cycle asset"
            )

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

        for decision_id in sorted(set(DECISION_PATTERN.findall(text))):
            if decision_id not in decisions:
                errors.append(f"{artifact_id}: references missing {decision_id}")

        for definition_id in sorted(set(DEFINITION_PATTERN.findall(text))):
            if definition_id not in definitions:
                errors.append(f"{artifact_id}: references missing {definition_id}")

        for url in LINK_PATTERN.findall(text):
            normalized = url.rstrip("/")
            if normalized not in registered_urls:
                errors.append(f"{artifact_id}: external link is not registered: {url}")

        for line_number, line in enumerate(text.splitlines(), start=1):
            if MONEY_OR_RATIO_PATTERN.search(line):
                has_claim = bool(CLAIM_PATTERN.search(line))
                labelled = any(marker in line.upper() for marker in SCENARIO_MARKERS)
                if not has_claim and not labelled:
                    message = (
                        f"{artifact_id}:{line_number}: amount or ratio lacks "
                        "CLM id/scenario label"
                    )
                    if artifact["status"] in {"reviewed", "release-candidate"}:
                        errors.append(message)
                    else:
                        warnings.append(message)
            if CAUSAL_PATTERN.search(line):
                labelled = any(marker in line.upper() for marker in SCENARIO_MARKERS)
                if not labelled:
                    message = (
                        f"{artifact_id}:{line_number}: strong causal wording lacks "
                        "an inference/hypothesis/recommendation label"
                    )
                    if artifact["status"] in {"reviewed", "release-candidate"}:
                        errors.append(message)
                    else:
                        warnings.append(message)

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
