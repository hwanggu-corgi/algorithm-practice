# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Write a function, def solution(A) that, given an array A consisting of
# N integers containing daily prices of a stock share for a period of N consecutive
# days, returns the maximum possible profit from one transaction during this period

def solution(A):
    # write your code in Python 3.6

    max_profit = profit_ending =  0
    max_sell_price = sell_price = purchase_price = A[0]

    for a in A:
        # calculate profit after selling with price a
        sell_price = a
        net_price = purchase_price - sell_price

        profit_ending = profit(0, profit_ending + net_price)

        # if the profit is positive
        if profit_ending > 0:
            # update the max profit
            max_profit = max(max_profit, profit_ending)
            max_sell_price = sell_price
        else:
            # if the profit is negative
            # reset the purchase price to current
    pass
