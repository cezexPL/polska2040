#!/usr/bin/env python3
"""Generate a human-readable validation summary from canonical registries and QA."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative: str) -> dict:
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8")) or {}


def main() -> int:
    qa_path = ROOT / "dist" / "output-qa.json"
    if not qa_path.exists():
        raise SystemExit("Run make qa before generating the validation report")
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if qa.get("status") != "passed":
        raise SystemExit("Output QA is not passing")

    sources = load_yaml("research/sources.yaml").get("sources", [])
    claims = load_yaml("research/claims.yaml").get("claims", [])
    definitions = load_yaml("research/definitions.yaml").get("definitions", [])
    decisions = load_yaml("research/decisions.yaml").get("decisions", [])
    gaps = load_yaml("research/gaps.yaml").get("gaps", [])
    usages = load_yaml("research/claim-usage.yaml").get("usages", [])
    claim_counts = Counter(record["status"] for record in claims)
    used_claims = [record for record in usages if record.get("artifact_ids")]
    pdf_results = [
        artifact["outputs"]["pdf"]
        for artifact in qa["artifacts"]
        if "pdf" in artifact["outputs"]
    ]
    total_pdf_pages = sum(record.get("pages", 0) for record in pdf_results)
    minimum_page_text_chars = min(
        (record.get("minimum_page_text_chars", 0) for record in pdf_results), default=0
    )
    docx_image_total = sum(
        artifact["outputs"].get("docx", {}).get("images_total", 0)
        for artifact in qa["artifacts"]
    )
    docx_image_alt = sum(
        artifact["outputs"].get("docx", {}).get("images_with_alt", 0)
        for artifact in qa["artifacts"]
    )
    pptx_image_total = sum(
        artifact["outputs"].get("pptx", {}).get("images_total", 0)
        for artifact in qa["artifacts"]
    )
    pptx_image_alt = sum(
        artifact["outputs"].get("pptx", {}).get("images_with_semantic_alt", 0)
        for artifact in qa["artifacts"]
    )

    rows = []
    for artifact in qa["artifacts"]:
        outputs = artifact["outputs"]
        pdf = outputs.get("pdf", {})
        docx = outputs.get("docx", {})
        pptx = outputs.get("pptx", {})
        forms = ", ".join(output.upper() for output in outputs)
        structure = []
        if pdf:
            structure.append(f"{pdf.get('pages')} s.; tagged={pdf.get('tagged')}")
        if docx:
            size = docx.get("page_size_mm", [])
            structure.append(f"DOCX {size[0]}×{size[1]} mm" if len(size) == 2 else "DOCX")
        if pptx:
            structure.append(f"{pptx.get('slides')} slajdów")
        rows.append(
            f"| `{artifact['id']}` | {forms} | {'; '.join(structure)} | PASS |"
        )

    report = f"""# Raport walidacyjny v0.1

**Data kontroli:** {date.today().isoformat()}<br>
**Werdykt techniczny:** `PASS`<br>
**Werdykt konsultacyjny:** `SHARE WITH CAVEATS`<br>
**Formalne przedłożenie Radzie Ministrów:** `NOT READY — GAP-0011`

## Executive Summary / Streszczenie wykonawcze

Wszystkie {qa['artifact_count']} zadeklarowanych artefaktów i model XLSX zostały zbudowane oraz przeszły automatyczną kontrolę strukturalną. Fakty jawnie użyte w materiałach publikacyjnych mają status `verified`; rekordy `unverified` i `disputed` pozostają w Księdze dowodowej i nie są przedstawiane jako potwierdzone fakty. Pakiet może służyć prywatnym konsultacjom eksperckim z zastrzeżeniami, lecz nie jest gotowy do formalnego obiegu rządowego, ponieważ właściwy minister, podstawa procesu i miejsce w hierarchii strategii wymagają rozstrzygnięcia przez kompetentne organy (`GAP-0011`).

## 1. Zakres automatycznej kontroli

