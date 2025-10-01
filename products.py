import random
from bank_system_fixed import BankStorage
from bank_system_fixed import BankSystem


class Product:
    def __init__(self, system):
        self.system = system
        # bank_system_fixed의 interface를 불러오고싶어

    def product1(self):
        # 로그인 체크
        if not self.system.current_login:
            print("로그인 후 이용 가능합니다.")
            return False

        user = self.system.find_user(self.system.current_user_id)
        if not user:
            print("사용자 정보를 찾을 수 없습니다.")
            return False

        # 사용자 계좌 선택 (여기서는 첫 번째 계좌 기준)
        if not user["accounts"]:
            print("사용자의 계좌가 없습니다.")
            return False

        account = user["accounts"][0]
        acc_number = list(account.keys())[0]

        # 잔액 확인
        if account[acc_number] < 100:
            print("잔액이 부족합니다. (최소 100원 필요)")
            return False

        # 100원 차감
        account[acc_number] -= 100
        choice = input("상품을 구매하시겟습니까? 1.구매한다 2.처음으로 돌아간다. : ")
        if choice != "1":
            print("구매를 취소하셧습니다.")
            return False

        # 랜덤 리워드 (0~300원)
        reward = random.randint(0, 300)
        account[acc_number] += reward

        # 결과 저장
        self.system.storage.save(self.system.db)

        print(f"상품 구매 완료! 100원을 사용했습니다.")
        print(f"리워드: {reward}원 획득")
        print(f"현재 계좌({acc_number}) 잔액: {account[acc_number]}원")
        return True

    def product2(self):
        

if __name__ == "__main__":
    storage = BankStorage("bank.json")
    bank = BankSystem(storage)
    product = Product(bank)


    if bank.login():  # 로그인 먼저
        product.product1()  # 상품 구매
