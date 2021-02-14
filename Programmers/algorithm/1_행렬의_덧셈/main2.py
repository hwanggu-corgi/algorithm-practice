# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

def solution(arr1, arr2):
    n_outer = len(arr1)
    n_inner = len(arr1[0])
    answer = []
    for i in range(n_outer):
        item = []
        for j in range(n_inner):
            res = (arr1[i][j] + arr2[i][j])
            item.append(res)
        answer.append(item)

    return answer

if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]])) #[[4,6],[7,9]]