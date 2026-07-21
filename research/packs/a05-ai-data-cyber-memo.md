# A05 — AI, dane, moc obliczeniowa i cyberbezpieczeństwo

## Executive Summary / Streszczenie wykonawcze

- **Polska potrzebuje federacyjnej bezpiecznej przestrzeni danych, a nie jednego centralnego „jeziora danych obronnych”.** Wspólne powinny być: reguły, tożsamość, katalog metadanych, format umów danych, ślad audytowy i bramki jakości. Dane pozostają u odpowiedzialnych stewardów, a w zastosowaniach wrażliwych domyślnym wzorcem jest przeniesienie zatwierdzonego obliczenia do danych oraz kontrola wyniku. `[INFERENCE: CLM-0530–CLM-0533]`

- **Moc obliczeniowa nie jest zdolnością państwową bez dopuszczenia, danych, usług i ciągłości.** Gaia AI Factory, PIAST-AI Factory i PLGrid tworzą ważny potencjał cywilno-badawczy, ale publiczne komunikaty nie dowodzą dostępności produkcyjnej, SLA ani dopuszczenia do chronionych danych obronnych. Potrzebny jest katalog poziomów C0–C3 z osobnym testem bezpieczeństwa, egress, łańcucha dostaw i odtworzenia dla każdego środowiska. `[FACT/UNKNOWN/INFERENCE: CLM-0507–CLM-0509, CLM-0528, CLM-0535–CLM-0536]`

- **System AI powinien być dopuszczany jako wersjonowany pakiet: cel, dane, model, kod, runtime, sprzęt, polityka i dowody.** Ewaluacja musi być ciągła, zależna od zastosowania i obejmować jakość celu, zachowanie poza typowym rozkładem, dryf, cyber, zasoby, human factors, bezpieczną degradację i rollback. Zmiana któregokolwiek elementu krytycznego uruchamia analizę wpływu i właściwy zakres ponownej oceny. `[FACT/INFERENCE: CLM-0501, CLM-0502, CLM-0503, CLM-0504, CLM-0505, CLM-0537, CLM-0538, CLM-0539, CLM-0540, CLM-0541]`

- **Minimalny poziom cyber musi powstać przed skalowaniem, nie po incydencie.** Kontrolowany build, pochodzenie zależności, SBOM, manifest modelu i danych, podpisane artefakty, zarządzanie podatnościami, aktualizacja, rollback i odporna ścieżka audytowa powinny być warunkiem odbioru nowych pilotaży państwowych od 2027 r. `[FACT/INFERENCE: CLM-0517, CLM-0520, CLM-0521, CLM-0522, CLM-0523, CLM-0524, CLM-0525, CLM-0542, CLM-0543, CLM-0544]`

**Odpowiedź dla Premiera i Prezydenta:** należy zatwierdzić państwowy kontrakt danych i AI assurance — wspólną architekturę federacyjną, role, poziomy compute, bramki TEVV, minimalny secure SDLC oraz reguły degradacji — a następnie sprawdzić go na dwóch lub trzech niewrażliwych pilotażach. Nie należy przenosić danych chronionych do repozytorium lub AI Factory na podstawie samego komunikatu projektowego. Szczegóły operacyjne, niejawne i techniczne pozostają w autoryzowanym obiegu, poza tym repozytorium.

## Mandat, odbiorca i granice

**Pytanie decyzyjne.** Jak zbudować bezpieczny i interoperacyjny stos danych, modeli i obliczeń, który przyspiesza eksperymenty oraz wdrażanie systemów AI, ale zachowuje odpowiedzialność za dane, kontrolę nad wersjami, odporność i możliwość niezależnego audytu?

**Odbiorca.** Premier i Rada Ministrów jako właściciele koordynacji i polityki cyfrowej; Prezydent i BBN jako odbiorcy oceny ciągłości strategicznej; Ministerstwo Cyfryzacji, MON, MNiSW, MSWiA, NASK, CSIRT-y, operatorzy PLGrid i AI Factories, właściciele danych, nabywcy publiczni, uczelnie i wykonawcy jako realizatorzy.

**Stan dowodów.** Źródła sprawdzono według stanu na 21 lipca 2026 r. Wyłącznie źródła urzędowe, akty prawne, dokumenty NATO/UE oraz publiczne abstrakty standardów stanowią bazę tego pakietu. Wszystkie twierdzenia autora A05 mają status `unverified` do niezależnej recenzji A12. Nie zbadano płatnych pełnych treści norm ISO/IEC, danych niejawnych, specyfikacji konkretnych systemów ani umów operatorów.

**Granice bezpieczeństwa.** Dokument nie zawiera danych operacyjnych, częstotliwości, podatności, procedur ataku, parametrów platform ani projektu środowiska niejawnego. Klasy danych i compute są opisane tylko jako wymagania polityki. Najwyższy poziom C3 jest `restricted-placeholder`: szczegóły, akredytacja i decyzje o dostępie muszą pozostać w obiegu autoryzowanym. Repozytorium GitHub nie jest miejscem na informacje niejawne, tajemnice dostawców, klucze ani surowe dane operacyjne.

## Dziesięć ustaleń sterujących strategią

1. **NATO wymaga jednocześnie odpowiedzialności i zdolności testowej.** Sześć Principles of Responsible Use obejmuje legalność, odpowiedzialność, wyjaśnialność i identyfikowalność, niezawodność, sterowalność oraz ograniczanie stronniczości; strategia wskazuje też sojuszniczy krajobraz TEV&V. Polska nie powinna traktować zasad jako deklaracji etycznej bez bramek i dowodów. `[FACT: CLM-0501–CLM-0503]`

2. **Jakość danych jest funkcją celu.** NATO wymienia dokładność, kompletność, spójność, unikalność, terminowość i ważność, lecz właściwe progi zależą od zadania, źródła i kosztu błędu. „Dane wysokiej jakości” bez wersji, celu i profilu pomiarowego nie są wymaganiem testowalnym. `[FACT/INFERENCE: CLM-0505, CLM-0532]`

