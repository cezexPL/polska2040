# Jawny szablon aneksu ograniczonego

**Status:** wyłącznie jawna specyfikacja procesu — bez informacji niejawnych  
**Program:** Polska 2040: Suwerenność technologiczna  
**Stan wersji:** v0.1, 21 lipca 2026 r.

> Ten plik nie jest aneksem niejawnym i nie może nim zostać przez dopisanie treści chronionej. Wskazuje jedynie pytania, klasy danych, role, metadane, bramki i zasady sanitizacji. Właściwy aneks powstaje wyłącznie w autoryzowanym środowisku wskazanym przez właścicieli informacji.

## Executive Summary / Streszczenie wykonawcze

### Cel

Szablon pozwala połączyć jawną strategię z odpowiedziami, których nie można bezpiecznie przechowywać w repozytorium. Każde pytanie ma właściciela decyzji, właściciela informacji, minimalny potrzebny zakres, podstawę dostępu, termin ważności i formę agregatu możliwego do zwrotu do dokumentu jawnego.

### Zasady bez wyjątków

1. Repozytorium prywatne lub publiczne nie jest systemem dla informacji niejawnych.
2. Klauzulę i zasady dostępu nadaje uprawniony właściciel informacji, nie autor strategii.
3. Zbieramy najmniejszy zakres potrzebny do konkretnej decyzji.
4. Brak dostępu zapisuje się jako status, nie próbuje rekonstruować z pośrednich danych.
5. Do warstwy jawnej wraca wyłącznie zatwierdzony agregat, przedział lub jakościowy wniosek.
6. Każdy eksport przechodzi kontrolę ujawnienia i zatwierdzenie właściciela.
7. Dane źródłowe, notatki robocze i wyniki pośrednie pozostają w środowisku autoryzowanym.
8. Naruszenie procesu zatrzymuje analizę i uruchamia właściwą procedurę incydentu.

### Oczekiwany produkt

Warstwa jawna otrzymuje odpowiedzi typu:

- „ryzyko przekracza przyjętą tolerancję — decyzja wymagana”;
- „istnieje przetestowana alternatywa dla większości elementów w klasie”;
- „wartość bazowa została ustalona, lecz może być publikowana tylko jako indeks”;
- „brak danych wystarczających do decyzji skali”;
- „wniosek może być ujawniony po agregacji według zatwierdzonej metody”.

Nie otrzymuje surowych wolumenów, lokalizacji, bibliotek, parametrów, podatności ani informacji o pojedynczych podmiotach, jeżeli właściciel ich nie dopuści.

## 1. Rozdzielenie środowisk

| Warstwa | Zawartość | Przykładowy produkt | Miejsce |
|---|---|---|---|
| jawna | cele, definicje, pytania, źródła publiczne, agregaty | strategia, dashboard publiczny | repozytorium i publikacja po akceptacji |
| wewnętrzna wrażliwa | dane prawnie chronione, tajemnica przedsiębiorstwa, dane osobowe | analiza ograniczona i notatka do decyzji | zatwierdzony system instytucji |
| niejawna | informacje z nadaną klauzulą | aneks i analiza dla uprawnionych | właściwy system/kancelaria |
| wynik sanitizowany | zatwierdzony agregat lub wniosek | claim do strategii jawnej | repozytorium po bramce ujawnienia |

Warstwy nie różnią się wyłącznie uprawnieniem użytkownika. Mogą wymagać innych systemów, urządzeń, pomieszczeń, procedur, retencji, logowania i sposobu komunikacji.

## 2. Karta zapytania do aneksu

Każde pytanie otrzymuje rekord:

| Pole | Wymaganie |
|---|---|
| `query_id` | stabilny identyfikator, np. AQ-001 |
| decyzja | konkretna decyzja, którą informacja zmienia |
| właściciel decyzji | organ/osoba `A` w RACI |
| pytanie | jedna sprawdzalna jednostka |
| minimalny zakres | najmniejsza szczegółowość wystarczająca |
| horyzont | rok/okres i data aktualności |
| właściciel informacji | podmiot mogący dopuścić dostęp/ujawnienie |
| podstawa | podstawa przetwarzania i udostępnienia |
| środowisko | autoryzowany system i tryb pracy |
| odbiorcy | role z potrzebą wiedzy |
| klasy danych | kategorie potrzebnych danych |
| metoda | sposób analizy i kontroli jakości |
| produkt | forma odpowiedzi do decydenta |
| agregat jawny | minimalny bezpieczny wynik, jeżeli możliwy |
| termin | data odpowiedzi i data utraty aktualności |
| status | otwarte, w toku, odpowiedziane, brak dostępu, zamknięte |
| zatwierdzenie | osoba/organ dopuszczający produkt i eksport |

