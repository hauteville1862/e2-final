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

    def wait_for_enter(self):
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")

    def run_quiz(self):
        data = self.storage.load()

        if not data["quizzes"]:
            print("\n[알림] 등록된 문제가 없습니다. 문제를 먼저 추가해주세요!")
            self.wait_for_enter()
            return

        quiz_bank = []
        for quiz_data in data["quizzes"]:
            quiz_bank.append(
                Quiz(quiz_data["question"], quiz_data["choices"], quiz_data["answer"])
            )

        game = QuizGame(quiz_bank)
        while game.still_has_quizzes():
            current_quiz = game.get_current_quiz()

            current_quiz.show(game.quiz_number + 1)

            user_answer = self.get_valid_int("\n정답을 입력하세요 (1-4): ", 1, 4)

            if game.submit_answer(user_answer):
                print("정답입니다!")
            else:
                print("틀렸습니다.")
                print(f"정답은 {current_quiz.answer}번이었습니다.")

            print(f"현재 점수: {game.score}/{game.quiz_number}")

        print("\n" + "=" * 30)
        print(f"퀴즈 종료! 최종 점수: {game.score}/{len(quiz_bank)}")

        data["play_count"] += 1

        if game.score > data["best_score"]:
            print(f"최고 점수 갱신! ({data['best_score']} -> {game.score})")
            data["best_score"] = game.score

        if not self.storage.save(data):
            print("[알림] 기록을 저장하지 못했습니다.")

        print("=" * 30)
        self.wait_for_enter()

    def add_new_quiz(self):
        print("[새 문제 추가]")

        question = input("문제 내용을 입력하세요: ").strip()
        while question == "":
            print("[알림] 문제 내용은 비어 있을 수 없습니다.")
            question = input("문제 내용을 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"보기 {i}번을 입력하세요: ").strip()
            while choice == "":
                print("[알림] 보기 내용은 비어 있을 수 없습니다.")
                choice = input(f"보기 {i}번을 입력하세요: ").strip()
            choices.append(choice)

        answer = self.get_valid_int("정답 번호를 입력하세요 (1-4): ", 1, 4)

        data = self.storage.load()
        data["quizzes"].append(
            {"question": question, "choices": choices, "answer": answer}
        )

        if self.storage.save(data):
            print("\n문제가 성공적으로 추가되었습니다!")
        else:
            print("\n[알림] 문제를 저장하지 못해 추가가 취소되었습니다.")

        self.wait_for_enter()

    def view_quiz_list(self):
        data = self.storage.load()
        print("[등록된 퀴즈 목록]")

        if not data["quizzes"]:
            print("등록된 문제가 없습니다.")
        else:
            for number, quiz_data in enumerate(data["quizzes"], 1):
                print(f"{number}. {quiz_data['question']}")

        print("-" * 30)
        self.wait_for_enter()

    def show_best_score(self):
        data = self.storage.load()
        print("[현재 최고 점수]")

        if data["play_count"] == 0:
            print("\n아직 퀴즈를 풀지 않아 기록이 없습니다.")
            print("\n퀴즈를 풀고 첫 기록을 남겨보세요!")
        else:
            print(f"\n현재까지의 최고 기록은 {data['best_score']}점입니다.")
            print(f"지금까지 {data['play_count']}번 풀었습니다.")
            print("\n더 높은 점수에 도전해보세요!")

        print("-" * 30)
        self.wait_for_enter()

    def main_menu(self):
        while True:
            print("=" * 40)
            print("      세계 문학 작가 퀴즈")
            print("=" * 40)
            print("  1. 퀴즈 시작")
            print("  2. 퀴즈 추가")
            print("  3. 퀴즈 목록 보기")
            print("  4. 최고 점수 확인")
            print("  5. 종료")
            print("-" * 40)

            choice = self.get_valid_int("메뉴를 선택하세요 (1-5): ", 1, 5)

            if choice == 1:
                self.run_quiz()
            elif choice == 2:
                self.add_new_quiz()
            elif choice == 3:
                self.view_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                print("\n게임을 종료합니다. 이용해주셔서 감사합니다!")
                break
