#성별 과 나이를 알려주는 프로그램


total = 0 
while True:  
    user = input("주민번호를 입력하세여요 ex)550830-1239874 : ")
    if len(user) == 14:  
        gender = user[7]  
        old = user[:2]  
        old_int = int(old)  
      
        if old_int < 25:  
            yyyy = "20"+old    
            print(f"당신의 나이는 {(2025+1-int(yyyy))}세")  
        else:
            yyyy = "19"+old
            print(f"당신의 나이는 {(2025+1-int(yyyy))}세")
        if gender in ["1","3"]: 
            print("남자 입니다")
        elif gender in ["2","4"]:
            print("여자 입니다")
        else:
            print("성별 입력이 잘못 되었습니다")
        break  
    
    else: 
        print("주민번호가 맞지 않습니다")
        total += 1 
        print(f"다시 입력한 횟수 : {total}")
           
        user2 = input("종료 하실려면 yes 계속 하실려면 아무키나 누르세요 : ")
        if user2.lower() == "yes":
            print("안녕히 가십시오")
            break
        else: 
            print("다시 시작 합니다")