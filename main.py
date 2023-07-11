import tkinter as tk
from tkinter import messagebox



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genereal Knowladge Quiz App")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Madrid", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "Which country won the 2018 FIFA World Cup?",
                "options": ["Brazil", "Germany", "France", "Spain"],
                "answer": "France"
            },
            {
                "question": "What is the capital of Italy?",
                "options": ["London", "Berlin", "Milan", "Rome"],
                "answer": "Rome"
            },
             {
                "question": "Where do polar bears live?",
                "options": ["The South Pole", "The Arctic", "Australia", "Canada"],
                "answer": "The Arctic"
            }
        ]
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.option_var = tk.StringVar()
        self.option_var.set(None)

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.option_var, value=i)
            button.pack()
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def next_question(self):
        selected_option = self.option_var.get()
        if selected_option is None:
            messagebox.showinfo("Quiz App", "Please select an option!")
            return

        question_data = self.questions[self.current_question]
        if question_data["options"][int(selected_option)] == question_data["answer"]:
            self.score += 1

        self.current_question += 1
        self.option_var.set(None)

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz App", f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()


root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()
