# A04 — Systemy autonomiczne i architektura technologiczna państwa

## Executive Summary / Streszczenie wykonawcze

- **Polska powinna budować portfel zdolności autonomicznych, a nie program „dronów”.** Wspólny rdzeń ma objąć systemy powietrzne, lądowe, nawodne, podwodne, międzydomenowe oraz C‑UAS, ale każda domena zachowuje własne wymagania prawne, środowiskowe, testowe i serwisowe. Podstawą jest system systemów, nie sam pojazd. `[RECOMMENDATION: CLM-0403, CLM-0406, CLM-0407]`

- **Autonomię należy opisywać funkcja po funkcji.** Jeden produkt może mieć inny poziom samodzielności w percepcji, planowaniu, nawigacji, wykonaniu zadania, współpracy i samokontroli. Wymagania muszą równocześnie określać rolę człowieka, zatwierdzony zakres warunków, ograniczenia, tryb degradacji i próg ponownej oceny po zmianie. `[FACT/RECOMMENDATION: CLM-0404, CLM-0405, CLM-0421]`

- **Suwerenność technologiczna to kontrola nad punktami krytycznymi, nie autarkia.** Państwo nie musi produkować każdego układu, ale musi kontrolować architekturę, konfigurację, krytyczne interfejsy, prawa do utrzymania i aktualizacji, dowody testowe oraz realną możliwość zastąpienia dostawcy albo odtworzenia zdolności. „Otwarta architektura” bez praw do danych i testu wymienności jest deklaracją, nie zdolnością. `[INFERENCE/RECOMMENDATION: CLM-0413–CLM-0415, CLM-0428–CLM-0430]`

- **Skalowanie wymaga bramek TEVV i dowodu utrzymywalności.** Pozytywny pokaz funkcji zadaniowej nie wystarcza. Przed zwiększeniem wolumenu trzeba wykazać zgodność interfejsów, zachowanie w warunkach normalnych i zdegradowanych, odtwarzalność konfiguracji, obsługiwalność, bezpieczne zarządzanie aktualizacją oraz koszty cyklu życia. `[FACT/RECOMMENDATION: CLM-0416–CLM-0423, CLM-0436]`

**Odpowiedź dla Premiera i Prezydenta:** należy zatwierdzić jeden państwowy kontrakt architektoniczny — wspólną taksonomię, minimalną referencyjną architekturę, profile interfejsów, reguły TEVV i lifecycle — ale nie centralizować wszystkich produktów w jednym megaprogramie ani jednym zakładzie. Realizacja powinna pozostać domenowa i konkurencyjna, z wyjątkami od otwartości udzielanymi jawnie, czasowo i po analizie ryzyka.

## Mandat, odbiorca i granice

**Pytanie decyzyjne.** Jak zbudować państwową architekturę systemów autonomicznych, która pozwala szybko wdrażać i wymieniać technologie, utrzymywać je w całym cyklu życia oraz integrować z NATO i UE bez próby pełnej autarkii?

**Odbiorca.** Premier i Rada Ministrów jako właściciele polityki wykonawczej; Prezydent i BBN jako odbiorcy oceny spójności z długoterminowym bezpieczeństwem państwa; MON, Sztab Generalny, Agencja Uzbrojenia, MSWiA, MRiT, resort cyfryzacji, ULC, PAŻP, PKN, jednostki testowe i użytkownicy jako wykonawcy lub współtwórcy.

**Stan dowodów.** Źródła sprawdzono 21 lipca 2026 r. Wszystkie twierdzenia A04 pozostają `unverified` do niezależnej recenzji. Publiczne dokumenty nie pozwalają ocenić faktycznego stanu interfejsów, praw do danych i utrzymania konkretnych polskich systemów — ta baza jest oznaczona jako `UNKNOWN` (CLM-0431).

**Granice bezpieczeństwa.** Memorandum nie zawiera instrukcji konstrukcji uzbrojenia, parametrów bojowych, częstotliwości, podatności, procedur taktycznych ani danych niejawnych. C‑UAS opisano wyłącznie jako architekturę polityki, odpowiedzialności, wymiany danych i oceny zgodności. MASS Code IMO jest cywilnym wzorcem assurance i wprost nie dotyczy okrętów wojennych; nie jest przedstawiany jako podstawa prawna dla MON (CLM-0420).

## Dziesięć ustaleń, które powinny sterować strategią

1. **„Autonomiczny” nie znaczy „bez człowieka”.** NATO wiąże systemy autonomiczne z odpowiedzialnym użyciem, prawem, sterowalnością i zaufaniem, a EDA zaleca charakteryzowanie autonomii na poziomie funkcji. Konsekwencja: opis roli człowieka jest częścią konfiguracji zdolności, nie dodatkiem szkoleniowym. `[FACT: CLM-0401, CLM-0402, CLM-0404]`

2. **Domena nie wystarcza do klasyfikacji.** Ten sam typ platformy może wykonywać zadania o różnej krytyczności, w innym reżimie prawnym i z innym zakresem nadzoru. Konsekwencja: katalog produktów musi być wielowymiarowy, a nie oparty wyłącznie na masie, zasięgu, nazwie producenta lub domenie. `[INFERENCE: CLM-0433, CLM-0434]`

3. **System jest większy niż platforma.** UAS w prawie cywilnym obejmuje statek i jednostkę sterowania; MASS Code obejmuje także centrum operacji zdalnych, łączność i człowieka; APAS wskazuje dane, AI, sieci i interfejsy jako elementy umożliwiające autonomię. Konsekwencja: zakup samej platformy bez systemu danych, kontroli konfiguracji, serwisu i testów tworzy niepełną zdolność. `[INFERENCE: CLM-0407]`

4. **Wspólny rdzeń między domenami jest możliwy.** Wspólne są: język funkcji, format dowodów, profile bezpieczeństwa, zarządzanie konfiguracją, prawa do danych, pomiar utrzymywalności oraz wzorce interfejsów. Różne pozostają: środowisko, certyfikacja, zagrożenia dla osób trzecich, łączność, mobilność i procedury dopuszczenia. `[FACT/INFERENCE: CLM-0403, CLM-0406, CLM-0410]`

