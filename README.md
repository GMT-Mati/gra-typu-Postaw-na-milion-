# gra typu "Postaw na milion"
Gra podobna do "Postaw na Milion". Baza pytań  w trakcie rozbudowy. Na razie tylko backend, frontendowa wersja pygame w przygotowaniu.

# Przygotowanie:
Pomysł na grę zrodził się jako jako pierwszy pojekt pythona.
W poczatkowej fazie gra miała być prostą gierką - w sumie nadal taka pozostała - gdzie naliczane są punkty za każdą poprawną odpowiedź, w trakcie rozbudowy kodu pojawiły się nowe pomysły i funkcjonalności.

# Przebieg tworzenia programu i napotkane po drodze trudności:
1. Zacząłem od napisania kodu doadającego punkt za każdą prawidłową odpowiedź. W każdym pytaniu można było wybrać tylko jedną odpowiedź, a same pytanie były zadawane po kolei.
2. W celach testowych stworzyłem plik json z zestawem pytań. Każde pytanie miało przypisane cztery propozycje odpowiedzi oraz prawidłową odpowiedź.
3. Następnie dodałem funkcjonalnoć w której pytania są losowane co sprawiło że każda gra mogła być inna, oraz opcję zakończenia gry po błędnej odpowiedzi.
4. Pojawia się pomysł przekształcenia gry w tę typu 'Postaw na milion' - w związku z tym do pliku json dopisałem "kategorię" każdego pytania, a w kodzie programu ustawiłem opcję w której najpierw losuje się dwie kategorie i gracz wybiera jedną z nich, dopiero później pada pytanie odpowiednie dla wybranej kategorii. Problemem na tym etapie było podwójne losowanie tej samej kategorii. Gracz nadal mógł wybrać tylko jedną odpowiedź.
5. Aby zbliżyć się do oryginału wprowadziłem opcję stawiania dowolnej kwoty na każdą z propozycji odpowiedzi. Następnie napisałem kod który weryfikował czy pod poprawną odpowiedzią jest jakaś kwota różna od zera i przypisywał kwotę z tej odpowiedzi jako kwotę wygraną w grze. Problemem na tym etapie okazało się nadpisywanie poprawnej dopowiedzi w zwiażku z czym program zawsze widział dwie odpowiedzi jako poprawne, nadpisywanie kwoty wygranej bez limitu, brak zakończenia gry przy kwocie zero.
6. W tym etapie priorytetem było poprawne sprawdzenie stawek z prawidłową odpowiedzią, jeśli odpowiedź była właściwa to dopisanie stawki do kwoty wygranej, naprawienie błędu limitu wygranej.
7. Ustawienie maksymalnej ilości pytań, ustawinie poziomu pytania w zależności od etapu gry: przy pytaniach 1-4 wyświetlanie czterech odpowiedzi, przy pytaniach 5-7 wyświetlanie trzech odpowiedzi, w finałowym 8 pytaniu wyświetlenie dwóch możliwych odpowiedzi, dopisanie w pliku json "poziomu" pytań.
8. Opcja informująca o zakończeniu gry kiedy kwota spada do 0 zł.
9. Skrócenie kodu poprzez stworzenie funkcji kategoria(pytanie, random_index) które okazało się wadliwe, pjawił się bug dobierajacy do kategori 1 odpowiedzi z kategorii 2 i na odwrót, błąd został naprawiony jednak działąnie tej funkcji okazało się niewystraczające.
10. !!! największy problem w programie !!! którego do końca nie roziwązałem to problem z dobieraniem odpowiedniego poziomu pytania, pojawił się duży bug zamykający program, a polegający na wyświetlaniu pytania cztero-odpowiedziowego(z poziomu 1-4) w momencie kiedy powinien losować pytania trzy- lub dwu-odpowiedziowe(poziom 5-8). W związku z brakiem wyświetlenia odpwiedzi C i D które były w pliku źrółowym json, program się zamykał z błędem.
11. Ponieważ nie potrafiłem rozwiązac problemu z indeksowaniem pytania po poziomie, postanowiłem zamiast jednego pliku json utworzyć trzy, po jednym dla każdego z poziomów pytań.
12. Utworzyłem funkcje losującą pytanie w zależności od poziomu.
13. Utworzyłem listę użytych pytań i uwarunkowanie poziomu gry w zależności od jej długości.
14. Funkcja drukowania dwóch kategorii i możliość wybrania jednej z nich.
15. Funkcja drukowania pytania praz odpowiedzi po wyborze kategorii.
16. Funkcja ustalenia stawek na konkretne odpowiedzi, bez limitu i wszystkie odpowiedzi mogą być obstawiane.
17. Sprawdzenie odpowiedzi, sprawdzenie jakie stawki zostały obstawione i zapisanie wygranej kwoty tymczsowej.
18. Ustawienie limitów stawek, automatyczne liczenie wygranej po pisaniu odpowiedzi, limit wygranej kwoty.
19. Funkcja wymuszająca jedną odpowiedź pustą.
20. Funkcja wymuszajaca skok stawki na 25tys, polegająca na zaokrąglaniu podanej przez gracza kwoty do tej najbliższej, podzielnej przez 25.
21. Skrócenie kody o połowę poprzez definicje i odpowiednie ustawienie pętli oraz \n print.
22. Stworzenie osobnej funkcji sprawdzajacej poprawną odpowiedź.
23. Stworzenie funkcji przebiegu gry.

Kluczowym elementem na następny etap gry jest dodanie funkcji niepowtarzania się pytań i praca nad frontendową wersją gry. Oraz poprawienie przejrzystości i funkcjonalności kodu.

Wszystkie uwagi i podpowiedzi jak ulepszyć kod mile widziane :)
