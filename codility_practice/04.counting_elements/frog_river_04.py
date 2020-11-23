# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: find the earliest time when the frog can jump to the other side of the river
#   - The frog can cross only when leaves appear at every position across the river from 1 to X
#   - If the frog is never able to jump to the other side of the river, the function should return -1.

def solution(X, A):
    # write your code in Python 3.6
    checklist = set(range(1, X))
    N = len(A)

    # iterate through the array
    i = 0
    while i < N:
        # check of element from the checklist
        if A[i] in checklist:
            checklist.remove(A[i])

        # if the checklist is empty, then return i
        if len(checklist) == 0:
            return i
        i += 1

    return -1
