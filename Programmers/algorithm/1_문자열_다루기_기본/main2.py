# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요

# 제한 사항
#   s는 길이 1 이상, 길이 8 이하인 문자열입니다

def solution(s):
    n = len(s)
    return s.isdigit() and (n == 4 or n == 6)