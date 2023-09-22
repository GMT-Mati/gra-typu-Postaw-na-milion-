import tkinter as tk
import json
from random import randint
import sys

class PostawNaMilionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Postaw na Milion")

        self.used_questions = []
        self.money = 1000

        self.load_questions()

        self.label_question = tk.Label(root, text="", wraplength=500)
        self.label_question.pack()

        self.radio_var = tk.StringVar()
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value=str(i))
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.label_money = tk.Label(root, text=f"Pieniądze: {self.money} zł")
        self.label_money.pack()

        self.submit_button = tk.Button(root, text="Odpowiedz", command=self.check_answer)
        self.submit_button.pack()

        self.next_question()

    def load_questions(self):
        self.questions = {"cztery": [], "trzy": [], "dwa": []}

        with open("level_four.json", "r", encoding="utf-8") as file:
            self.questions["cztery"] = json.load(file)

        with open("level_three.json", "r", encoding="utf-8") as file:
            self.questions["trzy"] = json.load(file)

        with open("level_two.json", "r", encoding="utf-8") as file:
            self.questions["dwa"] = json.load(file)

    def next_question(self):
        level = "cztery" if len(self.used_questions) < 4 else ("trzy" if len(self.used_questions) < 7 else "dwa")
        level_questions = self.questions[level]

        while True:
            random_index = randint(0, len(level_questions) - 1)
            if random_index not in self.used_questions:
                break

        self.used_questions.append(random_index)
        question = level_questions[random_index]

        self.label_question.config(text=question["pytanie"])

        answers = [question["a"], question["b"], question["c"], question["d"]]
        self.radio_var.set("-1")  # Deselect all radio buttons

        for i in range(4):
            self.radio_buttons[i].config(text=answers[i])

    def check_answer(self):
        selected_index = int(self.radio_var.get())

        if selected_index == -1:
            return  # No answer selected

        correct_answer = self.questions["cztery"][self.used_questions[-1]]["prawidłowa odpowiedź"]

        if selected_index == ["a", "b", "c", "d"].index(correct_answer):
            self.money *= 2
            self.label_money.config(text=f"Pieniądze: {self.money} zł")
            self.next_question()
        else:
            self.money = 0
            self.label_money.config(text="Przegrałeś wszystkie pieniądze. Koniec gry.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = PostawNaMilionGame(root)
    root.mainloop()
