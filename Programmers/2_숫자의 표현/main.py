# goal: 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는
# solution를 완성해주세요.

# 제한사항
# n은 10,000 이하의 자연수 입니다.

# Example
#   - 15
#       1 + 2 + 3 + 4 + 5 = 15 (yes) 1
#       2 + 3 + 4 + 5 + 6 = 20 (no)
#       3 + 4 + 5 + 6 = 18 (no)
#       4 + 5 + 6 = 15 (yes) 2
#       5 + 6 + 7 = 19 (no)
#       6 + 7 + 8 = 21 (no)
#       7 + 8 = 15 (yes) 3
# ...
#       15 = 15 (yes) 4

# There's 4 in total

def solution(n):
    answer = 0
    return answer