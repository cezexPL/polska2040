# Raport walidacyjny v0.1

**Data kontroli:** 2026-07-21<br>
**Werdykt techniczny:** `PASS`<br>
**Werdykt konsultacyjny:** `SHARE WITH CAVEATS`<br>
**Formalne przedłożenie Radzie Ministrów:** `NOT READY — GAP-0011`

## Executive Summary / Streszczenie wykonawcze

Wszystkie 17 zadeklarowanych artefaktów i model XLSX zostały zbudowane oraz przeszły automatyczną kontrolę strukturalną. Fakty jawnie użyte w materiałach publikacyjnych mają status `verified`; rekordy `unverified` i `disputed` pozostają w Księdze dowodowej i nie są przedstawiane jako potwierdzone fakty. Pakiet może służyć prywatnym konsultacjom eksperckim z zastrzeżeniami, lecz nie jest gotowy do formalnego obiegu rządowego, ponieważ właściwy minister, podstawa procesu i miejsce w hierarchii strategii wymagają rozstrzygnięcia przez kompetentne organy (`GAP-0011`).

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
| źródła | 278 |
| twierdzenia ogółem | 491 |
| `verified` | 84 |
| `unverified` | 401 |
| `disputed` | 6 |
| twierdzenia użyte w artefaktach | 39 |
| definicje kontrolowane | 10 |
| kandydaty decyzji | 10 |
| jawne luki | 11 |

## 3. Artefakty wynikowe

| ID | Formaty | Kontrola struktury | Wynik |
|---|---|---|---|
| `strategy` | HTML, PDF, DOCX | 37 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `implementation-roadmap` | HTML, PDF, DOCX | 21 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `impact-finance` | HTML, PDF, DOCX | 22 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `governance-law` | HTML, PDF, DOCX | 20 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `evidence-book` | HTML, PDF, DOCX | 123 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `restricted-annex-template` | HTML, PDF, DOCX | 14 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `prime-minister-brief` | HTML, PDF, DOCX | 7 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `president-bbn-brief` | HTML, PDF, DOCX | 8 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `ministerial-briefs` | HTML, PDF, DOCX | 14 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `international-brief` | HTML, PDF, DOCX | 6 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `regional-pilot-card` | HTML, PDF, DOCX | 28 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `voivodeship-data-template` | HTML, PDF, DOCX | 34 s.; tagged=True; DOCX 210.0×297.0 mm | PASS |
| `cabinet-deck` | HTML, PDF, PPTX | 15 s.; tagged=True; 15 slajdów | PASS |
| `president-deck` | HTML, PDF, PPTX | 12 s.; tagged=True; 12 slajdów | PASS |
| `economic-forum-deck` | HTML, PDF, PPTX | 17 s.; tagged=True; 17 slajdów | PASS |
| `regional-deck` | HTML, PDF, PPTX | 13 s.; tagged=True; 13 slajdów | PASS |
| `international-deck` | HTML, PDF, PPTX | 12 s.; tagged=True; 12 slajdów | PASS |

Model `dist/models/financing-scenarios.xlsx` zawiera 8 arkuszy i 33 formuł; brakujące wejścia pozostają `UNKNOWN` zamiast zera lub liczby modelowej.

Łącznie wyrenderowano 403 stron PDF. Żadna strona nie spadła poniżej progu 100 niebiałych znaków; najniższy wynik w pakiecie to 208.

Dostępność obrazów OOXML: DOCX 3/3 oraz PPTX 5/5 grafik ma semantyczny tekst alternatywny.

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
