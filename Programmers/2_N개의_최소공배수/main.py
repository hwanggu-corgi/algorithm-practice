# goal: n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항
#   - arr은 길이 1이상, 15이하인 배열입니다.
#   - arr의 원소는 100 이하인 자연수입니다.

# Example
#   1) [2,6,8,14]

# Pseudocode
#   - Find maximum in array, store in max_num
#   - in multiples of max_num, check if all divides the number
#   - if yes, return number
#   - if not keep going


def solution(arr):
    lcm_found = False
    # Find maximum in array, store in max_e
    max_e = max(arr)

    # in multiples of max_e, check if all divides the number
    i = 1
    while not lcm_found:
        number = max_e * i
        # if yes, return number
        if is_lcm(arr, number):
            lcm_found = True
        # if not keep going
        i += 1
    answer = number
    return answer

def is_lcm(arr, max_e):

    for number in arr:
        if max_e % number != 0:
            return False

    return True

if __name__ == "__main__":
    print(solution([2,6,8,14])) #168
    print(solution([1,2,3])) #6