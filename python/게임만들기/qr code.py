import random
import qrcode


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


question = random.sample(ran_sentence, len(ran_sentence))
for question, answer in question:
    print(f"속담:\"{question}____\"")
    
    img = qrcode.make(answer)
    img.save("show code")
    answer = input("끝부분을 입력해주세요").strip()
    print("정답이 담긴 QR코드가 저장 되었습니다")
    while True:
        cont  = input("계속 할까요? (y/n):  ").strip().lower()
        if cont in ("y" , "n"):
                break
        print("y 또는 n만 입력하세요")
    if cont == "n":
         print("프로그램을 종료합니다")
         break
        
