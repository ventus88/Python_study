# if조건문 6문제

import random

game = {1: "가위", 2: "바위", 3: "보"}
user = int(input("1:가위, 2:바위, 3:보  중 숫자로 선택하세요: "))
randomA = random.randint(1,3)

if user == 1 and randomA ==3 or user == 2 and randomA ==1 or user ==3 and randomA ==2:
    print("사용자 승리")
elif randomA == 1 and user == 3 or randomA == 2 and user == 1 or randomA == 3 and user == 2:
    print("컴퓨터 승리")
else:
    print("비겼습니다")

print("사용자 :",game[user], "컴퓨터 :",game[randomA])