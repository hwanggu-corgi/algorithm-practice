# goal: 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용
# 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.


# 제한사항

#   - 차량의 대수는 1대 이상 10,000대 이하입니다.
#   - routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
#   - 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
#   - 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

# Example
#   1) routes: [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
#
#   [[-20,15], [-18,-13], [-14,-5], [-5,-3]] = 2
#   [---[----[---]--------------------------][---- ]------------------------]
#  -20  -18 -14  -13                        -5    -3                       15



#   [[-20,15]] [[-18,-13], [-14,-5], [-5,-3]] --> do they overlap? --> yes [-20, 15]--> camera_count = 1
#   [----------------------------------------------------------------]
#  -20 -18 -14  -13                   -5    -3                       15


#   [[-20,15]] [-18,-13] [[-14,-5], [-5,-3]] --> do they overlap? --> yes [-18, -13]--> camera_count = 1
#   [----[--------]----------------------------------------------------]
#  -20 -18 -14  -13                   -5    -3                         15


#   [[-20,15],[-18,-13]] [-14,-5] [[-5,-3]]  --> do they overlap? --> yes [-14, -13]--> camera_count = 1
#   [----[---[-----]--------------------]--------------------------------]
#  -20 -18 -14  -13                    -5    -3                         15


#   [[-20,15],[-18,-13],[-14,-5]] [-5,-3] [] --> do they overlap? --> no --> camera_count = 2
#   [----[---[-----]--------------------][-----]---------------------------]
#  -20 -18 -14  -13                    -5     -3                         15



# Pseudocode
#   create list variable called current_overlap = []
#   create int variable called camera_count (val 0)
#   sort routes
#   turn routes to queue
#   while len(routes) is not 0
#   popleft route
#   if current_overlap is empty
#       increment camera_count
#       set current_overlap to route
#   if not empty,
#       check if route and current_overlap overlaps
#       if overlaps,
#           update current_overlap
#       if doesn't overlap
#           appendleft route
#           empty current_overlap

#   return camera_count

from collections import deque

def solution(routes):
    answer = 0
    #   create list variable called current_overlap = []
    current_overlap = []

    #   create int variable called camera_count (val 0)
    camera_count = 0

    #   sort routes
    routes = deque(sorted(routes, key = lambda e: e[0]))

    #   turn routes to queue
    #   while len(routes) is not 0
    while len(routes) > 0:
        #   popleft route
        route = routes.popleft()

        #   if current_overlap is empty
        if not current_overlap:
            #   increment camera_count
            camera_count += 1
            #   set current_overlap to route
            current_overlap = route
            #   continue
            continue

        #   check if route and current_overlap overlaps
        #   if overlaps,
        is_overlapping, val = get_overlap(current_overlap, route)
        if is_overlapping:
            #  update current_overlap
            current_overlap = val
        #   if doesn't overlap
        else:
            #   appendleft route
            routes.appendleft(route)
            #   empty current_overlap
            current_overlap = []

    #   return camera_count
    return camera_count

def get_overlap(current_overlap, route):
    res = [0,0]

    res[0] = max(current_overlap[0], route[0])
    res[1] = min(current_overlap[1], route[1])

    if res[0] <= res[1]:
        return True, res
    return False, res

if __name__ == "__main__":
    print(solution([[-20,15]])) #1
    print(solution([[-20,10], [2, 5]])) #1
    print(solution([[-20,-3], [-2, 5]])) #2
    print(solution([[0,1], [2, 3]])) #2
    print(solution([[0,1], [1, 3]])) #1
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2