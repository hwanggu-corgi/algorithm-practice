# goal: Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# - 중앙에는 노란색으로 칠해져 있고
# - 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# 제한사항
#   - 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
#   - 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
#   - 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

# Example
#   1) brown: 10    yellow: 2
#       - 12 x 1 - not possible
#       - 6 x 2 - not possible
#       - 4 x 3 - (4 x 3) - (4 + 4 + 3 + 3 - 4) = 2 (yes there is room fow yellow tile) --> possible
#   result [4,3]

#   2) brown: 8     yellow: 1
#       - 4 x 2 - (4 x 2) - (4 + 4 + 2 + 2 - 4) = 0 (no room for brown tiles) --> not possible
#       - 3 x 3 - (3 x 3) - (3 + 3 + 3 + 3 - 4) = 1 (yes there is room fow yellow tile) --> possible

# Pseudocode
#   calculate total squares, and store in total_squares
#   for number from 2,
#   check if number divides total_squares
#

def solution(brown, yellow):
    answer = []
    return answer