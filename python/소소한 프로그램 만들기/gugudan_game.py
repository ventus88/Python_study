import random
import time


score = 0
life = 3

print(f"목숨이 {life}개이니 신중히 써주시길 바랍니다")
while True:
    
        try:
            dan = random.randint(2,9)
            so = random.randint(1,9)
            ok = dan*so
            user = int(input(f"컴퓨터가 {dan}x{so} = 정답은?"))
            
            if ok == user : 
                print("사용자 정답입니다")
                score += 1
                print(f"현재 스코어는 {score}점 입니다.")
            else:
                print("틀렸습니다")
                life -= 1
                print (f"목숨이 {life}개 남았습니다")
                print(f"현재 스코어는 {score}점 입니다.")
        except ValueError:
            print("숫자만 입력해주세요")
        if life == 0:
             break
        user2 = input("게임을 다시 시작하실려면 엔터 / 종료는 yes를 입력하세여")
        if user2.lower() == "yes":
             break
             
            
time.sleep(2)
print(f"수고하셨습니다.\n최종 스코어는 {score}점 입니다")