# goal: 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 1이 될 때까지 계속해서 s에 이진
# 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return
# 하도록 solution 함수를 완성해주세요.
#
# 제한사항
#   - s의 길이는 1 이상 150,000 이하입니다.
#   - s에는 '1'이 최소 하나 이상 포함되어 있습니다.

# Example
#   1) "01110"
#       - "01110" --> erase 0 (2) ("111") --> get length (3) --> convert to binary ("11")
#       - "11" --> erase 0 (0)("11") --> get length (2) --> convert to binary ("10")
#       - "10" --> erase 0 (1)("1") --> get length (1) --> convert to binary ("1")

# Pseudocode
#   while length of s is greater than 1,
#   remove 0s, and add count to zeros_removed
#   get length
#   convert to binary, and add count to converted_count

def solution(s):
    answer = []
    zeros_removed = 0
    converted_count = 0
    while len(s) > 1:
        s, removed_count = remove_zeros(s)
        zeros_removed += removed_count

        s_length = len(s)
        s = convert_decimal_to_binary(s_length)
        converted_count += 1

    return answer

def remove_zeros(s):
    res = ""
    for bit in s:
        if bit == "1":
            res += 1

    return res

def convert_decimal_to_binary(number):
    binary = ""
    while number != 0:
        remainder = number % 2
        binary = remainder + binary
        number = number // 2

    return binary

if __name__ == "__main__":
    print(solution("01110")) # [3,3]