# A09 — Architektura prawna, etyka i bezpieczeństwo informacji programu „Polska 2040”

**Memorandum problem-spotting dla Prezesa Rady Ministrów i Prezydenta RP**
**Stan prawny i stan jawnych źródeł: 21 lipca 2026 r.**
**Klauzula metodologiczna:** dokument jest analizą problemów i bramek decyzyjnych, a nie opinią prawną dla konkretnej transakcji, zamówienia, systemu AI ani użycia siły. Obejmuje wyłącznie informacje jawne. Nie zawiera parametrów operacyjnych, instrukcji konstrukcji lub użycia broni, podatności, częstotliwości, danych poligonowych ani informacji niejawnych.

## Executive Summary / Streszczenie wykonawcze

Programu tej skali **nie należy zamykać w jednym wielkim dokumencie**. Potrzebny jest kontrolowany pakiet: jawna strategia wyznaczająca cele, program wykonawczy z finansowaniem i miernikami, uchwała uruchamiająca działania administracji, akty normatywne tylko tam, gdzie mają powstać obowiązki lub uprawnienia zewnętrzne, kontrakty zapewniające dostawy i prawa, a także odrębny chroniony obieg dla treści wrażliwych. Uchwała Rady Ministrów nie może sama stanowić podstawy obowiązków nakładanych na przedsiębiorców lub obywateli. `[CLM-0901]` `[CLM-0928]`

Przed wyborem nazwy i ścieżki przyjęcia RCL oraz minister właściwy do spraw rozwoju regionalnego powinny rozstrzygnąć, czy rdzeń ma być strategią rozwoju, polityką publiczną, czy dokumentem strategicznym innego rodzaju. Obecnie to `UNKNOWN`, ponieważ zakres, horyzont, relacja z istniejącymi strategiami i katalog działań ustawowych nie są jeszcze zamknięte. `[CLM-0902]` `[CLM-0903]` `[CLM-0940]`

Model szybkiego wdrażania musi mieć **co najmniej trzy legalne ścieżki pozyskania**. Cywilne partnerstwo innowacyjne nie może być automatycznie użyte do zamówień zakwalifikowanych jako obronne lub bezpieczeństwa — polskie PZP wyłącza ten tryb w tej dziedzinie. Dla projektów obronnych trzeba używać właściwych trybów, dokumentować konkurencję i ewentualne odstępstwa, a wymagania bezpieczeństwa dostaw, utrzymania, zmian w łańcuchu i środków do produkcji części wprowadzać proporcjonalnie do kontraktu. `[CLM-0906]` `[CLM-0907]` `[CLM-0908]` `[CLM-0930]`

„Bezpieczny pokój danych” nie może być jednym wspólnym dyskiem. Informacje niejawne, tajemnica przedsiębiorstwa, dane osobowe, dane podlegające kontroli eksportu i informacja publiczna mają odrębne podstawy i reguły. Publiczne repozytorium może zawierać tylko warstwę jawną; przetwarzanie informacji niejawnych wymaga właściwego środowiska, uprawnień i — gdy ma zastosowanie — akredytacji oraz bezpieczeństwa przemysłowego. `[CLM-0910]` `[CLM-0911]` `[CLM-0912]` `[CLM-0913]` `[CLM-0931]`

„Prawo do naprawy”, depozyt kodu i „produkcja awaryjna” nie powstają przez sam slogan. Krytyczny kontrakt powinien osobno regulować background IP, foreground IP, ulepszenia, dokumentację, interfejsy, build, testy, naprawę, modyfikację, sublicencję, wykonawcę zastępczego i zdarzenia step-in. Depozyt bez licencji, aktualizacji i testu odtworzenia daje pozorne bezpieczeństwo. `[CLM-0914]` `[CLM-0915]` `[CLM-0932]` `[CLM-0933]`

Kontrola eksportu i sankcji ma działać **od pierwszego udostępnienia technologii**, nie dopiero przed wysyłką produktu. Kod, modele, dokumentacja i zdalne wsparcie mogą stanowić kontrolowany transfer. Strategia eksportowa może opisywać rynki scenariuszowo, ale nie może obiecywać licencji, zanim właściwy organ oceni produkt, użytkownika końcowego, użycie, ryzyko dywersji, reeksport i aktualne sankcje. `[CLM-0916]` `[CLM-0917]` `[CLM-0918]` `[CLM-0919]` `[CLM-0934]`

Wyłączenie AI Act nie obejmuje automatycznie całego dual-use. Każdy przypadek potrzebuje karty zakresu. Niezależnie od kwalifikacji prawnej program powinien przyjąć wspólne Responsible Autonomy Assurance oparte na odpowiedzialności, identyfikowalności, niezawodności, sterowalności, kontroli zmian i niezależnej ocenie. Dla nowej broni, środka albo metody walki odrębną bramką pozostaje przegląd prawny zgodny z art. 36 Protokołu dodatkowego I. Etyka nie zastępuje prawa i nie może służyć jako „certyfikat moralny” produktu. `[CLM-0921]` `[CLM-0922]` `[CLM-0923]` `[CLM-0924]` `[CLM-0936]` `[CLM-0937]`

Strategia obejmująca przemysł, regiony, energetykę, centra danych, cywilne wdrożenia i infrastrukturę nie powinna zakładać wyłączenia z oceny środowiskowej jako dokument „wyłącznie obronny”. Screening SOOŚ trzeba rozpocząć razem z wyborem instrumentu, a konsultacje i udział społeczeństwa zaprojektować tak, aby chronić dane wrażliwe bez pozornego lub nadmiernego utajnienia. `[CLM-0920]` `[CLM-0938]` `[CLM-0944]`

Każde JV — także z partnerem ukraińskim — wymaga tej samej bramki: beneficjent rzeczywisty i kontrola, sankcje, FDI, koncentracja, FSR, pomoc państwa, eksport, IP, bezpieczeństwo informacji, cyber, ciągłość i konflikty interesów. Żadna firma nie może uzyskać statusu preferowanego partnera przed porównaniem i due diligence. `[CLM-0925]` `[CLM-0926]` `[CLM-0927]` `[CLM-0939]`

## 1. Jak czytać statusy twierdzeń

W pakiecie obowiązuje następujący język:

- `FACT` — twierdzenie opisowe oparte na wskazanym źródle; pozostaje `unverified`, dopóki niezależny reviewer go nie zatwierdzi;
- `INFERENCE` — wniosek z kilku norm lub faktów, który wymaga weryfikacji na konkretnym stanie faktycznym;
- `SCENARIO` — wariant architektury lub przyszłego zdarzenia, a nie prognoza;
- `RECOMMENDATION` — zalecenie doradcze z właścicielem i bramką;
- `UNKNOWN` — brak danych lub rozstrzygnięcia; wymaga pytania do właściwego organu lub pozyskania materiału;
- `ESTIMATE` — szacunek liczbowy. W tym pakiecie nie użyto szacunków kosztów ani prawdopodobieństw; powinny powstać w modelu A07 po ustaleniu podstaw prawnych i założeń.

Rejestr `a09-claims.yaml` zawiera autora `A09`, recenzenta `null` i status `unverified` dla każdego twierdzenia. Autor nie weryfikuje własnych tez.

## 2. Dziesięć kluczowych ustaleń

1. **Uchwała Rady Ministrów jest potrzebna, lecz niewystarczająca.** Uruchamia i koordynuje administrację, ale nie tworzy samodzielnie obowiązków przedsiębiorców, szkół niepublicznych, jednostek samorządu ani obywateli. `[CLM-0901]`
2. **Strategia i wykonanie to różne dokumenty.** Dokument polityczny powinien wskazywać cele i wybory; program wykonawczy ma opisywać system realizacji, finansowanie, mierniki i ewaluację. `[CLM-0902]` `[CLM-0903]`
3. **Pełnomocnik nie otrzymuje magicznej zwierzchności międzyresortowej.** Jego status, umocowanie, obsługa i relacja z ministrami muszą wynikać z właściwych instrumentów; tytuł „minister–pełnomocnik” nie rozstrzyga kompetencji. `[CLM-0904]`
4. **Szybkość nie znosi kwalifikacji zamówienia.** Ścieżka obronna, cywilna dual-use i B+R mają inne tryby, przesłanki, dokumentację oraz dopuszczalne odstępstwa. `[CLM-0906]` `[CLM-0907]` `[CLM-0930]`
5. **Informacja niejawna, tajemnica przedsiębiorstwa i dane osobowe to trzy różne reżimy.** Jedna klauzula NDA lub oznaczenie „confidential” nie zastępuje ustawy, uprawnień i zabezpieczeń. `[CLM-0910]` `[CLM-0911]` `[CLM-0913]`
6. **Depozyt kodu nie jest licencją.** Ciągłość wymaga praw, materiałów i praktycznej możliwości odtworzenia oraz przejęcia utrzymania po zdefiniowanym zdarzeniu. `[CLM-0914]` `[CLM-0915]` `[CLM-0933]`
7. **Eksport technologii może nastąpić bez fizycznej wysyłki.** Udostępnienie kodu, modelu, dokumentacji lub pomocy technicznej partnerowi zagranicznemu wymaga wcześniejszej kwalifikacji. `[CLM-0917]`
8. **Dual-use nie oznacza automatycznego wyłączenia AI Act.** O zakresie decyduje konkretne przeznaczenie, wprowadzenie do obrotu, oddanie do użytku i wykorzystanie. `[CLM-0921]` `[CLM-0942]`
9. **Przegląd art. 36 jest bramką prawną, nie kampanią etyczną.** Musi być niezależny od interesu dostawcy i pojawić się wystarczająco wcześnie, aby wpłynąć na decyzję o rozwoju lub pozyskaniu. `[CLM-0924]` `[CLM-0937]`
10. **JV jest transakcją, a nie tylko programem współpracy.** Wymaga warunków zawieszających i pełnego screeningu przed transferem kontroli, danych, technologii lub pieniędzy. `[CLM-0925]` `[CLM-0927]` `[CLM-0939]`

