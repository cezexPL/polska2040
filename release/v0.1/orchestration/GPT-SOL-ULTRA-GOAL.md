# Runbook Goal — Polska 2040

## 1. Polecenie nadrzędne

Buduj i utrzymuj audytowalny, niezależny oraz bezpartyjny pakiet strategiczny „Polska 2040: Suwerenność technologiczna”. Pakiet ma wspierać decyzje Prezesa Rady Ministrów, Rady Ministrów, Prezydenta RP, BBN, resortów, samorządów i partnerów gospodarczych, lecz nie może sugerować ich poparcia ani zastępować formalnego procesu państwowego.

Pierwsza sesja wykonawcza może trwać maksymalnie 24 godziny. Kolejne sesje są aktualizacjami wersjonowanymi, nie ponownym pisaniem całości od zera.

## 2. Definicja wyniku

Wynikiem nie jest jeden monolit. Kanoniczny pakiet składa się z modułów, z których budowane są wersje dla różnych odbiorców:

1. strategia jawna;
2. plan realizacji 2026–2040;
3. finansowanie i ocena wpływu wraz z modelem XLSX;
4. ład instytucjonalny, prawo i zamówienia;
5. księga dowodowa;
6. jawny szablon przyszłego aneksu ograniczonego;
7. nota dla Premiera i Rady Ministrów;
8. nota dla Prezydenta i BBN;
9. briefy portfeli ministerialnych;
10. anglojęzyczny executive brief;
11. prezentacje: RM, Prezydent/BBN, forum gospodarcze, regiony i odbiorcy międzynarodowi;
12. karta kwalifikacji pilotażu regionalnego i szablon danych wojewódzkich;
13. infografiki, metadane ich pochodzenia i powtarzalny proces budowy.

Pliki z `documents/` są źródłem kanonicznym. `dist/` jest wynikiem kompilacji i nie podlega ręcznej korekcie.

## 3. Granice

- Wyłącznie źródła jawne i legalnie dostępne.
- Zero sekretów dostępowych, danych osobowych bez podstawy, informacji niejawnych, podatności, częstotliwości, parametrów operacyjnych i instrukcji budowy lub użycia uzbrojenia.
- Brak źródła oznacza `UNKNOWN`, nie liczbę wygenerowaną dla kompletności.
- Model językowy, snippet wyszukiwarki i materiał dostawcy bez niezależnej kontroli nie są samodzielnym dowodem.
- Repozytorium robocze pozostaje prywatne. Publikacja, wysłanie do instytucji, kontakt z urzędnikiem, zatwierdzenie budżetu i użycie informacji niejawnej są bramkami `HUMAN-ONLY`.
- Wersja jawna opisuje pytania do przyszłego bezpiecznego obiegu, ale nie próbuje odtwarzać odpowiedzi.

## 4. Stan trwały

Przed działaniem odczytaj:

1. `README.md` i `GOAL.md`;
2. `documents/manifest.yaml`;
3. rejestry w `research/`;
4. ukończone pakiety oznaczone `research/packs/*.complete`;
5. otwarte P0/P1/P2 w raportach walidacyjnych;
6. bieżący branch, czystość worktree i stan draft PR;
7. wynik ostatniego `make release-check`.

Nie importuj pakietu agenta bez markera `.complete`. Nie nadpisuj zaakceptowanej syntezy tylko dlatego, że nowy agent ma inną preferencję; zapisuj konflikt i przedstaw warianty.

## 5. Graf wykonania

### Fala 0 — kontrola wejścia

- Znormalizuj materiał inicjujący jako hipotezy.
- Sprawdź daty, nazwy instytucji, system oświaty, status programów i znaczenie kwot.
- Utwórz rejestr sprzeczności i krytycznych luk.
- Nie przenoś błędu z briefu do executive summary.

### Fala 1 — państwo i bezpieczeństwo

- A01: bezpieczeństwo, NATO i doktryna;
- A02: realizacja rządowa i koordynacja;
- A03: potrzeby użytkowników i zamówienia iteracyjne.

### Fala 2 — technologia i wykonanie

- A04: systemy autonomiczne;
- A05: AI, dane, obliczenia i cyber;
- A06: przemysł, komponenty, produkcja i serwis.

### Fala 3 — ekonomia i partnerstwa

