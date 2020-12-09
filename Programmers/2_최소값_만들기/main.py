# goal: 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
#   - 배열 A, B의 크기 : 1,000 이하의 자연수
#   - 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

# Example
#   1)  A: [1, 4, 2] B: [5, 4, 4]
#       - 0 + (1 x 5) + (4 x 4) + (2 x 4) = 29
#   2)  A: [1,2] B:[3,4]
#       - 0 + (1 x 4) + (2 x 3) = 10

# Pseudocode
#   - order array A in increasing order
#   - order array B in decreasing order
#   - while i < N (len(A) or len(B)),
#       add A[i] * B[i] to sum answer
#   - return answer

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    N = len(A)

    while i < N:
        answer += A[i] * B[i]
        i += 1

    return answer