## 3. Zalecana architektura dokumentów i instrumentów

### 3.1. Odpowiedź na pytanie: jeden dokument czy wiele?

Należy zbudować **jeden spójny pakiet wielu dokumentów**, utrzymywany przez wspólny rejestr celów, decyzji, źródeł i wersji. Jeden dokument liczący kilkaset stron byłby jednocześnie zbyt ogólny dla wykonawców i zbyt szczegółowy dla Premiera, Prezydenta oraz opinii publicznej. Łączenie warstwy jawnej i chronionej zwiększałoby ryzyko nadmiernego utajnienia albo nieuprawnionego ujawnienia. `[CLM-0928]`

Rekomendowany zestaw:

| Artefakt | Funkcja | Odbiorca | Forma | Czego nie może zastąpić |
| --- | --- | --- | --- | --- |
| **Strategia jawna „Polska 2040”** | kierunek, diagnoza, cele, wybory, wskaźniki wynikowe, zasady odpowiedzialności | Rada Ministrów, Prezydent, Sejm, samorząd, przemysł, obywatele, UE/NATO | dokument strategiczny przyjęty po ustaleniu podstawy i konsultacjach | ustawy, budżetu, kontraktu, decyzji licencyjnej, niejawnego planu zdolności |
| **Program wykonawczy 2027–2030 z kroczącą aktualizacją** | portfel działań, właściciele, finansowanie, KPI, bramki, ewaluacja, harmonogram | RM, KPRM, resorty, instytucje finansujące | program w rozumieniu właściwej podstawy prawnej lub analogiczny dokument wykonawczy | indywidualnej decyzji o wydatku, pomocy państwa, zamówieniu lub inwestycji |
| **Uchwała RM** | przyjęcie dokumentu, zadania podległych jednostek, raportowanie, rozpoczęcie prac legislacyjnych | administracja rządowa | akt wewnętrzny | obowiązków podmiotów zewnętrznych `[CLM-0901]` |
| **Rozporządzenie RM o pełnomocniku** | status, zakres zadań, nadzór i obsługa pełnomocnika | administracja rządowa | rozporządzenie na podstawie ustawy o RM | nowych kompetencji materialnych niewynikających z ustaw `[CLM-0904]` |
| **Pakiet legislacyjny** | tylko zidentyfikowane obowiązki, uprawnienia, wydatki, rejestry lub zasady wymagające normy powszechnej | parlament, RM, organy stosujące prawo | ustawa i akty wykonawcze | szczegółów technicznych i warunków konkretnej dostawy |
| **Jawne plany dziedzinowe** | kadry, przemysł, dane i AI, regiony, eksport, cywilne wdrożenia | właściwe resorty i interesariusze | załączniki/programy sektorowe | chronionych potrzeb operacyjnych |
| **Chroniony aneks zdolności i ryzyk** | pytania, luki, wymagania i dane dostępne wyłącznie uprawnionym | Prezydent/BBN, PM, MON, uprawnione organy | dokument w odrębnym, legalnym obiegu | publicznej strategii, normy prawnej ani procedury art. 36 |
| **Playbook zamówień i klauzul** | kwalifikacja ścieżki, wzorce umów, IP, bezpieczeństwo dostaw, exit i audit | AU, zamawiający, instytucje finansujące | zatwierdzone procedury i wzorce | dokumentacji konkretnego postępowania |
| **Playbook transakcyjny JV/eksport** | due diligence, conditions precedent, screening, zgody, post-closing monitoring | KPRM, MON, MRiT, PFR/BGK, spółki | procedura i checklisty | opinii prawnej dla konkretnej transakcji |
| **Pakiet komunikacyjny** | prezentacja RM, brief Prezydenta, deck forum gospodarczego, karta regionalna | różne grupy | osobne skróty z jednej bazy twierdzeń | dokumentu decyzyjnego ani materiału chronionego |

### 3.2. Macierz instrumentów prawnych

| Instrument | Kiedy używać | Co może osiągnąć | Czego nie może osiągnąć | Właściciel projektu | Bramka |
| --- | --- | --- | --- | --- | --- |
| **Strategia rozwoju** | gdy program ma długofalowy, przekrojowy wpływ na rozwój kraju i system wykonawczy | ustalić cele, kierunki interwencji, wskaźniki i ramy programów | nałożyć bezpośredni obowiązek na firmę bez podstawy ustawowej | minister wyznaczony po konsultacji z MFiPR | zgodność z systemem strategii i konsultacje `[CLM-0902]` |
| **Polityka publiczna** | gdy potrzebny jest dokument dla konkretnej dziedziny i horyzont zgodny z ustawą | opisać cele, narzędzia, monitoring i ewaluację | obejść ograniczenia horyzontu lub obowiązki środowiskowe | właściwy minister i RM | opinia MFiPR, kwalifikacja horyzontu `[CLM-0940]` |
| **Program wykonawczy** | gdy istnieje strategia i trzeba przełożyć ją na działania i finansowanie | przydzielić zadania administracji, zbudować system realizacji i plan finansowy | zapewnić środki bez decyzji budżetowych lub właściwej podstawy | właściwy minister/koordynator | wskazane finansowanie, właściciel i miernik `[CLM-0903]` |
| **Uchwała RM** | do przyjęcia dokumentu i organizacji pracy rządu | zobowiązać podległe jednostki, uruchomić raportowanie i przygotowanie ustaw | nakładać obowiązki na przedsiębiorców lub obywateli | KPRM/RCL | test art. 93 Konstytucji `[CLM-0901]` |
| **Rozporządzenie** | tylko gdy ustawa zawiera szczegółowe upoważnienie | wykonać ustawę w granicach delegacji | stworzyć nową kompetencję bez delegacji | właściwy organ | kontrola zgodności z delegacją |
| **Ustawa** | gdy potrzebne są nowe obowiązki, rejestry, kompetencje, trwałe finansowanie lub ingerencja w prawa | stworzyć podstawę powszechną i mechanizmy kontroli | zastąpić specyfikację, umowę i zarządzanie | RM/parlament | OSR, konsultacje, zgodność konstytucyjna i unijna |
| **Umowa publiczna** | dla dostawy, B+R, usługi, licencji, utrzymania i praw | rozdzielić ryzyka, wynagrodzenie, IP, bezpieczeństwo, testy i exit | zalegalizować zakazany transfer lub obejść sankcje | zamawiający | kwalifikacja PZP, eksportu, informacji i pomocy państwa |
| **Umowa JV/akcjonariuszy** | dla wspólnego przedsięwzięcia z podziałem kontroli i praw | określić governance, aporty, IP, deadlock, exit i step-in | zastąpić zgody FDI, koncentracji, FSR lub eksportu | strony transakcji + nadzór państwowy | conditions precedent `[CLM-0939]` |
| **MOU z państwem** | dla niewiążącej intencji, jeśli treść rzeczywiście nie tworzy zobowiązań międzynarodowych | ustalić polityczny kierunek i obszary pracy | ukryć wiążącą umowę pod inną nazwą | MSZ/KPRM/właściwy minister | kwalifikacja przez MSZ/RCL `[CLM-0905]` |
| **Umowa międzynarodowa** | gdy zobowiązanie państw podlega prawu międzynarodowemu | wiążąco uregulować współpracę państw | pominąć wymaganej zgody, ratyfikacji lub publikacji | RM/MSZ/Prezydent w ramach Konstytucji | kwalifikacja trybu z art. 89 i 133 `[CLM-0905]` |

### 3.3. Trzy scenariusze legislacyjne

Nie należy zaczynać od „specustawy Polska 2040”. Najpierw trzeba przeprowadzić gap analysis. `[CLM-0946]`

