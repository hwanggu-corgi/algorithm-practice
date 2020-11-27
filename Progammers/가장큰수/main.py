# Goal: 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#   - numbers의 길이는 1 이상 100,000 이하입니다.
#   - numbers의 원소는 0 이상 1,000 이하입니다.
#   - 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다

# Example
#  [6, 10, 2]
#   - {1: [10], 2:[2], 3:[], 4:[], 5:[], 6:[6], 7:[], 8:[], 9:[]}

# Place number

from collections import deque

def solution(numbers):
    # convert all to string
    temp = {}
    # sort array
    numbers.sort()
    # convert all number to string
    numbers = [str(x) for x in numbers]

    # place numbers in dictionary
    for number in numbers:
        if number[0] not in temp:
            temp[number[0]] = deque([number])
        else:
            temp[number[0]].append(number)

    # form largest number in string
    #   iterate from 9 to 0

    answer = ''
    return answer