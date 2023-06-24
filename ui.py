from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH  = 340
HEIGHT = 500
PADX=20
PADY=20
WIDTH_rectangle = 300
HEIGHT_rectangle = 250
QUESTION_POS = (150, 125)

QUIZ_IS_OVER = False

SLEEPING_TIME_BETWEEN_QUESTIONS = 500 #ms
class QuizInterface:
    def __init__(self, question_data):
        #QUIZ
        self.quiz = QuizBrain(question_data)

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        #CANVAS
        self.canvas = Canvas(width=WIDTH_rectangle, height=HEIGHT_rectangle, highlightthickness=0, bg="white")

        self.question_displayed = self.canvas.create_text(QUESTION_POS, text="Question", font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)  # , padx=20, pady=20

        #BUTTONS
        image_true = PhotoImage(file="images/true.png")
        self.button_true  = Button(image=image_true, bg=THEME_COLOR, highlightthickness=0,
                                   command=lambda: self.answer_commande("True"))

        self.button_true.grid(column= 1, row=2, columnspan=1, padx=PADX, pady=PADY)

        image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=image_false, bg=THEME_COLOR, highlightthickness=0,
                                   command=lambda: self.answer_commande("False"))

        self.button_false.grid(column=0, row=2, columnspan=1, padx=PADX, pady=PADY)

        #LABEL
        self.score = 0
        self.score_label = Label(text=f"Score : {self.score} / {self.quiz.question_number}",
                                 font=("Arial", 14), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        #MAIN
        self.iterate_quiz_questions()


        self.window.mainloop()


    def display_question(self, question):
        self.canvas.config(bg="white")
        question = f"Q.{self.quiz.question_number}: {question}"
        self.canvas.itemconfig(self.question_displayed, text = question, width=WIDTH_rectangle-20)

    def iterate_quiz_questions(self):
        if self.quiz.still_has_questions():  # QUIZ interface
            question = self.quiz.next_question()
            self.display_question(question)

        else:
            self.canvas.config(bg="white")
            self.canvas.update()
            result = f"Your final score is :\n {self.score} / {self.quiz.question_number}"
            self.canvas.itemconfig(self.question_displayed, text=result, width=WIDTH_rectangle)



    def true_commande(self):
        global QUIZ_IS_OVER
        print(f"quiz over : {QUIZ_IS_OVER}")
        if not QUIZ_IS_OVER :
            #Update the score
            self.score += self.quiz.check_answer("True")
            self.score_label.config(text=f"Score : {self.score} / {self.quiz.question_number}")

            QUIZ_IS_OVER = self.quiz.question_number >= len(self.quiz.question_list)

        # Next question
        self.iterate_quiz_questions()


    def false_commande(self):
        global QUIZ_IS_OVER
        print(f"quiz over : {QUIZ_IS_OVER}")
        if not QUIZ_IS_OVER:
            # Update the score
            self.score += self.quiz.check_answer("False")
            self.score_label.config(text=f"Score : {self.score} / {self.quiz.question_number}")

            QUIZ_IS_OVER = self.quiz.question_number == len(self.quiz.question_list)

        # Next question
        self.iterate_quiz_questions()

    def answer_commande(self, answer):
        global QUIZ_IS_OVER

        if not QUIZ_IS_OVER:
            # Update the score
            self.score += self.quiz.check_answer(answer)
            self.score_label.config(text=f"Score : {self.score} / {self.quiz.question_number}")

            #Change background canvas red or green
            if self.quiz.check_answer(answer)==1:
                self.canvas.config(bg="#00FF00") #clear green
                self.canvas.update()

            else:
                self.canvas.config(bg="red")
                self.canvas.update()

            # update QUIZ_IS_OVER
            QUIZ_IS_OVER = self.quiz.question_number == len(self.quiz.question_list)

        # Next question
        self.window.after(SLEEPING_TIME_BETWEEN_QUESTIONS, self.iterate_quiz_questions)
