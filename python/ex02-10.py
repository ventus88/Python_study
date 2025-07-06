user = float(input("x 값 하나를 입력하세여"))

if user > 0:
    re = 7*user+2
elif user <= 0:
    re = 2*user**2-9*user+2

print(round(re))