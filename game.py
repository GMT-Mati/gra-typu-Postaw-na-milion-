import json
import random
import sys

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def ask_question(question):
    print(f"Pytanie {len(used_questions) + 1}: {question['pytanie']}")
    print(f"A: {question['a']}\nB: {question['b']}\nC: {question['c']}\nD: {question['d']}\n")
    answers = {
        'a': int(input("A: ")),
        'b': int(input("B: ")),
        'c': int(input("C: ")),
        'd': int(input("D: "))
    }
    return answers

def closest_number(answer, money):
    q = int(answer / 25)
    n1 = 25 * q
    n2 = 25 * (q + 1)
    return n1 if abs(answer - n1) < abs(answer - n2) else n2

def check_answer(answer, correct_answer, money):
    if answer == correct_answer:
        print(f"Prawidłowa odpowiedź to: {correct_answer}. Masz już {money} zł")
    else:
        print(f"Niestety prawidłowa odpowiedź to: {correct_answer}. Straciłeś wszystkie pieniądze. Koniec gry.")
        sys.exit(1)

print("Rozpoczynamy grę w 'Postaw na Milion'\n")

used_questions = []
money = 1000

while len(used_questions) < 8:
    if len(used_questions) < 4:
        level_questions = load_questions("level_four.json")
    elif len(used_questions) < 7:
        level_questions = load_questions("level_three.json")
    else:
        level_questions = load_questions("level_two.json")

    random_question = random.choice(level_questions)
    used_questions.append(random_question["pytanie"])
    
    answers = ask_question(random_question)
    correct_answer = random_question["prawidłowa odpowiedź"]
    
    if sum(answers.values()) > money:
        max_answer = max(answers, key=answers.get)
        answers[max_answer] -= sum(answers.values()) - money
    
    for letter, value in answers.items():
        money -= value
        print(f"{letter.upper()}: {value}")
    
    check_answer(correct_answer, max(answers, key=answers.get), money)

print("Koniec gry")
