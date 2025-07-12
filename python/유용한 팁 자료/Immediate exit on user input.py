#  “사용자가 특정 값을 입력하면 프로그램을 즉시 종료하고,
#  그 외에는 계속 실행하는 조건 분기 방식”

import sys

while True:
    ex = input("종료하실려면 0번을 입력해주세요 or 계속 하실려면 아무키나 적으세요")
    if ex == "0":
        sys.exit()
        break