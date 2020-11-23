# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# goal: rotate array A K times; that is, each element of A will be shifted to the right K times

def solution(A, K):
    # write your code in Python 3.6
    # find length
    N = len(A)
    # generate an array of identical size
    B = [0] * N

    temp_1 = A[0]
    temp_2 = A[0]

    # replace value
    i = 0
    while (i < N):
        if (i == 0):
            temp_1 = A[(i+K) % N]
            A[(i+K) % N] = A[i]
        else:
            temp_2  = A[(i+K) % N]
            A[(i+K) % N] = temp_1
            temp_1 = temp_2

        i += 1

    return A
