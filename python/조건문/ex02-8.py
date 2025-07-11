# if조건문 8문제

height = int(input("키를 입력해 주세여"))
weight = int(input("뭄무게를 입력해 주세여"))

ok = (height-100)*0.9



if  weight == round(ok) :
    
    ra = "표준 입니다"
elif weight > round(ok):
    
    ra = '과체중 입니다'
else:
    ra = '저체중 입니다'


print(f'{ra}')