# goal: 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   k는 1 이상 number의 자릿수 미만인 자연수입니다.

from collections import deque

def solution(number, k):
    answer = []
    comparator = []
    deleted = 0

    # split element
    number = deque([x for x in number])

    # if length of number is 1, then return number[0]
    if len(number) == 1:
        return number[0]

    # while length of number is not 0
    while len(number) > 0 and deleted != k:

        # add elements to comparator
        #   if element exists in answer, then pop the latest element and add to comparator, and leftmost element from number
        if len(answer) != 0:
            comparator.append(answer.pop())
            comparator.append(number.popleft())
        #   if element doesn't exist in answer, then pop two elements from number
        else:
            comparator.append(number.popleft())
            comparator.append(number.popleft())
        print(comparator)
        # if first element is larger than second element, discard second
        if comparator[0] > comparator[1]:
            comparator.pop()
            deleted += 1
        # if first element is smaller than second element, discard first
        elif comparator[0] < comparator[1]:
            comparator.pop(0)
            deleted += 1
        # if first element is same then keep both
        # pop the resulting element from comparator and add to answer
        answer.extend(comparator)
        comparator = []

        print(answer)
        print("------")

    answer.extend(list(number))
    answer = "".join(answer)
    return answer

if __name__ == "__main__":
    print(solution("1924", 2)) #94
    print(solution("1231234", 3)) #3234
    print(solution("4177252841", 4)) #775841