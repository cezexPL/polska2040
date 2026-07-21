# Polska 2040 — końcowa kontrola wizualna i techniczna v0.1

**Data kontroli:** 21 lipca 2026 r.
**Zakres:** finalny katalog `dist/`, 17 artefaktów, wszystkie formaty publikacyjne
**Werdykt końcowy:** **PASS**
**Klasyfikacja usterek:** P0 = 0, P1 = 0, P2 = 0

Pakiet przechodzi bramkę jakości renderu, integralności plików, geometrii, podstawowej dostępności technicznej i nawigacji. Skontrolowano wszystkie **403 strony PDF**: 334 strony A4 oraz 69 slajdów. Nie znaleziono obciętego tekstu, pustych lub przypadkowo niemal pustych stron, błędów numeracji, uszkodzonych linków ani wad struktury OOXML.

Ten wynik nie oznacza formalnej gotowości dokumentu do przedłożenia Radzie Ministrów. Kontrola merytoryczna nadal klasyfikuje pakiet jako `SHARE WITH CAVEATS` do kontrolowanej konsultacji i `NOT READY — GAP-0011` do formalnego przedłożenia RM; zob. [końcowy raport red-team](red-team-v0.1.md).

## 1. Kontrolowany snapshot

| Element | Wartość |
|---|---|
| Katalog artefaktów | [dist/index.html](../dist/index.html) |
| Wynik bramki generatora | [output-qa.json](../dist/output-qa.json): `passed`, 17 artefaktów, 0 błędów |
| SHA-256 `build-manifest.json` | `3ece0a2202538d28d389cb41a69d88e5e0d10a1b2b5521d2b0495ca8d0ae16ae` |
| SHA-256 `output-qa.json` | `bae77391a0b6a628d77e54d0d74fd43c584c1490eca4c828b9c561422d058e25` |
| Zbiorczy SHA-256 17 PDF | `e0494f6b7f64d2d84ebe26616b819cd2cf7ee9fcc09a5dbbe62bc63bdeeb4a4a` |
| Stabilność | brak zmiany plików podczas finalnych testów |

## 2. Metoda

1. **Pełny render.** Każdą z 403 stron wyrenderowano do obrazu i oceniono na planszach kontaktowych. Kluczowe strony wyrenderowano dodatkowo w 150–180 dpi.
2. **Regresja pikselowa.** Po poprawce metadanych dostępności ponownie wyrenderowano komplet; 403/403 obrazy były pikselowo identyczne z uprzednio przejrzanym zestawem.
3. **Geometria PDF.** Dla 78 961 ramek słów z `pdftotext -bbox-layout` sprawdzono położenie względem `MediaBox`; wynik: 0 ramek poza stroną.
4. **Stopki i numeracja.** Na każdej stronie wymagano dokładnie jednej stopki A4 albo jednego disclaimera slajdu oraz zgodnej numeracji.
5. **PDF i fonty.** Sprawdzono `pdfinfo` i `pdffonts`: format strony, obrót, `CropBox`, tagowanie, osadzenie fontów, subset i mapę Unicode.
6. **OOXML.** Każdy DOCX, PPTX i XLSX przeszedł test archiwum ZIP, relacji oraz odczyt właściwą biblioteką. Osobno sprawdzono rozmiary stron/slajdów, geometrię obiektów i teksty alternatywne.
7. **HTML.** Rozwiązano wszystkie lokalne ścieżki, kotwice i odwołania do zasobów; sprawdzono `title`, `lang`, identyfikatory i alty obrazów.
8. **Arkusz finansowy.** Sprawdzono arkusze, formuły, walidacje, błędy, odwołania zewnętrzne i ustawienie przeliczenia.

## 3. Wyniki przekrojowe

| Warstwa | Zakres | Wynik |
|---|---:|---|
| PDF | 17 plików, 403 strony | **PASS** |
| Strony A4 | 334, format 595,276 × 841,89 pt | **PASS** |
| Slajdy PDF | 69, format 959,976 × 540 pt | **PASS** |
| Tagowanie PDF | 17/17 `Tagged: yes` | **PASS** |
| Fonty PDF | 61/61 osadzone, subsetowane i z mapą Unicode | **PASS** |
| Geometria tekstu | 78 961 ramek; 0 poza `MediaBox` | **PASS** |
| Stopki/disclaimery | 403/403 dokładnie po jednym; 0 błędów numeracji | **PASS** |
| Puste strony | 0/403 | **PASS** |
| OOXML | 18/18 archiwów; 493/493 relacje wewnętrzne poprawne | **PASS** |
| DOCX | 12/12 A4, 210,01 × 297,00 mm; 145 tabel bez wad struktury | **PASS** |
| Obrazy DOCX | 3/3 z semantycznym `descr` i `title` | **PASS** |
| PPTX | 5/5, 69 slajdów, 281 obiektów; 0 poza granicami, 0 pustych slajdów | **PASS** |
| Obrazy PPTX | 5/5 z semantycznym `descr` i `title` | **PASS** |
| HTML | 18/18 z `title` i `lang`; 0 zerwanych celów i fragmentów | **PASS** |
| Obrazy HTML | 8/8 z opisowym `alt` | **PASS** |
| XLSX | 8 arkuszy, 33 formuły, 0 błędów i 0 linków zewnętrznych | **PASS** |

