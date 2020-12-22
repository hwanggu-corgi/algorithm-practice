# goal: 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

def solution(n):
    answer = 0
    sieve = [1] * (n+1)
    sieve[0] = sieve[1] = 0

    i = 2
    while i * i <= n:

        if sieve[i] == 1:
            k = i * i
            while k <= n:
                sieve[k] = 0
                k += i
        i += 1

    return sum(sieve)



# def solution(n):
#     answer = 0
#     for i in range(2,n+1):
#         answer += 1 if is_prime(i) else 0
#     return answer

# def is_prime(n):
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

if __name__ == "__main__":
    print(solution(10)) #4
    print(solution(5)) #3