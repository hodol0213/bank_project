import datetime
import random

# 계좌 관련 클래스
class BankAccount:
    def __init__(self, storage, personal):
        self.storage = storage
        self.db = self.storage.load()
        self.personal = personal

    # 계좌 조회
    def search(self, personal):
        # BankPersonal 최신화
        personal.db = self.storage.load()
        # id가 있으면 값 반환
        user = personal.find_user(personal.current_user_id)

        # user없으면 오류
        if not user:
            print("사용자를 찾을 수 없습니다.")
            return
        # 계좌 없으면 발생
        accounts = user.get("accounts", [])
        if not accounts:
            print("등록된 계좌가 없습니다.")
            return

        # 계좌 목록 확인
        print("계좌 목록:")
        for ac in accounts:
            for ac_no, balance in ac.items():
                print(f"- {ac_no}: {balance}원")

    # 계좌 개설
    def new_account(self, personal):

        ac_list = list()
        ac_list.append('{0:04d}'.format(random.randint(0, 10000)))
        ac_list.append('{0:02d}'.format(random.randint(0, 100)))
        ac_list.append('{0:04d}'.format(random.randint(0, 10000)))

        ac = '-'.join(map(str, ac_list))

        # 같은 계좌가 이미 있으면 안댐
        if personal.account_exists(ac):
            print("이미 존재하는 계좌번호입니다.")
            return False


        # 사용자 계좌에 추가
        self.db["accounts"].append({ac : 0})
        self.storage.save(self.db)
        print(f"새 계좌가 생성되었습니다. 계좌번호: {ac}")
        return True

    # 계좌 삭제
    def delete_account(self):
        pass

    # 계좌 이체
    def transfer_account(self):
        pass

    # 계좌 입/출금
    def deposit_and_withdrawal(self):
        pass