import random 
import time
ran_sentence = ["부산이 좋아요",
                "파이썬은 재밌습니다",
                "김치사발면은 맛있습니다",
                "김치랑 삼겹살은 어울립니다",
                "공압이 더 재밌습니다",
                "게임을 만들어 봅시다",
                "유산소는 필수 입니다",
                "반복문 부터 다시 복습",
                "코드는 어떻게 짜야 쉬울것인가",
                "뭐를 더 해볼까나"
                 ]
print("타자 속도 테스트 입니다")
print("엔터를 누르면 문장이 나옵니다")


index = random.choice(ran_sentence)
print("다음 문장이랑 똑같이 적어주새요")
print(f"{index}\n")

input("준비되면 엔터를 누르세요")
try_count = 0

start_time = time.time()
trial = 0
while True:
      type = input("\n 입력:")

      end_time= time.time()
    
      elasped = end_time - start_time
     

   

      correct = 0
      for i in range(min(len(index),len(type))):
         if index[i] == type[i]:
            correct += 1

      total = max(len(index), len(type))
      accuracy = correct / len(index) * 100
      speed = len(type) / elasped*60
    
      if accuracy == 100:
         print('안료했습니다')
         break
      else:
         print("다시 시도해보세요")
      trial += 1

print("\n 결과")
print(f"걸린 시간은 : {elasped: .2f}초")
print(f"정확도는 : {accuracy: .2f}%")
print(f"타자 속도는 : {speed: .2f}자/분")
print(f"오타 횟수는 : {trial}회")

