# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Given an array A consisting of N integers, returns the maximum sum of any slice of A.

def solution(A):
    # write your code in Python 3.6

    maximum_sum = sum_ending = 0
    smallest_negative_number = -1000000
    neg_number_count = 0
    N = len(A)

    if N == 0:
        return 0

    if N == 1:
        return A[0]

    for a in A:
        # compute sum ending
        sum_ending = max(0, sum_ending + a)
        maximum_sum = max(maximum_sum, sum_ending)

        # compute for case when all numbers in A are negative
        if a < 0:
            neg_number_count += 1
            if a > smallest_negative_number:
                smallest_negative_number = a


    if neg_number_count == N:
        return smallest_negative_number

    return maximum_sum