3. **Federacja jest już zgodna z kierunkiem NATO i europejskich przestrzeni danych.** Standaryzowane etykiety, metadane, federacyjna tożsamość oraz rozdzielenie control plane od data plane pozwalają zachować lokalną odpowiedzialność za dane. Nie oznacza to jednego technicznego produktu ani jednego operatora. `[FACT/INFERENCE: CLM-0504, CLM-0518, CLM-0530–CLM-0531]`

4. **Polska ma podstawy polityczne, ale nie ma jawnej linii bazowej.** Strategia MON z 2024 r. opisała potrzebę przełamania silosów; przyjęta strategia informatyzacji państwa z 2026 r. przewiduje rejestr AI, ośrodek bezpieczeństwa AI, standardy danych, PLGrid i przejrzysty dostęp do compute. Nie znaleziono jednak kompletnego, aktualnego obrazu aktywów, ownerów, jakości, mocy i zaległości ewaluacyjnych. `[FACT/UNKNOWN: CLM-0506–CLM-0507, CLM-0529]`

5. **AI Factories są częścią podaży, nie automatycznym bezpiecznym środowiskiem obronnym.** Gaia deklaruje ponad 1000 GPU i integrację z PLGrid, a PIAST zapowiada usługi od 2026 r. Publiczne źródła nie potwierdzają jednak akredytacji, SLA ani dopuszczenia do danych chronionych. `[FACT/UNKNOWN: CLM-0508–CLM-0509, CLM-0528]`

6. **Prawo wymaga rozdzielenia przypadków użycia.** AI Act wyłącza użycie wyłącznie wojskowe, obronne i bezpieczeństwa narodowego, ale nie każde użycie technologii dual-use. Data Governance Act daje cywilny wzorzec bezpiecznego przetwarzania, lecz nie jest podstawą udostępniania danych obronnych. `[FACT: CLM-0513, CLM-0514, CLM-0515, CLM-0516]`

7. **Governance musi wiązać cel, model, dane, cyber i akceptację ryzyka.** Sam komitet ds. AI bez jednoznacznych ownerów nie rozwiązuje konfliktu interesów. Twórca lub dostawca nie może być jedyną stroną, która projektuje test, interpretuje wynik i ostatecznie akceptuje własne ryzyko. `[FACT/INFERENCE: CLM-0501, CLM-0519, CLM-0538–CLM-0539]`

8. **Edge AI jest odrębnym produktem cyklu życia.** Model na urządzeniu musi być powiązany z runtime, konfiguracją, schematem wejść, zależnościami, zasobami, telemetrią i regułą degradacji. Zdalna możliwość aktualizacji bez wersjonowania, testu i rollbacku zwiększa ryzyko zamiast je redukować. `[FACT/INFERENCE: CLM-0504, CLM-0537, CLM-0541–CLM-0543]`

9. **SBOM jest konieczny, ale niewystarczający.** Pokazuje skład oprogramowania, nie pochodzenie zbioru, znaczenie wersji modelu, kryteria ewaluacji ani dopuszczony zakres użycia. Dlatego powinien być powiązany z manifestem modelu, danych i środowiska. `[FACT/INFERENCE: CLM-0517, CLM-0520, CLM-0524, CLM-0542]`

10. **Bezpieczna degradacja jest projektowanym zachowaniem, nie hasłem „człowiek przejmie”.** System musi mieć określone funkcje niezbędne, kryteria przejścia, ograniczone tryby, sposób odzyskania i test. Ręczne przejęcie może być niewykonalne albo mniej bezpieczne i nie może być uniwersalnym założeniem. `[FACT/INFERENCE: CLM-0522, CLM-0543]`

## Stan obecny, jawna luka i wniosek projektowy

| Obszar | Stan obecny — `FACT` | Jawna luka — `UNKNOWN` | Wniosek A05 — `INFERENCE` |
|---|---|---|---|
| Polityka AI | MON ma publiczną strategię do 2039 r.; strategia informatyzacji państwa z 2026 r. obejmuje bezpieczeństwo AI, dane i compute (CLM-0506–CLM-0507) | niepotwierdzony formalny status Polityki AI do 2030 r. opublikowanej w 2025 r. (CLM-0526) | oprzeć mandat wykonawczy na obowiązujących uchwałach, a status dokumentu 2030 zweryfikować przed cytowaniem jako przyjętej polityki |
| Prawo krajowe | nowa strategia cyber i nowelizacja KSC obowiązują; parlament opublikował tekst ustawy o systemach AI (CLM-0510–CLM-0512) | brak potwierdzenia ogłoszenia ustawy AI do daty odcięcia (CLM-0527) | każdy pilotaż ma kartę reżimu prawnego aktualizowaną przed G0 i G5 |
| Prawo UE | AI Act rozdziela wyłączone użycia obronne i użycia potencjalnie objęte; DGA, Data Act i CRA tworzą benchmarki danych, przenoszalności i cyklu życia (CLM-0513–CLM-0517) | zakres zależy od produktu, podmiotu, celu i terminu stosowania | profil programu ma mapowanie do prawa per przypadek, bez automatycznego „wyłączenia obronnego” |
| Dane | NATO określa wymiary jakości i federacyjny kierunek dostępu (CLM-0504–CLM-0505) | brak jawnego katalogu ownerów, jakości, praw i retencji dla danych obronnych (CLM-0529) | wprowadzić kontrakt produktu danych i federacyjny katalog metadanych bez kopiowania treści wrażliwej |
| Compute | rozwijane są Gaia, PIAST i PLGrid (CLM-0507–CLM-0509) | brak jawnego dowodu dostępności, SLA i akredytacji do chronionych workloadów (CLM-0528) | kwalifikować usługę per poziom C0–C3; komunikat projektowy nie otwiera bramki danych |
| Governance modeli | NATO, AI Act, NIST i ISO zapewniają spójne kategorie odpowiedzialności, ryzyka, jakości i wpływu (CLM-0501, CLM-0514, CLM-0519, CLM-0523) | brak jawnego wspólnego polskiego profilu bramek i ról dla dual-use | rozdzielić ownera użycia, modelu, danych, cyber, TEVV i akceptację ryzyka |
| Cyber i łańcuch dostaw | KSC, CRA, SSDF, SBOM i zero trust dostarczają elementy bazowe (CLM-0511, CLM-0517, CLM-0520–CLM-0524) | brak jawnej informacji o pokryciu istniejącego portfela przez te praktyki | nowe pilotaże zaczynają od identyfikowalnej wersji i planu utrzymania, a portfel istniejący przechodzi audyt ryzyka |

