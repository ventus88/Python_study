#파이썬 숙제 정수 문제 7번

x1 = int(input("x1 값을 입력하세요"))
x2 = int(input("x2 값을 입력하세요"))
y1 = int(input("y1 값을 입력하세요"))
y2 = int(input("y2 값을 입력하세요"))

x3 = (x1-x2)**2
y3 = (y1-y2)**2
x3y3 = x3 + y3

print("두 점 사이의 거리는:", round(x3y3**0.5))
