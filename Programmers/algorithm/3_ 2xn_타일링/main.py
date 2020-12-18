# goal: 직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return
# 하는 solution 함수를 완성해주세요.

# 타일을 가로로 배치 하는 경우
# 타일을 세로로 배치 하는 경우


# Example
#  1)
#      V V V V --> possible
#      V V 2H --> possible
#      V 2H V --> possible
#      2H V V --> possible
#      V 2H H --> not possible
#      2H H V --> not possible
#      2H 2H --> possible


# Pseudocode
#  1) For each combination starting with n-i many Vs and i many 2Hs (until there are 0 many Vs)
#  2) check if such formation is valid
#  3) Create permutations of V and 2H
#  4) Add it's length to count
#  3) increase i and continue

# Creating a permutation
#

from itertools import combinations

def solution(n):
    answer = 0
    return answer