# goal: 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   k는 1 이상 number의 자릿수 미만인 자연수입니다.

def solution(number, k):
    answer = ''

    # add elements to comparator
    #   if element exists in answer, then pop the latest element and add to comparator, and leftmost element from number
    #   if element doesn't exist in answer, then pop two elements from number

    # if first element is larger than second element, discard second
    # if first element is smaller than second element, discard first
    # pop the resulting element from comparator and add to answer
    return answer