- **Scenariusz minimalny:** istniejące strategie, dobrowolna koordynacja, obecne instrumenty finansowe, standardowe zamówienia i umowy. Najszybszy, ale słaby tam, gdzie państwo potrzebuje danych lub zachowania podmiotu prywatnego bez kontraktu.
- **Scenariusz bazowy:** jawna strategia, program wykonawczy, pełnomocnik w istniejących ramach, wzorce kontraktów, fundusze i pilotaże. Nowelizacje tylko punktowe.
- **Scenariusz pełny:** ustawa programowa ograniczona do udowodnionych luk, np. nowych kompetencji, obowiązków raportowych, ram bezpiecznego udostępniania, wieloletniego instrumentu finansowego lub produkcji awaryjnej. Każda ingerencja musi mieć cel, adresata, środki ochrony, kontrolę i finansowanie.

To są `SCENARIO`, nie rozstrzygnięcia. `[CLM-0947]`

## 4. Governance: KPRM, pełnomocnik, Prezydent i odpowiedzialność

### 4.1. Model wykonalny w istniejących ramach

Pełnomocnik Rządu może być dobrym właścicielem koordynacji, lecz nie zastąpi kompetencji MON, MRiT, MF, MNiSW, MEN, MC, MSWiA, MSZ, UOKiK, UODO, ABW/SKW ani zamawiających. Ustawa o Radzie Ministrów określa jego status i wymaga rozporządzenia. `[CLM-0904]`

Zalecany układ:

- **Prezes Rady Ministrów:** właściciel polityczny i arbiter sporów; zatwierdza bramki portfela i kieruje projekty na RM.
- **Pełnomocnik Rządu — sekretarz stanu w KPRM albo właściwym resorcie:** prowadzi Biuro Realizacji, dashboard, rejestr decyzji i przeglądy; nie wydaje poleceń poza kompetencją.
- **Komitet RM:** podejmuje decyzje międzyresortowe, uzgadnia finansowanie, kieruje akty prawne i zamyka projekty.
- **Właściwi ministrowie i kierownicy urzędów:** odpowiadają za działania w swoich działach i indywidualne decyzje.
- **Prezydent i BBN:** otrzymują brief bezpieczeństwa, identyfikują strategiczne ryzyka i zapewniają ciągłość dialogu; nie przejmują wykonawczych kompetencji Rady Ministrów.
- **Niezależny red-team:** nie podlega właścicielowi projektu ocenianego; raportuje krytyczne sprzeczności PM i — w odpowiednim zakresie — Prezydentowi/BBN.

### 4.2. RACI musi być oparty na kompetencji, nie prestiżu

Każdy rezultat ma mieć:

1. `A — Accountable`: jeden organ lub kierownik z podstawą prawną;
2. `R — Responsible`: zespół wykonawczy;
3. `C — Consulted`: organy wymagane prawem i eksperci;
4. `I — Informed`: odbiorcy jawni lub uprawnieni;
5. podstawę prawną i instrument;
6. źródło finansowania;
7. tryb odwoławczy lub audyt;
8. klasyfikację informacji;
9. stop-rule.

Jeżeli dwa podmioty są `A`, nikt nie jest faktycznie odpowiedzialny. Jeżeli pełnomocnik jest `A` bez podstawy do decyzji, dashboard będzie pokazywał postęp formalny zamiast wykonania.

## 5. Szybkie zamówienia i innowacje — legalne ścieżki

### 5.1. Karta kwalifikacji przed projektem

Przed kontaktem rynkowym, grantem lub specyfikacją każdy problem powinien otrzymać krótką kartę:

- właściciel potrzeby i użytkownik;
- wynik, który ma zostać osiągnięty, bez ujawniania treści operacyjnej w warstwie jawnej;
- czy przedmiot i cel mieszczą się w zamówieniach obronnych lub bezpieczeństwa;
- czy potrzebne są badania, prototyp, usługa, dostawa, licencja czy inwestycja;
- czy jest istniejący rynek i możliwa konkurencja;
- reżim informacji, danych osobowych i eksportu;
- źródło finansowania i reguły programu UE;
- potencjalny konflikt interesów;
- proponowany tryb i przesłanki;
- prawa do wyników, danych i ciągłości;
- organ zatwierdzający i stop-rule.

Brak karty nie blokuje wstępnego badania problemu, ale blokuje publikację zaproszenia, przekazanie informacji chronionej i zaciągnięcie zobowiązania. `[CLM-0930]`

### 5.2. Trzy podstawowe ścieżki

| Ścieżka | Kiedy | Możliwe narzędzia na wysokim poziomie | Kluczowa bramka | Największe ryzyko |
| --- | --- | --- | --- | --- |
| **A — obronność i bezpieczeństwo** | przedmiot i cel kwalifikują się do działu VI PZP | przetarg ograniczony lub negocjacje z ogłoszeniem; inne tryby tylko po spełnieniu przesłanek; fazowanie i opcje kontraktowe | udokumentowana kwalifikacja oraz dobór trybu `[CLM-0906]` `[CLM-0907]` | bezpodstawna wolna ręka albo mechaniczne użycie cywilnego partnerstwa innowacyjnego |
| **B — cywilny dual-use** | produkt/usługa ma cywilny cel i nie jest zamówieniem obronnym | zwykłe tryby PZP, w tym partnerstwo innowacyjne, jeżeli przesłanki są spełnione; zamówienia przedkomercyjne tylko po właściwej analizie | konkurencja, pomoc państwa, IP i AI/data scope | nazwanie cywilnego zakupu „bezpieczeństwem”, aby uniknąć reguł |
| **C — B+R/grant/inwestycja** | państwo finansuje rozwój zdolności, a nie kupuje z góry produktu na warunkach zamówienia | konkurs grantowy, instrument kapitałowy, pożyczka/gwarancja, kontrakt B+R; zasady zależą od podstawy | kwalifikacja zamówienia, pomocy państwa i praw do wyników | grant napisany jak ukryte zamówienie albo selektywne wsparcie bez podstawy |

### 5.3. Jak zaprojektować cykl 60–120 dni bez obchodzenia prawa

Szybkość wynika z przygotowanych wzorców i równoległych bramek, nie z pomijania procedury:

1. **Problem i karta kwalifikacji.** Jawna część opisuje efekt i kryterium; chroniona część pozostaje w właściwym obiegu.
2. **Badanie rynku lub konkurencyjny nabór.** Dostawca nie może samodzielnie zdefiniować potrzeby, wybrać trybu i ocenić własnego produktu.
3. **Kontrakt fazowy.** Kamienie milowe, płatności częściowe, kryteria wejścia/wyjścia i prawo zakończenia nierokującego projektu.
4. **Test.** Z góry określony właściciel dowodu, bezpieczeństwo danych, konflikt interesów i zasady przyjęcia; wynik negatywny jest pełnoprawnym rezultatem.
5. **Mała partia.** Opcja tylko po przejściu testu, dostępności finansowania i sprawdzeniu zgodności.
6. **Skalowanie.** Nowa bramka bezpieczeństwa dostaw, jakości, IP, serwisu, eksportu i kosztu cyklu życia.

### 5.4. Bezpieczeństwo dostaw i prawa awaryjne

PZP oraz dyrektywa obronna pozwalają stawiać wymagania dotyczące łańcucha, zdolności kryzysowej, utrzymania, modernizacji i określonych środków do produkcji części. `[CLM-0908]` Nie jest to jednak podstawa do automatycznego przejęcia całego IP dostawcy.

Minimalna klauzula dla elementu krytycznego powinna określać:

- zdarzenia, przy których powstaje obowiązek dodatkowej dostawy lub step-in;
- wymagany rezultat, terminy i maksymalny zakres;
- dokumentację, narzędzia, licencje i wsparcie niezbędne do rezultatu;
- prawa podmiotów trzecich i ograniczenia eksportowe;
- obowiązek zgłaszania zmian właściciela, lokalizacji, poddostawcy lub zakończenia wsparcia;
- wynagrodzenie, koszt utrzymania gotowości i zasady waloryzacji;
- audyt i test ciągłości;
- ochronę tajemnicy przedsiębiorstwa i informacji niejawnych;
- cure period, rozwiązanie umowy i odpowiedzialność.

**Stop-rule:** wymóg „państwo ma dostać wszystko” bez związku z krytycznością, wyceną i legalnym celem zatrzymuje klauzulę do przeprojektowania. Nadmierne prawa mogą wyeliminować MŚP, podnieść ceny i uniemożliwić JV.

### 5.5. Art. 346 TFUE

Art. 346 TFUE nie powinien być wpisany do strategii jako ogólna „furtka”. Przepis odnosi się do środków niezbędnych dla ochrony podstawowych interesów bezpieczeństwa i zawiera ograniczenie dotyczące rynku produktów nieściśle wojskowych. `[CLM-0909]`

Każde użycie wymaga odrębnego memo:

