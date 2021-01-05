# goal: 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를
# 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   선수의 수는 1명 이상 100명 이하입니다.
#   경기 결과는 1개 이상 4,500개 이하입니다.
#   results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
#   모든 경기 결과에는 모순이 없습니다.

# Example
#   n: 5       results: [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
#       [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
#
#       - [[1,3,0,0,0],
#          [2,1,2,2,3],
#          [0,3,1,0,0],
#          [0,3,0,1,0]
#          [0,2,0,0,1]]

#          [0,4,0,0,0]

# Example 2
#   n: 2    results: [[1,2]]
#       - [[1,2],
#          [0,1]]

#          [1,0] --> the first is player 1 and 2nd is player 2 --> the total is 2


#   n: 2    results: [[2,1]]
#          [0,1] --> the first is player 2 and 2nd is player 1 --> the total is 2

# Example 3
#   n: 3    results: [[1,2],[2,3]]
#          [2,1,0] --> the first player is 1, 2nd is player 2 and last is player 3 --> the total is 3


# Example 4
#   n: 3    results: [[1,2],[1,3]]
#          [2,0,0] --> the first is player 1, and the ranks of player 2 and 3 are equal, can't be ranked --> the total is 1


# Example 5
#   n: 4    results: [[1,2],[1,3],[2,4]]
#          [3,1,0,0] --> from here, we know the first is player 1, but since we don't know who came after player 1 --> the answer is 1 (may be incorrect)


# Example 6
#
#          [2,2,2,1,0] --> since there 3 2's we can't tell which comes first --> but we know 1 is after 0 --> so the answer is 2


# Example 7


# 플로이드 와샬 알고리즘
#   - https://www.youtube.com/watch?v=9574GHxCbKc&t=202s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#   - 모든 정점에서 정점으로 최단 알고리즘을 구하는 것이다
#   - 거쳐가는 정점을 기준으로 최단 거리를 구하는 것이다
#           1
#         /    \
#        5      7
#       /         \
#      v            v
#      2 -  1 - >   3
#
#      - 2 번 거쳐서 가는 비용 --> 6
#      - 1 번에서 3번으로 direct --> 7
#      -

#

# Pseudocode
#   - generate dp
#   - for each node, update dp with shorter paths using floyd warshall algorithm
import math

def solution(n, results):
    answer = 0
    dp = generate_dp(n, results)

    for node in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if i == node or j == node:
                    continue

                dp[i][j] = min(dp[i][j], dp[i][node] + dp[node][j])
    print(dp)

def generate_dp(n, results):
    res = [[math.inf] * (n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                res[i][j] = 0

    for i, j in results:
        res[i][j] = 1

    print(res)
    return res
if __name__ == "__main__":
    print(solution(5, [[3, 4], [2, 4], [2, 3], [2, 1], [5, 2]])) # 2
    # print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2