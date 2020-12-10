# goal: 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

# 입력 형식
#   - 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
#   - 2 ≦ n, m ≦ 30
#   - board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

# Example
#   1) [CCBDE,
#       AAADE,
#       AAABF,
#       CCBBF]
#
#           [CCBDE,  --> [1,0] and [1,1] has deletable tiles
#            AAADE,
#            AAABF,
#            CCBBF]

#           [---DE,  --> [2,0] and [2,2] has deletable tiles
#            --BDE,
#            CCBBF,
#            CCBBF]

#           [----E,  --> [2,0] and [2,2] has deletable tiles
#            ----E,
#            ---DF,
#            --BDF]


#           Total 14 tiles have been removed


#   0)
#           [CCBBF,  -->  Flip tiles
#            AAABF,
#            AAADE,
#            CCBDE]
#
#   1)
#           [CCBBF,  -->  [1,0] and [1,1] has removable tiles
#            AAABF,
#            AAADE,
#            CCBDE]

#            |C| |C| |B| |D| |E|
#            |A| |A| |A| |D| |E|
#            |A| |A| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


#   2)
#           [CCBBF,  --> Remove 1 and 2 of 0th queue
#            -AABF,
#            -AADE,
#            CCBDE]

#                |C| |B| |D| |E|
#                |A| |A| |D| |E|
#            |C| |A| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   3)
#           [CCBBF, --> Remove 1 and 2 of 1st queue
#            -AABF,
#            -AADE,
#            CCBDE]

#                |C| |B| |D| |E|
#                |A| |A| |D| |E|
#            |C| |A| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   4)
#           [CCBBF,
#            --ABF,
#            --ADE,
#            CCBDE]

#                    |B| |D| |E|
#                    |A| |D| |E|
#            |C| |C| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


#   5)
#           [CCBBF, --> Remove 1 and 2 of 2nd queue
#            --ABF,
#            --ADE,
#            CCBDE]

#                    |B| |D| |E|
#                    |A| |D| |E|
#            |C| |C| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   6)
#           [CCBBF,
#            ---BF,
#            ---DE,
#            CCBDE]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   6)
#           [CCBBF, --> regenerate matrix using queue
#            ---BF,
#            ---DE,
#            CCBDE]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   7)
#           [CCBBF,
#            CCBBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


#   8)
#           [CCBBF, --> search --> [0,0] and [0,2] has removable tiles
#            CCBBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


#   9)
#           [CCBBF, --> Remove 0 and 1 of 0th queue
#            CCBBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   10)
#           [-CBBF,
#            -CBBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                |C| |B| |B| |F|
#             *  |C| |B| |B| |F|  < - head of queue

#   11)
#           [-CBBF, --> Remove 0 and 1 of 1st queue
#            -CBBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                |C| |B| |B| |F|
#             *  |C| |B| |B| |F|  < - head of queue



#   12)
#           [--BBF,
#            --BBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                    |B| |B| |F|
#             *   *  |B| |B| |F|  < - head of queue

#   13)
#           [--BBF, --> Remove 0 and 1 of 2nd queue
#            --BBF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                    |B| |B| |F|
#             *   *  |B| |B| |F|  < - head of queue


#   14)
#           [---BF,
#            ---BF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                        |B| |F|
#             *   *   *  |B| |F|  < - head of queue


#   15)
#           [---BF, --> Remove 0 and 1 of 3rd queue
#            ---BF,
#            ---DE,
#            ---DE]

#                        |D| |E|
#                        |D| |E|
#                        |B| |F|
#             *   *   *  |B| |F|  < - head of queue


#   16)
#           [----F,
#            ----F,
#            ---DE,
#            ---DE]

#                            |E|
#                            |E|
#                        |D| |F|
#             *   *   *  |D| |F|  < - head of queue

#   16)
#           [----F, --> regenerate matrix using queue
#            ----F,
#            ---DE,
#            ---DE]

#                            |E|
#                            |E|
#                        |D| |F|
#             *   *   *  |D| |F|  < - head of queue


#   17)
#           [---DF, --> regenerate matrix using queue
#            ---DF,
#            ----E,
#            ----E]

#                            |E|
#                            |E|
#                        |D| |F|
#             *   *   *  |D| |F|  < - head of queue

#   18)
#           [---DF, --> search --> none
#            ---DF,
#            ----E,
#            ----E]

#                            |E|
#                            |E|
#                        |D| |F|
#             *   *   *  |D| |F|  < - head of queue


#   18)
#           [---DF, count number removed --> 14 --> return value
#            ---DF,
#            ----E,
#            ----E]

#                            |E|
#                            |E|
#                        |D| |F|
#             *   *   *  |D| |F|  < - head of queue



# Pseudocode
#   Create a copy of board using list of queues where each queue represents column
#   while True
#       find removable tiles using board
#           place coordinates in to_be_removed
#       if none found, break
#       else, for each item in to_be_removed, remove item in queue
#       refresh board using queue
#   -

from collections import deque

def solution(m, n, board):
    answer = 0
    to_be_removed = []

    # Flip board
    board = board[::-1]

    # create 2d board
    board = [[y for y in x] for x in board]

    # Create a copy of board using list of queues where each queue represents column
    board_queues = create_board_queues(board)

    # while True
    while True:
        # find removable tiles using board
        # place coordinates in to_be_removed
        to_be_removed = search_removable_tiles(board)
        print(to_be_removed)
        # if none found, break
        if len(to_be_removed) == 0:
            break

        while len(to_be_removed) > 0:
            item = to_be_removed.pop()
            queue_number = item[1]
            tile_number = item[0]


            # else, for each item in to_be_removed, remove item in queue
            if board[tile_number+1][queue_number] != "-":
                del board_queues[queue_number][tile_number+1]
                board[tile_number+1][queue_number] = "-"
            if board[tile_number][queue_number] != "-":
                del board_queues[queue_number][tile_number]
                board[tile_number][queue_number] = "-"
            if board[tile_number+1][queue_number+1] != "-":
                del board_queues[queue_number+1][tile_number+1]
                board[tile_number+1][queue_number+1] = "-"
            if board[tile_number][queue_number+1] != "-":
                del board_queues[queue_number+1][tile_number]
                board[tile_number][queue_number+1] = "-"


        # refresh board using queue
        board = refresh_board(board, board_queues)

    answer = count_removed(board)

    return answer

def create_board_queues(board):
    board_queues = []
    N_rows = len(board)
    N_cols = len(board[0])

    for j in range(N_cols):
        col = deque()
        for i in range(N_rows):
            col.append(board[i][j])

        board_queues.append(col)

    return board_queues

def search_removable_tiles(board):
    to_be_removed = []

    N_rows = len(board)
    N_cols = len(board[0])

    for i in range(N_rows-1):
        for j in range(N_cols-1):
            if ((board[i][j] != '-') and
               (board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1])):
                to_be_removed.append([i,j])

    return to_be_removed

def refresh_board(board, board_queues):
    N_cols = len(board[0])
    N_rows = len(board)
    new_board = []

    for i in range(N_rows):
        row = []
        for j in range(N_cols):
            try:
                row.append(board_queues[j][i])
            except IndexError:
                row.append("-")

        new_board.append(row)
    return new_board

def count_removed(board):
    N_rows = len(board)
    N_cols = len(board[0])
    count = 0
    for i in range(N_rows):
        for j in range(N_cols):
            if board[i][j] == "-":
                count += 1

    return count
if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) #14

