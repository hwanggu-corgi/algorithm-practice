
# Goal:
# - N:  >= 2 and <= 20
# - numbers[i]: >= 1 and <= 50
# - target: >= 1 and <= 1000

def solution(numbers, target):
    answer = 0
    answer += _solution(numbers[0], target, 1, numbers)
    answer += _solution(-numbers[0], target, 1, numbers)

    return answer

def _solution(value, target, depth, numbers):
    if depth == len(numbers) - 1:
        return 1 if value == target else 0

    count_left = _solution(value + numbers[depth], target, depth + 1, numbers)
    count_right = _solution(value - numbers[depth], target, depth + 1, numbers)

    return count_left + count_right

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([1], 3))
    print(solution([1], 1))
    print(solution([1,1], 1))