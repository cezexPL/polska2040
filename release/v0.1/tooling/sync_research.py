#!/usr/bin/env python3
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "research" / "packs"


def normalize_scalars(value):
    """Keep YAML dates JSON-Schema friendly and deterministic."""
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return [normalize_scalars(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_scalars(item) for key, item in value.items()}
    return value


def load_records(path: Path, key: str) -> list[dict]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records = data.get(key, [])
    if not isinstance(records, list):
        raise ValueError(f"{path}: {key} must be a list")
    return normalize_scalars(records)


def complete_pack_prefixes() -> set[str]:
    """Only import packs explicitly accepted by the coordinator.

    Agents write several files in parallel. The coordinator creates a
    ``<prefix>.complete`` marker only after receiving the final handoff and
    reviewing that both required registries exist. This prevents a sync from
    ingesting a structurally valid but unfinished pack.
    """
    source_prefixes = {
        path.name.removesuffix("-sources.yaml") for path in PACKS.glob("*-sources.yaml")
    }
    claim_prefixes = {
        path.name.removesuffix("-claims.yaml") for path in PACKS.glob("*-claims.yaml")
    }
    accepted_prefixes = {
        path.name.removesuffix(".complete") for path in PACKS.glob("*.complete")
    }
    return source_prefixes & claim_prefixes & accepted_prefixes


def merge(kind: str, key: str, eligible_prefixes: set[str]):
    destination = ROOT / "research" / f"{kind}.yaml"
    by_id: dict[str, dict] = {}
    for pack in sorted(PACKS.glob(f"*-{kind}.yaml")):
        prefix = pack.name.removesuffix(f"-{kind}.yaml")
        if prefix not in eligible_prefixes:
            continue
        for record in load_records(pack, key):
            record_id = record["id"]
            if record_id in by_id and by_id[record_id] != record:
                raise ValueError(f"Conflicting record {record_id} in {pack}")
            by_id[record_id] = record
    ordered = [by_id[record_id] for record_id in sorted(by_id)]
    destination.write_text(
        yaml.safe_dump({"schema_version": 1, key: ordered}, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )
    print(f"Synced {len(ordered)} {key} -> {destination.relative_to(ROOT)}")


def main():
    PACKS.mkdir(parents=True, exist_ok=True)
    eligible_prefixes = complete_pack_prefixes()
    print(f"Complete research packs: {', '.join(sorted(eligible_prefixes)) or 'none'}")
    merge("sources", "sources", eligible_prefixes)
    merge("claims", "claims", eligible_prefixes)
    merge("contradictions", "contradictions", eligible_prefixes)


if __name__ == "__main__":
    main()
