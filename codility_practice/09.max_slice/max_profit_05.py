import sys
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    max_ending = 0
    max_profit = -sys.maxsize
    # subtract A[i] and A[i-1] where i starts from 1
    i = 1
    while i < n:
        # update max_ending
        a = A[i]
        max_ending = max(0, max_ending + a)
        # update max_profit
        max_profit = max(max_profit, max_ending)
        i += 1

    return max_profit