- jaki jest podstawowy interes bezpieczeństwa;
- jakie ryzyko powstaje przy zastosowaniu zwykłych reguł;
- dlaczego środek i zakres są niezbędne;
- czy istnieje mniej ograniczająca alternatywa;
- jakie produkty i części programu pozostają poza odstępstwem;
- jak decyzja jest dokumentowana i kontrolowana.

## 6. Informacje chronione i bezpieczna przestrzeń danych

### 6.1. Cztery strefy, nie jeden magazyn

| Strefa | Przykładowa zawartość | Reżim | Gdzie może być przechowywana | Zasada publikacji |
| --- | --- | --- | --- | --- |
| **P0 — publiczna** | jawna strategia, metodologia, agregaty, źródła, decyzje i wskaźniki bez wrażliwych szczegółów | informacja publiczna, prawa autorskie, dostępność | publiczne repozytorium | publikacja po QA i red-team |
| **P1 — robocza administracyjna** | wersje robocze, komentarze, wewnętrzne analizy bez informacji prawnie chronionej | obieg dokumentów, archiwizacja, dostęp służbowy | zarządzane systemy administracji | ocena wniosku według prawa, nie automatyczna odmowa |
| **P2 — chroniona nieklasyfikowana** | tajemnica przedsiębiorstwa, dane osobowe, kontrolowana technologia, poufne materiały transakcyjne | umowa + właściwa ustawa, need-to-know, DLP, logi i retencja | autoryzowany data room z kontrolą dostępu | wyłącznie agregat lub prawidłowo zanonimizowana/redagowana wersja |
| **P3 — informacja niejawna** | materiał formalnie zaklasyfikowany przez uprawniony podmiot | ustawa o ochronie informacji niejawnych i wymagania przemysłowe/teleinformatyczne | wyłącznie właściwy, akredytowany obieg i uprawnieni użytkownicy | nie trafia do publicznego repozytorium `[CLM-0910]` |

Strefa wynika z treści i prawa, nie z wygody autora. Nadmierne oznaczanie ogranicza kontrolę publiczną i konkurencję; niedostateczna ochrona może narazić państwo, przedsiębiorcę i osoby fizyczne. `[CLM-0911]` `[CLM-0912]`

### 6.2. Karta każdego zbioru danych

Przed ingestem do data roomu trzeba zapisać:

1. nazwę i właściciela zbioru;
2. źródło i pochodzenie danych;
3. cel oraz zakazane cele wtórne;
4. podstawę prawną i reżim sektorowy;
5. administratora, procesora i odbiorców, jeśli występują dane osobowe;
6. klasy informacji i jurysdykcję;
7. minimalny zakres, jakość i okres retencji;
8. uprawnienia, zatwierdzenia i logowanie dostępu;
9. zasady trenowania, ewaluacji, eksportu i publikacji;
10. warunki usunięcia, zwrotu i audytu;
11. ocenę skutków dla ochrony danych, jeżeli jest wymagana;
12. plan incydentu i powiadomienia.

Nie ma obecnie zatwierdzonego katalogu zbiorów ani podstaw — stan pozostaje `UNKNOWN`. `[CLM-0941]`

### 6.3. Sześć twardych zasad data roomu

- **Brak danych niejawnych w GitHubie i chmurze publicznej przeznaczonej dla dokumentów jawnych.** `[CLM-0910]`
- **Brak domniemanej zgody na wtórne trenowanie.** Cel modelu i zakres licencji muszą być wskazane.
- **Brak dostępu całej firmy.** Imienny need-to-know, role, logi i data zakończenia dostępu.
- **Brak trwałej kopii „na wszelki wypadek”.** Retencja i usunięcie zgodnie z celem i prawem.
- **Brak eksportu przez link.** Dostęp transgraniczny i zdalne wsparcie przechodzą kwalifikację eksportową. `[CLM-0917]`
- **Brak deklaracji „anonimowe” bez testu.** Należy ocenić realną możliwość ponownej identyfikacji i połączenia zbiorów.

### 6.4. Informacja publiczna i transparency ledger

Program powinien publikować:

- jawne cele, wskaźniki i właścicieli;
- kryteria wyboru projektów i partnerów;
- zagregowane wyniki testów i liczbę projektów zamkniętych;
- beneficjentów wsparcia w zakresie wymaganym prawem;
- deklaracje konfliktów interesów;
- rejestr podstaw ograniczenia dostępu do poszczególnych kategorii, bez ujawniania chronionej treści;
- historię zmian strategii i uzasadnienie decyzji.

Ochrona tajemnicy nie powinna usuwać możliwości ustalenia, kto podjął decyzję, według jakiego kryterium i z jakiego budżetu — o ile prawo nie wymaga ochrony konkretnego elementu.

## 7. IP, escrow, prawo do naprawy i produkcja awaryjna

### 7.1. Macierz praw zamiast ogólnej klauzuli „IP dla państwa”

Każdy projekt powinien rozdzielić:

| Kategoria | Pytanie umowne | Minimalne zabezpieczenie państwa dla elementu krytycznego |
| --- | --- | --- |
| **Background IP** | co każda strona posiadała przed projektem? | identyfikacja załącznikiem i licencja tylko w niezbędnym zakresie |
| **Foreground IP** | kto posiada rezultat finansowanego projektu? | prawo użycia dla celu publicznego, zakres terytorialny i czasowy, reguły komercjalizacji |
| **Improvements** | kto posiada ulepszenia i feedback użytkownika? | prawo dostępu do wersji potrzebnych do utrzymania i interoperacyjności |
| **Kod i modele** | czy państwo dostaje binaria, źródła, wagi, konfigurację, narzędzia czy usługę? | jednoznaczny zakres, wersja, build, zależności, aktualizacje, logi i bezpieczeństwo |
| **Dane techniczne** | jakie rysunki, listy części, instrukcje i wyniki testów są potrzebne? | prawo użycia do odbioru, naprawy, bezpieczeństwa i kwalifikacji zamiennika |
| **Interfejsy** | co musi być znane drugiemu integratorowi? | kontrolowana dokumentacja interfejsu i test zgodności, bez wymogu publicznego ujawnienia |
| **Prawa osób trzecich** | jakie OSS, patenty, chmury, dane i komponenty ograniczają użycie? | pełny wykaz, warunki licencji, plan substytucji i indemnity adekwatne do ryzyka |
| **Naprawa i modyfikacja** | kto może diagnozować, poprawiać i integrować? | licencja i narzędzia dla wskazanych jednostek lub wykonawcy zastępczego |
| **Produkcja awaryjna** | co dokładnie może zostać wyprodukowane, kiedy, przez kogo i gdzie? | licencja warunkowa, trigger, wynagrodzenie, kontrola jakości, eksportu i informacji |
| **Koniec wsparcia** | co dzieje się po EOL, niewypłacalności lub sankcji? | obowiązek wcześniejszego powiadomienia, ostatni zakup, escrow i step-in |

Otwarte interfejsy są czym innym niż publiczny kod źródłowy. Państwo może wymagać interoperacyjności i kontrolowanego dostępu bez publikowania wrażliwej implementacji.

### 7.2. Depozyt, który rzeczywiście działa

Depozyt musi obejmować:

- dokładnie oznaczone wersje kodu, modeli, konfiguracji i dokumentacji;
- manifest zależności, licencji i narzędzi;
- instrukcję odtworzenia oraz kontrolowane sekrety/klucze w odrębnym reżimie;
- cykliczną aktualizację i raport różnic;
- niezależny test odtworzenia bez udziału podstawowego dostawcy;
- zdarzenia wydania: długotrwałe zaprzestanie wsparcia, niewypłacalność, trwała niemożność dostawy, istotne naruszenie po cure period lub inne precyzyjne zdarzenie;
- licencję aktywowaną przy wydaniu;
- listę uprawnionych odbiorców zastępczych;
- zgodność z eksportem, sankcjami i ochroną informacji;
- zasady zwrotu, zakończenia i audytu.

Samo złożenie pliku ZIP u depozytariusza nie jest ciągłością. `[CLM-0915]` `[CLM-0933]`

### 7.3. Produkcja awaryjna — granice

Prawo produkcji awaryjnej powinno być:

- ograniczone do zdefiniowanych elementów i sytuacji;
- uruchamiane przez wskazany organ oraz udokumentowaną decyzję;
- zgodne z istniejącymi licencjami, kontrolą eksportu i prawami osób trzecich;
- odpłatne według określonej metody, chyba że ustawa legalnie stanowi inaczej;
- powiązane z zapewnieniem jakości, odpowiedzialnością i bezpieczeństwem;
- okresowe i wygaszane po ustaniu zdarzenia;
- poddane audytowi.

Jeżeli państwo chce wymusić takie prawa poza dobrowolnym kontraktem, RCL musi odpowiedzieć, czy potrzebna jest szczególna podstawa ustawowa i jakie zabezpieczenia praw majątkowych są wymagane. To pozostaje `UNKNOWN`. `[CLM-0946]`

