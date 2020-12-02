# goal: 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이
# 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요
#
# 제한 사항
#   - 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
#   - 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

def solution(citations):
    N = len(citations)
    answer = 0

    if N == 0:
        return 0

    # sort citations to increasing order
    citations = sorted(citations, reverse=True)

    # find number that has h citations greater than h
    i = 0
    while i < N:
        paper_reference_count = citations[i]
        number_of_papers_referenced_higher_than_equal_to_i = i + 1

        if ((paper_reference_count >= number_of_papers_referenced_higher_than_equal_to_i) and
           (paper_reference_count <= number_of_papers_referenced_higher_than_equal_to_i)):
            answer = paper_reference_count
            break
        i += 1

    # return answer
    return answer

if __name__ == "__main__":
    print(solution([])) #0
    print(solution([1])) #1
    print(solution([3, 0, 6, 1, 5])) #3