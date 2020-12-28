# goal: 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번
# 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 제한사항
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# Example
#   1) n: 6 vertex: [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#       - distance 0 - [1]
#       - distance 1 - [2,3]
#       - distance 2 - [6,4,5] --> return 3

# Detailed Example
#   1) n: 6 vertex: [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

#   write matrix representation of graph
#       - create n x n matrix call it 'graph_matrix'
#       - set graph_matrix[i][i] = 1
#       - for each vertex of form [a,b], set graph_matrix[a-1][b-1] = 1 and graph_matrix[b-1][a-1] = 1
# [[1, 1, 1, 0, 0, 0],
#  [1, 1, 1, 1, 1, 0],
#  [1, 1, 1, 1, 0, 1],
#  [0, 1, 1, 1, 0, 0],
#  [0, 1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 0, 1]]

#   write matrix representation of graph
#       - create n x n matrix call it 'graph_matrix'
#       - set graph_matrix[i][i] = 1
#       - for each vertex of form [a,b], set graph_matrix[a-1][b-1] = 1 and graph_matrix[b-1][a-1] = 1
#   find all adjacent verticies to vertex 0, and put to queue
#   while queue is not empty [1,2]
#       increase depth by 1
#       for each vertex in queue,
#           add vertex to traveled
#           find adjacent vertices
#           if adjacent vertex not in traveled, then add to queue_temp
#       set queue = queue_temp
#   return depth


# Shortest path algorithm
#   Dijkstra
#       https://www.youtube.com/watch?v=611B-9zk2o4&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#       - finds shortest distance between one vertex and all other vertices
#       - 음의 간선 포함할 수 없음

#   Floyd Warshall
#       https://www.youtube.com/watch?v=9574GHxCbKc&t=408s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
#       - finds shortest path between all verticies
#       - Doesnt work with finiding longest path
#       - 음의 간선 포함할 수 있음
#       - 거쳐가는 값을 계산한다
#       - graph_matrix[a][a] = 0
#       - infinity -> no immediate path from vertex a to b
#

#   n = no of vertices
#   A = matrix of dimension n*n
#   for k = 1 to n
#       for i = 1 to n
#           for j = 1 to n
#               Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
#   return A


from collections import deque

def solution(n, edge):
    depth = 0
    number_of_nodes_at_depth = 0
    traveled = set([1])
    adj_vertices = {}

    for u,v in edge:
        if u not in adj_vertices:
            adj_vertices[u] = set()

        if v not in adj_vertices:
            adj_vertices[v] = set()

        adj_vertices[u].add(v)
        adj_vertices[v].add(u)

    # find all adjacent verticies to vertex 1, and put to queue
    queue = adj_vertices[1]

    # while queue is not empty
    while len(queue) > 0:
        queue_temp = set()
        # increase depth by 1
        depth += 1
        number_of_nodes_at_depth = len(queue)
        # add vertex to traveled
        for i in queue:
            traveled.add(i)

        # for each vertex in queue,
        for i in queue:
            # find adjacent vertices
            # if adjacent vertex not in traveled, then add to queue_temp
            for j in adj_vertices[i]:
                if j in traveled:
                    continue

                queue_temp.add(j)
        # set queue = queue_temp
        queue = queue_temp

    return number_of_nodes_at_depth

# from collections import deque

# def solution(n, edge):
#     max_depth = 0
#     # write matrix representation of graph
#     graph_matrix = create_graph_matrix(n, edge)

#     i = 0
#     while i < n:
#         traveled = set([i])
#         # find all adjacent verticies to vertex 0, and put to queue
#         queue = [j for j in range(n) if (j != i) and (graph_matrix[i][j] == 1)]

#         depth = 0
#         # while queue is not empty
#         while len(queue) > 0:
#             queue_temp = []
#             # increase depth by 1
#             depth += 1
#             # for each vertex in queue,
#             for i in queue:
#                 # add vertex to traveled
#                 traveled.add(i)
#                 # find adjacent vertices
#                 # if adjacent vertex not in traveled, then add to queue_temp
#                 adj_vertices = [j for j in range(n) if (j != i) and (not j in traveled) and (graph_matrix[i][j] == 1)]
#                 queue_temp.extend(adj_vertices)
#             # set queue = queue_temp
#             queue = queue_temp
#         max_depth = max(max_depth, depth)
#         i += 1

#     return max_depth
# def create_graph_matrix(n, edges):
#     res = [[0] * n for _ in range(n)]

#     for i in range(n):
#         res[i][i] = 1

#     for vertex_a, vertex_b in edges:
#         res[vertex_a-1][vertex_b-1] = 1
#         res[vertex_b-1][vertex_a-1] = 1

#     return res


# from collections import deque

# def solution(n, edge):
#     depth = 0
#     queue = []
#     traveled = set()
#     # write matrix representation of graph
#     graph_matrix = create_graph_matrix(n, edge)

#     # find all adjacent verticies to vertex 0, and put to queue
#     queue = [j for j in range(n) if (j != 0) and (graph_matrix[0][j] == 1)]
#     # while queue is not empty
#     while len(queue) > 0:
#         queue_temp = []
#         # increase depth by 1
#         depth += 1
#         # for each vertex in queue,
#         for i in queue:
#             # add vertex to traveled
#             traveled.add(i)
#             # find adjacent vertices
#             # if adjacent vertex not in traveled, then add to queue_temp
#             adj_vertices = [j for j in range(n) if (j != i) and (not j in traveled) and (graph_matrix[i][j] == 1)]
#             queue_temp.extend(adj_vertices)
#         # set queue = queue_temp
#         queue = queue_temp
#     return depth

# def create_graph_matrix(n, edges):
#     res = [[0] * n for _ in range(n)]

#     for i in range(n):
#         res[i][i] = 1

#     for vertex_a, vertex_b in edges:
#         res[vertex_a-1][vertex_b-1] = 1
#         res[vertex_b-1][vertex_a-1] = 1

#     return res

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) #3