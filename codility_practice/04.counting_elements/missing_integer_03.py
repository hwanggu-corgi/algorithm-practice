# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# The goal is to check whether array A is a permutation.

def solution(A):
    # write your code in Python 3.6

    N = len(A)
    # create checklist from 1 to N (number of elements in A)
    checklist = set(range(1, N+1))
    # iterate through elements in array
    i = 0
    while i < N:
        # if element not in array, then return false
        if A[i] not in checklist:
            return 0

        checklist.remove(A[i])

        i += 1


    # if set is not empty, return false
    if len(checklist) != 0:
        return 0
    else:
        # if set is empty, return true
        return 1
