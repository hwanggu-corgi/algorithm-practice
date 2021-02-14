# goal: 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

def solution(prices):
    answer = []
    n = len(prices)

    i = 0
    while i < n:
        count = 0
        j = i + 1
        while j < n:
            if prices[i] < price[j]:

            count += 1
        i += 1
    return answer