# goal: solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
# 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
# return 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - bridge_length는 1 이상 10,000 이하입니다.
#   - weight는 1 이상 10,000 이하입니다.
#   - truck_weights의 길이는 1 이상 10,000 이하입니다.
#   - 모든 트럭의 무게는 1 이상 weight 이하입니다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time_elapsed = 0
    N = len(truck_weights)

    # reformat trucks to following [[truck id, time spent moving across bridge]]
    # create a queue for waiting trucks
    trucks_queue = deque([[x,0] for x in truck_weights])
    in_progress = deque([])
    finished = deque([])

    # while
    while len(finished) == N:
        # wait until more truck can be added
        # add more truck when free
        if is_alright_to_cross_bridge(trucks_queue, weight):
            move_truck_to_bridge(trucks_queue, in_progress)

        update_trucks_on_bridge(in_progress)

        # if truck is done, then move to finished
        if is_alright_to_move_to_finish(in_progress):
            move_truck_to_finish(in_progress, finish, weight)

        time_elapsed += 1

    # once all trucks have moved to the end of bridge, return answer

    answer = time_elapsed
    return answer

def is_alright_to_cross_bridge(trucks_queue, bridge_weight, weight):
    if len(trucks_queue) == 0:
        return False

    if bridge_weight + trucks_queue[-1][0] > weight:
        return False

    if trucks_queue[-1][1] <= 1:
        return False

    return True

def move_truck_to_bridge(trucks_queue, in_progress):
    if len(trucks_queue) == 0:
        return

    truck = trucks_queue.popleft()
    in_progress.append(truck)

def update_trucks_on_bridge(in_progress):
    for truck in in_progress:
        truck[1] += 1

def is_alright_to_move_to_finish(in_progress, ):


def move_truck_to_finish(...):
    pass