5. **Modularność jest strategią kontraktową i inżynierską.** EDA wskazuje modularne, otwarte architektury; benchmark MOSA łączy projekt modułowy z prawami do danych, zarządzaniem interfejsami i sprawdzaniem zgodności. Konsekwencja: architekt, prawnik IP, nabywca i użytkownik muszą pracować na tej samej mapie modułów. `[FACT: CLM-0408, CLM-0413]`

6. **Otwartość wymaga dowodu.** Dokument interfejsu bez implementacji referencyjnej, testu zgodności i próby podmiany modułu nie wykazuje wymienności. Konsekwencja: co najmniej jeden test z niezależnym komponentem powinien poprzedzać uznanie kluczowego interfejsu za otwarty. `[INFERENCE: CLM-0414]`

7. **Nie wszystko powinno być równie otwarte.** Zbyt głęboka modularność może pogarszać koszt, termin, bezpieczeństwo lub wydajność. Konsekwencja: państwo powinno wyznaczać interfejsy strategiczne według krytyczności i ryzyka blokady, zamiast wymagać publiczności wszystkich szczegółów. `[FACT/RECOMMENDATION: CLM-0415, CLM-0429, CLM-0430]`

8. **TEVV jest procesem ciągłym.** EDA ocenia, że nie można wyczerpać zachowania bardziej adaptacyjnych systemów skończonym katalogiem przypadków; IMO wymaga ponownej oceny po zmianie założeń lub konfiguracji. Konsekwencja: dopuszczenie dotyczy wersji, funkcji i zatwierdzonego zakresu użycia, a nie marki „na zawsze”. `[FACT: CLM-0419, CLM-0420]`

9. **C‑UAS jest architekturą wielowarstwową i wieloinstytucjonalną.** NATO IAMD łączy sensory, C2, środki aktywne i pasywne, odporność oraz koordynację cywilno‑wojskową; plan UE rozdziela wsparcie europejskie od odpowiedzialności państw. Konsekwencja: wspólny obraz danych nie może oznaczać wspólnej, niejasnej kompetencji do działania. `[FACT/RECOMMENDATION: CLM-0424–CLM-0427]`

10. **Nie ma publicznej polskiej bazy do ustalenia celów ilościowych.** Nie wiadomo, ile systemów ma kompletne interfejsy, bazę konfiguracji, alternatywnego dostawcę i pakiet utrzymania. Konsekwencja: pierwszym KPI jest pokrycie audytem i jakość danych bazowych, nie deklarowany procent „polonizacji”. `[UNKNOWN: CLM-0431]`

## Proponowana taksonomia państwowa

### Zasada: klasyfikujemy zdolność, funkcję i ryzyko — nie tylko produkt

Każda pozycja w katalogu programu powinna mieć jedną „kartę zdolności” z następującymi osiami:

| Oś | Minimalny opis | Po co państwu |
|---|---|---|
| Tożsamość | identyfikator zdolności, właściciel operacyjny, integrator, wersja konfiguracji | eliminuje niejednoznaczność produktu i wersji |
| Domena fizyczna | powietrze, ląd, powierzchnia wody, pod wodą, instalacja stała lub układ międzydomenowy | kieruje do właściwego środowiska testowego i regulatora |
| Funkcja publiczna/operacyjna | problem użytkownika i mierzalny rezultat, bez parametrów wrażliwych | odrywa portfel od nazw handlowych |
| Funkcje autonomii | percepcja, interpretacja, planowanie, mobilność/nawigacja, wykonanie zadania, współpraca, samokontrola | pozwala przypisać osobny poziom nadzoru i dowodów |
| Rola człowieka | wykonuje, zatwierdza, nadzoruje, może przerwać, przejmuje sterowanie albo pozostaje odpowiedzialny organizacyjnie | przypisuje odpowiedzialność i wymagania HMI/szkoleniowe |
| Zakres działania | zatwierdzone środowisko, zależności, ograniczenia, warunki normalne i zdegradowane | ogranicza użycie poza zbadanymi warunkami |
| Łączność i dane | założenia dostępu do łączności, źródła danych, retencja logów, zachowanie przy utracie usługi | umożliwia ocenę odporności i audyt |
| Krytyczność | wpływ awarii na ludzi, środowisko, ciągłość działania, informacje i inne systemy | ustala rygor TEVV, zmian i zatwierdzania |
| Reżim prawny | cywilny, obronny, policyjny, infrastruktura krytyczna, podwójnego zastosowania; organ właściwy | zapobiega kopiowaniu dopuszczenia między reżimami |
| Cykl życia | status: koncepcja, prototyp, test, pilotaż, ograniczone użycie, skala, utrzymanie, wycofanie | łączy zakupy z wersją i pakietem dowodowym |
| Krytyczne zależności | moduły i dostawcy o wysokim wpływie, zastępowalność, czas odtworzenia, prawa i ograniczenia eksportowe | mierzy suwerenność zamiast pochodzenia etykiety |

Taksonomia ma być wspólnym słownikiem planowania, zamówień i TEVV. Nie powinna zastępować klasyfikacji NATO, norm domenowych ani przepisów cywilnych. Gdy klasyfikacja sojusznicza lub prawna jest obowiązująca, karta przechowuje mapowanie i wersję źródła, a nie tworzy konkurencyjnego pojęcia.

### Portfel domenowy

