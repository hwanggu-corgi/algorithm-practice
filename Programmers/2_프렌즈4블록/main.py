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
#      [CCBDE,
#       AAADE,
#       AAABF,
#       CCBBF]

def solution(m, n, board):
    answer = 0
    return answer