Minimalny prześwit tekstu od krawędzi strony wyniósł dla A4: 48,19 pt z lewej, 48,10 pt z prawej, 56,95 pt od góry i 23,69 pt od dołu. Dla slajdów minima wyniosły odpowiednio 32,40 / 32,40 / 52,39 / 19,45 pt. Minimalny odstęp treści od stopki wyniósł 26,09 pt na A4 i 18,00 pt na slajdach.

## 4. Wynik każdego artefaktu

| Artefakt | Format i zakres | Kontrola szczególna | Werdykt |
|---|---|---|---|
| Strategia | [HTML](../dist/strategy/index.html) · [PDF, 37 s.](../dist/strategy/strategy.pdf) · [DOCX](../dist/strategy/strategy.docx) | okładka, diagram cyklu, 2/2 alty DOCX, strona końcowa | **PASS** |
| Plan realizacji | [HTML](../dist/implementation-roadmap/index.html) · [PDF, 21 s.](../dist/implementation-roadmap/implementation-roadmap.pdf) · [DOCX](../dist/implementation-roadmap/implementation-roadmap.docx) | RACI s. 15–16, końcówka s. 20–21, 1/1 alt DOCX | **PASS** |
| Finansowanie i wpływ | [HTML](../dist/impact-finance/index.html) · [PDF, 22 s.](../dist/impact-finance/impact-finance.pdf) · [DOCX](../dist/impact-finance/impact-finance.docx) | szerokie tabele, marginesy, strona końcowa | **PASS** |
| Governance i prawo | [HTML](../dist/governance-law/index.html) · [PDF, 20 s.](../dist/governance-law/governance-law.pdf) · [DOCX](../dist/governance-law/governance-law.docx) | dwustronicowa tabela RACI s. 8–9 i ostatnia strona | **PASS** |
| Księga dowodowa | [HTML](../dist/evidence-book/index.html) · [PDF, 123 s.](../dist/evidence-book/evidence-book.pdf) · [DOCX](../dist/evidence-book/evidence-book.docx) | wszystkie strony rejestrów i wielostronicowych tabel | **PASS** |
| Jawny szablon aneksu ograniczonego | [HTML](../dist/restricted-annex-template/index.html) · [PDF, 14 s.](../dist/restricted-annex-template/restricted-annex-template.pdf) · [DOCX](../dist/restricted-annex-template/restricted-annex-template.docx) | tabele, workflow i końcowe zastrzeżenia | **PASS** |
| Nota dla Premiera i RM | [HTML](../dist/prime-minister-brief/index.html) · [PDF, 7 s.](../dist/prime-minister-brief/prime-minister-brief.pdf) · [DOCX](../dist/prime-minister-brief/prime-minister-brief.docx) | warianty, ryzyka i strona końcowa | **PASS** |
| Nota dla Prezydenta i BBN | [HTML](../dist/president-bbn-brief/index.html) · [PDF, 8 s.](../dist/president-bbn-brief/president-bbn-brief.pdf) · [DOCX](../dist/president-bbn-brief/president-bbn-brief.docx) | tabela doktrynalna, ryzyka i zastrzeżenia | **PASS** |
| Briefy ministerialne | [HTML](../dist/ministerial-briefs/index.html) · [PDF, 14 s.](../dist/ministerial-briefs/ministerial-briefs.pdf) · [DOCX](../dist/ministerial-briefs/ministerial-briefs.docx) | macierz zależności s. 12–13 | **PASS** |
| Brief międzynarodowy | [HTML](../dist/international-brief/index.html) · [PDF, 6 s.](../dist/international-brief/international-brief.pdf) · [DOCX](../dist/international-brief/international-brief.docx) | język angielski, disclaimery i strona końcowa | **PASS** |
| Karta regionalnego pilotażu | [HTML](../dist/regional-pilot-card/index.html) · [PDF, 28 s.](../dist/regional-pilot-card/regional-pilot-card.pdf) · [DOCX](../dist/regional-pilot-card/regional-pilot-card.docx) | s. 27–28; sekcja 16.4, tabela działań i miejsce na notatki | **PASS** |
| Karta danych województwa | [HTML](../dist/voivodeship-data-template/index.html) · [PDF, 34 s.](../dist/voivodeship-data-template/voivodeship-data-template.pdf) · [DOCX](../dist/voivodeship-data-template/voivodeship-data-template.docx) | wszystkie 53 tabele i końcowy rejestr decyzji | **PASS** |
| Prezentacja dla RM | [HTML](../dist/cabinet-deck/index.html) · [PDF, 15 slajdów](../dist/cabinet-deck/cabinet-deck.pdf) · [PPTX](../dist/cabinet-deck/cabinet-deck.pptx) | 2/2 diagramy z semantycznym altem | **PASS** |
| Prezentacja dla Prezydenta | [HTML](../dist/president-deck/index.html) · [PDF, 12 slajdów](../dist/president-deck/president-deck.pdf) · [PPTX](../dist/president-deck/president-deck.pptx) | 1/1 diagram z semantycznym altem | **PASS** |
| Prezentacja na forum ekonomiczne | [HTML](../dist/economic-forum-deck/index.html) · [PDF, 17 slajdów](../dist/economic-forum-deck/economic-forum-deck.pdf) · [PPTX](../dist/economic-forum-deck/economic-forum-deck.pptx) | 1/1 diagram z semantycznym altem | **PASS** |
| Prezentacja regionalna | [HTML](../dist/regional-deck/index.html) · [PDF, 13 slajdów](../dist/regional-deck/regional-deck.pdf) · [PPTX](../dist/regional-deck/regional-deck.pptx) | wszystkie slajdy, tytuły i stały disclaimer | **PASS** |
| Prezentacja międzynarodowa | [HTML](../dist/international-deck/index.html) · [PDF, 12 slajdów](../dist/international-deck/international-deck.pdf) · [PPTX](../dist/international-deck/international-deck.pptx) | angielski diagram na slajdzie 4; 1/1 angielski alt | **PASS** |

