import time
import random

wods= ["사과", "바나나", "포도" , "복숭아", "태블랏"]

score= 0
life = 3
speed = 2

print("한글 타자 시작")
print("제한 시간 내에 정확히 입력하세요")
print("기회는 3번! 시작합니다....\n")

while life > 0:
    targer = random.choice(wods)
    print(f"제시어: {targer}")

    start = time.time()
    user_input = input("입력: ").strip()
    end = time.time()

    elspsed = end - start

    if elspsed > speed:
        print(f"시간 초과({elspsed:.1f}초)")
        life -= 1
    elif user_input != targer:
        print("오타! 정확히 입력해야 해요.")
        life -= 1
    else:
        print("성공!")
        score += 1
    
    print(f"남은 목숨 : {life}, 점수: {score}, 제한시간 : {speed:.1f}초\n")
    time.sleep(1)

print("\n게임 종료!")
print(f"최종 점수: {score}")