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
#           [CCBDE,
#            --ABF,
#            --ADE,
#            CCBBF]

#                    |B| |D| |E|
#                    |A| |D| |E|
#            |C| |C| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


#   5)
#           [CCBDE, --> Remove 1 and 2 of 2nd queue
#            --ABF,
#            --ADE,
#            CCBBF]

#                    |B| |D| |E|
#                    |A| |D| |E|
#            |C| |C| |A| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   6)
#           [CCBDE,
#            ---BF,
#            ---DE,
#            CCBBF]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue

#   6)
#           [CCBDE, --> regenerate matrix using queue
#            ---BF,
#            ---DE,
#            CCBBF]

#                        |D| |E|
#                        |D| |E|
#            |C| |C| |B| |B| |F|
#            |C| |C| |B| |B| |F|  < - head of queue


# Pseudocode
#   - Create a copy of board using list of queues where each queue represents column
#   - find removable tiles using board
#   -

def solution(m, n, board):
    answer = 0
    return answer