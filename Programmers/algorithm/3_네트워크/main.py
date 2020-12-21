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
#   if computer in set continue
#   find all computers in a single network
#       if computer in set, return
#       find index of all computers other than itself and not in set, and add to queue
#       if length of queue is 0, then return
#       for each computer in queue,
#       add computer to set
#       perform recursion on value
#   increment network count by 1
#   return network count

def solution(n, computers):
    answer = 0

    #   for each computer (starting from 0)
    for computer in computers:
        #   if computer in set continue
        if computer in already_searched:
            continue

        _solution(...)

        #   increment network count by 1
        network_count += 1
    #   return network count
    return network_count

def _solution(...):
    #   find all computers in a single network
    #       if computer in set, return
    if computer in searched:
        return

    #       find index of all computers other than itself and not in set, and add to queue
    neighbouring_computers = find_neighbouring_computers(...)
    #       if length of queue is 0, then return
    #       for each computer in queue,
    #       add computer to set
    #       perform recursion on value