# goal: 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지
# 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - n은 1 이상 1,000 이하입니다.

# Example
#   - n = 4
#   1) traverse left side of triangle and fill values
#   [1,2,0,3,0,0,4,0,0,0], current_index = 6
#                ^

#   2) traverse bottom side of triangle and fill values
#   [1,2,0,3,0,0,4,5,6,7], current_index = 9
#                      ^

#   3) traverse bottom side of triangle and fill values
#   [1,2,0,3,0,0,4,5,6,7], current_index = 9
#                      ^

#   4) traverse right side of triangle and fill values
#   [1,2,9,3,0,8,4,5,6,7], current_index = 2
#        ^

#   5) check if smaller triangle exists
#   [1,2,9,3,0,8,4,5,6,7], current_index = 4
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
    answer = []

    while n > 0:
        traverse_left(...)
        traverse_bottom(...)
        traverse_right(...)

        n -= 3
    return answer