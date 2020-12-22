# goal: 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

def solution(n):
    answer = 0
    for i in range(2,n+1):
        answer += 1 if is_prime(i) else 0
    return answer

def is_prime(n):
    if n == 2:
        return True

    for i in range(2,n):
        if n % i == 0:
            return False
    return True