# A12 — audyt kluczowych twierdzen materialu inicjujacego

**Stan wiedzy:** 21 lipca 2026 r.  
**Zakres:** KAI–Fire Point, SAFE, Brave1, umowa Polska–Ukraina, BraveTech EU, Brave1 Dataroom, polska Polityka AI i Gaia/Piast, zasady NATO AI, program MRiT oraz Readiness Roadmap 2030.  
**Ocena:** **wymaga korekt przed wykorzystaniem w dokumencie decyzyjnym**.

## 1. Metoda i granice

Audyt objal tylko twierdzenia wskazane w zleceniu. Kazde rozbito na sprawdzalna jednostke i porownano z aktualnym zrodlem pierwotnym instytucji odpowiedzialnej. Status `verified` oznacza, ze zrodlo wspiera dokladnie sformulowane twierdzenie. `disputed` oznacza konflikt, nieaktualna przeslanke albo nadmiernie mocne sformulowanie. `unverified` oznacza, ze dostepne zrodlo nie pozwala potwierdzic calej tresci.

Komunikat instytucji potwierdza, co dana instytucja oficjalnie deklaruje. Nie jest automatycznie dowodem wykonania budzetu, rzeczywistej wyplaty, skutecznosci programu ani warunkow prawnych niewidocznych na stronie. Audyt nie ocenial zasadnosci nowych rekomendacji strategicznych i nie korzysta z informacji niejawnych.

## 2. Najwazniejsze ustalenia red-team

1. **P1 — BraveTech EU:** Polska jest juz wymieniona przez EDA jako panstwo uczestniczace. Przeslanka rekomendacji „natychmiast wejsc” jest nieaktualna (`CLM-1214`, `CLM-1215`).
2. **P1 — SAFE:** kwota 43,7 mld EUR, pozycja Polski i okres 2026–2030 sa potwierdzone, ale jest to wieloletnia pozyczka. Material nie moze utozsamiac podpisanej umowy i przyznanego finansowania z wyplata calej kwoty (`CLM-1207`, `CLM-1208`).
3. **P2 — KAI:** strona programu podaje 4 lata, a formalna oferta rekrutacyjna 3 lata i 10 miesiecy. Jest to wewnetrzna niespojnosc zrodel KAI (`CLM-1201`).
4. **P2 — Brave1:** oficjalny licznik wskazuje 2500 firm, nie „ponad 2500”; wskazuje natomiast 5000+ produktow (`CLM-1210`, `CLM-1211`).
5. Deklarowane przez KAI pelne finansowanie, 800 EUR miesiecznie i praktyka od drugiego roku sa widoczne na oficjalnej stronie, lecz bez publicznego regulaminu lub wzoru umowy audyt potwierdza tylko tresc deklaracji (`CLM-1202`–`CLM-1204`).
6. Okreslenia „elitarny” i „pilotaz” nie wynikaja z katalogu KAI. Liczba 30 dowodzi malej pojemnosci licencyjnej, nie statusu programu ani faktycznej liczby studentow (`CLM-1205`, `CLM-1206`).
7. Deklaracja 89% dla polskiego przemyslu i gospodarki jest potwierdzona jako plan KPRM, ale nie jako zakonczony wynik programu (`CLM-1209`).
8. Umowa Polska–Ukraina wprost obejmuje lokalizacje produkcji, lancuchy dostaw, wspolna produkcje i IP, lecz nie tworzy konkretnego JV (`CLM-1212`).
9. Brave1 Dataroom, elementy polskiej Polityki AI, zasady NATO, budzet MRiT i dwie inicjatywy Readiness Roadmap sa potwierdzone w aktualnych zrodlach oficjalnych (`CLM-1216`–`CLM-1222`).

## 3. Macierz weryfikacji

