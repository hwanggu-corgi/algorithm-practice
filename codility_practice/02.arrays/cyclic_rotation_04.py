# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# goal: rotate array A K times; that is, each element of A will be shifted to the right K times

def solution(A, K):
    # write your code in Python 3.6
    # brute force solution

    # find length
    N = len(A)
    # generate an array of identical size
    B = [0] * N


    # replace value
    i = 0
    while (i < N):
        B[(i+K) % N] = A[i]
        i += 1

    j = 0
    while (j < N):
        A[i] = B[i]
        j += 1
    return A
