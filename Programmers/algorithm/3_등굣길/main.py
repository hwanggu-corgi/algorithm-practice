# goal: 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈
# 나머지를 return 하도록 solution 함수를 작성해주세요.


# 제한사항
#   - 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
#   - m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
#   - 물에 잠긴 지역은 0개 이상 10개 이하입니다.
#   - 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.


# example
#   1)  m: 4	n: 3	puddles:[[2, 2]]	return:4
#
#   [[0,0,0,0],
#    [0,0,0,0],
#    [0,0,0,0]]

#   [[0,1,2,3],
#    [1,x,3,4],
#    [2,3,4,0]]

# pseudocode
#   generate dp of size n x m
#   mark puddles in dp (of size positive infinity)
#   mark dp[i][0] = i and dp[0][i] = i
#   find shortest path
#   for i (starting from 1)
#   for j (starting from 1)
#   if (i,j) of dp[i][j] is in puddle, then skip
#   else, set dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
#   return dp[-1][-1] - 1

def solution(m, n, puddles):
    answer = 0

    #   generate dp of size n x m
    dp = [[0] * (m+1) for _ in range(n+1)]

    #   mark puddles in dp (of size positive infinity)
    puddles = set([(x[1], x[0]) for x in puddles])

    dp[1][1] = 1

    #   find shortest path
    #   for i (starting from 1)
    for i in range(1,n+1):
        #   for j (starting from 1)
        for j in range(1,m+1):

            if (i == 1) and (j == 1):
                continue

            #   if (i,j) of dp[i][j] is in puddle, then skip
            if (i,j) in puddles:
                continue

            #   else, set dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    #   return dp[-1][-1] - 1
    return dp[-1][-1]

if __name__ == "__main__":
    print(solution(4,3,[[2, 2]])) #4
    print(solution(4,3,[[1, 3], [3, 1]])) #6