# goal: 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요

from functools import reduce

def solution(x):

    digit_sum = reduce(lambda acc, b: acc + int(b), str(x), 0)

    if x % digit_sum == 0:
        return True
    return False

if __name__ == "__main__":
    print(solution(10)) #true
    print(solution(12)) #true
    print(solution(11)) #false
    print(solution(13)) #false