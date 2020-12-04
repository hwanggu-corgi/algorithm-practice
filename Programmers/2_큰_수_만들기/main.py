#goal: number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   - k는 1 이상 number의 자릿수 미만인 자연수입니다.

from collections import deque

def solution(number, k):
    answer = ''

    # convert number to queue
    number_list = [x for x in number]

    # find biggest number after removing k
    current_i = 0
    while k > 0:

    # return result
    return answer