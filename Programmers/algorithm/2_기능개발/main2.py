# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌
# 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)

    while len(progresses) > 0:
        add_progress(progresses, speeds)
        count = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.popleft()
            count += 1
        answer.append(count)

    return answer