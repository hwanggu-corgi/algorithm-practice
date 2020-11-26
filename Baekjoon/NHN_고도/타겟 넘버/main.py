def solution(numbers, target):
    N = len(numbers)
    answer = _solution(1, target, 1, N) + _solution(-1, target, 1, N)
    return answer

def _solution(value, target, depth, N):
    if depth == N:
        return 1 if value == target else 0

    count_left = _solution(value + 1, target, depth + 1, N)
    count_right = _solution(value - 1, target, depth + 1, N)

    return count_left + count_right

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([1], 3))
    print(solution([1], 1))
    print(solution([1,1], 1))