# if조건문 6문제

import random

chois = ['가위',"바위","보"]
computer = chois[random.randint (0,2)]
user = input("가위,바위,보 중에 고르시오 ")

if user == '가위':      
     if computer == '가위':
          re = '비겼습니다'
     elif computer == '바위':
          re = '컴퓨터가 이겼습니다'
     else:
          re = '유저가 이겼습니다'
elif user == '바위':
     if computer == '바위':
          re = '비겼습니다'
     elif computer == '보':
          re = '컴퓨터가 이겼습니다'
     else:
          re = '유저가 이겼습니다'
elif user == '보':
     if computer == '보':
          re = '비겼습니다'
     elif computer == '가위':
          re = '컴퓨터가 이겼습니다'
     else:
          re = '유저가 이겼습니다'

print(f"{re}")
print("서로 낸 것은? " "사용자 :",user, "컴퓨터 :",computer)