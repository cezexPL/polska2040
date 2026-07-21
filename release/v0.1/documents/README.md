# Architektura pakietu i forma dla odbiorcy

## Dlaczego wiele dokumentów

Strategia państwa nie powinna być jednym plikiem używanym do wszystkich celów. Pełny dokument jest źródłem wspólnych założeń, lecz decyzja Rady Ministrów, rozmowa Prezydenta z BBN, praca resortu i wystąpienie na forum gospodarczym wymagają innego poziomu szczegółowości, języka i wezwania do działania.

Repozytorium stosuje model **jednego rdzenia i wielu kontrolowanych wyjść**. Fakty (`CLM-*`), definicje (`DEF-*`), kandydaty decyzji (`DEC-*`) i zastrzeżenia mają te same identyfikatory, ale każdy materiał odpowiada na pytania właściwe dla odbiorcy. Dzięki temu skrót nie staje się nową, niespójną strategią. Rekord `DEC-*` o statusie `candidate` nie jest decyzją organu państwa.

Wydanie v0.1 jest materiałem **przedmandatowym**. Nie jest gotowe do formalnego przedłożenia Radzie Ministrów, ponieważ właściwy minister, podstawa procesu i relacja do obowiązujących strategii pozostają nierozstrzygnięte (`GAP-0011`). Może służyć konsultacjom eksperckim z tym zastrzeżeniem.

## Mapa użycia

| Odbiorca / sytuacja | Materiał główny | Materiał podczas spotkania | Załączniki | Cel |
|---|---|---|---|---|
| Premier i Rada Ministrów | nota decyzyjna 6–8 stron | prezentacja 15 slajdów | roadmapa, finanse, governance | konsultacja kandydatów mandatu, właścicieli, przeglądu i działań odwracalnych; formalne przedłożenie dopiero po zamknięciu GAP-0011 |
| Prezydent RP i BBN | nota strategiczna 6–8 stron | prezentacja 12 slajdów | strategia jawna, jawny szablon aneksu ograniczonego | wniosek o przegląd ciągłości, odporności i zgodności sojuszniczej bez przejmowania kompetencji rządu |
| Minister / kierownictwo resortu | właściwy brief portfelowy ok. 2 stron | wybrane slajdy RM | karta działań z roadmapy i RACI | przyjęcie właściciela, danych, terminu, zależności i miernika |
| Zespół międzyresortowy | plan realizacji | dashboard i rejestr decyzji | model XLSX, rejestr ryzyk | zarządzanie bramkami, zależnościami, płatnościami i zamknięciami projektów |
| Forum gospodarcze | brak długiego pre-readu albo 2-stronicowy wyciąg | prezentacja 16–18 slajdów | publiczna strategia po zatwierdzeniu | reguły udziału rynku, popyt, kapitał, produktywność i eksport |
| Forum regionalne / samorząd | [karta pilotażu](templates/regional-pilot-card.md) | prezentacja 12–14 slajdów | brief właściwego portfela i [szablon danych wojewódzkich](templates/voivodeship-data-template.md) | role regionu, szkół, MŚP i infrastruktury; kwalifikacja do pilotażu bez obietnic politycznych |
| Partner UE/NATO/Ukraina | executive brief po angielsku | prezentacja 12 slajdów po angielsku | wybrane jawne moduły strategii | warunkowa propozycja wartości do zatwierdzenia przez rząd, z IP, bezpieczeństwem, due diligence i interoperacyjnością |
| Ekspert, legislator, kontroler | pełna strategia i dokumenty domenowe | warsztat roboczy | Księga dowodowa i raport red-team | sprawdzenie założeń, prawa, źródeł, finansów i wykonalności |

## Zasada pre-read i spotkania

1. Materiał główny trafia do odbiorcy przed spotkaniem, jeśli zezwala na to właściciel procesu.
2. Prezentacja nie zastępuje noty; prowadzi do konkretnych decyzji.
3. Na pierwszym spotkaniu nie przedstawia się niezweryfikowanych docelowych kwot, lokalizacji ani list preferowanych dostawców.
4. Wszystkie pytania wymagające danych chronionych trafiają do formalnego bezpiecznego obiegu. Jawny szablon określa strukturę, ale nie zawiera odpowiedzi.
5. Po spotkaniu aktualizuje się rejestr decyzji, właściciela, termin i przesłankę — nie tylko slajdy.

## Różnice w narracji

### Premier i Rada Ministrów

Pierwsza strona zaczyna się od decyzji wymaganej dziś, wariantów i kosztu zwłoki. Treść pokazuje odpowiedzialność międzyresortową, działania na 100 dni, bramkę powrotu do RM i kwestie, których jeszcze nie wolno zatwierdzić.

### Prezydent i BBN

Materiał zaczyna się od odporności państwa, ciągłości po zmianie rządu, zgodności z NATO oraz ochrony interesu strategicznego. Nie przypisuje Prezydentowi kompetencji wykonawczych rządu. Wyraźnie rozdziela część jawną od pytań do przyszłego aneksu w uprawnionym środowisku.

### Minister

Brief odpowiada na pięć pytań: za co portfel odpowiada, co ma dostarczyć w 100 dni, od kogo zależy, jakie dane są potrzebne i po czym poznać wynik. Powinien prowadzić do imiennego właściciela służbowego i harmonogramu, nie do ogólnej deklaracji poparcia.

### Forum gospodarcze

Przekaz publiczny koncentruje się na przewidywalnym popycie, konkurencji, standardach, cyklu życia, finansowaniu i eksporcie. Nie używa informacji wrażliwych ani narracji wojennej jako substytutu uzasadnienia gospodarczego. Jasno pokazuje, że grant nie gwarantuje zamówienia, a pilotaż nie gwarantuje skali.

### Forum regionalne

Materiał pokazuje kryteria, według których region może wejść do pilotażu: realny popyt, prowadzący, laboratoria, praktyki, MŚP, gotowość danych i dostęp mniejszych miejscowości. Nie obiecuje „po jednym centrum” bez audytu i nie kopiuje danych z innego województwa.

### Partner międzynarodowy

Wersja angielska opisuje **kandydującą propozycję wartości**, a nie oficjalną ofertę Polski. Potencjalna współpraca w testowaniu, certyfikacji, produkcji, finansowaniu i wejściu na rynek UE/NATO wymaga zatwierdzenia rządu, przeglądu prawnego oraz due diligence bezpieczeństwa. Każde partnerstwo ma mierzalny produkt, zasady IP, kontrolę eksportu, plan ciągłości i możliwość zakończenia.

## Kontrola wersji

- Dokument strategiczny i noty pokazują datę stanu wiedzy.
- Slajdy zawierają status niezależnego draftu na każdej stronie.
- Liczby zmienne są sprawdzane przy każdym wydaniu.
- Materiały publiczne są generowane dopiero z oczyszczonego eksportu.
- Zmiana faktu w rdzeniu wymaga aktualizacji identyfikatora twierdzenia i ponownej kompilacji wszystkich zależnych wyjść.
