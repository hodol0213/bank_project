# 은행 계좌 관리 시스템

from bank_deposit import deposit
from bank_withdraw import withdraw

def main():
    while True:
        print("===== 세종은행 시스템 =====")
        print("1. 입금")
        print("2. 출금")
        print("0. 종료")
        choice = input("선택: ")

        if choice == "1":
            user_name = input("사용자명을 입력하세요: ")
            deposit(user_name)
        elif choice == "2":
            user_name = input("사용자명을 입력하세요: ")
            withdraw(user_name)
        elif choice == "0":
            print("수고하셨습니다. 시스템을 종료합니다. \n 즐거운 날들 되시기 바랍니다.!!!")
            break
        else:
            print("번호를 잘못 선택하셨습니다.\n")

if __name__ == "__main__":

    main()