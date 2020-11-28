# goal: 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열
# hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된
# 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
#
#   - 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
#   - 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
#   - 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
#   - 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#       - 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 제한사항
#   - numbers 배열의 크기는 1 이상 1,000 이하입니다.
#   - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
#   - hand는 "left" 또는 "right" 입니다.
#   - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
#   - 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

def solution(numbers, hand):
    answer = ''

    # for each number
    for number in numbers:
        # find which thumb is pressed for the number
        hand_used = get_pressed_hand(left_position, right_position, number_position)
        # update current hand position
        if hand_used == "L":
            left_position = ...
        else:
            right_position = ...

        # concat to answer
        answer += hand_used

    # return answer
    return answer