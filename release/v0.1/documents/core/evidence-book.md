# Księga dowodowa

## Executive Summary / Streszczenie wykonawcze

- **Księga oddziela dowody od narracji.** Każde ważne twierdzenie ma status, źródło, datę i recenzenta.
- **Niepewność pozostaje widoczna.** Sprzeczne i niedostępne dane nie są usuwane z rejestru.
- **Dokument jest generowany z rejestrów.** Kolejne wydania pokażą historię zmian i wycofane twierdzenia.

## Spis treści

[TOC]

## Jak czytać księgę

Poniżej automatycznie dołączane są rejestry: źródeł, twierdzeń, użycia twierdzeń w artefaktach, sprzeczności, luk danych, definicji, decyzji i ryzyk. Identyfikator `SRC-####` prowadzi do opisu źródła; `CLM-####` do konkretnego twierdzenia; `DEF-####` i `DEC-####` do kontrolowanej definicji lub kandydata decyzji. Status `verified` oznacza recenzję przez osobę inną niż autor twierdzenia, a `unverified` — materiał badawczy, którego nie wolno cytować jako potwierdzonego faktu w dokumencie publikacyjnym.

## Reguła użycia

Rejestr jest szerszy niż treść strategii. Zachowuje również hipotezy odrzucone, sprzeczne i jeszcze niesprawdzone, aby proces był audytowalny. Z tego powodu sam fakt obecności rekordu w Księdze nie jest potwierdzeniem jego prawdziwości.

## Zakres automatycznej kompilacji


- `research/sources.yaml` — metadane i status źródeł;
- `research/claims.yaml` — typ, status, pewność, dowody i recenzent twierdzenia;
- `research/claim-usage.yaml` — dokumenty, w których wykorzystano dane twierdzenie;
- `research/contradictions.yaml` — nierozstrzygnięte i rozstrzygnięte konflikty źródeł;
- `research/gaps.yaml` — pytania wymagające danych lub decyzji właściciela;
- `research/definitions.yaml` — kontrolowany słownik pojęć;
- `research/decisions.yaml` i `research/risks.yaml` — kolejka kandydatów decyzji oraz ryzyk.

## Dalsze pytania

Które luki mogą zmienić rekomendację, a które wpływają jedynie na jej skalę?

## Zastrzeżenia i założenia

Brak źródła w księdze oznacza brak podstawy do publicznego użycia twierdzenia.
