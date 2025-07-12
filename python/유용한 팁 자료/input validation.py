# 입력 검증(input validation) 반복문

while True:
        try:
            cash = int(input("숫자를 입력 안하시면 오류 생김"))
            break
        except ValueError:
            print("숫자만 입력해주세요")