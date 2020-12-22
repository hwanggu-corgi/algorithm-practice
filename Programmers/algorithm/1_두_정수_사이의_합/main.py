def solution(a, b):
    bigger = max(a,b)
    lesser = min(a,b)
    answer = sum(range(lesser,bigger+1))
    return answer