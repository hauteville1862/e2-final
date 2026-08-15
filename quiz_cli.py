from quiz import Quiz
from quiz_game import QuizGame
from storage import Storage


class QuizCLI:
    def __init__(self):
        self.storage = Storage()

    def get_valid_int(self, prompt, min_value, max_value):
        while True:
            raw = input(prompt).strip()

            if raw == "":
                print("[알림] 입력이 비어 있습니다. 다시 입력해주세요.")
                continue

            try:
                value = int(raw)
            except ValueError:
                print("[알림] 숫자만 입력 가능합니다.")
                continue

            if value < min_value or value > max_value:
                print(f"[알림] {min_value}~{max_value} 사이의 숫자를 입력해주세요.")
                continue

            return value

    def run_quiz(self):
        data = self.storage.load()

        if not data["questions"]:
            print("\n[알림] 등록된 문제가 없습니다. 문제를 먼저 추가해주세요!")
            input("\n엔터를 누르면 메뉴로 돌아갑니다...")
            return

        question_bank = []
        for q in data["questions"]:
            question_bank.append(Quiz(q["question"], q["choices"], q["answer"]))

        quiz = QuizGame(question_bank)
        while quiz.still_has_questions():
            current_question = quiz.get_current_question()

            current_question.show(quiz.question_number + 1)

            user_answer = self.get_valid_int("\n정답을 입력하세요 (1-4): ", 1, 4)

            if quiz.submit_answer(user_answer):
                print("정답입니다!")
            else:
                print("틀렸습니다.")
                print(f"정답은 {current_question.answer}번이었습니다.")

            print(f"현재 점수: {quiz.score}/{quiz.question_number}")

        print("\n" + "="*30)
        print(f"퀴즈 종료! 최종 점수: {quiz.score}/{len(question_bank)}")

        if quiz.score > data["high_score"]:
            print(f"최고 점수 갱신! ({data['high_score']} -> {quiz.score})")
            data["high_score"] = quiz.score
            self.storage.save(data)

        print("="*30)
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")

    def main_menu(self):
        while True:
            print("="*40)
            print("      세계 문학 작가 퀴즈")
            print("="*40)
            print("  1. 퀴즈 시작")
            print("  2. 퀴즈 추가")
            print("  3. 퀴즈 목록 보기")
            print("  4. 최고 점수 확인")
            print("  5. 종료")
            print("-"*40)

            choice = self.get_valid_int("메뉴를 선택하세요 (1-5): ", 1, 5)

            if choice == 1:
                self.run_quiz()
            elif choice == 2:
                print("준비 중입니다.")
            elif choice == 3:
                print("준비 중입니다.")
            elif choice == 4:
                print("준비 중입니다.")
            elif choice == 5:
                print("\n게임을 종료합니다. 이용해주셔서 감사합니다!")
                break
