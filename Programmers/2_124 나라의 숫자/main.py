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
#       - 1 -> 1 -> 1
#       - 2 -> 2 -> 2
#       - 3 -> 10 -> 4
#       - 4 -> 11 -> 11
#       - 5 -> 12 -> 12
#       - 6 -> 20 -> 14
#       - 7 -> 21 -> 20
#       - 8

#   1. 2진법
#       - 1 -> 1 -> 1
#       - 2 -> 10 -> 2
#       - 3 -> 11 -> 4
#       - 4 -> 100 -> 4
#       - 5 -> 11 -> 4
#       - 6 -> 11 -> 4
#       - 7 -> 11 -> 4
# ...
#       - 10 -> 1010 -> 41
#       - 11 -> 1011 -> 42
#       - 12 -> 1100 -> 44
#       - 13 -> 1101 -> 111

def solution(n):
    answer = ''
    return answer