## Docelowa architektura federacyjnej przestrzeni danych

### Zasada ustrojowa: wspólny kontrakt, rozproszona odpowiedzialność

„Narodowa Bezpieczna Przestrzeń Danych Obronnych” powinna być **federacją usług i reguł**, nie nazwą jednego repozytorium. Właściciel domeny zachowuje odpowiedzialność za legalność, jakość, dostęp i retencję. Płaszczyzna wspólna zapewnia wzajemne rozpoznawanie tożsamości, polityki jako kod, metadane, ślad decyzji, dowody jakości i zgodne interfejsy. Fizyczne dane mogą pozostawać w instytucji, laboratorium, chmurze, HPC lub chronionej enklawie właściwej dla klasy.

### Osiem warstw architektury polityki

| Warstwa | Wspólna usługa państwowa | Odpowiedzialność domenowa | Minimalny dowód |
|---|---|---|---|
| 1. Mandat, prawo i etyka | słownik celów, wzór oceny wpływu, rejestr wyjątków | owner użycia ustala cel, podstawę prawną, ograniczenia i ryzyko | karta celu, zakres, owner, decyzja G0 |
| 2. Tożsamość i zaufanie | federacyjne ICAM, atrybuty, reguły uwierzytelnienia workloadów | instytucja potwierdza rolę, urządzenie, środowisko i uprawnienie | ślad autoryzacji, czas i polityka decyzji |
| 3. Katalog i kontrakt danych | wspólny schemat metadanych, identyfikatory, API discovery | steward utrzymuje dane, jakość, prawa, retencję i ograniczenia eksportu | wersjonowana karta produktu danych |
| 4. Płaszczyzny danych | profile interoperacyjności i przenoszalności | operator domenowy przechowuje i przetwarza dane w dopuszczonym środowisku | test interoperacyjności, plan wyjścia |
| 5. Bezpieczne przetwarzanie | wzorzec compute-to-data, kontrola wejścia i wyniku, katalog C0–C3 | owner środowiska egzekwuje izolację, egress, logowanie, usunięcie i ciągłość | raport kwalifikacji środowiska |
| 6. Lifecycle modeli | wspólny model registry, format evidence pack i trigger zmian | owner modelu wiąże kod, dane, runtime, sprzęt i wyniki z wersją | podpisany pakiet wersji i decyzja bramki |
| 7. Obserwowalność i audyt | wspólny format zdarzeń, czas, odsyłacze i dashboard ryzyka | system źródłowy zachowuje log adekwatny do wrażliwości | odtworzenie decyzji bez ujawnienia nadmiarowych danych |
| 8. Assurance i ciągłość | profil TEVV, katalog laboratoriów, mechanizm niezależnej recenzji | owner ryzyka definiuje próg, fallback, reakcję i wycofanie | test degradacji, recovery, rollback i zamknięcie zmian |

Rozdzielenie płaszczyzny sterowania i danych ma oparcie w Alliance Digital Strategy i Data Spaces Blueprint, ale nie przesądza technologii wdrożeniowej (CLM-0504, CLM-0518, CLM-0531). Zamówienie powinno opisywać zachowanie, artefakty i interfejsy, a nie wyłącznie markę platformy.

### Minimalny kontrakt produktu danych

Każdy zbiór, strumień lub produkt danych dopuszczony do treningu, ewaluacji albo wnioskowania powinien mieć kartę:

1. jednoznaczny identyfikator, ownera biznesowego i stewarda technicznego;
2. zatwierdzony cel użycia oraz cele zakazane lub wymagające ponownej zgody;
3. podstawę prawną, prawa do wykorzystania, ograniczenia licencji i eksportu;
4. klasę wrażliwości i dozwolone poziomy compute;
5. pochodzenie, metodę pozyskania, transformacje, wersję i łańcuch nadzoru;
6. schemat, semantykę, jednostki, czas, geometrię lub inne metadane potrzebne do poprawnej interpretacji;
7. profil jakości dla konkretnego celu: dokładność, kompletność, spójność, unikalność, terminowość i ważność oraz znane luki;
8. zakres reprezentacji, ryzyka stronniczości, duplikaty, dane syntetyczne i sposób rozdzielenia zbiorów treningowych od testowych;
9. retencję, archiwizację, `legal hold`, usunięcie i sposób propagacji korekty do kopii pochodnych;
10. regułę dostępu, export/egress, logowania, cytowania oraz kontakt w razie incydentu.

Karta nie powinna kopiować do katalogu wartości wrażliwych. Dla danych chronionych wspólny katalog może zawierać wyłącznie bezpieczny identyfikator, ownera, klasę, opis uprawnień i sposób złożenia wniosku; reszta pozostaje w domenie źródłowej (CLM-0532).

### Dostęp: tożsamość, cel i środowisko

Domyślny wzorzec dostępu łączy pięć pytań:

- **kto lub co** żąda dostępu — człowiek, usługa, pipeline, model albo urządzenie;
- **w jakiej roli i w jakim celu** — atrybuty, zadanie, podstawa i czas;
- **z jakiego środowiska** — stan urządzenia, workloadu, sieci i compute tier;
- **do jakiej wersji i klasy danych** — minimalny zakres, pola, czas i jakość;
- **jaki rezultat może opuścić domenę** — surowe dane, agregat, model, metryka lub wyłącznie decyzja.

Polityka powinna być egzekwowana maszynowo tam, gdzie jest to możliwe, ale musi mieć ownera i ścieżkę wyjątku. Uprawnienie wygasa; nie jest dziedziczone bez końca przez projekt, dostawcę ani użytkownika. Decyzja, odmowa i zmiana polityki trafiają do audytu (CLM-0533).

### Retencja i usunięcie

Nie rekomenduje się jednej liczby lat dla wszystkich artefaktów. Surowe dane, próbki testowe, logi bezpieczeństwa, evidence pack, model, dokumentacja odbiorowa i dane osobowe mają odmienne cele i obowiązki. Właściciel danych wraz z A09 powinien utworzyć harmonogram klasowy uwzględniający:

