# 은행 입금 계좌 관리 시스템
import json

def deposit(user_name):
    # json 파일 읽어 오기
    with open("bank.json", "r", encoding="utf-8") as f:
        bank = json.load(f)
    cnt = 0
    for user in bank['users']:
        if user['name'] == user_name:
            # 사용자의 계좌번호 읽어 오기
            print (f"{bank['users'][cnt]['accounts'][cnt]}의 계좌 : {cnt}")
            cnt += 1
    # 사용자의 계좌가 한 건도 없는 경우 확인
    if cnt == 0:
        print("사용자명을 확인 바랍니다.\n")
        return
    try:
        n = input("입금할 계좌를 선택하세요:(0,1,2.. ")
        # 조회된 계좌수 보다 더 큰 번호를 선택한 경우 확인
        if  int(n) > (cnt - 1):
            print("계좌번호 선택 오류입니다..\n")
            return
    except ValueError:
        print("❌ 숫자를 입력해야 합니다.\n")
        return
    # 조회된 계좌수 보다 더 큰 번호를 선택한 경우 확인
    except IndexError:
        print("선택 오류입니다.\n")
        n = 0
        return
# int로 전환
    n = int(n)

    try:
        amount = int(input("입금할 금액을 입력하세요: "))
    except ValueError:
        print("❌ 숫자를 입력해야 합니다.\n")
        return
    # 계좌번호, 잔액
    account_dict = bank['users'][n]['accounts'][n]
    # 계좌번호
    account_number = list(account_dict.keys())[n]
    # 입금액 잔액 반영
    account_dict[account_number] += amount
    # json 파일 수정
    with open("bank.json", "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=4)
    print(f"{amount}원이 입금되었습니다.")
    # 잔액 재확인
    with open("bank.json", "r", encoding="utf-8") as f:
        bank = json.load(f)
    print(f"현재 잔액: {list(bank['users'][0]["accounts"][0].values())[0]}원\n")


if __name__ == "__main__":
    # user_name = input("사용자명을 입력하세요: ")
    deposit(user_name)