# goal: 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해
# 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

# 제한사항
#   - 표(board)는 2차원 배열로 주어집니다.
#   - 표(board)의 행(row)의 크기 : 1,000 이하의 자연수
#   - 표(board)의 열(column)의 크기 : 1,000 이하의 자연수
#   - 표(board)의 값은 1또는 0으로만 이루어져 있습니다.


# Example
#   1) [[0,0,1,1],[1,1,1,1]]
#
#       | 0 | 0 | 1 | 1 | --> choose size 4 (biggest n x n square)
#       | 1 | 1 | 1 | 1 |

#         x
#       | 0 | 0 | 1 | 1 | --> i = 0, and there is 0 at j = 0 --> increment i
#       | 1 | 1 | 1 | 1 |

#             x
#       | 0 | 0 | 1 | 1 | --> i = 0, and there is 0 at j = 1 --> increment i
#       | 1 | 1 | 1 | 1 |

#                 x
#       | 0 | 0 | 1 | 1 | --> i = 0, and its all one !! --> return size 4
#       | 1 | 1 | 1 | 1 |


# Pseudocode
#   find max nxn size given board min(N_rows, N_cols)
#   for i in N_rows,
#   for j in N_cols,
#   check if square of size n at [i,j] has all 1s
#   if not, move to right
#   if index error, break
#   if none exists, reduce size of n by 1 and repeat


def solution(board):
    N_rows = len(board)
    N_cols = len(board[0])
    #   find max nxn size given board min(N_rows, N_cols)
    max_square_size = min(N_rows, N_cols)
    answer = -1

    #   for i in N_rows,
    for i in range(0,N_rows):
        #   for j in N_cols,
        for j in range(0,N_cols):

            if i == 0 or j == 0:
                 answer = max(answer, board[i][j] ** 2)
                 continue

            if board[i][j] == 0:
                continue

            board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
            answer = max(answer, board[i][j] ** 2)
    return answer



# ==== attempt 2=====
# from functools import reduce
# from copy import deepcopy

# def solution(board):
#     N_rows = len(board)
#     N_cols = len(board[0])
#     #   find max nxn size given board min(N_rows, N_cols)
#     max_square_size = min(N_rows, N_cols)
#     answer = -1
#     dp = deepcopy(board)

#     for square_size in range(2, max_square_size+1):
#         #   for i in N_rows,
#         for i in range(N_rows):
#             #   for j in N_cols,
#             for j in range(N_cols):
#                 target_row = i + (square_size-1)
#                 target_colum = j + (square_size-1)

#                 if (target_row >= N_rows) or (target_colum >= N_cols):
#                     break

#                 dp[i][j] += sum(board[target_row][j:j+square_size]) + sum([x[target_colum] for x in board[i:i+square_size]]) - board[target_row][target_colum]
#                 # print(board[i][j])
#                 if dp[i][j] == square_size**2:
#                     answer = max(answer, dp[i][j])
#     return answer


# ==== attempt 1=====
# from functools import reduce

# def solution(board):
#     N_rows = len(board)
#     N_cols = len(board[0])
#     #   find max nxn size given board min(N_rows, N_cols)
#     square_size = min(N_rows, N_cols)

#     while square_size > 0:
#         #   for i in N_rows,
#         for i in range(N_rows):
#             #   for j in N_cols,
#             for j in range(N_cols):
#                 try:

#                     #   check if square of size n at [i,j] has all 1s
#                     square_sum = sum([sum(x[j:(j + square_size)]) for x in board[i: (i + square_size)]])
#                     #   if not, move to right
#                     if square_sum == square_size**2:
#                         return square_sum

#                 #   if index error, break
#                 except IndexError:
#                     break
#         #   if none exists, reduce size of n by 1 and repeat
#         square_size -= 1

#     return 0

if __name__ == "__main__":
    print(solution([[0,0],[0,0]])) #1
    print(solution([[1,0],[0,0]])) #1
    print(solution([[0,0,1,1],[1,1,1,1]])) #4
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) #9