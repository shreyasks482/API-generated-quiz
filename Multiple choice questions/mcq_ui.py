from tkinter import *
from quiz_brain import QuizBrain
import random
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        # self.timer_id = None
        self.shuffled_options = None
        self.right_answer = None
        self.shuf_op4 = None
        self.shuf_op2 = None
        self.shuf_op3 = None
        self.shuf_op1 = None
        self.question_timer = None
        self.quiz = quizbrain
        

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(1400, 750)
        # self.window.minsize(1450, 400)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0)

        self.timer_label = Label(text="00", fg="white", font=("Arial", 10, "italic"), bg=THEME_COLOR)
        self.timer_label.grid(row=0, column=1)

        self.canvas = Canvas(width=1400, height=400, bg="white", highlightthickness=0)
        self.option1 = Button(width=40, height=2, text="Option 1", fg=THEME_COLOR, bg="white",
                              font=("Arial", 15, "italic"), command=self.pressed_op1)
        self.option1.grid(row=2, column=0, pady=20)
        self.option2 = Button(width=40, height=2, text="Option 2", fg=THEME_COLOR, bg="white",
                              font=("Arial", 15, "italic"), command=self.pressed_op2)
        self.option2.grid(row=2, column=1, pady=20)
        # self.window.columnconfigure(3,minsize=20, pad=10)
        self.option3 = Button(width=40, height=2, text="Option 3", fg=THEME_COLOR, bg="white",
                              font=("Arial", 15, "italic"), command=self.pressed_op3)
        self.option3.grid(row=3, column=0)
        self.option4 = Button(width=40, height=2, text="Option 4", fg=THEME_COLOR, bg="white",
                              font=("Arial", 15, "italic"), command=self.pressed_op4)
        self.option4.grid(row=3, column=1)

        self.question_text = self.canvas.create_text(
            700,
            200,
            width=1400,  # to align the question size
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def shuffle(self, right, wrong1, wrong2, wrong3):
        options = [right, wrong1, wrong2, wrong3]
        random.shuffle(options)
        self.shuffled_options = options
        shuffled_options = self.shuffled_options
        # print(self.shuffled_options)
        self.right_answer = right
        self.shuf_op1 = shuffled_options[0]
        self.shuf_op2 = shuffled_options[1]
        self.shuf_op3 = shuffled_options[2]
        self.shuf_op4 = shuffled_options[3]

        self.option1.config(text=shuffled_options[0], bg="white", state="normal")
        self.option2.config(text=shuffled_options[1], bg="white", state="normal")
        self.option3.config(text=shuffled_options[2], bg="white", state="normal")
        self.option4.config(text=shuffled_options[3], bg="white", state="normal")

    def update_timer(self):
        elapsed_time = int(11 - (time.time() - self.question_timer))
        if elapsed_time < 1:
            self.canvas.itemconfig(self.question_text, text="Time Up!!")
            self.option1.config(bg="white", state="disabled")
            self.option2.config(bg="white", state="disabled")
            self.option3.config(bg="white", state="disabled")
            self.option4.config(bg="white", state="disabled")
        if elapsed_time < 0:
            self.window.after(1, self.get_next_question)
        else:
            self.timer_label.config(text=f"{elapsed_time}")
            self.window.after(1000, self.update_timer)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.question_timer = time.time()
            q_text, right_option, wrong_option1, wrong_option2, wrong_option3 = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.shuffle(right_option, wrong_option1, wrong_option2, wrong_option3)
            self.update_timer()
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.option1.config(bg="white", text="View Score", state="disabled")
            self.option2.config(bg="white", text="Retake the quiz", state="disabled")
            self.option3.config(bg="white", text="Change Category", state="disabled")
            self.option4.config(bg="white", text="END", state="disabled")

    def pressed_op1(self):
        is_right = self.quiz.check_answer(self.shuf_op1)
        if not is_right:
            self.option1.config(bg="red")
        self.give_feedback(is_right)

    def pressed_op2(self):
        is_right = self.quiz.check_answer(self.shuf_op2)
        if not is_right:
            self.option2.config(bg="red")
        self.give_feedback(is_right)

    def pressed_op3(self):
        is_right = self.quiz.check_answer(self.shuf_op3)
        if not is_right:
            self.option3.config(bg="red")
        self.give_feedback(is_right)

    def pressed_op4(self):
        is_right = self.quiz.check_answer(self.shuf_op4)
        if not is_right:
            self.option4.config(bg="red")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            if self.shuf_op1 == self.right_answer:
                self.option1.config(bg="green")
            elif self.shuf_op2 == self.right_answer:
                self.option2.config(bg="green")
            elif self.shuf_op3 == self.right_answer:
                self.option3.config(bg="green")
            elif self.shuf_op4 == self.right_answer:
                self.option4.config(bg="green")

        else:
            if self.shuf_op1 == self.right_answer:
                self.option1.config(bg="green")
            elif self.shuf_op2 == self.right_answer:
                self.option2.config(bg="green")
            elif self.shuf_op3 == self.right_answer:
                self.option3.config(bg="green")
            elif self.shuf_op4 == self.right_answer:
                self.option4.config(bg="green")

        self.window.after(1000, self.get_next_question)
