# goal: Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution
# 함수를 작성해주세요.
#   - scoville의 길이는 2 이상 1,000,000 이하입니다.
#   - K는 0 이상 1,000,000,000 이하입니다.
#   - scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
#   - 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

def solution(scoville, K):
    N = scoville
    answer = 0

    i = 1
    # for each scoville in food
    while i < N:
        # if food at i is below threshold, mix food
        if scoville[i-1] < K:
            # update list with new mixed food (take out 2, add new mixed one)
            # add mixed count

        # update index or break
        i += 1

    return answer