| Segment | Co obejmuje na poziomie polityki | Typowe różnice wymagające osobnej ścieżki | Wspólny rdzeń programu |
|---|---|---|---|
| Systemy powietrzne | statek, sterowanie i monitorowanie, moduły zadaniowe, oprogramowanie, dane i zaplecze | przestrzeń powietrzna, zdatność, operatorzy, ryzyko dla osób trzecich | interfejsy, konfiguracja, TEVV, logi, utrzymanie |
| Systemy lądowe | platformy mobilne i stacjonarne roboty do logistyki, inspekcji, ratownictwa i innych zatwierdzonych funkcji | drogi publiczne vs teren zamknięty, interakcja z ludźmi, przeszkody i podłoże | modele funkcji, moduły, bezpieczeństwo, serwis |
| Systemy nawodne | jednostka, centrum operacji zdalnych, łączność, funkcje autonomiczne i wsparcie portowe | prawo morskie, współistnienie z żeglugą, warunki hydrometeorologiczne | ConOps, zakres działania, fallback, rejestry zmian |
| Systemy podwodne | pojazdy autonomiczne lub zdalnie operowane, sensory, węzły danych i zaplecze wydobycia/serwisu | ograniczona łączność, środowisko podwodne, odzyskanie, nawigacja i testy specjalistyczne | konfiguracja, symulacja, interfejsy C2/danych, utrzymanie |
| Systemy międzydomenowe | wspólne C2, wymiana danych i koordynacja różnych typów platform i sensorów | odpowiedzialność za integrację, semantyka danych, synchronizacja wersji | profile interfejsów, zarządzanie tożsamością, test systemu systemów |
| C‑UAS | łańcuch ochrony: obserwacja, fuzja, identyfikacja, wsparcie decyzji, prawnie uprawniona reakcja i ocena | różne organy, ochrona lotnictwa cywilnego, bezpieczeństwo publiczne, IAMD | wspólny obraz, interfejsy sensor–C2, audyt decyzji, ćwiczenia |

Źródła EDA potwierdzają zakres powietrzny, lądowy i morski oraz potrzebę działania między domenami (CLM-0403, CLM-0406). Rozdzielenie domeny morskiej na nawodną i podwodną jest rekomendacją A04 wynikającą z różnic środowiskowych i serwisowych, nie nową klasyfikacją EDA.

### Autonomia jako funkcja — proponowane etykiety robocze

Poniższe etykiety stosuje się **oddzielnie do każdej funkcji**, a nie do całego produktu:

| Kod | Rola systemu w danej funkcji | Minimalny opis roli człowieka | Warunek dopuszczenia |
|---|---|---|---|
| F0 — wykonanie ludzkie | system prezentuje dane lub wykonuje mechaniczne polecenie | człowiek interpretuje i decyduje | poprawność danych, ergonomia, bezpieczeństwo sterowania |
| F1 — automatyzacja | system wykonuje z góry zdefiniowaną procedurę lub rekomenduje | człowiek inicjuje, zatwierdza albo weryfikuje wynik | granice procedury, obsługa błędu, logi |
| F2 — autonomia nadzorowana | system wybiera i realizuje działania w zatwierdzonym zakresie | człowiek monitoruje, może przerwać lub przejąć zgodnie z procedurą | wykazana skuteczność nadzoru, czas i możliwość interwencji, fallback |
| F3 — autonomia ograniczona warunkami | system wykonuje funkcję bez bieżącej interwencji wewnątrz zatwierdzonej domeny | człowiek pozostaje odpowiedzialny organizacyjnie i zarządza wyjątkami | formalny zakres działania, monitoring, stany awaryjne, ponowna ocena zmian |

To nie jest uniwersalna norma ani skala do certyfikacji. Jej celem jest uniemożliwienie zdania „system ma poziom 3 autonomii” bez wskazania funkcji, warunków i odpowiedzialności. Ostateczny słownik powinien zostać zmapowany na terminologię NATO, EDA, regulatorów domenowych i norm obowiązujących w konkretnym programie (CLM-0404, CLM-0405, CLM-0420).

## Referencyjna architektura polityki technologicznej

### Dziewięć warstw, które muszą być widoczne w każdym programie

| Warstwa | Pytanie kontrolne | Artefakt wymagany od programu | Punkt kontroli suwerenności |
|---|---|---|---|
| 1. Misja, prawo i odpowiedzialność | jaki problem jest rozwiązywany i kto może podjąć daną decyzję? | zatwierdzony opis funkcji, RACI, ograniczenia i podstawa prawna | państwo kontroluje wymaganie i reguły użycia |
| 2. Człowiek i nadzór | co wykonuje, zatwierdza, nadzoruje lub przejmuje człowiek? | alokacja zadań, HMI, szkolenie, procedura przejęcia i wyjątku | możliwość niezależnej oceny human factors |
| 3. Dane i modele | jakie dane zasilają funkcję, jak są wersjonowane i oceniane? | karta zbiorów, pochodzenie, wersja modelu, logi i kryteria jakości | dostęp do śladu dowodowego i kontrola wersji |
| 4. Oprogramowanie autonomii | jakie funkcje realizuje oprogramowanie i gdzie są ich granice? | rozdzielone moduły, zależności, wymagania, testy i rollback | prawo do utrzymania lub konkurencyjnej wymiany modułu |
| 5. Obliczenia pokładowe i brzegowe | gdzie wykonywana jest funkcja i od czego zależy? | profil zasobów, konfiguracja, wymagania bezpieczeństwa i zamienności | co najmniej plan alternatyw dla elementów krytycznych |
| 6. Łączność, czas, pozycja i C2 | jakie usługi są wymagane i co dzieje się po ich degradacji? | kontrakt usług, interfejsy, tryby degradacji i test integracyjny | państwo kontroluje krytyczne interfejsy i kryteria zgodności |
| 7. Sensory i moduły zadaniowe | jakie wejścia lub funkcje można wymieniać bez przebudowy całości? | mechaniczny, elektryczny, programowy i semantyczny profil interfejsu | test podmiany z niezależnym modułem |
| 8. Platforma, zasilanie i mobilność | jakie są fizyczne granice systemu i obsługi? | bazowa konfiguracja, diagnostyka, części, bezpieczeństwo i środowisko | prawo do naprawy oraz odtworzenia konfiguracji |
| 9. TEVV, produkcja i utrzymanie | jak system jest testowany, wytwarzany, aktualizowany, naprawiany i wycofywany? | pakiet dowodowy wersji, plan produkcji i serwisu, rejestr zmian | niezależna akceptacja i ciągłość działania |

