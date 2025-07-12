#  숫자 쪼개기(자리수 추출) 방식
#  // (정수 나눗셈 연산자)
#  → 몫을 구할 때 사용
#  % (나머지 연산자, “modulo” 모듈로)
#  → 자리수(특정 위치의 숫자)를 “남긴다” 또는 “추출”할 때 사용

num = int(input("정수"))
print(num)

fourth = num//1000
third = (num%1000)//100
second = (num%100)//10
first = (num%10)

sum = fourth,third,second,first
print(sum)