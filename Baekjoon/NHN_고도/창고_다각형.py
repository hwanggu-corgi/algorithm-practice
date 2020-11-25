# Goal: 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.
#   - 첫 줄 - 기둥의 개수 N
#       - N은 1 이상 1,000 이하이다
#   - N 개의 줄 - 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H
#       - L과 H는 둘 다 1 이상 1,000 이하이다.

def main():
    # get input
    columns_list = []
    N = int(input())


    for i in range(N):
        column = [int(x) for x in input().split()]
        columns_list.add(column)

    # sort columns by position on x-axis
    columns.sort(key= lambda c: c[0])

    # starting at height h at position x, find the furthest located, valid column
    # for each column in array
    while j < HEIGHT:
        # at height j, find the furthest located two columns
        while ...:
            # evaluate number of blocks between two columns (including columns)

            # add to area

            # move height by 1
            height += 1



if __name__ == "__main__":
    print(main())