| Obszar | Status | Co dokladnie wspiera zrodlo | Ograniczenie lub blad materialu |
|---|---|---|---|
| KAI — czas programu | `disputed` | Strona programu: 4 lata; oferta 2026: 3 lata i 10 miesiecy. | Nie ma jednej zgodnej wartosci w dwoch oficjalnych stronach KAI. |
| KAI — finansowanie | `verified` | KAI deklaruje pokrycie 100% kosztow nauki przez Fire Point. | Brak publicznego regulaminu lub umowy opisujacej warunki. |
| KAI — stypendium | `verified` | KAI deklaruje 800 EUR miesiecznie. | Zrodlo nie podaje kryteriow utrzymania ani opodatkowania swiadczenia. |
| KAI — praktyka | `verified` | KAI deklaruje praktyke lub prace w zespole Fire Point od drugiego roku. | Audyt nie sprawdza wykonania programu. |
| KAI — 30 miejsc | `verified` | Oferta 2026 pokazuje pojemnosc licencyjna 30. | Nie jest to liczba przyjetych ani zapisanych. |
| „Elitarny pilotaz” | `unverified` | Liczba 30 wspiera jedynie mala skale. | KAI nie uzywa okreslen „elitarny” ani „pilotaz”. |
| SAFE — 43,7 mld EUR | `verified` po korekcie statusu | Umowe pozyczki podpisano 8 maja 2026 r.; Polska jest najwiekszym beneficjentem, a perspektywa obejmuje lata 2026–2030. | „Otrzymala” nie moze oznaczac, ze cala kwota zostala juz wyplacona. |
| SAFE — 89% | `verified` jako plan | KPRM deklaruje, ze 89% funduszy lub zamowien ma trafic do polskiego przemyslu i gospodarki. | Nie jest to jeszcze zmierzony udzial wykonania. |
| Brave1 — skala | `disputed` w pierwotnym brzmieniu | Licznik: 2500 firm, 5000+ produktow; 500+ UAV, 300+ EW/SIGINT, 200+ AI. | Zrodlo nie wspiera „ponad 2500 firm”; dane sa dynamiczne i samoopisowe. |
| Umowa Polska–Ukraina | `verified` | Punkty 4, 7 i 9 sekcji przemyslowej obejmuja lancuchy produkcyjne, lokalizacje Polska/Ukraina, wspolna produkcje i ochrone IP. | Sa to ramy wspolpracy, nie dowod utworzenia konkretnej spolki. |
| BraveTech EU — budzet i cel | `verified` | EDA podaje 100 mln EUR lacznego budzetu, wspolna inicjatywe UE–Ukraina i wykorzystanie doswiadczen operacyjnych. | Druga faza powierzona EDA ma wartosc 35 mln EUR; nie nalezy przypisywac EDA calego budzetu. |
| BraveTech EU — Polska | `disputed` dla wezwania do wejscia | EDA wymienia Polske wsrod uczestniczacych panstw. | Przeslanka braku uczestnictwa jest nieaktualna. |
| Brave1 Dataroom | `verified` | Uruchomiono bezpieczne srodowisko z Palantir do treningu i testow AI na danych pola walki; dostep wymaga procedur bezpieczenstwa. | Komunikat projektu nie jest niezalezna ewaluacja jego wynikow. |
| Polityka AI — Piast, Gaia, PLGrid | `verified` | Strona 29 wymienia obie Fabryki AI, vouchery obliczeniowe w PLGrid i piaskownice regulacyjne. | Dokument opisuje plan dzialan, nie pelne wykonanie. |
| Obronny stos danych i modeli | `verified` jako wniosek o zakresie dokumentu | Polityka AI opisuje ekosystem ogolny i odsyla do osobnej strategii MON. | Nie wynika z tego, ze obronny stos nie istnieje w innych, w tym niejawnych, dokumentach. |
| Gaia AI Factory | `verified` | Projekt oficjalnie ruszyl w maju 2026 r.; zaklada integracje z PLGrid i wspolprace z Piast oraz LUMI. | „Projekt ruszyl” nie oznacza pelnej gotowosci docelowej infrastruktury. |
| NATO Responsible AI | `verified` | NATO wymienia szesc Principles of Responsible Use odpowiadajacych liscie w briefie. | W polskim tekscie nalezy zachowac znaczenie „governability” jako sterowalnosci lub mozliwosci nadzoru. |
| MRiT dual-use | `verified` | Program trwa w latach 2025–2029, a zakladany budzet wynosi 22 mln PLN. | To budzet zakladany, nie wykonanie. |
| Readiness Roadmap 2030 | `verified` | European Drone Defence Initiative i Eastern Flank Watch sa dwiema z czterech inicjatyw flagowych. | Mapa zawiera kamienie milowe; samo wpisanie inicjatywy nie dowodzi osiagniecia funkcjonalnosci. |

