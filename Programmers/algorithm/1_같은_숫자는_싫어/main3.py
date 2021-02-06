# goal: 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
#   배열 arr의 크기 : 1,000,000 이하의 자연수
#   배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

def solution(arr):
    answer = []
    current_number = -1

    for i in arr:
        if i != current_number:
            answer.append(i)
            current_number = i
    return answer


if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1])) #