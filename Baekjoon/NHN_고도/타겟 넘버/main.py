def solution(numbers, target):
    answer = _solution(current, target)
    return answer

def _solution(...):
    # terminal case: when sum == target
    if depth == N:
        return 1 if value == target else 0

    # travel to the left with current + 1
    _solution(...)
    # travel to the right with current - 1