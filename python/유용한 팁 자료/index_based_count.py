# index_based_count.py
# ------------------------------------------
# 인덱스(index) 활용으로 짝수/홀수 개수 카운트
# even[0] = 짝수 개수, even[1] = 홀수 개수
# n % 2의 값(0/1)을 인덱스(주소)로 바로 사용
# ------------------------------------------

def solution(num_list):
    even = [0, 0]
    for n in num_list:
        even[n % 2] += 1
    return even

print(solution([1, 2, 3, 4, 5]))  # [2, 3]
print(solution([1, 3, 5, 7]))     # [0, 4]