- A07: finanse i wpływ;
- A08: Ukraina, UE, NATO, JV i eksport;
- A09: prawo, etyka i bezpieczeństwo informacji.

### Fala 4 — ludzie i dyfuzja

- A10: edukacja, kadry i retencja;
- A11: zastosowania cywilne, regiony, MŚP i produktywność.

### Fala kontrolna

- A12 sprawdza źródła niezależnie od autora, próbuje obalić wnioski, prowadzi listę P0/P1/P2 i wydaje ocenę gotowości.
- A12 nie zatwierdza hurtowo rekomendacji. Weryfikuje fakty i jakość wnioskowania.
- Po każdej dużej syntezie wykonaj ponowną falę A12 na dokumentach końcowych, a nie tylko rejestrze twierdzeń.

Liczba równoległych agentów nie może przekraczać aktualnego limitu środowiska. Zawsze pozostaw jednego koordynatora odpowiedzialnego za scalanie, konflikty identyfikatorów i spójność narracji.

## 6. Atomowa pętla badawcza

Dla każdego pytania wykonaj:

1. **Pytanie:** zdefiniuj decyzję, odbiorcę i warunek, przy którym odpowiedź zmienia rekomendację.
2. **Wyszukiwanie:** zacznij od aktu, datasetu lub dokumentu instytucji odpowiedzialnej; użyj drugiej strategii wyszukiwania, gdy wynik jest pusty, wtórny lub wątpliwy.
3. **Otwarcie:** przeczytaj właściwy dokument, nie wynik wyszukiwarki.
4. **Rejestracja źródła:** zapisz `SRC-####`, tytuł, wydawcę, datę, URL, datę dostępu, typ, poziom i dokładny lokalizator.
5. **Atomizacja:** jedno `CLM-####` powinno zawierać jedno sprawdzalne twierdzenie.
6. **Klasyfikacja:** oznacz `FACT`, `ESTIMATE`, `SCENARIO`, `INFERENCE`, `RECOMMENDATION` albo `UNKNOWN`.
7. **Recenzja:** inna persona sprawdza zgodność tekstu twierdzenia z zakresem źródła, datą i zastrzeżeniami.
8. **Synteza:** porównaj status quo, wariant minimalny, rekomendowany i maksymalny/alternatywny.
9. **Falsyfikacja:** zapisz, jaki dowód obaliłby rekomendację i kiedy program należy zamknąć.
10. **Użycie:** dopiero `verified` może być cytowane jako fakt w artefakcie publikacyjnym.

## 7. Przejścia statusu twierdzenia

```text
unverified ──niezależna kontrola──> verified
     │                                  │
     ├──sprzeczne dowody────────────> disputed
     └──utrata aktualności/decyzja──> retired
```

- Autor i recenzent muszą być różni.
- `verified` nie znaczy „wiecznie prawdziwe”; każde twierdzenie ma `as_of`.
- Twierdzenie zmienne sprawdza się ponownie przy wydaniu.
- Nowy fakt bez pełnego śladu pozostaje w memorandum badawczym, nie w nocie wykonawczej.

## 8. Reguły liczb i modelu

Każda liczba ma:

- jednostkę i walutę;
- okres i datę aktualności;
- mianownik lub populację;
- rok cen oraz kurs, jeśli są potrzebne;
- identyfikator źródła/twierdzenia albo etykietę `SCENARIO`;
- właściciela i plan odświeżenia.

Model finansowy nie jest prognozą. Puste wejście pozostaje `UNKNOWN`; nie jest zerem. Oddzielaj zobowiązania, płatności, gwarancje, finansowanie pożyczkowe, istniejący baseline, koszt finansowania, przyrostowy koszt programu i pełny TCO. Jeden koszt ma jeden identyfikator, aby zapobiec podwójnemu finansowaniu.

## 9. Synteza i format dla odbiorcy

- **Premier/RM:** decyzja, warianty, właściciel, termin, koszt decyzji odwracalnej, ryzyka i sprawy do powrotu na RM.
- **Prezydent/BBN:** ciągłość państwa, odporność, zgodność sojusznicza, horyzont wieloletni, pytania do bezpiecznego aneksu.
- **Minister:** mandat portfela, zależności, pierwsze 100 dni, dane do dostarczenia, KPI i konflikty do eskalacji.
- **Forum gospodarcze:** problem produktywności, popyt, reguły rynku, kapitał, eksport i warunki udziału sektora prywatnego.
- **Region:** kryteria wyboru pilotażu, role samorządu, MŚP, szkoły i infrastruktura; bez kopiowania liczb między województwami.
- **Odbiorca międzynarodowy:** interoperacyjność, współpraca UE/NATO/Ukraina, standardy, bezpieczeństwo IP i propozycja mierzalnego partnerstwa.