### Wzór

```text
query_id: AQ-...
decyzja: ...
właściciel_decyzji: ...
pytanie: ...
minimalny_zakres: ...
horyzont: ...
właściciel_informacji: ...
podstawa: ...
środowisko: ...
odbiorcy_role: ...
klasy_danych: ...
metoda: ...
produkt_autoryzowany: ...
proponowany_agregat_jawny: ...
ważne_do: ...
status: ...
zatwierdził: ...
```

## 3. Katalog pytań strategicznych

Poniższe pytania są kategoriami. Właściciel informacji może je rozbić, ograniczyć lub odrzucić.

### 3.1. Luki i scenariusze

- Które efekty zdolnościowe są krytyczne w horyzontach 2027, 2030 i 2035?
- Które luki mogą być częściowo adresowane technologiami autonomicznymi, a które wymagają innych instrumentów?
- Jaki poziom degradacji jest akceptowalny i kto akceptuje ryzyko?
- Jakie założenia scenariusza najbardziej zmieniają priorytet?
- Które odpowiedzi mogą zostać opublikowane jako ranking, indeks lub przedział?

**Zabronione w warstwie jawnej bez zatwierdzenia:** szczegółowe wymagania, parametry misji, rozmieszczenie, podatności i konfiguracje.

### 3.2. Popyt, wolumeny i tempo odtworzenia

- Jaki popyt wynika z zatwierdzonych planów, a jaki jest jedynie scenariuszem?
- Jakie tempo strat, zużycia, naprawy i odtworzenia przyjęto w analizie?
- Które wolumeny powinny być stałym zapasem, zdolnością produkcyjną lub opcją kontraktową?
- Jaki jest horyzont 30/90/180 dni dla klas, nie pojedynczych zakładów?
- Czy jawny raport może użyć indeksu gotowości bez odtwarzalności wartości źródłowej?

### 3.3. Przemysł i łańcuchy dostaw

- Jaka jest zweryfikowana, powtarzalna zdolność, a jaka deklaracja nominalna?
- Które maszyny, materiały, komponenty, software, licencje i kompetencje są wąskim gardłem?
- Które elementy mają przetestowaną alternatywę i czas kwalifikacji?
- Jaki jest plan przy braku dostawcy, energii, transportu lub personelu?
- Jakie prawa do dokumentacji, serwisu i produkcji są faktycznie wykonalne?

**Zabronione w warstwie jawnej bez zatwierdzenia:** dokładne moce pojedynczych zakładów, zapasy, topologia, lokalizacje, chronieni dostawcy i pojedyncze punkty awarii.

### 3.4. Serwis, logistyka i konfiguracja

- Jaki jest rzeczywisty czas naprawy i udział napraw możliwych na kolejnych poziomach?
- Czy istnieje pełna historia konfiguracji sprzętu, software i modeli?
- Jakie części, narzędzia i uprawnienia są potrzebne do utrzymania?
- Czy przetestowano aktualizację, wycofanie i migrację do alternatywy?
- Które agregaty niezawodności można opublikować bez ujawnienia słabości?

### 3.5. Dane i AI

- Kto jest właścicielem każdego zbioru i jaka jest podstawa użycia?
- Czy dane są reprezentatywne, kompletne i wersjonowane?
- Który zbiór jest treningowy, walidacyjny i odseparowany testowy?
- Jakie ograniczenia modelu i warunki bezpiecznej degradacji potwierdzono?
- Kto ma prawo dopuścić, monitorować, ograniczyć i wycofać model?
- Jaki wynik benchmarku może zostać ujawniony w agregacie?

