# goal: 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

def solution(prices):
    answer = []
    n = len(prices)

    i = 0
    while i < n:
        temp = []
        j = i + 1
        while j < n:
            temp.append(prices[j])

            if prices[i] > temp[-1]:
                break
            j += 1

        answer.append(len(temp))
        i += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3])) #[4, 3, 1, 1, 0]