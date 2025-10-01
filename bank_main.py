
# 다른 클래스들을 호출하는 클래스
class Main:
    def __init__(self, per, acc):
        self.per = per
        self.acc = acc

    def login_main(self, choice : str) -> bool:
        if choice == "0":
            self.per.join()
            return True
        elif choice == "1":
            self.per.login()
            return True
        elif choice == "9":
            print("종료합니다.")
            return False
        else:
            print("올바른 번호를 입력하세요.")
            return True

    def logout_main(self, choice):
        if choice == "0":
            self.per.join()
            return True
        elif choice == "1":
            self.per.logout()
            return True
        elif choice == "9":
            print("종료합니다.")
            return False
        else:
            print("올바른 번호를 입력하세요.")
            return True

    def account_main(self, choice):
        if choice == "0":
            self.acc.search(self.per)
            return True
        elif choice == "1":
            self.acc.new_account(self.per)
            return True
        elif choice == "2":
            self.acc.delete_account(self.per)
            return True
        elif choice == "3":
            self.acc.transfer_account(self.per)
            return True
        elif choice == "4":
            self.acc.deposit_and_withdrawal(self.per)
            return True
        elif choice == "9":
            return False
        else:
            print("올바른 번호를 입력하세요.")
            return True