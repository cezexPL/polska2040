# GOAL v0.1 — 24 godziny

## Cel

W ciągu maksymalnie 24 godzin zbudować audytowalny ekspercki draft v0.1 niezależnej strategii „Polska 2040: Suwerenność technologiczna”, oparty wyłącznie na jawnych, aktualnych i sprawdzalnych źródłach.

## Obowiązkowe rezultaty

1. Pełny rdzeń strategii i plan realizacji.
2. Analiza finansowania, wpływu gospodarczego, ryzyk i wariantów.
3. Pakiety dla Premiera/RM oraz Prezydenta/BBN.
4. Briefy funkcjonalne dla ośmiu portfeli ministerialnych.
5. Prezentacje gospodarcza, regionalna i anglojęzyczna.
6. Jawny szablon aneksu ograniczonego, bez treści niejawnych.
7. Rejestry źródeł, twierdzeń, luk, decyzji, ryzyk i sprzeczności.
8. Powtarzalne artefakty HTML, PDF, DOCX i PPTX.
9. Niezależny red-team, audyt halucynacji i raport walidacyjny.
10. Draft PR do `main` z przechodzącym CI.

## Pętla badawcza

1. **Plan:** zdefiniuj 3–6 pytań dla domeny.
2. **Retrieval:** zacznij od źródeł pierwotnych; wykonaj co najmniej dwie strategie wyszukiwawcze, gdy wynik jest pusty lub wątpliwy.
3. **Rejestracja:** zapisz źródło, datę, lokalizator, typ, licencję i sumę kontrolną, gdy pobrano kopię.
4. **Klasyfikacja:** oddziel fakt, estymację, scenariusz, wniosek i rekomendację.
5. **Weryfikacja:** autor nie zatwierdza własnego twierdzenia; ważne liczby wymagają drugiego źródła albo jawnego wyjątku dla autorytatywnego aktu lub datasetu.
6. **Synteza:** pokaż teorię zmiany, warianty, koszty alternatywne, ryzyka oraz kryteria przerwania programu.
7. **Red-team:** szukaj argumentów obalających rekomendację i niezamierzonych skutków.
8. **Budowa:** generuj wszystkie formaty z tych samych modułów i danych.
9. **Naprawa:** usuń, osłab lub oznacz twierdzenia, których nie udało się potwierdzić.
10. **Kontrola końcowa:** sprawdź kompletność, źródła, liczby, bezpieczeństwo, dostępność i rendering.

## Harmonogram

| Okno | Rezultat |
|---|---|
| 0:00–1:00 | repozytorium, polityki, schematy, pipeline |
| 1:00–4:30 | bezpieczeństwo/NATO, realizacja państwowa, bazowy audyt dowodów |
| 4:30–8:00 | potrzeby użytkowników, systemy autonomiczne, AI/dane/cyber |
| 8:00–11:30 | przemysł, finanse, Ukraina/UE/JV/eksport |
| 11:30–15:00 | prawo/etyka, edukacja/kadry, zastosowania cywilne/regiony |
| 15:00–18:30 | synteza strategii, planu realizacji, modelu i KPI |
| 18:30–20:30 | briefy, prezentacje i wersja angielska |
| 20:30–22:00 | wykresy, ilustracje i kompilacja formatów |
| 22:00–23:15 | red-team i ponowna kontrola źródeł |
| 23:15–24:00 | naprawy, walidacja, README i draft PR |

## Zasady bez wyjątków

- Używaj tylko jawnych źródeł.
- Nie wpisuj brakującej liczby „dla kompletności”. Zapisz `UNKNOWN` i plan pozyskania.
- Nie cytuj wyniku wyszukiwarki; otwórz źródło i wskaż stronę lub sekcję.
- Nie ukrywaj sprzeczności między źródłami.
- Nie twórz specyfikacji uzbrojenia, instrukcji operacyjnych, częstotliwości, lokalizacji wrażliwych obiektów ani katalogu podatności.
- Nie sugeruj oficjalnego poparcia państwa.
- Nie publikuj publicznie, nie wysyłaj materiałów i nie kontaktuj instytucji bez akceptacji człowieka.

## Warunki ukończenia

- Wszystkie wymagane artefakty istnieją albo mają precyzyjny status `BLOCKED` z brakującym wejściem.
- Zero niezweryfikowanych faktów w notach wykonawczych.
- Każda ważna liczba ma identyfikator twierdzenia, źródło i datę aktualności.
- Zero nierozwiązanych usterek krytycznych red-team.
- `make validate` i `make build` kończą się powodzeniem.
- Draft PR zawiera wynik walidacji, listę luk i artefakty do recenzji.