**Zabronione w warstwie jawnej bez zatwierdzenia:** surowe dane operacyjne, etykiety ujawniające metody, biblioteki sygnałów, szczegółowe wyniki odporności i konfiguracje.

### 3.6. Cyber i software supply chain

- Czy artefakty, zależności i aktualizacje mają pełny ślad pochodzenia?
- Jak monitorowane są podatności, incydenty i koniec wsparcia?
- Czy testowano utratę usługi, aktualizacji lub dostępu dostawcy?
- Jakie prawa i kompetencje pozwalają bezpiecznie utrzymać system?
- Jak zagregować dojrzałość bez ujawnienia konkretnej podatności?

**Zabronione:** publikacja nieusuniętych podatności, exploitów, szczegółów konfiguracji ochrony, kluczy i danych uwierzytelniających.

### 3.7. Kadry i mobilizacja kompetencji

- Które role są ograniczeniem krytycznym i ile czasu wymaga ich przygotowanie?
- Jaka jest retencja, dostępność instruktorów i wpływ mobilności?
- Które kompetencje mają pojedyncze osoby lub zespoły?
- Jak zabezpieczyć ciągłość po odejściu personelu kluczowego?
- Jakie dane można publikować bez identyfikacji osoby lub małej jednostki?

### 3.8. Finanse i zobowiązania

- Jakie koszty i zobowiązania już istnieją w programach w zakresie?
- Które źródła finansowania pokrywają ten sam koszt?
- Jaka jest ekspozycja warunkowa, koszt obsługi i pełny TCO?
- Jakie przyjęto założenia kursowe, cenowe, harmonogramowe i dotyczące wykorzystania?
- Które wartości można opublikować jako zakres lub udział bez ryzyka?

### 3.9. Partnerstwa, IP i bezpieczeństwo właścicielskie

- Kto kontroluje partnera i jakie są prawa osób trzecich?
- Jakie sankcje, ograniczenia eksportowe i obowiązki end-use mają zastosowanie?
- Gdzie powstaje IP i kto ma prawa do ulepszeń, danych, kodu i produkcji?
- Co dzieje się po zmianie właściciela, jurysdykcji lub sytuacji politycznej?
- Jakie elementy due diligence mogą być opisane jako status bez ujawnienia źródła?

### 3.10. Prawo, etyka i odpowiedzialność

- Kto podejmuje i dokumentuje decyzję o dopuszczeniu oraz ryzyku?
- Jakie prawo, procedura i nadzór mają zastosowanie?
- Czy istnieje możliwość ludzkiego nadzoru, interwencji i bezpiecznego wycofania?
- Jak rejestrowane są decyzje, dane i wersje dla audytu?
- Czy jawny wniosek może potwierdzić zgodność bez ujawnienia szczegółów?

## 4. Role i separacja obowiązków

| Rola | Odpowiedzialność | Nie może samodzielnie |
|---|---|---|
| właściciel decyzji | określa pytanie i akceptuje ryzyko | zmieniać klauzuli informacji innego właściciela |
| właściciel informacji | klasyfikuje, udostępnia, ogranicza i zatwierdza eksport | zatwierdzać merytorycznego wyniku za decydenta |
| kierownik środowiska | dostęp, logi, konfiguracja i incydenty | rozszerzać celu przetwarzania |
| analityk | wykonuje minimalną analizę i zapisuje ograniczenia | kopiować dane poza środowisko |
| recenzent | odtwarza metodę i kwestionuje wniosek | być jedynym autorem tego samego wyniku |
| bezpieczeństwo/ochrona danych | kontrola zgodności i ryzyka | zastępować decyzję polityczną |
| sanitizator | przygotowuje wersję możliwą do ujawnienia | sam zatwierdzać publikacji |
| approver eksportu | dopuszcza konkretny artefakt | udzielać zgody blankietowej na przyszłe wersje |
| audyt | sprawdza ślad i przestrzeganie reguł | zmieniać danych źródłowych |

## 5. Workflow analizy autoryzowanej

### Krok 1 — przyjęcie pytania

- sprawdzenie decyzji, proporcjonalności i minimalnego zakresu;
- potwierdzenie właścicieli;
- określenie środowiska i odbiorców;
- odrzucenie pytań „na wszelki wypadek”.

### Krok 2 — udostępnienie

