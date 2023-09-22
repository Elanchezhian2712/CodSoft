import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkthemes import ThemedStyle


quiz_data = {
    "question": [
        "Q1. What Indian city is the capital of two states?",
        "Q2. Which city is the capital of India?",
        "Q3. Smallest State of India?",
        "Q4. Where is Taj Mahal Located?"
    ],
    "answer": [
        1,
        2,
        3,
        2
    ],
    "options": [

        ["Chandigarh", "Kolkata", "Delhi", "Bangalore"],
        ["Jaipur", "Delhi", "Chennai", "Mumbai"],
        ["Rajasthan", "Punjab", "Goa", "Bihar"],
        ["Lucknow", "Agra", "Bhopal", "Delhi"]
    ]
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Codsoft Intern - Quiz Game")
        self.root.attributes('-fullscreen', True)  
        self.root.configure(bg="#EAF6FF")

        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")

        self.current_question = 0
        self.score = 0

        self.load_quiz_data()
        self.create_widgets()
        self.display_question()

    def load_quiz_data(self):
        pass

    def create_widgets(self):
        self.title_label = ttk.Label(self.root, text="Codsoft Intern - Quiz Game", font=("Helvetica", 40), background="#EAF6FF")
        self.title_label.pack(pady=20)

        self.question_label = ttk.Label(self.root, text="", font=("Helvetica", 30), background="#EAF6FF")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button_style = ttk.Style()
            button_style.configure("Option.TButton", font=("Helvetica", 20))
            button = ttk.Button(self.root, text="", style="Option.TButton", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
        
        self.next_button = ttk.Button(self.root, text="Next", style="Option.TButton", command=self.next_question)

        self.show_widgets() 

    def show_widgets(self):
        for button in self.option_buttons:
            button.pack(pady=10, padx=20)  

        self.next_button.pack(pady=20, padx=20)  

    def hide_widgets(self):
        for button in self.option_buttons:
            button.pack_forget()

        self.next_button.pack_forget()

    def display_question(self):
        if self.current_question < len(quiz_data["question"]):
            question_text = quiz_data["question"][self.current_question]
            options = quiz_data["options"][self.current_question]

            self.question_label.config(text=question_text)

            for i in range(4):
                self.option_buttons[i].config(text=options[i])

            self.show_widgets()
        else:
            self.hide_widgets()  # Hide the widgets when showing the result
            self.show_result()

    def check_answer(self, selected_option):
        correct_answer = quiz_data["answer"][self.current_question]
        if selected_option == correct_answer:
            self.score += 1

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Result", f"You scored {self.score}/{len(quiz_data['question'])}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
