import json
from random import randint
import sys

used_questions = []
money = 1000
print("Rozpoczynamy grę w 'Postaw na Milion'\n")

while True:
    file = open("level_four.json", "r", encoding="utf-8")
    questions_four = json.load(file)
    random_index_four_one = randint(0, len(questions_four) - 1)
    random_index_four_two = randint(0, len(questions_four) - 1)
    category_four_one = questions_four[random_index_four_one]["kategoria"]
    category_four_two = questions_four[random_index_four_two]["kategoria"]

    file2 = open("level_three.json", "r", encoding="utf-8")
    questions_three = json.load(file2)
    random_index_three_one = randint(0, len(questions_three) - 1)
    random_index_three_two = randint(0, len(questions_three) - 1)
    category_three_one = questions_three[random_index_three_one]["kategoria"]
    category_three_two = questions_three[random_index_three_two]["kategoria"]

    file3 = open("level_two.json", "r", encoding="utf-8")
    questions_two = json.load(file3)
    random_index_two_one = randint(0, len(questions_two) - 1)
    random_index_two_two = randint(0, len(questions_two) - 1)
    category_two_one = questions_two[random_index_two_one]["kategoria"]
    category_two_two = questions_two[random_index_two_two]["kategoria"]

    def losowe_pytanie(poziom, random_index):
        global used_questions
        global money
        global questions_four
        global questions_three
        global questions_two

        def closest_number(answer):
            q = int(answer / 25)
            n1 = 25 * q
            if (answer * 25) > 0:
                n2 = (25 * (q + 1))
            else:
                n2 = (25 * (q - 1))
            if abs(answer - n1) < abs(answer - n2):
                return n1
            return n2

        def sprawdzam(questions):
            global money
            global questions_four
            global questions_three
            global questions_two
            if questions[random_index]["prawidłowa odpowiedź"] == "a":
                if answer_a != 0:
                    money = answer_a
                    print(f"Prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Masz już {money} zł")
                else:
                    money = answer_a
                    print(f"Niestety prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Straciłeś wszystkie pieniądze. Koniec gry.")
                    sys.exit(1)
            if questions[random_index]["prawidłowa odpowiedź"] == "b":
                if int(answer_b) != 0:
                    money = answer_b
                    print(f"Prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Masz już {money} zł")
                else:
                    money = answer_b
                    print(f"Niestety prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Straciłeś wszystkie pieniądze. Koniec gry.")
                    sys.exit(1)
            if questions[random_index]["prawidłowa odpowiedź"] == "c":
                if int(answer_c) != 0:
                    money = answer_c
                    print(f"Prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Masz już {money} zł")
                else:
                    money = answer_c
                    print(f"Niestety prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Straciłeś wszystkie pieniądze. Koniec gry.")
                    sys.exit(1)
            if questions[random_index]["prawidłowa odpowiedź"] == "d":
                if int(answer_d) != 0:
                    money = answer_d
                    print(f"Prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Masz już {money} zł")
                else:
                    money = answer_d
                    print(f"Niestety prawidłowa odpowiedź to: {questions[random_index]['prawidłowa odpowiedź']}. "
                          f"Straciłeś wszystkie pieniądze. Koniec gry.")
                    sys.exit(1)

        if poziom == "cztery":
            print(f"Pytanie {len(used_questions) + 1}: {questions_four[random_index]['pytanie']}")
            used_questions.append(questions_four[random_index]["pytanie"])
            print(f"A: {questions_four[random_index]['a']}\nB: {questions_four[random_index]['b']}\n"
                  f"C: {questions_four[random_index]['c']}\nD: {questions_four[random_index]['d']}\n")
            answer_a = int(input("A: "))
            if answer_a >= money:
                answer_a = money
                answer_b = 0
                answer_c = 0
                answer_d = 0
                print(f"A: {money}\nB: 0\nC: 0\nD: 0")
            else:
                answer_b = int(input("B: "))
                if answer_a + answer_b >= money:
                    answer_a = closest_number(answer_a)
                    answer_b = money - answer_a
                    answer_c = 0
                    answer_d = 0
                    print(f"A: {answer_a}\nB: {answer_b}\nC: 0\nD: 0")
                else:
                    answer_c = int(input("C: "))
                    if answer_a + answer_b + answer_c >= money:
                        answer_a = closest_number(answer_a)
                        answer_b = closest_number(answer_b)
                        answer_c = money - answer_a - answer_b
                        answer_d = 0
                        print(f"A: {answer_a}\nB: {answer_b}\nC: {answer_c}\nD: 0")
                        print(f"B: {answer_b}")
                    else:
                        answer_d = int(input("D: "))
                        if answer_a and answer_b and answer_c != 0:
                            answer_a = closest_number(answer_a)
                            answer_b = closest_number(answer_b)
                            answer_c = money - answer_a - answer_b
                            answer_d = 0
                            print(f"A: {answer_a}\nB: {answer_b}\nC: {answer_c}\nD: 0")
                        else:
                            answer_a = closest_number(answer_a)
                            answer_b = closest_number(answer_b)
                            answer_c = closest_number(answer_c)
                            answer_d = money - answer_a - answer_b - answer_c
                            print(f"A: {answer_a}\nB: {answer_b}\nC: {answer_c}\nD: {answer_d}")
            sprawdzam(questions=questions_four)
        elif poziom == "trzy":
            print(f"Pytanie {len(used_questions) + 1}: {questions_three[random_index]['pytanie']}")
            used_questions.append(questions_three[random_index]["pytanie"])
            print(f"A: {questions_three[random_index]['a']}\nB: {questions_three[random_index]['b']}\n"
                  f"C: {questions_three[random_index]['c']}")
            answer_a = int(input("A: "))
            if answer_a >= money:
                answer_a = money
                answer_b = 0
                answer_c = 0
                print(f"A: {money}\nB: 0\nC: 0")
            else:
                answer_b = int(input("B: "))
                if answer_a + answer_b >= money:
                    answer_a = closest_number(answer_a)
                    answer_b = money - answer_a
                    answer_c = 0
                    print(f"A: {answer_a}\nB: {answer_b}\nC: 0")
                else:
                    answer_c = int(input("C: "))
                    if answer_a and answer_b != 0:
                        if answer_a >= answer_b:
                            answer_a = closest_number(answer_a)
                            answer_b = money - answer_a
                            answer_c = 0
                            print(f"A: {answer_a}\nB: {answer_b}\nC: 0")
                        else:
                            answer_b = closest_number(answer_b)
                            answer_a = money - answer_b
                            answer_c = 0
                            print(f"A: {answer_a}\nB: {answer_b}\nC: 0")
                    else:
                        answer_a = closest_number(answer_a)
                        answer_b = closest_number(answer_b)
                        answer_c = money - answer_a - answer_b
                        print(f"A: {answer_a}\nB: {answer_b}\nC: {answer_c}")
            sprawdzam(questions=questions_three)
        else:
            print(f"Pytanie {len(used_questions) + 1}: {questions_two[random_index]['pytanie']}")
            used_questions.append(questions_two[random_index]["pytanie"])
            print(f"A: {questions_two[random_index]['a']}\nB: {questions_two[random_index]['b']}")
            answer_a = int(input("A: "))
            if answer_a >= money:
                answer_a = money
                answer_b = 0
                print(f"A: {money}\nB: 0")
            else:
                answer_b = int(input("B: "))
                if answer_a != 0:
                    if answer_a >= answer_b:
                        answer_a = money
                        answer_b = 0
                        print(f"A: {answer_a}\nB: 0")
                    else:
                        answer_a = 0
                        answer_b = money
                        print(f"A: 0\nB: {answer_b}")
                else:
                    answer_a = 0
                    answer_b = money
                    print(f"A: 0\nB: {answer_b}")
            sprawdzam(questions=questions_two)

    def gra():
        if 0 <= len(used_questions) < 4:
            print(f"Którą kategorię wybierasz?\n[1] {category_four_one.upper()}\n[2] {category_four_two.upper()}")
            answer_category = input("->> ")
            print(f"Wybrana kategoria to: "
                  f"{category_four_one.upper() if answer_category == '1' else category_four_two.upper()}\n")
            if answer_category == "1":
                losowe_pytanie(poziom="cztery", random_index=random_index_four_one)
                print()
            else:
                losowe_pytanie(poziom="cztery", random_index=random_index_four_two)
                print()
        elif 4 <= len(used_questions) < 7:
            print(f"Którą kategorię wybierasz?\n[1] {category_three_one.upper()}\n[2] {category_three_two.upper()}")
            answer_category = input("->> ")
            print(f"Wybrana kategoria to: "
                  f"{category_three_one.upper() if answer_category == '1' else category_three_two.upper()}\n")
            if answer_category == "1":
                losowe_pytanie(poziom="trzy", random_index=random_index_three_one)
                print()
            else:
                losowe_pytanie(poziom="trzy", random_index=random_index_three_two)
                print()
        elif len(used_questions) == 7:
            print(f"Którą kategorię wybierasz?\n[1] {category_two_one.upper()}\n[2] {category_two_two.upper()}")
            answer_category = input("->> ")
            print(f"Wybrana kategoria to: "
                  f"{category_two_one.upper() if answer_category == '1' else category_two_two.upper()}\n")
            if answer_category == "1":
                losowe_pytanie(poziom="dwa", random_index=random_index_two_one)
                print()
            else:
                losowe_pytanie(poziom="dwa", random_index=random_index_two_two)
                print()
        else:
            print("Koniec gry")
            sys.exit(1)

    gra()