## 8. Kontrola eksportu, sankcje i end-use

### 8.1. Jedna bramka przed każdym transferem

Właścicielem zgodności powinien być eksporter lub podmiot dokonujący transferu, przy centralnym wsparciu MRiT/MSZ i odpowiednich służb. Karta transakcji musi zawierać:

1. dokładny przedmiot: towar, komponent, kod, model, dokumentacja, technologia, usługa, pośrednictwo lub pomoc techniczna;
2. kwalifikację według aktualnych list i catch-all;
3. stronę, beneficjenta rzeczywistego oraz własność i kontrolę;
4. kraj przeznaczenia, tranzytu, hostingu i zdalnego dostępu;
5. użytkownika końcowego i zamierzone użycie;
6. odbiorców pośrednich, reeksport i ograniczenia dalszego transferu;
7. sankcje UE, krajowe i inne mające zastosowanie;
8. wymagane zezwolenie, organ i warunki;
9. WSK oraz dokumentację end-user/importową;
10. monitoring po transferze, ewidencję i trigger ponownej oceny.

**Stop-rule:** brak klasyfikacji, brak wiarygodnego użytkownika końcowego, nierozwiązana własność/kontrola, sankcja, brak wymaganej zgody lub niedopuszczalne ryzyko dywersji zatrzymują transfer. `[CLM-0934]`

### 8.2. WSK i eksport-by-design

WSK nie powinien być dokumentem przygotowywanym dopiero przed pierwszym wnioskiem. Dla programu oznacza:

- rolę export control w projekcie i przeglądzie zmian;
- klasyfikację w repozytorium produktu;
- kontrolę dostępu według obywatelstwa/jurysdykcji tylko tam, gdzie prawo tego wymaga;
- szkolenie inżynierów i sprzedaży;
- zatwierdzanie demonstracji, konferencji, repozytoriów i zdalnego wsparcia;
- ewidencję wersji technologii przekazanej konkretnemu odbiorcy;
- monitoring warunków licencji i end-use;
- procedurę dobrowolnego wstrzymania przy wątpliwości i eskalacji do organu.

Nie ustalono jeszcze klasyfikacji produktów ani rynków, dlatego deklarowane przychody eksportowe są wyłącznie scenariuszem. `[CLM-0943]`

### 8.3. Sankcje są procesem ciągłym

Screening powinien wystąpić:

- przed dopuszczeniem partnera do danych;
- przed shortlistą i wyborem;
- przed podpisaniem NDA, jeśli już samo ujawnienie informacji może być transferem lub udostępnieniem zasobu;
- przed umową i closingiem;
- przed każdą istotną płatnością, dostawą, aktualizacją lub wsparciem;
- okresowo;
- po zmianie właściciela, kontroli, zarządu, banku, jurysdykcji, produktu albo listy.

Należy badać własność i kontrolę, a nie wyłącznie identyczność nazwy. `[CLM-0919]` `[CLM-0935]`

## 9. AI, autonomia, prawo wojenne i etyka

### 9.1. Scope memo dla każdego zastosowania

Karta AI powinna wskazać:

- zamierzone przeznaczenie i funkcje;
- czy użycie jest wyłącznie wojskowe, obronne lub bezpieczeństwa narodowego;
- czy system będzie oferowany lub używany cywilnie;
- dostawcę, deployera, importera, dystrybutora i użytkownika w rozumieniu właściwego reżimu;
- dane, model, aktualizacje i zależności;
- poziom wpływu na prawa, bezpieczeństwo i decyzje;
- zastosowanie AI Act, RODO lub innych ustaw;
- wymagania oceny zgodności, rejestracji, przejrzystości i monitorowania;
- organ prawny zatwierdzający kwalifikację;
- datę ponownego przeglądu.

Samo dodanie etykiety „defence AI” nie tworzy wyłączenia. `[CLM-0921]` `[CLM-0942]`

Na dzień 21 lipca 2026 r. zasadnicza data rozpoczęcia stosowania większości AI Act — 2 sierpnia 2026 r. — jest bliska, ale każdy dokument wykonawczy powinien mieć automatyczny check aktualnego Dziennika Urzędowego UE przed wydaniem, bo harmonogram i akty wdrożeniowe mogą się zmieniać. `[CLM-0922]`

### 9.2. Responsible Autonomy Assurance — minimum wspólne

Nawet jeśli konkretne wdrożenie jest poza AI Act, program powinien wymagać:

1. **Lawfulness:** wskazanych podstaw prawnych i ograniczeń zastosowania.
2. **Responsibility and accountability:** imiennego właściciela decyzji, systemu i ryzyka.
3. **Explainability and traceability:** wersji modelu, danych, konfiguracji, testów i decyzji w zakresie adekwatnym do ryzyka.
4. **Reliability:** udokumentowanego zakresu testów, ograniczeń i warunków ponownej oceny.
5. **Governability:** możliwości nadzoru, bezpiecznego ograniczenia lub wycofania systemu oraz kontroli zmian.
6. **Bias mitigation:** oceny danych i wyników pod kątem systematycznych błędów, zwłaszcza gdy wpływają na osoby.
7. **Security:** modelowania zagrożeń, kontroli dostępu, integralności łańcucha i zarządzania incydentem.
8. **Human factors:** określenia odpowiedzialności, kompetencji i ograniczeń użytkownika; sama obecność człowieka nie dowodzi skutecznego nadzoru.
9. **Independent challenge:** red-team niezależny od dostawcy i zespołu, który otrzymuje premię za wdrożenie.
10. **Change control:** ponownej kwalifikacji po zmianie modelu, danych, funkcji, środowiska, dostawcy lub celu.

To operacjonalizuje zasady NATO bez udawania, że strategia NATO jest ustawą. `[CLM-0923]` `[CLM-0936]`

### 9.3. Art. 36 i prawo konfliktów zbrojnych

Dla nowej broni, środka lub metody walki należy uruchomić formalny, niezależny przegląd prawny podczas badań, rozwoju, pozyskania lub przyjęcia. `[CLM-0924]`

Governance powinno obejmować:

- trigger przeglądu oraz organ odpowiedzialny;
- dostęp przeglądającego do niezbędnych informacji w odpowiednim reżimie;
- oddzielenie od decyzji handlowej i oceny dostawcy;
- dokumentację norm i założeń;
- wynik: dopuszczalne, dopuszczalne pod warunkami, wymagające zmiany albo niedopuszczalne;
- ponowny przegląd po materialnej zmianie;
- kontrolowany sposób przechowywania wyniku i jawny jedynie opis procesu, jeśli treść jest chroniona.

**Stop-rule:** brak wymaganego przeglądu blokuje przyjęcie lub użycie; pozytywny wynik nie jest zgodą na każde przyszłe użycie w dowolnym kontekście. `[CLM-0937]`

### 9.4. Granice etyki

Rada etyczna powinna:

- identyfikować szkody, konflikty wartości i grupy dotknięte;
- sprawdzać jakość procesu, dowodu i mechanizmów odpowiedzialności;
- publikować jawne zasady, skład, konflikty interesów i zdania odrębne;
- kierować pytanie prawne do prawnika lub właściwego organu;
- nie zatwierdzać sama użycia operacyjnego;
- nie nadawać marketingowego znaku „ethical AI”.

**Ethics washing** zachodzi, gdy pozytywna opinia niewładnego ciała zastępuje zgodność, test, audyt lub odpowiedzialną decyzję. Program musi temu przeciwdziałać.

## 10. SOOŚ, konsultacje i jawność procesu

### 10.1. Cztery różne procesy

Nie należy mieszać:

1. **konsultacji dokumentu polityki rozwoju** z partnerami, samorządem i opinią publiczną;
2. **rządowego procesu legislacyjnego** z OSR, uzgodnieniami, opiniowaniem i raportem konsultacji;
3. **strategicznej oceny oddziaływania na środowisko** z prognozą, opiniami organów i udziałem społeczeństwa;
4. **wstępnych konsultacji rynkowych/zamówienia** z wykonawcami, które nie są konsultacją polityki publicznej.

Każdy ma inny cel i konflikt interesów. Dostawca może dostarczyć wiedzę techniczną, ale nie powinien samodzielnie ustalać celu publicznego ani reguł własnego wyboru.

### 10.2. Screening SOOŚ od D+0

Program obejmuje cywilne zastosowania, fabryki, centra danych, energetykę, regiony, poligony i infrastrukturę. Dlatego nie wolno zakładać wyłączenia dla dokumentu przygotowywanego „wyłącznie dla obrony”. `[CLM-0920]`

Sekwencja:

1. zamrożenie roboczego zakresu i listy rodzajów przedsięwzięć;
2. nota screeningowa do właściwych organów;
3. formalne uzgodnienie potrzeby i zakresu prognozy albo podstawy odstąpienia;
4. jeśli ocena jest wymagana — prognoza alternatyw, wpływów i środków ograniczających;
5. udział społeczeństwa z wersją bez chronionych szczegółów;
6. pisemne podsumowanie sposobu uwzględnienia opinii i uwag;
7. monitoring skutków.

