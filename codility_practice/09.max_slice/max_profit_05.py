import sys
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    max_ending = 0
    max_profit = -sys.maxsize
    # subtract A[i] and A[i-1] where i starts from 1

    if n == 1 or n == 0:
        return 0

    i = 1
    while i < n:
        # update max_ending
        revenue = A[i] - A[i-1]
        max_ending = max(0, max_ending + revenue)
        # update max_profit
        max_profit = max(max_profit, max_ending)
        i += 1

    return max_profit

if __name__ == "__main__":
    print(solution([0]))
    print(solution([1,2]))
    print(solution([2,1]))