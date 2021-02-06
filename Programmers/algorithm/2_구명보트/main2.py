# goal: 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든
#       사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
#   각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
#   구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
#   구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.


def solution(people, limit):
    answer = 0

    # sort people by the weight
    people.sort()

    while len(people) != 0:
        weight = 0
        # pop person with the most weight
        weight += get_highest_weight(people)

        # pop person with least weight
        while weight + people[0] <= limit and len(people) != 0:
            # repeat this process until full
            weight += people.pop(0)

        # if full, add count, and empty weight and startover
        print(weight)
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100)) #3