Każdy format ma własną funkcję; nie jest mechanicznym skrótem tego samego dokumentu.

## 10. Pętla budowy i QA

Po każdej zamkniętej fali:

```bash
make sync
make validate
make audit
make build
make qa
```

Następnie:

1. sprawdź reprezentatywne strony pierwsze, środkowe i ostatnie wszystkich typów dokumentu;
2. sprawdź każdy slajd pod kątem przepełnienia, ucięcia, podwójnych stopek i niespójnej skali;
3. sprawdź DOCX, PPTX i XLSX jako struktury, nie tylko rozszerzenia plików;
4. zweryfikuj liczbę stron/slajdów, A4 w DOCX oraz tagowanie dostępności PDF;
5. sprawdź linki, obrazy, źródła zewnętrzne, brak sekretów i treści wrażliwych;
6. usuń, osłab albo oznacz każdą tezę, której dowód nie odpowiada dokładnie jej brzmieniu;
7. zapisz wynik i znane ograniczenia w raporcie walidacyjnym.

## 11. Priorytety usterek

- **P0:** fałszywy lub niezweryfikowany fakt w nocie wykonawczej, sekret/informacja wrażliwa, istotnie błędna liczba, sugestia oficjalnego poparcia, uszkodzony wymagany artefakt. Blokuje wydanie.
- **P1:** rekomendacja wykracza poza dowody, brak właściciela decyzji, podwójne liczenie, luka prawna przedstawiona jako pewność, render utrudniający użycie. Wymaga naprawy albo jawnego odstępstwa przed wydaniem.
- **P2:** redakcja, styl, drugorzędne metadane lub dodatkowa możliwość poprawy. Nie blokuje draftu, lecz pozostaje w backlogu.

## 12. Bramki człowieka

Model zatrzymuje się i prosi o decyzję człowieka przed:

- upublicznieniem repozytorium lub materiałów;
- wysłaniem dokumentu do RM, KPRM, Prezydenta, BBN, ministerstwa lub partnera;
- zatwierdzeniem nazwiska patrona, składu rady, dostawcy, lokalizacji, budżetu albo zobowiązania liczbowego;
- użyciem materiału chronionego lub wejściem do systemu wymagającego poświadczeń;
- scaleniem do `main`, jeśli polecenie obejmuje tylko draft PR.

## 13. Warunek ukończenia v0.1

Sesja może zostać oznaczona jako kompletna wyłącznie, gdy:

- wszystkie pozycje `documents/manifest.yaml` istnieją i zostały zbudowane;
- rejestry oraz wszystkie ukończone pakiety przechodzą schematy;
- noty wykonawcze nie zawierają niezweryfikowanych faktów;
- A12 nie pozostawił P0, a każde P1 jest naprawione albo jawnie zaakceptowane jako zastrzeżenie;
- model XLSX zachowuje `UNKNOWN`, a formuły i arkusze przechodzą kontrolę strukturalną;
- reprezentatywne rendery zostały obejrzane;
- PDF-y mają tagi i deklarowany wariant PDF/UA-1, a ograniczenie braku pełnej certyfikacji jest jawne;
- README zawiera aktualny spis treści, stan wydania, polecenia budowy i znane ograniczenia;
- branch jest wypchnięty, CI przechodzi, a draft PR opisuje dowody, luki, ryzyka i zakres decyzji człowieka;
- nie wykonano publikacji ani merge bez odrębnego upoważnienia.

## 14. Protokół wznowienia

Po przerwaniu nie zaczynaj od nowa. Odczytaj stan trwały, uruchom walidację, znajdź pierwszą niespełnioną bramkę, sprawdź aktualność twierdzeń zależnych od czasu i kontynuuj od najmniejszego bezpiecznego zadania. W nowym wydaniu zachowaj historię sprzeczności, wycofań i zmian rekomendacji.
