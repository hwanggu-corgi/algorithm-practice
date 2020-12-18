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
#  2) Create permutations of V and 2H
#  3) Add it's length to count
#  4) increase i and continue

# Creating a permutation
#
#
# n = 1 -> there is  1 combination (V)
# n = 2 -> there are 2 combinations ([V,V], [2H])
# n = 3 -> there are 3 combinations ([V,V,V], [2H,V], [V,2H])
# n = 4 -> there are 5 combinations ([V,V,V,V], [V,2H,V], [V,V,2H], [2H,V,V], [2H, 2H])

def solution(n):
    count = 0

    if n == 0 or n == 1 or n == 2:
        return n

    dp = [0] * (n+1)

    while

    return asnwer

# from itertools import permutations

# def solution(n):
#     count = 0

#     #  1) For each combination starting with n-i many Vs and i many 2Hs (until there are 0 many Vs)
#     i = 0
#     while i < (n+1):
#         number_of_2hs = i/2
#         number_of_vs = n - i

#         #  2) Check if 2H is valid
#         if number_of_2hs > 0 and number_of_2hs < 1:
#             continue

#         tiling = get_tiling(int(number_of_2hs), number_of_vs)
#         #  3) Create permutations of V and 2H
#         combs = permutations(tiling)
#         #  4) Add it's length to count
#         count += len(list(set(combs)))
#         #  5) increase i and continue
#         i += 2

#     return count

# def get_tiling(number_2h, number_v):
#     res = []

#     for i in range(number_2h):
#         res.append("2H")

#     for j in range(number_v):
#         res.append("V")

#     return res

if __name__ == "__main__":
    print(solution(3)) # 3
    print(solution(4)) # 5