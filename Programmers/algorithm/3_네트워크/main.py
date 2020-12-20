# goal: 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
#   - 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
#   - 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
#   - i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
#   - computer[i][i]는 항상 1입니다.

# Examples
#   1) n: 3     computers:[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#
#       - has two networks
#           - the connection between computer 0 and 1
#           - computer 2 (alone)

#   2) n: 3     computers:[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#       - has 1 network
#           - the connection between computer 0, 1 and 2

# Pseudocode
#   for each computer (starting from 0)
#   if computer in set, continue
#   if computer not in set, find all computers in a single network
#       for each col of a row,
#       find index of all computers other than itself and not in set, and add to queue
#       for each computer in queue,
#       add computer to set
#       perform recursion on value
#   add found computers to set
#   increment network count by 1
#   return network count

def solution(n, computers):
    answer = 0
    return answer