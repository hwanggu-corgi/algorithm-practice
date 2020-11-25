# Goal: 고이는 빗물의 총량을 출력하여라.
# - 비가 오면 블록 사이에 빗물이 고인다
# - 2차원 세계에서는 한 칸의 용량은 1이다
# - 빗물이 전혀 고이지 않을 경우 0을 출력하여라

# 입력
# - 첫 번째 줄 - 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이
# - 두 번째 줄 - 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다
# - 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

def main():
    # parse input
    dimensions = [int(x) for x in input().split()]
    wall_heights = [int(x) for x in input().split()]

    WIDTH = dimensions[0]
    HEIGHT = dimensions[1]
    total_water_blocks = 0

    # Find left wall. Store it's index in left_wall_position
    i_left_wall = get_left_wall(wall_heights, WIDTH)
    i_right_wall = i_left_wall

    # For each wall_height (가로)
    while i_left_wall < (WIDTH-1):
        j = 0
        while j < HEIGHT:
            # Find right wall at hight j. Store it's index in right_wall_position
            i_right_wall = get_right_wall(wall_heights, i_right_wall, j, WIDTH)
            if (i_right_wall < 0):
                break

            if not water_can_be_filled_at_this_height(j, i_left_wall, i_right_wall, wall_heights):
                break

            print("I am here")
            # Calculate blocks of water at height h betwen left_wall_position and right_wall_position
            water_blocks = calculate_water_blocks(i_left_wall, i_right_wall)

            # Add to total
            total_water_blocks += water_blocks

            # Update height
            j += 1
        # Update index
        if i_right_wall < 0:
            break

        i_left_wall = i_right_wall

    return total_water_blocks

def get_left_wall(wall_heights, width):
    i = 0
    while i < width:
        if wall_heights[i] > 0:
            return i
        i += 1

    return -1

def get_right_wall(wall_heights, index_right_wall, current_height, width):
    i = index_right_wall
    j = current_height
    while i < width:
        if j < wall_heights[i]:
            return i
        i += 1

    return -1

def water_can_be_filled_at_this_height(current_height, index_left_wall, index_right_wall, wall_heights):
    left_wall_height = wall_heights[index_left_wall]
    right_wall_height = wall_heights[index_right_wall]

    if ((current_height <= left_wall_height) and
        (current_height <= right_wall_height)):

        return True

    return False

def calculate_water_blocks(index_left_wall, index_right_wall):
    return index_right_wall - index_left_wall - 1


if __name__ == "__main__":
    print(main())