# Goal: 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.
#   - 첫 줄 - 기둥의 개수 N
#       - N은 1 이상 1,000 이하이다
#   - N 개의 줄 - 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H
#       - L과 H는 둘 다 1 이상 1,000 이하이다.

def main():
    # get input
    columns_list = []
    total_blocks = 0
    N = int(input())


    for i in range(N):
        column = [int(x) for x in input().split()]
        columns_list.append(column)

    # sort columns by position on x-axis
    columns_list.sort(key= lambda c: c[0])

    # get height
    HEIGHT = max(columns_list, key= lambda e: e[1])[1]
    print("Height {}".format(HEIGHT))
    # starting at height h at position x, find the furthest located, valid column
    # for each column in array
    j = 0
    while j < HEIGHT:
        # at height j, find the furthest located two columns
        index_left_column = get_left_column(j, columns_list, N)
        index_right_column = get_right_column(j, columns_list, N)
        print("Index Left Column: {}".format(index_left_column))
        print("Index Right Column: {}".format(index_right_column))
        # calculate number of blocks between them
        blocks = calculate_blocks_between_columns(index_left_column, index_right_column)
        print("Blocks: {}".format(blocks))
        print("==============")
        # add to total
        total_blocks += blocks

        j += 1

    return total_blocks

def get_left_column(current_height, columns_list, N):
    i = 0
    while i < N:
        if current_height <= columns_list[i][1]:
            return columns_list[i][0]

        i += 1


def get_right_column(current_height, columns_list, N):
    i = N - 1
    while i >= 0:
        if current_height <= columns_list[i][1]:
            return columns_list[i][0]

        i -= 1


def calculate_blocks_between_columns(index_left_column, index_right_column):
    return (index_right_column - index_left_column) + 1

if __name__ == "__main__":
    print(main())