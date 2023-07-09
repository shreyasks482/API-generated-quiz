import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        correct_answer = self.current_question.answer
        wrong_options1 = self.current_question.options[0]
        wrong_options2 = self.current_question.options[1]
        wrong_options3 = self.current_question.options[2]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}", correct_answer, wrong_options1, wrong_options2, wrong_options3

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True, user_answer
        else:
            return False

