total = 0 # 잘못 입력한 횟수를 누적하는 변수
while True:  # 계속 반복(무한루프)
    user = input("주민번호를 입력하세여요 ex)550830-1239874")
    if len(user) == 14:  # 주민번호가 14자리(올바른 입력)인지 먼저 확인
        gender = user[7]  # 뒷자리 첫 번째 숫자로 성별 확인
        old = user[:2]  # 앞 두 자리는 출생 연도의 마지막 두 자리
        old_int = int(old)  # 출생 연도를 정수로 변환 (비교용)
        # 출생 연도에 따라 2000년대/1900년대 구분 후 나이 계산
        if old_int < 25:  # 2000년 ~ 2024년생
            yyyy = "20"+old   # 출생 연도 앞에 '20'을 붙여 2000년대 4자리 연도로 만듦 (예: '01' → '2001') 
            print(f"당신의 나이는 {(2025+1-int(yyyy))}세")  # 2026년 기준 한국식 나이
        else:
            yyyy = "19"+old
            print(f"당신의 나이는 {(2025+1-int(yyyy))}세")
        # 성별 과련
        if gender in ["1","3"]: 
            print("남자 입니다")
        elif gender in ["2","4"]:
            print("여자 입니다")
        else:
            print("성별 입력이 잘못 되었습니다")
        break  # 문제 없이 적을 경우 브레이크 시켜주는곳
    else: 
        print("주민번호가 맞지 않습니다")
        total += 1 
        print(f"다시 입력한 횟수 : {total}")
           
        user2 = input("종료 하실려면 yes 계속 하실려면 아무키나 누르세요")
        if user2.lower() == "yes":
            print("안녕히 가십시오")
            break
        else: 
            print("다시 시작 합니다")