Model jest rekomendacją A04 (CLM-0435). Nie przesądza fizycznego podziału produktu; służy temu, aby każda zależność miała właściciela, interfejs, kryterium testu i strategię utrzymania.

### Minimalny kontrakt interfejsu

Dla każdego interfejsu strategicznego program powinien określić:

1. właściciela i organ zatwierdzający profil;
2. funkcję i granice odpowiedzialności po obu stronach;
3. syntaktykę, semantykę, jednostki, synchronizację i obsługę błędów — na poziomie adekwatnym do jawności;
4. wymagania bezpieczeństwa, wersjonowania i kompatybilności wstecznej;
5. środowisko referencyjne lub narzędzie testu zgodności;
6. wymagane prawa do dokumentacji, danych, oprogramowania lub użycia testowego;
7. regułę zmiany, wycofania wersji i okres wsparcia;
8. co najmniej jedną próbę integracji z niezależną implementacją, jeżeli interfejs ma dawać opcję zmiany dostawcy.

EDA i INTERACT potwierdzają znaczenie interfejsów i standardów, a MOSA pokazuje, że prawa i conformance są integralne z projektem (CLM-0408–CLM-0414). „Otwarte” nie znaczy „opublikowane w internecie”: specyfikacja może być chroniona, lecz państwo musi mieć wystarczający dostęp i prawa do bezpiecznej konkurencji oraz utrzymania (CLM-0415).

### Standardy: profil, nie lista życzeń

Polska powinna prowadzić kontrolowany **Katalog Profilów Interoperacyjności Systemów Autonomicznych**, mapowany na EDSTAR i właściwe standardy NATO. Każdy profil ma:

- status: kandydat, pilotaż, zatwierdzony, wygaszany, wycofany;
- zakres domenowy i wersję;
- właściciela oraz datę przeglądu;
- test zgodności i implementację referencyjną, gdy to możliwe;
- analizę, gdzie norma cywilna wystarcza, a gdzie potrzebne jest uzupełnienie wojskowe;
- mapę licencji i dostępu do pełnej treści normy;
- decyzję o wyjątkach i termin ich ponownej oceny.

ISO 22166-1 oraz 22166-201 są użytecznymi cywilnymi przykładami modularności i wspólnego modelu informacji, ale mają ograniczony zakres i nie stanowią kompletnego profilu bezpieczeństwa ani obronności (CLM-0411, CLM-0412). Podobnie publiczny raport CMRE o projekcie STANAG 4817 potwierdza kierunek interoperacyjnego C2, lecz nie daje podstawy do deklaracji zgodności bez aktualnej specyfikacji i testu (CLM-0432).

## Suwerenność bez autarkii

### Co państwo musi kontrolować

Minimalny „rdzeń kontrolowany” dla klasy systemu strategicznego powinien obejmować:

- definicję problemu i architekturę zdolności;
- kluczowe decyzje projektowe i granice modułów;
- bazę konfiguracji sprzętu, oprogramowania, danych i modeli;
- specyfikacje krytycznych interfejsów i testy zgodności;
- klucze, tożsamości i polityki dostępu — w odpowiednim bezpiecznym obiegu;
- logi potrzebne do odtworzenia zdarzeń i oceny wersji;
- dokumentację diagnostyczną, obsługową i szkoleniową;
- prawa pozwalające utrzymać, naprawić, zaktualizować albo zlecić te działania innemu podmiotowi;
- kryteria odbioru, bezpieczeństwa, ponownego dopuszczenia i wycofania;
- plan alternatywy dla dostawcy lub komponentu, którego utrata zatrzymałaby zdolność.

Kontrola nie musi oznaczać własności pełnego kodu źródłowego każdego modułu ani produkcji każdego procesora. Oznacza uzyskanie praw i artefaktów proporcjonalnych do ryzyka oraz realnej opcji działania po utracie dostawcy. Jest to definicja robocza strategii (CLM-0428), wymagająca doprecyzowania prawnego i ekonomicznego przez A06, A07 i A09.

### Trzy poziomy polityki dostaw

| Poziom | Kryterium | Domyślna polityka | Test decyzji |
|---|---|---|---|
| S1 — kontrola krytyczna | awaria lub blokada zatrzymuje zdolność; brak szybkiego zamiennika; wysoki wpływ bezpieczeństwa | kontrola architektury, danych i konfiguracji; alternatywa; prawa do utrzymania; test substytucji | czy państwo może utrzymać usługę bez pierwotnego dostawcy? |
| S2 — zaufany łańcuch sojuszniczy | komponent ważny, ale istnieją kwalifikowalne źródła w UE/NATO | co najmniej dwa kierunki dostaw, kompatybilny profil, zapas lub zdolność przeprojektowania | czy podmiana jest wykazana i ile wymaga ponownej kwalifikacji? |
| S3 — rynek konkurencyjny | element towarowy, niska blokada i mały wpływ systemowy | zakupy konkurencyjne, monitoring wycofania, bez wymogu produkcji krajowej | czy koszt kontroli przewyższa wartość opcji? |

Klasyfikacja ma być oparta na wpływie, zastępowalności, czasie odtworzenia, prawach, ryzyku cyber i ograniczeniach eksportowych — nie wyłącznie na kraju montażu. Benchmark MOSA ostrzega, że maksymalna modularność wszędzie może generować koszt i kompromisy, dlatego stosujemy „otwartość tam, gdzie daje opcję strategiczną” (CLM-0429, CLM-0430).

## TEVV i zarządzanie cyklem życia

### Bramki od problemu do skali