- minimalny czas potrzebny do audytu wersji i obrony decyzji;
- maksymalny czas dopuszczalny przez cel, prawo i ryzyko;
- zależności pochodne: model, cecha, agregat i backup;
- wstrzymanie usunięcia dla incydentu, postępowania lub kontroli;
- bezpieczne usunięcie i potwierdzenie wykonania u procesorów;
- ponowną ocenę danych archiwalnych przed użyciem w nowym celu.

Wspólny katalog przechowuje regułę i dowód wykonania, nie musi przechowywać samego zbioru (CLM-0534).

### Audyt bez budowania nowego ryzyka

Ścieżka audytowa ma pozwolić odpowiedzieć: kto, kiedy, na jakiej podstawie, przy jakiej polityce i wersji danych/modelu wykonał operację; jaki wynik lub wyjątek powstał; kto zaakceptował ryzyko; czy możliwe jest odtworzenie decyzji. Wymagane są spójny czas, identyfikatory, kontrola integralności, retencja i kontrola dostępu do logów.

Nie każdy centralny dashboard powinien otrzymywać pełną treść zdarzenia. W wielu przypadkach wystarczy odporny na manipulację odsyłacz, skrót, identyfikator wersji, wynik bramki i lokalizacja logu w domenie chronionej. Centralizacja treści logów może utworzyć nowy koncentrator ryzyka (CLM-0544).

## Katalog mocy obliczeniowej C0–C3

| Poziom | Przeznaczenie polityki | Typ danych | Minimalne warunki wejścia | Wyjście i ciągłość | Stop-rule |
|---|---|---|---|---|---|
| **C0 — publiczny / otwarty** | prace na danych publicznych, syntetycznych lub jawnych benchmarkach | jawne, bez ograniczeń licencyjnych i bezpieczeństwa poza standardową ochroną | owner zadania, podstawowy secure SDLC, kontrola kosztu i wersji | standardowy egress, backup, przenoszalność artefaktów | wykrycie danych osobowych, chronionych lub ograniczeń licencyjnych |
| **C1 — kontrolowany dual-use** | projekty publiczne i przemysłowe z ograniczonym dostępem | dane umowne, poufne handlowo lub kontrolowane, lecz niedopuszczone jako niejawne | federacyjna tożsamość, szyfrowanie, segmentacja, polityka egress, logi, ocena dostawcy | kontrolowany eksport, plan zmiany dostawcy, SLA i reakcja na incydent | brak ownera danych, brak prawa do przetwarzania albo niemożliwy audyt |
| **C2 — chroniona enklawa** | zadania o wysokiej wrażliwości wymagające dedykowanej oceny i ścisłego ograniczenia przepływów | dane chronione zgodnie z decyzją właściwego organu, bez domniemania danych niejawnych | formalna kwalifikacja środowiska, administracja uprzywilejowana pod kontrolą, kontrola nośników, supply chain, odtworzenie i zatwierdzony output review | compute-to-data, minimalny egress, niezależny audyt i ćwiczone recovery | brak aktualnej kwalifikacji, niekontrolowany egress albo brak testu ciągłości |
| **C3 — odseparowany `restricted-placeholder`** | zastosowania wymagające osobnego, autoryzowanego obiegu | wyłącznie klasy wskazane przez właściwe organy poza tym dokumentem | wymagania, topologia, akredytacja i personel określone w bezpiecznym obiegu | ślad dowodowy i interoperacyjność tylko w zakresie dopuszczonym | jakakolwiek próba opisania lub przetwarzania szczegółów w repozytorium jawnym |

Poziom nie jest etykietą marki. To wynik kwalifikacji konkretnego operatora, lokalizacji, usługi, konfiguracji i wersji. Ta sama instytucja może świadczyć różne poziomy tylko po wykazaniu separacji i kontroli. Gaia, PIAST i PLGrid należy włączyć do katalogu usług, ale nie przypisywać im C2/C3 bez niezależnego dowodu (CLM-0528, CLM-0535–CLM-0536).

### Kryteria kwalifikacji usługi compute

1. jurysdykcja, lokalizacja danych i podwykonawców;
2. tożsamość administratorów, separacja obowiązków i dostęp uprzywilejowany;
3. izolacja tenantów/workloadów i kontrola wejścia oraz egress;
4. pochodzenie sprzętu, firmware, hypervisora, bibliotek i obrazów;
5. identyfikowalność wersji, logowanie i dostęp ownera do dowodów;
6. dostępność, kolejki, SLA, rezerwacja mocy i priorytety w kryzysie;
7. backup, odtworzenie, przenoszalność modelu/danych i plan wyjścia;
8. obsługa incydentu, aktualizacji, podatności, usunięcia i zakończenia umowy;
9. koszt całego cyklu i ryzyko blokady dostawcy;
10. zakres dopuszczonych danych oraz data owner podpisujący decyzję.

## Edge AI i bezpieczna degradacja

### Edge AI jako wersjonowany pakiet

Rejestr wersji nie może zawierać jedynie pliku modelu. Minimalny pakiet edge obejmuje:

- hash i podpis modelu, runtime, konfiguracji, polityk i zależności;
- identyfikator sprzętu lub profilu sprzętowego oraz dopuszczone warianty;
- schemat i założenia wejść, preprocessing i wersję kalibracji;
- zatwierdzony zakres warunków, ograniczenia i znane zachowania niebadane;
- budżet opóźnienia, pamięci, energii i dostępności usług zewnętrznych;
- lokalną telemetrię, buforowanie i reguły synchronizacji po odzyskaniu łączności;
- kryteria alarmu, degradacji, zatrzymania funkcji, rollbacku i odzyskania;
- powiązanie do evidence pack, decyzji bramki i ownera akceptacji ryzyka.

Takie powiązanie odpowiada kierunkowi NATO dotyczącym edge inference, identyfikowalności i niezawodności oraz praktykom cyklu życia oprogramowania (CLM-0501, CLM-0504, CLM-0537).

### Safe degradation

Projekt ma jawnie zdefiniować:

