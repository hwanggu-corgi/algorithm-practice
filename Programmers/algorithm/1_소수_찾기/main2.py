# goal: 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

def solution(n):
    answer = sieve(n).count(True)
    return answer

def sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    i = 2

    while (i * i <= n):
        if (sieve[i]):
            k = i * i
        while (k <= n):
            sieve[k] = False
            k += i
        i += 1

    return sieve

if __name__ == "__main__":
    print(solution(10)) #4
    print(solution(5)) #3