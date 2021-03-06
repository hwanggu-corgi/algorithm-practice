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
        A[j] = B[j]
        j += 1
    return A


# # attempt 2: better case (timed out) got 62%
# def solution(A, K):
#     # write your code in Python 3.6
#     # find length
#     N = len(A)
#     # generate an array of identical size
#     B = [0] * N

#     temp_1 = A[0]
#     temp_2 = A[0]

#     # replace value
#     count = 0
#     i = 0
#     while (count < N):
#         if (i == 0):
#             temp_1 = A[(i+K) % N]
#             A[(i+K) % N] = A[i]
#         else:
#             temp_2  = A[(i+K) % N]
#             A[(i+K) % N] = temp_1
#             temp_1 = temp_2

#         i = (i+K) % N
#         count += 1

#     return A
