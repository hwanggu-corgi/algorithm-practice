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
    world_dimensions = [int(x) for x in input().split()]
    wall_heights = [int(x) for x in input().split()]

    W = world_dimensions[0]
    H = world_dimensions[1]

    total_water_blocks = 0

    # Find left wall. Store it's index in left_wall_position
    left_wall_position = find_left_wall(...)

    # For each wall_height (가로)
    while left_wall_position < W:
        j = 0

        # Find right wall at hight h. Store it's index in right_wall_position
        right_wall_position = find_right_wall(..., j)

        while j < H:
            # Calculate blocks of water at height h betwen left_wall_position and right_wall_position
            water_blocks = calculate_water_blocks(...)

            # Add to total
            total_water_blocks += water_blocks

            # Check if index of left_wall should be updated. If so, move left wall to right position
            if (left_wall_should_be_updated(...)):
                left_wall_position = right_wall_position


if __name__ == "__main__":
    main()