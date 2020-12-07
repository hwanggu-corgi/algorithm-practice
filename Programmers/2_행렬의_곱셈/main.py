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
    #       add to list new_row
    #   append new_row to answer
def solution(arr1, arr2):
    answer = []
    n_row_arr1 = len(arr1)
    n_col_arr1 = len(arr1[0])

    n_row_arr2 = len(arr2)
    n_col_arr2 = len(arr2[0])

    #   for each row in arr1 (i),
    for i in range(n_row_arr1):
        #   for each column in arr2 (j),
        new_row = []
        for j in range(n_col_arr2):
            new_value = 0
            #   calculate element after matrix multiplication
            #   for each column in arr1 (m),
            for m in range(n_col_arr1):
                #   compute sum of A[i][m]B[m][j] for all m
                new_value = arr1[i][m] * arr2[m][j]
            #   add to list new_row
            new_row.append(new_value)
        #   append new_row to answer
        answer.append(new_row)
    return answer

if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]