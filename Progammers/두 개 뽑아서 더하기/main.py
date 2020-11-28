# 문제를 이해한다
# goal: numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - numbers의 길이는 2 이상 100 이하입니다.
#   - numbers의 모든 수는 0 이상 100 이하입니다.

def solution(numbers):
    answer = []

    # for each number in numbers,
    # for each differand starting from 0 to number,
    # check if differand exists
    # check if number - differrend exists
    #   if both of the above are true, then
    return answer