# goal: Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution
# 함수를 작성해주세요.
#   - scoville의 길이는 2 이상 1,000,000 이하입니다.
#   - K는 0 이상 1,000,000,000 이하입니다.
#   - scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
#   - 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

from collections import deque

def solution(scoville, K):
    N = len(scoville)
    answer = 0

    scoville.sort()

    queue = deque(scoville)

    i = 1
    # for each scoville in food
    while i < N:
        # if food at i is below threshold, mix food
        if queue[i-1] < K:
            new_food_scoville = mix_food(i, queue)
            queue.popleft()
            # update list with new mixed food (take out 2, add new mixed one)
            # add mixed count
            if new_food_scoville <= K:
                queue[0] = new_food_scoville
            else:
                queue.popleft()
                queue.append(new_food_scoville)

            # update N
            N = len(queue)
            answer += 1

        # update index or break
        if N == 1 and queue[0] <= K:
            return -1

        if queue[0] > K:
            break

    return answer

def mix_food(index, queue):
    lesser_spicy = min(queue[index-1], queue[index])
    more_spicy = max(queue[index-1], queue[index])

    return lesser_spicy + (more_spicy * 2)

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1,1], 2))
    print(solution([1,1], 4))