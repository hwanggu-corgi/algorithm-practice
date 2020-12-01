# goal: 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록
# solution 함수를 완성해 주세요.

# 제한사항
#   - n은 500,000,000이하의 자연수 입니다.

# brute force method
#   - count
#       - on every 3rd number increment value right after
    #       - if the value after is 4, then append value of 1 after and reset prev count to 1
#   but is crazy inefficient

# Improved method
#   1. 3진법
#       - 1 / 3 = 0 && 1 % 3 = 1
#       - 2 / 3 = 0 && 2 % 3 = 2
#       - 3 / 3 = 1 && 3 % 3 = 0

#   1. 2진법
#       - 10/ 2 = 5 && 10 % 2 = 0
#       - 5 / 2 = 2 && 5 % 2 = 1 - 4
#       - 2 / 2 = 1 && 2 % 2 = 0
#       - 1 / 2 = 0 && 1 % 2 = 1 - 1

#       - 20 / 2 = 10 && 20 % 2 = 0
#       - 10 / 2 = 5 && 10 % 2 = 0


def solution(n):
    answer = ''
    return answer