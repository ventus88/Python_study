# pip install 라이브러리이름(numpy)

# np.mean (평균값)
# 리스트, 배열 등 여러 값들의 평균값(산술 평균, 모든 값 더해서 개수로 나눈 값)을 구함

# 리스트 안에 평균값 구하는 공식

solution = [1,2,3,4,5,6,7,8,9,10]

re = sum(solution)/len(solution)

print(re)

###########################################

# 리스트 안에 평균값 구하는 공식(numpy 라이브러리 이용)

import numpy as up

solution = [1,2,3,4,5,6,7,8,9,10]
print(up.mean(solution))

############################################

#np.array (넘파이 배열 만들기)

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)         # 결과: array([1, 2, 3, 4, 5])
print(a + 10)    # 결과: array([11, 12, 13, 14, 15])