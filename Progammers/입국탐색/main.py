# Goal: 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하라
#
# restrictions
#   - 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
#   - 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
#   - 심사관은 1명 이상 100,000명 이하입니다.

# time max - 60 minutes (upper bound)
# time min - 0 minutes
#   - 심사관 1: floor(60 / 7) -> 8
#   - 심시관 2: floor(60 / 10) -> 10
# More people can be analyzed

# time max - 30 minutes (upper bound)
# time min - 0 minutes (lower bound)
#   - 심사관 1: floor(30 / 7) -> 4
#   - 심사관 2: floor(30 / 10) -> 3
#   More people can be analyzed

# time max - 15 minutes (upper bound)
# time min - 0 minutes (lower bound)
#   - 심사관 1: floor(15 / 7) -> 2
#   - 심시관 2: floor(15 / 10) -> 1

# time max -


def solution(n, times):
    answer = 0
    return answer

if __name__ == "__main__":
    print(solution(5, [7,10])) #28