| Bramka | Pytanie decyzyjne | Minimalny dowód | Stop-rule |
|---|---|---|---|
| G0 — potrzeba | czy istnieje właściciel problemu, mierzalny rezultat i dopuszczalna ścieżka prawna? | karta problemu, owner, zakres jawny/chroniony, kryterium sukcesu | brak właściciela lub niemożliwa podstawa prawna |
| G1 — architektura | czy funkcje, rola człowieka, granice i interfejsy są zdefiniowane? | karta zdolności, model funkcji, wstępny profil interfejsów, strategia danych/IP | kluczowa zależność bez właściciela lub praw |
| G2 — komponent/lab | czy elementy spełniają wymagania i dają się odtworzyć? | testy komponentowe, symulacja, baza konfiguracji, ryzyka | wynik niepowtarzalny albo brak identyfikowalnej wersji |
| G3 — integracja kontrolowana | czy cały system działa oraz bezpiecznie przechodzi w tryby degradacji? | test integracyjny, logi, scenariusze błędów, ocena interfejsów | brak bezpiecznego zachowania poza zakresem lub brak logów |
| G4 — środowisko reprezentatywne | czy zachowanie odpowiada zatwierdzonym warunkom i użytkownikowi? | test w warunkach reprezentatywnych, human factors, niezależna ocena | istotna rozbieżność z wymaganiem lub niemożność nadzoru |
| G5 — ograniczony pilotaż | czy można bezpiecznie użyć małej liczby systemów i zbierać dowody? | ograniczenia użycia, plan wsparcia, obsada, monitoring, procedura wycofania | brak zdolności obsługi, reagowania na incydent lub rollbacku |
| G6 — pierwsza partia | czy konfiguracja jest produkowalna, serwisowalna i kontrolowana? | wzorzec produkcyjny, odbiór jakości, części, szkolenie, koszt cyklu życia | niekontrolowana zmiana konfiguracji lub nieakceptowalna dostępność |
| G7 — skalowanie | czy wzrost wolumenu zachowuje jakość, interoperacyjność i ciągłość? | dane z kohorty, audyt dostaw, test zamiennika, plan mocy i serwisu | skalowanie obniża jakość poniżej progu lub tworzy krytyczną blokadę |
| G8 — utrzymanie/zmiana | czy aktualizacja mieści się w zatwierdzonej bazie i zakresie? | analiza wpływu, regresja, nowa wersja dowodów, monitoring eksploatacji | zmiana funkcji, ODD lub ryzyka bez ponownej oceny |

Bramki są rekomendacją A04. Dokładne progi należą do właściwego regulatora, użytkownika i organu akceptującego. EDA i NATO potwierdzają potrzebę iteracyjnego, domenowego TEVV, a aktualny MASS Code dostarcza jawnego przykładu powiązania ConOps, zakresu działania, fallbacku i ponownej oceny zmian (CLM-0419–CLM-0423).

### Pakiet dowodowy wersji

Każda wersja dopuszczona do pilotażu lub użycia powinna mieć jednoznaczny pakiet:

- identyfikator konfiguracji sprzętu, firmware, oprogramowania, danych i modelu;
- wymagania i macierz śladowania do testów;
- listę zatwierdzonych funkcji, trybów, zakresów i ograniczeń;
- wyniki weryfikacji, walidacji, bezpieczeństwa, cyber i human factors;
- listę znanych problemów i warunków, których nie badano;
- instrukcję diagnostyki, aktualizacji, rollbacku, naprawy i wycofania;
- wykaz części, narzędzi, kompetencji i terminów wsparcia;
- właściciela decyzji o dopuszczeniu i datę następnego przeglądu;
- rejestr incydentów, zmian i dowodów z eksploatacji.

To praktyczne zastosowanie cyklu życia ISO/IEC/IEEE 15288, zarządzania aktywami ISO 55001 oraz kontroli konfiguracji i conformance z benchmarku MOSA (CLM-0416–CLM-0418, CLM-0436). Zastosowanie normy musi być formalnie ocenione; sama obecność jej numeru w specyfikacji nie dowodzi zgodności.

### KPI bez fałszywych celów liczbowych

Do czasu audytu bazowego rekomenduję mierzyć kierunek i kompletność, bez deklarowania arbitralnych targetów:

- udział aktywnych programów z kompletną kartą zdolności i bazą konfiguracji;
- udział interfejsów strategicznych z profilem, właścicielem i testem zgodności;
- liczba udanych demonstracji podmiany modułu lub dostawcy;
- czas identyfikacji konfiguracji po incydencie i czas od decyzji o zmianie do zamknięcia regresji;
- udział aktualizacji z udokumentowanym rollbackiem i analizą wpływu;
- dostępność systemu rozbita na przyczyny techniczne, logistyczne i organizacyjne;
- czas naprawy oraz udział napraw wykonywanych przez więcej niż jeden autoryzowany podmiot;
- pokrycie zatwierdzonego zakresu działania scenariuszami TEVV;
- udział systemów z kosztem cyklu życia aktualizowanym danymi eksploatacyjnymi;
- liczba wyjątków od architektury otwartej, ich wartość, właściciel i termin wygaśnięcia.

Wartości bazowe i cele powinny powstać po audycie, ponieważ stan krajowy jest obecnie `UNKNOWN` w dowodach publicznych (CLM-0431).

## C‑UAS jako architektura państwa

### Łańcuch funkcji, nie katalog efektorów

Krajowa architektura C‑UAS powinna definiować usługi i odpowiedzialności:

1. **obserwacja i zgłoszenie** — dane z legalnie dostępnych źródeł;
2. **fuzja, śledzenie i identyfikacja** — wspólny obraz wraz z jakością i pochodzeniem danych;
3. **ocena i autoryzacja** — jawnie zdefiniowany organ i próg decyzji dla danego reżimu;
4. **prawnie uprawniona reakcja** — usługa wywoływana według kompetencji, bez ukrycia właściciela decyzji w algorytmie;
5. **ocena wyniku i bezpieczeństwa osób trzecich** — informacja zwrotna oraz zakończenie incydentu;
6. **uczenie systemu** — zanonimizowane dane, aktualizacja wymagań, testów i konfiguracji.

