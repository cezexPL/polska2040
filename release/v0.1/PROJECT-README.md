# Polska 2040: Suwerenność technologiczna

Niezależny, bezpartyjny i audytowalny projekt strategii państwa dotyczącej suwerenności technologicznej, systemów autonomicznych, AI oraz technologii podwójnego zastosowania.

> **Status:** prywatny, przedmandatowy draft ekspercki v0.1 do konsultacji. To nie jest dokument rządowy ani stanowisko Prezydenta RP, Rady Ministrów, BBN, Sił Zbrojnych RP lub którejkolwiek instytucji publicznej. Nie jest gotowy do formalnego przedłożenia RM: właściwy minister, podstawa procesu i miejsce w hierarchii strategii pozostają nierozstrzygnięte (`GAP-0011`).

## Wynik, który budujemy

Projekt ma połączyć problem operacyjny, dane, prototypowanie, testy, zamówienia, produkcję, kadry, finansowanie, eksport i aktualizację zdolności w jeden mierzalny system realizacji. Brakujące dane pozostają jawnie oznaczone jako nieznane; nie są zastępowane liczbami wygenerowanymi przez model.

## Spis treści repozytorium

- [`GOAL.md`](GOAL.md) — cel, harmonogram, warunki ukończenia i bramki jakości.
- [`orchestration/GPT-SOL-ULTRA-GOAL.md`](orchestration/GPT-SOL-ULTRA-GOAL.md) — trwały runbook pętli Goal, fal agentów, wznowienia i wydania.
- [`AGENTS.md`](AGENTS.md) — role dwunastu doradców, kontrakty wyjściowe i zasady handoffu.
- [`METHODOLOGY.md`](METHODOLOGY.md) — metodologia źródeł, twierdzeń, syntezy i red-team.
- [`SECURITY.md`](SECURITY.md) — granice informacji jawnych, wrażliwych i niejawnych.
- [`DATA_POLICY.md`](DATA_POLICY.md) — sposób przechowywania źródeł, danych i metadanych.
- [`documents/README.md`](documents/README.md) — dlaczego pakiet jest modułowy i jakiej formy używać dla Premiera, Prezydenta, ministra oraz forów.
- [`inputs/initial-brief.md`](inputs/initial-brief.md) — znormalizowany materiał inicjujący, traktowany jako zestaw hipotez.
- `research/` — rejestry źródeł, twierdzeń, kontrolowanych definicji, kandydatów decyzji, luk, ryzyk i sprzeczności.
- `documents/` — kanoniczne moduły strategii oraz dokumenty dla konkretnych odbiorców.
- `assets/` — wykresy, ilustracje, prompty i metadane pochodzenia.
- `tooling/` — budowa HTML/PDF/DOCX/PPTX i automatyczna walidacja.

## Pakiet v0.1

Kanoniczny manifest obejmuje 17 artefaktów oraz model finansowy XLSX:

| Grupa | Zawartość | Formaty |
|---|---|---|
| rdzeń | strategia, roadmapa, finansowanie i wpływ, governance/prawo, Księga dowodowa | HTML, PDF, DOCX |
| centrum państwa | nota i 15-slajdowy deck dla Premiera/RM; nota i 12-slajdowy deck dla Prezydenta/BBN | HTML, PDF, DOCX/PPTX |
| wykonanie | briefy ośmiu portfeli ministerialnych i jawny szablon przyszłego aneksu ograniczonego | HTML, PDF, DOCX |
| gospodarka i regiony | deck gospodarczy, deck regionalny, [karta pilotażu](documents/templates/regional-pilot-card.md) i [szablon danych wojewódzkich](documents/templates/voivodeship-data-template.md) | HTML, PDF, PPTX/DOCX |
| międzynarodowe | angielski executive brief i 12-slajdowy deck | HTML, PDF, DOCX/PPTX |
| model | zobowiązania, koszty, finansowanie, wpływ, wrażliwość i KPI z propagacją `UNKNOWN` | XLSX |

Wersjonowana migawka po pozytywnej bramce powstaje w `release/v0.1/`; sposób jej budowy opisuje [instrukcja wydania](README.md). Pliki w katalogu wersji są wynikiem kompilacji i nie podlegają ręcznej korekcie.

## Stan dowodów

- 278 zarejestrowanych źródeł i 491 atomowych twierdzeń;
- 84 twierdzenia `verified`, 401 `unverified` i 6 `disputed`;
- 39 zweryfikowanych twierdzeń wykorzystanych w artefaktach narracyjnych;
- 10 kontrolowanych definicji `DEF-*`, 10 kandydatów decyzji `DEC-*` i 11 jawnych luk `GAP-*`;
- rekordy niezweryfikowane i sporne pozostają widoczne w Księdze dowodowej, lecz nie mogą być cytowane jako potwierdzone fakty.

## Werdykty v0.1

- [raport walidacyjny](reports/validation-report-v0.1.md): `PASS` techniczny dla 17 artefaktów i modelu XLSX;
- [niezależny red-team](reports/red-team-v0.1.md): `SHARE WITH CAVEATS`, 0 otwartych P0; formalne RM nadal `NOT READY — GAP-0011`;
- [kontrola wizualna i techniczna](reports/visual-qa-v0.1.md): `PASS`, P0/P1/P2 = 0 dla wszystkich 403 stron PDF oraz formatów Office/HTML;
- [noty wydania](reports/release-notes-v0.1.md) opisują zakres, ograniczenia i sugerowaną kolejność recenzji.

## Budowa i kontrola

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make validate
make release-check
make package
```

`make release-check` ponownie synchronizuje pakiety badawcze, waliduje schematy i użycie twierdzeń, buduje wszystkie formaty oraz sprawdza strukturę HTML/PDF/DOCX/PPTX/XLSX. Wyniki robocze trafiają do `dist/`, a `make package` tworzy `release/v0.1/` wraz z `SHA256SUMS`.

Pipeline generuje tagowane PDF-y z wariantem `PDF/UA-1` i wymusza A4 w DOCX. Automatyczna kontrola dowodzi obecności drzewa tagów, nie zastępuje pełnego audytu zgodności PDF/UA przez specjalistę i czytniki asystujące.

## Zasady publikacji

- Repozytorium robocze pozostaje prywatne.
- Publiczna wersja powstanie jako oczyszczony eksport bez historii roboczej.
- Żaden materiał nie jest publikowany ani wysyłany do instytucji bez bramki akceptacyjnej człowieka.
- Repozytorium nie może zawierać informacji niejawnych, danych operacyjnie wrażliwych ani sekretów dostępowych.
- Ilustracja okładkowa jest syntetyczna i nie stanowi dowodu ani mapy. Platforma nie ujawniła dokładnej wersji modelu; repozytorium nie przypisuje jej niepotwierdzonej etykiety „GPT Image 2”.
