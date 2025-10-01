from datetime import datetime

class BankInterface:
    def __init__(self, per, acc, main):
        self.per = per
        self.acc = acc
        self.main = main

    # 로그인 전 인터페이스 기능
    def main_interface(self):
        while True:
            now = datetime.now()
            if self.per.current_login == 0:
                print("")
                print(f"현재 시간은 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 입니다.")
                print("-----------------------------------------")
                print("| [메뉴] 0: 회원가입 | 1: 로그인 | 9: 종료 |")
                print("-----------------------------------------")
                choice = input("번호를 입력하세요: ").strip()
                if not self.main.login_main(choice):
                    break


            else:
                print("")
                print(f"현재 시간은 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 입니다.")
                print("----------------------------------------------------")
                print("| [메뉴] 0: 회원가입 | 1: 로그아웃 | 2: 계좌 | 9: 종료 |")
                print("----------------------------------------------------")
                choice = input("번호를 입력하세요: ").strip()
                if choice == "2":
                    self.account_interface()
                else:
                    if not self.main.logout_main(choice):
                        break

    # 로그인 후 2번을 누르면 나오는 계좌 관련 인터페이스
    def account_interface(self):
        while True:
            print("")
            print("----------------------------------------------------------------------")
            print("| [계좌] 0: 조회 | 1: 개설 | 2: 삭제 | 3: 이체 | 4. 입/출금 | 9. 뒤로가기 |")
            print("----------------------------------------------------------------------")
            choice = input("번호를 입력하세요: ")
            if not self.main.account_main(choice):
                break