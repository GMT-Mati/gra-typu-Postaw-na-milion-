import json
import random
import sys
import tkinter as tk
from tkinter import messagebox

class MillionaireGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Postaw na Milion")
        
        self.used_questions = []
        self.money = 1000
        
        self.load_questions()
        self.create_gui()
        
    def load_questions(self):
        self.level_questions = {}
        levels = ["level_four.json", "level_three.json", "level_two.json"]
        for i, level in enumerate(levels, start=2):
            self.level_questions[i] = load_questions(level)
        
    def create_gui(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)
        
        self.answer_buttons = []
        for letter in ["A", "B", "C", "D"]:
            button = tk.Button(self.root, text="", font=("Helvetica", 10))
            button.config(command=lambda letter=letter: self.select_answer(letter))
            self.answer_buttons.append(button)
            button.pack(padx=10, pady=5, fill="both")
        
        self.next_question_button = tk.Button(self.root, text="Next Question", font=("Helvetica", 12))
        self.next_question_button.config(state="disabled", command=self.next_question)
        self.next_question_button.pack(pady=10)
        
        self.update_question()
        
    def update_question(self):
        if len(self.used_questions) < 8:
            level = self.determine_level()
            random_question = random.choice(self.level_questions[level])
            self.used_questions.append(random_question["pytanie"])
            self.current_question = random_question
            self.display_question()
        else:
            self.game_over()
            
    def determine_level(self):
        if len(self.used_questions) < 4:
            return 2
        elif len(self.used_questions) < 7:
            return 3
        else:
            return 4
            
    def display_question(self):
        self.question_label.config(text=f"Pytanie {len(self.used_questions)}: {self.current_question['pytanie']}")
        answers = [self.current_question['a'], self.current_question['b'], self.current_question['c'], self.current_question['d']]
        random.shuffle(answers)
        for i, button in enumerate(self.answer_buttons):
            button.config(text=f"{chr(65 + i)}. {answers[i]}")
        self.next_question_button.config(state="disabled")
        
    def select_answer(self, letter):
        selected_index = ord(letter) - 65
        selected_answer = self.current_question['abcd'][selected_index]
        self.money -= selected_answer
        self.display_question()
        correct_answer = self.current_question["prawidłowa odpowiedź"]
        if selected_answer == correct_answer:
            if len(self.used_questions) == 8:
                self.game_over()
            else:
                self.next_question_button.config(state="active")
        else:
            self.game_over()
            
    def next_question(self):
        self.update_question()
        
    def game_over(self):
        if self.money == 1000000:
            message = "Gratulacje! Wygrałeś milion!"
        else:
            message = f"Koniec gry. Wygrałeś {self.money} zł."
        messagebox.showinfo("Koniec gry", message)
        self.root.destroy()

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()
