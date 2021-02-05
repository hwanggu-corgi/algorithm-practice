# goal: 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로
# 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   n은 1 이상 100,000,000 이하인 자연수입니다.

def solution(n):
    answer = 0

    # convert to ternary
    ternary = get_ternary(n)

    # flip number
    # convert reversed ternary to decimal
    answer = get_decimal(ternary[::-1])

    # return answer
    return answer

def get_ternary(n):
    answer = ''

    while n > 0:
        remainder = n % 3
        n = n // 3

        answer = str(remainder) + answer

    return answer

def get_decimal(ternary):
    answer = 0

    n = len(ternary)
    i = n - 1

    while i >= 0:
        answer += int(ternary[i]) * 3**((n - 1) - i)
        i -= 1

    return answer

if __name__ == "__main__":
    print(solution(45))
    print(solution(125))