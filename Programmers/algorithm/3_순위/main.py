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

#       Check array for players with full info
#          [1,0] --> the first is player 1 and 2nd is player 2 --> the total is 2


# Example 3
#   n: 3    results: []

#       Starting from node with full info find node with smaller value

# Pseudocode
#   - create graph matrix (mark 2 as win and 3 as loss)
#   - using the information fill rank   [0,1,0,0,1]
#       - first fill array on player with full info
#       - starting with array with full info check if a neighboring player is rankable
#       - fill array if a player is rankable
#       - repeat until can't be filled further
#   - return answer
def solution(n, results):
    answer = 0
    return