1. funkcje niezbędne, które system ma zachować;
2. sygnały wejścia w stan zdegradowany oraz regułę unikania oscylacji między trybami;
3. ograniczenia zachowania w każdym stanie;
4. rolę człowieka i warunek przekazania tylko wtedy, gdy przekazanie jest wykonalne i przetestowane;
5. zachowanie po utracie danych, modelu, łączności, compute lub zaufania do wejścia — wyłącznie na poziomie właściwym dla danego systemu;
6. rejestrację przyczyny, decyzji, wersji i skutku;
7. bezpieczne odzyskanie, walidację stanu i powrót do pełnej funkcji;
8. testy normalne, graniczne i odtwarzania, zatwierdzone przez niezależnego reviewera.

Memo nie narzuca jednego trybu. Dla jednego systemu bezpieczne może być ograniczenie funkcji, dla innego zatrzymanie, a dla jeszcze innego kontynuacja usługi minimalnej. Założenie „człowiek zawsze przejmie” jest dopuszczalne tylko po wykazaniu czasu, informacji, interfejsu i kompetencji potrzebnych do przejęcia (CLM-0522, CLM-0543).

## Governance modeli i odpowiedzialność

| Rola | Odpowiedzialność | Czego nie może zatwierdzić samodzielnie |
|---|---|---|
| **Owner celu / użycia** | problem, oczekiwany rezultat, dopuszczony zakres, wpływ i budżet ryzyka | jakości modelu poza zakresem własnych kompetencji ani wyjątku prawnego |
| **Owner modelu** | architektura, wersja, pipeline, ograniczenia, utrzymanie i wycofanie | ostatecznej akceptacji ryzyka własnego systemu |
| **Steward danych** | legalność i jakość danych, karta produktu, dostęp, retencja i korekty | nowego celu użycia poza mandatem ownera i prawa |
| **Owner cyber** | model zagrożeń, secure SDLC, tożsamości, zależności, incident/patch/rollback | ryzyka misji lub społecznego wpływu w imieniu ownera użycia |
| **Niezależny TEVV** | plan i wykonanie niezależnych testów, reprodukcja, luki, pass/fail względem progu | zmiany progu po zobaczeniu wyniku bez śladu i zatwierdzenia |
| **Organ akceptujący ryzyko** | decyzja o pilotażu, wdrożeniu, warunkach, wyjątku lub wycofaniu | delegowania odpowiedzialności do dostawcy przez brak decyzji |
| **Operator / użytkownik** | użytkowanie w zakresie, raportowanie zdarzeń, feedback i procedury degradacji | aktualizacji modelu lub konfiguracji poza kontrolowanym procesem |
| **Audyt / red team** | badanie dowodów, konfliktów, obejść i skuteczności zabezpieczeń | tworzenia własnej rekomendacji domenowej bez ujawnienia konfliktu roli |

RACI szczegółowe powinno powstać per zastosowanie. Dla systemów krytycznych niezależność TEVV oznacza co najmniej odrębność decyzji i śladu dowodowego; nie musi oznaczać tworzenia nowej instytucji dla każdego projektu (CLM-0538).

## Bramki lifecycle i TEVV

| Bramka | Pytanie decyzyjne | Minimalny dowód | Stop-rule |
|---|---|---|---|
| **G0 — cel, prawo i wpływ** | czy problem ma ownera, mierzalny rezultat, dopuszczony cel i zakres? | karta celu, reżim prawny, impact/risk screen, alternatywa nie-AI | brak ownera, podstawy, miernika albo użycie AI bez przewagi nad prostszą metodą |
| **G1 — dane** | czy dane są legalne, właściwe, wersjonowane, wystarczająco reprezentatywne i separują test? | karty produktów danych, profil jakości, lineage, prawa, podział train/validation/test | nieustalone pochodzenie, prawo, istotna luka lub skażony zbiór testowy |
| **G2 — ocena offline** | czy wersja spełnia progi użyteczności, ryzyka, robustness, cyber i zasobów? | plan testów, benchmarki, uncertainty, stress, reprodukcja i znane luki | próg zmieniony po wyniku, brak odtwarzalności lub krytyczny scenariusz bez oceny |
| **G3 — integracja i środowisko reprezentatywne** | czy cały system, człowiek, interfejsy i degradacja działają w granicach? | test integracyjny/symulacja, human factors, logi, safe degradation, rollback | brak identyfikowalnej konfiguracji, audytu, kontroli wersji lub bezpiecznego stanu |
| **G4 — ograniczony pilotaż** | czy można zebrać dowody od użytkownika przy ograniczonym ryzyku? | ograniczenia, owner dyżurny, monitoring, plan incydentu, kryteria wycofania | pilotaż nie ma końca, staje się produkcją lub nie pozwala szybko wyłączyć funkcji |
| **G5 — wdrożenie** | czy organizacja potrafi bezpiecznie utrzymać system i dane? | SLA, support owner, secure SDLC, SBOM/manifests, patch, rollback, szkolenie i retencja | brak wsparcia, znane krytyczne zależności bez planu lub brak decyzji ryzyka |
| **G6 — monitoring, zmiana i wycofanie** | czy wyniki, dryf, incydenty i zmiany pozostają w zatwierdzonym zakresie? | dashboard, trigger zmian, rejestr wersji, okresowa ewaluacja i plan wycofania | spadek poniżej progu, istotna zmiana bez oceny albo niemożność odtworzenia decyzji |

Bramka dotyczy konkretnej wersji i zakresu. Ponowna ocena może być proporcjonalna: zmiana dokumentacji nie musi powtarzać pełnego testu, ale zmiana modelu, danych, runtime, sprzętu, sensora, celu, warunków albo zabezpieczeń wymaga analizy wpływu. Istotny dryf lub incydent także uruchamia decyzję (CLM-0539–CLM-0541).

### Macierz ewaluacji i monitoringu