- przyznanie imiennego, czasowego dostępu;
- obowiązkowe szkolenie i akceptacja zasad;
- rejestr plików, zbiorów i wersji;
- zakaz użycia prywatnych urządzeń, chmur i narzędzi niezatwierdzonych.

### Krok 3 — analiza

- kod/metoda pozostają w środowisku;
- wynik ma dane wejściowe, założenia, ograniczenia i recenzenta;
- sprzeczności nie są usuwane;
- każdy wykres przechowuje tabelę źródłową i transformację.

### Krok 4 — recenzja

- odtworzenie obliczenia na zatwierdzonej próbce;
- kontrola dostępu i celu;
- red-team wniosku oraz ryzyka agregacji;
- decyzja: przyjąć, poprawić, ograniczyć albo odrzucić.

### Krok 5 — sanitizacja

- usuwa identyfikatory, dokładność, małe komórki i kombinacje pozwalające odtworzyć źródło;
- porównuje z innymi publicznymi danymi pod kątem inferencji;
- wybiera najniższą szczegółowość wystarczającą do decyzji jawnej;
- zapisuje, co usunięto i dlaczego w środowisku autoryzowanym.

### Krok 6 — eksport

- właściciel informacji zatwierdza konkretną wersję i kanał;
- plik otrzymuje checksumę, datę i okres ważności;
- eksport jest logowany;
- w repozytorium powstaje nowy claim z publicznym źródłem/zgodą i recenzentem.

### Krok 7 — zamknięcie

- odebranie dostępu;
- retencja/usunięcie zgodnie z regułą;
- zapis lekcji i incydentów;
- termin ponownej weryfikacji.

## 6. Matryca form odpowiedzi

| Forma | Kiedy użyć | Przykład bez treści wrażliwej |
|---|---|---|
| odpowiedź binarna | decyzja wymaga tylko spełnienia warunku | spełniono / nie spełniono |
| status RAG | monitorowanie wielu obszarów | zielony / bursztynowy / czerwony z definicją |
| indeks | dokładna wartość jest zbyt wrażliwa | baza 2026 = 100, zmiana trendu |
| przedział | dokładność nie jest potrzebna | niski / średni / wysoki zakres |
| percentyl | porównanie bez jednostki źródłowej | wynik powyżej ustalonego progu |
| ranking | priorytet bez ujawnienia wielkości | grupa A/B/C z kryteriami |
| jakościowy wniosek | monetyzacja/kwantyfikacja byłaby myląca | ryzyko nieakceptowalne bez alternatywy |
| brak odpowiedzi | nawet agregat tworzy szkodę | status: dostęp tylko autoryzowany |

Status RAG bez definicji i progu jest niedopuszczalny. Przedział nie może być tak wąski, by ujawniał wartość, ani tak szeroki, by nie zmieniał decyzji.

## 7. Kontrola ujawnienia

### Checklista przed eksportem

- Czy odbiorca i decyzja nadal są aktualne?
- Czy wynik zawiera najmniejszy potrzebny zakres?
- Czy można połączyć go z publicznym źródłem i odtworzyć informację chronioną?
- Czy małe komórki, skrajne wartości lub metadane identyfikują podmiot?
- Czy czas, lokalizacja albo szczegół techniczny ujawniają podatność?
- Czy wykres ma osie, komentarze lub nazwę pliku zdradzające więcej niż treść?
- Czy usunięto komentarze, warstwy, historię zmian i metadane dokumentu?
- Czy eksport nie narusza praw osoby trzeciej, danych osobowych lub tajemnicy przedsiębiorstwa?
- Czy właściciel informacji zatwierdził tę konkretną wersję?
- Czy ustawiono datę ponownego sprawdzenia lub wycofania?

### Test inferencji

Sanitizator porównuje proponowany agregat z innymi danymi publicznymi i wcześniej opublikowanymi agregatami. Bezpieczne osobno liczby mogą ujawnić wartość po odjęciu. W takim przypadku zmienia się grupowanie, okres, miarę albo nie publikuje wyniku.

## 8. Rejestr wyjść do warstwy jawnej

