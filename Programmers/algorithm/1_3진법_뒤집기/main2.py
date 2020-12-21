def solution(n):
    answer = 0

    # get ternary representation of decimal
    ternary = get_ternary(n)
    # flip number
    # convert back to decimal
    answer = get_decimal(ternary[::-1])
    return answer