NATO wymaga spójnej integracji C‑UAS z IAMD, odpornym C2 i warstwową obroną, a TIE 26 pokazuje znaczenie wymiany danych między sensorami i aplikacjami C2 (CLM-0424, CLM-0425). Plan UE dodaje wymiar lotnisk, granic, infrastruktury i przestrzeni publicznej oraz potrzebę koordynacji cywilno‑wojskowej (CLM-0426).

**Zasada ustrojowa:** wspólny standard danych i techniczna interoperacyjność nie mogą tworzyć domniemania wspólnej kompetencji. Każda usługa reagowania musi mieć osobnego właściciela prawnego, warunki wywołania, log decyzji i tryb nadzoru. Dokładna mapa kompetencji jest zależnością od A09 i zatwierdzenia właściwych organów (CLM-0427).

## Pięć decyzji do podjęcia

| Decyzja | Adresat i owner | Termin | Rezultat | Bramka / stop-rule | Zależności | Główne ryzyko |
|---|---|---|---|---|---|---|
| **D‑A04‑1. Zatwierdzić mandat do wspólnej taksonomii i referencyjnej architektury** | decyzja RM; owner wykonawczy MON z KPRM; BBN recenzuje spójność strategiczną | mandat do 30.09.2026, wersja 0.9 do 31.12.2026 | jeden słownik kart zdolności i dziewięć warstw architektury dla nowych pilotaży | wejście: właściciele domen; wyjście: mapowanie do NATO/EDA; stop: próba zastąpienia terminologii prawnej lub niejawnej publicznym słownikiem | A01, A02, A03, A09; udział SGWP, AU, MSWiA, ULC/PAŻP i PKN | nadmierna centralizacja i dokument bez użycia w zakupach |
| **D‑A04‑2. Wprowadzić politykę interfejsów strategicznych i praw do danych** | MON/AU; współwłaściciele MRiT, podmiot właściwy ds. cyfryzacji i PKN; kontrola prawna A09 | projekt do 31.12.2026, pilotaż w co najmniej dwóch różnych domenach do 30.06.2027 | rejestr kluczowych interfejsów, profile, repozytorium kontrolowane, testy conformance i klauzule kontraktowe | bramka: udana integracja niezależnej implementacji; stop: brak praw do utrzymania/testu albo nieproporcjonalny koszt/ryzyko bezpieczeństwa | A06, A07, A09; dostęp do umów i architektury istniejących systemów | spór IP, koszt przejścia, ujawnienie chronionych informacji |
| **D‑A04‑3. Utworzyć federację TEVV i wspólny pakiet dowodowy** | MON jako owner; wykonawcy domenowi WITU i inne akredytowane ośrodki; połączenie z EDA DTEB i NATO Innovation Ranges | katalog usług do 31.03.2027, pierwsza kampania przekrojowa do 30.06.2027 | wspólne bramki G0–G8, format dowodów, niezależny reviewer i ścieżka ponownej oceny zmian | bramka: powtarzalny test z identyfikowalną konfiguracją; stop: laboratorium jest zarazem wyłącznym wykonawcą i ostatecznym akceptującym bez niezależnej kontroli | A03, A05, A09; zasady informacji niejawnych i bezpieczeństwa poligonów | „teatr testów”, rozbieżne metody i wolniejsza adopcja |
| **D‑A04‑4. Włączyć gotowość cyklu życia do decyzji o skalowaniu** | MON/AU i właściwi nabywcy cywilni; ownerzy logistyczni użytkowników | nowe pilotaże od 01.01.2027, audyt portfela do 30.06.2027 | baza konfiguracji, pakiet utrzymania, plan części i kompetencji, rollback, koszt cyklu życia i plan wycofania jako warunek G6/G7 | bramka: odtworzenie konfiguracji i demonstracja naprawy/aktualizacji; stop: skalowanie bez support ownera, danych lub wersjonowania | A06, A07, A10; dane dostawców i użytkowników | większy koszt wejścia i pokusa omijania bramki dla pilnych potrzeb |
| **D‑A04‑5. Zatwierdzić międzyresortową architekturę C‑UAS z rozdziałem uprawnień** | KPRM jako sponsor; współwłaściciele MON i MSWiA; udział organów lotniczych, infrastruktury krytycznej i BBN | mapa funkcji i kompetencji do 31.12.2026, ćwiczenie stołowe do 31.03.2027 | wspólny model danych i usług, RACI decyzji, interfejs do NATO IAMD i plan cywilno‑wojskowych testów | bramka: każda reakcja ma podstawę prawną, ownera i audyt; stop: niejasna kompetencja, ryzyko dla lotnictwa cywilnego lub brak bezpiecznej wymiany danych | A01, A03, A05, A09; decyzje resortowe i ewentualne zmiany prawa | konflikt kompetencyjny, vendor lock-in wspólnego C2, ryzyko dla osób trzecich |

Decyzje są kolejnością logiczną. D‑A04‑1 definiuje język; D‑A04‑2 zapewnia opcję technologiczną; D‑A04‑3 tworzy dowody; D‑A04‑4 chroni dostępność po zakupie; D‑A04‑5 stosuje te reguły do zdolności wymagającej szczególnej koordynacji. Prezydent i BBN powinni oceniać ciągłość strategiczną i interoperacyjność, lecz nie przejmować ustawowych kompetencji zakupowych rządu.

## Luki danych i plan ich pozyskania

