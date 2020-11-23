# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# goal: rotate array A K times; that is, each element of A will be shifted to the right K times

def solution(A, K):
    # write your code in Python 3.6

    # find length
    N = len(A)

    # replace value
    A[(i+K) % N] = A[i]


    return A
