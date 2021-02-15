# goal: solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
# 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
# return 하도록 solution 함수를 완성하세요

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    bridge = deque([])
    truck_weights = deque(truck_weights)

    while len(truck_weights) > 0:
        # if truck at front of bridge meets condtion, pop left
        if bridge_should_pop(bridge_length, bridge):
            bridge.popleft()
        # if truck at truck_weights meets condition, pop left and move to bridge
        if bridge_is_available(weight, bridge):
            truck_weight = truck_weights.popleft()
            bridge.append([truck_weight, 0])

        # count time
        update_trucks_on_bridge(bridge)
        time += 1

    # return total time
    answer = time
    return answer