## 4. Rejestr zrodel uzytych w audycie

- `SRC-1201` — [KAI: FirePoint](https://pk.kai.edu.ua/firepoint/)
- `SRC-1202` — [KAI: oferty licencjackie 2026](https://pk.kai.edu.ua/offers-bachelor/)
- `SRC-1203` — [KPRM: nowe zdolnosci dzieki SAFE](https://www.gov.pl/web/premier/nowe-zdolnosci-wojska-polskiego-dzieki-programowi-safe---lista-zadan)
- `SRC-1204` — [Ministerstwo Finansow: podpisanie umowy SAFE](https://www.gov.pl/web/finanse/podpisanie-umowy-pozyczki-z-instrumentu-safe)
- `SRC-1205` — [Brave1: oficjalny licznik ekosystemu](https://www.brave1.gov.ua/en/)
- `SRC-1206` — [Prezydent Ukrainy: umowa o wspolpracy w dziedzinie bezpieczenstwa](https://www.president.gov.ua/en/news/ugoda-pro-spivrobitnictvo-u-sferi-bezpeki-mizh-ukrayinoyu-ta-92009)
- `SRC-1207` — [EDA: BraveTech EU](https://eda.europa.eu/news-and-events/news/2026/04/29/eda-partners-with-the-european-commission-on-bravetech-eu)
- `SRC-1208` — [Digital State UA: Brave1 Dataroom](https://digitalstate.gov.ua/news/tech/ukraine-launches-brave1-dataroom-with-palantir-to-train-ai-models-using-battlefield-data)
- `SRC-1209` — [Ministerstwo Cyfryzacji: Polityka AI do 2030 r.](https://ai.gov.pl/media/2025/11/Polityka-rozwoju-sztucznej-inteligencji-w-Polsce-do-2030-roku-17.11.2025__-1.pdf)
- `SRC-1210` — [Ministerstwo Cyfryzacji: Gaia AI Factory](https://www.gov.pl/web/cyfryzacja/gaia-ai--fabryka-sztucznej-inteligencji-powstaje-w-krakowie)
- `SRC-1211` — [NATO: revised AI strategy](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2024/07/10/summary-of-natos-revised-artificial-intelligence-ai-strategy)
- `SRC-1212` — [MRiT: program kompetencji dual-use](https://www.gov.pl/web/rozwoj-technologia/program-ministra-na-lata-20252029-wsparcie-kompetencji-w-obszarze-innowacji-dual-use)
- `SRC-1213` — [Komisja Europejska: Readiness Roadmap 2030](https://defence-industry-space.ec.europa.eu/eu-defence-industry/readiness-roadmap-2030_en)

## 5. Wynik bramki A12

**FAIL dla bezposredniego przeniesienia materialu inicjujacego do dokumentu publicznego.** Powodem sa cztery otwarte sprzecznosci zapisane w `a12-contradictions.yaml`. Pozostale zweryfikowane twierdzenia moga wejsc do dalszej syntezy dopiero z kwalifikatorami zapisanymi w rejestrze roszczen: deklaracja zamiast wykonania, pozyczka zamiast dotacji, pojemnosc licencyjna zamiast liczby studentow oraz projekt uruchomiony zamiast infrastruktury w pelni gotowej.
