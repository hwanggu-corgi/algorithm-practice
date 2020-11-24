# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Given an array A consisting of N integers, returns the maximum sum of any slice of A.

def solution(A):
    # write your code in Python 3.6

    maximum_sum = sum_ending = 0

    for a in A:
        # compute sum ending
        sum_ending = max(0, sum_ending + a)
        maximum_sum = max(maximum_sum, sum_ending)

        # update su
    return maximum_sum
