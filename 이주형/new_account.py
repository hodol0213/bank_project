def new_account(self):
    # 로그인 체크
    if not self.personal.current_login:
        print("로그인 후 이용 가능합니다.")
        return False
    # id 기반으로 db에서 사용자 검색
    user = self.personal.find_user(self.personal.current_user_id)

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
            if exist:
                break

        if not exist:
            break

    now = datetime.datetime.now()
    # 사용자 계좌에 추가 + bal 0
    user["accounts"].append({formatted_number: 0})

    # db에 저장
    try:
        self.storage.save(self.personal.db)
    except Exception as e:
        print("저장 중 오류가 발생했습니다:", e)
        return False

    print(f"새 계좌가 생성되었습니다. 계좌번호: {formatted_number}, 생성일: {now}")
    return True