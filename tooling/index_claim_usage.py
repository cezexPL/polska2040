#!/usr/bin/env python3
"""Build a deterministic claim-to-artifact traceability index."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CLAIM_PATTERN = re.compile(r"\bCLM-[0-9]{4}\b")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> None:
    claims = {
        claim["id"]: claim
        for claim in load_yaml(ROOT / "research" / "claims.yaml").get("claims", [])
    }
    artifacts = load_yaml(ROOT / "documents" / "manifest.yaml").get("artifacts", [])
    found: dict[str, dict[str, set[str]]] = {
        claim_id: {"artifact_ids": set(), "source_paths": set()}
        for claim_id in claims
    }

    for artifact in artifacts:
        path = ROOT / artifact["source"]
        if not path.exists():
            continue
        for claim_id in set(CLAIM_PATTERN.findall(path.read_text(encoding="utf-8"))):
            if claim_id not in found:
                continue
            found[claim_id]["artifact_ids"].add(artifact["id"])
            found[claim_id]["source_paths"].add(artifact["source"])

    usages = []
    for claim_id in sorted(claims):
        artifact_ids = sorted(found[claim_id]["artifact_ids"])
        source_paths = sorted(found[claim_id]["source_paths"])
        usages.append(
            {
                "id": claim_id,
                "status": claims[claim_id]["status"],
                "artifact_ids": artifact_ids,
                "source_paths": source_paths,
            }
        )

    destination = ROOT / "research" / "claim-usage.yaml"
    destination.write_text(
        yaml.safe_dump(
            {"schema_version": 1, "usages": usages},
            allow_unicode=True,
            sort_keys=False,
            width=120,
        ),
        encoding="utf-8",
    )
    used = sum(bool(record["artifact_ids"]) for record in usages)
    print(f"Indexed {used}/{len(usages)} claims used in publication artifacts.")


if __name__ == "__main__":
    main()
