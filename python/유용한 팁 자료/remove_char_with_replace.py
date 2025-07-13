# remove_char_with_replace.py
# ----------------------------------------------
# 특정 문자(letter)를 문자열(my_string)에서 제거하는 함수
# - 파이썬의 문자열 내장 메서드 replace()를 활용
# - my_string.replace(letter, '') : letter가 빈 문자로 치환(= 제거)
# - 반복문 없이 한 줄로 아주 간단하게 처리 가능
# ----------------------------------------------

def solution(my_string, letter):
    return my_string.replace(letter, '')

# 테스트 예시
print(solution("abcdef", "f"))    # 출력: abcde
print(solution("BCBdbe", "B"))    # 출력: Cdbe