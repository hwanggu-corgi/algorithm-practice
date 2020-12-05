# goal: 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을
# return 하도록 solution 함수를 만드세요

# 제한 사항
#   - name은 알파벳 대문자로만 이루어져 있습니다.
#   - name의 길이는 1 이상 20 이하입니다.

# Example
#   - JAZ --> 56
#       - [9]: 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
#       - [10]: 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
#       - [11]: 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
#           - 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
#   - JAN --> 23
#       - [9]: 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
#       - [10]: 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
#       - [23]: 마지막 위치에서 조이스틱을 아래로 13번 조작하여 N를 완성합니다.
#           - 따라서 23번 이동시켜 "JAN"를 만들 수 있고, 이때가 최소 이동입니다.

# pattern
#   - Always choose directions closest to current cursor

# Detail
#   - JAZ
#       1. AAA -> Check distance between A and J (9 by up 17 by down) --> choose up by 9 --> add to total (9)
#          ^
#          JAZ
#          *
#       2. JAA
#          ^
#          JAZ
#          *
#       3. JAA -> Next is A --> skip
#          ^
#          JAZ
#           *
#       4. JAA -> Next is Z --> Calculate  distance between left and right cursur (2 by right, 1 by left) --> move left by 1 --> add tototal (10)
#          ^
#          JAZ
#            *
#       5. JAA ->Check distance between A and Z (25 by up 1 by down) --> choose down by 1 --> add to total (11)
#            ^
#          JAZ
#            *
#       6. JAZ
#            ^
#          JAZ
#            *

# cases
#   Vertical
#       1. if the current letter and target letter are the same
#       2. if the current letter and target letter are not the same
#           2.1 if is closer moving up
#           2.2 if is closer moving down
#   Horizontal
#       1. if closer by moving left
#       1. if closer by moving right

def solution(name):
    answer = 0
    my_index = 0

    for i, letter in enumerate(name):
        if letter == "A":
            continue

        total_moves += move_vertical(name)

        if i < N:
            total_moves += move_horizontal(i, my_index)
            my_index = i


    return answer