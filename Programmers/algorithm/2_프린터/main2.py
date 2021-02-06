# goal: 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가
#       현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한
#       문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

from collections import deque

def solution(priorities, location):
    count = 0

    # zip location to priorities
    # convert list to deque
    queue = deque(zip(range(len(priorities)), priorities))
    while True:
        # find the max value in the list
        to_be_removed = max(queue, key= lambda e: e[1])
        while queue[0] != to_be_removed:
            # popleft and append until reaching the target
            queue.append(queue.popleft())
            # add count for each pop

        # if element is desired, then return count
        # if element is not desired, then continue
        count += 1

        if queue[0][0] != location:
            queue.popleft()
            continue
        else:
            answer = count
            break
    return answer

if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2)) #1
    print(solution([1, 1, 9, 1, 1, 1], 0)) #5