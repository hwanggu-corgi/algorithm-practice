# goal: 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록
# solution 함수를 완성해 주세요.

# 제한사항
#   - n은 500,000,000이하의 자연수 입니다.

# brute force method
#   - count
#       - on every 3rd number increment value right after
    #       - if the value after is 4, then append value of 1 after and reset prev count to 1
#   but is crazy inefficient

# Improved method
#   1. 3진법
#       - 1 -> 1 -> 1
#       - 2 -> 2 -> 2
#       - 3 -> 10 -> 4
#       - 4 -> 11 -> 11
#       - 5 -> 12 -> 12
#       - 6 -> 20 -> 14
#       - 7 -> 21 -> 21
#       - 8 -> 22 -> 22
#       - 9 -> 100 -> 24
#       - 10 -> 101 -> 41
#       - 11 -> 102 -> 42
#       - 12 -> 110 -> 44
#       - 13 -> 111 -> 111
#       - 14 -> 112 -> 112
#       - 15 -> 120 -> 114
#       - 16 -> 121 -> 121
#       - 17 -> 122 -> 122
#       - 18 -> 200 -> 124  - first 0 from right becomes 4,
#       - 18 -> 201 -> 141 - 0 becomes 4 and number after gets subtracted by 1

#   1. 2진법
#       - 1 -> 1 -> 1
#       - 2 -> 10 -> 2
#       - 3 -> 11 -> 4
#       - 4 -> 100 -> 4
#       - 5 -> 11 -> 4
#       - 6 -> 11 -> 4
#       - 7 -> 11 -> 4
# ...
#       - 10 -> 1010 -> 41
#       - 11 -> 1011 -> 42
#       - 12 -> 1100 -> 44
#       - 13 -> 1101 -> 111

def solution(n):
    ternary_number = convert_from_decimal_to_ternary(n)
    strange_number = convert_from_ternary_to_strange(ternary_number)

    answer = strange_number
    return answer

def convert_from_decimal_to_ternary(n):
    ternary_number = ''
    quotient = n

    while quotient != 0:
        remainder = quotient % 3
        quotient = quotient // 3

        ternary_number += str(remainder) + ternary_number

    return ternary_number

def convert_from_ternary_to_strange(ternary_number):
    ternary_number_list = ternary_number.split()

    i = 1
    while i < N:

        i += 1

    return strange_number