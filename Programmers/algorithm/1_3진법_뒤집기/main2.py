def solution(n):
    answer = 0

    # get ternary representation of decimal
    ternary = get_ternary(n)
    # flip number
    # convert back to decimal
    answer = get_decimal(ternary[::-1])
    return answer

def get_ternary(n):
    res = ''

    while n != 0:
        r = n % 3
        res = str(r) + res
        n = n // 3

    return res

def get_decimal(ternary):
    res = 0
    i = 0
    n = len(ternary) - 1

    while i <= n:
        res += int(ternary[i]) * 3**(n-i)
        i += 1

    return res

if __name__ == "__main__":
    print(solution(45))
    print(solution(125))