Model pomocniczy [financing-scenarios.xlsx](../dist/models/financing-scenarios.xlsx) również przechodzi kontrolę. Zawiera osiem widocznych, niepustych arkuszy (`README`, `Assumptions`, `Commitments`, `Cost model`, `Funding map`, `Impact logic`, `Sensitivity`, `KPI`), 33 formuły i trzy walidacje danych. Nie ma błędów `#REF!`, komórek błędu ani odwołań do zewnętrznych skoroszytów. Wszystkie 33 wartości cache pozostają `UNKNOWN` zgodnie z zasadą fail-closed, a `fullCalcOnLoad=true` wymusza przeliczenie w zgodnym arkuszu kalkulacyjnym.

## 5. Zamknięte regresje

| Wcześniejszy problem | Kontrola finalna | Status |
|---|---|---|
| obcięta tabela RACI w governance | s. 8–9 w 180 dpi, 0 ramek poza stroną | **zamknięty** |
| obcięcie tabeli w roadmapie | s. 15–16 w 150–180 dpi | **zamknięty** |
| obcięta macierz ministerialna | s. 12–13 w 180 dpi | **zamknięty** |
| niemal pusta końcowa strona governance | finalne 20 stron, treść i metadane na s. 20 | **zamknięty** |
| osierocona s. 22 roadmapy | dokument ma 21 stron; komplet treści i metadane mieszczą się na s. 21 | **zamknięty** |
| niejednoznaczna końcówka karty regionalnej | s. 28 zawiera sekcję 16.4, tabelę działań, notatki i metadane | **zamknięty** |
| DOCX w formacie Letter | 12/12 dokumentów ma format A4 | **zamknięty** |
| nieotagowane PDF | 17/17 ma `Tagged: yes` | **zamknięty** |
| polskie etykiety diagramu w wersji międzynarodowej | slajd 4 i diagram są w całości po angielsku | **zamknięty** |
| brak lub techniczny alt w OOXML | DOCX 3/3 i PPTX 5/5 mają semantyczne opisy; walidator odrzuca brak i nazwę pliku | **zamknięty** |

## 6. Ograniczenia kontroli

- Jest to kontrola finalnych plików i renderu, nie ponowny audyt prawdziwości wszystkich twierdzeń. Ten zakres realizuje [red-team](red-team-v0.1.md).
- DOCX i PPTX sprawdzono strukturalnie oraz przez odpowiadające im finalne PDF; nie wykonano osobnej sesji ręcznej w każdej wersji Microsoft Office i LibreOffice.
- `Tagged: yes` oraz obecność altów nie zastępują pełnego audytu kolejności odczytu z konkretnym czytnikiem ekranu.
- Formuły XLSX sprawdzono statycznie. Nie zastępuje to zatwierdzenia założeń finansowych ani decyzji budżetowej.
- Publikacja, wysłanie materiału, wystąpienie w imieniu państwa i deklaracja oficjalnego poparcia pozostają bramką `HUMAN-ONLY`.

## 7. Decyzja bramki

**PASS — pakiet `dist/` jest technicznie i wizualnie gotowy do kontrolowanej konsultacji eksperckiej.** Nie ma otwartego defektu P0, P1 ani P2 w zakresie tej kontroli. Formalne przedłożenie RM pozostaje zablokowane przez `GAP-0011`, a publiczna dystrybucja wymaga decyzji człowieka, przeglądu prawnego, bezpieczeństwa i aktualności.
