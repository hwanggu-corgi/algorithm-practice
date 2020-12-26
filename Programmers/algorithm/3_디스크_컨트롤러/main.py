# goal: 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로
# 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가
# 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

# 제한 사항
#   - jobs의 길이는 1 이상 500 이하입니다.
#   - jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
#   - 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
#   - 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
#   - 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

# Example
#   1) [[0, 3], [1, 9], [2, 6]]
#       - use shorttest job first
#       (0,3)
#           - Time taken from beginning 3   --> shortest
#       (1,9)
#           - Time taken from beginning 10  --> longest
#       (2,6)
#           - Time taken from beginning 8   --> second shortest

#       (0,3) starts first
#           - time starts 0
#           - calculate time deplayed (0 - 0) = 0
#           - calculate total time taken 0 + 3  = 3
#           - time ends 3
#
#       (2,6) comes next
#           - time starts 3
#           - calculate time deplayed (3 - 2) = 1
#           - calculate total time taken 1 + 6  = 7
#           - time ends 7
#
#       (1,9) comes next
#           - time starts 9
#           - calculate time deplayed (9 - 1) = 8
#           - calculate total time taken 8 + 9 = 17

# average time =  (3 + 7 + 17) / 3 = 9

# Pseudocode
#   create heap based on time taken from the start
#       [3, 10, 8] --> heap
#   for each time time taken from start, store its [starting time, time taken] to dictionary
#       {3: [[0,3]], 8:[[2,6]] 10:[[1,9]]}

#   pop an element from heap
#   popleft dictionary by the value of heap
#   compute its turnaround time
#   add to turnaround time to sum
#   compute average

import heapq
from collections import deque
import math

def solution(jobs):
    total = 0
    completed_jobs = 0
    current_time = jobs[0][0]
    n = len(jobs)
    processing_jobs = []

    jobs = deque(jobs)

    while completed_jobs < n:
        processing_jobs = get_processing_jobs(jobs, processing_jobs, current_time)
        processing_jobs = sort_by_shortest_job_first(processing_jobs, current_time)

        job = processing_jobs.pop()

        delayed_time = current_time - job[0]
        turnaround_time = delayed_time + job[1]
        current_time += job[1]
        total += turnaround_time
        completed_jobs += 1

    #   compute average
    avg = total // n
    return avg

def sort_by_shortest_job_first(processing_jobs, current_time):
    return sorted(processing_jobs, key = lambda e: e[1], reverse=True)

def get_processing_jobs(jobs, processing_jobs, current_time):
    while (len(jobs) > 0) and (jobs[0][0] <= current_time):
        job = jobs.popleft()
        processing_jobs.append(job)

    return processing_jobs

if __name__ == "__main__":
    print(solution( [[0, 3], [1, 9], [2, 6], [4, 3]])) #9
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution([[0, 10], [4, 10], [5, 11], [15, 2]])) #15