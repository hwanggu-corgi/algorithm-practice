# goal: 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수,
# solution을 완성해 주세요.

# 제한사항
#   - * n은 1이상, 100000이하인 자연수입니다.

def solution(n):
    answer = 0
    hash = {}

    fib = _solution(n, hash)

    return fib % 1234567

def _solution(n, hash):

    if n == 0 or n == 1:
        return n

    if n in hash:
        return hash[n]

    return _solution(n-1) + _solution(n-2)