| Luka | Status | Sposób pozyskania | Owner danych | Rezultat | Termin orientacyjny |
|---|---|---|---|---|---|
| katalog systemów, wersji i ownerów operacyjnych | `UNKNOWN` | kontrolowany spis programów i aktywów z jednoznaczną definicją jednostki analizy | MON/AU i użytkownicy; odpowiedniki cywilne | baza portfela z poziomem kompletności | 90 dni od mandatu |
| specyfikacje interfejsów i rzeczywiste prawa państwa | `UNKNOWN` | przegląd umów, TDP, licencji, repozytoriów i kryteriów odbioru | AU, kancelarie prawne, integratorzy | heatmapa interfejsów strategicznych i luk praw | 120 dni |
| wykazana wymienność komponentów | `UNKNOWN` | wybrać reprezentatywne moduły i przeprowadzić test substytucji w bezpiecznym środowisku | owner programu + niezależny ośrodek TEVV | raport pass/fail i koszt zmiany | 6 miesięcy |
| baza konfiguracji sprzętu, software, danych i modeli | `UNKNOWN` | audyt konfiguracji oraz próba odtworzenia wersji użytej w wybranym teście | integrator i użytkownik, kontrola AU | wskaźnik odtwarzalności konfiguracji | 120 dni |
| zdolności laboratoriów, symulatorów i poligonów | `UNKNOWN` | katalog usług, akredytacji, ograniczeń, kolejek i formatów danych; mapowanie do DTEB/NATO | MON/WITU i sieć ośrodków | mapa federacji TEVV i luk inwestycyjnych | 90 dni |
| dostępność, awarie, naprawy i koszty cyklu życia | `UNKNOWN` | wspólny słownik zdarzeń, próbka kohort, dane logistyczne i serwisowe | użytkownicy, logistyka, dostawcy | linia bazowa availability/repair/cost | 6 miesięcy |
| podział kompetencji C‑UAS w pokoju, kryzysie i wojnie | `UNKNOWN` | prawny i operacyjny tabletop z przypadkami abstrakcyjnymi, bez danych taktycznych | KPRM, MON, MSWiA, organy lotnicze, A09 | RACI i lista zmian prawa/procedur | 4 miesiące |
| aktualne profile NATO/EDA i status standardów | częściowo publiczny | kontrolowany dostęp przez narodowe organy standaryzacji i delegacje; rejestr wersji | MON/PKN i przedstawiciele NATO/EDA | katalog profili z datą obowiązywania | proces ciągły |

Każde dwukrotne niepowodzenie w pozyskaniu wiarygodnego źródła powinno zakończyć się wpisem `UNKNOWN`, a nie imputacją zdolności firmie lub instytucji. Dane niejawne powinny trafiać do autoryzowanego obiegu, nie do tego repozytorium.

## Ryzyka, konflikty interesów i argumenty przeciw

### Ryzyka wykonawcze

1. **Architektura staje się biurokracją.** Zespół może produkować diagramy bez wpływu na wymagania i umowy. Mitigacja: każdy profil musi być użyty w pilotażu, mieć test i ownera; nieużywany profil wygasa.
2. **Standaryzacja zamraża technologię.** Zbyt szeroki standard obejmujący implementację utrudni innowację. Mitigacja: stabilizować granice i zachowanie interfejsu, nie rozwiązanie wewnętrzne; wersjonować i okresowo wygaszać profile.
3. **Otwartość obniża wynik lub bezpieczeństwo.** W niektórych systemach integracja pionowa może być lepsza. Mitigacja: dopuszczać wyjątek po analizie koszt–korzyść, z terminem wygaśnięcia i planem ryzyka blokady (CLM-0429).
4. **Test nie odzwierciedla użycia.** Pokaz przygotowany przez dostawcę może potwierdzić tylko scenariusz demonstracyjny. Mitigacja: użytkownik definiuje kryteria, niezależny ośrodek utrwala konfigurację i surowe wyniki, a G4 wymaga warunków reprezentatywnych.
5. **Ciągłe aktualizacje obchodzą dopuszczenie.** Model lub software zmienia zachowanie po odbiorze. Mitigacja: identyfikator wersji, analiza wpływu i G8; zmiana funkcji, danych lub zakresu uruchamia ponowną ocenę.
6. **Wspólny C2 tworzy pojedynczy punkt blokady.** Jeden integrator może kontrolować cały ekosystem. Mitigacja: architektura federacyjna, rozdzielone usługi, kontrolowane interfejsy i test z więcej niż jednym dostawcą.
7. **Suwerenność jest mylona z krajowym montażem.** Wysoki udział montażu nie gwarantuje praw, konfiguracji ani dostaw. Mitigacja: KPI kontrolowalności, substytucji i czasu odtworzenia zamiast samego pochodzenia.
8. **Wymogi lifecycle opóźniają pilne wdrożenie.** Pełny pakiet dla prototypu może być nieproporcjonalny. Mitigacja: dowody rosną bramka po bramce; pilotaż ma ograniczenia i plan wycofania, a pełne wymagania są warunkiem skali, nie pierwszej próby.
9. **Normy są niedostępne lub zmieniają status.** Publiczny abstrakt nie wystarcza do conformance. Mitigacja: licencjonowany dostęp, rejestr wersji, data przeglądu i zakaz deklarowania zgodności na podstawie strony marketingowej.
10. **Niejasny owner ryzyka systemu systemów.** Każdy moduł może przejść test osobno, a zintegrowana całość nadal zawieść. Mitigacja: jeden integrator odpowiedzialny za dowód end-to-end i niezależny organ akceptujący.

### Konflikty interesów

- Integrator dominujący może promować własny interfejs jako „standard”, a następnie kontrolować narzędzia zgodności.
- Dostawca może definiować wymaganie, implementować produkt i oceniać własny test; te role trzeba rozdzielić.
- Ośrodek testowy finansowany niemal wyłącznie przez jednego dostawcę lub program może nie być wystarczająco niezależny.
- Właściciel laboratorium może postulować budowę nowej infrastruktury mimo dostępnej zdolności w innym ośrodku UE/NATO.
- Użytkownik może żądać wyjątku od dokumentacji dla szybkości, przenosząc koszt i ryzyko na logistykę po zakupie.
- Organ standaryzacyjny lub ekspert może mieć interes licencyjny, patentowy albo konsultingowy w rekomendowanym profilu.

Każdy członek grupy architektonicznej powinien deklarować role dostawcy, właściciela IP, wykonawcy testów i beneficjenta zamówień. Dostawca może uczestniczyć w konsultacjach, ale nie może samodzielnie ustalić kryterium, wybrać profilu i zatwierdzić zgodności własnego produktu.

