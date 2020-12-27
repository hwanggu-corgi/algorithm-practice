# goal: n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행
# 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.



# 제한사항
#   - 섬의 개수 n은 1 이상 100 이하입니다.
#   - costs의 길이는 ((n-1) * n) / 2이하입니다.
#   - 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
#   - 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
#   - 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
#   - 연결할 수 없는 섬은 주어지지 않습니다.

# Example
#   1) n - 4 costs - [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]


#   Minimal Spanning Tree Problem
#   - https://www.youtube.com/watch?v=LQ3JHknGy8c&feature=emb_title&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#       Pseudcode
#           MST-kruskal(G,w):
#               A = empty
#               for each vertex v in G.V
#                   Make-set(v)
#                   for each edge (u,v) in G.E taken in non-decreasing order by weight
#                       if FIND-SET(u) != FIND-SET(v):
#                           A = A union of {(u,v)}
#                           union(u,v)
#             return A

# Union Find algorithm
#   - https://www.youtube.com/watch?v=AMByrd53PHM&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#   - for each vertex use recursion to find the end vertex it points to

def get_parent(cycle, x):
    if cycle[x] == x:
        return x

    return get_parent(cycle, cycle[x])

# pseudocode
#   1. create cycle table
#   2. sort costs with weights in increasing order
#   3. for each weight of vertex x connecting to y
#       - check if is valid (i.e cycle[x] == x)
#       - check if it doesn't form a cycle
#       - set end vertex of cycle[y] to cycle[x]
#       - add weight to total


def solution(n, costs):
    answer = 0
    return answer