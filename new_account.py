def new_account(self):
    # 로그인 체크
    if not self.current_login:
        print("로그인 후 이용 가능합니다.")
        return False

    user = self.find_user(self.current_user_id)
    if not user:
        print("사용자 정보를 찾을 수 없습니다.")
        return False

    # 새로운 계좌번호(랜덤 10자리) 생성 중복x
    while True:
        new_number = ''.join(map(str, np.random.randint(0, 10, size=10)))
        formatted_number = f"{new_number[:4]}-{new_number[4:6]}-{new_number[6:]}"

        exist = False
        for u in self.db["users"]:
            for acc in u["accounts"]:
                if formatted_number in acc:
                    exist = True
                    break

        if not exist:
            break
        else:
            print(f"중복된 계좌번호입니다.{formatted_number}, 새로운 계좌를 생성합니다.")

    now = datetime.datetime.now()

    # 사용자 계좌에 추가
    user["accounts"].append({formatted_number: 0})

    self.storage.save(self.db)

    print(f"새 계좌가 생성되었습니다. 계좌번호: {formatted_number}, 생성일: {now}")
    return True