| Wymiar | Przykładowe pytanie | Przed pilotażem | Po wdrożeniu |
|---|---|---|---|
| Użyteczność | czy wynik poprawia miernik problemu wobec baseline i alternatywy nie-AI? | test porównawczy i próg | rezultat użytkownika i skutki uboczne |
| Błąd i kalibracja | czy prawdopodobieństwo/pewność odpowiada rzeczywistości i wspiera decyzję? | błąd, kalibracja, progi | zmiana kalibracji i rozkładu błędów |
| Zakres i reprezentacja | gdzie dane są słabe lub nieadekwatne? | segmenty/warunki, pokrycie i luki | nowe warunki, kohorty i źródła |
| Robustness i uncertainty | jak system reaguje na szum, braki, wartości graniczne i nieznane wejścia? | test stresowy, OOD i bezpieczny stan | alarmy OOD, niepewność i incydenty |
| Cyber i supply chain | czy artefakt i zależności są znane, kontrolowane i aktualizowalne? | threat model, SBOM, podpis, test rollbacku | podatności, aktualność, wyjątki i czas naprawy |
| Human factors | czy człowiek rozumie zakres, alarm, możliwość interwencji i odpowiedzialność? | badanie zadania, interfejsu i szkolenia | błędy użycia, obejścia, obciążenie i feedback |
| Zasoby edge/compute | czy opóźnienie, pamięć, energia i dostępność mieszczą się w budżecie? | profil zasobów i stany degradowane | p95/p99, błędy zasobów, kolejki i koszt |
| Audytowalność | czy można odtworzyć wersję, wejście, politykę i decyzję? | test evidence pack i spójności czasu | próbka odtworzenia, kompletność logów |
| Ciągłość | czy system utrzymuje funkcję minimalną, odzyskuje i wraca bezpiecznie? | test degradacji, backup i recovery | RTO/RPO właściwe dla usługi, realny czas odzyskania |

Nie ma jednego wspólnego progu dla wszystkich zastosowań. Owner celu proponuje progi przed testem, TEVV ocenia ich adekwatność, a organ ryzyka je zatwierdza. Zmiana progów po poznaniu wyniku musi być widoczna i uzasadniona (CLM-0540).

## Secure SDLC, SBOM i artefakty cyklu życia

### Minimalna linia bazowa

Każdy nowy pilotaż finansowany przez państwo powinien dostarczać:

1. model zagrożeń i granice odpowiedzialności;
2. kontrolowane repozytoria, przegląd zmian, chroniony pipeline i rejestr buildów;
3. przypięte zależności, źródło pochodzenia i regułę aktualizacji;
4. maszynowo czytelny SBOM o kontrolowanej wersji formatu;
5. manifest modelu: identyfikator, pochodzenie, cel, wersja, parametry środowiska i ograniczenia;
6. manifest danych: identyfikatory produktów, wersje, prawa, lineage, profil jakości i zakres użycia;
7. manifest runtime/sprzętu: obrazy, biblioteki, firmware, konfiguracja i warianty dopuszczone;
8. podpisanie i weryfikację artefaktów oraz bezpieczne zarządzanie kluczami poza repozytorium;
9. proces zgłaszania i obsługi podatności, wsparcie, patch, rollback i termin wycofania;
10. dowód odtwarzalności proporcjonalny do krytyczności oraz ślad wyjątków.

SSDF, CRA i SPDX/SBOM tworzą bazę dla oprogramowania, lecz AI wymaga dodatkowego wiązania danych, modelu i warunków (CLM-0517, CLM-0520, CLM-0524, CLM-0542). Format powinien być wersjonowany i wymienny; nie należy uzależniać programu od jednej starzejącej się edycji standardu.

### Proporcjonalność dla MŚP i badań

Wymóg nie powinien sprowadzać się do kosztownego certyfikatu. Państwo może dostarczyć szablony, referencyjne pipeline'y, narzędzia generowania SBOM, checklisty i usługę niezależnego skanu. Mały pilotaż C0 może mieć lżejszy dowód niż wdrożenie C2, ale nie może zrezygnować z ownera, wersji, praw do danych i rollbacku. Wyjątek ma zakres, właściciela, datę wygaśnięcia i plan zamknięcia.

## Plan wdrożenia

### Pierwsze 100 dni od mandatu

- ustanowić KPRM jako sponsora i wskazać współownerów MC/MON;
- utworzyć kontrolowaną linię bazową: systemy, ownerzy, produkty danych, środowiska compute, laboratoria, logi, backlog ewaluacyjny i ryzyka;
- zatwierdzić słownik klasyfikacji `FACT/ESTIMATE/SCENARIO/INFERENCE/RECOMMENDATION/UNKNOWN` oraz wersję 0.9 kontraktu danych;
- zinwentaryzować Gaia, PIAST, PLGrid i środowiska resortowe według kryteriów C0–C3, bez przypisywania poziomu przed dowodem;
- wybrać dwa lub trzy pilotaże na danych jawnych albo kontrolowanych niewrażliwych;
- wskazać ownerów profilu TEVV, secure SDLC i rejestru wyjątków;
- uzgodnić z A09 mapę prawa, retencji i bezpiecznego obiegu.

### Do 31 marca 2027 r.

- uruchomić pilotaże federacji z jednym wspólnym control plane i co najmniej dwiema domenowymi płaszczyznami danych;
- przeprowadzić test odmowy dostępu, kontrolowanego egress, odtworzenia śladu oraz zmiany komponentu lub operatora;
- opublikować jawny profil ról G0–G6 i format evidence pack;
- przeprowadzić niezależną replikację co najmniej jednego testu modelu;
- wprowadzić minimalny secure SDLC/SBOM/manifests do nowych pilotaży;
- przygotować decyzję go/no-go dla rozszerzenia federacji.

### Do 30 czerwca 2027 r. i dalej

- opublikować jawny katalog usług compute C0–C2 oraz placeholder C3, bez szczegółów chronionych;
- ustanowić rytm kwartalnego przeglądu jakości danych, zmian modeli, incydentów, wyjątków i dostępności compute;
- zintegrować wymagania z zamówieniami, TEVV, szkoleniami i wsparciem MŚP;
- raz w roku wykonać ćwiczenie przeniesienia wybranego workloadu, rollbacku i odtworzenia;
- aktualizować profile po zmianie prawa, standardów NATO/UE, NIST lub ISO, unikając deklaracji zgodności na podstawie samego numeru normy.

## Pięć decyzji do podjęcia