**Stop-rule:** brak rozstrzygnięcia przy wymaganej ocenie blokuje przyjęcie strategii. `[CLM-0938]` `[CLM-0944]`

### 10.3. Jak konsultować bez ujawniania chronionych informacji

- konsultować cele, warianty, kryteria, koszty alternatywne, skutki regionalne i środowiskowe;
- agregować lub redagować tylko elementy mające podstawę ochrony;
- prowadzić chronione warsztaty dla uprawnionych uczestników, ale nie przedstawiać ich jako substytutu konsultacji jawnej;
- publikować raport uwag, odpowiedź i podstawę odrzucenia;
- prowadzić wykaz materiałów wyłączonych z publikacji i podstaw prawnych;
- oddzielić potrzebę ochrony od chęci uniknięcia krytyki.

## 11. JV z Ukrainą i innymi partnerami — due diligence

### 11.1. Zasada neutralności dostawcy

Doświadczenie ukraińskie jest strategicznie cenne, ale żadna firma, grupa kapitałowa ani osoba nie może zostać „preferowanym partnerem państwa” wyłącznie na podstawie narracji, relacji politycznej lub demonstracji. Program powinien porównywać co najmniej:

- realny wkład technologiczny i prawa do niego;
- beneficjenta rzeczywistego, kontrolę i finansowanie;
- referencje i możliwość ich legalnej weryfikacji;
- bezpieczeństwo informacji i cyber;
- zdolność utrzymania, jakości i eksportu;
- konflikty interesów;
- sankcje, spory, zobowiązania i ryzyka ciągłości;
- alternatywnych partnerów lub plan wyjścia.

### 11.2. Bramka transakcyjna

| Moduł | Pytanie | Dowód minimalny | Stop-rule |
| --- | --- | --- | --- |
| **Tożsamość i UBO** | kto posiada i kontroluje strony, bezpośrednio i pośrednio? | CRBR/rejestry zagraniczne, dokumenty korporacyjne, cap table, umowy kontroli | nieustalony UBO lub ukryta kontrola |
| **Sankcje i reputacja** | czy strona, właściciel, kontrolujący, bank lub poddostawca jest objęty ograniczeniem? | screening aktualnych aktów i list, analiza ownership/control | sankcja albo nierozwiązana kontrola |
| **FDI** | czy transakcja dotyczy podmiotu chronionego lub wymaga zgłoszenia? | memo na podstawie struktury i progów | brak wymaganej decyzji przed closingiem `[CLM-0925]` |
| **Koncentracja** | czy JV jest pełnofunkcyjne i czy progi są spełnione? | analiza obrotów, stron, rynku i wyłączeń | brak wymaganej zgody `[CLM-0927]` |
| **FSR** | czy wkłady z państw trzecich uruchamiają obowiązek zgłoszenia lub ryzyko call-in? | trzyletni rejestr foreign financial contributions | brak kompletnego rejestru przy obowiązku |
| **Pomoc państwa** | czy finansowanie daje selektywną korzyść na warunkach innych niż rynkowe? | podstawa pomocy, test inwestora rynkowego lub wyłączenie/notyfikacja | brak legalnej podstawy przed przyrzeczeniem środków |
| **IP** | kto wnosi background, kto posiada wynik i co dzieje się po wyjściu? | schedule IP, freedom-to-operate, licencje, escrow i exit | brak prawa do użycia wniesionego kluczowego IP |
| **Eksport/end-use** | czy transfer technologii i przyszły eksport są dopuszczalne? | klasyfikacja, zezwolenia, end-user, warunki re-eksportu | brak zezwolenia lub niedopuszczalne ryzyko dywersji |
| **Informacje i cyber** | czy strony mogą bezpiecznie przetwarzać dany poziom informacji? | audyt, uprawnienia, certyfikaty, architektura dostępu | brak zdolności dla planowanego poziomu |
| **Governance** | kto kontroluje budżet, zmiany, eksport, bezpieczeństwo i IP? | umowa udziałowców, reserved matters, deadlock, audit | jedna strona może jednostronnie przenieść kluczowe akty lub technologię |
| **Ciągłość** | co po zmianie rządu, wojnie, sankcji, niewypłacalności lub przejęciu? | BCP, step-in, alternatywa, rozwiązanie i post-closing covenants | brak realistycznego wyjścia lub substytutu |

CRBR jest punktem startowym, nie dowodem końcowym. `[CLM-0926]` `[CLM-0931]` `[CLM-0939]`

### 11.3. Conditions precedent przed closingiem

Term sheet i umowa powinny uzależniać closing co najmniej od:

- wymaganych zgód korporacyjnych;
- rozstrzygnięcia FDI, koncentracji, FSR i pomocy państwa;
- licencji eksportowych i zgód na transfer, jeśli są potrzebne;
- potwierdzenia praw do wniesionego IP;
- pozytywnego screeningu UBO, sankcji i konfliktów interesów;
- uzgodnienia reżimu informacji oraz prawa audytu;
- zatwierdzenia planu danych, cyber i ciągłości;
- braku material adverse change w określonym zakresie.

Nie ustalono dziś, które transakcje przekroczą progi lub wymagają zgłoszeń, bo brak term sheetów i danych stron. `[CLM-0945]`

## 12. Pięć decyzji dla Premiera i Prezydenta

| Nr | Decyzja i adresat | Termin | Odpowiedzialny właściciel | Rezultat | Bramka / stop-rule | Zależności | Główne ryzyko |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **D1** | **Premier:** zlecić formalną mapę kompetencji i wybór instrumentu; **Prezydent/BBN:** wskazać wymagane produkty bezpieczeństwa bez wchodzenia w wykonawcze kompetencje RM | **D+30** | KPRM + RCL + MFiPR, konsultacja MON/MSZ/MF | macierz działania → organ → podstawa → instrument → finansowanie → konsultacje → jawność; rekomendacja strategia/polityka/program/ustawa | działanie bez podstawy, właściciela albo finansowania nie przechodzi do zobowiązania `[CLM-0929]` | zamknięty zakres programu i mapa istniejących strategii | spór resortowy i wybór nazwy przed treścią |
| **D2** | **Premier/RM:** zatwierdzić trzy wzorce szybkiego pozyskania i zakazać automatycznego kopiowania partnerstwa innowacyjnego do obronności | **D+100** | MON/AU + UZP + RCL + MRiT/MFiPR + UOKiK | karty kwalifikacji, wzorce fazowego kontraktu, IP, bezpieczeństwa dostaw, testów, exit i audytu | nierozstrzygnięta kwalifikacja, nieuzasadniony tryb, brak konkurencji lub konflikt interesów blokują wszczęcie `[CLM-0930]` | klasy problemów A03, krytyczność A04/A06, finansowanie A07 | legalizm spowalniający pilotaż albo „pilotaż” użyty do ominięcia konkurencji |
| **D3** | **Premier:** uruchomić projekt dwóch obiegów danych — jawnego i chronionego — bez przenoszenia informacji niejawnych do repozytorium publicznego | **D+90** | KPRM + MC + MON + ABW/SKW + UODO + właściciele danych | katalog zbiorów, karty podstaw, strefy P0–P3, DPIA gdzie wymagana, architektura akredytacji, retencji, audytu i incydentu | brak podstawy, zgody właściciela, kwalifikacji eksportowej lub właściwego środowiska blokuje ingest/udostępnienie `[CLM-0931]` | inwentaryzacja A05, klasy informacji, środki i infrastruktura | wyciek, nadmierna klasyfikacja, centralizacja bez odpowiedzialności |
| **D4** | **Premier/RM:** ustanowić wspólną bramkę JV i eksportu przed wyborem pięciu pilotaży; **Prezydent/BBN:** otrzymywać syntetyczny rejestr ryzyk partnerstw strategicznych | **standard D+60; przed każdym NDA/term sheetem/transferem** | MRiT + MSZ + MON + ABW/SKW + UOKiK + PFR/BGK + właściwa spółka | single transaction file: UBO, sankcje, FDI, koncentracja, FSR, pomoc, IP, eksport, end-use, cyber, ciągłość i COI | nierozwiązany UBO/kontrola, sankcja, brak zgody, brak praw do IP albo niedopuszczalny transfer blokują podpisanie/closing `[CLM-0939]` | dane partnera, term sheet, klasyfikacja technologii, źródło finansowania | opóźnienie transakcji, efekt odstraszający, pozorne due diligence pod presją polityczną |
| **D5** | **Premier i Prezydent:** przyjąć wspólną zasadę, że żaden system autonomiczny nie otrzymuje politycznego poparcia jako „odpowiedzialny” bez assurance, a system objęty art. 36 nie przechodzi do przyjęcia bez niezależnego przeglądu prawnego | **D+120** | MON + właściwe organy AI/data + BBN w roli strategicznego challenge + niezależny red-team | Responsible Autonomy Assurance, scope memo AI Act, rejestr odpowiedzialności i zmian, procedura art. 36 | brak właściciela, dowodu testowego, kontroli zmian lub wymaganego legal review blokuje akceptację `[CLM-0936]` `[CLM-0937]` | taksonomia A04, data/model governance A05, doktryna A01 | biurokratyczny checkbox, utajnienie krytyki, ethics washing |

