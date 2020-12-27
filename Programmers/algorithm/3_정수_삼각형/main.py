# goal: 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return
# 하도록 solution 함수를 완성하세요.

# 제한사항
#   - 삼각형의 높이는 1 이상 500 이하입니다.
#   - 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

# Example

# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10        15
# 18        11/16                   15                                              <- take max
# 20        25/18/23                15/20/19                19                      <- take max
# 24        25/30/23/28             27/20/25/17/22/21       21/26/25/25       24    <- take max


# 7         -inf                    -inf                    -inf              -inf
# 10        15                      -inf                    -inf              -inf  triangle[i][j] = max([triangle[i-1][j] + triangle[i][j], triangle[i-1][j+1] + triangle[i][j]])
# 18        11/16                   15                      -inf              -inf  triangle[i][j] = max([triangle[i-1][j] + triangle[i][j], triangle[i-1][j+1] + triangle[i][j]])
# 20        25/18/23                15/20/19                19                -inf  triangle[i][j] = max([triangle[i-1][j] + triangle[i][j], triangle[i-1][j+1] + triangle[i][j]])
# 24        25/30/23/28             27/20/25/17/22/21       21/26/25/25       24    triangle[i][j] = max([triangle[i-1][j] + triangle[i][j], triangle[i-1][j+1] + triangle[i][j]])

#

# Pseudocode
#   1) match column size for all rows
#   2) for each row i (starting from row 1)
#   3) for each column j (starting from column 0 to i + 1)
#   4) compute
#       - (if j == 0) dp[i][j] = dp[i-1][j] + triangle[i][j]
#       - (if j == i) dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#       - (if none of the above) dp[i][j] = max([dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j]])
#   5) return max value in last row

def solution(triangle):
    answer = 0
    n_rows = len(triangle)
    # copy triangle, call it dp
    dp = [triangle[i][:] for i in range(len(triangle))]

    # for each row i (starting from row 1)
    for i in range(n_rows):
        # for each column j (starting from column 0 to i + 1)
        for j in range(i+1):
            # compute
            # (if j == 0) dp[i][j] = dp[i-1][j] + triangle[i][j]
            if j == 0:
            # (if j == i) dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            elif j == 1:

            # (if none of the above) dp[i][j] = max([dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j]])
            else:
    # return max value in last row
    answer = max(triangle[-1])
    return answer

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) #30