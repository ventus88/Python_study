import random

ran_sentence = [["호기심 많은 마음은 새로운" , "문을 연다."], 

                ["짧은 길에도" ,"울퉁불퉁함은 있다."], 

                ["따뜻한 말 한마디가 가장" , "추운 날도 녹인다."], 

                ["노력이라는 물을 주면" , "꿈도 빨리 자란다."], 

                ["조용한 친구가 가장 큰" , "울음도 들어준다."], 

                ["구름마다 저마다의" , "이야기를 품고 있다."], 

                ["인내는 성공을" , "그리는 붓이다."], 

                ["작은 불씨 하나가 천 개의" , "촛불을 밝힌다."], 

                ["신뢰는 쌓는 것이지," , "사는 게 아니다."], 

                ["새로운 길은 작은" , "질문에서 시작된다."]]  

score = 0
tries = 0

for total in range(5):
    front, back = random.choice(ran_sentence)

    print(f"속담:\"{front}____\"")
    answer = input("끝부분을 입력해주세요").strip()

# conunt = 0
# for i in range(min(len(back),len(answer))):
#          if back[i] == answer[i]:
#             conunt += 1
#          else:
#              print("정답 입니다")


    if answer == back:
        print("정답입니다\n")
        score += 1
        break
    else:
        hint = back[0]
        lenght = len(back)
        print(f"오답입니다 힌트는: {hint} 글자수는: {lenght}")
        answer = input("힌트를 보고 다시 입력하세요").strip()
        if answer == back:
            print("정답입니다\n")
            score += 1
        else:
            print(f"오답입니다. 정답은: \"{back}\"\n")
        
        
total =+ 1
print(f"총 맞춘 시도:{total}")
print(f"맞춤 개수:{score}")