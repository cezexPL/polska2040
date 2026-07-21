# Polska 2040: Suwerenność technologiczna

Niezależny, bezpartyjny i audytowalny projekt strategii państwa dotyczącej suwerenności technologicznej, systemów autonomicznych, AI oraz technologii podwójnego zastosowania.

> **Status:** prywatny draft ekspercki v0.1. To nie jest dokument rządowy ani stanowisko Prezydenta RP, Rady Ministrów, BBN, Sił Zbrojnych RP lub którejkolwiek instytucji publicznej.

## Wynik, który budujemy

Projekt ma połączyć problem operacyjny, dane, prototypowanie, testy, zamówienia, produkcję, kadry, finansowanie, eksport i aktualizację zdolności w jeden mierzalny system realizacji. Brakujące dane pozostają jawnie oznaczone jako nieznane; nie są zastępowane liczbami wygenerowanymi przez model.

## Spis treści repozytorium

- [`GOAL.md`](GOAL.md) — cel, harmonogram, warunki ukończenia i bramki jakości.
- [`AGENTS.md`](AGENTS.md) — role dwunastu doradców, kontrakty wyjściowe i zasady handoffu.
- [`METHODOLOGY.md`](METHODOLOGY.md) — metodologia źródeł, twierdzeń, syntezy i red-team.
- [`SECURITY.md`](SECURITY.md) — granice informacji jawnych, wrażliwych i niejawnych.
- [`DATA_POLICY.md`](DATA_POLICY.md) — sposób przechowywania źródeł, danych i metadanych.
- [`inputs/initial-brief.md`](inputs/initial-brief.md) — znormalizowany materiał inicjujący, traktowany jako zestaw hipotez.
- `research/` — rejestry źródeł, twierdzeń, decyzji, luk, ryzyk i sprzeczności.
- `documents/` — kanoniczne moduły strategii oraz dokumenty dla konkretnych odbiorców.
- `assets/` — wykresy, ilustracje, prompty i metadane pochodzenia.
- `tooling/` — budowa HTML/PDF/DOCX/PPTX i automatyczna walidacja.

## Artefakty v0.1

| Artefakt | Status |
|---|---|
| Strategia jawna | w przygotowaniu |
| Plan realizacji 2026–2040 | w przygotowaniu |
| Analiza finansowania i wpływu | w przygotowaniu |
| Ład instytucjonalny i prawny | w przygotowaniu |
| Nota dla Premiera i Rady Ministrów | w przygotowaniu |
| Pakiet dla Prezydenta i BBN | w przygotowaniu |
| Briefy resortowe | w przygotowaniu |
| Prezentacje: decyzyjna, gospodarcza, regionalna i międzynarodowa | w przygotowaniu |
| Jawny szablon aneksu ograniczonego | w przygotowaniu |
| Księga dowodowa | w przygotowaniu |

## Budowa i kontrola

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make validate
make build
```

Wyniki są zapisywane w `dist/`. Kanoniczna treść pozostaje w plikach źródłowych; pliki wynikowe nie są ręcznie poprawiane.

## Zasady publikacji

- Repozytorium robocze pozostaje prywatne.
- Publiczna wersja powstanie jako oczyszczony eksport bez historii roboczej.
- Żaden materiał nie jest publikowany ani wysyłany do instytucji bez bramki akceptacyjnej człowieka.
- Repozytorium nie może zawierać informacji niejawnych, danych operacyjnie wrażliwych ani sekretów dostępowych.

