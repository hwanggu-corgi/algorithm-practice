# goal: Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution
# 함수를 작성해주세요.

import heapq

def solution(scoville, K):
    answer = 0
    count = 0

    # turn scoville into heap
    heapq.heapify(scoville)

    # while true
    while True:

        # if len of scoville is 1, then return -1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        if scoville[0] >= K:
            break

        # pop two heap elements from scoville
        e_1 = heapq.heappop(scoville)
        e_2 = heapq.heappop(scoville)

        # mix two elements and add back to scoville
        new_e = e_1 + (e_2 * 2)

        # repeat until the first element is over K
        heapq.heappush(scoville, new_e)

        # add count
        count += 1

    # return total count
    answer = count
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7)) #2