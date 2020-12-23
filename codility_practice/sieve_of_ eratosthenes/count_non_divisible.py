# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    answer = []
    # write your code in Python 3.6
    for index_a, a in enumerate(A):
        count = 0
        for index_b, b in enumerate(A):

            if index_a == index_b:
                continue

            if a % b != 0:
                count += 1
        answer.append(count)
    return answer
