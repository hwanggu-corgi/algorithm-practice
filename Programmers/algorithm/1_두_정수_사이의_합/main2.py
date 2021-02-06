def solution(a, b):
    answer = 0
    larger = max(a,b)
    smaller = min(a,b)
    answer = sum(range(smaller, larger+1))
    return answer

if __name__ == "__main__":
    print(solution(3, 5)) #12
    print(solution(3, 3)) #3
    print(solution(5, 3)) #12