# goal: 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 1이 될 때까지 계속해서 s에 이진
# 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return
# 하도록 solution 함수를 완성해주세요.
#
# 제한사항
#   - s의 길이는 1 이상 150,000 이하입니다.
#   - s에는 '1'이 최소 하나 이상 포함되어 있습니다.

# Example
#   1) "01110"
#       - "01110" --> erase 0 (2) ("111") --> get length (4) --> convert to binary ("100")
#       - "100" --> erase 0 ("1") --> get length (1) --> convert to binary ("1")

def solution(s):
    answer = []

    while len(s) > 1:

    return answer