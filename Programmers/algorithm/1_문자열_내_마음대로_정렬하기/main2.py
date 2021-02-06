# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를
# 기준으로 오름차순 정렬하려 합니다.

def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings, key=lambda e: e[n])
    return answer

if __name__ == "__main__":
    print(solution(["sun", "bed", "car"], 1)) #[car, bed, sun]
    print(solution(["abce", "abcd", "cdx"], 2)) #[abcd, abce, cdx]