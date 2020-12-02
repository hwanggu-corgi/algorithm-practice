# goal: 가로의 길이 W와 세로의 길이 H가 주어질 때, 사용할 수 있는 정사각형의 개수를 구하는 solution
# 함수를 완성해 주세요.

# 제한사항
#   - W, H : 1억 이하의 자연수

# idea
#   - Moe having trouble finding how to get the squares in a diagonal;;;

def solution(w,h):
    answer = 1

    # if it's a square
    if w == h:
        return w # or h

    # if it's not a square
    number_of_squares_in_a_diagonal = get_number_of_squares_in_a_diagonal(...)

    answer = number_of_squares_in_a_diagonal
    return answer