### Najsilniejsze argumenty przeciw rekomendacji — i odpowiedź

**„Wojna wymaga szybkości, nie standardów.”** To prawda, że pełna normalizacja przed pierwszym testem byłaby błędem. Proponowany model narasta: G1 wymaga minimalnych granic i praw, a pełny pakiet jest warunkiem skali. Szybkość prototypu nie usprawiedliwia niewiedzy, jaką wersję kupiono i kto ją naprawi.

**„Zamknięty system jednego dostawcy będzie działał lepiej.”** W wybranych przypadkach może. Wyjątek powinien opisywać korzyść, koszt zależności, warunek wyjścia i termin ponownej oceny. Strategia nie zabrania integracji pionowej; zabrania ukrywania jej kosztu strategicznego.

**„Jedna wspólna architektura nie pasuje do powietrza i podwodnia.”** Nie pasuje jedna implementacja. Pasuje wspólny kontrakt: karta funkcji, właściciel, wersja, interfejs, dowód, zakres działania i lifecycle. Właściwe testy i szczegóły pozostają domenowe.

**„Pełna krajowa produkcja jest bezpieczniejsza.”** Nie zawsze. Autarkia może zwiększyć koszt, opóźnić dostęp i stworzyć krajowy monopol. Bezpieczniejsza jest kontrola punktów krytycznych, zaufane alternatywy i wykazana zdolność odtworzenia.

**„Wspólne C‑UAS powinno mieć jeden centralny organ.”** Techniczna koordynacja i wspólny obraz są potrzebne, ale kompetencje zależą od miejsca, czasu, zagrożenia i reżimu prawnego. Centralizacja bez podstawy prawnej zwiększa ryzyko decyzji i odpowiedzialności; najpierw potrzebny jest RACI oraz architektura federacyjna.

## Dalsze pytania decyzyjne

1. Które jawne klasy problemów mają być pierwszymi „mission threads” do walidacji wspólnej architektury w dwóch różnych domenach?
2. Kto będzie państwowym właścicielem referencyjnej architektury i kto ma prawo zatwierdzić wyjątek od niej?
3. Jakie minimalne prawa do danych, interfejsów i utrzymania państwo jest gotowe finansować — i kiedy zaakceptuje system zamknięty?
4. Który organ będzie niezależnym akceptującym TEVV dla systemu systemów, gdy składowe podlegają różnym regulatorom?
5. Jak mapować jawny katalog profili na chronione standardy NATO bez tworzenia ryzyka ujawnienia?
6. Jaki reżim zmian obejmie modele uczące się, aktualizacje danych i konfiguracje zdalne?
7. Kto ma utrzymywać implementacje referencyjne i narzędzia conformance po zakończeniu projektu finansującego?
8. Jak rozdzielić wspólny obraz C‑UAS od prawnych uprawnień do konkretnej reakcji w pokoju, kryzysie i wojnie?
9. Które elementy wymagają krajowej kontroli S1, a które mogą pozostać w zaufanym łańcuchu UE/NATO S2?
10. Jakie koszty przejścia poniosą istniejące systemy i które z nich lepiej pozostawić jako kontrolowane wyjątki niż modernizować za wszelką cenę?

## Założenia i zastrzeżenia

- Memorandum korzysta wyłącznie z jawnych źródeł urzędowych i oficjalnych stron standardów dostępnych 21 lipca 2026 r.
- Opisy norm ISO opierają się na publicznych abstraktach i metadanych; nie przeprowadzono oceny zgodności z pełnym tekstem.
- Przewodnik MOSA Departamentu Obrony USA jest benchmarkiem zagranicznym, nie źródłem prawa polskiego ani wymaganiem NATO.
- INTERACT był projektem rozwoju standardu; komunikat z 2023 r. nie dowodzi istnienia obowiązującego kompletnego standardu.
- CMRE opisuje „new draft version” STANAG 4817; nie wolno skracać tego do deklaracji pełnej zgodności NATO (CLM-0432).
- MASS Code jest niewiążącym kodem cywilnym, nie dotyczy okrętów wojennych i służy tu tylko jako aktualny wzorzec funkcjonalnego assurance.
- Liczb docelowych dla modularności, dostępności, napraw i substytucji nie ustalono, bo brak publicznej bazy polskiego portfela (CLM-0431).
- Szczegółowe kwestie AI/cyber, przemysłu, finansów i prawa należą odpowiednio do A05, A06, A07 i A09; A04 definiuje miejsca styku i artefakty przekazania.

## Skrócona mapa dowodów

- NATO Autonomy Implementation Plan — SRC-0401, CLM-0401–CLM-0402.
- EDA APAS i taksonomia — SRC-0402–SRC-0404, CLM-0403–CLM-0408.
- Interoperacyjność i standardy EDA/INTERACT — SRC-0405–SRC-0407, CLM-0409–CLM-0410, CLM-0419.
- Lifecycle i modularność — SRC-0408–SRC-0409, SRC-0418–SRC-0420, CLM-0411–CLM-0418, CLM-0428–CLM-0430, CLM-0435–CLM-0436.
- Domeny powietrzna, lądowa, nawodna i podwodna — SRC-0410–SRC-0412, CLM-0406.
- Funkcjonalne assurance i zakres działania — SRC-0413, CLM-0420–CLM-0421.
- C‑UAS, NATO IAMD i UE — SRC-0414–SRC-0417, CLM-0424–CLM-0427.
- Cywilny przykład klasyfikacji ryzyka UAS — SRC-0421, CLM-0433–CLM-0434.
- Interoperacyjne C2 systemów bezzałogowych NATO — SRC-0422, CLM-0432.

**Wniosek końcowy:** państwo powinno finansować nie tylko platformy, lecz także możliwość ich kontrolowanego łączenia, sprawdzania, naprawiania, aktualizowania i zastępowania. Najważniejszym produktem pierwszego roku nie jest „uniwersalny dron”, lecz działający kontrakt architektoniczny użyty w realnych pilotażach dwóch domen i C‑UAS.
