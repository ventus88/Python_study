# if조건문 3문제

user = input('영어 문자 하나를 입력하세요')

if user == 'R' or user == 'r':
    r = "Rectangle"
elif user == 'C' or user == 'c':
    r = 'Circle'
else:
    r = 'Unknown'
print(f"{r}")

