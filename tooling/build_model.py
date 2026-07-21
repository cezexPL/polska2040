#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import xlsxwriter


def build_financing_model(destination: Path):
    destination.parent.mkdir(parents=True, exist_ok=True)
    workbook = xlsxwriter.Workbook(destination)
    title = workbook.add_format({"bold": True, "font_size": 15, "font_color": "#0B1F33"})
    header = workbook.add_format({"bold": True, "bg_color": "#0B1F33", "font_color": "#FFFFFF", "border": 1})
    text = workbook.add_format({"text_wrap": True, "valign": "top", "border": 1})
    unknown = workbook.add_format({"text_wrap": True, "valign": "top", "border": 1, "bg_color": "#FFF4D7", "font_color": "#8A5A00"})
    money = workbook.add_format({"num_format": "#,##0.0", "border": 1})

    readme = workbook.add_worksheet("README")
    readme.set_column("A:A", 24)
    readme.set_column("B:B", 92)
    readme.write("A1", "Polska 2040 — model finansowy v0.1", title)
    rows = [
        ("Status", "Szkielet scenariuszowy. Nie jest prognozą budżetową ani ofertą inwestycyjną."),
        ("Zasada", "Komórka UNKNOWN pozostaje nieuzupełniona, dopóki nie istnieje jawne źródło lub zatwierdzone założenie."),
        ("Scenariusze", "Niski, bazowy i wysoki różnią się skalą i tempem; nie różnią się przez arbitralne mnożniki bez uzasadnienia."),
        ("Jednostka", "mln PLN w cenach roku bazowego wskazanego przy założeniu."),
    ]
    for index, (label, value) in enumerate(rows, start=3):
        readme.write(index, 0, label, header)
        readme.write(index, 1, value, text)

    assumptions = workbook.add_worksheet("Assumptions")
    assumptions.set_column("A:A", 18)
    assumptions.set_column("B:B", 42)
    assumptions.set_column("C:F", 20)
    assumptions.write_row("A1", ["ID", "Założenie", "Wartość", "Jednostka", "Rok bazowy", "Źródło/status"], header)
    assumption_rows = [
        ("ASM-001", "Istniejące zobowiązania publiczne objęte zakresem", "UNKNOWN", "mln PLN", "UNKNOWN", "wymagany audyt"),
        ("ASM-002", "Koszt systemu danych i ewaluacji", "UNKNOWN", "mln PLN", "UNKNOWN", "wymagana wycena"),
        ("ASM-003", "Koszt regionalnego centrum", "UNKNOWN", "mln PLN", "UNKNOWN", "wymagany pilotaż"),
        ("ASM-004", "Dodatkowość względem programów UE", "UNKNOWN", "%", "UNKNOWN", "wymagana analiza podwójnego finansowania"),
    ]
    for row_index, row in enumerate(assumption_rows, start=1):
        for col_index, value in enumerate(row):
            assumptions.write(row_index, col_index, value, unknown if value == "UNKNOWN" else text)

    scenarios = workbook.add_worksheet("Scenarios")
    scenarios.set_column("A:A", 34)
    scenarios.set_column("B:D", 18)
    scenarios.set_column("E:E", 60)
    scenarios.write_row("A1", ["Kategoria", "Niski", "Bazowy", "Wysoki", "Podstawa/uwagi"], header)
    categories = [
        "Governance i ewaluacja",
        "Dane, AI, obliczenia i cyber",
        "Testy i małe partie",
        "Przemysł i komponenty",
        "Kadry i edukacja",
        "Partnerstwa międzynarodowe",
        "Zastosowania cywilne i regiony",
    ]
    for row_index, category in enumerate(categories, start=1):
        scenarios.write(row_index, 0, category, text)
        for col_index in range(1, 4):
            scenarios.write_blank(row_index, col_index, None, money)
        scenarios.write(row_index, 4, "UNKNOWN — do powiązania z audytem bazowym", unknown)
    scenarios.write(len(categories) + 1, 0, "SUMA", header)
    for col_index, column in enumerate(["B", "C", "D"], start=1):
        scenarios.write_formula(len(categories) + 1, col_index, f"=SUM({column}2:{column}{len(categories)+1})", money)

    funding = workbook.add_worksheet("Funding map")
    funding.set_column("A:A", 26)
    funding.set_column("B:E", 24)
    funding.write_row("A1", ["Instrument", "Etap", "Status", "Ryzyko podwójnego finansowania", "Źródło"], header)
    instruments = ["Budżet państwa", "SAFE", "EDF", "EUDIS", "STEP", "PFR/BGK", "NCBR/PARP", "Kapitał prywatny"]
    for row_index, instrument in enumerate(instruments, start=1):
        funding.write(row_index, 0, instrument, text)
        funding.write(row_index, 1, "do przypisania", unknown)
        funding.write(row_index, 2, "do weryfikacji", unknown)
        funding.write(row_index, 3, "do oceny", unknown)
        funding.write(row_index, 4, "SRC-…", unknown)

    kpis = workbook.add_worksheet("KPI")
    kpis.set_column("A:A", 28)
    kpis.set_column("B:F", 24)
    kpis.write_row("A1", ["Miernik", "Definicja", "Wartość bazowa", "Cel", "Właściciel", "Źródło"], header)
    for row_index, metric in enumerate(["Czas do pilotażu", "Czas do pierwszej partii", "Udział testów użytkownika", "Odporność dostaw", "Wartość dodana w Polsce", "Retencja kadr", "Eksport", "Projekty zamknięte"], start=1):
        kpis.write(row_index, 0, metric, text)
        for col_index in range(1, 6):
            kpis.write(row_index, col_index, "UNKNOWN", unknown)

    workbook.close()

