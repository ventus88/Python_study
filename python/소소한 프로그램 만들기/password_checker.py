# 비밀번호 맞추기 프로그램

Error = 0
Error_ex = 5
pas_w = 3456
while True:
    try:
        id_p = int(input("패스워드를 입력하세요"))
        if id_p == pas_w :
            print("비밀 번호가 맞아서 프로그램을 종료합니다")
            break
        elif id_p != pas_w :
            Error += 1
            print("비밀 번호가 맞지 않습니다")
            if Error == Error_ex:
                print("5회 초과 하여 프로그램을 종료 합니다")
                break
            
    except ValueError:
        Error += 1
        print("숫자를입력하세요")
        if Error == Error_ex:
            print("5회 초과 하여 프로그램을 종료 합니다")
            break
