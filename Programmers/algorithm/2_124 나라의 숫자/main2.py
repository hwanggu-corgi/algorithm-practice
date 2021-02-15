# goal: 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록
# solution 함수를 완성해 주세요.

# 제한사항
#   n은 500,000,000이하의 자연수 입니다.


# dec - 1       1         [1*, 2, 4]
# dec - 2       2         [1, 2*, 4]
# dec - 3       4         [1, 2, 4*]
# dec - 4       11        [1**, 2, 4]
# dec - 5       12        [1*, 2*, 4]
# dec - 6       14        [1*, 2, 4*]
# dec - 7       21        [1*, 2*, 4]
# dec - 8       21        [1*, 2*, 4]
# dec - 9       24        [1, 2*, 4*]


# 4 - 1 = 3 / 3 = 1 r 0
# 5 - 1 = 4 / 3 = 1 r 1
# 6 - 1 = 5 / 3 = 1 r 2

def solution(n):
    num  = ["1", "2", "4"]
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n = n // 3

    return answer

if __name__ == "__main__":
    print(solution(1)) # 1
    print(solution(2)) # 2
    print(solution(4)) # 4
    print(solution(5)) # 11
    print(solution(10)) # 41