| Decyzja | Adresat i owner | Termin | Rezultat | Bramka / stop-rule | Zależności | Główne ryzyko |
|---|---|---|---|---|---|---|
| **D-A05-1. Zlecić 100-dniową linię bazową i architekturę federacyjną** | decyzja RM; sponsor KPRM; współownerzy MC i MON; BBN recenzuje spójność | mandat do 30.09.2026; wynik 100 dni później | inwentarz ownerów i aktywów, słownik danych, mapa przepływów i compute tiers, architektura v0.9 | bramka: owner, reżim prawny i miejsce dowodu dla każdego aktywa; stop: kopiowanie danych chronionych do repo roboczego albo brak ownera ryzyka | A01, A02, A04, A09; właściciele danych i operatorzy | pozorna inwentaryzacja, spór kompetencyjny, koncentracja wrażliwych metadanych |
| **D-A05-2. Uruchomić 2–3 niewrażliwe pilotaże federacji** | MC jako owner platformy; MON/MSWiA i inne instytucje jako ownerzy domen | wybór do 31.12.2026; wynik do 31.03.2027 | sprawdzony control plane, co najmniej dwa data plane, kontrakt danych, audyt egress i jakości | bramka: test odmowy, odtworzenie logu i wymiana komponentu; stop: niejasna podstawa, niekontrolowany eksport lub niemożliwy audyt | A03, A09, operatorzy danych i tożsamości | pilotaż bez końca staje się ukrytym systemem produkcyjnym |
| **D-A05-3. Ustanowić wspólny profil AI assurance i federację TEVV** | MON dla profilu obronnego; NASK dla metod publicznych/cywilnych; niezależny reviewer per system | profil 0.9 do 31.03.2027 | role, G0–G6, evidence pack, trigger zmian, rejestr wyjątków i katalog usług testowych | bramka: niezależna replikacja testu i ślad akceptacji ryzyka; stop: twórca sam ostatecznie zatwierdza własny system | A03, A04, A09, laboratoria i użytkownicy | biurokracja wydłużająca pilotaże albo pozorna niezależność |
| **D-A05-4. Włączyć secure SDLC, SBOM i manifesty do odbioru** | AU i centralni nabywcy publiczni; MC/MON utrzymują profil techniczny | nowe pilotaże od 01.01.2027 | identyfikowalna wersja kodu, modelu, danych, runtime i sprzętu; plan patch/rollback | bramka: odtworzenie builda lub równoważny dowód, kontrola zależności, próba rollbacku; stop: nieznane komponenty krytyczne lub brak ownera wsparcia | A03, A06, A09; wsparcie narzędziowe MŚP | koszt wejścia, compliance papierowy, zamrożenie starego formatu |
| **D-A05-5. Zatwierdzić katalog compute tiers i edge assurance** | MC dla katalogu; MNiSW/operatorzy dla podaży; MON dla wymagań obronnych | do 30.06.2027 | profile C0–C3, SLA, dowody izolacji/egress/ciągłości, format edge package i rezerwacja mocy | bramka: audyt per tier i ćwiczenie odtworzenia; stop: dane chronione skierowane do usługi na podstawie samego komunikatu projektowego | A04, A06, A07, A09; Gaia, PIAST, PLGrid i środowiska resortowe | duplikacja inwestycji, niedostępność mocy, vendor lock-in i niekontrolowany koszt |

Decyzje tworzą sekwencję. D-A05-1 ustala prawdziwy stan i ownerów; D-A05-2 sprawdza federację bez ryzyka danych chronionych; D-A05-3 ustanawia niezależne dowody; D-A05-4 chroni cykl życia; D-A05-5 kwalifikuje compute i edge. Prezydent i BBN oceniają ciągłość, interoperacyjność i akceptowalność ryzyka, ale nie przejmują kompetencji wykonawczych rządu ani resortów. `[RECOMMENDATION: CLM-0545, CLM-0546, CLM-0547, CLM-0548, CLM-0549]`

## Luki danych i plan ich pozyskania

| Luka | Status | Sposób pozyskania | Owner danych | Rezultat | Termin po mandacie |
|---|---|---|---|---|---|
| inwentarz systemów AI, ownerów i wersji | `UNKNOWN` | kontrolowany spis z jednoznaczną definicją systemu i pakietu wersji; nie kopiować treści niejawnej | MON, MSWiA, MC i inni użytkownicy | pokrycie portfela oraz lista sierot bez ownera | 60 dni |
| katalog produktów danych, praw i jakości | `UNKNOWN` | sampling kart danych, lineage, licencji, zgód, retencji i wymiarów jakości | stewardzi danych i A09 | heatmapa gotowości do treningu/testu | 100 dni |
| status formalny Polityki AI 2030 | `UNKNOWN` | potwierdzenie w MC/KPRM i ponowny check ELI | MC/KPRM, recenzja A09 | jednoznaczny status i wersja | przed publikacją strategii |
| status ogłoszenia polskiej ustawy AI | `UNKNOWN` | ponowny check ELI i ścieżki legislacyjnej | A09 / RCL | data ogłoszenia, wejścia i przepisy przejściowe albo potwierdzony brak | przed każdym wydaniem |
| dostępność i akredytacja Gaia/PIAST/PLGrid | `UNKNOWN` | due diligence operatora: usługi, kolejki, SLA, administratorzy, supply chain, egress, backup, recovery | MC, MNiSW i operatorzy; MON kwalifikuje użycie | karta usługi i dopuszczony poziom C0–C2 | 100 dni |
| rzeczywista pojemność i zapotrzebowanie compute | `UNKNOWN` | telemetryczna linia bazowa z jednostką GPU-time/CPU-time/storage/network, profilem workloadu i sezonowością | operatorzy + ownerzy programów | popyt/podaż niski–bazowy–wysoki bez fałszywej precyzji | 6 miesięcy |
| niezależność i zdolność laboratoriów TEVV | `UNKNOWN` | katalog metod, ludzi, kolejek, akredytacji, konfliktów i próba replikacji | MON/NASK i laboratoria | mapa usług oraz luki inwestycyjne | 6 miesięcy |
| pokrycie portfela secure SDLC/SBOM/manifests | `UNKNOWN` | audyt próbki repozytoriów, buildów, zależności, update/rollback i support ownerów | nabywcy, integratorzy i ownerzy cyber | baseline pokrycia i plan ryzyka | 6 miesięcy |
| incydenty, dryf i skuteczność degradacji | `UNKNOWN` | wspólny słownik zdarzeń, bezpieczna agregacja i test tabletop/recovery | użytkownicy, CSIRT-y, ownerzy modeli | trend, czas detekcji/decyzji/odzyskania i luki | 9 miesięcy |