- synchronizacja wyłącznie pakietów z markerem `.complete`;
- walidacja schematów, unikalności ID, relacji claim–source i decyzja–evidence;
- zakaz użycia twierdzenia innego niż `verified` w artefakcie publikacyjnym;
- rejestracja zewnętrznych URL-i, kontrola linków wewnętrznych i wzorców sekretów;
- budowa HTML, PDF, DOCX, PPTX i XLSX z kanonicznych źródeł;
- otwarcie i kontrola liczby stron/slajdów, A4 w DOCX, tagów PDF, formuł i arkuszy XLSX;
- blokada pustych lub osieroconych stron PDF na podstawie minimalnej ilości tekstu;
- kontrola lokalnych obrazów, SVG, metadanych pochodzenia oraz sumy SHA-256 obrazu syntetycznego.

## 2. Stan dowodów

| Element | Liczba |
|---|---:|
| źródła | {len(sources)} |
| twierdzenia ogółem | {len(claims)} |
| `verified` | {claim_counts.get('verified', 0)} |
| `unverified` | {claim_counts.get('unverified', 0)} |
| `disputed` | {claim_counts.get('disputed', 0)} |
| twierdzenia użyte w artefaktach | {len(used_claims)} |
| definicje kontrolowane | {len(definitions)} |
| kandydaty decyzji | {len(decisions)} |
| jawne luki | {len(gaps)} |

## 3. Artefakty wynikowe

| ID | Formaty | Kontrola struktury | Wynik |
|---|---|---|---|
{chr(10).join(rows)}

Model `dist/models/financing-scenarios.xlsx` zawiera {len(qa['financing_model'].get('sheets', []))} arkuszy i {qa['financing_model'].get('formulas', 0)} formuł; brakujące wejścia pozostają `UNKNOWN` zamiast zera lub liczby modelowej.

Łącznie wyrenderowano {total_pdf_pages} stron PDF. Żadna strona nie spadła poniżej progu 100 niebiałych znaków; najniższy wynik w pakiecie to {minimum_page_text_chars}.

Dostępność obrazów OOXML: DOCX {docx_image_alt}/{docx_image_total} oraz PPTX {pptx_image_alt}/{pptx_image_total} grafik ma semantyczny tekst alternatywny.

## 4. Ograniczenia i bramki człowieka

1. `GAP-0011` blokuje formalne przedłożenie RM; model nie może sam wyznaczyć organu właściwego ani podstawy prawnej.
2. Automatyczna kontrola potwierdza tagowanie i wygenerowanie wariantu `PDF/UA-1`, ale nie jest certyfikacją pełnej zgodności PDF/UA ani testem z każdym czytnikiem asystującym.
3. Obraz okładkowy jest syntetyczną ilustracją, nie dowodem. Dokładna wersja modelu generującego nie została ujawniona przez platformę i pozostaje `UNKNOWN`.
4. Repozytorium i pakiet wynikowy są wyłącznie jawne; nie są środowiskiem akredytowanym dla informacji niejawnych ani operacyjnie wrażliwych.
5. Publikacja, wysłanie do instytucji, użycie nazwy organu jako patrona, wybór dostawcy, budżetu lub lokalizacji wymaga osobnej akceptacji człowieka.
6. Pełny wynik niezależnej kontroli merytorycznej znajduje się w `reports/red-team-v0.1.md`.
7. Pełny wynik niezależnej kontroli renderów znajduje się w `reports/visual-qa-v0.1.md`.

## 5. Polecenie odtworzenia

```bash
make release-check
make package
```

Kontrola techniczna jest powtarzalna. Werdykt merytoryczny i prawny wymaga niezależnych recenzentów oraz ponownego sprawdzenia danych zmiennych na dzień każdego przyszłego wydania.
"""
    reports = ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    (reports / "validation-report-v0.1.md").write_text(report, encoding="utf-8")
    print(f"Generated validation report for {qa['artifact_count']} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
