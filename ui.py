from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="White", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="New Text", font=('arial', 20, 'italic'),
                                                     width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_click)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_click)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="Questions Completed")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_click(self):
        result = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas_color(result)

    def false_click(self):
        result = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas_color(result)

    def canvas_color(self, result):

        print(result)
        if result:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, func=self.get_next_question)