Do czasu uzyskania linii bazowej cele ilościowe powinny być oznaczane jako `SCENARIO` albo `ESTIMATE`, nigdy jako fakt. Dwa nieskuteczne podejścia do pozyskania źródła kończą się wpisem `UNKNOWN`, a nie uzupełnieniem przypuszczeniem.

## Ryzyka, konflikty interesów i argumenty przeciw

| Ryzyko / argument przeciw | Dlaczego jest zasadne | Odpowiedź i warunek |
|---|---|---|
| **Federacja będzie wolniejsza niż centralne jezioro danych.** | wiele ownerów i polityk komplikuje dostęp | wspólny control plane i kontrakty upraszczają powtarzalne przypadki; centralizacja jest dopuszczalna tylko dla jasno wydzielonej klasy, po analizie ryzyka |
| **Wspólne standardy zamrożą innowację.** | modele, NIST, ISO i formaty SBOM szybko się zmieniają | profil ma wersję, status kandydata/pilotażu/zatwierdzenia/wygaszenia i okresowy przegląd; wymagamy interoperacyjnego rezultatu, nie jednej marki |
| **Bramki TEVV zabiją tempo pilotaży.** | pełna ocena może być kosztowna i długa | rygor jest proporcjonalny do krytyczności; G0 eliminuje zbędne AI, a wspólne szablony i laboratoria skracają powtarzalne prace |
| **NASK, operator compute lub laboratorium może stać się monopolistą.** | podmiot definiujący profil i świadczący usługę ma konflikt | rozdzielić autorstwo metody, wykonanie testu i akceptację ryzyka; publikować interfejsy i umożliwiać niezależną replikację |
| **Dostawcy ujawnią zbyt dużo IP przez SBOM i manifesty.** | pełny pakiet może zawierać informacje handlowe lub zwiększać ryzyko | kontrolowany dostęp, minimalne niezbędne pola, escrow/inspekcja i ochrona informacji; brak publicznego ujawnienia nie może oznaczać braku dowodu dla państwa |
| **Zero trust i logowanie mogą zwiększyć centralny ślad o osobach i operacjach.** | tożsamość i audyt tworzą dane wrażliwe | minimalizacja logów centralnych, lokalna treść, odsyłacze i role dostępu do audytu; retencja oparta na celu |
| **Compute-to-data ograniczy wydajność i swobodę badaczy.** | bezpieczne środowiska mają narzut, kolejki i ograniczony tooling | stosować tylko tam, gdzie uzasadnia to klasa danych; C0/C1 pozostają szybkimi ścieżkami dla danych jawnych i kontrolowanych |
| **Gaia/PIAST mogą dublować resortowe inwestycje.** | brak wspólnego katalogu podaży tworzy nadmiar albo luki | decyzje inwestycyjne po pomiarze popytu, katalogu usług i ćwiczeniu przeniesienia; rezerwacja mocy może być tańsza niż własność |
| **Safe degradation może obniżyć zdolność w kryzysie.** | zbyt konserwatywne progi mogą często ograniczać funkcję | próg ustala owner misji przed testem, a TEVV mierzy koszt fałszywych przejść; tryb degradacji jest domenowy, nie uniwersalny |
| **Wyłączenie obronne AI Act upraszcza program.** | część zastosowań jest poza zakresem rozporządzenia | wyłączenie zależy od wyłącznego celu; systemy cywilne, dual-use i public safety mogą wymagać pełnej kwalifikacji, a standardy assurance są użyteczne niezależnie od zakresu |

**Konflikty interesów.** Dostawca modelu nie powinien sam wybrać danych testowych i progu sukcesu; operator chmury nie powinien sam określić własnego compute tier; owner programu nie powinien sam zamknąć krytycznej niezgodności; laboratorium odpłatnie rozwijające rozwiązanie nie powinno być jedynym niezależnym recenzentem. Każdy wyjątek wymaga ujawnienia roli, terminu i drugiej linii kontroli.

## Pytania wymagające decyzji lub bezpiecznego aneksu

1. Które kategorie danych i systemów wymagają autoryzowanego aneksu, a które mogą wejść do jawnych pilotaży?
2. Kto jest formalnym data ownerem w procesach międzyresortowych, gdy źródło, użytkownik i nabywca są różnymi instytucjami?
3. Które istniejące systemy mają pierwszeństwo w audycie ze względu na wpływ, brak alternatywy i zależności dostawcy?
4. Czy KPRM otrzyma mandat do wymuszenia wspólnego kontraktu danych i bramek, czy będą to jedynie rekomendacje resortowe?
5. Jaki organ może akceptować ryzyko systemu dual-use działającego w kilku reżimach prawnych?
6. Jak oddzielić publiczny katalog usług compute od chronionych szczegółów mocy, lokalizacji i rezerwacji?
7. Które metryki sukcesu mogą być publikowane bez ujawniania zdolności lub luk bezpieczeństwa?

## Handoff i kontrola publikacji

- `AUTO`: uzupełnianie źródeł, walidacja schematów, wykrywanie linków i numerów wersji, skład jawnego PDF.
- `HUMAN-IN-LOOP`: wybór ostatecznej architektury, poziomów C0–C2, progów TEVV, retencji, KPI, budżetu i nazw publicznych.
- `HUMAN-ONLY`: dopuszczenie do danych chronionych, publikacja, kontakt z urzędnikiem, akceptacja ryzyka, użycie informacji niejawnej i przypisanie C3.

Przed użyciem memorandum w materiale dla Rady Ministrów lub Prezydenta A09 powinien potwierdzić status Polityki AI 2030 i polskiej ustawy o systemach AI; A12 powinien ponownie otworzyć źródła, sprawdzić daty i podważyć co najmniej twierdzenia CLM-0507–CLM-0509, CLM-0512 oraz CLM-0526–CLM-0529. Wynik `fail` na krytycznej sprzeczności blokuje publikację twierdzenia, ale nie usuwa go z księgi dowodowej.
