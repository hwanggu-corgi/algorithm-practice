# goal: 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지
# 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - n은 1 이상 1,000 이하입니다.

# Example
#   - n = 4
#   1) traverse left side of triangle and fill values
#   [1,2,0,3,0,0,4,0,0,0], i = 6
#                ^

#   2) traverse bottom side of triangle and fill values
#   [1,2,0,3,0,0,4,5,6,7], i = 9
#                      ^

#   3) traverse bottom side of triangle and fill values
#   [1,2,0,3,0,0,4,5,6,7], i = 9
#                      ^

#   4) traverse right side of triangle and fill values
#   [1,2,9,3,0,8,4,5,6,7], i = 2
#        ^

#   5) check if smaller triangle exists
#   [1,2,9,3,0,8,4,5,6,7], i = 4
#            ^

# Pseudocode
#   1) find size of array (sigma of i from 1 to n)
#   2) create array
#   3) traverse left side of triangle and fill values
#   4) traverse bottom side of triangle and fill values
#   5) traverse right side of triangle and fill values
#   6) check if smaller triangle exists
#   7) if exists, find the starting point of the smaller triangle
#       7.1) repeat step 1) to 6) until no more inner, smaller triangle is found

def solution(n):
    list_size = calculate_list_size(n)
    answer = [0] * list_size

    if n == 1:
        return [1]

    i = 0
    current_value = 0
    layer = 0
    while n > 0:
        i = get_starting_index(answer, i)
        current_value += 1
        i, current_value = traverse_left(answer, i, current_value, layer, n)
        i, current_value = traverse_bottom(answer, i, current_value, n)
        i, current_value = traverse_right(answer, i, current_value, layer, n)
        layer += 1
        n -= 3

    return answer

def calculate_list_size(n):
    size = 0
    i = 0
    while i < n:
        size += (i+1)
        i += 1

    return size

def get_starting_index(answer, i):
    list_size = len(answer)
    while i < list_size:
        if answer[i] == 0:
            break
        i += 1
    return i

def traverse_left(answer, i, current_value, layer, n):
    steps = 0
    depth = 0

    if n == 1:
        answer[i] = current_value
        return i, current_value

    while depth < n:
        answer[i] = current_value

        if depth == (n-1):
            break

        steps += 1
        i += steps + (2 * layer)
        depth += 1
        current_value += 1

    return i, current_value


def traverse_bottom(answer, i, current_value, n):
    to_be_filled = (n - 1)
    while to_be_filled > 0:
        i += 1
        current_value += 1

        answer[i] = current_value

        to_be_filled -= 1

    return i, current_value

def traverse_right(answer, i, current_value, layer, n):
    steps = n
    to_be_filled = (n - 2)

    while to_be_filled > 0:
        i -= steps + (2 * layer)
        steps -= 1
        current_value += 1

        answer[i] = current_value

        to_be_filled -= 1

    return i, current_value

if __name__ == "__main__":
    print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
    print(solution(1)) # [1]
    print(solution(2)) # [1,2,3]
    print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]