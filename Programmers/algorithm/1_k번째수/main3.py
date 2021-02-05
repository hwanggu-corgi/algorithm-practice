# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의
# 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   array의 길이는 1 이상 100 이하입니다.
#   array의 각 원소는 1 이상 100 이하입니다.
#   commands의 길이는 1 이상 50 이하입니다.
#   commands의 각 원소는 길이가 3입니다.

def solution(array, commands):
    answer = []

    for i,j,k in commands:
        sub_arr = sorted(array[i-1:j])
        answer.append(sub_arr[k-1])

    return answer

if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]