class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, quiz_number):
        print(f"\nQ.{quiz_number}: {self.question}")
        for number, choice in enumerate(self.choices, 1):
            print(f"   {number}) {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer