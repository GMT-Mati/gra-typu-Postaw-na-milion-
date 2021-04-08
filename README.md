# gra-typu-Postaw-na-milion-
Gra podobna do "Postaw na Milion". Baza pytań  w trakcie rozbudowy. Na razie tylko backend, frontendowa wersja pygame w przygotowaniu.

# Przygotowanie:
Pomysł na grę zrodził się jako jako pierwszy pojekt pythona.
W poczatkowej fazie gra miała być prostą gierką - w sumie nadal taka pozostała - gdzie naliczane są punkty za każdą poprawną odpowiedź, w trakcie rozbudowy kodu pojawiły się nowe pomysły i funkcjonalności.

# Przebieg tworzenia programu i napotkane po drodze trudności:
1. zacząłem od napisania kodu doadającego punkt za każdą prawidłową odpowiedź. W każdym pytaniu można było wybrac tylko jedną odpowiedź, a same pytanie były zadawane po kolei.
2. w celach testowych stworzyłem plik json z zestawem pytań. Każde pytanie miało przypisane cztery propozycje odpowiedzi oraz prawidłową odpowiedź.
3. następnie dodałem funkcjonalnoć w której pytania są losowane co sprawiło że każda gra mogła być inna
4. pojawia się pomysł przekształcenia gry w te typu 'Postaw na milion' - w związku z tym do pliku json dopisałem kategorię każdego pytania, a w kodzie programu ustawiłem opcję w której najpierw losuje się dwie kategorie i gracz wybiera jedną z nich, dopiero później pada pytanie odpowiednie dla wybranej kategorii. Problemem na tym etapie było podwójne losowanie tej samej kategorii.
