def delete_account(self):
    if not self.current_login:
        print("로그인 후 이용 가능합니다.")
        return False

    user = self.find_user(self.current_user_id)
    if not user:
        print("사용자 정보를 찾을 수 없습니다.")
        return False

    if not user["accounts"]:
        print("삭제할 계좌가 없습니다.")
        return False

    print(f"\n[{user['name']}]님의 계좌 목록")
    for i, account in enumerate(user["accounts"], 1):
        for account_num, balance in account.items():
            print(f"{i}. 계좌번호: {account_num} | 잔액: {balance}원")

    account_number = input("삭제할 계좌번호를 입력하세요: ").strip()

    for account in user["accounts"]:
        if account_number in account:
            if account[account_number] > 0:
                confirm = input("계좌에 잔액이 있습니다. 그래도 삭제하시겠습니까? (y/n): ")
                if confirm.lower() != "y":
                    print("삭제를 취소했습니다.")
                    return False
            user["accounts"].remove(account)
            self.storage.save(self.db)  # 삭제 후 저장
            print(f"계좌 {account_number}가 삭제되었습니다.")
            return True

    print("해당 계좌번호를 찾을 수 없습니다.")
    return False