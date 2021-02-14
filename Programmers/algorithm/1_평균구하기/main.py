# goal 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def solution(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    print(solution([1,2,3,4])) #2.5
    print(solution([5,5])) #5