## 13. Plan prac A09 na pierwsze 100 dni

| Termin | Zadanie | Właściciel | Produkt | Bramka |
| --- | --- | --- | --- | --- |
| D+0–15 | freeze zakresu strategii i mapa istniejących dokumentów | KPRM/RCL/MFiPR | rejestr instrumentów i kolizji | brak zakresu = brak rekomendacji instrumentu |
| D+0–30 | macierz kompetencji i pytań ustawowych | RCL + resorty | legal authority matrix | brak organu/podstawy = `UNKNOWN` |
| D+0–30 | screening SOOŚ i konsultacji | właściciel dokumentu + właściwe organy | nota kwalifikacyjna i harmonogram | brak stanowiska = nie zamykać kalendarza przyjęcia |
| D+15–45 | standard karty zamówienia | AU/UZP/RCL | trzy legal pathways | niezatwierdzony wzorzec = brak szybkiego naboru |
| D+15–60 | IP/escrow/emergency rights playbook | AU + Prokuratoria/właściwe legal + przemysł i MŚP | klauzule stopniowane K1–K4 | klauzula bez wyceny i praw osób trzecich nie przechodzi |
| D+15–60 | transaction gate JV/eksport | MRiT/MSZ/MON/UOKiK/PFR/BGK | checklista i conditions precedent | brak UBO/licencji/zgody = stop |
| D+20–75 | data inventory i strefy P0–P3 | KPRM/MC/MON/ABW/SKW/UODO | katalog zbiorów i wzorce kart | brak podstawy/retencji = brak ingestu |
| D+30–90 | konsultacje wzorców z MŚP, uczelniami i zamawiającymi | KPRM/RCL | raport zmian i COI | dostawca nie zatwierdza własnej reguły |
| D+45–100 | Responsible Autonomy Assurance i art. 36 trigger | MON + właściwe organy + red-team | standard bramek i zmiany | brak niezależności oceny = fail |
| D+75–100 | red-team całej architektury | A12/niezależny zespół | P0/P1/P2 i pass/fail | P0 nierozwiązane = brak publikacji |

## 14. Pytania prawne wymagające formalnej odpowiedzi

Poniższe kwestie należy zapisać jako pytania, nie założenia:

1. **RCL/MFiPR:** czy dokument główny jest strategią rozwoju, polityką publiczną czy innym dokumentem, oraz jaki maksymalny horyzont i tryb przyjęcia mają zastosowanie? `[CLM-0940]`
2. **RCL/MFiPR:** z którymi obowiązującymi strategiami dokument musi być zgodny, które aktualizuje i które programy może uruchomić?
3. **RCL/KPRM:** jaki dokładnie status ma mieć „minister–pełnomocnik” i jakie decyzje pozostają wyłącznie u ministrów? `[CLM-0904]`
4. **RCL:** które planowane obowiązki wobec firm, uczelni, szkół i samorządu wymagają ustawy?
5. **RCL/MON/UZP:** jakie kryteria kwalifikują poszczególne projekty do zamówień obronnych i bezpieczeństwa, cywilnego PZP, B+R lub wyłączeń?
6. **RCL/MON:** czy i w jakim zakresie dla konkretnego projektu może być zastosowany art. 346 TFUE, po analizie niezbędności i zakresu? `[CLM-0909]`
7. **MF/UOKiK/MRiT:** jaka podstawa pomocy państwa lub warunki rynkowe obejmą dotacje, gwarancje, inwestycje i preferencyjne finansowanie?
8. **KPRM/MON/ABW/SKW/UODO:** jakie są kategorie zbiorów, podstawy prawne, administratorzy, retencja i środowiska planowanej przestrzeni danych? `[CLM-0941]`
9. **ABW/SKW:** które elementy wymagają informacji niejawnych, świadectw bezpieczeństwa przemysłowego i akredytacji systemu?
10. **UODO/właściwy organ:** czy każdy zbiór podlega RODO, reżimowi organów ścigania, przepisom sektorowym czy jest poza prawem UE ze względu na bezpieczeństwo narodowe?
11. **AU/Prokuratoria/właściwe legal:** jaki minimalny pakiet praw jest proporcjonalny dla klas krytyczności, a kiedy wymaganie pełnego kodu lub dokumentacji ogranicza konkurencję?
12. **RCL:** czy prawo produkcji awaryjnej poza kontraktem wymaga ustawy i jak chronić prawa majątkowe oraz tajemnicę? `[CLM-0946]`
13. **MRiT/MSZ:** jaka jest klasyfikacja towarów, oprogramowania, modeli, technologii i usług każdego pilotażu? `[CLM-0943]`
14. **MRiT/MSZ:** jakie warunki end-use, re-eksportu i post-shipment monitoring są legalnie i praktycznie dostępne dla danego odbiorcy?
15. **właściwy organ AI/RCL:** które use case’y podlegają AI Act, a które są wyłącznie wojskowe, obronne lub bezpieczeństwa narodowego? `[CLM-0942]`
16. **MON:** jaki organ prowadzi polski przegląd art. 36, jakie ma zasady niezależności i jakie zmiany uruchamiają re-review?
17. **właściciel strategii/GDOŚ i właściwe organy:** czy wymagana jest SOOŚ i jaki jest zakres prognozy? `[CLM-0944]`
18. **UOKiK/MRiT/KE:** czy planowane JV lub transakcje wymagają kontroli koncentracji, FDI lub FSR? `[CLM-0945]`
19. **MSZ/RCL:** czy planowany dokument z Ukrainą jest niewiążącym MOU, czy umową międzynarodową wymagającą właściwej procedury? `[CLM-0905]`
20. **RCL/MF:** czy finansowanie wieloletnie i zobowiązania warunkowe wymagają dodatkowych podstaw ustawowych?

## 15. Luki danych i plan ich pozyskania

| Luka | Status | Właściciel pozyskania | Metoda | Termin | Wpływ braku |
| --- | --- | --- | --- | --- | --- |
| ostateczny zakres i horyzont dokumentu | `UNKNOWN` `[CLM-0940]` | KPRM/MFiPR/RCL | warsztat zakresu + mapa strategii | D+15 | nie można wybrać instrumentu ani SOOŚ |
| katalog obowiązków wobec podmiotów zewnętrznych | `UNKNOWN` `[CLM-0946]` | każdy resort + RCL | action-by-action legal inventory | D+30 | ryzyko uchwały przekraczającej skutek wewnętrzny |
| katalog zbiorów i podstaw danych | `UNKNOWN` `[CLM-0941]` | A05 + właściciele + legal | dataset cards, DPIA screening, classification review | D+45 | brak legalnej architektury data roomu |
| klasyfikacja zamówień pilotów | brak | A03/A04 + AU/UZP/legal | procurement classification cards | przed naborem | ryzyko niewłaściwego trybu |
| background/foreground IP partnerów | brak | strony + niezależny IP counsel | schedule praw, rejestry, FTO, umowy twórców | przed term sheetem | niemożność wykorzystania rezultatu |
| klasyfikacja eksportowa i rynki | `UNKNOWN` `[CLM-0943]` | MRiT/MSZ + eksporter | product/technology classification, end-use dossier | przed transferem | brak podstaw prognozy eksportu |
| scope AI Act | `UNKNOWN` `[CLM-0942]` | A05 + właściwy legal | use-case cards i role mapping | przed pilotażem | brak właściwego compliance i assurance |
| SOOŚ | `UNKNOWN` `[CLM-0944]` | właściciel strategii | screening i uzgodnienie organów | D+30 | ryzyko wadliwej procedury przyjęcia |
| JV thresholds/approvals | `UNKNOWN` `[CLM-0945]` | transakcja + UOKiK/MRiT/legal | term sheet, obroty, wkłady zagraniczne, control map | przed podpisaniem | gun-jumping lub brak zgody |
| procedura art. 36 | brak jawnego potwierdzenia operacyjnego | MON | formalna odpowiedź i kontrolowany SOP | D+90 | brak bramki dla nowych środków/metod |

Dwa nieudane, udokumentowane podejścia do uzyskania dowodu kończą się wpisem `UNKNOWN`, nie domysłem.

## 16. Ryzyka, konflikty interesów i argumenty przeciw rekomendacjom

### 16.1. Główne ryzyka

