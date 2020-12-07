# goal: 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.

# Example
#   1) A: [[1, 4], [3, 2], [4, 1]]	B: [[3, 3], [3, 3]]
#   This is matrix multiplication

# Pseudocode
#   for each row in arr1 (i),
    #   for each column in arr2 (j),
    #   calculate element after matrix multiplication
    #       get column length of arr1
    #       for each column in arr1 (m),
    #       compute sum of A[i][m]B[m][j] for all m
    #       add to list
    #   after going through all columns in arr2
def solution(arr1, arr2):
    answer = [[]]
    return answer