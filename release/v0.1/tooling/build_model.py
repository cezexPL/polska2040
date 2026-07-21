#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import xlsxwriter


NAVY = "#0B1F33"
BLUE = "#194F7A"
RED = "#C7333E"
GOLD = "#C7A24A"
PALE_GOLD = "#FFF4D7"
PALE_BLUE = "#EAF2F8"
PALE_RED = "#FCEBEC"
WHITE = "#FFFFFF"


def build_financing_model(destination: Path):
    """Create an auditable, intentionally unpopulated scenario workbook.

    The workbook is a decision model, not a forecast. Numeric inputs remain
    blank while status is UNKNOWN. Formulas propagate UNKNOWN instead of
    silently treating missing evidence as zero.
    """

    destination.parent.mkdir(parents=True, exist_ok=True)
    workbook = xlsxwriter.Workbook(destination)
    workbook.set_properties(
        {
            "title": "Polska 2040 — model finansowania i wpływu v0.1",
            "subject": "Audytowalny model scenariuszowy L/B/H",
            "author": "Polska 2040 — niezależny draft ekspercki",
            "comments": "Brak danych pozostaje UNKNOWN; dokument nie jest prognozą budżetową.",
        }
    )

    fmt = {
        "title": workbook.add_format(
            {"bold": True, "font_size": 16, "font_color": NAVY}
        ),
        "subtitle": workbook.add_format(
            {"bold": True, "font_size": 11, "font_color": BLUE}
        ),
        "header": workbook.add_format(
            {
                "bold": True,
                "bg_color": NAVY,
                "font_color": WHITE,
                "border": 1,
                "text_wrap": True,
                "valign": "vcenter",
            }
        ),
        "text": workbook.add_format(
            {"text_wrap": True, "valign": "top", "border": 1}
        ),
        "input": workbook.add_format(
            {
                "text_wrap": True,
                "valign": "top",
                "border": 1,
                "bg_color": PALE_BLUE,
            }
        ),
        "unknown": workbook.add_format(
            {
                "text_wrap": True,
                "valign": "top",
                "border": 1,
                "bg_color": PALE_GOLD,
                "font_color": "#8A5A00",
            }
        ),
        "warning": workbook.add_format(
            {
                "text_wrap": True,
                "valign": "top",
                "border": 1,
                "bg_color": PALE_RED,
                "font_color": RED,
            }
        ),
        "money": workbook.add_format(
            {"num_format": "#,##0.0", "border": 1, "bg_color": PALE_BLUE}
        ),
        "percent": workbook.add_format(
            {"num_format": "0.0%", "border": 1, "bg_color": PALE_BLUE}
        ),
        "formula": workbook.add_format(
            {"num_format": "#,##0.0", "border": 1, "bg_color": "#F6F8FA"}
        ),
        "total": workbook.add_format(
            {
                "bold": True,
                "num_format": "#,##0.0",
                "border": 1,
                "bg_color": NAVY,
                "font_color": WHITE,
            }
        ),
        "note": workbook.add_format(
            {"italic": True, "font_color": "#5D6873", "text_wrap": True}
        ),
    }

    # README
    readme = workbook.add_worksheet("README")
    readme.hide_gridlines(2)
    readme.set_column("A:A", 28)
    readme.set_column("B:B", 100)
    readme.write("A1", "Polska 2040 — model finansowy v0.1", fmt["title"])
    readme.write(
        "A2",
        "Niezależny draft — nie jest prognozą budżetową ani ofertą inwestycyjną",
        fmt["subtitle"],
    )
    readme_rows = [
        (
            "Zasada nadrzędna",
            "Wartość brakująca nie jest zerem. Status UNKNOWN pozostaje widoczny, a formuły nie zwracają sumy, dopóki wymagany składnik jest nieznany.",
        ),
        (
            "Jednostka kosztowa",
            "mln PLN w cenach roku bazowego wskazanego przy każdym założeniu; waluta źródłowa i kurs mają osobne rekordy.",
        ),
        (
            "Scenariusze",
            "L — integracja niskokosztowa; B — portfel bazowy; H — przyspieszona mobilizacja. To warianty decyzji, nie przedziały ufności.",
        ),
        (
            "Kolor niebieski",
            "Komórka wejściowa do uzupełnienia wyłącznie po wpisaniu źródła/claimu, statusu, właściciela i daty ważności.",
        ),
        (
            "Kolor żółty",
            "UNKNOWN albo wymagany plan pozyskania; nie zastępować wartością modelową bez decyzji o założeniu.",
        ),
        (
            "Źródła",
            "Każde wejście wskazuje CLM-####, SRC-#### albo identyfikator zatwierdzonej decyzji/założenia. Arkusz nie jest samodzielnym źródłem faktu.",
        ),
        (
            "Podwójne finansowanie",
            "Ten sam koszt ma jeden Cost ID. Legalne współfinansowanie ujawnia udziały; dwóch instrumentów nie wolno liczyć jako dwóch rezultatów.",
        ),
        (
            "Wynik",
            "Model pokazuje zobowiązania, płatności, ekspozycje warunkowe, TCO, dodatkowość, wpływ i wrażliwość. Publikacja wymaga niezależnej walidacji.",
        ),
    ]
    for row_index, (label, value) in enumerate(readme_rows, start=3):
        readme.write(row_index, 0, label, fmt["header"])
        readme.write(row_index, 1, value, fmt["text"])

    # Assumptions
    assumptions = workbook.add_worksheet("Assumptions")
    assumptions.freeze_panes(1, 4)
    assumptions.autofilter("A1:N100")
    widths = [14, 12, 42, 14, 14, 14, 14, 13, 12, 18, 22, 14, 14, 45]
    for index, width in enumerate(widths):
        assumptions.set_column(index, index, width)
    assumption_headers = [
        "ID",
        "Cost ID",
        "Parametr / założenie",
        "Status",
        "L",
        "B",
        "H",
        "Jednostka",
        "Rok cen",
        "Claim / źródło",
        "Właściciel",
        "Ważne do",
        "Wrażliwość",
        "Plan pozyskania / uwagi",
    ]
    assumptions.write_row("A1", assumption_headers, fmt["header"])
    assumption_rows = [
        ("ASM-001", "C01", "Przyrostowy koszt governance i ewaluacji"),
        ("ASM-002", "C02", "Koszt katalogu problemów, testów i małych partii"),
        ("ASM-003", "C03", "Koszt przestrzeni danych, AI i obliczeń"),
        ("ASM-004", "C04", "Koszt cyber i bezpiecznego cyklu software"),
        ("ASM-005", "C05", "Przyrostowy CAPEX przemysłowy i komponentowy"),
        ("ASM-006", "C06", "Koszt serwisu, logistyki, części i utylizacji"),
        ("ASM-007", "C07", "Koszt kadr, praktyk i programów kompetencji"),
        ("ASM-008", "C08", "Koszt partnerstw, IP, due diligence i certyfikacji"),
        ("ASM-009", "C09", "Koszt pilotaży regionalnych i cywilnych"),
        ("ASM-010", "C10", "Koszt instrumentów eksportu i obsługi rynków"),
        ("ASM-011", "X01", "Istniejące zobowiązania w zakresie programu"),
        ("ASM-012", "X02", "Koszt obsługi finansowania pożyczkowego"),
        ("ASM-013", "X03", "Ekspozycja warunkowa gwarancji"),
        ("ASM-014", "X04", "Koszt zakończenia lub migracji"),
        ("ASM-015", "X05", "Udział kosztów dodatkowych względem bazowej aktywności"),
    ]
    for row_index, (assumption_id, cost_id, description) in enumerate(
        assumption_rows, start=1
    ):
        assumptions.write(row_index, 0, assumption_id, fmt["text"])
        assumptions.write(row_index, 1, cost_id, fmt["text"])
        assumptions.write(row_index, 2, description, fmt["text"])
        assumptions.write(row_index, 3, "UNKNOWN", fmt["unknown"])
        for column in range(4, 7):
            assumptions.write_blank(row_index, column, None, fmt["money"])
        assumptions.write(row_index, 7, "mln PLN", fmt["input"])
        assumptions.write(row_index, 8, "UNKNOWN", fmt["unknown"])
        assumptions.write(row_index, 9, "UNKNOWN", fmt["unknown"])
        assumptions.write(row_index, 10, "do wskazania", fmt["unknown"])
        assumptions.write(row_index, 11, "UNKNOWN", fmt["unknown"])
        assumptions.write(row_index, 12, "do oceny", fmt["unknown"])
        assumptions.write(
            row_index,
            13,
            "Wymagany audyt bazowy i zatwierdzone założenie.",
            fmt["unknown"],
        )
    assumptions.data_validation(
        "D2:D100",
        {
            "validate": "list",
            "source": ["UNKNOWN", "FACT", "ASSUMPTION", "SCENARIO", "RETIRED"],
        },
    )
    assumptions.data_validation(
        "M2:M100",
        {"validate": "list", "source": ["low", "medium", "high", "critical"]},
    )
    assumptions.conditional_format(
        "D2:D100",
        {
            "type": "text",
            "criteria": "containing",
            "value": "UNKNOWN",
            "format": fmt["unknown"],
        },
    )

    # Commitments and disbursements
    commitments = workbook.add_worksheet("Commitments")
    commitments.freeze_panes(1, 3)
    commitments.autofilter("A1:O200")
    for index, width in enumerate(
        [16, 18, 34, 18, 14, 14, 14, 14, 16, 16, 16, 20, 18, 16, 38]
    ):
        commitments.set_column(index, index, width)
    commitment_headers = [
        "Cost ID",
        "Project ID",
        "Opis kosztu",
        "Instrument",
        "Status",
        "Rok zobowiązania",
        "Rok płatności",
        "Kwota mln PLN",
        "Udział krajowy",
        "Udział UE/inny",
        "Waluta źródłowa",
        "Claim / źródło",
        "Dodatkowość",
        "Ryzyko kolizji",
        "Uwagi / sposób rozstrzygnięcia",
    ]
    commitments.write_row("A1", commitment_headers, fmt["header"])
    for row in range(1, 26):
        commitments.write(row, 0, f"COST-{row:03d}", fmt["text"])
        commitments.write(row, 1, "UNKNOWN", fmt["unknown"])
        commitments.write(row, 2, "UNKNOWN", fmt["unknown"])
        commitments.write(row, 3, "do przypisania", fmt["unknown"])
        commitments.write(row, 4, "UNKNOWN", fmt["unknown"])
        commitments.write(row, 5, "UNKNOWN", fmt["unknown"])
        commitments.write(row, 6, "UNKNOWN", fmt["unknown"])
        commitments.write_blank(row, 7, None, fmt["money"])
        commitments.write_blank(row, 8, None, fmt["percent"])
        commitments.write_blank(row, 9, None, fmt["percent"])
        commitments.write(row, 10, "PLN", fmt["input"])
        commitments.write(row, 11, "UNKNOWN", fmt["unknown"])
        commitments.write(row, 12, "do oceny", fmt["unknown"])
        commitments.write(row, 13, "do oceny", fmt["unknown"])
        commitments.write(row, 14, "", fmt["input"])
    commitments.data_validation(
        "E2:E200",
        {
            "validate": "list",
            "source": [
                "UNKNOWN",
                "planned",
                "contracted",
                "paid",
                "cancelled",
                "retired",
            ],
        },
    )

    # Cost model
    cost_model = workbook.add_worksheet("Cost model")
    cost_model.set_column("A:A", 12)
    cost_model.set_column("B:B", 42)
    cost_model.set_column("C:E", 18)
    cost_model.set_column("F:F", 65)
    cost_model.write_row(
        "A1", ["Cost ID", "Kategoria", "L", "B", "H", "Reguła"], fmt["header"]
    )
    categories = [
        ("C01", "Governance i ewaluacja"),
        ("C02", "Problemy, testy i małe partie"),
        ("C03", "Dane, AI i obliczenia"),
        ("C04", "Cyber i software"),
        ("C05", "Przemysł i komponenty"),
        ("C06", "Serwis i logistyka"),
        ("C07", "Kadry i edukacja"),
        ("C08", "Partnerstwa, IP i certyfikacja"),
        ("C09", "Regiony i zastosowania cywilne"),
        ("C10", "Eksport"),
    ]
    assumption_value_columns = {2: "E", 3: "F", 4: "G"}
    for row_index, (cost_id, label) in enumerate(categories, start=1):
        cost_model.write(row_index, 0, cost_id, fmt["text"])
        cost_model.write(row_index, 1, label, fmt["text"])
        for output_column, assumption_column in assumption_value_columns.items():
            formula = (
                f'=IF(COUNTIFS(Assumptions!$B$2:$B$100,$A{row_index+1},'
                f'Assumptions!$D$2:$D$100,"UNKNOWN")>0,"UNKNOWN",'
                f'SUMIFS(Assumptions!${assumption_column}$2:${assumption_column}$100,'
                f'Assumptions!$B$2:$B$100,$A{row_index+1}))'
            )
            cost_model.write_formula(
                row_index, output_column, formula, fmt["formula"], "UNKNOWN"
            )
        cost_model.write(
            row_index,
            5,
            "UNKNOWN propaguje się do wyniku; zero wymaga jawnego założenia FACT/ASSUMPTION.",
            fmt["text"],
        )
    total_row = len(categories) + 1
    cost_model.write(total_row, 0, "TOTAL", fmt["header"])
    cost_model.write(total_row, 1, "SUMA PRZYROSTOWA", fmt["header"])
    for column, letter in zip(range(2, 5), ["C", "D", "E"]):
        formula = (
            f'=IF(COUNTIF({letter}2:{letter}{len(categories)+1},"UNKNOWN")>0,'
            f'"UNKNOWN",SUM({letter}2:{letter}{len(categories)+1}))'
        )
        cost_model.write_formula(total_row, column, formula, fmt["total"], "UNKNOWN")
    cost_model.write(
        total_row,
        5,
        "Suma nie obejmuje istniejących zobowiązań ani kosztu finansowania, dopóki nie zostaną osobno zmapowane.",
        fmt["header"],
    )

    # Funding map
    funding = workbook.add_worksheet("Funding map")
    funding.freeze_panes(1, 2)
    for index, width in enumerate([24, 26, 26, 18, 24, 22, 20, 48]):
        funding.set_column(index, index, width)
    funding.write_row(
        "A1",
        [
            "Instrument",
            "Etap/ryzyko",
            "Potencjalna funkcja",
            "Status analizy",
            "Współfinansowanie",
            "Podwójne finansowanie",
            "Claim / źródło",
            "Warunek użycia / zastrzeżenie",
        ],
        fmt["header"],
    )
    funding_rows = [
        (
            "Budżet państwa",
            "zadania publiczne i zakupy",
            "mandat, usługi, kontrakty",
            "do mapowania",
            "zależne od pozycji",
            "wysokie",
            "UNKNOWN",
            "Wskazać dysponenta, zobowiązanie, płatność i koszt alternatywny.",
        ),
        (
            "SAFE",
            "zdolności i zamówienia",
            "finansowanie pożyczkowe",
            "umowa podpisana",
            "do weryfikacji",
            "wysokie",
            "CLM-1208/1209",
            "Nie traktować 43,7 mld EUR jako dotacji ani całej kwoty nowego programu; kwalifikowalność per koszt.",
        ),
        (
            "EDF",
            "B+R i demonstracja",
            "projekty konsorcjalne",
            "do weryfikacji call",
            "zależne od call",
            "wysokie",
            "UNKNOWN",
            "Sprawdzić bieżący regulamin, IP, konsorcjum i koszty kwalifikowane.",
        ),
        (
            "EUDIS",
            "innowacje i scale-up",
            "instrument zależny od ścieżki",
            "do weryfikacji",
            "zależne",
            "średnie",
            "UNKNOWN",
            "Nie zakładać dostępności ani kwalifikowalności bez aktualnego naboru.",
        ),
        (
            "STEP",
            "technologie strategiczne",
            "platforma/oznaczenie i instrumenty powiązane",
            "do weryfikacji",
            "zależne",
            "wysokie",
            "UNKNOWN",
            "Wskazać konkretny program finansujący, nie liczyć całej platformy.",
        ),
        (
            "PFR/BGK",
            "kapitał, kredyt, gwarancja",
            "moce i kapitał obrotowy",
            "do mapowania",
            "zależne",
            "średnie",
            "UNKNOWN",
            "Prywatny udział ryzyka, wycena ekspozycji i strategia wyjścia.",
        ),
        (
            "NCBR/PARP",
            "B+R, MŚP, internacjonalizacja",
            "granty i programy",
            "do mapowania",
            "zależne",
            "wysokie",
            "UNKNOWN",
            "Połączyć z użytkownikiem i bramką wdrożeniową; nie dublować kosztu.",
        ),
        (
            "Kapitał prywatny",
            "ryzyko rynkowe i skala",
            "equity/debt/strategic",
            "case-by-case",
            "nie dotyczy",
            "niskie/średnie",
            "UNKNOWN",
            "Nie gwarantować całego wyniku; ujawnić prawa, wycenę i konflikt interesów.",
        ),
    ]
    for row_index, row in enumerate(funding_rows, start=1):
        for column, value in enumerate(row):
            funding.write(
                row_index,
                column,
                value,
                fmt["unknown"] if value in {"UNKNOWN", "do mapowania", "do weryfikacji"} else fmt["text"],
            )

    # Impact logic
    impact = workbook.add_worksheet("Impact logic")
    for index, width in enumerate([14, 34, 40, 24, 24, 22, 46]):
        impact.set_column(index, index, width)
    impact.write_row(
        "A1",
        [
            "ID",
            "Rezultat",
            "Kontrfaktyczny wariant",
            "Baza",
            "Miara",
            "Źródło",
            "Ryzyka atrybucji / uwagi",
        ],
        fmt["header"],
    )
    impact_rows = [
        ("IMP-01", "krótszy czas do testu", "obecny proces", "UNKNOWN", "dni/mediana"),
        ("IMP-02", "odporność dostaw", "pojedynczy dostawca", "UNKNOWN", "% testowanej substytucji"),
        ("IMP-03", "wartość dodana w Polsce", "import lub baza 2026", "UNKNOWN", "mln PLN / %"),
        ("IMP-04", "produktywność procesu cywilnego", "proces bez interwencji", "UNKNOWN", "wynik na nakład"),
        ("IMP-05", "retencja kompetencji", "brak programu", "UNKNOWN", "% po 12/24 mies."),
        ("IMP-06", "wykonany eksport", "trend bazowy", "UNKNOWN", "przychód/marża/serwis"),
        ("IMP-07", "uniknięte zobowiązania", "automatyczne skalowanie", "UNKNOWN", "mln PLN opcji niewykonanych"),
    ]
    for row_index, row in enumerate(impact_rows, start=1):
        impact.write(row_index, 0, row[0], fmt["text"])
        impact.write(row_index, 1, row[1], fmt["text"])
        impact.write(row_index, 2, row[2], fmt["text"])
        impact.write(row_index, 3, row[3], fmt["unknown"])
        impact.write(row_index, 4, row[4], fmt["text"])
        impact.write(row_index, 5, "UNKNOWN", fmt["unknown"])
        impact.write(
            row_index,
            6,
            "Wymagana metodologia dodatkowości; nie przypisywać całej obserwowanej zmiany programowi.",
            fmt["unknown"],
        )

    # Sensitivity
    sensitivity = workbook.add_worksheet("Sensitivity")
    for index, width in enumerate([14, 40, 18, 18, 18, 18, 24, 46]):
        sensitivity.set_column(index, index, width)
    sensitivity.write_row(
        "A1",
        [
            "ID",
            "Czynnik",
            "Low",
            "Base",
            "High",
            "Jednostka",
            "Wpływ na decyzję",
            "Plan walidacji",
        ],
        fmt["header"],
    )
    sensitivity_factors = [
        ("SEN-01", "odchylenie CAPEX", "%"),
        ("SEN-02", "opóźnienie uruchomienia", "miesiące"),
        ("SEN-03", "wykorzystanie mocy", "%"),
        ("SEN-04", "koszt finansowania", "%"),
        ("SEN-05", "kurs walutowy", "PLN/waluta"),
        ("SEN-06", "koszt serwisu i aktualizacji", "mln PLN"),
        ("SEN-07", "retencja kadr", "%"),
        ("SEN-08", "opóźnienie przychodu eksportowego", "miesiące"),
        ("SEN-09", "udział projektów zamkniętych przed skalą", "%"),
        ("SEN-10", "dostępność komponentów", "indeks"),
    ]
    for row_index, (factor_id, factor, unit) in enumerate(
        sensitivity_factors, start=1
    ):
        sensitivity.write(row_index, 0, factor_id, fmt["text"])
        sensitivity.write(row_index, 1, factor, fmt["text"])
        for column in range(2, 5):
            sensitivity.write_blank(row_index, column, None, fmt["money"])
        sensitivity.write(row_index, 5, unit, fmt["text"])
        sensitivity.write(row_index, 6, "do oceny", fmt["unknown"])
        sensitivity.write(row_index, 7, "właściciel i termin do wskazania", fmt["unknown"])

    # KPI dictionary
    kpis = workbook.add_worksheet("KPI")
    for index, width in enumerate([14, 30, 46, 22, 18, 18, 24, 22, 38]):
        kpis.set_column(index, index, width)
    kpis.write_row(
        "A1",
        [
            "ID",
            "Miernik",
            "Definicja",
            "Wartość bazowa",
            "Cel",
            "Jednostka",
            "Właściciel",
            "Źródło",
            "Guardrail / uwagi",
        ],
        fmt["header"],
    )
    kpi_rows = [
        ("KPI-01", "Czas do pilotażu", "mediana dni B0→kontrakt pilotażowy", "dni"),
        ("KPI-02", "Czas do testu użytkownika", "mediana dni B1→B3", "dni"),
        ("KPI-03", "Udział testów użytkownika", "projekty z B3 / projekty po B2", "%"),
        ("KPI-04", "Dyscyplina zamknięć", "zamknięte z powodem / decyzje końcowe", "%"),
        ("KPI-05", "Testowana substytucja", "elementy z testem / elementy krytyczne", "%"),
        ("KPI-06", "Pełny TCO", "koszt cyklu na jednostkę rezultatu", "mln PLN/jedn."),
        ("KPI-07", "Retencja kadr", "osoby w roli po 12/24 mies. / absolwenci", "%"),
        ("KPI-08", "Wartość dodana w Polsce", "według zatwierdzonej metodologii", "mln PLN / %"),
        ("KPI-09", "Popyt po pilotażu", "kontynuacje z budżetu właściciela / pilotaże", "%"),
        ("KPI-10", "Wykonany eksport", "dostawy, przychód i serwis", "mln PLN"),
    ]
    for row_index, (kpi_id, name, definition, unit) in enumerate(kpi_rows, start=1):
        kpis.write(row_index, 0, kpi_id, fmt["text"])
        kpis.write(row_index, 1, name, fmt["text"])
        kpis.write(row_index, 2, definition, fmt["text"])
        kpis.write(row_index, 3, "UNKNOWN", fmt["unknown"])
        kpis.write(row_index, 4, "UNKNOWN", fmt["unknown"])
        kpis.write(row_index, 5, unit, fmt["text"])
        kpis.write(row_index, 6, "do wskazania", fmt["unknown"])
        kpis.write(row_index, 7, "UNKNOWN", fmt["unknown"])
        kpis.write(
            row_index,
            8,
            "Cel nie może zostać zatwierdzony bez bazy, mianownika i kosztu pomiaru.",
            fmt["unknown"],
        )

    # Consistent print setup and tab colors.
    for sheet in workbook.worksheets():
        sheet.set_landscape()
        sheet.fit_to_pages(1, 0)
        sheet.set_margins(0.25, 0.25, 0.45, 0.45)
        sheet.set_footer("&LPolska 2040 — draft v0.1&C&P / &N&R&F")
    readme.set_tab_color(GOLD)
    assumptions.set_tab_color(BLUE)
    commitments.set_tab_color(RED)
    cost_model.set_tab_color(NAVY)
    funding.set_tab_color(BLUE)
    impact.set_tab_color(GOLD)
    sensitivity.set_tab_color(RED)
    kpis.set_tab_color(NAVY)

    workbook.close()
