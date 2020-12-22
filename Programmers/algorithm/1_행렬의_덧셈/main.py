# goal:  2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

def solution(arr1, arr2):
    return [[sum(y) for y in zip (*x)] for x in zip(arr1, arr2)]

if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]])) #	[[4,6],[7,9]]
    print(solution([[1],[2]], [[3],[4]])) #	[[4,6],[7,9]]