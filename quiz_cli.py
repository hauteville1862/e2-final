class QuizCLI:
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
                print("준비 중입니다.")
            elif choice == 2:
                print("준비 중입니다.")
            elif choice == 3:
                print("준비 중입니다.")
            elif choice == 4:
                print("준비 중입니다.")
            elif choice == 5:
                print("\n게임을 종료합니다. 이용해주셔서 감사합니다!")
                break