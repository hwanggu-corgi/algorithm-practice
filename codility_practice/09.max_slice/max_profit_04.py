# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Write a function, def solution(A) that, given an array A consisting of
# N integers containing daily prices of a stock share for a period of N consecutive
# days, returns the maximum possible profit from one transaction during this period

def solution(A):
    # write your code in Python 3.6

    N = len(A)

    if N == 0:
        return 0

    if N == 1:
        return 0

    max_profit = profit_ending =  0
    purchase_price = A[0]

    i = 1
    while i < N:
        # calculate profit after selling with price a
        net_price = A[i] - purchase_price
        profit_ending = max(0, profit_ending + net_price)
        # update the max profit
        max_profit = max(max_profit, profit_ending)
        purchase_price = A[i]
        i += 1
    return max_profit