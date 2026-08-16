class QuizGame:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.score = 0
        self.quiz_list = quiz_list

    def still_has_quizzes(self):
        return self.quiz_number < len(self.quiz_list)

    def get_current_quiz(self):
        return self.quiz_list[self.quiz_number]

    def submit_answer(self, user_answer):
        is_correct = self.get_current_quiz().is_correct(user_answer)
        self.quiz_number += 1

        if is_correct:
            self.score += 1

        return is_correct
