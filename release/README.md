# Wersjonowane pakiety wynikowe

Każdy katalog wersji jest migawką zbudowaną z kanonicznych źródeł w `documents/` i rejestrów w `research/`. Zawiera HTML, PDF, DOCX, PPTX, model XLSX, zasoby wizualne, manifest budowy, wynik strukturalnego QA i `SHA256SUMS`.

Migawka służy do recenzji w prywatnym repozytorium. Nie jest oficjalną publikacją ani materiałem zatwierdzonym przez państwo. Publiczne wydanie wymaga oddzielnej zgody, oczyszczonego eksportu i ponownego sprawdzenia danych zależnych od czasu.

## Jak czytać pakiet

Po zbudowaniu wersji:

1. otwórz `index.html` w katalogu danej wersji (np. `release/v0.1/index.html`), aby przejść do katalogu wszystkich 17 artefaktów;
2. przeczytaj `reports/validation-report-v0.1.md` w tym samym katalogu wersji;
3. sprawdź niezależne raporty `red-team-v0.1.md` i `visual-qa-v0.1.md`;
4. wybierz notę albo prezentację odpowiednią dla odbiorcy;
5. traktuj Księgę dowodową jako rejestr statusów, nie jako zbiór samych potwierdzonych faktów;
6. nie wysyłaj ani nie publikuj materiałów bez bramki akceptacyjnej człowieka.

`release-metadata.json` podaje status wydania i otwartą bramkę formalną. `build-manifest.json` opisuje artefakty, a `output-qa.json` zapisuje wynik kontroli strukturalnej.

Aktualizację wykonuje się dopiero po przejściu:

```bash
make release-check
make package
```

Nie poprawia się ręcznie plików w katalogu wersji; poprawkę wprowadza się w źródle i generuje cały pakiet ponownie.

Integralność gotowej migawki sprawdza się poleceniem:

```bash
cd release/v0.1
sha256sum -c SHA256SUMS
```
