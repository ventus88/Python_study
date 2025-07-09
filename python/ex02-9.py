#if 조건문 9번 문제

import random

rum1 = random.randrange(1,10)
rum2 = random.randrange(1,10)
rangame = random.randint(4)

if rangame == 1:
    addition = rum1+rum2
    userr = int(input("{0}+{1}은 무엇입니다" .format(rum1,rum2)))
    if userr == addition :
     re = "더하기 값에 대한 문제가 정답입니다"
    else:
     re = "더하기 값에 대한 문제가 틀렸습니다"
if rangame == 2:
    addition = rum1-rum2
    userr = int(input("{0}-{1}은 무엇입니다" .format(rum1,rum2)))
    if userr == addition :
     re = "빼기 값에 대한 문제가 정답입니다"
    else:
     re = "빼기 값에 대한 문제가 틀렸습니다"
if rangame == 3:
    addition = rum1*rum2
    userr = int(input("{0}x{1}은 무엇입니다" .format(rum1,rum2)))
    if userr == addition :
     re = "곱하기 값에 대한 문제가 정답입니다"
    else:
     re = "곱하기 값에 대한 문제가 틀렸습니다"

if rangame == 4:
    addition = rum1/rum2
    userr = float(input("{0}/{1}은 무엇입니다" .format(rum1,rum2)))
    if userr == addition or round(userr ,2) == round(addition ,2):
     re = "나누기 값에 대한 문제가 정답입니다"
    else:
     re = "나누기 값에 대한 문제가 틀렸습니다"

print(re)