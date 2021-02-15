# goal: 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는
# 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   numbers는 길이 1 이상 7 이하인 문자열입니다.
#   numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#   013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import permutations

def solution(numbers):
    n = len(numbers)
    perm_set = set()
    i = 1
    while i <= n:
        perm_list = permutations(numbers, i)
        for e in perm_list:
            number = int("".join(e))
            if is_prime(number):
                perm_set.add(number)
        i += 1

    answer = len(perm_set)
    return answer

def is_prime(n):
    if n == 1 or n == 0:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    print(solution("17")) #3
    print(solution("011")) #2