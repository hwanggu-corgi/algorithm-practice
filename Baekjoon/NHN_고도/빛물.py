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

    HEIGHT = dimensions[0]
    WIDTH = dimensions[1]
    total_water_blocks = 0

    j = 0

    # For each wall_height (가로)
    while j < HEIGHT:
        current_height = j + 1
        i_a = get_index_left_wall(wall_heights, current_height, WIDTH)
        i_b = i_a + 1

        while i_a < WIDTH:
            if is_a_wall(i_b, wall_heights, current_height, WIDTH):
                water_blocks = calculate_water_blocks(i_a, i_b, WIDTH)
                total_water_blocks += water_blocks
                i_a = i_b
            i_b += 1

        j += 1

    return total_water_blocks

def get_index_left_wall(wall_heights, current_height, width):
    i = 0
    while i < width:
        if current_height <= wall_heights[i]:
            break
        i += 1

    return i

def is_a_wall(index_width, wall_heights, current_height, width):
    if index_width >= width:
        return True

    if current_height <= wall_heights[index_width]:
        return True

    return False


def calculate_water_blocks(index_left, index_right, width):
    if index_right >= width:
        return 0

    return index_right - index_left - 1


if __name__ == "__main__":
    print(main())