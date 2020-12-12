# goal: 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를
# 완성해 주세요.

# - 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다

# 제한사항
# 행의 개수 N : 100,000 이하의 자연수
# 열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
# 점수 : 100 이하의 자연수

# Example
#   1) [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
#       5 + 7 + 4 = 16
#
#
# | 1 | 2 | 3 | 5 |  -> copy first row [(0,1), (1,2), (2,3), (3,5)]  -> & sort ([(0,1), (1,2), (2,3), (3,5)]) --> check if maximum value (3,5) on same column --> no --> add to sum
#
# | 5 | 6 | 7 | 8 |
#
# | 4 | 3 | 2 | 1 |


# | 1 | 2 | 3 | *5 |
#
# | 5 | 6 | 7 | 8 | -> copy second row [(0,5), (1,6), (2,7), (3,8)]  -> & sort ([(0,5), (1,6), (2,7), (3,8)]) --> check if maximum value (3,8) on same column --> yes --> add second largest value
#
# | 4 | 3 | 2 | 1 |


# | 1 | 2 | 3 | *5 |
#
# | 5 | 6 | *7 | 8 |
#
# | 4 | 3 | 2 | 1 | -> copy third row [(0,4), (1,3), (2,2), (3,1)]  -> & sort ([(3,1), (2,2), (1,3), (0,4)]) --> check if maximum value (0,4) on same column --> no --> add to sum


# | 1 | 2 | 3 | *5 |
#
# | 5 | 6 | *7 | 8 |
#
# | *4 | 3 | 2 | 1 |

# Pseudocode
#   - For each row,
#   - crease a new array with element of form [(index, value)].\ (call it row)
#   - sort array
#   - check if max value row[-1] is on the same column as before (initially -1)
#   - if yes, choose row[-2], and add to sum
#   - if not, choose row[-1], and add to sum
#   - return value

# fix
  # | 1 | 2 | 3 | 5 |
  #
  # | 5 | 6 | 7 | 100 |    | 10 | 11 | 12 | 11 |
  #
  # | 4 | 3 | 2 | 1 |      | 16 | 15 | 13 | 13 | --> 16

def solution(land):
    N_rows = len(land)
    N_cols = len(land[0])
    dp = [[0] * N_cols for x in range(N_rows)]
    dp[0] = land[0]

    for i in range(1,N_rows):

        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
        dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]

    answer = max (dp[-1])

    return answer

# def solution(land):
#     answer = 0
#     prev_column_index = -1

#     # For each row,
#     for row in land:
#         # crease a new array with element of form [(index, value)].\ (call it row)
#         row_copy = list(zip(range(4), row))
#         # sort array
#         row_copy.sort(key=lambda e: e[1])
#         # check if max value row[-1] is on the same column as before (initially -1)
#         # if yes, choose row[-2], and add to sum
#         # if not, choose row[-1], and add to sum
#         if row_copy[-1][0] == prev_column_index:
#             answer += row_copy[-2][1]
#             prev_column_index = row_copy[-2][0]
#         else:
#             answer += row_copy[-1][1]
#             prev_column_index = row_copy[-1][0]

#     # return value
#     return answer

if __name__ == "__main__":
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) #16