| Ryzyko | Mechanizm szkody | Wczesny sygnał | Odpowiedź |
| --- | --- | --- | --- |
| **Specustawa przed diagnozą** | nadmiar kompetencji, kolizje, szybka dezaktualizacja | projekt ustawy powstaje przed action inventory | gap analysis i sunset/review dla nowych instrumentów |
| **Paraliż proceduralny** | każda mała decyzja trafia do komitetu centralnego | rosnący czas oczekiwania i brak delegated authority | progi ryzyka, standardowe wzorce i decyzje delegowane |
| **Pilotaż jako obejście zamówienia** | powtarzane małe partie bez konkurencji i planu skali | ten sam dostawca, to samo uzasadnienie, brak exit | limit etapów, ponowna kwalifikacja i audyt ex post |
| **Nadmierne IP dla państwa** | MŚP nie uczestniczą, rośnie cena, partner nie wnosi technologii | szeroka klauzula „wszystkie prawa” bez krytyczności | macierz praw, wynagrodzenie, background pozostaje właściciela |
| **Pozorny escrow** | kod nie buduje się, brak zależności lub licencji | brak niezależnego restore test | test i warunkowa licencja; brak testu = brak zaliczenia ciągłości |
| **Nadmierna klasyfikacja** | mniejsza konkurencja, brak kontroli, wolniejsza współpraca | większość dokumentów w strefie chronionej bez podstaw | classification challenge i jawne agregaty |
| **Niedostateczna ochrona** | wyciek operacyjny, handlowy lub osobowy | kopiowanie do maila/repozytorium, współdzielone konta | strefy P0–P3, logi, DLP, szkolenie i incydent response |
| **Eksport po fakcie** | niedozwolony transfer kodu/dokumentacji | inżynier udostępnia repo przed klasyfikacją | export-by-design i zatwierdzanie dostępu |
| **Sanctions checkbox** | ekranowanie tylko nazwy, pominięcie kontroli | brak cap table i okresowego rescreeningu | ownership/control review i event-driven monitoring |
| **AI exemption creep** | cywilne wdrożenie bez zgodności, bo produkt nazwano obronnym | ten sam model trafia do cywilnego rynku | scope memo per use case i change trigger |
| **Ethics washing** | rada etyczna zastępuje prawo i test | marketing używa opinii jako certyfikatu | jawny mandat, brak uprawnienia do legal approval, zdania odrębne |
| **JV pod presją polityczną** | pominięte UBO/IP/sankcje, partner staje się single point of failure | term sheet przed due diligence | conditions precedent i niezależny deal team |
| **SOOŚ za późno** | opóźnienie lub wada procedury strategii | projekt gotowy przed screeningiem | równoległy screening od D+0 |
| **Konflikt Prezydent–RM** | rozmyta odpowiedzialność wykonawcza | dwa konkurencyjne biura wydają zalecenia operacyjne | rozdzielenie strategicznego challenge od wykonania |

### 16.2. Argumenty przeciw proponowanemu modelowi

**„Tyle bramek zabije szybkość.”** To realne ryzyko. Odpowiedzią nie jest rezygnacja z bramek, lecz standardowe karty, decyzje równoległe, terminy SLA, progi ryzyka i automatyczna eskalacja. Bramka bez właściciela i terminu staje się kolejką; bramka z jednym ownerem skraca spór.

**„Państwo nie powinno żądać kodu i praw, bo odstraszy najlepszych.”** Zasadne. Dlatego wymagania są stopniowane krytycznością. Dla COTS wystarczą interfejsy, serwis i substytucja; escrow i step-in są dla elementów, których brak zatrzymuje zdolność państwa. Background IP pozostaje u właściciela, chyba że dobrowolna, odpłatna umowa stanowi inaczej. `[CLM-0932]`

**„Jawne konsultacje ujawnią wrażliwe potrzeby.”** Nie trzeba publikować wolumenów, lokalizacji ani parametrów. Konsultować można cele, warianty, kryteria, wpływy, finansowanie i governance. Chroniony aneks nie może jednak być pretekstem do ukrycia całej polityki.

**„W czasie kryzysu liczy się rezultat, nie procedura.”** Właśnie wtedy brak licencji, dokumentacji, zgody eksportowej albo właściwego organu może uniemożliwić rezultat. Gotowość prawna jest częścią gotowości produkcyjnej.

**„Współpraca z Ukrainą wymaga zaufania, nie biurokracji.”** Due diligence chroni obie strony: precyzuje wkład, IP, eksport i ciągłość. Bez niego spór po sukcesie produktu jest bardziej prawdopodobny niż przed podpisaniem.

### 16.3. Konflikty interesów

Obowiązkowe ujawnienie powinno objąć:

- udziały, opcje, wynagrodzenie, granty i kontrakty osoby lub jej najbliższych interesów ekonomicznych;
- role doradcze, naukowe i lobbingowe;
- zatrudnienie w ocenianej firmie lub organie w określonym okresie;
- prawa do patentu, kodu, danych lub prowizji eksportowej;
- udział w definiowaniu potrzeby, pisaniu wymagań, wyborze i odbiorze;
- finansowanie organizacji publikującej opinię.

Reguła minimalna: dostawca może opisać technologię, ale nie może samodzielnie zdefiniować potrzeby, wybrać trybu, napisać kryteriów i zweryfikować własnego wyniku. Recusal powinien być odnotowany w rejestrze decyzji.

## 17. Kryteria gotowości artefaktów

### 17.1. Strategia jawna — `pass` tylko gdy

- instrument i podstawa przyjęcia są rozstrzygnięte;
- cele nie tworzą nielegalnych obietnic lub obowiązków;
- wskazano właścicieli i finansowanie albo jawnie oznaczono lukę;
- przeprowadzono wymagane konsultacje i SOOŚ albo formalnie uzasadniono brak;
- dane i twierdzenia mają źródła, status i datę;
- część chroniona została oddzielona, nie „wycięta bez śladu”;
- A12 nie ma nierozwiązanego P0.

### 17.2. Program wykonawczy — `pass` tylko gdy

- każde działanie ma ownera, instrument, koszt/scenariusz i miernik;
- obowiązki zewnętrzne mają właściwą podstawę;
- projekty mają stop-rule i procedurę zamknięcia;
- finansowanie przeszło pomoc państwa/FSR i reguły źródła;
- prawa do danych, IP, utrzymania i ewaluacji są wykonalne;
- publiczny dashboard nie ujawnia chronionych danych.

### 17.3. Pilotaż/JV — `pass` tylko gdy

- karta zamówienia lub transakcji jest kompletna;
- UBO, sankcje, FDI, konkurencja i eksport są rozstrzygnięte;
- strony rzeczywiście posiadają wnoszone IP;
- zdefiniowano test, dowód, odpowiedzialność, exit i ciągłość;
- dostęp do danych jest legalny, minimalny i audytowalny;
- wymagany AI/legal/art. 36 review ma właściciela i termin.

## 18. Czego ten dokument nie rozstrzyga

Memorandum nie:

- kwalifikuje konkretnego zamówienia ani odstępstwa;
- stwierdza, że określony system jest zgodny z AI Act, IHL lub zasadami NATO;
- ocenia legalności konkretnej broni, środka lub metody;
- klasyfikuje towaru lub technologii do kontroli eksportu;
- zatwierdza partnera, JV, finansowania lub pomocy państwa;
- wskazuje, które dane są informacją niejawną;
- tworzy prawa do IP ani produkcji awaryjnej;
- zastępuje opinii RCL, Prokuratorii, właściwego organu, zamawiającego lub niezależnego counsel;
- zawiera informacji niejawnych, tajemnicy przedsiębiorstwa ani danych osobowych.

## 19. Konkluzja

Najważniejszym produktem A09 nie jest „specustawa o dronach”, lecz **architektura rozdzielająca politykę, prawo, kontrakt, dane chronione i odpowiedzialność**. Państwo powinno móc działać szybko, lecz każda szybka ścieżka musi z góry wiedzieć:

> kto ma kompetencję → jaki instrument stosuje → jakie dane może zobaczyć → jak wybiera wykonawcę → jakie prawa kupuje → co blokuje transfer → kto odpowiada → kiedy projekt jest zamykany.

Jeżeli któregokolwiek z tych pól brakuje, wpisujemy `UNKNOWN` i kierujemy pytanie do właściwego organu. Nie zastępujemy podstawy prawnej uchwałą, licencji depozytem kodu, zezwolenia eksportowego NDA, testu opinią etyczną ani due diligence politycznym poparciem.

To rozdzielenie pozwala przygotować różne formy dla różnych odbiorców bez sprzeczności: Prezydent otrzymuje strategiczne ryzyka i decyzje, Premier — delivery book i bramki międzyresortowe, minister — program i akty, zamawiający — playbook, forum gospodarcze — jawny deck, a region — własną kartę wdrożeniową. Wszystkie wersje korzystają z jednej księgi twierdzeń, lecz żadna nie miesza warstwy jawnej z chronioną.