| Pole | Opis |
|---|---|
| `release_id` | identyfikator eksportu |
| `query_id` | pytanie źródłowe |
| `public_claim` | dokładne dopuszczone brzmienie |
| `form` | indeks/przedział/status/wniosek |
| `as_of` | data stanu wiedzy |
| `valid_until` | data ponownego sprawdzenia |
| `owner` | właściciel informacji |
| `approved_by` | osoba/organ zatwierdzający |
| `checksum` | suma konkretnego artefaktu |
| `restrictions` | dozwolone użycie i kanał |
| `withdrawal` | sposób wycofania po zmianie stanu |

Repozytorium przechowuje wyłącznie dopuszczony `public_claim` i jawne metadane zaakceptowane do publikacji, nie ukryte źródło ani uzasadnienie klasyfikacji.

## 9. Incydenty i zatrzymanie pracy

Incydent obejmuje m.in. dostęp bez potrzeby wiedzy, skopiowanie do niewłaściwego systemu, użycie niezatwierdzonego narzędzia, próbę rekonstrukcji, utratę urządzenia, ujawnienie w komentarzu/metadanych lub wysłanie niezatwierdzonej wersji.

Minimalna odpowiedź:

1. zatrzymać dalsze kopiowanie i analizę;
2. nie usuwać śladów poza poleceniem właściwej procedury;
3. powiadomić właściciela informacji i bezpieczeństwo;
4. odebrać lub ograniczyć dostęp;
5. ustalić zakres oraz odbiorców;
6. uruchomić właściwe obowiązki prawne i organizacyjne;
7. wycofać publiczny artefakt, jeżeli konieczne;
8. zapisać działania naprawcze i warunek wznowienia.

Repozytorium nie powinno przechowywać szczegółów incydentu, jeżeli nie zostały dopuszczone. Może zawierać status „materiał wycofany” i publiczne wyjaśnienie zatwierdzone przez właściciela.

## 10. Bramka pass/fail

Zapytanie otrzymuje `FAIL`, jeżeli:

- nie ma decyzji ani właściciela;
- zakres jest szerszy niż potrzebny;
- nie wskazano podstawy, środowiska lub odbiorców;
- analityk jest jedynym recenzentem;
- nie istnieje metoda kontroli ujawnienia;
- proponowany agregat pozwala odtworzyć dane źródłowe;
- produkt ma trafić do repozytorium przed zatwierdzeniem;
- data lub wersja danych jest nieznana;
- użycie narzędzia nie zostało zatwierdzone;
- nie ma procedury odebrania dostępu i retencji.

`PASS` oznacza zgodę na konkretny etap i zakres, nie blankietowy dostęp do kolejnych danych.

## 11. Minimalny pakiet dla decydenta

Decydent powinien otrzymać:

1. pytanie i znaczenie dla decyzji;
2. odpowiedź oraz poziom pewności;
3. datę, zakres i ograniczenia;
4. scenariusz przeciwny lub zdanie red-team;
5. konsekwencje wariantów;
6. ryzyko, którego nie udało się zmierzyć;
7. rekomendację i właściciela;
8. termin ponownego sprawdzenia;
9. jawny agregat, jeśli został dopuszczony;
10. informację, czego nie wolno dalej udostępniać.

## Dalsze pytania

- Które instytucje są właścicielami poszczególnych klas odpowiedzi?
- Jakie autoryzowane środowiska i narzędzia są dostępne dla wspólnej analizy?
- Jak testować ryzyko inferencji między kolejnymi raportami publicznymi?
- Kto zatwierdza indeksy i przedziały dla dashboardu?
- Jak szybko wycofać claim po zmianie stanu lub wykryciu ryzyka?

## Zastrzeżenia i założenia

- Szablon nie zastępuje ustawy o ochronie informacji niejawnych, kancelarii tajnej, polityk instytucji, RODO, tajemnicy przedsiębiorstwa ani innych obowiązków.
- Kategorie w dokumencie nie nadają klauzuli ani uprawnienia.
- Właściciel może odmówić odpowiedzi lub ograniczyć jej formę.
- Informacji chronionej nie wolno umieszczać w komentarzu, issue, PR, mailu, komunikatorze ani narzędziu AI bez właściwego dopuszczenia.
- Brak jawnej odpowiedzi nie jest dowodem braku zdolności, danych lub działania państwa.
