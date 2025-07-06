# if조건문 5문제
x = int(input("첫 번째 정수를 입력하세요: "))
y = int(input("두 번째 정수를 입력하세요: ")) 
z = int(input("세 번째 정수를 입력하세요: "))

if x < y and x < z:
    ra = x
elif y < z and y < x :
    ra = y
else:
    ra = z

print(f"가장 작은 값은 {ra}")

# x < y, x < z
# y < z, y < x
# z < x, z < y
