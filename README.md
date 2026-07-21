# Polska 2040: Suwerenność technologiczna

Niezależny, bezpartyjny i audytowalny projekt strategii państwa dotyczącej suwerenności technologicznej, systemów autonomicznych, AI oraz technologii podwójnego zastosowania.

> **Status:** prywatny, przedmandatowy draft ekspercki v0.1 do konsultacji. To nie jest dokument rządowy ani stanowisko Prezydenta RP, Rady Ministrów, BBN, Sił Zbrojnych RP lub którejkolwiek instytucji publicznej. Nie jest gotowy do formalnego przedłożenia RM: właściwy minister, podstawa procesu i miejsce w hierarchii strategii pozostają nierozstrzygnięte (`GAP-0011`).

## Spis treści

1. [Gdzie są dokumenty](#gdzie-sa-dokumenty)
2. [Zacznij tutaj](#zacznij-tutaj)
3. [Materiały według odbiorcy](#materialy-wedlug-odbiorcy)
4. [Pełny katalog v0.1](#pelny-katalog-v01)
   - [Rdzeń strategii](#rdzen-strategii)
   - [Noty, briefy i szablony](#noty-briefy-i-szablony)
   - [Prezentacje](#prezentacje)
   - [Model finansowy](#model-finansowy)
5. [Status projektu i publikacji](#status-projektu-i-publikacji)
6. [Dowody i kontrola halucynacji](#dowody-i-kontrola-halucynacji)
7. [Raporty walidacyjne](#raporty-walidacyjne)
8. [Mapa repozytorium](#mapa-repozytorium)
9. [Landing page](#landing-page)
10. [Budowa i kontrola](#budowa-i-kontrola)
11. [Zasady publikacji](#zasady-publikacji)

<a id="gdzie-sa-dokumenty"></a>
## Gdzie są dokumenty

Repozytorium ma cztery różne warstwy. Najczęstsze źródło pomyłki to szukanie gotowych PDF-ów w katalogu ze źródłami Markdown.

| Potrzeba | Katalog | Co zawiera |
|---|---|---|
| edycja treści | [`documents/`](documents/) | kanoniczne źródła Markdown 17 artefaktów |
| gotowe pliki do prywatnej recenzji | [`release/v0.1/`](release/v0.1/) | wersjonowana migawka: 17 PDF, 12 DOCX, 5 PPTX, HTML i model XLSX |
| ostatni lokalny build | `dist/` | wynik generowany ponownie przez `make build`; katalog jest ignorowany przez Git |
| publikacja internetowa | [`landingpage/`](landingpage/) | kod strony i manifest publikacyjny; nie jest automatycznym lustrem `documents/` |

Najwygodniej czytać pliki PDF bezpośrednio z tabel poniżej. Lokalny katalog HTML całego wydania zaczyna się w [`release/v0.1/index.html`](release/v0.1/index.html), ale GitHub nie działa jak serwer dla tych stron — po sklonowaniu repozytorium plik należy otworzyć lokalnie.

Pliki w `documents/` są źródłem prawdy. `dist/` i `release/v0.1/` są wynikami kompilacji i nie powinny być poprawiane ręcznie.

<a id="zacznij-tutaj"></a>
## Zacznij tutaj

Jeżeli chcesz szybko zrozumieć projekt, otwórz kolejno:

1. [Pełna strategia — PDF](release/v0.1/strategy/strategy.pdf) albo [źródło Markdown](documents/core/strategy.md).
2. [Plan realizacji — PDF](release/v0.1/implementation-roadmap/implementation-roadmap.pdf).
3. [Finansowanie i ocena wpływu — PDF](release/v0.1/impact-finance/impact-finance.pdf).
4. [Niezależny red-team](reports/red-team-v0.1.md), aby poznać ograniczenia i otwarte luki.
5. [Noty wydania](reports/release-notes-v0.1.md), aby sprawdzić zakres migawki v0.1.

Do spotkania decyzyjnego użyj materiału właściwego dla odbiorcy, a nie pełnej strategii jako jedynego dokumentu.

<a id="materialy-wedlug-odbiorcy"></a>
## Materiały według odbiorcy

| Odbiorca / sytuacja | Materiał do przeczytania | Materiał na spotkanie |
|---|---|---|
| Premier i Rada Ministrów | [nota decyzyjna — PDF](release/v0.1/prime-minister-brief/prime-minister-brief.pdf) | [prezentacja RM — PDF](release/v0.1/cabinet-deck/cabinet-deck.pdf) lub [PPTX](release/v0.1/cabinet-deck/cabinet-deck.pptx) |
| Prezydent RP i BBN | [nota strategiczna — PDF](release/v0.1/president-bbn-brief/president-bbn-brief.pdf) | [prezentacja — PDF](release/v0.1/president-deck/president-deck.pdf) lub [PPTX](release/v0.1/president-deck/president-deck.pptx) |
| Minister / kierownictwo resortu | [briefy portfeli — PDF](release/v0.1/ministerial-briefs/ministerial-briefs.pdf) | właściwe slajdy prezentacji RM i działania z roadmapy |
| Zespół międzyresortowy | [plan realizacji — PDF](release/v0.1/implementation-roadmap/implementation-roadmap.pdf) | [model finansowy — XLSX](release/v0.1/models/financing-scenarios.xlsx) oraz rejestry decyzji i ryzyk |
| Forum gospodarcze | [strategia — PDF](release/v0.1/strategy/strategy.pdf) | [prezentacja gospodarcza — PDF](release/v0.1/economic-forum-deck/economic-forum-deck.pdf) lub [PPTX](release/v0.1/economic-forum-deck/economic-forum-deck.pptx) |
| Forum regionalne / samorząd | [karta pilotażu — PDF](release/v0.1/regional-pilot-card/regional-pilot-card.pdf) | [prezentacja regionalna — PDF](release/v0.1/regional-deck/regional-deck.pdf) lub [PPTX](release/v0.1/regional-deck/regional-deck.pptx) |
| Partner międzynarodowy | [executive brief EN — PDF](release/v0.1/international-brief/international-brief.pdf) | [international deck — PDF](release/v0.1/international-deck/international-deck.pdf) lub [PPTX](release/v0.1/international-deck/international-deck.pptx) |
| Ekspert, legislator lub kontroler | [strategia](release/v0.1/strategy/strategy.pdf), [governance i prawo](release/v0.1/governance-law/governance-law.pdf) | [Księga dowodowa](release/v0.1/evidence-book/evidence-book.pdf) i [raport red-team](reports/red-team-v0.1.md) |

Pełne objaśnienie formy, pre-readu i różnic narracyjnych znajduje się w [`documents/README.md`](documents/README.md).

<a id="pelny-katalog-v01"></a>
## Pełny katalog v0.1

Kanoniczny [`documents/manifest.yaml`](documents/manifest.yaml) obejmuje 17 artefaktów. Wszystkie mają status źródłowy `reviewed`, ale ten status nie oznacza zgody na publikację ani formalnej gotowości rządowej.

<a id="rdzen-strategii"></a>
### Rdzeń strategii

| Dokument | Źródło | PDF v0.1 | Format edytowalny |
|---|---|---|---|
| Polska 2040: Suwerenność technologiczna | [Markdown](documents/core/strategy.md) | [PDF](release/v0.1/strategy/strategy.pdf) | [DOCX](release/v0.1/strategy/strategy.docx) |
| Plan realizacji 2026–2040 | [Markdown](documents/core/implementation-roadmap.md) | [PDF](release/v0.1/implementation-roadmap/implementation-roadmap.pdf) | [DOCX](release/v0.1/implementation-roadmap/implementation-roadmap.docx) |
| Finansowanie i ocena wpływu | [Markdown](documents/core/impact-finance.md) | [PDF](release/v0.1/impact-finance/impact-finance.pdf) | [DOCX](release/v0.1/impact-finance/impact-finance.docx) |
| Ład instytucjonalny, prawo i zamówienia | [Markdown](documents/core/governance-law.md) | [PDF](release/v0.1/governance-law/governance-law.pdf) | [DOCX](release/v0.1/governance-law/governance-law.docx) |
| Księga dowodowa | [Markdown](documents/core/evidence-book.md) | [PDF](release/v0.1/evidence-book/evidence-book.pdf) | [DOCX](release/v0.1/evidence-book/evidence-book.docx) |

<a id="noty-briefy-i-szablony"></a>
### Noty, briefy i szablony

| Dokument | Źródło | PDF v0.1 | Format edytowalny |
|---|---|---|---|
| Nota decyzyjna dla Premiera i RM | [Markdown](documents/briefs/prime-minister.md) | [PDF](release/v0.1/prime-minister-brief/prime-minister-brief.pdf) | [DOCX](release/v0.1/prime-minister-brief/prime-minister-brief.docx) |
| Nota strategiczna dla Prezydenta i BBN | [Markdown](documents/briefs/president-bbn.md) | [PDF](release/v0.1/president-bbn-brief/president-bbn-brief.pdf) | [DOCX](release/v0.1/president-bbn-brief/president-bbn-brief.docx) |
| Briefy portfeli ministerialnych | [Markdown](documents/briefs/ministerial-briefs.md) | [PDF](release/v0.1/ministerial-briefs/ministerial-briefs.pdf) | [DOCX](release/v0.1/ministerial-briefs/ministerial-briefs.docx) |
| Poland 2040 — Executive Brief (EN) | [Markdown](documents/briefs/international-en.md) | [PDF](release/v0.1/international-brief/international-brief.pdf) | [DOCX](release/v0.1/international-brief/international-brief.docx) |
| Karta kwalifikacji i realizacji pilotażu regionalnego | [Markdown](documents/templates/regional-pilot-card.md) | [PDF](release/v0.1/regional-pilot-card/regional-pilot-card.pdf) | [DOCX](release/v0.1/regional-pilot-card/regional-pilot-card.docx) |
| Szablon danych wojewódzkich | [Markdown](documents/templates/voivodeship-data-template.md) | [PDF](release/v0.1/voivodeship-data-template/voivodeship-data-template.pdf) | [DOCX](release/v0.1/voivodeship-data-template/voivodeship-data-template.docx) |
| Jawny szablon przyszłego aneksu ograniczonego | [Markdown](documents/annexes/restricted-template.md) | [PDF](release/v0.1/restricted-annex-template/restricted-annex-template.pdf) | [DOCX](release/v0.1/restricted-annex-template/restricted-annex-template.docx) |

Szablon aneksu nie zawiera informacji niejawnych ani operacyjnych odpowiedzi. Materiał właściwy dla ograniczonego obiegu może powstać wyłącznie w autoryzowanym środowisku.

<a id="prezentacje"></a>
### Prezentacje

Źródła slajdów są w [`documents/decks/`](documents/decks/). Nie istnieje osobny katalog `presentations/`.

| Prezentacja | Źródło | PDF v0.1 | PPTX |
|---|---|---|---|
| Decyzje Rady Ministrów — 15 slajdów | [Markdown](documents/decks/cabinet.md) | [PDF](release/v0.1/cabinet-deck/cabinet-deck.pdf) | [PPTX](release/v0.1/cabinet-deck/cabinet-deck.pptx) |
| Odporność i ciągłość państwa — 12 slajdów | [Markdown](documents/decks/president.md) | [PDF](release/v0.1/president-deck/president-deck.pdf) | [PPTX](release/v0.1/president-deck/president-deck.pptx) |
| Forum gospodarcze — 16–18 slajdów | [Markdown](documents/decks/economic-forum.md) | [PDF](release/v0.1/economic-forum-deck/economic-forum-deck.pdf) | [PPTX](release/v0.1/economic-forum-deck/economic-forum-deck.pptx) |
| Forum regionalne — 12–14 slajdów | [Markdown](documents/decks/regional.md) | [PDF](release/v0.1/regional-deck/regional-deck.pdf) | [PPTX](release/v0.1/regional-deck/regional-deck.pptx) |
| Technology Sovereignty (EN) — 12 slajdów | [Markdown](documents/decks/international-en.md) | [PDF](release/v0.1/international-deck/international-deck.pdf) | [PPTX](release/v0.1/international-deck/international-deck.pptx) |

<a id="model-finansowy"></a>
### Model finansowy

- [Model scenariuszy finansowania — XLSX](release/v0.1/models/financing-scenarios.xlsx)
- [Dokument metodologiczny finansowania i wpływu — PDF](release/v0.1/impact-finance/impact-finance.pdf)

Model zachowuje `UNKNOWN` tam, gdzie nie zatwierdzono wartości bazowych, budżetu lub celu liczbowego. Nie jest zatwierdzoną prognozą budżetową ani prognozą PKB.

<a id="status-projektu-i-publikacji"></a>
## Status projektu i publikacji

| Warstwa | Stan |
|---|---|
| źródła 17 artefaktów | `reviewed` |
| techniczna migawka `release/v0.1` | QA `passed` |
| niezależny red-team | `SHARE WITH CAVEATS`; 0 otwartych P0 |
| formalne przedłożenie Radzie Ministrów | `NOT READY — GAP-0011` |
| publikacja dokumentów na stronie | `HOLD — HUMAN-ONLY`; obecnie 0 publicznych linków |
| A13 / przyszły Filar VII | zakres v0.2, jeszcze bez pełnego researchu, integracji i nowego red-teamu |

`reviewed` oznacza przejście kontroli źródłowej i technicznej w tym repozytorium. Nie oznacza zatwierdzenia przez organ państwa, zgody na wysyłkę ani zgody na publikację.

<a id="dowody-i-kontrola-halucynacji"></a>
## Dowody i kontrola halucynacji

Projekt ma połączyć problem operacyjny, dane, prototypowanie, testy, zamówienia, produkcję, kadry, finansowanie, eksport i aktualizację zdolności w jeden mierzalny system realizacji. Brakujące dane pozostają jawnie oznaczone jako nieznane; nie są zastępowane liczbami wygenerowanymi przez model.

Stan migawki v0.1:

- 278 zarejestrowanych źródeł i 491 atomowych twierdzeń;
- 84 twierdzenia `verified`, 401 `unverified` i 6 `disputed`;
- 39 zweryfikowanych twierdzeń wykorzystanych w artefaktach narracyjnych;
- 10 kontrolowanych definicji `DEF-*`, 10 kandydatów decyzji `DEC-*` i 11 jawnych luk `GAP-*`;
- rekordy niezweryfikowane i sporne pozostają widoczne w Księdze dowodowej, lecz nie mogą być cytowane jako potwierdzone fakty.

Zasady weryfikacji opisuje [`METHODOLOGY.md`](METHODOLOGY.md). Rejestry źródeł, twierdzeń, użycia twierdzeń, decyzji, luk, ryzyk i sprzeczności znajdują się w [`research/`](research/). Role 13 person doradczych A01–A13, w tym niezależnego red-teamu A12, opisuje [`AGENTS.md`](AGENTS.md).

<a id="raporty-walidacyjne"></a>
## Raporty walidacyjne

- [Raport walidacyjny v0.1](reports/validation-report-v0.1.md) — techniczny `PASS` dla 17 artefaktów i modelu XLSX.
- [Niezależny red-team v0.1](reports/red-team-v0.1.md) — `SHARE WITH CAVEATS`; formalne RM nadal `NOT READY — GAP-0011`.
- [Kontrola wizualna i techniczna](reports/visual-qa-v0.1.md) — `PASS`, P0/P1/P2 = 0 dla 403 stron PDF oraz formatów Office/HTML.
- [Noty wydania v0.1](reports/release-notes-v0.1.md) — zakres, ograniczenia i sugerowana kolejność recenzji.
- [Metadane wydania](release/v0.1/release-metadata.json), [manifest budowy](release/v0.1/build-manifest.json), [wynik QA](release/v0.1/output-qa.json) i [sumy SHA-256](release/v0.1/SHA256SUMS).

<a id="mapa-repozytorium"></a>
## Mapa repozytorium

| Ścieżka | Rola |
|---|---|
| [`GOAL.md`](GOAL.md) | cel, harmonogram, bramki jakości i warunki ukończenia |
| [`orchestration/GPT-SOL-ULTRA-GOAL.md`](orchestration/GPT-SOL-ULTRA-GOAL.md) | runbook pętli Goal, fal agentów, wznowienia i wydania |
| [`AGENTS.md`](AGENTS.md) | persony doradcze, kontrakty wyników i handoff |
| [`METHODOLOGY.md`](METHODOLOGY.md) | metodologia źródeł, twierdzeń, syntezy i red-team |
| [`SECURITY.md`](SECURITY.md) | granice informacji jawnych, wrażliwych i niejawnych |
| [`DATA_POLICY.md`](DATA_POLICY.md) | przechowywanie źródeł, danych i metadanych |
| [`inputs/initial-brief.md`](inputs/initial-brief.md) | znormalizowany materiał inicjujący, traktowany jako zestaw hipotez |
| [`documents/`](documents/) | kanoniczne moduły strategii, noty, szablony i źródła prezentacji |
| [`documents/manifest.yaml`](documents/manifest.yaml) | kanoniczny rejestr 17 artefaktów |
| [`research/`](research/) | źródła, twierdzenia, definicje, decyzje, luki, ryzyka i sprzeczności |
| [`reports/`](reports/) | raporty walidacji, red-team, QA i noty wydania |
| [`assets/`](assets/) | ilustracje, wykresy, prompty i metadane pochodzenia |
| [`tooling/`](tooling/) | generowanie HTML/PDF/DOCX/PPTX/XLSX oraz automatyczna walidacja |
| [`release/v0.1/`](release/v0.1/) | zamrożona, wersjonowana migawka do prywatnej recenzji |
| [`landingpage/`](landingpage/) | kod landing page i odrębny manifest publikacyjny |

<a id="landing-page"></a>
## Landing page

Landing page nie publikuje automatycznie plików z `documents/` ani `release/`. Rejestr kafli strony znajduje się w [`landingpage/documents.json`](landingpage/documents.json). Obecnie wszystkie pozycje pozostają w stanie `preparing`, bez publicznych odnośników do dokumentów.

Publikacja wymaga oczyszczonego HTML i PDF z tego samego zatwierdzonego źródła, ponownej kontroli treści i linków oraz jawnej zgody człowieka. Audyt wykazał też niespójności landing page z pakietem v0.1; nie należy traktować strony jako źródła prawdy dla treści strategii.

<a id="budowa-i-kontrola"></a>
## Budowa i kontrola

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make validate
make release-check
make package
```

`make release-check` synchronizuje pakiety badawcze, waliduje schematy i użycie twierdzeń, buduje wszystkie formaty oraz sprawdza strukturę HTML/PDF/DOCX/PPTX/XLSX. Wyniki robocze trafiają do ignorowanego przez Git katalogu `dist/`. `make package` tworzy wersjonowaną migawkę w `release/v0.1/` wraz z `SHA256SUMS`.

Instrukcja wydania znajduje się w [`release/README.md`](release/README.md). Integralność migawki można sprawdzić poleceniem:

```bash
cd release/v0.1
sha256sum -c SHA256SUMS
```

Pipeline generuje tagowane PDF-y z wariantem `PDF/UA-1` i wymusza A4 w DOCX. Automatyczna kontrola dowodzi obecności drzewa tagów, nie zastępuje pełnego audytu zgodności PDF/UA przez specjalistę i czytniki asystujące.

<a id="zasady-publikacji"></a>
## Zasady publikacji

- Repozytorium robocze pozostaje prywatne.
- Publiczna wersja powstaje jako oczyszczony eksport bez historii roboczej.
- Żaden materiał nie jest publikowany ani wysyłany do instytucji bez bramki akceptacyjnej człowieka.
- Repozytorium nie może zawierać informacji niejawnych, danych operacyjnie wrażliwych ani sekretów dostępowych.
- Pliki `AGENTS.md`, `GOAL.md`, surowe rejestry badawcze i materiały ograniczone nie są publikowane przez mechanizm landing page.
- Ilustracja okładkowa jest syntetyczna i nie stanowi dowodu ani mapy. Platforma nie ujawniła dokładnej wersji modelu; repozytorium nie przypisuje jej niepotwierdzonej etykiety „GPT Image 2”.

Aktualny pakiet służy do prywatnej konsultacji eksperckiej. Publikacja, wysyłka do instytucji, deklaracja patronatu lub formalne przedłożenie pozostają decyzjami `HUMAN-ONLY`.
