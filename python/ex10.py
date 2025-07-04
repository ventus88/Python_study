#1문제
in0 = int(input('첫번째 정수 하나를 입력하세여'))
in1 = int(input('두번째 정수 하나를 입력하세여'))
if in0 % in1 == 0:
    re = ("정수 입니다")
else:
    re = ("약수 입니다")
print(f"나오는 값은 {re}")