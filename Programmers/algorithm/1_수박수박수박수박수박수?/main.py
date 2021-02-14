def solution(n):
    length = 1
    answer = ""
    while length <= n:
        if length % 2 == 1:
            answer += "수"
        else:
            answer += "박"
        length += 1
    return answer

if __name__ == "__main__":
    print(solution(3)) #수박수
    print(solution(4)) #수박수박